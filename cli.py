"""JobOS CLI -- command-line interface for all features."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import click
from rich.console import Console
from rich.table import Table

console = Console()


@click.group()
def cli():
    """JobOS - AI 求职全能工具"""
    pass


@cli.command()
@click.option("--keyword", "-k", default="AI Agent", help="搜索关键词")
@click.option("--location", "-l", default="武汉", help="目标城市")
def search(keyword, location):
    """搜索岗位（使用默认平台）"""
    from crawlers.aggregator import collect_all_jobs
    jobs = collect_all_jobs(keyword, location)
    console.print(f"[green]采集到 {len(jobs)} 个岗位[/]")
    for j in jobs:
        console.print(f"  [{j['platform']}] {j['company']} | {j['title']} | {j.get('location','')} | {j.get('salary','')}")


@cli.command()
@click.option("--keyword", "-k", default="AI Agent", help="搜索关键词")
@click.option("--location", "-l", default="武汉", help="目标城市")
@click.option("--platform", "-p", multiple=True,
              type=click.Choice(["boss", "boss_drission", "nowcoder", "liepin", "curated"]),
              help="指定平台(可多选)")
@click.option("--pages", default=3, help="每个平台爬取页数")
def crawl(keyword, location, platform, pages):
    """多平台真实爬虫采集岗位"""
    from crawlers.aggregator import collect_all_jobs
    platforms = list(platform) if platform else None
    jobs = collect_all_jobs(keyword, location, platforms=platforms, max_pages=pages)

    console.print(f"\n[bold green]采集完成: {len(jobs)} 个岗位[/]")

    table = Table(title="采集结果", show_lines=True)
    table.add_column("#", style="dim", width=4)
    table.add_column("公司", style="bold")
    table.add_column("岗位")
    table.add_column("地点")
    table.add_column("薪资")
    table.add_column("类型")
    table.add_column("来源")

    for i, j in enumerate(jobs[:50], 1):
        table.add_row(
            str(i), j["company"], j["title"],
            j.get("location", ""), j.get("salary", ""),
            j.get("job_type", ""), j["platform"],
        )
    console.print(table)

    if len(jobs) > 50:
        console.print(f"[dim]... 还有 {len(jobs) - 50} 个岗位，使用 export 命令导出查看全部[/]")


@cli.command()
@click.option("--format", "-f", "fmt",
              type=click.Choice(["excel", "csv", "json", "all"]),
              default="excel", help="导出格式")
@click.option("--output", "-o", default=None, help="输出文件路径")
@click.option("--all-columns", is_flag=True, help="导出所有字段（默认只导出核心字段）")
def export(fmt, output, all_columns):
    """导出岗位数据为 Excel/CSV/JSON"""
    import db

    jobs = db.get_all_jobs_df()
    if not jobs:
        console.print("[yellow]数据库中没有岗位数据，请先运行 crawl 或 search 命令[/]")
        return

    console.print(f"[dim]共 {len(jobs)} 个岗位[/]")

    if fmt in ("excel", "all"):
        from export.excel import export_excel
        path = export_excel(jobs, output if fmt == "excel" else None,
                            include_all_columns=all_columns)
        console.print(f"[green]✓[/] Excel 导出: {path}")

    if fmt in ("csv", "all"):
        from export.csv_export import export_csv
        path = export_csv(jobs, output if fmt == "csv" else None,
                          include_all_columns=all_columns)
        console.print(f"[green]✓[/] CSV 导出: {path}")

    if fmt in ("json", "all"):
        from export.json_export import export_json
        path = export_json(jobs, output if fmt == "json" else None)
        console.print(f"[green]✓[/] JSON 导出: {path}")


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
@click.option("--platform", "-p", default=None, help="按平台过滤")
@click.option("--min-score", "-s", default=None, type=float, help="最低评分过滤")
def list_jobs(platform, min_score):
    """列出数据库中的所有岗位"""
    import db
    jobs = db.get_jobs(limit=50, platform=platform, min_score=min_score)
    if not jobs:
        console.print("[yellow]数据库中没有岗位[/]")
        return

    table = Table(title=f"岗位列表 ({len(jobs)})", show_lines=True)
    table.add_column("#", style="dim", width=4)
    table.add_column("评分", justify="right", width=6)
    table.add_column("公司", style="bold")
    table.add_column("岗位")
    table.add_column("地点")
    table.add_column("薪资")
    table.add_column("来源")

    for i, j in enumerate(jobs, 1):
        score = j.get("score") or 0
        color = "green" if score >= 0.65 else "yellow" if score >= 0.45 else "red"
        table.add_row(
            str(i), f"[{color}]{score:.2f}[/]",
            j["company"], j["title"],
            j.get("location", ""), j.get("salary", ""),
            j.get("platform", ""),
        )
    console.print(table)


if __name__ == "__main__":
    cli()
