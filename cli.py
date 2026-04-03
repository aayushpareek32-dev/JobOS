"""JobOS CLI -- command-line interface for all features."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import click
from rich.console import Console

console = Console()


@click.group()
def cli():
    """JobOS - AI 求职全能工具"""
    pass


@cli.command()
@click.option("--keyword", "-k", default="AI Agent", help="搜索关键词")
@click.option("--location", "-l", default="武汉", help="目标城市")
def search(keyword, location):
    """搜索岗位"""
    from crawlers.aggregator import collect_all_jobs
    jobs = collect_all_jobs(keyword, location)
    console.print(f"[green]采集到 {len(jobs)} 个岗位[/]")
    for j in jobs:
        console.print(f"  [{j['platform']}] {j['company']} | {j['title']} | {j.get('location','')} | {j.get('salary','')}")


@cli.command()
@click.argument("jd_text")
def analyze(jd_text):
    """分析JD并评分"""
    import json
    from agents.analyst import analyze_jd, score_job
    jd_info = analyze_jd(jd_text)
    total, details = score_job(jd_info)
    console.print(f"[green]评分: {total}[/]")
    console.print(json.dumps(details, ensure_ascii=False, indent=2))


@cli.command()
@click.option("--keyword", "-k", default="AI Agent", help="搜索关键词")
@click.option("--location", "-l", default="武汉", help="目标城市")
@click.option("--top", "-n", default=3, help="处理前N个岗位")
def run(keyword, location, top):
    """运行完整管线"""
    from pipeline import run_pipeline
    run_pipeline(keyword, location, top)


@cli.command()
@click.option("--keyword", "-k", default="AI Agent", help="搜索关键词")
@click.option("--location", "-l", default="武汉", help="目标城市")
@click.option("--top", "-n", default=5, help="处理前N个岗位")
@click.option("--interval", "-i", default=30, help="检查间隔（分钟）")
def batch(keyword, location, top, interval):
    """批量模式 -- 适合夜间自动运行"""
    from pipeline import run_pipeline
    from apscheduler.schedulers.blocking import BlockingScheduler

    console.print(f"[bold cyan]批量模式启动[/]")
    console.print(f"关键词: {keyword} | 地点: {location} | Top-{top}")
    console.print(f"每 {interval} 分钟检查一次新岗位")

    run_pipeline(keyword, location, top)

    try:
        scheduler = BlockingScheduler()
        scheduler.add_job(
            run_pipeline, "interval", minutes=interval,
            args=[keyword, location, top],
        )
        scheduler.start()
    except ImportError:
        console.print("[yellow]APScheduler未安装，使用简单循环模式[/]")
        import time
        while True:
            time.sleep(interval * 60)
            run_pipeline(keyword, location, top)


@cli.command()
def list_jobs():
    """列出数据库中的所有岗位"""
    import db
    jobs = db.get_jobs(limit=50)
    if not jobs:
        console.print("[yellow]数据库中没有岗位[/]")
        return
    for j in jobs:
        score = j.get("score") or 0
        color = "green" if score >= 0.65 else "yellow" if score >= 0.45 else "red"
        console.print(f"  [{color}]{score:.2f}[/] | {j['company']} | {j['title']} | {j.get('location','')}")


if __name__ == "__main__":
    cli()
