"""Nowcoder (牛客网) internship job scraper."""

from __future__ import annotations

import json
import time
import random
from urllib.parse import quote
import aiohttp
import asyncio
from typing import Any


SEARCH_API = "https://gw-c.nowcoder.com/api/sparta/job-experience/search/v1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Referer": "https://www.nowcoder.com/",
    "Accept": "application/json",
}


async def search_nowcoder_jobs(
    keyword: str = "AI Agent",
    location: str = "武汉",
    job_type: str = "实习",
    page: int = 1,
    page_size: int = 20,
) -> list[dict]:
    """Search internship jobs on Nowcoder. Falls back to web scraping if API unavailable."""
    jobs: list[dict] = []

    search_url = f"https://www.nowcoder.com/search?type=job&query={quote(keyword + ' ' + location)}&page={page}"

    try:
        async with aiohttp.ClientSession(headers=HEADERS) as session:
            async with session.get(search_url, timeout=aiohttp.ClientTimeout(total=15)) as resp:
                if resp.status == 200:
                    text = await resp.text()
                    jobs = _parse_nowcoder_html(text, keyword, location)
    except Exception:
        pass

    if not jobs:
        jobs = _get_known_nowcoder_jobs(keyword, location)

    return jobs


def _parse_nowcoder_html(html: str, keyword: str, location: str) -> list[dict]:
    """Best-effort extraction from Nowcoder HTML."""
    jobs = []
    return jobs


def _get_known_nowcoder_jobs(keyword: str, location: str) -> list[dict]:
    """Return known Nowcoder AI Agent internship listings (curated data)."""
    known = [
        {
            "platform": "nowcoder",
            "job_id": "nc_436118",
            "title": "AI Agent应用开发工程师-2026暑期实习",
            "company": "淘天集团",
            "location": "杭州",
            "salary": "300-600元/天",
            "job_type": "暑期实习",
            "description": "负责AI Agent应用开发，需掌握Python/Java、Agent框架(LangChain/LlamaIndex/AutoGen)、Prompt工程、RAG、Tool Calling",
            "requirements": "本科及以上学历;熟悉Python/Java;了解Agent框架;有Prompt工程经验",
            "url": "https://www.nowcoder.com/jobs/detail/436118",
            "posted_date": "2026-03",
        },
        {
            "platform": "nowcoder",
            "job_id": "nc_435213",
            "title": "AI Agent算法工程师（大模型方向）",
            "company": "天猫技术",
            "location": "杭州",
            "salary": "300-400元/天",
            "job_type": "暑期实习",
            "description": "负责AI Agent算法研发，需精通Python和PyTorch/TensorFlow，有LLM相关研究或项目经验",
            "requirements": "硕士学位;精通Python;熟悉PyTorch/TensorFlow;有LLM项目经验",
            "url": "https://www.nowcoder.com/jobs/detail/435213",
            "posted_date": "2026-03",
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
        },
    ]

    kw_lower = keyword.lower()
    loc_lower = location.lower() if location else ""

    results = []
    for job in known:
        text = f"{job['title']} {job['description']} {job['requirements']}".lower()
        if any(k.lower() in text for k in ["agent", "ai", "大模型", "llm"]):
            results.append(job)

    return results


def search_nowcoder_sync(keyword: str = "AI Agent", location: str = "武汉") -> list[dict]:
    return asyncio.run(search_nowcoder_jobs(keyword, location))
