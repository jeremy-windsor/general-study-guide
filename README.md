# Amateur Radio General Class Exam Study Guide

Pass the FCC General class license exam. Every question in the official pool, answered and explained, with study guides, audio, and a study app.

**[Open the Study App](https://jeremy-windsor.github.io/general-study-guide/apps/study-app/)**: flashcards, timed practice exams, weak-area drills, and progress tracking. Works offline and installs to your phone's home screen.

## The Exam

| | |
|---|---|
| **Questions** | 35 multiple choice, one from each topic group in the pool |
| **Passing** | 26 correct (74%) |
| **Prerequisite** | Technician class license |
| **Fee** | ~$15 VEC session fee (no FCC fee for an upgrade) |
| **Where** | [Find an exam session](http://www.arrl.org/find-an-amateur-radio-license-exam-session) |
| **Question pool** | [2023–2027 pool](pools/2023-2027/), 423 questions, valid July 1, 2023 – June 30, 2027, through NCVEC's 6th errata ([source](https://www.ncvec.org/index.php/2023-2027-general-question-pool-release), public domain) |

Every possible question and answer is published, and this guide covers all of them.

## Study Materials

Each section has a narrative study guide, a question bank (every question with the correct answer and an explanation), and an MP3 of each.

| Section | Topic | Study guide | Question bank | Audio (guide + questions) | Exam Qs | Pool |
|---|---|---|---|---|:-:|:-:|
| G1 | Commission's Rules | [guide](subelements/G1-commission-rules.md) | [questions](subelements/G1-commission-rules-questions.md) | [21 min](subelements/G1-commission-rules.mp3) + [56 min](subelements/G1-commission-rules-questions.mp3) | 5 | 52 |
| G2 | Operating Procedures | [guide](subelements/G2-operating-procedures.md) | [questions](subelements/G2-operating-procedures-questions.md) | [18 min](subelements/G2-operating-procedures.mp3) + [59 min](subelements/G2-operating-procedures-questions.mp3) | 5 | 60 |
| G3 | Radio Wave Propagation | [guide](subelements/G3-radio-wave-propagation.md) | [questions](subelements/G3-radio-wave-propagation-questions.md) | [17 min](subelements/G3-radio-wave-propagation.mp3) + [39 min](subelements/G3-radio-wave-propagation-questions.mp3) | 3 | 37 |
| G4 | Amateur Radio Practices | [guide](subelements/G4-amateur-practices.md) | [questions](subelements/G4-amateur-practices-questions.md) | [18 min](subelements/G4-amateur-practices.mp3) + [63 min](subelements/G4-amateur-practices-questions.mp3) | 5 | 60 |
| G5 | Electrical Principles | [guide](subelements/G5-electrical-principles.md) | [questions](subelements/G5-electrical-principles-questions.md) | [20 min](subelements/G5-electrical-principles.mp3) + [30 min](subelements/G5-electrical-principles-questions.mp3) | 3 | 40 |
| G6 | Circuit Components | [guide](subelements/G6-circuit-components.md) | [questions](subelements/G6-circuit-components-questions.md) | [16 min](subelements/G6-circuit-components.mp3) + [20 min](subelements/G6-circuit-components-questions.mp3) | 2 | 23 |
| G7 | Practical Circuits | [guide](subelements/G7-practical-circuits.md) | [questions](subelements/G7-practical-circuits-questions.md) | [23 min](subelements/G7-practical-circuits.mp3) + [34 min](subelements/G7-practical-circuits-questions.mp3) | 3 | 38 |
| G8 | Signals and Emissions | [guide](subelements/G8-signals-emissions.md) | [questions](subelements/G8-signals-emissions-questions.md) | [19 min](subelements/G8-signals-emissions.mp3) + [44 min](subelements/G8-signals-emissions-questions.mp3) | 3 | 42 |
| G9 | Antennas and Feed Lines | [guide](subelements/G9-antennas-feedlines.md) | [questions](subelements/G9-antennas-feedlines-questions.md) | [21 min](subelements/G9-antennas-feedlines.mp3) + [50 min](subelements/G9-antennas-feedlines-questions.mp3) | 4 | 46 |
| G0 | Electrical and RF Safety | [guide](subelements/G0-safety.md) | [questions](subelements/G0-safety-questions.md) | [14 min](subelements/G0-safety.mp3) + [28 min](subelements/G0-safety-questions.mp3) | 2 | 25 |
| | **Total** | | | **10h 8m** | **35** | **423** |

Also included:

- **[Cram Sheet](CRAM-SHEET.md)** ([audio](CRAM-SHEET.mp3), 8 min): key facts, formulas, frequencies, and power limits on one page. Read it the morning of the exam.
- **[Technician Refresher](TECHNICIAN-BRIDGE.md)** ([audio](TECHNICIAN-BRIDGE.mp3), 4 min): the Technician concepts the General exam builds on.
- **[Glossary](GLOSSARY.md)**: 100+ terms with definitions and section references.
- **[Study Plan](STUDY-PLAN.md)**: a 7-day schedule.

## How to Study

1. Read each study guide (or listen to it), then drill its question bank.
2. Follow the [7-day plan](STUDY-PLAN.md): rules and safety (G1, G0), operating (G2), propagation (G3), practices (G4), theory and components (G5, G6), then circuits, signals, and antennas (G7, G8, G9). Spend the last day on the cram sheet and practice exams.
3. Take practice exams every session, in the app or from the command line:

   ```bash
   python3 scripts/practice-test.py          # one question per group, like the real exam
   python3 scripts/practice-test.py --drill  # 35 random questions from the whole pool
   ```

Tips: learn your privileges (G1) first, don't skip the G5 math (Ohm's Law, power, reactance), and use the app's formula button for a quick reference.

## Maintaining

**New question pool:** download it from [NCVEC](https://ncvec.org/index.php/amateur-question-pools), parse it into `pools/YYYY-YYYY/questions.json` with `scripts/parse-pool.py`, regenerate the question banks with `scripts/gen-question-files.py`, update the pool path in `scripts/practice-test.py` and the app, update the dates here, and regenerate the audio.

**Audio:** generated with a self-hosted [Open Speech](https://github.com/jeremy-windsor/open-speech) server, voice "will" (`am_puck(1)+am_liam(1)+am_onyx(0.5)` at 1.1× speed), as MP3. Text is prepared following the narration rules and vocabulary in [`tts/pronunciation.txt`](tts/pronunciation.txt). The cram sheet audio is read from [`tts/CRAM-SHEET-audio.md`](tts/CRAM-SHEET-audio.md), so keep it in agreement with `CRAM-SHEET.md`.

## License

Question pool content is public domain (NCVEC). Study guide explanations and scripts are MIT licensed.
