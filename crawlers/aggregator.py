"""Job aggregator -- collects from all platforms, deduplicates, and stores."""

from __future__ import annotations

import logging
from typing import Literal

import db

logger = logging.getLogger(__name__)

Platform = Literal["boss", "boss_drission", "nowcoder", "liepin", "curated"]

DEFAULT_PLATFORMS: list[Platform] = ["boss", "nowcoder", "liepin"]


def collect_all_jobs(
    keyword: str = "AI Agent",
    location: str = "武汉",
    *,
    platforms: list[Platform] | None = None,
    max_pages: int = 3,
) -> list[dict]:
    """Collect jobs from selected platforms, store in DB, return list.

    Platform priority:
      1. boss      -- boss-cli real API (fast, no browser)
      2. boss_drission -- DrissionPage browser fallback
      3. nowcoder  -- requests + HTML parsing
      4. liepin    -- requests + HTML parsing
      5. curated   -- hardcoded fallback data (always works)
    """
    if platforms is None:
        platforms = list(DEFAULT_PLATFORMS)

    all_jobs: list[dict] = []

    for platform in platforms:
        try:
            jobs = _fetch_platform(platform, keyword, location, max_pages)
            logger.info("[%s] fetched %d jobs", platform, len(jobs))
            all_jobs.extend(jobs)
        except Exception as e:
            logger.error("[%s] failed: %s", platform, e)

    deduped = _deduplicate(all_jobs)
    logger.info("Total after dedup: %d (from %d raw)", len(deduped), len(all_jobs))

    stored = _store_jobs(deduped)
    return stored


def _fetch_platform(platform: str, keyword: str, location: str, max_pages: int) -> list[dict]:
    """Dispatch to the appropriate crawler."""
    if platform == "boss":
        from crawlers.boss_real import search_boss_real
        jobs = search_boss_real(keyword, location)
        if not jobs:
            from crawlers.boss import search_boss_jobs
            jobs = search_boss_jobs(keyword, location)
        return jobs

    elif platform == "boss_drission":
        from crawlers.boss_drission import search_boss_drission
        return search_boss_drission(keyword, location, max_pages=max_pages)

    elif platform == "nowcoder":
        from crawlers.nowcoder import search_nowcoder
        return search_nowcoder(keyword, location, max_pages=max_pages)

    elif platform == "liepin":
        from crawlers.liepin import search_liepin
        return search_liepin(keyword, location, max_pages=max_pages)

    elif platform == "curated":
        from crawlers.boss import search_boss_jobs
        return search_boss_jobs(keyword, location)

    else:
        logger.warning("Unknown platform: %s", platform)
        return []


def _deduplicate(jobs: list[dict]) -> list[dict]:
    """Remove duplicate jobs based on (company, title) or job_id."""
    seen_ids: set[str] = set()
    seen_company_title: set[str] = set()
    unique: list[dict] = []

    for job in jobs:
        jid = job.get("job_id", "")
        key_ct = f"{job.get('company', '')}|{job.get('title', '')}".lower().strip()

        if jid and jid in seen_ids:
            continue
        if key_ct in seen_company_title:
            continue

        if jid:
            seen_ids.add(jid)
        seen_company_title.add(key_ct)
        unique.append(job)

    return unique


def _store_jobs(jobs: list[dict]) -> list[dict]:
    """Store jobs in SQLite, return list with db_id attached."""
    stored = []
    for job in jobs:
        row_id = db.insert_job(
            platform=job.get("platform", "unknown"),
            title=job.get("title", ""),
            company=job.get("company", ""),
            job_id=job.get("job_id", ""),
            location=job.get("location", ""),
            salary=job.get("salary", ""),
            job_type=job.get("job_type", ""),
            description=job.get("description", ""),
            requirements=job.get("requirements", ""),
            url=job.get("url", ""),
            posted_date=job.get("posted_date", ""),
            skills=job.get("skills", ""),
            degree=job.get("degree", ""),
            experience=job.get("experience", ""),
            company_size=job.get("company_size", ""),
            company_industry=job.get("company_industry", ""),
            company_stage=job.get("company_stage", ""),
            welfare=job.get("welfare", ""),
            hr_name=job.get("hr_name", ""),
            hr_title=job.get("hr_title", ""),
            chat_url=job.get("chat_url", ""),
            full_jd=job.get("full_jd", ""),
            deadline=job.get("deadline", ""),
            source_url=job.get("source_url", ""),
        )
        if row_id:
            job["db_id"] = row_id
        stored.append(job)

    return stored
