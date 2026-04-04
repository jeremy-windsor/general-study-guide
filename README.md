# Amateur Radio General Class Exam Study Guide

Pass the FCC General class license exam. All questions, all answers, explained.

## What's Inside

- **429 real exam questions** (2023-2027 pool) with correct answers
- **10 study sections** organized by topic (subelements G1-G0)
- **Cram sheet** for last-minute review
- **Practice test script** to simulate the real exam
- **7-day study plan** to get you from zero to licensed
- **PWA study app** with flashcards, practice exams, and progress tracking

## The Exam

| | |
|---|---|
| **Questions** | 35 multiple choice |
| **Passing** | 26 correct (74%) |
| **Time** | No official time limit |
| **Fee** | ~$15 VEC session fee + $35 FCC application fee |
| **Prerequisite** | Technician class license |
| **Where** | Find a session at [arrl.org/find-an-amateur-radio-license-exam-session](http://www.arrl.org/find-an-amateur-radio-license-exam-session) |

The exam pulls from a **fixed public question pool** — every possible question and answer is published. This guide covers all of them.

## Study App (PWA)

The fastest way to study — a browser-based app that works on your phone, tablet, or desktop. No install required.

### **[Open the Study App](https://jeremy-windsor.github.io/general-study-guide/apps/study-app/)**

| Feature | |
|---------|---|
| **Flashcard mode** | Tap through all questions with instant answer reveal |
| **Practice exams** | Timed 35-question tests drawn randomly from the real pool |
| **Section study** | Drill down into individual subelements and groups |
| **Weak areas** | Automatically focuses on questions you've missed |
| **Progress tracking** | Mastery tracking, streaks, and achievements |
| **Offline capable** | Works without internet after first load |
| **Installable** | Add to Home Screen on mobile, or install from Chrome/Edge on desktop |

> **Tip:** Add it to your phone's home screen — it runs like a native app, works offline, and tracks your progress across sessions.

## Question Pool

| Pool | Effective | Expires | Questions |
|------|-----------|---------|-----------|
| [2023-2027](pools/2023-2027/) | July 1, 2023 | June 30, 2027 | 429 |

**Source:** [NCVEC](https://www.ncvec.org/index.php/2023-2027-general-question-pool-release) — released into public domain.

## How to Study

### Quick Path (7 days)

See [STUDY-PLAN.md](STUDY-PLAN.md) for the full day-by-day plan.

| Day | Topic | Section |
|-----|-------|---------|
| 1 | Rules & Privileges | [G1](subelements/G1-commission-rules.md), [G0](subelements/G0-safety.md) |
| 2 | Operating Procedures | [G2](subelements/G2-operating-procedures.md) |
| 3 | Propagation | [G3](subelements/G3-radio-wave-propagation.md) |
| 4 | Amateur Practices | [G4](subelements/G4-amateur-practices.md) |
| 5 | Electrical Theory & Components | [G5](subelements/G5-electrical-principles.md), [G6](subelements/G6-circuit-components.md) |
| 6 | Circuits, Signals & Antennas | [G7](subelements/G7-practical-circuits.md), [G8](subelements/G8-signals-emissions.md), [G9](subelements/G9-antennas-feedlines.md) |
| 7 | Review + Practice Test | [Cram Sheet](CRAM-SHEET.md) + `python3 scripts/practice-test.py` |

### Study Sections

Each subelement has three files:

- **`G{N}-{name}.md`** — Study guide: a narrative walkthrough of the topic, written for learning
- **`G{N}-{name}.mp3`** — Audio version of the study guide (listen while driving, working out, etc.)
- **`G{N}-{name}-questions.md`** — Exam question bank: every question with the correct answer highlighted and explained

Start with the study guide to learn the material, then drill the question bank to lock in the answers.

| Section | Topic | Study Guide | Question Bank | Exam Qs | Pool Size |
|---------|-------|-------------|---------------|:-:|:-:|
| G1 | Commission's Rules | [guide](subelements/G1-commission-rules.md) | [questions](subelements/G1-commission-rules-questions.md) | 5 | 57 |
| G2 | Operating Procedures | [guide](subelements/G2-operating-procedures.md) | [questions](subelements/G2-operating-procedures-questions.md) | 5 | 60 |
| G3 | Radio Wave Propagation | [guide](subelements/G3-radio-wave-propagation.md) | [questions](subelements/G3-radio-wave-propagation-questions.md) | 3 | 37 |
| G4 | Amateur Radio Practices | [guide](subelements/G4-amateur-practices.md) | [questions](subelements/G4-amateur-practices-questions.md) | 5 | 60 |
| G5 | Electrical Principles | [guide](subelements/G5-electrical-principles.md) | [questions](subelements/G5-electrical-principles-questions.md) | 3 | 40 |
| G6 | Circuit Components | [guide](subelements/G6-circuit-components.md) | [questions](subelements/G6-circuit-components-questions.md) | 2 | 23 |
| G7 | Practical Circuits | [guide](subelements/G7-practical-circuits.md) | [questions](subelements/G7-practical-circuits-questions.md) | 3 | 38 |
| G8 | Signals and Emissions | [guide](subelements/G8-signals-emissions.md) | [questions](subelements/G8-signals-emissions-questions.md) | 3 | 43 |
| G9 | Antennas and Feed Lines | [guide](subelements/G9-antennas-feedlines.md) | [questions](subelements/G9-antennas-feedlines-questions.md) | 4 | 46 |
| G0 | Electrical and RF Safety | [guide](subelements/G0-safety.md) | [questions](subelements/G0-safety-questions.md) | 2 | 25 |
| | **Total** | | | **35** | **429** |

### Practice Test

```bash
python3 scripts/practice-test.py
```

Generates a random 35-question exam from the real pool, scores it, and shows which areas need work.

### Audio Study Guide

Every section and the cram sheet are available as MP3 audio — study while driving, working out, or doing chores.

| File | Duration |
|------|----------|
| `subelements/G1-commission-rules.mp3` | 17 min |
| `subelements/G1-commission-rules-questions.mp3` | 54 min |
| `subelements/G2-operating-procedures.mp3` | 17 min |
| `subelements/G2-operating-procedures-questions.mp3` | 54 min |
| `subelements/G3-radio-wave-propagation.mp3` | 17 min |
| `subelements/G3-radio-wave-propagation-questions.mp3` | 36 min |
| `subelements/G4-amateur-practices.mp3` | 18 min |
| `subelements/G4-amateur-practices-questions.mp3` | 58 min |
| `subelements/G5-electrical-principles.mp3` | 19 min |
| `subelements/G5-electrical-principles-questions.mp3` | 27 min |
| `subelements/G6-circuit-components.mp3` | 16 min |
| `subelements/G6-circuit-components-questions.mp3` | 18 min |
| `subelements/G7-practical-circuits.mp3` | 23 min |
| `subelements/G7-practical-circuits-questions.mp3` | 31 min |
| `subelements/G8-signals-emissions.mp3` | 19 min |
| `subelements/G8-signals-emissions-questions.mp3` | 42 min |
| `subelements/G9-antennas-feedlines.mp3` | 20 min |
| `subelements/G9-antennas-feedlines-questions.mp3` | 46 min |
| `subelements/G0-safety.mp3` | 13 min |
| `subelements/G0-safety-questions.mp3` | 26 min |
| `CRAM-SHEET.mp3` | 7 min |
| **Total** | **9h 37m** |

Each MP3 is the audio version of the corresponding study guide narrative or question bank. Pronunciation of ham radio acronyms follows standard conventions (see `tts/pronunciation.txt`).

### Study Tips

- **Start with rules (G1)** — know your privileges before anything else
- **Spend extra time on G4** — Amateur Radio Practices has the most exam questions tied with G1 and G2
- **Don't skip the math** — G5 formulas show up repeatedly; learn Ohm's Law, power, and reactance
- **Practice exams daily** — take at least one practice test per study session
- **Use the formula reference** — tap the formula button in the app for quick formula access

### Cram Sheet

[CRAM-SHEET.md](CRAM-SHEET.md) — one page of key facts, formulas, frequencies, and power limits. Read this the morning of your exam.

## Quick References

- **[Cram Sheet](CRAM-SHEET.md)** — Formulas, frequencies, and key numbers on one page
- **[Glossary](GLOSSARY.md)** — 100+ key terms (A-Z) with definitions and subelement references
- **[Study Plan](STUDY-PLAN.md)** — 7-day structured study schedule

## Coming from Technician?

New to HF? Check [What You Should Already Know](TECHNICIAN-BRIDGE.md) — a quick refresher on Technician concepts (Ohm's Law, frequency/wavelength, VHF/UHF propagation) that the General exam builds on.

## Regenerating Audio

Audio is generated via [Kokoro](https://github.com/remsky/Kokoro-FastAPI) (OpenAI-compatible TTS). Requires Python 3.6+, `curl`, `ffmpeg`.

```bash
tts/scripts/gen-all.sh
```

Pronunciation rules are in `tts/pronunciation.txt`. Individual modules can be regenerated with `tts/scripts/gen-module-tts.sh`.

## Updating for a New Pool

1. Download the new pool PDF from [ncvec.org](https://ncvec.org/index.php/amateur-question-pools)
2. Parse into `pools/YYYY-YYYY/questions.json` using `python3 scripts/parse-pool.py`
3. Regenerate subelement files with `python3 scripts/gen-question-files.py`
4. Update practice test pool path in `scripts/practice-test.py`
5. Update dates in this README
6. Regenerate audio with the TTS pipeline above

## License

Question pool content is public domain (NCVEC). Study guide explanations and scripts are MIT licensed.
