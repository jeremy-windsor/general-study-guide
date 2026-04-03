#!/usr/bin/env python3
"""
Convert General study guide markdown to spoken text for TTS.

Handles the tech guide format:
  - ### T1A01 question headers
  - - A) / - **C) answer ✅** answer choices
  - > explanation blocks
  - # T1 — FCC Rules section headers
"""
import re
import sys


def clean_md(text: str) -> str:
    """Strip markdown formatting, return natural spoken text."""
    # Remove checkmark emoji
    text = text.replace('✅', '')
    # Remove blockquote markers
    text = re.sub(r'^>\s?', '', text, flags=re.MULTILINE)
    # Remove bold/italic markers
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    # Remove inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Remove links
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Remove markdown headers (keep content)
    text = re.sub(r'^#{1,4}\s+', '', text, flags=re.MULTILINE)
    # Collapse excess whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def parse_question_block(header: str, body: str) -> list[str]:
    """
    Parse a question block and return lines of spoken text.

    header: e.g. "T1A01"
    body:   everything after the ### T1A01 line until next question
    """
    lines = []
    body = body.strip()

    # Extract the [rule-ref] if present — strip it
    body = re.sub(r'^\[.*?\]\s*', '', body)

    # Split into question text, answer choices, and explanation
    # Question text is everything before the first "- A)" line
    choice_pattern = re.compile(r'^-\s+(?:\*\*)?([A-D])\)', re.MULTILINE)
    first_choice = choice_pattern.search(body)

    if first_choice:
        question_text = body[:first_choice.start()].strip()
        rest = body[first_choice.start():]
    else:
        question_text = body
        rest = ''

    # Find the explanation (> block) — it comes after the choices
    explanation_match = re.search(r'^>\s', rest, re.MULTILINE)
    if explanation_match:
        choices_raw = rest[:explanation_match.start()].strip()
        explanation_raw = rest[explanation_match.start():].strip()
    else:
        choices_raw = rest.strip()
        explanation_raw = ''

    # Parse choices — find the correct one (marked with ✅ or **)
    choices = []
    correct_letter = None
    correct_text = None

    for m in re.finditer(r'^-\s+(?:\*\*)?([A-D])\)\s+(.+?)(?:\s+✅)?(?:\*\*)?$', choices_raw, re.MULTILINE):
        letter = m.group(1)
        text = m.group(2).strip().rstrip('*').strip()
        choices.append((letter, text))
        # Check if this line contains the correct answer marker
        raw_line = m.group(0)
        if '✅' in raw_line or ('**' in raw_line and '**' in raw_line[3:]):
            correct_letter = letter
            correct_text = text

    lines.append(f'Question {header}.')
    lines.append('')
    lines.append(clean_md(question_text))
    lines.append('')

    # Speak each choice
    for letter, text in choices:
        lines.append(f'{letter}. {clean_md(text)}')

    lines.append('')

    # Correct answer
    if correct_letter and correct_text:
        lines.append(f'The correct answer is {correct_letter}. {clean_md(correct_text)}.')
    lines.append('')

    # Explanation
    if explanation_raw:
        explanation = clean_md(explanation_raw)
        if explanation:
            lines.append(explanation)
            lines.append('')

    return lines


def convert_file(path: str) -> str:
    """Convert a subelement markdown file to spoken text."""
    with open(path) as f:
        content = f.read()

    spoken = []

    # Extract title from first # header
    title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    if title_match:
        title = clean_md(title_match.group(1))
        spoken.append(f'{title}.')
        spoken.append('')

    # Split on ### TxXnn headers (question IDs)
    # Pattern: ### T0A01 or ### T1A01 etc.
    parts = re.split(r'^### (T\w+)\s*\n', content, flags=re.MULTILINE)

    if len(parts) < 3:
        # No questions found — probably a cram sheet or different format
        spoken.append(clean_md(content))
        return '\n'.join(spoken)

    # parts[0] = preamble (before first question), then alternating id/body
    preamble = parts[0]

    # Extract group headers from preamble and inject them
    # Group headers look like: ## Group T1A — Purpose and permissible use...
    group_headers = re.findall(r'^##\s+(.+)', preamble, re.MULTILINE)
    for gh in group_headers:
        spoken.append(clean_md(gh) + '.')
        spoken.append('')

    for i in range(1, len(parts), 2):
        qid = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ''

        # Check if a new group header appears in the body before any answer choices
        # (Groups start with ## Group ...)
        group_match = re.search(r'^## Group .+$', body, re.MULTILINE)
        if group_match:
            # Inject group header
            gh_text = clean_md(group_match.group(0))
            spoken.append(gh_text + '.')
            spoken.append('')
            # Remove the group header from body
            body = body[:group_match.start()] + body[group_match.end():]

        spoken.extend(parse_question_block(qid, body))

    return '\n'.join(spoken)


def convert_cram_sheet(path: str) -> str:
    """Convert the cram sheet markdown to spoken text."""
    with open(path) as f:
        content = f.read()

    spoken = []

    title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    if title_match:
        spoken.append(clean_md(title_match.group(1)) + '.')
        spoken.append('')

    # Just clean up the markdown and speak it naturally
    # Remove table formatting nicely
    lines = content.split('\n')
    for line in lines:
        # Skip title (already handled)
        if re.match(r'^#\s+', line):
            continue
        # Section headers
        if re.match(r'^##\s+', line):
            text = re.sub(r'^##\s+', '', line).strip()
            spoken.append('')
            spoken.append(text + '.')
            continue
        # Table separator lines
        if re.match(r'^[\|\-:\s]+$', line):
            continue
        # Table rows
        if '|' in line:
            cells = [c.strip() for c in line.strip('|').split('|')]
            cells = [c for c in cells if c]
            if cells:
                spoken.append('. '.join(clean_md(c) for c in cells) + '.')
            continue
        # Bullet points
        m = re.match(r'^-\s+\*\*(.+?)\*\*:?\s*(.*)', line)
        if m:
            term = clean_md(m.group(1))
            desc = clean_md(m.group(2))
            if desc:
                spoken.append(f'{term}: {desc}.')
            else:
                spoken.append(f'{term}.')
            continue
        # Blockquotes
        if line.startswith('>'):
            spoken.append(clean_md(line))
            continue
        # Normal lines
        cleaned = clean_md(line)
        if cleaned:
            spoken.append(cleaned)

    return '\n'.join(spoken)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: tech-to-tts.py <file.md> [--cram]', file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    is_cram = '--cram' in sys.argv

    if is_cram:
        print(convert_cram_sheet(path))
    else:
        print(convert_file(path))
