#!/usr/bin/env python3
"""
pool-diff.py — Diff 2022-2026 and 2026-2030 Technician question pools.

Categorizes every question as UNCHANGED, REWORDED, ANSWER_CHANGED, NEW, or REMOVED.
Outputs JSON and Markdown reports.
"""

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OLD_POOL = REPO_ROOT / "pools" / "2022-2026" / "questions.json"
NEW_POOL = REPO_ROOT / "pools" / "2026-2030" / "questions.json"
REPORT_DIR = REPO_ROOT / "reports"
REPORT_MD = REPORT_DIR / "2026-pool-audit.md"
REPORT_JSON = REPORT_DIR / "2026-pool-audit.json"

# Categories
UNCHANGED = "UNCHANGED"
REWORDED = "REWORDED"
ANSWER_CHANGED = "ANSWER_CHANGED"
NEW = "NEW"
REMOVED = "REMOVED"


def load_pool(path: Path) -> dict:
    """Load a question pool JSON file."""
    with open(path) as f:
        return json.load(f)


def index_by_id(questions: list[dict]) -> dict[str, dict]:
    """Index questions by their ID."""
    return {q["id"]: q for q in questions}


def extract_subelement(qid: str) -> str:
    """Extract subelement from question ID: T1A01 -> T1."""
    m = re.match(r"(T\d+)", qid)
    return m.group(1) if m else qid[:2]


def extract_group(qid: str) -> str:
    """Extract group from question ID: T1A01 -> T1A."""
    m = re.match(r"(T\d+[A-Z])", qid)
    return m.group(1) if m else qid[:3]


def normalize_text(text: str) -> str:
    """Normalize question text for comparison (strip refs, collapse whitespace)."""
    return re.sub(r"\s+", " ", text.strip())


def categorize_questions(
    old_idx: dict[str, dict], new_idx: dict[str, dict]
) -> dict[str, list[dict]]:
    """Categorize all questions into change categories."""
    results: dict[str, list[dict]] = {
        UNCHANGED: [],
        REWORDED: [],
        ANSWER_CHANGED: [],
        NEW: [],
        REMOVED: [],
    }

    all_ids = sorted(set(old_idx.keys()) | set(new_idx.keys()))

    for qid in all_ids:
        old_q = old_idx.get(qid)
        new_q = new_idx.get(qid)

        if old_q and not new_q:
            results[REMOVED].append({"id": qid, "old": old_q})
        elif new_q and not old_q:
            results[NEW].append({"id": qid, "new": new_q})
        else:
            # Both exist — compare
            old_text = normalize_text(old_q["question"])
            new_text = normalize_text(new_q["question"])
            old_correct = old_q["correct"]
            new_correct = new_q["correct"]

            # Check if the correct answer TEXT changed (not just the letter)
            old_answer_text = old_q["answers"].get(old_correct, "")
            new_answer_text = new_q["answers"].get(new_correct, "")

            if old_text == new_text and old_q["answers"] == new_q["answers"] and old_correct == new_correct:
                results[UNCHANGED].append({"id": qid, "old": old_q, "new": new_q})
            elif old_correct != new_correct:
                results[ANSWER_CHANGED].append({
                    "id": qid,
                    "old": old_q,
                    "new": new_q,
                    "old_correct_letter": old_correct,
                    "new_correct_letter": new_correct,
                    "old_correct_text": old_answer_text,
                    "new_correct_text": new_answer_text,
                })
            elif old_text != new_text or old_q["answers"] != new_q["answers"]:
                results[REWORDED].append({"id": qid, "old": old_q, "new": new_q})
            else:
                results[UNCHANGED].append({"id": qid, "old": old_q, "new": new_q})

    return results


def find_figure_refs(questions: list[dict]) -> set[str]:
    """Find all figure references (e.g., T-1, T-2) in question text and answers."""
    fig_pattern = re.compile(r"\bT-\d+\b")
    refs = set()
    for q in questions:
        refs.update(fig_pattern.findall(q["question"]))
        for ans in q["answers"].values():
            refs.update(fig_pattern.findall(ans))
    return refs


def subelement_stats(
    results: dict[str, list[dict]],
    old_sub_meta: dict,
    new_sub_meta: dict,
) -> dict[str, dict]:
    """Compute per-subelement statistics."""
    stats: dict[str, dict] = {}
    sub_ids = sorted(set(list(old_sub_meta.keys()) + list(new_sub_meta.keys())))

    for sub in sub_ids:
        s = {
            "old_name": old_sub_meta.get(sub, {}).get("name", "N/A"),
            "new_name": new_sub_meta.get(sub, {}).get("name", "N/A"),
            "name_changed": (
                old_sub_meta.get(sub, {}).get("name", "")
                != new_sub_meta.get(sub, {}).get("name", "")
            ),
            UNCHANGED: [],
            REWORDED: [],
            ANSWER_CHANGED: [],
            NEW: [],
            REMOVED: [],
        }
        for cat in [UNCHANGED, REWORDED, ANSWER_CHANGED]:
            for item in results[cat]:
                if extract_subelement(item["id"]) == sub:
                    s[cat].append(item)
        for item in results[NEW]:
            if extract_subelement(item["id"]) == sub:
                s[NEW].append(item)
        for item in results[REMOVED]:
            if extract_subelement(item["id"]) == sub:
                s[REMOVED].append(item)
        stats[sub] = s

    return stats


def group_stats(results: dict[str, list[dict]]) -> dict[str, dict]:
    """Compute per-group statistics."""
    all_groups: set[str] = set()
    for cat in results:
        for item in results[cat]:
            qid = item["id"]
            all_groups.add(extract_group(qid))

    stats: dict[str, dict] = {}
    for grp in sorted(all_groups):
        s = {UNCHANGED: 0, REWORDED: 0, ANSWER_CHANGED: 0, NEW: 0, REMOVED: 0}
        for cat in results:
            for item in results[cat]:
                if extract_group(item["id"]) == grp:
                    s[cat] += 1
        s["total_changes"] = s[REWORDED] + s[ANSWER_CHANGED] + s[NEW] + s[REMOVED]
        stats[grp] = s
    return stats


def generate_markdown(
    results: dict[str, list[dict]],
    sub_stats: dict[str, dict],
    grp_stats: dict[str, dict],
    old_pool: dict,
    new_pool: dict,
    old_figs: set[str],
    new_figs: set[str],
    existing_figs: list[str],
) -> str:
    """Generate the full markdown report."""
    lines: list[str] = []
    w = lines.append

    w("# 2026-2030 Technician Pool Audit Report")
    w("")
    w(f"*Generated by `scripts/pool-diff.py`*")
    w("")

    # === SUMMARY ===
    w("## Summary")
    w("")
    old_total = len(old_pool["questions"])
    new_total = len(new_pool["questions"])
    w(f"| Metric | Value |")
    w(f"|--------|-------|")
    w(f"| 2022-2026 pool size | {old_total} questions |")
    w(f"| 2026-2030 pool size | {new_total} questions |")
    w(f"| Unchanged | {len(results[UNCHANGED])} |")
    w(f"| Reworded | {len(results[REWORDED])} |")
    w(f"| Answer changed | {len(results[ANSWER_CHANGED])} |")
    w(f"| New questions | {len(results[NEW])} |")
    w(f"| Removed questions | {len(results[REMOVED])} |")
    w("")

    total_changed = (
        len(results[REWORDED])
        + len(results[ANSWER_CHANGED])
        + len(results[NEW])
        + len(results[REMOVED])
    )
    w(f"**Total affected**: {total_changed} questions "
      f"({total_changed * 100 / max(old_total, 1):.1f}% of old pool)")
    w("")

    # Percentage changed per subelement
    w("### Change Rate by Subelement")
    w("")
    w("| Subelement | Name (2026) | Unchanged | Reworded | Answer Changed | New | Removed | % Changed |")
    w("|------------|-------------|-----------|----------|----------------|-----|---------|-----------|")
    for sub in sorted(sub_stats.keys()):
        s = sub_stats[sub]
        total_in_sub = (
            len(s[UNCHANGED]) + len(s[REWORDED]) + len(s[ANSWER_CHANGED])
            + len(s[NEW]) + len(s[REMOVED])
        )
        changed_in_sub = (
            len(s[REWORDED]) + len(s[ANSWER_CHANGED])
            + len(s[NEW]) + len(s[REMOVED])
        )
        pct = changed_in_sub * 100 / max(total_in_sub, 1)
        w(f"| {sub} | {s['new_name']} | {len(s[UNCHANGED])} | {len(s[REWORDED])} | "
          f"{len(s[ANSWER_CHANGED])} | {len(s[NEW])} | {len(s[REMOVED])} | {pct:.1f}% |")
    w("")

    # Subelement name changes
    name_changes = [
        (sub, s["old_name"], s["new_name"])
        for sub, s in sub_stats.items()
        if s["name_changed"]
    ]
    if name_changes:
        w("### Subelement Name Changes")
        w("")
        w("| Subelement | 2022-2026 Name | 2026-2030 Name |")
        w("|------------|----------------|----------------|")
        for sub, old_name, new_name in name_changes:
            w(f"| {sub} | {old_name} | {new_name} |")
        w("")

    # New/removed groups
    old_groups = {extract_group(q["id"]) for q in old_pool["questions"]}
    new_groups = {extract_group(q["id"]) for q in new_pool["questions"]}
    added_groups = sorted(new_groups - old_groups)
    removed_groups = sorted(old_groups - new_groups)

    if added_groups or removed_groups:
        w("### Group Changes")
        w("")
        if added_groups:
            w(f"**New groups**: {', '.join(added_groups)}")
            w("")
        if removed_groups:
            w(f"**Removed groups**: {', '.join(removed_groups)}")
            w("")

    # === PER-SUBELEMENT BREAKDOWN ===
    w("---")
    w("")
    w("## Per-Subelement Breakdown")
    w("")

    subelement_guide_map = {
        "T0": "subelements/T0-safety.md",
        "T1": "subelements/T1-fcc-rules.md",
        "T2": "subelements/T2-operating-procedures.md",
        "T3": "subelements/T3-radio-waves.md",
        "T4": "subelements/T4-amateur-practices.md",
        "T5": "subelements/T5-electrical-principles.md",
        "T6": "subelements/T6-components.md",
        "T7": "subelements/T7-practical-circuits.md",
        "T8": "subelements/T8-signals-emissions.md",
        "T9": "subelements/T9-antennas-feedlines.md",
    }

    for sub in sorted(sub_stats.keys()):
        s = sub_stats[sub]
        w(f"### {sub} — {s['new_name']}")
        if s["name_changed"]:
            w(f"")
            w(f"⚠️ **Name changed**: \"{s['old_name']}\" → \"{s['new_name']}\"")
        w("")

        total_in_sub = (
            len(s[UNCHANGED]) + len(s[REWORDED]) + len(s[ANSWER_CHANGED])
            + len(s[NEW]) + len(s[REMOVED])
        )
        changed_in_sub = (
            len(s[REWORDED]) + len(s[ANSWER_CHANGED])
            + len(s[NEW]) + len(s[REMOVED])
        )
        w(f"- **Unchanged**: {len(s[UNCHANGED])} | **Changed**: {changed_in_sub} | "
          f"**Total**: {total_in_sub}")
        w("")

        # NEW questions
        if s[NEW]:
            w(f"#### New Questions ({len(s[NEW])})")
            w("")
            for item in s[NEW]:
                q = item["new"]
                correct_text = q["answers"].get(q["correct"], "?")
                w(f"- **{q['id']}**: {q['question']}")
                w(f"  - ✅ **{q['correct']}**: {correct_text}")
                w("")

        # REMOVED questions
        if s[REMOVED]:
            w(f"#### Removed Questions ({len(s[REMOVED])})")
            w("")
            for item in s[REMOVED]:
                q = item["old"]
                w(f"- **{q['id']}**: {q['question']}")
                w("")

        # ANSWER_CHANGED
        if s[ANSWER_CHANGED]:
            w(f"#### Answer Changed ({len(s[ANSWER_CHANGED])})")
            w("")
            for item in s[ANSWER_CHANGED]:
                w(f"- **{item['id']}**: {item['new']['question']}")
                w(f"  - Old answer: **{item['old_correct_letter']}** — {item['old_correct_text']}")
                w(f"  - New answer: **{item['new_correct_letter']}** — {item['new_correct_text']}")
                w("")

        # REWORDED
        if s[REWORDED]:
            w(f"#### Reworded ({len(s[REWORDED])})")
            w("")
            for item in s[REWORDED]:
                old_text = item["old"]["question"]
                new_text = item["new"]["question"]
                w(f"- **{item['id']}**")
                if old_text != new_text:
                    w(f"  - Old: {old_text}")
                    w(f"  - New: {new_text}")
                # Check for answer option changes
                for letter in ["A", "B", "C", "D"]:
                    old_ans = item["old"]["answers"].get(letter, "")
                    new_ans = item["new"]["answers"].get(letter, "")
                    if old_ans != new_ans:
                        w(f"  - Option {letter}: \"{old_ans}\" → \"{new_ans}\"")
                w("")

        # Impact assessment
        guide_path = subelement_guide_map.get(sub, "N/A")
        w(f"#### Impact Assessment")
        w("")
        if changed_in_sub == 0:
            w(f"✅ **No updates needed** for `{guide_path}`.")
        else:
            w(f"📝 **`{guide_path}` needs review.**")
            if s[NEW]:
                topics = set()
                for item in s[NEW]:
                    # Extract the core topic from the question
                    q_text = item["new"]["question"]
                    topics.add(q_text[:80] + "..." if len(q_text) > 80 else q_text)
                w(f"  - {len(s[NEW])} new question(s) may introduce new topics")
            if s[REMOVED]:
                w(f"  - {len(s[REMOVED])} question(s) removed — check for obsolete content")
            if s[ANSWER_CHANGED]:
                w(f"  - {len(s[ANSWER_CHANGED])} answer(s) changed — verify correctness of guide explanations")
            if s[REWORDED]:
                w(f"  - {len(s[REWORDED])} question(s) reworded — minor review for alignment")
            if s["name_changed"]:
                w(f"  - ⚠️ Subelement name changed — update guide title and references")
        w("")

    # === PER-GROUP BREAKDOWN ===
    w("---")
    w("")
    w("## Per-Group Breakdown")
    w("")
    w("| Group | Unchanged | Reworded | Answer Changed | New | Removed | Total Changes |")
    w("|-------|-----------|----------|----------------|-----|---------|---------------|")
    for grp in sorted(grp_stats.keys()):
        g = grp_stats[grp]
        w(f"| {grp} | {g[UNCHANGED]} | {g[REWORDED]} | {g[ANSWER_CHANGED]} | "
          f"{g[NEW]} | {g[REMOVED]} | {g['total_changes']} |")
    w("")

    # Most changed groups
    top_groups = sorted(grp_stats.items(), key=lambda x: x[1]["total_changes"], reverse=True)[:10]
    w("### Most Changed Groups")
    w("")
    for grp, g in top_groups:
        if g["total_changes"] > 0:
            w(f"1. **{grp}** — {g['total_changes']} changes "
              f"(+{g[NEW]} new, -{g[REMOVED]} removed, "
              f"~{g[REWORDED]} reworded, ⇄{g[ANSWER_CHANGED]} answer changed)")
    w("")

    # === FIGURES CHECK ===
    w("---")
    w("")
    w("## Figures Check")
    w("")
    w(f"- 2022-2026 pool references: {sorted(old_figs) if old_figs else 'none'}")
    w(f"- 2026-2030 pool references: {sorted(new_figs) if new_figs else 'none'}")
    w(f"- Existing figures in `figures/`: {sorted(existing_figs)}")
    w("")
    new_fig_refs = new_figs - old_figs
    if new_fig_refs:
        w(f"⚠️ **New figure references**: {sorted(new_fig_refs)} — need to add images")
    else:
        w("✅ No new figure references in 2026-2030 pool.")
    removed_fig_refs = old_figs - new_figs
    if removed_fig_refs:
        w(f"ℹ️ Figures no longer referenced: {sorted(removed_fig_refs)}")
    w("")

    # Check which figures are actually present
    missing_figs = []
    for fig in sorted(new_figs):
        fig_file = f"{fig}.png"
        if fig_file not in existing_figs:
            missing_figs.append(fig)
    if missing_figs:
        w(f"⚠️ **Missing figure files**: {missing_figs}")
    else:
        w("✅ All referenced figures have corresponding files.")
    w("")

    return "\n".join(lines)


def generate_json_report(
    results: dict[str, list[dict]],
    sub_stats: dict[str, dict],
    grp_stats: dict[str, dict],
    old_pool: dict,
    new_pool: dict,
) -> dict:
    """Generate a structured JSON report."""
    def simplify_q(q: dict) -> dict:
        return {
            "id": q["id"],
            "subelement": q["subelement"],
            "group": q["group"],
            "question": q["question"],
            "correct": q["correct"],
            "correct_text": q["answers"].get(q["correct"], ""),
        }

    report = {
        "summary": {
            "old_pool_size": len(old_pool["questions"]),
            "new_pool_size": len(new_pool["questions"]),
            "unchanged": len(results[UNCHANGED]),
            "reworded": len(results[REWORDED]),
            "answer_changed": len(results[ANSWER_CHANGED]),
            "new": len(results[NEW]),
            "removed": len(results[REMOVED]),
        },
        "subelement_stats": {},
        "group_stats": grp_stats,
        "new_questions": [simplify_q(item["new"]) for item in results[NEW]],
        "removed_questions": [simplify_q(item["old"]) for item in results[REMOVED]],
        "answer_changed": [
            {
                "id": item["id"],
                "question": item["new"]["question"],
                "old_answer": f"{item['old_correct_letter']}: {item['old_correct_text']}",
                "new_answer": f"{item['new_correct_letter']}: {item['new_correct_text']}",
            }
            for item in results[ANSWER_CHANGED]
        ],
        "reworded": [
            {
                "id": item["id"],
                "old_question": item["old"]["question"],
                "new_question": item["new"]["question"],
            }
            for item in results[REWORDED]
        ],
    }

    for sub, s in sub_stats.items():
        report["subelement_stats"][sub] = {
            "old_name": s["old_name"],
            "new_name": s["new_name"],
            "name_changed": s["name_changed"],
            "unchanged": len(s[UNCHANGED]),
            "reworded": len(s[REWORDED]),
            "answer_changed": len(s[ANSWER_CHANGED]),
            "new": len(s[NEW]),
            "removed": len(s[REMOVED]),
        }

    return report


def main() -> None:
    # Load pools
    old_pool = load_pool(OLD_POOL)
    new_pool = load_pool(NEW_POOL)

    old_idx = index_by_id(old_pool["questions"])
    new_idx = index_by_id(new_pool["questions"])

    # Categorize
    results = categorize_questions(old_idx, new_idx)

    # Stats
    sub_stats = subelement_stats(
        results,
        old_pool.get("subelements", {}),
        new_pool.get("subelements", {}),
    )
    grp = group_stats(results)

    # Figures
    old_figs = find_figure_refs(old_pool["questions"])
    new_figs = find_figure_refs(new_pool["questions"])
    figures_dir = REPO_ROOT / "figures"
    existing_figs = [f.name for f in figures_dir.iterdir() if f.is_file()] if figures_dir.exists() else []

    # Generate reports
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    md = generate_markdown(results, sub_stats, grp, old_pool, new_pool, old_figs, new_figs, existing_figs)
    REPORT_MD.write_text(md)
    print(f"✅ Markdown report: {REPORT_MD}")

    json_report = generate_json_report(results, sub_stats, grp, old_pool, new_pool)
    REPORT_JSON.write_text(json.dumps(json_report, indent=2))
    print(f"✅ JSON report: {REPORT_JSON}")

    # Print summary
    print()
    print("=== SUMMARY ===")
    print(f"Old pool: {len(old_pool['questions'])} questions")
    print(f"New pool: {len(new_pool['questions'])} questions")
    print(f"Unchanged:      {len(results[UNCHANGED]):>4}")
    print(f"Reworded:       {len(results[REWORDED]):>4}")
    print(f"Answer changed: {len(results[ANSWER_CHANGED]):>4}")
    print(f"New:            {len(results[NEW]):>4}")
    print(f"Removed:        {len(results[REMOVED]):>4}")


if __name__ == "__main__":
    main()
