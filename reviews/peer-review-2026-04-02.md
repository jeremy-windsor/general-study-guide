# Peer Review — General Class Study Guide Scaffold
**Reviewer:** Senior Ham Radio Operator & Technical Writer (AI Agent)  
**Date:** April 2, 2026  
**Scope:** All files in `/home/claude/repos/general-study-guide/`  
**Methodology:** Full read of all content, cross-referenced against FCC Part 97.301(d) (current as of Jan 2026 amendment), ARRL band plan, and NCVEC 2023-2027 General pool structure.

---

## Overall Grade: C-

**Verdict:** The scaffold has good bones — clean organization, logical study progression, solid electrical/electronics theory, and thoughtful features like TTS pronunciation guides and audio study aids. However, the frequency privilege tables contain **dangerous errors that could lead to FCC violations**, the question banks are completely empty despite the README claiming "~456 real exam questions with correct answers," and several important General class topics are missing entirely. The structural foundation is B+ work undermined by D-level accuracy in the most critical content.

---

## 🔴 CRITICAL — Technical Accuracy Errors

### CRIT-1: Wrong 20m Phone Lower Edge (14.175 vs 14.225 MHz)
**Files:** `CRAM-SHEET.md` line 10, `subelements/G1-commission-rules.md` line 56  
**Severity:** 🔴 DANGEROUS — Could cause FCC violations

The guide lists the General class 20m lower phone edge as **14.175 MHz**. This is **wrong**. Per FCC §97.301(d):

| Class | 20m Phone Segment |
|-------|-------------------|
| **General** | **14.225–14.350 MHz** |
| Advanced | 14.175–14.350 MHz |
| Extra | 14.150–14.350 MHz |

**14.175 MHz is the Advanced class privilege**, not General. A General class operator transmitting phone between 14.175 and 14.224 MHz would be operating outside their authorized frequency range — a Part 97 violation. This is the single most dangerous error in the entire guide.

### CRIT-2: Frequency Tables Inconsistently Mix Full-Band and Phone-Only Allocations
**Files:** `CRAM-SHEET.md` lines 5-15, `subelements/G1-commission-rules.md` lines 48-58  
**Severity:** 🔴 Misleading — Implies incomplete privileges

The "HF Privileges (General)" table is labeled as "Frequency Range" and "General Privileges" but inconsistently shows:
- **160m**: Full band (1.800–2.000) — includes CW, digital, and phone ✓
- **80m/75m**: Phone only (3.800–4.000) — missing 3.525–3.600 CW/digital segment
- **40m**: Phone only (7.175–7.300) — missing 7.025–7.125 CW/digital segment
- **30m**: Full band (10.100–10.150) — CW/data only, no phone at all
- **20m**: Wrong phone edge (see CRIT-1) — missing 14.025–14.150 CW/digital segment
- **17m**: Phone only (18.110–18.168) — missing 18.068–18.110 CW/digital segment
- **15m**: Phone only (21.275–21.450) — missing 21.025–21.200 CW/digital segment
- **12m**: Phone only (24.930–24.990) — missing 24.890–24.930 CW/digital segment
- **10m**: Phone only (28.300–29.700) — missing 28.000–28.300 CW/digital segment

Without labeling this as "Phone Sub-bands," students will believe these are their **complete** General class privileges. They'd have no idea they can do CW on 80m at 3.525 MHz, digital on 40m at 7.040 MHz, or CW on 10m at 28.050 MHz.

**Fix:** Either (a) show both CW/digital and phone sub-bands per band, or (b) clearly label as "Phone Privileges" and add a second "CW/Digital Privileges" table.

### CRIT-3: "No HF Privileges" for Technician Is Factually Wrong
**File:** `subelements/G1-commission-rules.md` line 38  
**Severity:** 🔴 Factually incorrect

The Technician vs. General comparison table states: "No HF privileges" for Technician.

Per FCC §97.301(e), Technician class has:
- **80m:** 3.525–3.600 MHz (CW)
- **40m:** 7.025–7.125 MHz (CW)
- **15m:** 21.025–21.200 MHz (CW)
- **10m:** 28.0–28.5 MHz (CW, data, phone)

These are limited but real HF privileges. Telling a Technician they have "no HF" could cause them to miss operating opportunities or misunderstand their existing license. The correct framing is "Limited HF (CW only on 80/40/15m, CW/data/phone on 10m below 28.5 MHz)."

---

## 🟠 MAJOR — Incorrect or Missing Content

### MAJ-1: 60m Band Completely Missing
**Files:** All frequency tables (CRAM-SHEET.md, G1-commission-rules.md)  
**Severity:** 🟠 Missing testable content

General class has 60m privileges: 5.3515–5.3665 MHz plus four channelized frequencies (5330.5, 5346.5, 5371.5, 5403.5 kHz). Max 100W PEP ERP (9.15W ERP on the continuous segment). USB phone and CW/RTTY/data. This band is tested on the General exam and is entirely absent from the guide.

### MAJ-2: 630m and 2200m Bands Missing
**Files:** All frequency tables  
**Severity:** 🟠 Incomplete coverage

Per §97.301(d), General class has privileges on:
- **2200m:** 135.7–137.8 kHz (1W EIRP)
- **630m:** 472–479 kHz (5W EIRP)

Both require UTC notification to the PLC database. These appear in the exam pool.

### MAJ-3: G1B Topic Description Is Wrong
**File:** `subelements/G1-commission-rules.md` line 17  
**Severity:** 🟠 Content misalignment

The guide describes G1B as "Station Identification — Call sign requirements on HF, Self-assigned indicators (portable, mobile), Vanity calls and 1x2, 2x1 formats."

The actual NCVEC G1B topic is: "Antenna structure limitations; good engineering and good amateur practice; beacon operation; prohibited transmissions; retransmitting radio signals."

Station identification is not the primary G1B topic. This misalignment means the study guide content doesn't prepare students for the actual G1B questions.

### MAJ-4: G1E Topic Description Is Incomplete
**File:** `subelements/G1-commission-rules.md` line 26  
**Severity:** 🟠 Content misalignment

Described as "Controlled Operations — MARS, RACES, Emergency communications." The actual G1E covers: "Control categories; repeater regulations; auxiliary stations; remotely controlled stations; automatic control in certain bands." MARS and RACES are part of it, but the control categories and repeater/auxiliary station rules are the primary content.

### MAJ-5: G6 Has Wrong Number of Groups
**File:** `subelements/G6-electronic-components.md` lines 15-24  
**Severity:** 🟠 Structural error

The study guide creates three subsections (G6A, G6B, G6C) but the official pool only has **two groups** (G6A and G6B). The fabricated "G6C — Transistors and Amplifiers" doesn't correspond to any exam group. The actual pool structure:
- **G6A:** Resistors; capacitors; inductors; rectifiers; solid-state diodes and transistors; vacuum tubes; batteries
- **G6B:** Analog and digital integrated circuits; microprocessors; memory; I/O devices; MMICs; display devices; connectors; ferrite cores

Transistors and amplifier classes belong under G6A, not a nonexistent G6C.

### MAJ-6: Question Banks Are All Empty Placeholders
**Files:** All 10 `*-questions.md` files  
**Severity:** 🟠 Feature gap (mitigated by README status note)

Every question bank file is a placeholder with zero actual exam questions. The `questions.json` has an empty `"questions": []` array. While this is noted as "Status: Placeholder" in each file, the main README claims "~456 real exam questions with correct answers" without qualification. Either populate the questions or fix the README claim.

### MAJ-7: 80m Calling Frequency Listed as SSB but Is Actually AM
**File:** `subelements/G2-operating-procedures.md` line 56  
**Severity:** 🟠 Wrong mode attribution

The table "HF Calling Frequencies" lists 3.885 MHz as the "SSB Calling Frequency" for 80m. Per ARRL band plan, **3.885 MHz is the AM calling frequency** on 80m. SSB activity on 80m is typically around 3.850–3.860 MHz. Using 3.885 for SSB would put you in the AM window.

### MAJ-8: Broken Link in README
**File:** `README.md` line 31  
**Severity:** 🟠 Broken navigation

Day 2 links to `G7-circuit-types.md` but the actual file is `G7-practical-circuits.md`. Anyone following the 7-day plan would hit a 404 on Day 2.

### MAJ-9: "71.9 kHz: Maritime Distress" in Emergency Frequencies
**File:** `CRAM-SHEET.md` line 67  
**Severity:** 🟠 Dubious/incorrect

71.9 kHz is not a standard maritime distress frequency. Maritime distress frequencies are:
- **2182 kHz** — International maritime distress and calling (MF)
- **156.8 MHz** — VHF Channel 16 (distress, safety, calling)
- **500 kHz** — Historical maritime CW distress (discontinued 1999)

This entry appears fabricated or confused with another frequency. Including incorrect emergency frequencies in a study guide is particularly irresponsible.

---

## 🟡 MODERATE — Gaps and Inaccuracies

### MOD-1: Missing Smith Chart Coverage
**File:** `STUDY-PLAN.md` line 17 mentions Smith charts; no study guide covers them  
**Severity:** 🟡 Promised but not delivered

Smith charts are mentioned in the Day 3 focus area ("Dipoles, Yagis, SWR, impedance matching, Smith charts") but no study guide actually explains Smith chart reading or usage. There are General pool questions about Smith charts.

### MOD-2: Volunteer Monitor Program Not Covered
**Severity:** 🟡 Missing testable topic

The Volunteer Monitor (VM) program replaced the Official Observer program and appears in the G2 exam questions. It's not mentioned anywhere in the study guide.

### MOD-3: Third-Party Traffic Rules Not Covered
**Severity:** 🟡 Missing testable topic

Third-party traffic rules, including which countries allow third-party messages and the requirements for third-party communications, are testable General pool topics not addressed in the guides.

### MOD-4: International Operating (CEPT/IARP) Barely Covered
**File:** `subelements/G1-commission-rules.md` line 43  
**Severity:** 🟡 Underdeveloped

CEPT and IARP licensing are mentioned in passing ("CEPT agreements affect operating in Europe") but not explained. General class students need to know what a CEPT license allows, how IARP works, and the limitations of international operation.

### MOD-5: Antenna Tuner Description Oversimplified
**File:** `subelements/G4-amateur-practices.md` line 34  
**Severity:** 🟡 Technically incomplete

"An antenna tuner doesn't 'tune' the antenna — it transforms the impedance at the feed point." This is a common but slightly misleading simplification. The tuner transforms impedance **at the radio end of the feed line**, not at the antenna feed point. The mismatch still exists on the feed line between the tuner and the antenna. This distinction matters because feed line losses increase with high SWR even when the tuner makes the radio see 50Ω.

### MOD-6: Pool Size Should Account for Withdrawn Questions
**Files:** `README.md`, `STUDY-PLAN.md`, `pools/2023-2027/README.md`  
**Severity:** 🟡 Inconsistent

The guide consistently says "~456 questions" but 9 have been withdrawn, making the active pool ~447. The guide itself documents all 9 withdrawals but doesn't update the totals.

### MOD-7: Referenced Features/Files Don't Exist
**Files:** `README.md`, `REPO-STRUCTURE.md`  
**Severity:** 🟡 Broken references

- `scripts/practice-test.py` — Referenced in README and STUDY-PLAN.md, doesn't exist
- `scripts/` directory — Doesn't exist
- `apps/` directory — Referenced in REPO-STRUCTURE.md, doesn't exist
- `figures/` directory — Referenced in REPO-STRUCTURE.md, doesn't exist
- `reports/` directory — Referenced in REPO-STRUCTURE.md, doesn't exist
- All `.mp3` audio files — Referenced with "TBD" duration, none exist

### MOD-8: RTTY Bandwidth Conflates Shift and Bandwidth
**File:** `subelements/G2-operating-procedures.md` line 33  
**Severity:** 🟡 Imprecise

RTTY bandwidth listed as "170-250 Hz." The 170 Hz is the standard frequency shift, not the bandwidth. The occupied bandwidth of a standard 45.45 baud, 170 Hz shift RTTY signal is approximately 250–350 Hz. Listing "170-250 Hz" conflates two different parameters.

---

## 🟢 MINOR — Formatting, Typos, Polish

### MIN-1: Pool Group Count Inconsistency
**File:** `pools/2023-2027/README.md` line 24  
The "Groups" column totals to 35 (matching exam questions drawn), but the label "Groups" should count question groups within subelements, not exam questions. The numbers happen to be the same (35 groups, 35 exam questions) but the table structure is misleading.

### MIN-2: G4 Study Guide Is Thin
**File:** `subelements/G4-amateur-practices.md`  
Only covers station setup and measurement. Missing topics tested in the actual G4 pool:
- Audio filtering and processing
- RF interference (RFI) troubleshooting
- Two-tone testing
- Proper grounding techniques for RFI reduction

### MIN-3: G0 Section Numbering vs. Subelement Order
The guide uses G0 as the last section (matching the subelement numbering) but some students expect it to follow G9 numerically. The study plan handles this correctly by placing G0 on Day 7. No fix needed, just noting it.

### MIN-4: Emergency Frequency Section Out of Scope
**File:** `CRAM-SHEET.md` lines 65-70  
The emergency frequencies listed (121.5 MHz aviation, 243 MHz military, 406 MHz COSPAS-SARSAT) are general knowledge, not tested on the General exam. Including them isn't wrong, but they take cram sheet space from actually tested material.

### MIN-5: Amplifier Efficiency Ranges Vary Between Files
**Files:** `CRAM-SHEET.md` line 45 vs `subelements/G6-electronic-components.md` line 40  
- Cram sheet: Class A ~25%
- G6 guide: Class A 25-30%
- These are both within acceptable ranges but should be consistent.

### MIN-6: Missing .gitignore for Generated Content
**File:** `.gitignore`  
The `.gitignore` excludes `.DS_Store`, `__pycache__`, `.env`, and `node_modules/` but doesn't exclude generated MP3 files, build artifacts, or temporary files that the TTS pipeline or practice test would create.

---

## Comparison to Technician Level — Appropriate Advancement?

**Grade: B-**

The guide does a reasonable job of stepping up from Technician concepts:
- Electrical theory (G5) goes deeper into reactance, impedance, and resonance — appropriate
- Electronic components (G6) adds semiconductor physics and amplifier classes — good progression
- Propagation (G3) is almost entirely new for General — well handled
- Operating procedures (G2) correctly focuses on HF operation, DX, and digital modes

**However:**
- The Technician comparison table in G1 is factually wrong (see CRIT-3)
- The guide doesn't build on Technician VHF/UHF knowledge — it treats HF as if Technician students know nothing about radio at all
- Several topics that bridge Technician and General (like repeater operation expanding to HF, or extending digital mode knowledge) are not connected

---

## What's Done Well

1. **Repository structure** — Clean, logical, easy to navigate
2. **Study plan progression** — Theory → Circuits → Antennas → Propagation → Operating → Rules → Safety is a smart order
3. **TTS pronunciation guide** — Thoughtful addition for audio study (ionosphere → "EYE-on-oh-sfear")
4. **Reactance/impedance/resonance formulas** — All correct and clearly presented
5. **Superheterodyne receiver explanation** — Good block diagram, clear mixer/IF explanation
6. **Antenna section** — Dipole formula, feed line table, Yagi description all solid
7. **Safety section** — Comprehensive coverage of grounding, lightning, RF exposure
8. **Errata tracking** — Properly documents all 9 withdrawn questions with dates
9. **Cram sheet concept** — Right idea, would be very useful if accuracy issues were fixed
10. **Dual-file approach** (narrative guide + question bank) — Excellent pedagogy

---

## Summary of Issues by Severity

| Severity | Count | Description |
|----------|-------|-------------|
| 🔴 Critical | 3 | Wrong 20m frequency, missing CW/digital bands, wrong Technician comparison |
| 🟠 Major | 9 | Missing bands (60m, 630m, 2200m), wrong topics, empty question banks, broken link |
| 🟡 Moderate | 8 | Missing topics (Smith chart, VM program, CEPT), imprecise technical descriptions |
| 🟢 Minor | 6 | Thin content, formatting inconsistencies, out-of-scope material |
| **Total** | **26** | |

---

## Recommended Priority Fixes

1. **IMMEDIATE:** Fix 20m phone edge from 14.175 to 14.225 MHz (CRIT-1)
2. **IMMEDIATE:** Add CW/digital sub-bands to all frequency tables or clearly label as phone-only (CRIT-2)
3. **HIGH:** Fix Technician comparison to acknowledge limited HF privileges (CRIT-3)
4. **HIGH:** Add 60m band to frequency tables and study content (MAJ-1)
5. **HIGH:** Fix G1B and G1E topic descriptions to match actual pool content (MAJ-3, MAJ-4)
6. **HIGH:** Fix broken G7 link in README (MAJ-8)
7. **HIGH:** Remove or correct "71.9 kHz: Maritime distress" (MAJ-9)
8. **MEDIUM:** Fix G6 group structure to match official 2-group layout (MAJ-5)
9. **MEDIUM:** Correct 80m calling frequency attribution (AM, not SSB) (MAJ-7)
10. **MEDIUM:** Populate question banks or remove the "~456 real exam questions" claim (MAJ-6)

---

## Final Assessment

This is a well-structured scaffold that needs a serious accuracy pass before anyone should study from it. The organizational thinking is sound — dual narrative/question-bank files, a logical 7-day progression, TTS support, errata tracking. The electrical theory and circuit content is mostly correct.

But the frequency tables are the heart of a General class study guide, and they have critical errors. A student who memorizes "I can do phone on 20m starting at 14.175" would be transmitting in the Advanced/Extra sub-band — a real FCC violation. The missing CW/digital sub-bands mean students would think they have far fewer privileges than they actually do.

Fix the frequency tables, populate the question banks, and this becomes a solid B+ study guide. As-is, it's a C- scaffold with some dangerous landmines.

---

*Review generated by AI peer reviewer. Cross-referenced against FCC Part 97.301(d) as amended January 14, 2026, and ARRL band plan. All frequency claims verified against official regulatory sources.*
