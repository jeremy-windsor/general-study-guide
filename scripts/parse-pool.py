#!/usr/bin/env python3
"""Parse the 2023-2027 General Class question pool text into questions.json."""

import json
import re
import sys
from pathlib import Path

# Subelement metadata from the official syllabus
SUBELEMENTS = {
    "G1": {"name": "Commission's Rules", "exam_questions": 5},
    "G2": {"name": "Operating Procedures", "exam_questions": 5},
    "G3": {"name": "Radio Wave Propagation", "exam_questions": 3},
    "G4": {"name": "Amateur Radio Practices", "exam_questions": 5},
    "G5": {"name": "Electrical Principles", "exam_questions": 3},
    "G6": {"name": "Circuit Components", "exam_questions": 2},
    "G7": {"name": "Practical Circuits", "exam_questions": 3},
    "G8": {"name": "Signals and Emissions", "exam_questions": 3},
    "G9": {"name": "Antennas and Feed Lines", "exam_questions": 4},
    "G0": {"name": "Electrical and RF Safety", "exam_questions": 2},
}

# Regex for question header: e.g. "G1A01 (C) [97.301(d)]"
Q_HEADER = re.compile(
    r'^(G[0-9][A-Z]\d{2})\s+\(([A-D])\)\s*(?:\[([^\]]*)\])?\s*$'
)

# Regex for answer lines: "A. text", "B. text", etc.
# Some lines have no space after the dot (e.g. "D.A DX spotting system")
ANSWER_LINE = re.compile(r'^([A-D])\.\s*(.+)$')

# Question separator
SEPARATOR = re.compile(r'^~~\s*$')


def parse_pool(text: str) -> list[dict]:
    """Parse the raw pool text into a list of question dicts."""
    lines = text.split('\n')
    questions = []
    
    # Find where actual questions start (first line matching Q_HEADER)
    start_idx = 0
    for i, line in enumerate(lines):
        if Q_HEADER.match(line.strip()):
            start_idx = i
            break
    
    current_q = None
    question_lines = []
    
    for line in lines[start_idx:]:
        stripped = line.strip()
        
        # Check for question header
        m = Q_HEADER.match(stripped)
        if m:
            # Save previous question if any
            if current_q and current_q.get('answers'):
                questions.append(current_q)
            
            qid = m.group(1)
            correct = m.group(2)
            refs = m.group(3) or ''
            
            # Derive subelement and group
            subelement = qid[:2]
            group = qid[:3]
            
            current_q = {
                'id': qid,
                'subelement': subelement,
                'group': group,
                'correct': correct,
                'refs': refs,
                'question': '',
                'answers': {},
            }
            question_lines = []
            continue
        
        # Check for separator
        if SEPARATOR.match(stripped):
            if current_q and current_q.get('answers'):
                questions.append(current_q)
                current_q = None
            continue
        
        if current_q is None:
            continue
        
        # Check for answer line
        am = ANSWER_LINE.match(stripped)
        if am:
            letter = am.group(1)
            answer_text = am.group(2).strip()
            current_q['answers'][letter] = answer_text
            continue
        
        # Otherwise it's part of the question text
        if stripped and not current_q['answers']:
            if current_q['question']:
                current_q['question'] += ' ' + stripped
            else:
                current_q['question'] = stripped
    
    # Don't forget last question
    if current_q and current_q.get('answers'):
        questions.append(current_q)
    
    return questions


def build_output(questions: list[dict]) -> dict:
    """Build the final JSON structure."""
    # Count per subelement
    se_counts = {}
    for q in questions:
        se = q['subelement']
        se_counts[se] = se_counts.get(se, 0) + 1
    
    subelements = {}
    for se_id, meta in SUBELEMENTS.items():
        subelements[se_id] = {
            "name": meta["name"],
            "exam_questions": meta["exam_questions"],
            "pool_size": se_counts.get(se_id, 0),
        }
    
    # Format questions with refs in the question text
    formatted = []
    for q in questions:
        question_text = q['question']
        if q['refs']:
            question_text = f"[{q['refs']}] {question_text}"
        
        formatted.append({
            "id": q['id'],
            "subelement": q['subelement'],
            "group": q['group'],
            "question": question_text,
            "correct": q['correct'],
            "answers": q['answers'],
        })
    
    return {
        "pool": "General",
        "effective": "2023-07-01",
        "expires": "2027-06-30",
        "total": len(formatted),
        "subelements": subelements,
        "questions": formatted,
    }


def validate(data: dict) -> list[str]:
    """Validate the parsed data."""
    errors = []
    
    for q in data['questions']:
        # Must have all 4 answers
        for letter in ['A', 'B', 'C', 'D']:
            if letter not in q['answers']:
                errors.append(f"{q['id']}: missing answer {letter}")
        
        # Correct answer must be one of A-D
        if q['correct'] not in ['A', 'B', 'C', 'D']:
            errors.append(f"{q['id']}: invalid correct answer '{q['correct']}'")
        
        # Correct answer must exist in answers
        if q['correct'] not in q['answers']:
            errors.append(f"{q['id']}: correct answer {q['correct']} not in answers")
        
        # Question must not be empty
        if not q['question'].strip():
            errors.append(f"{q['id']}: empty question text")
        
        # ID format check
        if not re.match(r'^G[0-9][A-Z]\d{2}$', q['id']):
            errors.append(f"{q['id']}: invalid ID format")
    
    return errors


def main():
    pool_dir = Path(__file__).parent.parent / 'pools' / '2023-2027'
    raw_file = Path('/tmp/general-pool-utf8.txt')
    output_file = pool_dir / 'questions.json'
    
    if not raw_file.exists():
        print(f"Error: {raw_file} not found", file=sys.stderr)
        sys.exit(1)
    
    text = raw_file.read_text(encoding='utf-8')
    questions = parse_pool(text)
    
    print(f"Parsed {len(questions)} questions")
    
    # Print per-subelement counts
    se_counts = {}
    for q in questions:
        se = q['subelement']
        se_counts[se] = se_counts.get(se, 0) + 1
    
    for se in sorted(se_counts.keys(), key=lambda x: (x != 'G0', x)):
        print(f"  {se}: {se_counts[se]} questions")
    
    data = build_output(questions)
    errors = validate(data)
    
    if errors:
        print(f"\nValidation errors ({len(errors)}):", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        sys.exit(1)
    
    print(f"\nValidation passed ✓")
    print(f"Total: {data['total']} questions")
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    print(f"Written to {output_file}")


if __name__ == '__main__':
    main()
