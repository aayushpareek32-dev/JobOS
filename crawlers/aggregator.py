"""Job aggregator -- collects from all platforms and deduplicates."""

from __future__ import annotations

from crawlers.boss import search_boss_jobs
from crawlers.nowcoder import search_nowcoder_sync
import db


def collect_all_jobs(keyword: str = "AI Agent", location: str = "武汉") -> list[dict]:
    """Collect jobs from all platforms, store in DB, return list."""
    all_jobs: list[dict] = []

    boss_jobs = search_boss_jobs(keyword, location)
    all_jobs.extend(boss_jobs)

    nc_jobs = search_nowcoder_sync(keyword, location)
    all_jobs.extend(nc_jobs)

    stored = []
    for job in all_jobs:
        row_id = db.insert_job(
            platform=job["platform"],
            title=job["title"],
            company=job["company"],
            job_id=job.get("job_id", ""),
            location=job.get("location", ""),
            salary=job.get("salary", ""),
            job_type=job.get("job_type", ""),
            description=job.get("description", ""),
            requirements=job.get("requirements", ""),
            url=job.get("url", ""),
            posted_date=job.get("posted_date", ""),
        )
        if row_id:
            job["db_id"] = row_id
            stored.append(job)
        else:
            stored.append(job)

    return stored
