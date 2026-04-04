# General Class Exam — 7-Day Study Plan

A structured plan to prepare for the FCC General class exam in one week. This assumes you already hold a Technician class license.

## Before You Start

**What you need:**
- This study guide (you're holding it)
- The [PWA Study App](https://jeremy-windsor.github.io/general-study-guide/apps/study-app/) on your phone or desktop
- A quiet hour or two each day
- Optionally: the MP3 audio files in `subelements/` for listening during commutes

**Coming from Technician?** Good news — you already know basic electronics, FM repeater operation, and VHF/UHF propagation. The General exam builds on that foundation. The biggest new areas are HF operating (SSB, CW, digital modes), radio wave propagation (ionospheric skip), and deeper electrical theory. The rules section is mostly about which HF frequencies you can use.

---

## Day 1: Rules & Privileges (~2 hours)

> 📋 **Rusty on Technician material?** Start with [What You Should Already Know](TECHNICIAN-BRIDGE.md) — a quick 10-minute refresher on Ohm's Law, frequency/wavelength, and VHF/UHF basics that the General exam builds on.

**Goal:** Know exactly what a General license lets you do.

| Activity | Time | Resource |
|----------|------|----------|
| Read G1 narrative | 30 min | `subelements/G1-commission-rules.md` |
| Drill G1 questions | 45 min | PWA → Study by Section → G1 |
| Read G0 narrative | 20 min | `subelements/G0-safety.md` |
| Drill G0 questions | 15 min | PWA → Study by Section → G0 |
| Review missed questions | 10 min | PWA → Weak Areas |

**Focus areas:**
- HF band allocations — know which bands allow phone, which are CW/data only
- 60m channelized operation (5 channels, 100W ERP, USB only)
- 30m power limit (200W PEP, no phone)
- Third-party traffic rules and CEPT agreements
- VE requirements (3 VEs, only test up to their own class)
- RF safety basics — MPE limits, when evaluation is required

**Technician bridge:** You already know Part 97 basics. General adds HF-specific rules: band edges, power limits per band, and international operating agreements.

---

## Day 2: Operating Procedures (~2 hours)

**Goal:** Understand HF operating conventions and digital modes.

| Activity | Time | Resource |
|----------|------|----------|
| Read G2 narrative | 35 min | `subelements/G2-operating-procedures.md` |
| Drill G2 questions | 50 min | PWA → Study by Section → G2 |
| Review missed questions | 15 min | PWA → Weak Areas |
| Take first practice exam | 20 min | PWA → Practice Exam |

**Focus areas:**
- USB vs LSB convention: USB on 20m and above, LSB on 40m and below
- CQ DX and split-frequency operating
- VOX operation and purpose
- Digital modes: FT8 (8-FSK, ~50 Hz BW), RTTY, PSK31, Winlink
- RACES vs ARES — who activates RACES (local/state/federal government)
- Volunteer Monitor Program (replaced Official Observer)

**Technician bridge:** You know FM repeater procedures. HF operating is different — SSB requires tuning, there are no repeaters, and DX contacts follow specific etiquette. Digital modes are the fastest-growing part of HF.

**Practice exam:** Don't worry about your score on the first practice test. It establishes your baseline and shows the PWA which areas need work.

---

## Day 3: Propagation (~1.5 hours)

**Goal:** Understand how HF signals travel long distances.

| Activity | Time | Resource |
|----------|------|----------|
| Read G3 narrative | 30 min | `subelements/G3-radio-wave-propagation.md` |
| Drill G3 questions | 30 min | PWA → Study by Section → G3 |
| Review CRAM-SHEET propagation section | 10 min | `CRAM-SHEET.md` |
| Review missed questions | 10 min | PWA → Weak Areas |

**Focus areas:**
- Ionospheric layers: D (daytime absorber), E (sporadic-E), F1/F2 (long-distance)
- F2 single-hop distance: ~2,500 miles
- E single-hop distance: ~1,200 miles
- MUF and LUF — what they are and why they matter
- Solar cycle effects: sunspot numbers, K-index (0–1 = quiet, 5+ = storm), A-index
- NVIS: Near Vertical Incidence Skywave — 40m, low horizontal antenna, regional coverage
- Scatter modes: tropospheric, ionospheric, meteor scatter
- Gray-line propagation

**Technician bridge:** VHF/UHF is mostly line-of-sight. HF is a completely different world — signals bounce off the ionosphere, conditions change hourly, and understanding propagation is what separates operators who make contacts from those who don't.

---

## Day 4: Amateur Practices (~2 hours)

**Goal:** Know your receiver controls, test equipment, and station setup.

| Activity | Time | Resource |
|----------|------|----------|
| Read G4 narrative | 30 min | `subelements/G4-amateur-practices.md` |
| Drill G4 questions | 50 min | PWA → Study by Section → G4 |
| Review missed questions | 15 min | PWA → Weak Areas |
| Take second practice exam | 20 min | PWA → Practice Exam |

**Focus areas:**
- Receiver controls: notch filter (removes single-frequency interference), noise blanker (pulse noise), IF shift, attenuator
- S-meter: 6 dB per S-unit = 4× power difference
- Oscilloscope: vertical channel displays waveform shape
- Two-tone test: non-harmonically related tones to check transmitter linearity
- ALC: prevents excessive drive to final amplifier
- Speech processor: increases average power (not peak)
- Mobile installations: screwdriver antennas, grounding, noise
- Solar panels and LiFePO4 batteries for field ops

**Technician bridge:** You know basic transceiver operation. G4 goes deeper into the controls you'll actually use on HF — especially the receiver controls that make weak signals readable.

---

## Day 5: Electrical Principles & Components (~2.5 hours)

**Goal:** Master the math and understand the components.

| Activity | Time | Resource |
|----------|------|----------|
| Read G5 narrative | 40 min | `subelements/G5-electrical-principles.md` |
| Drill G5 questions | 30 min | PWA → Study by Section → G5 |
| Read G6 narrative | 25 min | `subelements/G6-circuit-components.md` |
| Drill G6 questions | 20 min | PWA → Study by Section → G6 |
| Review CRAM-SHEET formulas | 15 min | `CRAM-SHEET.md` |
| Review missed questions | 10 min | PWA → Weak Areas |

**Focus areas (G5 — the math day):**
- Reactance: X_L = 2πfL, X_C = 1/(2πfC)
- Impedance: Z = √(R² + X²)
- Resonance: f = 1/(2π√LC) — series resonance = minimum impedance
- PEP: P = V_peak²/(2R) — **watch out for peak-to-peak vs peak voltage**
- Power: P = IE, P = I²R, P = E²/R
- dB: +3 dB = 2× power, +10 dB = 10× power, 1 dB ≈ 20.6% change
- Transformer turns ratio: impedance ratio = (turns ratio)²

**Focus areas (G6 — components):**
- Diode thresholds: Silicon 0.7V, Germanium 0.3V
- MOSFET: insulated gate (voltage-controlled)
- BJT switching: saturation (ON) and cutoff (OFF)
- Connector limits: BNC 4 GHz, Type N 10 GHz, SMA 18+ GHz
- Ferrite core behavior varies by material mix

**Technician bridge:** You covered Ohm's Law and basic components. G5/G6 goes deeper — reactance, impedance, and resonance are the core of how radio circuits work. Spend extra time on the formulas.

---

## Day 6: Circuits, Signals & Antennas (~2.5 hours)

**Goal:** Understand how circuits and antennas work together.

| Activity | Time | Resource |
|----------|------|----------|
| Read G7 narrative | 35 min | `subelements/G7-practical-circuits.md` |
| Drill G7 questions | 25 min | PWA → Study by Section → G7 |
| Read G8 narrative | 35 min | `subelements/G8-signals-emissions.md` |
| Drill G8 questions | 25 min | PWA → Study by Section → G8 |
| Read G9 narrative | 35 min | `subelements/G9-antennas-feedlines.md` |
| Drill G9 questions | 30 min | PWA → Study by Section → G9 |
| Review missed questions | 15 min | PWA → Weak Areas |

**Focus areas (G7 — circuits):**
- Rectifiers: half-wave (1 diode), full-wave (2 diodes + center tap), bridge (4 diodes)
- Amplifier classes: A (25%, linear), B (60%, push-pull), C (80%, FM only)
- Balanced modulator → DSB suppressed carrier
- SDR and I/Q: 90° phase difference between I and Q channels
- **Study Figure G7-1** — 5 questions reference schematic symbols directly

**Focus areas (G8 — signals):**
- SSB bandwidth ≈ 2.4 kHz (narrowest phone mode)
- FM bandwidth = Carson's Rule: 2 × (deviation + max audio freq)
- Intermodulation products and their order
- Link budget: transmit power + antenna gains − path loss
- PSK31, FT8, ARQ vs FEC

**Focus areas (G9 — antennas):**
- Dipole: 468/f(MHz) feet, ~73Ω feed point, figure-8 pattern
- Quarter-wave vertical: 234/f(MHz) feet, needs ground radials
- Yagi: reflector longest, directors shortest, driven element in between
- SWR = bigger impedance ÷ smaller impedance
- Feed lines: coax (50/75Ω) vs window line (450Ω)
- Antenna tuner: matches impedance but does NOT reduce SWR on the feed line

---

## Day 7: Review & Practice Exams (~2–3 hours)

**Goal:** Solidify weak areas and build exam confidence.

| Activity | Time | Resource |
|----------|------|----------|
| Review CRAM-SHEET front to back | 20 min | `CRAM-SHEET.md` |
| Drill Weak Areas | 30 min | PWA → Weak Areas |
| Practice Exam #1 | 20 min | PWA → Practice Exam |
| Review missed questions from exam | 15 min | Re-read explanations |
| Practice Exam #2 | 20 min | PWA → Practice Exam |
| Review missed questions from exam | 15 min | Re-read explanations |
| Practice Exam #3 (if time) | 20 min | PWA → Practice Exam |
| Final CRAM-SHEET review | 15 min | `CRAM-SHEET.md` |

**Review strategy:**
1. Start with the PWA's Weak Areas — these are questions you've missed before
2. Re-read the explanation for every question you get wrong, not just the correct answer
3. If you're consistently scoring 80%+ on practice exams, you're ready
4. If you're below 74%, focus on the subelements where you lose the most points
5. Don't cram new material on exam day — trust your preparation

---

## Exam Day Tips

### The Night Before
- Review the CRAM-SHEET one final time
- Get a full night's sleep — a rested brain recalls better than a crammed one
- Confirm your exam session time and location
- Charge your phone (if using for ID or confirmation)

### What to Bring
- **Government-issued photo ID** (driver's license, passport)
- **Your Technician license** (or FRN printout from the FCC ULS website)
- **FRN (FCC Registration Number)** — you'll need this on the paperwork
- **$15 cash or check** for the VEC session fee (check with your VEC)
- **Pencil** (usually provided, but bring one)

### During the Exam
- Read each question carefully — watch for "NOT" and "EXCEPT" in the question stem
- If you don't know an answer, eliminate obviously wrong choices first
- Mark uncertain questions and come back — don't get stuck
- You need 26 out of 35 — you can miss 9 and still pass
- There's no time limit, so don't rush

### After the Exam
- If you pass, your VE team submits your paperwork electronically (most do same-day)
- Pay the **$35 FCC application fee** when you receive the email from the FCC
- Your new privileges appear in the ULS database, usually within a few business days
- You can operate on HF as soon as your upgrade appears in ULS
- Consider studying for Amateur Extra while the material is fresh!

---

## Quick Reference: What's On the Exam

| Subelement | Topic | Exam Qs | Study Day |
|:----------:|-------|:-------:|:---------:|
| G1 | Commission's Rules | 5 | Day 1 |
| G0 | Electrical and RF Safety | 2 | Day 1 |
| G2 | Operating Procedures | 5 | Day 2 |
| G3 | Radio Wave Propagation | 3 | Day 3 |
| G4 | Amateur Radio Practices | 5 | Day 4 |
| G5 | Electrical Principles | 3 | Day 5 |
| G6 | Circuit Components | 2 | Day 5 |
| G7 | Practical Circuits | 3 | Day 6 |
| G8 | Signals and Emissions | 3 | Day 6 |
| G9 | Antennas and Feed Lines | 4 | Day 6 |
| | **Total** | **35** | |

---

## Audio Study Option

All narrative guides and question files have MP3 audio recordings available in `subelements/`. Use them for:
- Commute listening (narratives explain concepts conversationally)
- Reinforcement after reading the written guides
- Accessibility — if you learn better by listening

---

*Good luck on your exam. You've got this. 73!* 🎓
