"""Boss直聘 crawler using DrissionPage (真实浏览器监听API响应).

Backup plan when boss-cli is unavailable. Requires Chrome/Chromium installed.
First run: browser will open for manual login, cookie persists afterwards.

Install: pip install DrissionPage
"""

from __future__ import annotations

import time
import random
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

CITY_CODES = {
    "武汉": "101200100", "北京": "101010100", "上海": "101020100",
    "杭州": "101210100", "深圳": "101280600", "广州": "101280100",
    "成都": "101270100", "南京": "101190100", "西安": "101110100",
}

USER_DATA_DIR = str(Path(__file__).parent.parent / "data" / ".boss_browser")


def search_boss_drission(
    keyword: str = "AI Agent",
    city: str = "武汉",
    *,
    max_pages: int = 3,
    delay_range: tuple[float, float] = (3.0, 6.0),
) -> list[dict]:
    """Search Boss直聘 by intercepting API responses in a real browser.

    Returns normalized job dicts ready for db.insert_job().
    """
    try:
        from DrissionPage import ChromiumPage, ChromiumOptions
    except ImportError:
        logger.error("DrissionPage not installed. Run: pip install DrissionPage")
        return []

    city_code = CITY_CODES.get(city, "101200100")
    url = f"https://www.zhipin.com/web/geek/job?query={keyword}&city={city_code}"

    co = ChromiumOptions()
    co.set_user_data_path(USER_DATA_DIR)
    co.set_argument("--disable-blink-features=AutomationControlled")
    co.set_argument("--no-sandbox")

    try:
        page = ChromiumPage(co)
    except Exception as e:
        logger.error("Failed to launch Chrome: %s", e)
        return []

    all_jobs: list[dict] = []

    try:
        for pg in range(1, max_pages + 1):
            page.listen.start("wapi/zpgeek/search/joblist")
            target = url if pg == 1 else f"{url}&page={pg}"
            page.get(target)

            try:
                packet = page.listen.wait(timeout=15)
            except Exception:
                logger.warning("Page %d: no API response captured", pg)
                break

            if not packet or not packet.response.body:
                logger.warning("Page %d: empty response", pg)
                break

            body = packet.response.body
            if body.get("code") != 0:
                logger.warning("Page %d: API error code %s", pg, body.get("code"))
                break

            job_list = body.get("zpData", {}).get("jobList", [])
            if not job_list:
                break

            for j in job_list:
                encrypt_boss_id = j.get("encryptBossId", "")
                security_id = j.get("securityId", "")
                chat_url = ""
                if encrypt_boss_id and security_id:
                    chat_url = f"https://www.zhipin.com/web/geek/chat?id={encrypt_boss_id}&securityId={security_id}"

                job = {
                    "platform": "boss",
                    "job_id": j.get("encryptJobId", ""),
                    "title": j.get("jobName", ""),
                    "company": j.get("brandName", ""),
                    "location": f"{j.get('cityName', '')} {j.get('areaDistrict', '')} {j.get('businessDistrict', '')}".strip(),
                    "salary": j.get("salaryDesc", ""),
                    "job_type": "实习" if "实习" in " ".join(j.get("jobLabels", [])) else "社招",
                    "description": j.get("jobName", ""),
                    "requirements": "",
                    "url": f"https://www.zhipin.com/job_detail/{j.get('encryptJobId', '')}.html",
                    "posted_date": "",
                    "skills": ",".join(j.get("skills", [])),
                    "degree": j.get("jobDegree", ""),
                    "experience": j.get("jobExperience", ""),
                    "company_size": j.get("brandScaleName", ""),
                    "company_industry": j.get("brandIndustry", ""),
                    "company_stage": j.get("brandStageName", ""),
                    "welfare": ",".join(j.get("welfareList", [])),
                    "hr_name": j.get("bossName", ""),
                    "hr_title": j.get("bossTitle", ""),
                    "chat_url": chat_url,
                    "full_jd": "",
                    "source_url": f"https://www.zhipin.com/job_detail/{j.get('encryptJobId', '')}.html",
                }
                all_jobs.append(job)

            logger.info("DrissionPage Boss: page %d got %d jobs", pg, len(job_list))

            page.listen.stop()

            if not body.get("zpData", {}).get("hasMore", False):
                break

            delay = random.uniform(*delay_range)
            time.sleep(delay)

    except Exception as e:
        logger.error("DrissionPage Boss error: %s", e)
    finally:
        try:
            page.quit()
        except Exception:
            pass

    logger.info("DrissionPage Boss: total %d jobs for '%s' in %s", len(all_jobs), keyword, city)
    return all_jobs


def fetch_job_detail(job_url: str) -> str:
    """Fetch full JD text from a job detail page."""
    try:
        from DrissionPage import ChromiumPage, ChromiumOptions
    except ImportError:
        return ""

    co = ChromiumOptions()
    co.set_user_data_path(USER_DATA_DIR)
    co.set_argument("--disable-blink-features=AutomationControlled")

    try:
        page = ChromiumPage(co)
        page.get(job_url)
        time.sleep(2)
        jd_el = page.ele("css:.job-sec-text")
        jd_text = jd_el.text if jd_el else ""
        page.quit()
        return jd_text
    except Exception as e:
        logger.error("Failed to fetch JD from %s: %s", job_url, e)
        return ""
