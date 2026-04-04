# Adversarial Review — General Class Study Guide

**Date:** 2026-04-02  
**Reviewer:** Will (adversarial subagent)  
**Verdict:** Structurally sound skeleton. Would absolutely NOT pass a student in current state.  
**Overall Grade: D**

---

## Executive Summary

The study guide has a well-organized structure, clear writing style, and covers concepts at an appropriate conceptual level. However, it contains **zero actual exam questions** (despite claiming ~456), has **factually incorrect frequency allocations** that would cause wrong answers on the exam, and is missing an entire band (60m). The narrative study guides are a solid B+ in isolation, but the product as a whole is a dressed-up skeleton selling itself as a finished house.

---

## CRITICAL — Would Cause Exam Failure

### 🔴 C1. ALL Question Banks Are Empty Placeholders (ALL *-questions.md files)

Every single question bank file contains only section headers and a "⚠️ Status: Placeholder" warning. There are **zero actual exam questions** in the entire repository. The README claims:

> **~456 real exam questions** with correct answers

and:

> every possible question and answer is published

This is false. A student relying solely on this material would have **no question-level practice** and would almost certainly fail.

**Files affected:** All 10 `*-questions.md` files  
**Severity:** CRITICAL — this alone makes the guide non-functional for exam prep

---

### 🔴 C2. 20m Phone Frequency Is WRONG (CRAM-SHEET.md, G1-commission-rules.md)

The guide consistently lists General class 20m phone privileges as:

> **20m | 14.175-14.350 MHz**

The correct General class 20m phone allocation is:

> **20m | 14.225-14.350 MHz**

Verified against FCC Part 97 and multiple ARRL band charts. The guide gives an extra 50 kHz of phantom privileges. A student who answers "14.175 MHz" on a band-edge question **will get it wrong**.

**Files affected:**
- `CRAM-SHEET.md` — HF Privileges table
- `subelements/G1-commission-rules.md` — Quick Reference table
- `README.md` — implicitly references G1 content

**Severity:** CRITICAL — direct wrong answer on exam questions

---

### 🔴 C3. CW/Data Allocations Completely Omitted (G1-commission-rules.md, CRAM-SHEET.md)

The band privilege tables ONLY show phone allocations but present them as complete "General Privileges." Missing allocations include:

| Band | Missing CW/Data Allocation |
|------|---------------------------|
| 80m | 3.525-3.600 MHz CW/Data |
| 40m | 7.025-7.125 MHz CW/Data |
| 20m | 14.025-14.150 MHz CW/Data |
| 15m | 21.025-21.200 MHz CW/Data |
| 12m | 24.890-24.930 MHz CW/Data |

The exam frequently asks about CW and data mode frequency allocations. A student who only sees the phone ranges will miss these questions.

**Files affected:**
- `subelements/G1-commission-rules.md` — Quick Reference table
- `CRAM-SHEET.md` — HF Privileges table

**Severity:** CRITICAL — multiple exam questions cover CW/data allocations

---

### 🔴 C4. 60m Band Completely Missing (ALL files)

The 60-meter band (5 MHz) is never mentioned anywhere in the study guide. General class operators have 60m privileges — four channels plus a 15 kHz segment at 100W PEP ERP (expanded in February 2026 FCC R&O). Multiple exam questions cover 60m operation, power limits, and channelized operation.

The G1 guide even acknowledges this exists with a parenthetical "(with some 60m restrictions)" in the Technician comparison table, but then never actually covers it.

**Files affected:** All files — complete omission  
**Severity:** CRITICAL — 60m questions will be unanswerable

---

### 🔴 C5. No Diagrams or Figures (figures/ directory empty)

The NCVEC question pool includes circuit diagrams that are directly referenced in exam questions (e.g., "Refer to Figure G7-1"). Without these figures, students cannot answer figure-based questions at all.

**Files affected:** `figures/` directory is empty per REPO-STRUCTURE.md  
**Severity:** CRITICAL — figure questions are unanswerable without the images

---

## MAJOR — Factual Errors and Contradictions

### 🟠 M1. Self-Contradicting Technician Comparison Table (G1-commission-rules.md)

The "Key Distinctions from Technician" table contains two contradictory claims:

```
| Technician | General |
|------------|---------|
| No HF privileges | Full HF privileges (with some 60m restrictions) |
| 200W PEP max on HF | 1500W PEP on most HF bands |
```

- Row 1 says Technicians have "**No HF privileges**"
- Row 2 says Technicians have "**200W PEP max on HF**"

Both are wrong, and they contradict each other. Technicians actually have:
- 80m: 3.525-3.600 MHz CW/Data, 200W PEP
- 40m: 7.025-7.125 MHz CW/Data, 200W PEP  
- 15m: 21.025-21.200 MHz CW/Data, 200W PEP
- 10m: 28.000-28.500 MHz all modes, 200W PEP

**File:** `subelements/G1-commission-rules.md` — Key Distinctions table  
**Severity:** MAJOR — misleading, contradictory, partially wrong

---

### 🟠 M2. Broken Link in README (README.md)

The Day 2 study plan links to a non-existent file:

```markdown
[G7](subelements/G7-circuit-types.md)
```

The actual file is `subelements/G7-practical-circuits.md`. This 404s and breaks navigation.

**File:** `README.md` — Quick Path table, Day 2  
**Severity:** MAJOR — broken user experience

---

### 🟠 M3. Exam Fee Is Incomplete/Outdated (README.md)

The guide states:

> **Fee** | $35 (ARRL VEC)

Since April 19, 2022, the FCC also charges a **$35 application fee** for new licenses and upgrades. The total cost for a General upgrade is potentially **$50-70** depending on VEC (some VECs charge $0-15, ARRL charges $15). The guide's "$35 (ARRL VEC)" figure is misleading.

**File:** `README.md` — The Exam table  
**Severity:** MAJOR — students may show up with the wrong amount of money

---

### 🟠 M4. Suspect Emergency Frequency (CRAM-SHEET.md)

The CRAM-SHEET lists:

> **71.9 kHz:** Maritime distress

71.9 kHz is not a recognized international maritime distress frequency. Standard maritime distress frequencies are:
- **2182 kHz** — HF maritime distress and calling
- **156.8 MHz** — VHF Channel 16 maritime distress
- **500 kHz** — CW distress/calling (now discontinued)

This appears to be fabricated or confused with another frequency. Additionally, the entire "Emergency Frequencies" section lists non-amateur frequencies that are not typically tested on the General exam.

**File:** `CRAM-SHEET.md` — Emergency Frequencies section  
**Severity:** MAJOR — potentially misleading information

---

### 🟠 M5. Practice Test Script Does Not Exist (scripts/)

The README instructs students to:

```bash
python3 scripts/practice-test.py
```

This script does not exist. The REPO-STRUCTURE.md confirms it's "TBD." Combined with empty question banks, there is literally no way to practice.

**File:** `README.md`, `scripts/` directory  
**Severity:** MAJOR — advertised feature doesn't exist

---

## MODERATE — Incomplete or Misleading Content

### 🟡 D1. MUF Formula Oversimplified (G3, CRAM-SHEET.md)

Both state:

> MUF ≈ 3-4 × critical frequency

The actual relationship is MUF = critical frequency × sec(θ), where θ is the angle of incidence. The "3-4×" approximation is only valid for specific path geometries. The exam may ask about the actual relationship. At minimum, the guide should explain this is an approximation for typical DX paths.

**Files:** `subelements/G3-radio-wave-propagation.md`, `CRAM-SHEET.md`  
**Severity:** MODERATE

---

### 🟡 D2. Smith Charts Mentioned but Never Explained (G9-antennas-feedlines.md)

The G9 overview mentions "Smith charts" in the focus areas:

> **Focus:** Dipoles, Yagis, SWR, impedance matching, Smith charts

But the guide never actually explains Smith charts. If a student encounters a Smith chart question, they're on their own.

**File:** `STUDY-PLAN.md` — Day 3, `subelements/G9-antennas-feedlines.md`  
**Severity:** MODERATE

---

### 🟡 D3. Audio Files All "TBD" (README.md)

The README has an audio section showing TBD for all durations. The study plan says "Use the audio" as tip #3. Students can't use what doesn't exist.

**File:** `README.md` — Audio Study Guide table  
**Severity:** MODERATE — advertised feature doesn't exist

---

### 🟡 D4. 17m Privileges Start Frequency May Be Wrong (G1, CRAM-SHEET.md)

The guide shows:

> **17m | 18.110-18.168 MHz | 1500W PEP**

Per the ARRL band plan, General class has two allocations on 17m:
- 18.068-18.110 MHz: CW/Data
- 18.110-18.168 MHz: CW/Phone/Image

The 18.068 MHz CW/Data start is omitted (same CW/Data omission pattern as C3).

**Files:** `CRAM-SHEET.md`, `subelements/G1-commission-rules.md`  
**Severity:** MODERATE — part of the C3 pattern

---

### 🟡 D5. G4 Subelement May Be Structurally Incomplete (G4-amateur-practices.md)

The G4 study guide covers only two topic groups (G4A, G4B). The official NCVEC pool for the 2019-2023 cycle had groups G4A through G4E. While the pools metadata says "2 groups," the actual pool structure should be verified. Topics like interference, digital station setup, and test equipment may be under-covered.

**File:** `subelements/G4-amateur-practices.md`  
**Severity:** MODERATE — needs verification

---

### 🟡 D6. Amplifier Class Efficiency Inconsistency (CRAM-SHEET vs G6)

| Source | Class A | Class B |
|--------|---------|---------|
| CRAM-SHEET | ~25% | ~60% |
| G6 study guide | ~25-30% | ~50-60% |
| G6 question bank | 25-30% | 50-60% |

Minor inconsistency, but any discrepancy in a cram sheet vs study guide creates uncertainty.

**Files:** `CRAM-SHEET.md`, `subelements/G6-electronic-components.md`  
**Severity:** LOW-MODERATE

---

## MINOR — Stylistic and Structural Issues

### 🟢 N1. No Prerequisite Knowledge Bridge

The guide assumes Technician-level knowledge but never reviews it. Topics like Ohm's Law, basic circuit concepts, and VHF/UHF operation from the Tech exam are assumed. A brief "What You Should Already Know" section would help.

### 🟢 N2. Study Plan Day 1 Is Overloaded

Day 1 assigns G5 (~35 questions) + G6 (~26 questions) = 61 questions of technical material. Day 3 is only G9 (~39 questions). Better balancing would improve the study experience.

### 🟢 N3. No Mnemonics or Memory Aids

The guide is purely factual. Ham radio exam prep traditionally includes mnemonics (e.g., "468 over frequency" for dipoles). Adding memory devices would significantly aid retention.

### 🟢 N4. No Cross-References Between Subelements

The subelements are siloed. Concepts that span topics (e.g., impedance appears in G5, G9, and G4) are never cross-linked.

### 🟢 N5. Pronunciation Guide Is Nice but Low Priority

`tts/pronunciation.md` is well-done but is a luxury feature on a guide that's missing its core content.

---

## Scoring Rubric

| Category | Grade | Notes |
|----------|-------|-------|
| **Structure/Organization** | A- | Excellent repo layout, clear navigation, logical study order |
| **Narrative Quality** | B+ | Good explanations, appropriate depth, readable |
| **Factual Accuracy** | D | 20m frequency wrong, CW/data omissions, Tech claims wrong |
| **Question Coverage** | F | Zero questions out of ~456 claimed |
| **Completeness** | D- | 60m missing, CW/Data missing, no figures, no practice test |
| **Would Pass the Exam** | F | No question practice = no exam readiness |
| **VE Confidence** | D+ | A VE would flag the frequency errors immediately |
| **CCIE Technical Depth** | B | Concepts are correctly explained; formulas are right |
| **Copy-Paste Safety** | C+ | Wrong frequencies could cause out-of-band operation |

---

## Answer to Review Questions

### 1. Would a student pass studying ONLY this material?
**No.** Zero exam questions means zero active recall practice. The 20m frequency error would cause wrong answers. Missing 60m content means at least 1-2 questions are unanswerable. Missing CW/Data allocations could cost 2-3 more. Missing figures could cost 1-2 more. That's 5-7 questions at risk on a 35-question exam needing 26 to pass. Combined with no practice testing, this is a fail.

### 2. Are there contradictions between subelements?
**Yes.** The G1 Technician comparison table contradicts itself ("No HF privileges" vs "200W PEP max on HF"). Amplifier efficiency numbers vary slightly between CRAM-SHEET and G6.

### 3. Are there formulas or facts that would mislead?
**Yes.** The 20m phone allocation (14.175 instead of 14.225) would mislead students. The MUF "3-4×" simplification could mislead on detailed questions. The emergency frequency 71.9 kHz appears fabricated.

### 4. Is the difficulty ramp appropriate?
**Yes, mostly.** The 7-day plan progression from theory → circuits → antennas → propagation → operating → rules → safety is logical and well-paced. Day 1 is slightly overloaded.

### 5. What would a VE call wrong?
Band-edge frequencies (20m especially), missing CW/Data allocations, missing 60m, wrong Technician HF claims, and the self-contradicting table.

### 6. What would a CCIE say about technical depth?
The technical explanations are solid. Formulas are correct. The superheterodyne receiver explanation is clear. Reactance/impedance coverage is good. A CCIE would approve the conceptual depth but note the missing operational details (no protocol-level FT8/WSJT-X coverage, no APRS details, no SDR discussion).

### 7. Could this content be copy-pasted and cause harm?
**Yes.** A student using the 20m frequency table could transmit at 14.175 MHz SSB, which is in the Extra-class-only portion of 20m. This would be an FCC violation. The missing CW/Data allocations, while less dangerous (omission rather than error), could cause confusion about where CW operation is permitted.

### 8. What's incomplete that looks complete?
The question bank files look structured and organized with headers, withdrawn question lists, and study tips — but contain **zero actual questions**. A casual reader might think they're complete. Similarly, the README and STUDY-PLAN present the guide as ready for use when it's fundamentally a skeleton.

---

## Priority Fix List

| Priority | Issue | Fix |
|----------|-------|-----|
| P0 | Populate all 10 question banks (~456 questions) | Source from NCVEC pool |
| P0 | Fix 20m phone frequency (14.225, not 14.175) | Update CRAM-SHEET + G1 |
| P0 | Add CW/Data allocations to all band tables | Update CRAM-SHEET + G1 |
| P0 | Add 60m band coverage | New section in G1 + CRAM-SHEET |
| P0 | Add pool figures/diagrams | Source from NCVEC PDF |
| P1 | Fix Technician comparison table | Remove contradictions, add actual Tech HF |
| P1 | Fix broken G7 link in README | G7-circuit-types.md → G7-practical-circuits.md |
| P1 | Update exam fee information | Add FCC $35 application fee |
| P1 | Remove or verify 71.9 kHz emergency frequency | Research or remove |
| P1 | Create practice test script | Implement scripts/practice-test.py |
| P2 | Add Smith chart explanation to G9 | At least basic coverage |
| P2 | Add mnemonics/memory aids | Throughout all subelements |
| P2 | Cross-reference related topics | Link between subelements |
| P3 | Generate audio files | TTS pipeline is scaffolded |
| P3 | Balance study plan day load | Redistribute Day 1 |

---

*Review conducted adversarially with the goal of finding every way this guide could fail a student. The structure is excellent — fix the content and this becomes a genuinely useful study resource.*
