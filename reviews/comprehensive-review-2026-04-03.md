# Comprehensive Review — General Class Ham Radio Study Guide

**Date:** 2026-04-03  
**Reviewer:** Forge (comprehensive audit subagent)  
**Pool cross-referenced:** `pools/2023-2027/questions.json` (429 questions, 10 subelements)  
**Previous reviews checked:** adversarial-review-2026-04-02.md, peer-review-2026-04-02.md  

---

## Overall Grade: B+

**Verdict:** This guide has been transformed from a skeleton (D grade yesterday) into a genuinely useful study resource. All 429 exam questions are covered with detailed explanations, all critical frequency errors are fixed, the narrative guides are well-written and teach concepts rather than just restate answers, and a fully functional PWA study app is deployed. The remaining issues are minor-to-moderate — missing Figure G7-1 images, an incomplete study plan, and some cram sheet refinements. A student using this guide could pass the exam.

---

## Previous Review Status

### Issues from April 2 Reviews — What's Fixed ✅

| Issue | Status | Notes |
|-------|--------|-------|
| **C1: All question banks empty** | ✅ FIXED | All 429/429 questions populated with detailed explanations |
| **C2: 20m phone frequency wrong (14.175)** | ✅ FIXED | Now correctly shows 14.225–14.350 MHz |
| **C3: CW/Data allocations missing** | ✅ FIXED | CRAM-SHEET now has separate CW/Data and Phone columns |
| **C4: 60m band completely missing** | ✅ FIXED | Full 60m coverage: 5 channels + 15 kHz segment, 100W ERP |
| **M1: Technician comparison contradictory** | ✅ FIXED | G1 now correctly states "a few slices of HF" for Techs |
| **M2: Broken G7 link in README** | ✅ FIXED | Link removed, README restructured |
| **M3: Exam fee incomplete** | ✅ FIXED | Now shows "~$15 VEC session fee + $35 FCC application fee" |
| **M4: 71.9 kHz maritime distress** | ✅ FIXED | Emergency frequencies section removed from CRAM-SHEET |
| **M5: Practice test script missing** | ⚠️ PARTIAL | No standalone practice test script, but PWA study app provides full practice exam functionality |
| **M7: 80m calling frequency wrong mode** | N/A | Could not locate the specific error in current G2 file |
| **M8: Broken G7 link** | ✅ FIXED | README restructured |
| **C5: No figures/diagrams** | ❌ STILL OPEN | No Figure G7-1 images — see below |
| **D2: Smith charts not covered** | ✅ NON-ISSUE | No Smith chart questions exist in the 2023-2027 pool |
| **D3: Audio files all TBD** | ✅ FIXED | All 20 MP3 files exist (10 narrative + 10 question files) |
| **MOD-1 (peer): 630m/2200m missing** | ✅ NON-ISSUE | No 630m/2200m questions in the pool |
| **MAJ-5 (peer): G6 wrong group count** | ✅ FIXED | G6 narrative correctly structured |
| **MAJ-3 (peer): G1B topic wrong** | ✅ FIXED | G1 topics properly aligned with pool |

### Issues Still Open ❌

| Issue | Severity | Details |
|-------|----------|---------|
| Figure G7-1 missing | MODERATE | 5 questions (G7A09-G7A13) reference Figure G7-1; no image exists. Explanations describe symbols well, partially compensating. |
| STUDY-PLAN.md is a placeholder | MODERATE | Only has a 7-row table. No detailed daily plan, tips, or study strategies. |
| No standalone practice test script | LOW | PWA covers this functionality; `scripts/practice-test.py` was never created but isn't needed |

---

## Per-Subelement Audit

### Question Coverage

| Subelement | Pool | Covered | Score | Grade |
|------------|------|---------|-------|-------|
| G0 — Electrical & RF Safety | 25 | 25 | 100% | A |
| G1 — Commission's Rules | 57 | 57 | 100% | A |
| G2 — Operating Procedures | 60 | 60 | 100% | A |
| G3 — Radio Wave Propagation | 37 | 37 | 100% | A |
| G4 — Amateur Radio Practices | 60 | 60 | 100% | A |
| G5 — Electrical Principles | 40 | 40 | 100% | A |
| G6 — Circuit Components | 23 | 23 | 100% | A |
| G7 — Practical Circuits | 38 | 38 | 100% | A |
| G8 — Signals and Emissions | 43 | 43 | 100% | A |
| G9 — Antennas and Feed Lines | 46 | 46 | 100% | A |
| **TOTAL** | **429** | **429** | **100%** | **A** |

### Answer Accuracy

**429/429 correct answers verified against pool.** Zero mismatches found. Every bolded answer in every question file matches the `correct` field in `questions.json`.

### Explanation Quality

| Metric | Value |
|--------|-------|
| Total explanations | 429 |
| Average length | 622 characters |
| Minimum length | 201 characters |
| Maximum length | 894 characters |
| Over 500 chars | 359 (84%) |
| Under 200 chars | 0 (0%) |
| Teaching indicators ("because", "think of", "remember", etc.) | 39.4% |

**Assessment:** Every explanation is substantive — no one-liners or answer restaters. The majority explain *why* the answer is correct and *why* the distractors are wrong. This is genuine teaching, not just answer keys.

### Narrative Study Guide Quality

| Subelement | Lines | Teaching Quality | Key Topics Covered | Cross-refs |
|------------|-------|-----------------|-------------------|------------|
| G0 — Safety | 199 | Good | RF exposure, MPE, GFCI, NEC, tower, lightning, grounding | None |
| G1 — Rules | 310 | Excellent | Frequencies, 60m, beacons, third-party, CEPT, VE, control ops | None |
| G2 — Operating | 345 | Excellent | USB/LSB, CQ DX, VOX, RACES, FT8, RTTY, Winlink, VM program | None |
| G3 — Propagation | 271 | Excellent | D/E/F layers, MUF, LUF, sunspots, K/A-index, NVIS, scatter, gray line | None |
| G4 — Practices | 296 | Excellent | Notch filter, noise blanker, oscilloscope, two-tone, ALC, S meter, mobile, solar | G2, G5, G9 |
| G5 — Electrical | 374 | Excellent | Reactance, impedance, resonance, RMS, PEP, transformer, dB, series/parallel | None |
| G6 — Components | 283 | Very Good | Diodes, MOSFET, BJT, vacuum tubes, ferrite, connectors, batteries | None |
| G7 — Circuits | 376 | Excellent | Rectifiers, amplifiers, oscillators, SSB gen, filters, SDR, I/Q | G5, G6 |
| G8 — Signals | 365 | Excellent | Modulation, FSK, PSK31, FT8, bandwidth, mixing, intermod, link budget | G5, G7 |
| G9 — Antennas | 400 | Excellent | Dipoles, Yagis, verticals, SWR, feed lines, NVIS, log-periodic, traps | G3, G5 |

**Assessment:** The narrative guides are genuinely well-written. They use analogies, real-world examples, and build concepts progressively. The later guides (G4, G7, G8, G9) appropriately reference earlier material. G5's formula explanations with worked examples are particularly strong.

### Per-Subelement Technical Accuracy

#### G0 — Electrical & RF Safety (25 questions, 2 on exam)
- ✅ RF exposure rules correctly explained (MPE, time averaging, evaluation methods)
- ✅ Grounding requirements correct
- ✅ Tower safety covered (lockout/tagout, safety harness)
- ✅ NEC coverage correct (20A → AWG 12, 15A → AWG 14)
- ⚠️ Narrative doesn't explicitly use the phrase "first aid" but covers electrical shock prevention
- **Grade: A-** (minor narrative gap, questions fully covered)

#### G1 — Commission's Rules (57 questions, 5 on exam)
- ✅ All band allocations verified correct against pool
- ✅ 20m phone edge correctly at 14.225 MHz
- ✅ CW/Data sub-bands all present
- ✅ 60m channels and power limits correct (100W ERP, 2.8 kHz BW)
- ✅ 30m power limit correct (200W PEP)
- ✅ Third-party traffic rules covered
- ✅ VE requirements correct (3 VEs, class restrictions)
- ✅ Control operator rules correct
- ✅ Beacon rules covered
- **Grade: A** (comprehensive and accurate)

#### G2 — Operating Procedures (60 questions, 5 on exam)
- ✅ USB/LSB conventions correct (LSB below 10 MHz, USB above)
- ✅ Volunteer Monitor Program covered
- ✅ CW Q-signals and prosigns covered
- ✅ Digital modes (FT8, RTTY, PACTOR, Winlink) covered
- ✅ RACES rules covered
- ✅ DX operating practices covered
- ⚠️ No satellite-specific section in narrative, but no satellite questions exist in the pool
- **Grade: A** (complete for the actual pool)

#### G3 — Radio Wave Propagation (37 questions, 3 on exam)
- ✅ D region absorption correct (daytime HF absorber)
- ✅ F2 layer characteristics correct (main long-distance layer)
- ✅ F2 hop distance correct (2,500 miles per pool G3B09)
- ✅ E region hop distance correct (1,200 miles per pool G3B10)
- ✅ MUF/LUF concepts correct
- ✅ Solar indices (K-index, A-index, sunspot cycle) covered
- ✅ NVIS explained correctly (40m, low horizontal antenna)
- ✅ Scatter propagation modes covered
- **Grade: A** (thorough and accurate)

#### G4 — Amateur Radio Practices (60 questions, 5 on exam)
- ✅ Receiver controls well-explained (notch filter, noise blanker, attenuator, noise reduction)
- ✅ Oscilloscope usage correct (vertical channel shows waveform)
- ✅ Two-tone test correctly described (non-harmonically related tones)
- ✅ ALC purpose correct (prevent excessive drive)
- ✅ Speech processor effects correct (increases average power, not peak)
- ✅ S-meter math correct (6 dB per S-unit, 4× power)
- ✅ Sideband direction rules correct (LSB extends below, USB extends above)
- ✅ Mobile antenna limitations covered
- ✅ Solar panel and LiFePO4 battery rules correct
- **Grade: A** (excellent practical coverage)

#### G5 — Electrical Principles (40 questions, 3 on exam)
- ✅ Reactance formulas correct (X_L = 2πfL, X_C = 1/(2πfC))
- ✅ Impedance concept correct (Z = √(R² + X²))
- ✅ Resonance formula correct (f = 1/(2π√(LC)))
- ✅ Series resonance = low impedance (correct per pool G5A01)
- ✅ RMS/peak conversions correct (0.707 and 1.414)
- ✅ PEP formula correct with peak-to-peak trap explained
- ✅ 1 dB ≈ 20.6% loss correct (per pool G5B10)
- ✅ Transformer turns ratio and impedance matching correct
- ✅ Series/parallel component rules correct with worked examples
- **Grade: A** (excellent with worked examples)

#### G6 — Circuit Components (23 questions, 2 on exam)
- ✅ Silicon threshold 0.7V, Germanium 0.3V (correct)
- ✅ MOSFET insulated gate (correct)
- ✅ BJT switch modes: saturation and cutoff (correct)
- ✅ Ferrite core frequency behavior = material mix (correct)
- ✅ Connector frequency limits correct (BNC 4 GHz, Type N 10 GHz, SMA 18+ GHz)
- ✅ Battery rules correct (10.5V minimum for 12V lead-acid)
- **Grade: A** (accurate and well-organized)

#### G7 — Practical Circuits (38 questions, 3 on exam)
- ✅ Rectifier types correct (half-wave 1 diode, full-wave center-tap 2 diodes, bridge 4 diodes)
- ✅ Bleeder resistor purpose correct (safety discharge)
- ✅ Amplifier classes and efficiency correct
- ✅ Class C appropriate for FM (correct)
- ✅ Oscillator feedback loop requirement correct
- ✅ Balanced modulator output correct (DSB suppressed carrier)
- ✅ Product detector for SSB reception correct
- ✅ SDR and I/Q concepts correct (90° phase difference)
- ⚠️ Figure G7-1 referenced in 5 questions but no image file exists
- **Grade: A-** (missing figure is the only gap)

#### G8 — Signals and Emissions (43 questions, 3 on exam)
- ✅ SSB = narrowest phone bandwidth (correct per pool G8A07)
- ✅ FM bandwidth calculation correct (Carson's Rule: 2×(deviation + max modulating freq))
- ✅ PSK31 and Varicode explained correctly
- ✅ FT8 characteristics correct (8-FSK, ~50 Hz bandwidth, low SNR decode)
- ✅ Intermodulation order determination correct
- ✅ Link budget and margin concepts correct
- ✅ ARQ vs FEC correctly distinguished
- ✅ Waterfall display axes correct (frequency × time × intensity)
- **Grade: A** (comprehensive)

#### G9 — Antennas and Feed Lines (46 questions, 4 on exam)
- ✅ Dipole formula correct (468/f(MHz))
- ✅ Quarter-wave formula correct (234/f(MHz))
- ✅ SWR calculation correct (bigger impedance ÷ smaller)
- ✅ Window line impedance correct (450 ohms per pool G9A03)
- ✅ Dipole feed point impedance correct (~73 ohms free space)
- ✅ Yagi element relationships correct (reflector longest, director shortest)
- ✅ dBi vs dBd relationship correct (+2.15)
- ✅ Stacking gain correct (+3 dB)
- ✅ NVIS antenna requirements correct (low horizontal dipole)
- ✅ Antenna tuner doesn't reduce feed line SWR (correctly explained)
- **Grade: A** (thorough with good practical advice)

---

## Supporting Materials Audit

### CRAM-SHEET.md — Grade: B+

**What works:**
- Frequency table now has separate CW/Data and Phone columns — major improvement
- 60m channel table with all 5 channels + 15 kHz segment
- Key formulas are correct and useful
- Modulation bandwidth table is accurate
- Quick conversions section is practical

**Issues:**
- Amplifier class table includes Class D (~90%, switching) — not tested in the pool, wastes cram sheet space
- Missing PEP formula (PEP = V_peak²/(2R)) — one of the most commonly calculated exam formulas
- Missing power formulas (P = I²R, P = E²/R) — tested multiple times
- No mention of key connector facts (BNC 4 GHz, Type N 10 GHz, etc.)
- The propagation section is thin — missing F2 hop distance (2,500 mi), E hop (1,200 mi), K-index meaning

### STUDY-PLAN.md — Grade: D

Still a placeholder. Has a 7-row table with subelement-to-day mapping but:
- No daily study tips or strategies
- No time estimates per day
- No review/practice test schedule
- No "what to focus on" guidance
- The header still says "Placeholder — detailed study plan will be written after subelement study guides are complete"
- Now that the guides ARE complete, this should be fleshed out

### README.md — Grade: A-

- Accurate question count (429)
- Correct exam parameters (35 questions, 26 to pass, 74%)
- Fee information updated and accurate
- PWA link present and functional
- Subelement table correct
- Study tips section helpful
- Minor: still no mention of audio files being available (they exist as .mp3 in subelements/)

### PWA Study App — Grade: A

Fully functional study application with:
- ✅ Flashcard mode with weak-spot prioritization
- ✅ Practice exam mode (35 questions, weighted by subelement, timed)
- ✅ Section/group study drill-down
- ✅ Progress tracking with mastery system
- ✅ Dark/light mode
- ✅ Formula quick reference (📐 button)
- ✅ Installable PWA with offline capability
- ✅ Accessibility features (skip links, ARIA labels, screen reader announcements)
- ✅ Loads from correct pool JSON (2023-2027, 429 questions)
- ✅ Correct exam weights per subelement

### Audio Files — Grade: A

All 20 MP3 files exist:
- 10 narrative study guide audio files
- 10 question file audio files
- TTS pronunciation guide exists at `tts/pronunciation.txt`

### Figures — Grade: F

**No figure images exist.** Figure G7-1 (schematic symbols) is referenced by 5 pool questions. The question explanations describe the symbols textually, which partially compensates, but visual learners are at a disadvantage.

### Scripts — Grade: B

Three utility scripts exist:
- `gen-question-files.py` — generates question markdown from pool JSON
- `parse-pool.py` — parses the question pool
- `pool-diff.py` — compares pool versions

No standalone practice test script, but the PWA fully replaces this need.

---

## Remaining Gaps Ranked by Exam Impact

| Rank | Gap | Exam Impact | Questions Affected |
|------|-----|------------|-------------------|
| 1 | Figure G7-1 missing | MODERATE | 5 (G7A09-G7A13) — partially mitigated by text descriptions |
| 2 | STUDY-PLAN.md is a placeholder | LOW-MODERATE | Indirect — affects study efficiency, not content |
| 3 | Cram sheet missing PEP/power formulas | LOW | Indirect — formulas exist in G5 guide |
| 4 | No cross-references in G0-G3, G5-G6 narratives | LOW | Indirect — affects learning connections |
| 5 | README doesn't mention audio files | LOW | Discoverability issue only |

---

## What's Working Well

1. **100% question coverage** — Every single pool question is present with a substantive explanation
2. **100% answer accuracy** — Zero mismatches between guide answers and pool correct answers
3. **Teaching quality** — Explanations average 622 characters, all over 200 chars, 84% over 500 chars. They teach concepts, not just answers.
4. **Narrative guides** — Well-written, progressive, with analogies and worked examples. G5's formula walkthroughs and G9's antenna explanations are particularly strong.
5. **Critical fixes from April 2** — 20m frequency, CW/Data allocations, 60m band, Technician comparison — all corrected
6. **PWA study app** — Fully functional, installable, with flashcards, practice exams, section study, progress tracking, and formula reference
7. **Audio files** — Complete set of TTS recordings for all content
8. **Cross-referencing in later guides** — G4, G7, G8, G9 appropriately reference earlier material
9. **CRAM-SHEET** — Now has proper CW/Data + Phone columns and 60m channel table
10. **Clean repo structure** — Logical file organization, proper naming conventions

---

## Specific Items That Need Fixing

### Priority 1 (High Impact)

1. **Add Figure G7-1 image** — Source the NCVEC schematic symbols figure or create an equivalent. 5 exam questions directly reference it. Place in a `figures/` directory and link from G7 questions and narrative guide.

2. **Flesh out STUDY-PLAN.md** — Remove the "placeholder" header. Write a proper 7-day plan with:
   - Daily time estimates (e.g., "Day 1: ~2 hours")
   - What to read and what to drill
   - When to take practice exams
   - Review strategy for the final day
   - Tips for exam day

### Priority 2 (Moderate Impact)

3. **Enhance CRAM-SHEET** — Add:
   - PEP formula: PEP = V_peak²/(2R)
   - Power formulas: P = I²R, P = E²/R
   - Key numbers: F2 hop ~2,500 mi, E hop ~1,200 mi
   - Connector frequency limits
   - Remove Class D amplifier row (not tested)

4. **Mention audio files in README** — Add a section noting that TTS audio recordings of all guides and question files are available in `subelements/*.mp3`

### Priority 3 (Low Impact)

5. **Add cross-references to early guides** — G0, G1, G2, G3, G5, G6 could benefit from forward-references to where their concepts get applied (e.g., G5 reactance → used in G7 filters and G9 antenna matching)

6. **Add a "What You Should Already Know" section** — Brief Technician knowledge recap for students who haven't studied in a while

---

## Final Assessment

### Would a student pass using only this guide?

**Yes, very likely.** The guide covers 100% of pool questions with teaching-quality explanations, has a functional practice exam app, and all critical frequency/rule information is now correct. The missing Figure G7-1 could cost 1-2 questions but the text descriptions partially compensate. The average student using this guide systematically (reading narratives + drilling questions + taking practice exams) should pass comfortably.

### Is it publishable?

**Almost.** Fix the Figure G7-1 gap and flesh out the study plan, and it's ready. The content quality is genuinely good — this isn't a "memorize the answers" guide, it's a "understand the material" guide. That's the right approach.

### Grade Breakdown

| Category | Grade | Notes |
|----------|-------|-------|
| Question Coverage | A | 429/429, zero gaps |
| Answer Accuracy | A | 429/429 verified against pool |
| Teaching Quality | A | Substantive explanations that teach concepts |
| Technical Accuracy | A | All frequencies, formulas, rules verified correct |
| Narrative Guides | A | Well-written, progressive, with worked examples |
| CRAM-SHEET | B+ | Good but missing a few key formulas |
| STUDY-PLAN | D | Still a placeholder |
| PWA Study App | A | Full-featured and functional |
| Audio Files | A | Complete set |
| Figures | F | Figure G7-1 missing |
| README | A- | Accurate but doesn't mention audio |
| **Overall** | **B+** | **One day of work away from an A** |

---

*Review cross-referenced all 429 pool questions against study guide content. Answer accuracy verified programmatically. Technical facts checked against pool correct answers (the source of truth for exam prep). Previous review issues tracked and status verified.*
