"""SQLite storage for jobs, companies, and application tracking."""

from __future__ import annotations

import sqlite3
import json
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent / "data" / "jobs.db"


def get_conn() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT NOT NULL,
            job_id TEXT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT,
            salary TEXT,
            job_type TEXT,
            description TEXT,
            requirements TEXT,
            url TEXT,
            posted_date TEXT,
            scraped_at TEXT DEFAULT (datetime('now')),
            score REAL,
            score_details TEXT,
            status TEXT DEFAULT 'new',
            UNIQUE(platform, job_id)
        );

        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            industry TEXT,
            size TEXT,
            location TEXT,
            description TEXT,
            rating REAL,
            pros TEXT,
            cons TEXT,
            avg_salary TEXT,
            work_life_balance TEXT,
            updated_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id INTEGER REFERENCES jobs(id),
            resume_path TEXT,
            interview_pack_path TEXT,
            applied_at TEXT,
            status TEXT DEFAULT 'pending',
            notes TEXT,
            updated_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS interview_materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id INTEGER REFERENCES jobs(id),
            skill_tree TEXT,
            study_path TEXT,
            eight_part_essay TEXT,
            mock_questions TEXT,
            real_interview_exp TEXT,
            generated_at TEXT DEFAULT (datetime('now'))
        );
    """)
    conn.commit()
    conn.close()


def insert_job(
    platform: str, title: str, company: str, *,
    job_id: str = "", location: str = "", salary: str = "",
    job_type: str = "", description: str = "", requirements: str = "",
    url: str = "", posted_date: str = "",
) -> int | None:
    conn = get_conn()
    try:
        cur = conn.execute(
            """INSERT OR IGNORE INTO jobs
               (platform, job_id, title, company, location, salary, job_type,
                description, requirements, url, posted_date)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (platform, job_id or f"{company}_{title}", title, company, location,
             salary, job_type, description, requirements, url, posted_date),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()


def update_job_score(job_db_id: int, score: float, details: dict):
    conn = get_conn()
    conn.execute(
        "UPDATE jobs SET score=?, score_details=? WHERE id=?",
        (score, json.dumps(details, ensure_ascii=False), job_db_id),
    )
    conn.commit()
    conn.close()


def get_jobs(*, min_score: float | None = None, status: str | None = None, limit: int = 100) -> list[dict]:
    conn = get_conn()
    sql = "SELECT * FROM jobs WHERE 1=1"
    params: list = []
    if min_score is not None:
        sql += " AND score >= ?"
        params.append(min_score)
    if status:
        sql += " AND status = ?"
        params.append(status)
    sql += " ORDER BY score DESC LIMIT ?"
    params.append(limit)
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_job_by_id(job_db_id: int) -> dict | None:
    conn = get_conn()
    row = conn.execute("SELECT * FROM jobs WHERE id=?", (job_db_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


init_db()
