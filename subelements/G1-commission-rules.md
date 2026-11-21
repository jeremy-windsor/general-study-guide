# G1 — Commission's Rules

The General class license is your gateway to the HF bands — worldwide communication, DX contests, digital modes, and everything that makes amateur radio addictive. But with great power (literally, 1500 watts on most bands) comes a thicker rulebook. Subelement G1 is where the FCC lays out what you can do, where you can do it, and what happens when you screw up.

This is the most memorization-heavy section on the exam. You'll see 5 questions from a pool of 52. The good news: the rules follow patterns, and once you see the patterns, the memorization gets much easier.

---

## Your New Frequency Privileges

The single biggest upgrade from Technician to General is HF access. As a Tech, you had a few slices of HF. As a General, you get most of it. But not all of it — some segments are reserved for Amateur Extra licensees.

### The Big Four Restricted Bands

On **four** HF bands, General class licensees are restricted to only a portion of the voice/phone segment — and they are also locked out of the bottom 25 kHz of the CW/data segment:

| Band | General Phone Privileges | Phone Segment Closed to Generals |
|------|------------------------|--------------------|
| **80 meters** (3.5 MHz) | 3.800–4.000 MHz | 3.600–3.800 MHz |
| **40 meters** (7 MHz) | 7.175–7.300 MHz | 7.125–7.175 MHz |
| **20 meters** (14 MHz) | 14.225–14.350 MHz | 14.150–14.225 MHz |
| **15 meters** (21 MHz) | 21.275–21.450 MHz | 21.200–21.275 MHz |

Notice the pattern: **Generals always get the upper portion** of the voice segment. Extras get the lower portion. No exceptions.

Two details the table doesn't show. First, the bottom 25 kHz of each of these bands — 3.500–3.525, 7.000–7.025, 14.000–14.025, and 21.000–21.025 MHz — is Extra-only CW and data territory, so Generals can't transmit there either. Second, parts of the phone segments closed to Generals are shared with the older Advanced class, which can no longer be issued; the phone slices that are truly Extra-only are 3.600–3.700, 14.150–14.175, and 21.200–21.225 MHz.

These same four bands — 80, 40, 20, and 15 meters — are the ones with Extra-only segments. Every other HF/MF band gives Generals full access.

> **Memory trick:** The "big four" bands (80, 40, 20, 15) have Extra-only zones. Everything else — 160m, 60m, 30m, 17m, 12m, 10m — is open to Generals on all segments.

### Bands with Full General Privileges

On these bands, your General class license gives you the same access as an Extra:

| Band | Frequency | Notes |
|------|-----------|-------|
| **160 meters** | 1.800–2.000 MHz | Full access, 1500W |
| **60 meters** | 4 channels + 5351.5–5366.5 kHz | 100W ERP on channels, 9.15W ERP in the segment, 2.8 kHz max |
| **30 meters** | 10.100–10.150 MHz | CW and data only, 200W max |
| **17 meters** | 18.068–18.168 MHz | Full access, 1500W |
| **12 meters** | 24.890–24.990 MHz | Full access, 1500W |
| **10 meters** | 28.000–29.700 MHz | Full access, 1500W |

### CW Is King

Here's a useful rule of thumb: **CW is permitted everywhere you have privileges**. On 10 meters, for example, a General class operator can transmit CW across the entire band — 28.000 to 29.700 MHz. CW restrictions, where they exist, only apply within the segments of the big four bands that are closed to Generals.

### Key Frequencies to Know

The exam tests specific frequencies. Here are the ones you should recognize:

- **7.125–7.175 MHz** — Extra and Advanced only on 40m (Generals are prohibited here)
- **21.300 MHz** — Within the General portion of 15 meters ✓
- **14.250 MHz** — In the General class portion of 20m (above 14.225) ✓
- **29.5+ MHz** — The only portion of 10m available for repeater use

---

## The Special Bands: 30 and 60 Meters

Two bands have unique restrictions that come up repeatedly on the exam.

### 30 Meters — The Quiet Band

The 30-meter band (10.100–10.150 MHz) is the most restricted HF band:

- **No phone (voice)** — CW and data modes only
- **No image transmissions** — No SSTV, no FAX
- **200 watts PEP maximum** — Not the usual 1500W
- **Secondary allocation** — Amateurs must defer to government fixed stations

Think of 30 meters as the "narrow, quiet, low-power data band." It's only 50 kHz wide, shared with government services, and everything about it is designed to minimize interference.

### 60 Meters — Channels Plus a Small Segment

The 60-meter band (5 MHz region) is unique in amateur radio. As of **February 13, 2026**, the FCC changed it to match the WRC-15 worldwide allocation:

- **Four channels** — centered on 5332, 5348, 5373, and 5405 kHz, at up to **100 watts ERP**
- **A contiguous segment** — **5351.5–5366.5 kHz**, where you can tune anywhere, at up to **9.15 watts ERP**. (The old 5358.5 kHz channel was absorbed into this segment.)
- **USB for voice by convention** — Upper Sideband is the standard practice on 60m, even though 60m is below 10 MHz, and the channel dial frequencies assume it. The rules permit phone, data, RTTY, and CW; they don't legally mandate USB.
- **2.8 kHz maximum bandwidth** — applies to all 60m transmissions
- **Secondary allocation** — government users are primary
- **Antenna gain records** — If you use anything other than a dipole, you must record the antenna gain

The ERP measurement is the trickiest part. On most bands, power is measured as PEP at the transmitter output. On 60 meters, it's measured as ERP relative to a dipole. If you use a beam antenna with gain, you must reduce your transmitter power so the effective radiated power stays under the limit. That's why the FCC requires you to record your antenna gain — to prove you're doing the math.

> **Exam note:** Questions G1A04 and G1C09 (60m channels and the 100W limit) were withdrawn by NCVEC because of this rule change, so they won't appear on your exam.

---

## Power Limits

The default maximum power for US amateurs is **1500 watts PEP output from the transmitter**. But two bands have lower limits:

| Band | Maximum Power | Why |
|------|--------------|-----|
| Most HF bands | 1500 watts PEP | Standard amateur maximum |
| 30 meters | 200 watts PEP | Secondary allocation, shared with government |
| 60 meters | 100 watts ERP on the channels; 9.15 watts ERP in 5351.5–5366.5 kHz | Shared with government (secondary) |

### How Power Is Measured

FCC rules specify power as **PEP (Peak Envelope Power) output from the transmitter**. Not RMS, not average, not at the antenna — PEP at the transmitter output. PEP is the average power during one RF cycle at the crest of the modulation envelope.

The main HF exception: 60 meters measures **ERP** (Effective Radiated Power, relative to a dipole). On the other HF bands, feed line losses don't factor in — you're measured at the transmitter output. (The 630m and 2200m bands also use radiated-power (EIRP) limits.)

---

## Primary vs. Secondary Allocations

The concept of primary and secondary spectrum allocation is fundamental to understanding your operating privileges:

- **Primary users** have priority. They don't need to worry about you.
- **Secondary users** (that's amateurs on some bands) must not cause harmful interference to primary users AND must accept interference from primary users.

When you're secondary, you're a guest. If a primary user shows up and your signal interferes with them, you must stop transmitting. You can't file a complaint about their interference to you — that's the deal you accepted when you got access to their spectrum.

Bands where amateurs are secondary include 30 meters, 60 meters, and portions of several other allocations, including part of the 2.4 GHz band, where government radiolocation is primary. Note that Wi-Fi is not a primary user there — unlicensed Wi-Fi devices have no allocation status at all and must accept interference from licensed services like ours.

---

## Data Emission Standards

### Bandwidth Limits (Symbol Rate Limits Removed)

The HF symbol-rate limits you may see in older study material (300 baud below 28 MHz, 1200 baud on 10 meters) **no longer exist**. In a November 2023 order, the FCC replaced the HF baud limits with a **2.8 kHz bandwidth limit** for data emissions. NCVEC withdrew questions G1C08 and G1C10 because of this change.

The bandwidth limit keeps HF data signals about as wide as an SSB voice signal, while letting newer, faster modes use that space efficiently. Common HF digital modes are far narrower anyway: RTTY ~250 Hz, PSK31 ~31 Hz, FT8 ~50 Hz.

### New Digital Protocols

Before using a new digital protocol on the air, you must **publicly document the technical characteristics**. This is a fundamental amateur radio principle — all transmissions must be decodable by anyone. Publish the specs and you're good. No FCC approval, no experimental license, no rule-making petition needed.

---

## Antenna Structures and PRB-1

### Height Limits

An antenna structure **under 200 feet** (not near a public-use airport) doesn't require FAA notification or FCC registration. Once you exceed 200 feet, both become mandatory. Proximity to airports changes the rules — even short towers may require notification near airports.

### State and Local Regulation (PRB-1)

The FCC's 1985 PRB-1 ruling established the framework for state and local antenna regulation:

- State and local governments **CAN** regulate amateur antennas (the FCC doesn't completely preempt local authority)
- But they must **reasonably accommodate** amateur communications
- Regulations must be the **minimum practical** to achieve a legitimate purpose

This means a city or county can't ban amateur antennas outright, but it can apply reasonable rules (setbacks, safety, some aesthetics). Note that PRB-1 applies to **state and local governments only** — it does **not** override private deed restrictions or HOA covenants (CC&Rs).

---

## Beacon Stations

Beacons are automated transmitters designed for one purpose: **observation of propagation and reception**. Key rules:

- **100 watts PEP maximum** output power
- **One beacon per band** from the same station location
- **Automatically controlled beacons on HF** are permitted only on **28.20–28.30 MHz** (10 meters)
- Purpose is propagation observation, not bulletins or repeater ID

### The International Beacon Network

The NCDXF/IARU International Beacon Project operates synchronized beacons on five frequencies: 14.100, 18.110, 21.150, 24.930, and 28.200 MHz. These frequencies should be avoided by other operators — transmitting on them interferes with propagation monitoring. It's not illegal, but it's bad operating practice.

---

## Permitted and Prohibited Transmissions

### What You CAN Do
- **Retransmit weather forecasts** from US government stations (occasionally)
- **Send one-way code practice transmissions** to help people learn Morse code
- **Use abbreviations and procedural signals** as long as they don't obscure the meaning of your message
- **Contact stations in most countries** — the exception is countries whose administrations have notified the ITU that they object

### What You CAN'T Do
- **Unidentified transmissions** — you must always identify, period
- **Encrypted messages** — amateur radio is a transparent service
- **Automatic retransmission** of other amateur signals without authorization
- **Obscure your message** with codes designed to hide meaning (different from standard abbreviations)

---

## Volunteer Examiner Program

Amateur radio is unique — hams test hams. The Volunteer Examiner (VE) system is how new licenses are issued.

### Who Can Be a VE?

| Requirement | Details |
|-------------|---------|
| License class | General can administer Technician exams only; Extra can administer all exams |
| Minimum age | 18 years |
| Citizenship | Not required — non-US citizens with FCC licenses can serve |
| Accreditation | Must be accredited by a VEC (Volunteer Examiner Coordinator) |

The key principle: **each exam requires VEs of a specific minimum class**. General VEs → Technician exams only. Extra VEs → Technician, General, and Extra exams.

### Exam Session Requirements

Every exam session requires at least **three VEs** of the appropriate license class. For Technician exams, all three must be General or higher. For the General exam, they must hold Advanced or Extra; for the Extra exam, all three must be Extra class.

### The CSCE

A Certificate of Successful Completion of Examination (CSCE) is valid for **365 days** (one year). During that time:

- You can operate using your new privileges immediately (with the AG identifier if upgrading, G1D06)
- You can use the CSCE for element credit at future exam sessions
- You don't have to wait for the FCC database to update

### Expired License Credit

If you once held a General, Advanced, or Extra class license and it expired (but was NOT revoked), you can get **element credit** for the exam elements you already passed. There's no time limit — even a license that expired 30 years ago qualifies. To get a new General license after your old one expired beyond the grace period, you need to show proof of the expired license and pass the current Technician (Element 2) exam. The General element gets credited.

---

## Control Operators and Remote Control

### Control Operator Privileges

The control operator's license class determines what the station can do. This creates interesting scenarios with repeaters:

- A **10-meter repeater** retransmitting a **2-meter signal** from a Technician requires a General class (or higher) control operator on the 10-meter side. The Tech is fine on 2 meters, but someone with General privileges must authorize the 10-meter output.

### Remote Control

- **US station controlled remotely from abroad**: You need a US operator/primary station license. No special permits, no foreign license. The station is in the US, so US rules apply.
- **Foreign station controlled remotely from the US**: Only the regulations of the foreign country apply. The station is in their country, transmitting from their country — their rules govern.

The principle: **regulations follow the station's physical location**, not the operator's location.

---

## Third-Party Traffic

Third-party traffic means non-licensed people communicating through your amateur station. The rules:

- **Who CAN be a third party**: Anyone — including non-US citizens and non-English speakers
- **Who CANNOT be a third party**: Anyone whose amateur license has been revoked and not reinstated
- **Content restrictions** (to countries with third-party agreements): Messages must relate to amateur radio, be personal in nature, or relate to emergencies/disaster relief
- **Digital modes are NOT exempt**: The same third-party rules apply to all modes — phone, CW, digital, everything
- **Remote control doesn't change anything**: If third-party messages are normally permitted, they're also permitted via remote control

---

## ITU Regions and International Operation

The ITU divides the world into three regions:

| Region | Coverage |
|--------|----------|
| Region 1 | Europe, Africa, most of the Middle East, northern Asia |
| **Region 2** | North and South America, Caribbean, Hawaii |
| Region 3 | Southern Asia, Australia, Pacific |

North and South American amateur operators follow Region 2 frequency allocations. Allocations differ between regions — for example, the 40-meter band extends to 7.300 MHz in Region 2 but only to 7.200 MHz in Regions 1 and 3.

---

## Spread Spectrum and Automatic Control

### Spread Spectrum
- Maximum power: **10 watts PEP** (extremely low compared to normal limits)
- Restricted to frequencies above 222 MHz

### Automatically Controlled Digital Stations
- Can operate on the **6-meter band and shorter wavelengths** broadly
- On HF, restricted to **limited designated segments**
- To initiate contact with an auto-controlled station outside designated segments, the initiating station must be under **local or remote control** (human in the loop)

### Wi-Fi Coexistence
Although amateurs share the 2.4 GHz band with Wi-Fi, amateur stations may **NOT communicate with non-licensed Wi-Fi stations** on any part of the band. The two services operate under different rule parts and intentional cross-communication isn't permitted.

---

## Interference Avoidance

Several situations require specific steps to avoid harmful interference:

- Operating within **one mile of an FCC Monitoring Station**
- Using a band where amateurs are **secondary users**
- Transmitting **spread spectrum emissions**

All three conditions trigger interference-avoidance requirements. The common thread: when your transmissions could impact sensitive government operations or primary users, extra care is required.

---

## Quick-Reference Summary

### Power Limits
| Band | Limit |
|------|-------|
| Most bands | 1500W PEP output |
| 30 meters | 200W PEP output |
| 60 meters | 100W ERP on channels; 9.15W ERP in 5351.5–5366.5 kHz (dipole ref.) |
| Spread spectrum | 10W PEP |
| Beacons | 100W PEP output |

### Band Restrictions
| Band | Restriction |
|------|------------|
| 80, 40, 20, 15m | Extra-only segments exist; Generals get upper voice portion |
| 30m | CW/data only, 200W, no phone/image |
| 60m | 4 channels (100W ERP) + 5351.5–5366.5 kHz (9.15W ERP), USB by convention, 2.8 kHz BW, record antenna gain |
| 10m repeaters | Above 29.5 MHz only |

### Key Numbers
| Item | Value |
|------|-------|
| Max antenna height without FAA/FCC | 200 feet |
| HF data bandwidth limit | 2.8 kHz (baud limits removed) |
| CSCE validity | 365 days |
| Minimum VE age | 18 years |
| VEs per exam session | 3 minimum |
| HF auto-beacon segment | 28.20–28.30 MHz |

---

## Where These Concepts Apply Later

- **Band allocations and frequency limits** → essential context for [G2 (Operating Procedures)](G2-operating-procedures.md) — you need to know where you can transmit before learning how
- **Power limits per band** → connects to [G5 (Electrical Principles)](G5-electrical-principles.md) power calculations and [G4 (Amateur Practices)](G4-amateur-practices.md) station setup
- **60m channels and bandwidth limits** → a unique case that ties rules to [G8 (Signals)](G8-signals-emissions.md) bandwidth and emission types
