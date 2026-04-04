#!/usr/bin/env python3
"""
General Class Ham Radio Practice Exam

Simulates the real FCC General exam: 35 questions drawn randomly from the
2023-2027 question pool, weighted by subelement (same distribution as the
actual exam). Interactive CLI — no dependencies beyond stdlib.

Usage:
    python3 scripts/practice-test.py
    python3 scripts/practice-test.py --pool pools/2023-2027/questions.json
"""

import json
import random
import sys
import os
from pathlib import Path

# Real exam weights per subelement (total = 35)
EXAM_WEIGHTS: dict[str, int] = {
    "G1": 5,  # Commission's Rules
    "G2": 5,  # Operating Procedures
    "G3": 3,  # Radio Wave Propagation
    "G4": 5,  # Amateur Radio Practices
    "G5": 3,  # Electrical Principles
    "G6": 2,  # Circuit Components
    "G7": 3,  # Practical Circuits
    "G8": 3,  # Signals and Emissions
    "G9": 4,  # Antennas and Feed Lines
    "G0": 2,  # Electrical and RF Safety
}

PASSING_SCORE = 26
TOTAL_QUESTIONS = 35

SUBELEMENT_NAMES: dict[str, str] = {
    "G0": "Electrical & RF Safety",
    "G1": "Commission's Rules",
    "G2": "Operating Procedures",
    "G3": "Radio Wave Propagation",
    "G4": "Amateur Radio Practices",
    "G5": "Electrical Principles",
    "G6": "Circuit Components",
    "G7": "Practical Circuits",
    "G8": "Signals & Emissions",
    "G9": "Antennas & Feed Lines",
}


def load_pool(pool_path: str) -> list[dict]:
    """Load question pool from JSON file."""
    with open(pool_path) as f:
        data = json.load(f)
    questions = data.get("questions", data)
    if not isinstance(questions, list):
        print(f"Error: Expected a list of questions in {pool_path}")
        sys.exit(1)
    return questions


def select_exam_questions(pool: list[dict]) -> list[dict]:
    """Select 35 questions weighted by subelement, matching real exam distribution."""
    by_subelement: dict[str, list[dict]] = {}
    for q in pool:
        sub = q["subelement"]
        by_subelement.setdefault(sub, []).append(q)

    selected: list[dict] = []
    for sub, count in EXAM_WEIGHTS.items():
        available = by_subelement.get(sub, [])
        if len(available) < count:
            print(f"Warning: {sub} has only {len(available)} questions, need {count}")
            selected.extend(available)
        else:
            selected.extend(random.sample(available, count))

    random.shuffle(selected)
    return selected


def clear_screen() -> None:
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def format_question(num: int, total: int, question: dict) -> str:
    """Format a question for display."""
    lines = []
    lines.append(f"━━━ Question {num}/{total} ━━━  [{question['id']}]")
    lines.append("")
    lines.append(question["question"])
    lines.append("")
    for letter in ("A", "B", "C", "D"):
        answer_text = question["answers"].get(letter, "")
        if answer_text:
            lines.append(f"  {letter}) {answer_text}")
    lines.append("")
    return "\n".join(lines)


def get_answer() -> str:
    """Get a valid answer (A-D) or Q to quit."""
    while True:
        try:
            raw = input("Your answer (A/B/C/D or Q to quit): ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print()
            return "Q"
        if raw in ("A", "B", "C", "D", "Q"):
            return raw
        print("  Please enter A, B, C, or D (or Q to quit)")


def run_exam(pool_path: str) -> None:
    """Run a full practice exam."""
    pool = load_pool(pool_path)
    questions = select_exam_questions(pool)

    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║     General Class Amateur Radio Practice Exam    ║")
    print("║                                                  ║")
    print("║  35 questions • 26 to pass (74%)                 ║")
    print("║  Same subelement weights as the real exam        ║")
    print("║                                                  ║")
    print("║  Enter A, B, C, or D for each question           ║")
    print("║  Press Q at any time to quit                     ║")
    print("╚══════════════════════════════════════════════════╝")
    print()
    input("Press Enter to begin...")
    print()

    correct = 0
    wrong = 0
    missed: list[dict] = []
    sub_correct: dict[str, int] = {}
    sub_total: dict[str, int] = {}

    for i, q in enumerate(questions, 1):
        sub = q["subelement"]
        sub_total[sub] = sub_total.get(sub, 0) + 1

        print(format_question(i, TOTAL_QUESTIONS, q))
        answer = get_answer()

        if answer == "Q":
            print(f"\n  Exam ended early after {i - 1} questions.")
            break

        correct_letter = q["correct"]
        correct_text = q["answers"][correct_letter]

        if answer == correct_letter:
            correct += 1
            sub_correct[sub] = sub_correct.get(sub, 0) + 1
            print(f"  ✅ Correct! The answer is {correct_letter}) {correct_text}")
        else:
            wrong += 1
            your_text = q["answers"].get(answer, "")
            missed.append({"question": q, "your_answer": answer})
            print(f"  ❌ Wrong. You chose {answer}) {your_text}")
            print(f"     Correct answer: {correct_letter}) {correct_text}")

        print(f"     Score so far: {correct}/{i}")
        print()

    # Results
    total_answered = correct + wrong
    if total_answered == 0:
        print("No questions answered.")
        return

    pct = (correct / total_answered) * 100
    passed = correct >= PASSING_SCORE and total_answered == TOTAL_QUESTIONS

    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║                  EXAM RESULTS                    ║")
    print("╚══════════════════════════════════════════════════╝")
    print()
    print(f"  Score: {correct}/{total_answered} ({pct:.0f}%)")
    print(f"  Passing: {PASSING_SCORE}/{TOTAL_QUESTIONS} (74%)")
    print()

    if total_answered < TOTAL_QUESTIONS:
        print(f"  ⚠️  Exam incomplete ({total_answered}/{TOTAL_QUESTIONS} answered)")
        if correct >= PASSING_SCORE:
            print("  You have enough correct answers to pass!")
        else:
            remaining = TOTAL_QUESTIONS - total_answered
            needed = PASSING_SCORE - correct
            if needed <= remaining:
                print(f"  You need {needed} more correct out of {remaining} remaining to pass")
            else:
                print("  Not enough remaining questions to pass")
    elif passed:
        print("  🎉 PASSED! You would pass the General exam!")
    else:
        needed = PASSING_SCORE - correct
        print(f"  ❌ Not passing. Need {needed} more correct answers.")

    # Per-subelement breakdown
    print()
    print("  Per-Subelement Breakdown:")
    print("  ─────────────────────────────────────────────")
    for sub in ("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G0"):
        total_sub = sub_total.get(sub, 0)
        correct_sub = sub_correct.get(sub, 0)
        name = SUBELEMENT_NAMES.get(sub, sub)
        if total_sub > 0:
            bar = "█" * correct_sub + "░" * (total_sub - correct_sub)
            print(f"  {sub} {name:<28s} {bar} {correct_sub}/{total_sub}")

    # Missed questions review
    if missed:
        print()
        print(f"  Questions to Review ({len(missed)} missed):")
        print("  ─────────────────────────────────────────────")
        for m in missed:
            q = m["question"]
            correct_letter = q["correct"]
            print(f"  {q['id']}: {q['question'][:70]}...")
            print(f"         Correct: {correct_letter}) {q['answers'][correct_letter]}")
            print()

    print()


def find_pool() -> str:
    """Find the question pool file."""
    # Check common locations relative to script and repo root
    candidates = [
        Path(__file__).parent.parent / "pools" / "2023-2027" / "questions.json",
        Path("pools/2023-2027/questions.json"),
        Path("../pools/2023-2027/questions.json"),
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    print("Error: Could not find pools/2023-2027/questions.json")
    print("Usage: python3 scripts/practice-test.py [--pool PATH]")
    sys.exit(1)


def main() -> None:
    """Entry point."""
    pool_path = None
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print(__doc__)
        sys.exit(0)

    if "--pool" in args:
        idx = args.index("--pool")
        if idx + 1 < len(args):
            pool_path = args[idx + 1]
        else:
            print("Error: --pool requires a path argument")
            sys.exit(1)

    if pool_path is None:
        pool_path = find_pool()

    try:
        run_exam(pool_path)
    except KeyboardInterrupt:
        print("\n\nExam cancelled.")
        sys.exit(0)


if __name__ == "__main__":
    main()
