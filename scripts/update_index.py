#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重建 README.md 中的「笔记索引」「进度统计」，并同步 notes 数量徽章。

用法:
    python scripts/update_index.py            # 就地更新 README.md
    python scripts/update_index.py --dry-run  # 只打印结果，不写文件

设计要点:
- 仅依赖 Python 标准库，无需安装 PyYAML。
- 笔记元信息从每个 .md 文件的 YAML frontmatter 中读取。
- frontmatter 缺失或字段不全时不会崩，会以 "?" 占位并在结尾给出警告。
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from urllib.parse import quote

# --------------------------------------------------------------------------
# 分类目录 -> 中文题型名（顺序即 README 中索引的展示顺序）
# --------------------------------------------------------------------------
CATEGORIES: list[tuple[str, str]] = [
    ("01-array", "数组"),
    ("02-string", "字符串"),
    ("03-hash-table", "哈希表"),
    ("04-two-pointers", "双指针与滑动窗口"),
    ("05-binary-search", "二分查找"),
    ("06-linked-list", "链表"),
    ("07-stack-queue", "栈与队列"),
    ("08-monotonic-stack", "单调栈"),
    ("09-tree", "树"),
    ("10-backtracking", "回溯"),
    ("11-greedy", "贪心"),
    ("12-dynamic-programming", "动态规划"),
    ("13-graph", "图论"),
    ("14-grid", "网格图"),
    ("15-bit-manipulation", "位运算"),
    ("16-math", "数学"),
    ("17-data-structures", "常用数据结构"),
    ("18-others", "其他"),
]

DIFFICULTY_ICON = {"简单": "🟢", "中等": "🟡", "困难": "🔴"}
DIFFICULTY_ORDER = ["简单", "中等", "困难"]

INDEX_START = "<!-- INDEX:START -->"
INDEX_END = "<!-- INDEX:END -->"
STATS_START = "<!-- STATS:START -->"
STATS_END = "<!-- STATS:END -->"

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(REPO_ROOT, "README.md")


# --------------------------------------------------------------------------
# frontmatter 解析（最小实现，覆盖本项目模板用到的情况）
# --------------------------------------------------------------------------
def _strip_quotes(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
        return v[1:-1]
    return v


def _parse_inline_list(v: str) -> list[str]:
    inner = v.strip()[1:-1]
    if not inner.strip():
        return []
    return [_strip_quotes(p) for p in inner.split(",") if p.strip()]


def parse_frontmatter(path: str) -> dict:
    """读取文件头部的 YAML frontmatter，返回扁平字典。失败返回空字典。"""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError):
        return {}

    if not text.startswith("---"):
        return {}

    m = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.S)
    if not m:
        return {}

    data: dict = {}
    for raw in m.group(1).splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip() or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if val.startswith("[") and val.endswith("]"):
            data[key] = _parse_inline_list(val)
        else:
            data[key] = _strip_quotes(val)
    return data


# --------------------------------------------------------------------------
# 扫描
# --------------------------------------------------------------------------
def collect() -> tuple[list[dict], list[str]]:
    """遍历分类目录，收集所有笔记。返回 (笔记列表, 警告列表)。

    笔记列表按 (分类顺序, 题号) 排序。
    """
    order = {d: i for i, (d, _) in enumerate(CATEGORIES)}
    notes: list[dict] = []
    warnings: list[str] = []

    for cat_dir, _ in CATEGORIES:
        abs_dir = os.path.join(REPO_ROOT, cat_dir)
        if not os.path.isdir(abs_dir):
            continue
        for name in sorted(os.listdir(abs_dir)):
            if not name.endswith(".md") or name == "README.md":
                continue
            fpath = os.path.join(abs_dir, name)
            if not os.path.isfile(fpath):
                continue

            fm = parse_frontmatter(fpath)
            if not fm:
                warnings.append(f"缺少 frontmatter: {cat_dir}/{name}")
                fm = {}

            # 题号：优先 frontmatter，其次从文件名 "123-xxx.md" 推断
            num = fm.get("number", "")
            if not str(num).strip():
                guess = re.match(r"^(\d+)", name)
                num = guess.group(1) if guess else "?"
                warnings.append(f"frontmatter 缺 number，已从文件名推断: {cat_dir}/{name}")

            title = str(fm.get("title", "")).strip() or re.sub(r"^\d+[-_ ]*", "", name[:-3])

            raw_tags = fm.get("tags", [])
            if isinstance(raw_tags, str):
                tags = [t.strip() for t in raw_tags.strip("[]").split(",") if t.strip()]
            else:
                tags = [str(t).strip() for t in raw_tags if str(t).strip()]

            diff = str(fm.get("difficulty", "")).strip() or "?"
            if diff not in DIFFICULTY_ICON:
                diff = "?"

            notes.append(
                {
                    "cat": cat_dir,
                    "file": name,
                    "rel": f"{cat_dir}/{name}",
                    "num_sort": int(num) if str(num).isdigit() else 10**9,
                    "num": str(num),
                    "title": title,
                    "difficulty": diff,
                    "tags": tags,
                    "link": str(fm.get("leetcode", "")).strip(),
                    "date": str(fm.get("date", "")).strip(),
                }
            )

    notes.sort(key=lambda n: (order.get(n["cat"], 999), n["num_sort"], n["title"]))
    return notes, warnings


# --------------------------------------------------------------------------
# 渲染
# --------------------------------------------------------------------------
def render_index(notes: list[dict]) -> str:
    if not notes:
        return "_暂无笔记。_"

    blocks: list[str] = []
    for cat_dir, cn_name in CATEGORIES:
        group = [n for n in notes if n["cat"] == cat_dir]
        if not group:
            continue

        lines = [
            f"### {cn_name} <sub>`{cat_dir}`</sub>",
            "",
            "| # | 题目 | 难度 | 标签 | 原题 |",
            "| ---: | :--- | :--- | :--- | :-: |",
        ]
        for n in group:
            icon = DIFFICULTY_ICON.get(n["difficulty"], "")
            diff = f"{icon} {n['difficulty']}".strip() if icon else "?"
            tags = " · ".join(n["tags"]) if n["tags"] else "—"
            note_link = f"[{n['title']}]({quote(n['rel'])})"
            src = f"[LeetCode]({n['link']})" if n["link"] else "—"
            lines.append(f"| {n['num']} | {note_link} | {diff} | {tags} | {src} |")

        blocks.append("\n".join(lines))

    return "\n\n".join(blocks)


def render_stats(notes: list[dict]) -> str:
    lines = [
        "| 题型 | 已整理题数 |",
        "| :--- | ---: |",
    ]
    for cat_dir, cn_name in CATEGORIES:
        cnt = sum(1 for n in notes if n["cat"] == cat_dir)
        if cnt:
            lines.append(f"| {cn_name} | {cnt} |")
    lines.append(f"| **合计** | **{len(notes)}** |")

    counts = {d: sum(1 for n in notes if n["difficulty"] == d) for d in DIFFICULTY_ORDER}
    unknown = sum(1 for n in notes if n["difficulty"] == "?")
    dist = " · ".join(f"{d} {counts[d]}" for d in DIFFICULTY_ORDER)
    if unknown:
        dist += f" · 未标注 {unknown}"

    lines += ["", f"_按难度分布：{dist}_"]
    return "\n".join(lines)


def splice(text: str, start: str, end: str, body: str, label: str) -> tuple[str, bool]:
    """把 text 中 start..end 之间的内容替换为 body。返回 (新文本, 是否成功)。"""
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        print(f"  ! README 中找不到 {label} 标记，已跳过", file=sys.stderr)
        return text, False
    return pattern.sub(lambda _: f"{start}\n{body}\n{end}", text, count=1), True


# --------------------------------------------------------------------------
# 主流程
# --------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description="重建 README 的笔记索引与统计")
    ap.add_argument("--dry-run", action="store_true", help="只打印，不写入 README.md")
    args = ap.parse_args()

    if not os.path.isfile(README):
        print(f"找不到 README.md: {README}", file=sys.stderr)
        return 1

    notes, warnings = collect()
    with open(README, encoding="utf-8") as f:
        text = f.read()

    text, ok1 = splice(text, INDEX_START, INDEX_END, render_index(notes), "INDEX")
    text, ok2 = splice(text, STATS_START, STATS_END, render_stats(notes), "STATS")

    # 同步 notes 数量徽章
    text = re.sub(r"(badge/notes-)\d+(-)", rf"\g<1>{len(notes)}\g<2>", text, count=1)

    if args.dry_run:
        print("=" * 60)
        print(render_index(notes))
        print("=" * 60)
        print(render_stats(notes))
    elif ok1 or ok2:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(f"已更新 README.md（共 {len(notes)} 篇笔记）")
    else:
        print("没有可更新的内容（标记缺失）", file=sys.stderr)

    for w in warnings:
        print(f"  ! {w}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
