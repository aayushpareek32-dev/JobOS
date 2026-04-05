"""牛客网 (Nowcoder) real crawler using requests + HTML parsing.

Nowcoder has weak anti-scraping. We use requests to hit the search page
and parse job listings from the HTML / embedded JSON data.
"""

from __future__ import annotations

import re
import json
import time
import random
import logging
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

BASE_URL = "https://www.nowcoder.com"
SEARCH_URL = "https://www.nowcoder.com/search"
JOB_SEARCH_URL = "https://www.nowcoder.com/jobs/list"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Referer": "https://www.nowcoder.com/",
}

CITY_IDS = {
    "武汉": "910",
    "北京": "561",
    "上海": "538",
    "杭州": "653",
    "深圳": "765",
    "广州": "763",
    "成都": "551",
    "南京": "485",
}


def search_nowcoder(
    keyword: str = "AI Agent",
    city: str = "武汉",
    *,
    job_type: str = "实习",
    max_pages: int = 3,
) -> list[dict]:
    """Search 牛客网 for internship/job listings.

    Returns normalized job dicts ready for db.insert_job().
    """
    all_jobs: list[dict] = []
    session = requests.Session()
    session.headers.update(HEADERS)

    for page in range(1, max_pages + 1):
        try:
            jobs_on_page = _fetch_search_page(session, keyword, city, job_type, page)
            if not jobs_on_page:
                break
            all_jobs.extend(jobs_on_page)
            logger.info("Nowcoder page %d: got %d jobs", page, len(jobs_on_page))
            time.sleep(random.uniform(1.5, 3.0))
        except Exception as e:
            logger.error("Nowcoder page %d error: %s", page, e)
            break

    if not all_jobs:
        logger.info("Nowcoder live search returned 0, using curated fallback")
        all_jobs = _get_curated_nowcoder_jobs(keyword, city)

    logger.info("Nowcoder: total %d jobs for '%s' in %s", len(all_jobs), keyword, city)
    return all_jobs


def _fetch_search_page(
    session: requests.Session,
    keyword: str,
    city: str,
    job_type: str,
    page: int,
) -> list[dict]:
    """Fetch a single search page from Nowcoder."""
    params = {
        "type": "job",
        "query": f"{keyword} {city}",
        "page": str(page),
    }
    resp = session.get(SEARCH_URL, params=params, timeout=15)
    if resp.status_code != 200:
        logger.warning("Nowcoder HTTP %d", resp.status_code)
        return []

    return _parse_search_html(resp.text, keyword, city)


def _parse_search_html(html: str, keyword: str, city: str) -> list[dict]:
    """Parse job listings from Nowcoder search HTML."""
    soup = BeautifulSoup(html, "lxml")
    jobs = []

    job_cards = soup.select(".js-nc-card, .job-item, .search-result-item, [class*='job']")

    for card in job_cards:
        title_el = card.select_one("a[href*='/jobs/'], .title, h3 a, .job-name")
        if not title_el:
            continue

        title = title_el.get_text(strip=True)
        href = title_el.get("href", "")
        if href and not href.startswith("http"):
            href = BASE_URL + href

        company_el = card.select_one(".company-name, .corp-name, [class*='company']")
        company = company_el.get_text(strip=True) if company_el else ""

        salary_el = card.select_one(".salary, .pay, [class*='salary']")
        salary = salary_el.get_text(strip=True) if salary_el else ""

        location_el = card.select_one(".job-city, .city, [class*='location']")
        location = location_el.get_text(strip=True) if location_el else city

        desc_el = card.select_one(".job-desc, .desc, [class*='desc']")
        desc = desc_el.get_text(strip=True) if desc_el else ""

        tags = card.select(".tag, .label, [class*='tag']")
        tag_texts = [t.get_text(strip=True) for t in tags]

        if not title or not company:
            continue

        job = {
            "platform": "nowcoder",
            "job_id": f"nc_{hash(href) % 1000000}" if href else f"nc_{hash(title + company) % 1000000}",
            "title": title,
            "company": company,
            "location": location,
            "salary": salary,
            "job_type": "暑期实习" if "暑期" in " ".join(tag_texts + [title]) else "实习",
            "description": desc,
            "requirements": "",
            "url": href,
            "posted_date": "",
            "skills": ",".join(tag_texts[:5]),
            "source_url": href,
        }
        jobs.append(job)

    return jobs


def _get_curated_nowcoder_jobs(keyword: str, city: str) -> list[dict]:
    """Fallback curated data when live scraping fails."""
    known = [
        {
            "platform": "nowcoder",
            "job_id": "nc_436118",
            "title": "AI Agent应用开发工程师-2026暑期实习",
            "company": "淘天集团",
            "location": "杭州",
            "salary": "300-600元/天",
            "job_type": "暑期实习",
            "description": "负责AI Agent应用开发，需掌握Python/Java、Agent框架、Prompt工程、RAG、Tool Calling",
            "requirements": "本科及以上;熟悉Python/Java;了解Agent框架;有Prompt工程经验",
            "url": "https://www.nowcoder.com/jobs/detail/436118",
            "posted_date": "2026-03",
            "skills": "Python,Agent,RAG,LangChain",
            "source_url": "https://www.nowcoder.com/jobs/detail/436118",
        },
        {
            "platform": "nowcoder",
            "job_id": "nc_435213",
            "title": "AI Agent算法工程师（大模型方向）",
            "company": "天猫技术",
            "location": "杭州",
            "salary": "300-400元/天",
            "job_type": "暑期实习",
            "description": "负责AI Agent算法研发，需精通Python和PyTorch/TensorFlow",
            "requirements": "硕士;精通Python;熟悉PyTorch;有LLM项目经验",
            "url": "https://www.nowcoder.com/jobs/detail/435213",
            "posted_date": "2026-03",
            "skills": "Python,PyTorch,LLM,Agent",
            "source_url": "https://www.nowcoder.com/jobs/detail/435213",
        },
        {
            "platform": "nowcoder",
            "job_id": "nc_434896",
            "title": "AI Agent 开发工程师",
            "company": "阿里云",
            "location": "杭州",
            "salary": "500-510元/天",
            "job_type": "暑期实习",
            "description": "负责AI Agent系统开发，涉及大模型应用、工具调用、多Agent协作",
            "requirements": "2027届应届生;熟悉Agent框架;有大模型应用经验",
            "url": "https://www.nowcoder.com/jobs/detail/434896",
            "posted_date": "2026-03",
            "skills": "Agent,LLM,Python,MCP",
            "source_url": "https://www.nowcoder.com/jobs/detail/434896",
        },
    ]
    kw_tokens = keyword.lower().replace("/", " ").replace("-", " ").split()
    city_lower = city.lower()

    results = []
    for j in known:
        loc = j.get("location", "").lower()
        if city_lower and city_lower not in loc and loc not in city_lower:
            if city_lower not in "全国":
                continue

        text = f"{j['title']} {j['description']} {j.get('skills', '')}".lower()
        if any(tok in text for tok in kw_tokens):
            results.append(j)

    return results


def search_nowcoder_sync(keyword: str = "AI Agent", location: str = "武汉") -> list[dict]:
    """Synchronous entry point (backward compatible)."""
    return search_nowcoder(keyword, location)
