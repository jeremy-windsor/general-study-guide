#!/usr/bin/env python3
"""Generate question files for each subelement from the 2023-2027 General pool JSON.

Reads pools/2023-2027/questions.json and outputs one markdown file per
subelement into subelements/, matching the existing study-guide format.
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parent.parent
POOL_PATH = REPO / "pools" / "2023-2027" / "questions.json"
OUTPUT_DIR = REPO / "subelements"

# Mapping of subelement IDs to output filenames (stem only)
SUBELEMENT_FILES = {
    "G0": "G0-electrical-rf-safety",
    "G1": "G1-commissions-rules",
    "G2": "G2-operating-procedures",
    "G3": "G3-radio-wave-propagation",
    "G4": "G4-amateur-radio-practices",
    "G5": "G5-electrical-principles",
    "G6": "G6-circuit-components",
    "G7": "G7-practical-circuits",
    "G8": "G8-signals-emissions",
    "G9": "G9-antennas-feed-lines",
}

# Group descriptions for the General 2023-2027 pool
GROUP_DESCRIPTIONS = {
    # G0 — Electrical and RF Safety
    "G0A": "Electrical safety; lightning and grounding; fusing",
    "G0B": "RF safety principles; rules and guidelines; routine station evaluation",
    # G1 — Commission's Rules
    "G1A": "General class control operator frequency privileges; primary and secondary allocations",
    "G1B": "Antenna structure limitations; good engineering and good amateur practice; beacon operation; prohibited transmissions; retransmitting radio signals",
    "G1C": "Transmitter power regulations; data emission standards",
    "G1D": "Volunteer Examiners and Volunteer Examiner Coordinators; temporary identification; element credit",
    "G1E": "Control categories; repeater regulations; third-party rules; ITU regions; automatically controlled digital station",
    # G2 — Operating Procedures
    "G2A": "Phone operating procedures; USB/LSB conventions; procedural signals; breaking into a contact; VOX operation",
    "G2B": "Operating courtesy; band plans; emergencies, including distress calling and detecting communications; RACES",
    "G2C": "CW operating procedures and prosigns; Q signals and common abbreviations; full break-in",
    "G2D": "Amateur satellite operation; Doppler shift; spin fading; LEO; HEO; orbital; telemetry",
    "G2E": "Digital operating: procedures,  modes, andடperformance; monitoring digital transmissions; digital message forwarding; Winlink",
    # G3 — Radio Wave Propagation
    "G3A": "Sunspots and solar radiation; ionospheric disturbances; propagation forecasting and indices",
    "G3B": "Maximum Usable Frequency; Lowest Usable Frequency; propagation; trans-equatorial; long-path; gray-line; multi-hop; scatter",
    "G3C": "Ionospheric layers; critical angle; critical frequency; HF scatter; near vertical incidence skywave (NVIS)",
    # G4 — Amateur Radio Practices
    "G4A": "Station operation and set up",
    "G4B": "Test and monitoring equipment; two-tone test",
    "G4C": "Interference to consumer electronics; grounding; shielding",
    "G4D": "Speech processors; S meters; sideband operation near band edges",
    "G4E": "HF mobile radio installations; alternative energy source operation",
    # G5 — Electrical Principles
    "G5A": "Reactance; inductance; capacitance; impedance; impedance matching",
    "G5B": "The decibel; current and voltage dividers; electrical power calculations; sine wave root-mean-square (RMS) values; PEP calculations",
    "G5C": "Resistors, capacitors, and inductors in series and parallel; transformers",
    # G6 — Circuit Components
    "G6A": "Resistors; capacitors; inductors; rectifiers; solid-state diodes and transistors; vacuum tubes; batteries",
    "G6B": "Analog and digital integrated circuits (ICs); microprocessors; memory; I/O devices; microwave ICs (MMICs); display devices; connectors; ferrite cores",
    # G7 — Practical Circuits
    "G7A": "Power supplies; schematic symbols",
    "G7B": "Digital circuits; flip-flops; counters; logic gates; programmable logic devices (PLDs); solid-state switches; LC and crystal oscillators",
    "G7C": "Receivers and transmitters;டlow-noise amplifiers; IF; mixing; oscillators; phase-locked loops; DSP; SDR fundamentals",
    # G8 — Signals and Emissions
    "G8A": "carriers and signals; modulation; AM; FM; single sideband; modulation envelope; digital modulation; overmodulation",
    "G8B": "Frequency mixing; multiplication; bandwidths of various modes; deviation; duty cycle; intermodulation",
    "G8C": "Digital emission modes; information rate vs bandwidth; error correction",
    # G9 — Antennas and Feed Lines
    "G9A": "Antenna feed point impedance; antenna efficiency; half-wavelength dipole; quarter-wavelength vertical; radiation patterns; polarization; effect of ground",
    "G9B": "Feed lines: types; attenuation vs. frequency; SWR concepts; SWR protection; weather protection; coaxial cable connectors",
    "G9C": "Directional antennas: Yagi; quad; stacking; NVIS; mobile; effects of ground; portable HF antennas",
    "G9D": "Specialized antennas: loop; Beverage; phased; multi-band; stealth; mobile and receive-only",
}

# ── Explanation generator ────────────────────────────────────────────
# Hand-written explanations for every question in the 2023-2027 General pool.
# Key = question ID, value = explanation paragraph.

EXPLANATIONS: dict[str, str] = {}


def _load_explanations() -> None:
    """Populate the EXPLANATIONS dict.

    The explanations are defined inline below rather than in a separate
    data file so the script is fully self-contained.
    """
    # fmt: off
    E = EXPLANATIONS

    # ── G1A — General Class Frequency Privileges ───────────────────

    E["G1A01"] = (
        "The four bands where General class licensees CANNOT transmit on certain portions are "
        "80 meters, 40 meters, 20 meters, and 15 meters. These are the same four bands that have "
        "segments reserved exclusively for Amateur Extra licensees (G1A08). On these bands, Generals "
        "get the upper portion of the voice segments (G1A11) but are locked out of the lower portions "
        "where the Extras operate. On all other HF/MF bands — 160m, 60m, 30m, 17m, 12m, and 10m — "
        "Generals have full privileges. Memory trick: the 'big four' bands (80, 40, 20, 15) are the "
        "ones with Extra-only segments."
    )

    E["G1A02"] = (
        "Phone (voice) operation is prohibited on the 30-meter band (10.1-10.15 MHz). The 30-meter "
        "band is a narrow allocation shared with government fixed services, and it's restricted to "
        "CW and data modes only — no phone, no image. This keeps transmissions narrow and reduces "
        "interference potential with the primary users. The 30-meter band is also limited to 200 watts "
        "PEP (G1C01). Think of 30 meters as the 'quiet, data-only' band. All the other listed bands "
        "(160m, 17m, 12m) allow phone operation."
    )

    E["G1A03"] = (
        "Image transmission is also prohibited on the 30-meter band, for the same reasons phone is "
        "banned (G1A02). Image modes like SSTV and FAX take up significant bandwidth — more than CW "
        "or narrow data modes — and the 30-meter band's narrow, shared allocation can't accommodate "
        "them. The rule is simple: on 30 meters, you get CW and data, nothing else. All the other "
        "bands listed (160m, 20m, 12m) permit image transmissions."
    )

    E["G1A04"] = (
        "The 60-meter band (5 MHz region) is restricted to specific channels rather than a continuous "
        "frequency range. Unlike every other amateur band where you can tune anywhere within the "
        "allocation, on 60 meters you must operate on one of five specific center frequencies: 5332, "
        "5348, 5358.5, 5373, and 5405 kHz. You're limited to USB phone and specific data modes with "
        "a maximum bandwidth of 2.8 kHz (G1C03) and 100 watts ERP (G1C09). The 60-meter band is "
        "shared with government users, and the channel-based allocation is the compromise that got "
        "amateurs access. The 11-meter band (27 MHz) is Citizens Band, not amateur."
    )

    E["G1A05"] = (
        "General class licensees are prohibited from operating on 7.125 MHz to 7.175 MHz — this is "
        "the Extra-only portion of the 40-meter phone band. To remember: the General class 40-meter "
        "phone privileges start at 7.175 MHz and go up to 7.300 MHz. The segment below 7.175 (down "
        "to 7.125) is reserved for Extra class. The other choices are all frequencies where Generals "
        "CAN operate: 28.000-28.025 MHz is in the 10-meter band (full privileges), and 21.275-21.300 "
        "MHz is in the General portion of 15 meters."
    )

    E["G1A06"] = (
        "When the amateur service is a secondary user on a band, amateurs must not cause harmful "
        "interference to primary users AND must accept interference from primary users. This is the "
        "fundamental definition of secondary status in spectrum allocation. You don't get to complain "
        "about interference from primary users — you're a guest on their spectrum. And you must "
        "immediately stop transmitting if you're interfering with a primary user. There's no "
        "requirement to record call signs, no restriction to emergencies only, and no specific hours "
        "of operation. Secondary status means: play nice, and if there's a conflict, you lose."
    )

    E["G1A07"] = (
        "General class operators can transmit CW on the ENTIRE 10-meter band (28.000-29.700 MHz). "
        "The 10-meter band has no Extra-only segments at all — every license class from General up "
        "has full access to the entire band. CW is permitted everywhere on 10 meters (and on most "
        "bands, CW is always allowed anywhere you have privileges). The specific sub-bands like "
        "28.000-28.300 apply to phone and data restrictions, but CW has no such limitations on 10m."
    )

    E["G1A08"] = (
        "The four HF bands with segments exclusively allocated to Amateur Extra licensees are "
        "80 meters, 40 meters, 20 meters, and 15 meters — the same 'big four' bands from G1A01. "
        "On each of these bands, the bottom portion of the voice segment is reserved for Extras only. "
        "For example, on 20 meters, Extras get 14.150-14.175 MHz exclusively, while Generals start "
        "at 14.175 MHz. Notice the pattern: every band that has General restrictions (G1A01) is the "
        "same band that has Extra-only segments. The other bands (160m, 60m, 30m, 17m, 12m, 10m) "
        "have no Extra-only segments."
    )

    E["G1A09"] = (
        "21,300 kHz (21.300 MHz) is within the General class portion of the 15-meter band. The "
        "General class phone privileges on 15 meters run from 21.275 to 21.450 MHz. The key is "
        "knowing your band edges: 21.300 MHz is clearly within that range. The other choices are "
        "traps: 14,250 kHz (14.250 MHz) is 20 meters but falls in the Extra-only segment below "
        "14.275 MHz. 18,155 kHz is 17 meters (where Generals do have full privileges, but it's not "
        "15 meters). 24,900 kHz is 12 meters (again, full General privileges, but not 15m). The "
        "question specifically asks about the 15-meter band."
    )

    E["G1A10"] = (
        "The portion of the 10-meter band available for repeater use is above 29.5 MHz. Repeater "
        "operation on 10 meters is confined to the top of the band (29.5-29.7 MHz) to keep "
        "repeater operations separated from simplex activity. The 10-meter FM repeater sub-band "
        "uses channels with 100 kHz spacing. This is a common exam question because 10 meters is "
        "one of the few HF bands with repeater activity — most repeaters operate on VHF/UHF, but "
        "10 meters has enough bandwidth to support them in this small slice at the top."
    )

    E["G1A11"] = (
        "When General class licensees are restricted on a voice band, they get the UPPER frequency "
        "portion. This is consistent across all four restricted bands (80m, 40m, 20m, 15m). Extras "
        "get the lower portion of the voice segment, Generals get the upper portion. For example, on "
        "20-meter phone: Extras start at 14.150 MHz, Generals start at 14.225 MHz, and both go up "
        "to 14.350 MHz. The pattern is always the same — Generals are pushed to the upper portion. "
        "This is a straightforward memorization point with no exceptions."
    )

    # ── G1B — Antenna Structures, Good Practice, Beacons, Prohibited Transmissions ──

    E["G1B01"] = (
        "The maximum antenna height without requiring FAA notification and FCC registration is "
        "200 feet above ground level. This applies to antenna structures NOT near a public-use "
        "airport. If your antenna is under 200 feet and away from airports, you don't need to notify "
        "the FAA or register with the FCC. Once you exceed 200 feet, you must file with the FAA "
        "(who evaluates whether the structure is a hazard to air navigation) and register the "
        "structure with the FCC. Note: being NEAR an airport changes everything — even short "
        "towers may require notification depending on proximity and runway configuration."
    )

    E["G1B02"] = (
        "No more than one beacon station may transmit in the same band from the same station "
        "location. This prevents a single operator from monopolizing beacon frequencies across "
        "multiple beacons at one site. One location, one beacon per band. There is no 'National "
        "Beacon Organization' that coordinates frequencies, and there's no requirement to post "
        "frequencies on the internet or in publications. The rule is simply: one beacon per band "
        "per location."
    )

    E["G1B03"] = (
        "A beacon station's purpose is observation of propagation and reception. Beacons are "
        "automated transmitters that send signals (usually CW) continuously or on a schedule so "
        "that distant stations can determine whether a band is open. If you can hear a beacon in "
        "Australia on 20 meters, you know the band is open to Australia. The International Beacon "
        "Project (NCDXF/IARU) runs a network of beacons on 14.100, 18.110, 21.150, 24.930, and "
        "28.200 MHz (G1E10). Beacons are NOT for repeater identification, and NOT for transmitting "
        "bulletins — they exist purely for propagation observation."
    )

    E["G1B04"] = (
        "Amateur stations are permitted to occasionally retransmit weather and propagation forecast "
        "information from US government stations (like NOAA weather radio). The key word is "
        "'occasional' — you can relay a severe weather warning during a net, for example, but you "
        "can't just rebroadcast NOAA continuously. The other choices describe things that are NOT "
        "permitted: unidentified transmissions are never allowed (you must always identify), "
        "automatic retransmission of amateur signals requires specific authorization, and encrypted "
        "messages are generally prohibited in the amateur service."
    )

    E["G1B05"] = (
        "Transmissions to assist with learning the International Morse code are permitted as "
        "one-way transmissions. Practice code transmissions are a recognized and encouraged activity "
        "in amateur radio — organizations like W1AW send regular code practice sessions. Unidentified "
        "test transmissions are NOT permitted (you must always identify, even during testing). Regular "
        "equipment-for-sale transmissions aren't permitted as one-way broadcasts (that would be "
        "commercial use). One-way transmissions are generally prohibited in amateur radio, but code "
        "practice is a specific exception."
    )

    E["G1B06"] = (
        "State and local governments may regulate amateur radio antenna structures, but they must "
        "reasonably accommodate amateur communications and their regulations must be the minimum "
        "practical to achieve a legitimate purpose. This comes from the FCC's PRB-1 declaratory "
        "ruling (1985), which established that while state and local governments CAN regulate "
        "antennas (the FCC doesn't completely preempt them), they can't impose blanket bans or "
        "unreasonable restrictions. They must balance their legitimate concerns (safety, aesthetics) "
        "against the federally licensed amateur's need to communicate. It's NOT true that FCC rules "
        "always take priority with no exceptions — local governments do have some authority, just "
        "limited authority."
    )

    E["G1B07"] = (
        "Abbreviations and procedural signals may be used in the amateur service as long as they "
        "do not obscure the meaning of a message. This is a common-sense rule — you can use Q "
        "signals, prosigns, abbreviations, and shorthand freely as long as your communication "
        "remains understandable. There's no restriction to only 'Q' signals, no blanket prohibition, "
        "and no requirement that abbreviations be listed in Part 97. The rule is about intent: "
        "don't use codes or abbreviations to hide the meaning of your transmissions (that would "
        "approach encryption, which IS prohibited)."
    )

    E["G1B08"] = (
        "You may communicate with amateur stations in any country EXCEPT those whose administrations "
        "have notified the ITU that they object to such communications. Most countries allow amateur "
        "radio contacts with US stations. A few (like North Korea) have filed objections with the "
        "ITU. You don't need a formal third-party agreement just to make a contact — that's only "
        "required for passing third-party messages (G1E05). UN membership and IARU membership are "
        "irrelevant to whether you can contact a station in that country. The restriction is "
        "specifically about ITU notifications of objection."
    )

    E["G1B09"] = (
        "Automatically controlled beacons on HF are permitted only on 28.20 MHz to 28.30 MHz. This "
        "is a very specific, narrow allocation within the 10-meter band. The 10-meter band was "
        "chosen because its propagation characteristics are most variable — beacons there are most "
        "useful for detecting band openings. The NCDXF/IARU beacon network operates beacons on "
        "28.200 MHz (among other frequencies) within this segment. Automatically controlled beacons "
        "are NOT permitted on just any HF frequency at low power — the rules specify this exact "
        "sub-band."
    )

    E["G1B10"] = (
        "The power limit for beacon stations is 100 watts PEP output. Beacons don't need high "
        "power — they use CW (which is efficient) and are designed to be heard when propagation "
        "supports it. If you can hear a 100-watt beacon halfway around the world, you know the "
        "band is open. Higher power would cause unnecessary interference. Most beacons actually "
        "run well under 100 watts, with many NCDXF beacons running stepped power from 0.1W to 100W "
        "to help gauge signal strength. The key number to remember: 100 watts PEP output."
    )

    E["G1B11"] = (
        "The FCC determines what constitutes 'good engineering and good amateur practice' for "
        "situations not specifically covered by Part 97 rules. This is a catch-all provision — "
        "the FCC can't write rules for every possible scenario, so they reserve the authority to "
        "decide what's appropriate on a case-by-case basis. It's NOT up to the individual control "
        "operator to decide (though operators should use good judgment), NOT the IEEE (an "
        "engineering standards body with no regulatory authority), and NOT the ITU (which sets "
        "international frameworks, not US amateur operating standards). The FCC has the final say."
    )

    # ── G1C — Transmitter Power, Data Emission Standards ─────────────

    E["G1C01"] = (
        "The maximum transmitter power on 10.140 MHz is 200 watts PEP output. 10.140 MHz is in "
        "the 30-meter band (10.100-10.150 MHz), and the entire 30-meter band is limited to 200 watts "
        "PEP because amateurs share it with government fixed stations as secondary users. This lower "
        "power limit reduces the potential for interference with primary users. Remember the pair: "
        "30 meters = 200 watts AND data/CW only (no phone, G1A02). The 30-meter band has the most "
        "restrictions of any HF band: low power, no voice, no images, secondary status."
    )

    E["G1C02"] = (
        "The maximum transmitter power on the 12-meter band is 1500 watts PEP output — the standard "
        "amateur maximum. Most HF bands allow 1500 watts PEP unless there's a specific restriction. "
        "The bands with LOWER limits are the exceptions you need to memorize: 30 meters (200W, "
        "G1C01) and 60 meters (100W ERP, G1C09). Every other HF band — including 12 meters — "
        "allows the full 1500 watts."
    )

    E["G1C03"] = (
        "The maximum bandwidth on USB frequencies in the 60-meter band is 2.8 kHz. The 60-meter "
        "band operates on specific channels (G1A04) using Upper Sideband, and each channel has a "
        "maximum occupied bandwidth of 2.8 kHz — which is the standard bandwidth of an SSB voice "
        "signal. This means you can use voice or data modes as long as the total occupied bandwidth "
        "stays within 2.8 kHz of the channel center frequency. Going wider would splatter into "
        "adjacent channels used by government stations. The 2.8 kHz limit is specific to 60 meters."
    )

    E["G1C04"] = (
        "If you're using an antenna other than a dipole on the 60-meter band, you must keep a "
        "record of the gain of your antenna. This unique requirement exists because 60-meter power "
        "is measured as ERP (Effective Radiated Power) relative to a dipole (G1C09). If you use a "
        "beam antenna with 6 dBd of gain, your transmitter power must be reduced so the ERP doesn't "
        "exceed 100 watts. Keeping a record of antenna gain proves you're doing the math correctly. "
        "With a dipole, no record is needed because the ERP equals the transmitter output. This "
        "requirement is unique to 60 meters — no other band requires logging your antenna gain."
    )

    E["G1C05"] = (
        "The transmitter power limit on the 28 MHz (10-meter) band for a General class control "
        "operator is 1500 watts PEP output. The 10-meter band has no special power restrictions — "
        "it uses the standard amateur maximum of 1500 watts PEP. Remember, the only HF bands with "
        "reduced power limits are 30 meters (200W) and 60 meters (100W ERP). Everything else, "
        "including 10 meters, gets the full 1500 watts."
    )

    E["G1C06"] = (
        "The transmitter power limit on the 1.8 MHz (160-meter) band is 1500 watts PEP output. "
        "Same as 10 meters — the full amateur maximum. Despite 160 meters being shared with other "
        "services in some areas, there's no general power reduction for the band. The only bands "
        "with power restrictions below 1500 watts are 30 meters (200W) and 60 meters (100W ERP). "
        "Don't let the low frequency fool you — you can run full legal limit on 160 meters."
    )

    E["G1C07"] = (
        "Before using a new digital protocol on the air, you must publicly document the technical "
        "characteristics of the protocol. This rule exists because amateur radio is a non-encrypted, "
        "transparent service — anyone must be able to decode your transmissions. If you invent a "
        "new digital mode, publishing the technical specs ensures that other amateurs (and the FCC) "
        "can monitor and decode your signals. You don't need FCC type certification, don't need an "
        "experimental license, and don't need to submit a rule-making petition. Just document it "
        "publicly and you're good to go."
    )

    E["G1C08"] = (
        "The maximum symbol rate for RTTY or data emissions below 28 MHz is 300 baud. This limit "
        "keeps digital signals narrow on the HF bands where spectrum is scarce and shared. 300 baud "
        "is adequate for modes like RTTY (45.45 baud), PSK31 (31.25 baud), and even some faster "
        "modes, but it prevents wide-bandwidth digital signals from occupying excessive spectrum. "
        "Compare this to the 10-meter band, where the limit is 1200 baud (G1C10) — four times "
        "faster, reflecting 10 meters' wider allocation. The 300-baud limit applies to ALL HF "
        "bands below 28 MHz."
    )

    E["G1C09"] = (
        "The maximum power on the 60-meter band is ERP of 100 watts PEP with respect to a dipole. "
        "This is unique for two reasons: it's measured as ERP (not transmitter output), and it's "
        "referenced to a dipole (dBd), not an isotropic antenna (dBi). ERP means the power that "
        "would produce the same field strength as a dipole fed with that power. If you use a dipole, "
        "your transmitter can output 100 watts. If you use a 3 dBd gain antenna, you must cut your "
        "transmitter power to 50 watts so the ERP stays at 100W. This is why G1C04 requires you to "
        "log your antenna gain if it's not a dipole."
    )

    E["G1C10"] = (
        "The maximum symbol rate for RTTY or data emissions on the 10-meter band is 1200 baud. "
        "This is four times the limit below 28 MHz (300 baud, G1C08). The 10-meter band gets a "
        "higher symbol rate limit because it has more bandwidth available and historically has been "
        "used for higher-speed data experimentation. Remember the pair: below 28 MHz = 300 baud, "
        "10 meters (28 MHz) = 1200 baud. On VHF and above, the limits are even higher or "
        "unrestricted."
    )

    E["G1C11"] = (
        "FCC rules regulate maximum power as PEP output from the transmitter. PEP (Peak Envelope "
        "Power) is measured at the transmitter output — not at the antenna input, not as RMS, and "
        "not as average power. PEP is the average power during one RF cycle at the crest of the "
        "modulation envelope. This is important because feed line losses between the transmitter and "
        "antenna don't count — you're measured at the transmitter output. And it's PEP, not RMS or "
        "average, which means your SSB transmitter is rated at its peak voice power, not its "
        "average-during-speech power. The one exception: 60 meters measures ERP at the antenna "
        "(G1C09), not PEP at the transmitter."
    )

    # ── G1D — Volunteer Examiners, Temporary ID, Element Credit ──────

    E["G1D01"] = (
        "Any person who can demonstrate they once held an FCC-issued General, Advanced, or Amateur "
        "Extra class license that was not revoked may receive partial credit for the elements "
        "represented by that expired license. The key phrase is 'not revoked' — if the FCC took "
        "your license away for rules violations, you don't get credit. But if it simply expired "
        "(even decades ago), you can get credit for the written exam elements you already passed. "
        "This applies to General, Advanced, and Extra class — NOT to Novice or Technician class. "
        "There's no time limit on how long ago the license expired, and foreign licenses don't "
        "count for this credit."
    )

    E["G1D02"] = (
        "A General class Volunteer Examiner may administer Technician exams only. The rule is: you "
        "can only administer exams for license classes BELOW your own. General is one step above "
        "Technician, so that's the only exam you can give. You cannot administer General exams "
        "(that's your own class) or Extra exams (that's above you). To administer General and "
        "Extra exams, you need to be an Amateur Extra class VE. This prevents the obvious conflict "
        "of someone proctoring their own level of exam."
    )

    E["G1D03"] = (
        "A Technician with a valid CSCE for General class privileges may operate on any General or "
        "Technician class band segment immediately. The CSCE (Certificate of Successful Completion "
        "of Examination) grants you operating privileges right away — you don't have to wait for "
        "the FCC database to update. You DO need to identify with the temporary '/AG' suffix until "
        "the upgrade appears in the FCC database (G1D06), but you can start using your new "
        "privileges immediately. No bands are excluded — you get the full General class allocation "
        "including 30 and 60 meters."
    )

    E["G1D04"] = (
        "At least three Volunteer Examiners of General class or higher must observe the "
        "administration of a Technician class exam. The magic number is THREE — every amateur radio "
        "exam session requires a minimum of three VEs. For a Technician exam, those VEs must hold "
        "General class or higher licenses. For General and Extra exams, all three VEs must hold "
        "Extra class licenses (since you can only administer exams below your own class, G1D02). "
        "Two VEs isn't enough, and Technician class VEs can't administer any exam."
    )

    E["G1D05"] = (
        "When operating a US station by remote control from outside the country, the control "
        "operator needs a US operator/primary station license — period. No special permits, no "
        "foreign licenses, nothing extra. If you're a US-licensed amateur sitting in England and "
        "controlling your home station in Texas via the internet, your US license is all you need. "
        "The station is in the US, you're a US licensee, and the rules are straightforward. "
        "The key concept: the rules that apply are based on where the STATION is located, not "
        "where the operator is sitting."
    )

    E["G1D06"] = (
        "A Technician licensee with a General class CSCE must identify with 'AG' after their call "
        "sign whenever they operate using General class frequency privileges. The AG identifier "
        "tells other stations and the FCC that this operator has passed the General exam but the "
        "upgrade hasn't been posted in the database yet. You only need to use AG when operating on "
        "General-class frequencies — if you're operating within Technician band segments, your "
        "regular call sign is sufficient. Once the FCC database shows your General class license, "
        "you drop the AG and use your regular call sign everywhere."
    )

    E["G1D07"] = (
        "Volunteer Examiners are accredited by a Volunteer Examiner Coordinator (VEC). The VEC is "
        "the organization that coordinates exam sessions — examples include the ARRL VEC, W5YI VEC, "
        "and Laurel VEC. The VEC accredits individual VEs, coordinates session logistics, and "
        "processes license applications to the FCC. The FCC itself doesn't directly accredit VEs — "
        "it delegated that responsibility to VECs. The Universal Licensing System (ULS) is the FCC's "
        "database system, and the Wireless Telecommunications Bureau is an FCC division — neither "
        "accredits VEs."
    )

    E["G1D08"] = (
        "A non-US citizen can be an accredited Volunteer Examiner if they hold an FCC-granted "
        "amateur radio license of General class or above. Citizenship doesn't matter — what matters "
        "is having the appropriate FCC license. If a Canadian citizen holds an FCC General or Extra "
        "license, they can serve as a VE under the same rules as a US citizen. There's no residency "
        "requirement, no ITU region restriction, and non-US citizens are NOT automatically "
        "disqualified. The requirement is: FCC license of appropriate class + minimum age of 18 "
        "(G1D10) + VEC accreditation."
    )

    E["G1D09"] = (
        "A Certificate of Successful Completion of Examination (CSCE) is valid for exam element "
        "credit for 365 days. You have one year to use your CSCE — whether that means upgrading "
        "to the next class or getting credit for a passed element at a future exam session. If you "
        "pass Element 3 (General) but don't get it processed within 365 days, you'd need to retake "
        "the exam. The 365-day validity applies to the CSCE itself, not to the license — once your "
        "license is granted, it follows normal 10-year renewal cycles."
    )

    E["G1D10"] = (
        "The minimum age to qualify as an accredited Volunteer Examiner is 18 years. There's no "
        "minimum age to GET a license (a 5-year-old can hold an Extra class license), but to "
        "ADMINISTER exams as a VE, you must be at least 18. This makes sense — VEs are acting in "
        "an official capacity, verifying identities and certifying exam results. The 18-year "
        "requirement ensures a level of legal responsibility. Remember: any age to take the exam, "
        "18+ to give the exam."
    )

    E["G1D11"] = (
        "To obtain a new General class license after a previously held license has expired and the "
        "two-year grace period has passed, the applicant must show proof of the expired license "
        "grant AND pass the current Element 2 (Technician) exam. You get credit for the General "
        "element you already passed (thanks to G1D01 — expired license element credit), but you "
        "still need to demonstrate current knowledge by passing the Technician exam. You can't "
        "just contact the FCC to reinstate, and a copy of the expired license alone isn't enough — "
        "you must actually sit for and pass Element 2."
    )

    E["G1D12"] = (
        "When operating a station in South America by remote control from the US, only the "
        "regulations of the remote station's country apply. The station is physically located in "
        "South America, transmitting from South America, and the signals originate in that country — "
        "so that country's rules govern. This is different from G1D05 where the station was IN "
        "the US (US rules apply). The principle: regulations follow the station's physical location, "
        "not the operator's location. If the remote station is in Brazil, Brazilian amateur radio "
        "regulations apply — regardless of where you're sitting when you press the PTT button."
    )

    # ── G1E — Control Categories, Repeaters, Third-Party, ITU Regions ──

    E["G1E01"] = (
        "A third party whose amateur license has been revoked and not reinstated is disqualified "
        "from participating in sending a message via an amateur station. If the FCC revoked your "
        "license, you're specifically prohibited from amateur radio participation — even as a third "
        "party using someone else's station. Non-US citizenship is NOT a disqualifier (anyone can "
        "be a third party), and speaking a non-English language is NOT prohibited (amateur radio "
        "has no English-only requirement). The ONLY disqualifier listed is having a revoked license. "
        "The idea is that if the FCC banned you from amateur radio, you can't sneak back in through "
        "someone else's microphone."
    )

    E["G1E02"] = (
        "A 10-meter repeater may retransmit a 2-meter signal from a Technician operator only if "
        "the 10-meter repeater control operator holds at least a General class license. Here's why: "
        "the Technician licensee has privileges on 2 meters but NOT on 10 meters. The repeater's "
        "output is on 10 meters, which requires General class or higher privileges. The control "
        "operator of the 10-meter repeater must hold a license that covers 10-meter operation — at "
        "least General class. The Technician operator is fine on the 2-meter input; the General class "
        "control operator authorizes the 10-meter output. This is a classic control operator "
        "privilege question."
    )

    E["G1E03"] = (
        "To communicate with an automatically controlled digital station operating outside the "
        "automatic control band segments, the station initiating the contact must be under local "
        "or remote control (meaning a human is at the controls). Automatic control outside the "
        "designated auto-control segments is allowed, but only if a human-controlled station "
        "initiates the contact. This prevents two unattended stations from starting conversations "
        "on bands where automatic operation isn't normally permitted. Once the human-initiated "
        "contact is established, the auto-controlled station can respond. The interrogating station "
        "doesn't need an Extra class license, and the contact can include third-party traffic "
        "under normal third-party rules."
    )

    E["G1E04"] = (
        "ALL of the listed conditions require specific steps to avoid harmful interference: "
        "operating within one mile of an FCC Monitoring Station (your signal could overload their "
        "sensitive receivers), using a band where the amateur service is secondary (you must defer "
        "to primary users, G1A06), and transmitting spread spectrum emissions (which have special "
        "requirements under Part 97). Each of these situations has specific rules about interference "
        "avoidance. The correct answer is 'All these choices are correct' — there's no trick here, "
        "all three conditions genuinely require interference-avoidance measures."
    )

    E["G1E05"] = (
        "Third-party messages to countries with which the US has a Third-Party Agreement must relate "
        "to amateur radio, or be remarks of a personal character, or relate to emergencies or "
        "disaster relief. You can't conduct business, advertise, or send commercial messages — but "
        "you can pass personal greetings, discuss amateur radio topics, or handle emergency traffic. "
        "The messages don't have to be limited to emergencies only (that's too restrictive) and "
        "don't have to be for licensed amateurs (the whole point of third-party traffic is involving "
        "non-licensees). There's no 1-minute time limit. The rules strike a balance: personal and "
        "amateur-related messages are fine, commercial messages are not."
    )

    E["G1E06"] = (
        "ITU Region 2 covers North and South America (plus Hawaii and the Caribbean). The ITU "
        "divides the world into three regions for frequency allocation purposes: Region 1 is "
        "Europe, Africa, the Middle East, and northern Asia. Region 2 is the Americas. Region 3 "
        "is southern Asia, Australia, and the Pacific. There is no Region 4. Amateur band "
        "allocations differ between regions — for example, the 40-meter band extends to 7.200 MHz "
        "in Region 2 but only to 7.100 MHz in Region 1. Knowing you're in Region 2 matters for "
        "understanding your frequency allocations and for operating in other regions."
    )

    E["G1E07"] = (
        "Amateur stations may NOT communicate with non-licensed Wi-Fi stations on any part of the "
        "2.4 GHz band. Even though amateurs share the 2.4 GHz band with Wi-Fi (G8C01), the amateur "
        "service and the unlicensed Wi-Fi service are separate services under different rule parts. "
        "Amateur stations must comply with Part 97, and non-licensed Wi-Fi stations operate under "
        "Part 15. Intentional communication between the two services isn't permitted. You CAN use "
        "amateur mesh networking equipment on 2.4 GHz to communicate with OTHER amateur stations, "
        "but not with your neighbor's Wi-Fi router."
    )

    E["G1E08"] = (
        "The maximum PEP output for spread spectrum transmissions is 10 watts. Spread spectrum is "
        "a technique that spreads the signal across a wide bandwidth, and the low power limit "
        "ensures the spectral power density stays low enough to minimize interference. 10 watts is "
        "quite restrictive compared to the normal 1500-watt limit, reflecting the unique interference "
        "potential of wideband transmissions. Spread spectrum is also restricted to frequencies above "
        "222 MHz. The low power limit, combined with the wide bandwidth, means the actual power "
        "density per hertz is extremely low."
    )

    E["G1E09"] = (
        "Digital mode messages are NEVER exempt from Part 97 third-party rules — under no "
        "circumstances. The same third-party rules that apply to phone and CW apply equally to "
        "digital modes. Just because your message goes through a computer rather than a microphone "
        "doesn't change the regulatory framework. Whether it's encrypted, unencrypted, under "
        "automatic control, or manually controlled — third-party rules apply. This is a clear-cut "
        "'no exceptions' answer. Some people assume digital modes get special treatment, but the "
        "FCC rules apply uniformly across all modes."
    )

    E["G1E10"] = (
        "Amateur operators should avoid transmitting on 14.100, 18.110, 21.150, 24.930, and "
        "28.200 MHz because a system of propagation beacon stations operates on those frequencies. "
        "These are the frequencies used by the NCDXF/IARU International Beacon Project — a network "
        "of 18 synchronized beacons worldwide that transmit on a precise schedule. Transmitting on "
        "these frequencies would interfere with propagation monitoring. While it's not technically "
        "illegal to transmit there, it's strongly discouraged as a matter of good operating practice "
        "(G1B11). These frequencies are easy to remember: one per WARC and upper HF band."
    )

    E["G1E11"] = (
        "Automatically controlled stations transmitting RTTY or data may communicate with other "
        "automatically controlled digital stations anywhere in the 6-meter or shorter wavelength "
        "bands, and in limited segments of some HF bands. The rules designate specific HF sub-bands "
        "for automatic digital operation — you can't just park an unattended digital station "
        "anywhere on HF. On VHF and above (6 meters and shorter), the restrictions are much more "
        "relaxed. This tiered approach reflects the difference in spectrum availability: HF spectrum "
        "is scarce and shared, while VHF/UHF has plenty of room for automated stations."
    )

    E["G1E12"] = (
        "Third-party messages may be transmitted via remote control under any circumstances where "
        "third-party messages are normally permitted. Remote control doesn't add any extra "
        "restrictions to third-party traffic. If you could pass a third-party message while sitting "
        "in front of your radio, you can pass the same message while controlling the radio remotely. "
        "Remote control doesn't change the nature of the communication — it just changes where the "
        "operator is sitting. The same rules about third-party agreements (G1E05), permitted content, "
        "and control operator responsibility apply regardless of whether control is local or remote."
    )

    # ── G2A — Phone Operating Procedures, USB/LSB Conventions ────────

    E["G2A01"] = (
        "Upper sideband (USB) is the standard mode for voice on frequencies of 14 MHz and higher. "
        "This is one of the most fundamental operating conventions in amateur radio — it's not a "
        "regulation, just universally accepted practice (G2A09). The dividing line is roughly "
        "10 MHz: above that, use USB. Below that (160m, 75/80m, 40m), use LSB (G2A02). The "
        "17-meter and 12-meter bands (G2A04) are above 14 MHz, so they follow the USB convention "
        "too. VHF and UHF SSB also uses USB (G2A03). Memory trick: Upper bands = Upper sideband."
    )

    E["G2A02"] = (
        "Lower sideband (LSB) is the standard mode for voice on the 160-, 75-, and 40-meter bands. "
        "These are the low HF bands — below 10 MHz — and the convention is LSB. Why? It's purely "
        "historical tradition (G2A09), not a technical requirement. Early SSB equipment on these "
        "bands happened to use LSB, and the convention stuck. The key dividing line: below 10 MHz "
        "= LSB, above 10 MHz = USB. Both sidebands work equally well technically — it's just "
        "that everyone needs to agree so you can actually understand each other."
    )

    E["G2A03"] = (
        "Upper sideband (USB) is the standard for SSB voice on VHF and UHF. Since VHF starts at "
        "50 MHz and UHF at 420 MHz, these are well above the 10 MHz dividing line, so USB is the "
        "convention. VHF/UHF SSB is used primarily for weak-signal work — mountaintopping, "
        "meteor scatter, EME (moonbounce), and tropospheric ducting contacts. FM dominates VHF/UHF "
        "for local repeater work, but when you switch to SSB for weak signals, it's always USB."
    )

    E["G2A04"] = (
        "Upper sideband (USB) is the standard for voice on the 17- and 12-meter bands. The "
        "17-meter band is at 18.068 MHz and 12 meters is at 24.890 MHz — both well above the "
        "10 MHz dividing line. These WARC bands (named for the 1979 World Administrative Radio "
        "Conference that created them) follow the same USB convention as 20 meters and above. "
        "Quick summary: 160m, 75/80m, 40m = LSB. Everything else (20m and up, plus VHF/UHF) = USB."
    )

    E["G2A05"] = (
        "Single sideband (SSB) is the most commonly used voice mode on HF. Not AM, not FM — SSB. "
        "From G2A06 and G8A07, SSB uses less bandwidth than AM or FM and is more power-efficient "
        "(all the transmitter power goes into the information-carrying sideband rather than being "
        "wasted on a carrier). On HF, where spectrum is scarce and every decibel counts for DX, "
        "SSB is king. FM is used for VHF/UHF repeaters. AM has a small following among enthusiasts "
        "but isn't mainstream. 'Single phase modulation' isn't a real mode."
    )

    E["G2A06"] = (
        "The key advantages of SSB over other analog voice modes on HF are less bandwidth used "
        "AND greater power efficiency. SSB occupies about 2.4 kHz — less than half of AM's ~6 kHz "
        "(G8A07). And since SSB suppresses the carrier (which contains no information), ALL of the "
        "transmitter power goes into the sideband carrying your voice. In AM, roughly 2/3 of the "
        "power is wasted on the carrier. SSB is NOT higher fidelity than AM (it's actually lower), "
        "NOT less subject to static (static affects all modes similarly), and NOT easier to tune "
        "(SSB requires more careful tuning than AM). It wins on efficiency, not audio quality."
    )

    E["G2A07"] = (
        "In SSB, only one sideband is transmitted — the other sideband AND the carrier are both "
        "suppressed. This is the definition of single sideband: you take the output of a balanced "
        "modulator (which produces both sidebands with no carrier, from G7C02) and filter out one "
        "sideband (G7C01), leaving just one sideband. The receiver reinserts the carrier using a "
        "BFO/product detector (G7C04) to make the audio intelligible. Choice A is wrong because "
        "the carrier is NOT transmitted — if it were, that would be a different mode. SSB is also "
        "not the 'only voice mode authorized' on any band — AM and FM are also permitted."
    )

    E["G2A08"] = (
        "To break into an ongoing phone contact, simply say your call sign once. That's it — "
        "clean, professional, and minimally disruptive. The stations in the QSO will hear you, "
        "acknowledge you when there's a natural pause, and invite you in. 'QRZ' means 'who is "
        "calling me?' — that's what you send when YOU hear someone calling, not when you want to "
        "break in. 'Breaker Breaker' is CB radio culture, not amateur radio. And calling CQ is "
        "for initiating new contacts, not breaking into existing ones. One call sign, once. Done."
    )

    E["G2A09"] = (
        "The reason for using LSB on 160/75/40 meters is simply commonly accepted amateur practice "
        "— it's convention, not regulation. There's no law requiring LSB on these bands, and LSB "
        "isn't technically 'better' at lower frequencies. The convention dates back to early SSB "
        "equipment designs in the 1950s-60s. Some early filter-type SSB generators on the lower "
        "bands produced LSB more conveniently, and the practice became universal. The FCC doesn't "
        "mandate which sideband to use — but if you transmit USB on 75 meters, nobody will "
        "understand you because they're all listening on LSB."
    )

    E["G2A10"] = (
        "VOX (Voice-Operated Transmit) allows 'hands free' operation — the transmitter keys "
        "automatically when you speak into the microphone. With PTT (Push-To-Talk), you press a "
        "button to transmit and release it to receive. VOX frees your hands for logging, tuning, "
        "or adjusting controls while talking. It does NOT make received audio more natural, does "
        "NOT reduce bandwidth, and does NOT provide more power output. The tradeoff: VOX can be "
        "triggered by background noise or receiver audio (unless the VOX delay and anti-VOX are "
        "properly adjusted). Many operators use VOX for ragchewing and PTT for contests."
    )

    E["G2A11"] = (
        "When a station in the contiguous 48 states calls 'CQ DX,' they're specifically looking "
        "for distant contacts — stations OUTSIDE the lower 48 states. 'DX' means distance, and "
        "from a US perspective, that includes Alaska, Hawaii, US territories, and all foreign "
        "countries. If you're also in the lower 48, don't answer a CQ DX call — the calling "
        "station isn't looking for you. It's not restricted to only Germany or only contest "
        "stations — any station outside the lower 48 qualifies. This is operating courtesy, not "
        "a regulation — but violating it will earn you no friends."
    )

    E["G2A12"] = (
        "The transmit audio or microphone gain control is what you adjust for proper ALC setting. "
        "ALC (Automatic Level Control) prevents your transmitter from being overdriven, which "
        "causes splatter and distortion (G8A08, G8A10). You set mic gain so the ALC meter shows "
        "activity on voice peaks but doesn't slam to maximum. Too much mic gain = ALC constantly "
        "pegged = flat-topping and excessive bandwidth. RF clipping is a speech processor function, "
        "not an ALC adjustment. Antenna tuning affects SWR, not ALC. And attenuator level is a "
        "receive function. The mic gain knob is your primary ALC control."
    )

    # ── G2B — Operating Courtesy, Band Plans, Emergencies, RACES ─────

    E["G2B01"] = (
        "Except during emergencies, no amateur station has priority access to any frequency. This "
        "is a foundational principle from Part 97.101 — the amateur bands are shared equally. Nets "
        "don't get priority. A QSO already in progress doesn't get priority. Contest stations "
        "don't yield to non-contest stations (or vice versa). Everyone shares. The only exception "
        "is emergencies — stations providing emergency communications DO get priority. This "
        "principle encourages cooperation and courtesy rather than turf wars over frequencies."
    )

    E["G2B02"] = (
        "If you hear a station in distress break into your contact, the FIRST thing to do is "
        "acknowledge the station in distress and determine what assistance may be needed. Don't "
        "go off to call the emergency coordinator (the distressed station needs help NOW). Don't "
        "decrease power (they need to hear you). Don't cease all transmissions (silence doesn't "
        "help anyone). You acknowledge them, find out what's happening, and then coordinate "
        "whatever assistance is needed — which might include relaying to emergency services, "
        "clearing the frequency for emergency traffic, or providing direct assistance."
    )

    E["G2B03"] = (
        "If propagation changes cause interference with other stations on your frequency, good "
        "practice is to attempt to resolve the problem in a mutually acceptable manner. This means "
        "talking it out — maybe one station moves, maybe you take turns, maybe you find a "
        "compromise. You do NOT claim priority and tell others to leave (G2B01 — no one has "
        "priority). Decreasing power might help but doesn't address the core issue. Switching "
        "sidebands is impractical because everyone on the band uses the same sideband convention. "
        "Amateur radio is built on cooperation, and this question tests that philosophy."
    )

    E["G2B04"] = (
        "When selecting a CW frequency, maintain 150 Hz to 500 Hz separation from other stations. "
        "CW signals are narrow — a typical CW signal occupies about 100-150 Hz of bandwidth. So "
        "150 Hz minimum separation prevents direct overlap, and up to 500 Hz gives comfortable "
        "breathing room. Compare this to SSB, which needs 2-3 kHz separation (G2B05) because SSB "
        "signals are much wider. The 5-50 Hz range would cause constant interference. The 1-3 kHz "
        "and 3-6 kHz ranges are overkill for CW and would waste valuable spectrum space."
    )

    E["G2B05"] = (
        "When selecting an SSB transmitting frequency, maintain 2 kHz to 3 kHz separation from "
        "other stations. An SSB signal occupies about 2.4 kHz of bandwidth (G8A07), so 2-3 kHz "
        "separation prevents the signals from overlapping. Compare this to CW's 150-500 Hz "
        "(G2B04) — SSB needs roughly 10× more spacing because the signals are roughly 10× wider. "
        "5-50 Hz is way too close, 150-500 Hz is CW spacing, and 6 kHz is unnecessarily wide "
        "(you'd be wasting half the band)."
    )

    E["G2B06"] = (
        "Before calling CQ on an apparently clear frequency, ask 'QRL?' on CW or 'Is this "
        "frequency in use?' on phone, followed by your call sign. This is essential operating "
        "courtesy — a frequency may sound clear because the station you can't hear is between "
        "transmissions, or because propagation only carries their signal one way. By asking first, "
        "you give any stations already using the frequency a chance to respond before you start "
        "transmitting on top of them. Just listening for 2 minutes isn't enough (you might miss a "
        "pause). Sending 'V' or 'test' is not standard practice. And 'QSY' means 'change "
        "frequency' — that's what you tell someone ELSE to do, not what you send when checking."
    )

    E["G2B07"] = (
        "Following the voluntary band plan is good amateur practice when choosing a frequency to "
        "initiate a call. Band plans designate which modes and activities go where — CW at the "
        "bottom, digital modes in the middle, phone at the top (roughly). They're voluntary (not "
        "enforceable by law, with a few exceptions), but following them keeps the bands organized "
        "and reduces interference. Listening for 2 minutes isn't the accepted practice (you ask "
        "if the frequency is in use — G2B06). Identifying 3 times isn't required. And 'all these "
        "choices' is wrong because the other options aren't correct. The band plan is the answer."
    )

    E["G2B08"] = (
        "The voluntary band plan restriction for 50.1-50.125 MHz is contacts with stations NOT "
        "within the 48 contiguous states only. This segment of the 6-meter band is reserved by "
        "band plan for DX — intercontinental contacts, contacts with Hawaii, Alaska, Caribbean "
        "stations, etc. It's the 6-meter equivalent of 'CQ DX' territory. During band openings, "
        "this narrow segment can be packed with DX signals, and local contacts would cause harmful "
        "interference. Below 50.1 MHz is CW/beacon territory; above 50.125 MHz is available for "
        "all contacts including domestic. This is voluntary but widely respected."
    )

    E["G2B09"] = (
        "Only a person holding an FCC-issued amateur operator license may be the control operator "
        "of a station transmitting in RACES. RACES (Radio Amateur Civil Emergency Service) "
        "operates under Part 97.407 with strict rules — the control operator must hold a real "
        "amateur license. It's not enough to be a 'RACES net control operator' without a license, "
        "and government officials without amateur licenses can't be control operators. RACES is "
        "specifically for amateurs who are registered with their local civil defense organization "
        "to provide emergency communications."
    )

    E["G2B10"] = (
        "Good practice for net management includes having a backup frequency in case of "
        "interference or poor conditions. When your primary frequency gets clobbered by QRM, "
        "atmospheric noise, or propagation changes, a pre-arranged backup frequency lets the net "
        "move quickly without losing participants. Multiple sets of phonetics during check-in is "
        "annoying and wastes time — one set is enough. Transmitting the full roster at the start "
        "is impractical for large nets and also wastes airtime. The backup frequency is the "
        "genuinely useful practice that keeps a net running smoothly."
    )

    E["G2B11"] = (
        "RACES training drills and tests may be conducted routinely for no more than 1 hour per "
        "week without special authorization. This is straight from Part 97.407(d)(4). RACES "
        "stations are only authorized to transmit during actual emergencies and during authorized "
        "drills — they can't just chat whenever they want. The 1-hour-per-week limit keeps "
        "training regular while minimizing non-emergency use of RACES frequencies. More frequent "
        "or longer drills require special authorization from the responsible civil defense "
        "organization. Memorize: 1 hour, per week."
    )

    # ── G2C — CW Operating Procedures, Prosigns, Q Signals ───────────

    E["G2C01"] = (
        "Full break-in CW (QSK) means the transmitting station can receive between code characters "
        "and even between individual elements (dits and dahs). The transmitter switches from "
        "transmit to receive so rapidly that you can hear other stations in the gaps between your "
        "own code elements. This lets you know immediately if someone is trying to break in, if "
        "conditions change, or if you need to stop. It's like having a full-duplex conversation. "
        "Without QSK (semi break-in), you can only hear during longer pauses between words or "
        "sentences. QSK requires fast T/R switching hardware — it's not about sending 'BK,' using "
        "automatic keyers, or manual switching."
    )

    E["G2C02"] = (
        "If a CW station sends 'QRS,' you should send slower. QRS literally means 'Send more "
        "slowly' — it's a request from the other operator who's having trouble copying at your "
        "speed. It's one of the most practical Q signals for CW operation. Don't change frequency "
        "(QSY is for that), don't increase power (QRO is for that), and don't repeat everything "
        "twice (that's just annoying if they can't copy your speed). Slow down to match their "
        "ability. Good CW practice means being considerate of the other operator's skill level."
    )

    E["G2C03"] = (
        "KN at the end of a CW transmission means 'listening only for a specific station or "
        "stations.' The K alone means 'go ahead, anyone can respond.' Adding the N makes it "
        "exclusive — 'only the station I'm in contact with should respond.' It's the CW "
        "equivalent of a private conversation. If you hear a station end with KN and you're not "
        "the station they're talking to, don't call them. Other prosigns: SK means 'end of "
        "contact,' BK means 'break' (back to you quickly), AR means 'end of message' (G2C08)."
    )

    E["G2C04"] = (
        "QRL? means 'Are you busy?' or 'Is this frequency in use?' This is the CW equivalent of "
        "asking if a frequency is clear before calling CQ (G2B06). You send QRL? and listen — if "
        "someone responds with 'C' (yes), 'QRL,' or 'YES,' the frequency is occupied and you "
        "should move. If silence, it's probably clear. QRL is one of the most commonly used Q "
        "signals in everyday CW operating. Don't confuse it with QSK (full break-in, G2C01), "
        "QRN (static, G2C10), or QSL (received and understood, G2C09)."
    )

    E["G2C05"] = (
        "When answering a CQ in Morse code, send at the fastest speed you can comfortably copy, "
        "but no faster than the CQ. If someone calls CQ at 15 WPM, don't answer at 25 WPM — "
        "they probably can't copy that fast, which is why they're calling at 15. Match or go "
        "slower than their speed, never faster. If you can copy 20 WPM but they called at 12, "
        "answer at 12. There's no 'standard calling speed' of 5 or 10 WPM — you match the other "
        "station. This is basic CW courtesy and ensures both stations can actually communicate."
    )

    E["G2C06"] = (
        "'Zero beat' means matching your transmit frequency to the frequency of a received signal. "
        "The term comes from the audio beat note you hear when two frequencies are close but not "
        "identical — as you tune closer, the beat note drops in pitch until it reaches zero Hz "
        "(silence) when the frequencies match exactly. In CW, zero-beating ensures you're "
        "transmitting on the same frequency as the station you're trying to work, so they hear "
        "you in their receiver passband. It's NOT about matching speed, operating split, or "
        "sending without errors. Zero beat = same frequency."
    )

    E["G2C07"] = (
        "A 'C' added to a CW RST report indicates a chirpy or unstable signal. The standard RST "
        "report has three numbers: Readability (1-5), Signal Strength (1-9), and Tone (1-9). The "
        "'C' suffix is an additional qualifier meaning the signal's frequency is drifting or "
        "chirping — the tone shifts noticeably, usually due to an unstable oscillator or power "
        "supply issue. Getting a report of '579C' means 'I can read you fine and you're strong, "
        "but your signal sounds chirpy — check your rig.' It does NOT mean 100% copy or S-meter "
        "reading. 'K' suffix would indicate key clicks (if used)."
    )

    E["G2C08"] = (
        "AR is the prosign sent to indicate the end of a formal message in CW. AR means 'end of "
        "message' — it tells the receiving station that the formal message (like a radiogram or "
        "NTS traffic) is complete. Don't confuse it with: SK (end of contact — signing off), "
        "BK (break — quick back-and-forth), or KN (go ahead, specific station only — G2C03). "
        "AR is specifically for formal traffic handling. In casual CW contacts, you might use K, "
        "KN, BK, or SK, but AR is the formal 'message complete' prosign."
    )

    E["G2C09"] = (
        "QSL means 'I have received and understood.' It's an acknowledgment — 'I copy, message "
        "received.' In everyday ham radio, 'QSL' is most famously associated with QSL cards "
        "(confirmation cards exchanged after contacts), but the Q signal itself simply means "
        "'received and understood.' It does NOT mean 'send slower' (that's QRS — G2C02), doesn't "
        "mean 'we've confirmed the contact' (though QSL cards serve that purpose), and doesn't "
        "mean 'we've worked before.' It's a simple acknowledgment."
    )

    E["G2C10"] = (
        "QRN means 'I am troubled by static.' Static — atmospheric noise from thunderstorms, "
        "power line noise, or other natural/man-made interference. When a CW operator sends QRN, "
        "they're telling you the band is noisy at their end and they're having trouble copying. "
        "This is especially common on the lower bands during summer (G3B12). Don't confuse QRN "
        "(static/noise) with QRM (man-made interference from other stations) or QRS (send more "
        "slowly — G2C02). QRN is about atmospheric noise specifically."
    )

    E["G2C11"] = (
        "QRV means 'I am ready to receive.' It's a simple status signal — 'I'm here, I'm "
        "listening, go ahead and send.' You might hear QRV at the beginning of a contact or "
        "during traffic handling when one station is ready for the next message. It doesn't mean "
        "'you're sending too fast' (QRS handles speed requests), doesn't indicate interference "
        "(QRM or QRN), and doesn't mean signing off for the day. QRV = ready."
    )

    # ── G2D — Volunteer Monitors, DX Operating, Logging, Contests ────

    E["G2D01"] = (
        "The Volunteer Monitor Program consists of amateur volunteers who are formally enlisted "
        "to monitor the airwaves for rules violations. Think of them as the amateur radio "
        "neighborhood watch — they listen for out-of-band operation, excessive bandwidth, "
        "unlicensed operators, and other Part 97 violations, then report their findings to the "
        "FCC. The VM Program replaced the older Official Observer (OO) program in 2019. VMs are "
        "NOT Volunteer Examiners (that's the VE program for licensing — G1D), NOT frequency "
        "coordinators (that's for repeaters), and NOT ARES/RACES emergency volunteers."
    )

    E["G2D02"] = (
        "The objectives of the Volunteer Monitor Program are to encourage amateur radio operators "
        "to self-regulate and comply with the rules. The program is about self-policing — the "
        "amateur community monitoring itself rather than relying solely on the FCC's limited "
        "enforcement resources. VMs can issue advisory notices for minor violations and refer "
        "serious cases to the FCC. The VM program is NOT about licensing exams (that's VEs), "
        "NOT about emergency communications (that's ARES/RACES), and NOT about repeater "
        "coordination. It's specifically about rules compliance and self-regulation."
    )

    E["G2D03"] = (
        "Volunteer Monitors can localize a station holding a repeater open by comparing beam "
        "headings from their home locations with those of other Volunteer Monitors. This is "
        "basic radio direction finding (triangulation) — if one VM determines the signal is "
        "coming from the northeast and another VM 20 miles away determines it's coming from "
        "the northwest, the source is where those two bearings intersect on a map. This "
        "requires directional antennas (beams) at multiple locations. It's NOT about comparing "
        "vertical vs. horizontal signal strengths, and NOT about comparing repeater input vs. "
        "output. Triangulation from multiple bearings is the standard technique."
    )

    E["G2D04"] = (
        "An azimuthal projection map shows true bearings and distances from a specific location. "
        "It's centered on YOUR location, and every point on the map shows the correct compass "
        "bearing (azimuth) and great-circle distance from the center. This is invaluable for "
        "pointing directional antennas — look up the DX station's location on your azimuthal "
        "map and you instantly know which direction to point your beam. Regular Mercator maps "
        "distort bearings and distances at high latitudes. An azimuthal map is only accurate "
        "from its center point — a map centered on New York is useless for someone in Tokyo. "
        "It has nothing to do with satellite orbits or equator crossings."
    )

    E["G2D05"] = (
        "To look for an HF contact with any station, you call CQ: repeat 'CQ' a few times, "
        "followed by 'this is,' then your call sign a few times, pause to listen, and repeat "
        "as necessary. CQ is the universal 'calling any station' signal. The format is: "
        "'CQ CQ CQ, this is [callsign] [callsign] [callsign], standing by.' A few CQs (not "
        "too many — nobody wants to listen to 30 seconds of CQ), your call sign clearly, then "
        "LISTEN. Too many people call CQ endlessly without pausing to hear replies. The other "
        "choices describe incorrect or non-standard procedures — transmitting an unmodulated "
        "carrier is never appropriate."
    )

    E["G2D06"] = (
        "For a long-path contact, point your directional antenna 180 degrees from the short-path "
        "heading. The short path is the direct great-circle route to the other station. The long "
        "path goes the other way around the globe — exactly opposite direction. If the short path "
        "to Japan from the US east coast is northwest (~330°), the long path is southeast (~150°). "
        "Long-path propagation can sometimes provide better signals than short path, especially "
        "when the short path crosses the polar regions during geomagnetic storms (G3A08) or when "
        "the long path follows the gray line. It's 180° opposite — not toward the rising sun, "
        "not along the gray line specifically, and not toward the north."
    )

    E["G2D07"] = (
        "Alpha, Bravo, Charlie, Delta are examples of the NATO Phonetic Alphabet. The NATO "
        "alphabet is the international standard used in amateur radio for spelling out call signs "
        "clearly: Alpha, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliet, Kilo, "
        "Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, "
        "Whiskey, X-ray, Yankee, Zulu. 'Able, Baker, Charlie, Dog' is the old US military phonetic "
        "alphabet (pre-NATO). 'Adam, Boy, Charles, David' and 'America, Boston, Canada, Denmark' "
        "are informal alternatives sometimes heard but are NOT the NATO standard."
    )

    E["G2D08"] = (
        "Many amateurs keep a station log to help with a reply if the FCC requests information "
        "about their station. While the FCC no longer requires a mandatory station log, keeping "
        "one is still excellent practice. If the FCC investigates an interference complaint or "
        "questions your operating activities, a detailed log provides evidence of what you were "
        "doing, when, and on what frequency. Logs are also valuable for award tracking, contest "
        "submissions, and personal records. The FCC does NOT require logs of international "
        "contacts (choice A) or third-party traffic (choice B) — those mandatory logging "
        "requirements were eliminated years ago. And logs are NOT needed for license renewal."
    )

    E["G2D09"] = (
        "When participating in a contest on HF, the only thing REQUIRED is to identify your "
        "station according to normal FCC regulations — every 10 minutes during a contact and at "
        "the end. Contest operation doesn't create any special requirements beyond normal Part 97 "
        "rules. Submitting a log to the contest sponsor is voluntary (you're encouraged to, but "
        "it's not an FCC requirement). Sending QSL cards is optional courtesy. The FCC doesn't "
        "care about your contest score — they care that you identify properly, stay in band, "
        "and follow the rules. Normal identification rules apply in contests just like any other "
        "operating activity."
    )

    E["G2D10"] = (
        "QRP means low-power transmit operation. The generally accepted definition is 5 watts or "
        "less on CW and 10 watts or less on SSB (PEP). QRP operators intentionally limit their "
        "power to challenge themselves — making contacts with minimal power tests your skills, "
        "antenna, and propagation knowledge. It's a popular operating style with its own contests, "
        "clubs (QRP ARCI, for example), and award programs. QRP is NOT remote piloted model "
        "control, NOT 'Quick Response Protocol' (made-up), and NOT a traffic relay procedure. "
        "The Q signal QRP literally means 'reduce power' — and QRP operators take that to heart."
    )

    E["G2D11"] = (
        "Signal reports are exchanged at the beginning of an HF contact so each station can "
        "operate according to conditions. If you give me a 59 report, I know conditions are "
        "great and we can have a leisurely conversation. If you give me a 33 report, I know to "
        "keep it short, speak slowly and clearly, and maybe repeat key information. The signal "
        "report sets expectations for the entire contact. It's NOT primarily for award programs "
        "(though some awards require signal reports), NOT related to radiogram format, and NOT "
        "for calibrating frequency displays. It's practical information that helps both operators "
        "adjust their operating style to match actual conditions."
    )

    # ── G2E — Digital Operating Procedures and Protocols ─────────────

    E["G2E01"] = (
        "LSB (Lower Sideband) is normally used when sending RTTY via AFSK with an SSB transmitter. "
        "This seems backwards since most digital modes use USB, but RTTY via AFSK on LSB is the "
        "long-established convention. When using Audio Frequency Shift Keying (AFSK), the audio "
        "tones fed into the SSB transmitter's mic input shift the RF output — and the mark/space "
        "relationship comes out correctly on LSB. If you used USB, the mark and space frequencies "
        "would be reversed (which can actually be compensated for in software, but LSB is the "
        "standard). Note: when using direct FSK (keying the transmitter directly), the sideband "
        "setting doesn't matter the same way. AFSK + RTTY = LSB."
    )

    E["G2E02"] = (
        "VARA is a digital protocol used with Winlink. VARA (developed by EA5HVK) provides "
        "high-speed data transfer for Winlink email operations on both HF and VHF/UHF. It "
        "automatically adjusts its speed based on channel conditions — starting slow and ramping "
        "up as conditions allow, or slowing down when conditions degrade. VARA has largely "
        "replaced older protocols like WINMOR and PACTOR for Winlink gateway connections because "
        "it offers good performance with just a sound card interface (no expensive PACTOR modem "
        "required). It's NOT a moon-bounce mode, NOT a direction-finding system, and NOT a DX "
        "spotting network."
    )

    E["G2E03"] = (
        "ALL of the listed symptoms can result from interference with a PACTOR or VARA "
        "transmission: frequent retries or timeouts, long pauses, and failure to establish a "
        "connection. These are ARQ (Automatic Repeat reQuest) protocols — they request "
        "retransmission when packets are corrupted (G8C05). Interference corrupts packets, "
        "triggering retries. If retries keep failing, the protocol pauses and eventually times "
        "out. If the interference is bad enough from the start, the initial handshake fails and "
        "no connection is established at all. This is why choosing a clear frequency is especially "
        "important for digital modes — interference doesn't just degrade quality like it does with "
        "voice, it can completely prevent communication."
    )

    E["G2E04"] = (
        "When answering a CQ on FT8, good practice is to find a clear frequency during the "
        "alternate time slot to the calling station. FT8 operates in strict 15-second time slots — "
        "even slots (0, 15, 30, 45 seconds) and odd slots. If the calling station transmitted in "
        "an even slot, you respond in the next odd slot, and vice versa. You should also choose a "
        "different audio frequency (a clear spot on the waterfall) rather than calling on the "
        "station's own frequency. Calling on their exact frequency would collide with their "
        "transmissions. The WSJT-X software handles much of this automatically, but understanding "
        "the principle matters for the exam."
    )

    E["G2E05"] = (
        "USB (Upper Sideband) is the standard for JT65, JT9, FT4, and FT8 when using AFSK. This "
        "follows the modern digital mode convention — virtually all newer digital modes use USB. "
        "RTTY via AFSK is the notable exception that uses LSB (G2E01), but that's a legacy "
        "convention. The WSJT-X suite (which runs FT8, FT4, JT65, JT9) is designed for USB "
        "operation. Using the wrong sideband would invert the audio spectrum and make decoding "
        "impossible. When your software says 'USB,' believe it."
    )

    E["G2E06"] = (
        "The most common RTTY frequency shift on amateur HF is 170 Hz. This is the spacing "
        "between the mark and space tones (G8C11). The 170 Hz shift is an amateur convention — "
        "commercial RTTY often uses 425 Hz or 850 Hz shifts, but amateur RTTY standardized on "
        "170 Hz because it keeps the signal narrow and allows more stations to fit in the band. "
        "Standard amateur RTTY uses 45.45 baud with 170 Hz shift on a 2125/2295 Hz tone pair "
        "(for AFSK). The 85 Hz option is too narrow for standard RTTY, and 425/850 Hz are "
        "commercial standards, not amateur."
    )

    E["G2E07"] = (
        "FT8 requires computer time accurate to within approximately 1 second. FT8's structured "
        "protocol depends on precise 15-second time slots — all stations worldwide must be "
        "synchronized so transmissions start and stop at the same moment. If your computer clock "
        "is off by more than about a second, your transmissions won't align with the time slots "
        "and other stations won't decode you. Use NTP (Network Time Protocol) or GPS to keep your "
        "clock accurate. FT8 does NOT require a special hardware modem (just a sound card), "
        "does NOT need receiver attenuation set to -12 dB, and does NOT require vertical "
        "polarization. Time accuracy is the critical requirement."
    )

    E["G2E08"] = (
        "Most digital mode operations on the 20-meter band are found between 14.070 MHz and "
        "14.100 MHz. This segment sits between the CW portion (below 14.070) and the voice "
        "portion (above 14.150) of the band. Within this range, you'll find FT8 around "
        "14.074 MHz (G2E15), RTTY near 14.080-14.090 MHz, PSK31 around 14.070 MHz, and various "
        "other digital modes. It's NOT near 14.230 MHz (that's SSTV), NOT near 14.325 MHz "
        "(that's the middle of the phone band), and NOT near 14.100 MHz (that's a beacon "
        "frequency — G1E10, stay away). Know where digital modes live on 20 meters."
    )

    E["G2E09"] = (
        "You cannot join an existing PACTOR contact — PACTOR connections are limited to two "
        "stations. PACTOR is a point-to-point ARQ protocol; it establishes a dedicated link "
        "between exactly two stations that exchange data packets with acknowledgments (G8C05-06). "
        "There's no provision for a third station to jump in. This is fundamentally different "
        "from a phone QSO or packet radio net where multiple stations can participate. If you "
        "need to contact one of the stations, you have to wait until their PACTOR session ends. "
        "Sending broadcast packets, transmitting a carrier, or sending NAK won't get you into "
        "an active PACTOR link."
    )

    E["G2E10"] = (
        "To establish contact with a digital messaging system gateway station, transmit a connect "
        "message on the station's published frequency. Gateway stations (like Winlink RMS gateways "
        "— G2E13) publish their operating frequencies in directories. You tune to their frequency "
        "and initiate a connection using the appropriate protocol (VARA, PACTOR, or packet). You "
        "don't email the operator, don't send QRL in Morse code, and gateways don't broadcast "
        "SSIDs like Wi-Fi access points. The connection process is protocol-specific: your Winlink "
        "client software handles the connect sequence once you select the gateway and frequency."
    )

    E["G2E11"] = (
        "AREDN (Amateur Radio Emergency Data Network) mesh networks provide high-speed data "
        "services during emergencies or community events. AREDN uses repurposed commercial Wi-Fi "
        "hardware on amateur microwave bands (900 MHz, 2.4 GHz, 5.8 GHz) to create self-healing "
        "mesh networks (G8C09) that can carry IP-based services — VoIP phones, video feeds, "
        "email, situational awareness maps, and other data-heavy applications. It's NOT for FM "
        "repeater coverage, NOT for propagation monitoring (that's WSPR — G8C02), and NOT for "
        "DX spotting. AREDN fills the gap when internet infrastructure fails during disasters."
    )

    E["G2E12"] = (
        "Winlink is ALL of the described things: an amateur radio wireless network for sending "
        "and receiving email on the internet, a form of packet radio (at its core, it uses "
        "packet-based digital protocols), and capable of operating on both VHF and HF bands. "
        "Winlink connects amateur stations to the internet email system through gateway stations "
        "(G2E13). You can send email from a remote location with no internet access by connecting "
        "via HF radio to a Winlink gateway, which forwards your message to the internet. It "
        "supports multiple connection protocols: VARA, PACTOR, packet, and ARDOP. All three "
        "descriptions are accurate, so the answer is 'All of the above.'"
    )

    E["G2E13"] = (
        "A Winlink Remote Message Server is also called a gateway. The RMS (Remote Message Server) "
        "is the station that bridges between amateur radio and the internet — it receives your "
        "radio-transmitted email and forwards it to the internet, and vice versa. The term "
        "'gateway' makes sense because it's literally the gateway between the radio world and "
        "the internet world. It's NOT a Terminal Node Controller (TNC — that's a hardware device "
        "for packet radio), NOT an RJ-45 (that's an Ethernet connector), and definitely NOT a "
        "printer/server. Gateway = Winlink RMS."
    )

    E["G2E14"] = (
        "ALL of the listed problems could prevent decoding an RTTY or FSK signal: mark and space "
        "frequencies may be reversed (called 'inverted'), you may have selected the wrong baud "
        "rate, or you may be listening on the wrong sideband. Each of these would make the signal "
        "look correct on your waterfall but be undecodable. Reversed mark/space is common when "
        "one station uses USB and another uses LSB for RTTY. Wrong baud rate means the timing "
        "is off (G8C04 — Baudot code uses specific start/stop timing). Wrong sideband inverts "
        "the entire audio spectrum. All three are real troubleshooting steps when RTTY won't "
        "decode."
    )

    E["G2E15"] = (
        "FT8 on the 20-meter band is commonly found at approximately 14.074 MHz to 14.077 MHz. "
        "This is within the digital mode segment of 20 meters (G2E08: 14.070-14.100 MHz) and "
        "is the specific slice where FT8 activity is concentrated. FT8 signals are narrow (~50 Hz "
        "each) but there can be dozens active simultaneously in this 3 kHz window. It's NOT in "
        "the voice portion, NOT in the CW segment, and NOT near 14.110 MHz (which is above the "
        "digital segment). The 14.074 MHz frequency is worth memorizing — it's one of the most "
        "active frequencies in all of amateur radio, with thousands of contacts made there daily."
    )

    # ── G3A — Sunspots, Solar Radiation, Propagation Forecasting ────

    E["G3A01"] = (
        "More sunspots mean more ultraviolet radiation hitting the ionosphere, which increases "
        "ionization — especially in the F2 layer. Higher ionization raises the Maximum Usable "
        "Frequency (MUF), so bands like 15, 12, and 10 meters that are dead during solar minimums "
        "come alive during high sunspot numbers. Think of sunspots as the ionosphere's power supply: "
        "more sunspots → more ionization → higher MUF → higher bands open up. A zero sunspot number "
        "doesn't kill ALL propagation — the lower HF bands still work via F2 reflection — it just "
        "means the higher bands won't have enough ionization to support skip."
    )

    E["G3A02"] = (
        "A Sudden Ionospheric Disturbance (SID) is caused by a burst of X-ray and UV radiation from "
        "a solar flare. This radiation massively increases D-region ionization on the sunlit side of "
        "Earth. The D region is an absorber, not a reflector — and it absorbs lower frequencies more "
        "than higher ones (absorption is roughly proportional to 1/f²). So a SID hammers the lower HF "
        "bands (80m, 40m) while higher frequencies (15m, 10m) may still get through with less "
        "disruption. SIDs only affect the daytime side of Earth because the D region disappears at "
        "night — the radiation that creates it travels at the speed of light (see G3A03)."
    )

    E["G3A03"] = (
        "UV and X-ray radiation from a solar flare travels at the speed of light — roughly 8 minutes "
        "from Sun to Earth (93 million miles ÷ 186,000 miles/second ≈ 500 seconds ≈ 8 minutes). This "
        "is essentially instantaneous compared to charged particles from a coronal mass ejection, "
        "which take 15 hours to several days (G3A11). The 8-minute delay is important: when you see "
        "a solar flare reported, the radiation has already arrived. You can't prepare for it — it's "
        "already affecting the ionosphere by the time astronomers announce it. The 28-day answer is "
        "the Sun's rotation period (G3A10)."
    )

    E["G3A04"] = (
        "15, 12, and 10 meters are the highest HF bands, and they need the most ionospheric support "
        "to work. During low solar activity, the F2 layer's ionization drops and the MUF falls — "
        "often below 21 MHz (15m). The higher bands simply don't have enough ionization to refract "
        "signals back to Earth. The lower bands (160m, 80m, 40m, 30m, 20m) still work because their "
        "frequencies are lower and easier for the weakened ionosphere to refract. This is why 20 "
        "meters is the workhorse band — it works at any point in the solar cycle (G3A07), while 10 "
        "meters goes from spectacular to silent depending on sunspot numbers."
    )

    E["G3A05"] = (
        "The Solar Flux Index (SFI) measures radio emissions from the Sun at a wavelength of 10.7 cm "
        "(a frequency of 2800 MHz). It's measured daily at the Dominion Radio Astrophysical "
        "Observatory in Penticton, British Columbia. SFI correlates well with sunspot activity and "
        "ionospheric ionization — higher SFI means more solar radiation, more ionization, higher MUF. "
        "SFI values range from about 64 (quiet sun, solar minimum) to over 300 (extremely active). "
        "An SFI above 150 generally means excellent HF conditions on the higher bands. Don't confuse "
        "SFI with the sunspot number (SSN) — they correlate but are different measurements. SFI is a "
        "direct measurement of solar radiation, not a count of visible spots."
    )

    E["G3A06"] = (
        "A geomagnetic storm is a temporary disturbance in Earth's magnetic field, typically caused "
        "by a coronal mass ejection (CME) or high-speed solar wind stream interacting with Earth's "
        "magnetosphere. It is NOT a thunderstorm, NOT a drop in solar flux, and NOT just 'ripples' — "
        "it's a significant disruption. Geomagnetic storms are measured by the K-index (short-term, "
        "G3A12) and A-index (long-term, G3A13). They degrade HF propagation, especially at high "
        "latitudes (G3A08), but can create auroras that benefit VHF operators (G3A09). Think of it "
        "as the Sun punching Earth's magnetic shield — the shield wobbles, and that wobble disrupts "
        "the ionosphere."
    )

    E["G3A07"] = (
        "The 20-meter band (14 MHz) is the workhorse of HF — it supports worldwide propagation at "
        "ANY point in the solar cycle. Even during solar minimum, the F2 layer maintains enough "
        "ionization to refract 14 MHz signals around the globe during daylight hours. At solar "
        "maximum, 20m is open longer and to more paths. At solar minimum, openings are shorter but "
        "still happen daily. This is why 20m is the most popular DX band — you can count on it "
        "regardless of where we are in the 11-year cycle. Compare this to 10m and 15m, which go "
        "essentially dead during solar minimum (G3A04)."
    )

    E["G3A08"] = (
        "Geomagnetic storms degrade HF propagation at high latitudes. The mechanism: charged "
        "particles from CMEs are funneled by Earth's magnetic field toward the magnetic poles, "
        "where they crash into the ionosphere and increase D-region absorption. This creates a "
        "'polar cap absorption' event that can wipe out HF signals on paths crossing the polar "
        "regions — which includes many paths between North America and Europe/Asia. A geomagnetic "
        "storm does NOT improve high-latitude propagation and does NOT affect ground wave propagation "
        "(ground wave follows Earth's surface and doesn't care about the ionosphere). The polar path "
        "degradation is why operators switch to long-path propagation during geomagnetic storms."
    )

    E["G3A09"] = (
        "Here's the silver lining of geomagnetic storms: auroras. The same charged particles that "
        "wreck HF propagation at high latitudes create visible auroras — and those auroras can "
        "reflect VHF signals. Aurora scatter on 6 meters and 2 meters is a real propagation mode, "
        "though signals are distorted (buzzy, fluttery) because the aurora curtain is constantly "
        "moving. CW works best for aurora contacts since voice becomes hard to copy through the "
        "distortion. So while HF operators curse geomagnetic storms, VHF operators in northern "
        "latitudes get excited — it's a rare chance to work stations hundreds of miles away on "
        "bands that normally only reach the horizon."
    )

    E["G3A10"] = (
        "The Sun rotates on its axis approximately once every 26-28 days (it's not a solid body, "
        "so different latitudes rotate at different speeds). Active regions — sunspot groups that "
        "produce solar radiation — rotate with the Sun. If a particular active region boosts "
        "propagation this week, it'll rotate away (conditions decline), then come back around "
        "26-28 days later (conditions improve again). This creates a predictable monthly cycle "
        "in propagation conditions. Experienced operators track active regions and can predict "
        "when good conditions will return — literally waiting for the Sun to rotate the active "
        "region back to face Earth. This is NOT caused by Earth's radiation belts, the Moon, "
        "or atmospheric oscillations."
    )

    E["G3A11"] = (
        "A coronal mass ejection (CME) sends billions of tons of charged particles toward Earth "
        "at speeds of 300-2000 km/s. Unlike the UV/X-ray radiation from a flare (which arrives "
        "in 8 minutes at the speed of light, G3A03), these slower-moving particles take 15 hours "
        "to several days to reach Earth. When they arrive, they trigger geomagnetic storms (G3A06). "
        "The time delay is actually useful — space weather forecasters can observe a CME leaving "
        "the Sun and give advance warning before the particles arrive. The 28-day option is the "
        "Sun's rotation period (G3A10), and 14 days is half of that — neither relates to CME "
        "transit time."
    )

    E["G3A12"] = (
        "The K-index measures the short-term stability of Earth's geomagnetic field, updated every "
        "3 hours. It uses a 0-9 scale: K0-K1 means quiet (good HF propagation), K2-K3 is unsettled, "
        "K4 is active, and K5-K9 indicates a geomagnetic storm (bad for HF, especially polar paths). "
        "Think of K as the 'right now' geomagnetic indicator. Compare it to the A-index (G3A13), "
        "which is a daily average derived from K values. When checking propagation forecasts, the "
        "K-index tells you current conditions. A sudden jump in K-index means a geomagnetic "
        "disturbance just hit — conditions are degrading NOW. Don't confuse it with sunspot "
        "position (visual observation) or solar flux (radio emission measurement)."
    )

    E["G3A13"] = (
        "The A-index measures the long-term stability of Earth's geomagnetic field — it's a daily "
        "average derived from the eight 3-hour K-index values. While K gives you a snapshot (updated "
        "every 3 hours), A gives you the bigger picture (daily). A-index values: A0-A7 = quiet "
        "(excellent HF), A8-A15 = unsettled, A16-A29 = active, A30+ = storm. Lower A-index = better "
        "HF propagation. Higher A-index = more disturbed. Together, K and A tell you what the "
        "geomagnetic field is doing: K for right now, A for the overall day. Both are measured at "
        "Earth (not the Sun) — they tell you how OUR magnetic field is responding to solar activity."
    )

    E["G3A14"] = (
        "Charged particles streaming from coronal holes (persistent openings in the Sun's corona) "
        "create high-speed solar wind that disturbs Earth's geomagnetic field and degrades HF "
        "communication. Coronal holes are different from flares and CMEs — they're long-lasting "
        "features that can persist for months, rotating with the Sun (tying into the 27-day cycle "
        "from G3A10). The high-speed wind particles increase D-region absorption and disrupt the "
        "F-region, degrading HF skywave propagation. They do NOT improve HF or affect VHF/UHF "
        "ducting (ducting is a tropospheric phenomenon caused by temperature inversions, completely "
        "unrelated to solar particles and the ionosphere)."
    )

    # ── G3B — MUF, LUF, Propagation Paths, Skip ────────────────────

    E["G3B01"] = (
        "When a signal reaches you via BOTH the short path (direct great-circle route) AND the long "
        "path (the other way around the globe — roughly 25,000 miles longer), you hear a slightly "
        "delayed echo. The long-path signal arrives a fraction of a second later because it traveled "
        "a much greater distance. At the speed of light, the extra ~25,000 miles adds about 0.13 "
        "seconds of delay — enough to hear as a distinct echo. This doesn't cause 3 dB gain (the "
        "two signals are rarely in phase) and doesn't cause severe cancellation (the delay is too "
        "long for destructive interference at HF). The echo effect is a recognizable signature of "
        "simultaneous short-path and long-path propagation."
    )

    E["G3B02"] = (
        "ALL of the listed factors affect the MUF: path distance and location, time of day and "
        "season, and solar radiation and ionospheric disturbances. The MUF is the highest frequency "
        "that will be refracted back to Earth for a specific path at a specific time — it's not a "
        "single global number. It varies by path (a signal to Europe has a different MUF than one "
        "to Japan), by time (MUF rises during the day as solar UV ionizes the F2 layer, drops at "
        "night), by season (winter MUF can actually be higher than summer at mid-latitudes), and "
        "by solar activity (more sunspots → more ionization → higher MUF, as in G3A01). The MUF "
        "is dynamic — it changes constantly."
    )

    E["G3B03"] = (
        "The frequency just below the MUF has the least attenuation for long-distance skip. Here's "
        "why: as frequency increases toward the MUF, the signal penetrates deeper into the "
        "ionosphere before being refracted back — spending less time in the absorptive D region. "
        "Higher frequency = less D-region absorption = stronger received signal. But go ABOVE the "
        "MUF and the signal punches through the ionosphere entirely — no propagation at all. So "
        "the sweet spot is just below the MUF: maximum frequency that still refracts, with minimum "
        "absorption along the way. Operating just above the LUF works, but signals there suffer "
        "heavy D-region absorption. The critical frequency relates to vertical incidence, not "
        "long-distance skip. The practical lesson: tune as high as the band supports."
    )

    E["G3B04"] = (
        "Networks like WSPRnet, PSKReporter, and the Reverse Beacon Network (RBN) are automated "
        "receiving stations that monitor bands 24/7 and report what they hear. Transmit a WSPR "
        "beacon or make a CQ call, and within seconds you can see on a map exactly which stations "
        "heard you — giving you real-time, path-specific propagation data from YOUR station with "
        "YOUR antenna. This is far more useful than checking the A-index (which tells you about "
        "geomagnetic conditions globally, not your specific path) or sending dots and listening for "
        "echoes (which is unreliable and may cause interference). The automated network approach "
        "gives actual, empirical propagation data — not predictions."
    )

    E["G3B05"] = (
        "Frequencies between the LUF and MUF are in the 'sweet spot' for skywave propagation — "
        "they are refracted (bent) back to Earth by the ionosphere. Below the LUF, signals are "
        "absorbed. Above the MUF, they pass through. Between the two, the ionosphere has enough "
        "electron density to refract the signal back down without absorbing too much energy. "
        "Important: the ionosphere REFRACTS radio waves — it bends them gradually through a region "
        "of varying electron density. It does NOT reflect them like a mirror (though we often say "
        "'reflect' casually). And it definitely doesn't amplify them or trap them in orbit around "
        "Earth. The signal goes up, bends in the ionosphere, and comes back down."
    )

    E["G3B06"] = (
        "Signals below the LUF (Lowest Usable Frequency) are absorbed by the D region before they "
        "can reach the reflecting F layer. They don't make it to the destination — they're "
        "attenuated to uselessness along the way. The D region is the villain here: it sits at the "
        "lowest part of the ionosphere (60-90 km altitude), and it absorbs lower frequencies much "
        "more aggressively than higher ones (absorption ∝ 1/f²). Signals below the LUF lose so "
        "much energy passing through the D region that they arrive too weak to use — even if the "
        "F layer above would have refracted them perfectly. This is why the LUF rises during the "
        "day (when D-region ionization peaks) and drops at night (when the D region disappears)."
    )

    E["G3B07"] = (
        "LUF = Lowest Usable Frequency — the lowest frequency you can use for skywave communication "
        "between two SPECIFIC points. Below the LUF, signals are absorbed by the D region (G3B06). "
        "Notice it's path-specific: the LUF for a path from New York to London differs from New York "
        "to Tokyo. It's also not fixed to any time period — it changes constantly with ionospheric "
        "conditions. The LUF depends on D-region absorption (which varies with time of day, solar "
        "activity, and path length) and on the minimum signal strength needed for communication "
        "(a 1000W station has a lower effective LUF than a 5W station because it can overcome more "
        "absorption). The LUF and MUF together define your usable frequency window."
    )

    E["G3B08"] = (
        "MUF = Maximum Usable Frequency — the highest frequency that will be refracted back to "
        "Earth between two specific points. Above the MUF, signals pass through the ionosphere "
        "into space (G3B05). Like the LUF, the MUF is path-specific and constantly changing. It's "
        "NOT the minimum usable frequency (that's the LUF, G3B07), and it's NOT defined for a "
        "24-hour period (it changes hour to hour). The MUF depends on F-region ionization — more "
        "ionization means higher MUF. This is why sunspot numbers matter (G3A01): more sunspots → "
        "more UV → more F-region ionization → higher MUF → higher bands open. Your usable frequency "
        "window for any path is: LUF (bottom) to MUF (top). Best performance is just below the "
        "MUF (G3B03)."
    )

    E["G3B09"] = (
        "One F2-region hop covers approximately 2,500 miles maximum. The F2 layer sits at about "
        "250-400 km altitude — the highest ionospheric layer. A signal launched at a low angle hits "
        "the F2 layer and comes back down roughly 2,500 miles away. For longer paths, the signal "
        "bounces off the ground and goes back up for another hop (multi-hop propagation). To cross "
        "the Atlantic (~3,500 miles) typically takes two hops. Compare this to the E region at about "
        "100 km altitude — much lower, so the maximum single-hop distance is only about 1,200 miles "
        "(G3B10). The F2 region's greater height is exactly why it supports longer skip distances "
        "(G3C03)."
    )

    E["G3B10"] = (
        "One E-region hop covers approximately 1,200 miles maximum. The E region sits at about "
        "100-115 km altitude — roughly half the height of the F2 layer. Lower reflection point means "
        "shorter hop distance. Think of it geometrically: the higher the mirror, the farther apart "
        "the endpoints can be. F2 at ~300 km → 2,500 miles (G3B09). E at ~100 km → 1,200 miles. "
        "Normal E-region propagation is less common for routine long-distance work because the E "
        "region's ionization is weaker and less predictable than F2. However, sporadic E (Es) — "
        "patches of intense ionization that appear unpredictably in the E region — can produce "
        "strong, single-hop signals out to about 1,200 miles on bands as high as 6 meters."
    )

    E["G3B11"] = (
        "When the LUF exceeds the MUF, there's no usable frequency for skywave propagation on that "
        "path — your frequency window has collapsed. Normally, LUF is the floor and MUF is the "
        "ceiling, and you operate between them. But if D-region absorption increases enough (raising "
        "the LUF) or F-region ionization drops enough (lowering the MUF), the floor rises above "
        "the ceiling and there's nothing in between. This can happen during strong solar disturbances "
        "(D-region absorption spikes) or at night on paths where the MUF drops very low. The only "
        "options are ground wave (short range), NVIS (G3C10), or wait for conditions to change. "
        "This condition does NOT enhance anything — it's a propagation blackout."
    )

    E["G3B12"] = (
        "Summer on the lower HF bands (80m, 40m) means high atmospheric noise — primarily from "
        "thunderstorms. Summer produces massive convective thunderstorm activity, and lightning "
        "generates broadband RF noise that propagates for thousands of miles via skywave. This noise "
        "is worst on the lower frequencies (it decreases with increasing frequency). A signal that "
        "would copy perfectly on 40m in winter may be buried under a wall of static crashes in "
        "summer. This is why the lower bands are traditionally 'winter bands' — not because "
        "propagation is better in winter (it's actually similar), but because the noise floor drops "
        "dramatically when thunderstorm activity decreases. The noise is atmospheric, not ionospheric."
    )

    # ── G3C — Ionospheric Layers, Critical Angle/Frequency, Scatter ─

    E["G3C01"] = (
        "The D region is closest to Earth's surface, at roughly 60-90 km altitude. The layers stack "
        "up in alphabetical order: D (lowest), E (~100-115 km), F1 (~150-200 km), F2 (highest, "
        "~250-400 km). The D region is the troublemaker for HF — it ABSORBS signals rather than "
        "refracting them, especially at lower frequencies. It exists only during daylight (created "
        "by solar UV/X-ray radiation) and disappears at night, which is why the lower HF bands "
        "(80m, 160m) work better for DX at night — the absorptive D region is gone, letting signals "
        "pass through to the F2 layer for refraction."
    )

    E["G3C02"] = (
        "The critical frequency is the HIGHEST frequency that will be refracted back to Earth at a "
        "given incidence angle. Think of it as the MUF for a specific angle of incidence. At "
        "vertical incidence (straight up), the critical frequency is the highest frequency that "
        "comes straight back down — this is the MUF for zero distance. At lower (more oblique) "
        "angles, higher frequencies can be refracted because the signal spends more time in the "
        "ionized region and gets bent more. This is why the MUF for long-distance paths is higher "
        "than the critical frequency measured by an ionosonde shooting straight up. Don't confuse "
        "critical frequency (about maximum frequency returned) with critical angle (about maximum "
        "angle returned, G3C04)."
    )

    E["G3C03"] = (
        "The F2 region produces the longest skip distance because it's the HIGHEST ionospheric "
        "layer — roughly 250-400 km above Earth. Simple geometry: the higher the refraction point, "
        "the farther apart the transmitter and receiver can be while still making contact. Imagine "
        "bouncing a ball off a high ceiling versus a low ceiling — you can throw the ball much "
        "farther with a high ceiling. F2 at ~300 km gives about 2,500 miles per hop (G3B09), while "
        "E at ~100 km gives only about 1,200 miles (G3B10). The F2 region is NOT the densest layer "
        "(density doesn't determine skip distance — height does). Doppler effect and temperature "
        "inversions are unrelated to ionospheric skip distance."
    )

    E["G3C04"] = (
        "The critical angle is the HIGHEST takeoff angle that will still return a radio wave to "
        "Earth under current ionospheric conditions. Signals launched at angles above the critical "
        "angle pass through the ionosphere into space — they're not bent enough to come back down. "
        "Signals at or below the critical angle hit the ionosphere at a more oblique angle, spend "
        "more time being refracted, and bend back to Earth. Lower takeoff angles = longer skip "
        "distance. The critical angle defines the boundary: above it, no return; below it, "
        "successful refraction. This creates the skip zone — the area between the end of ground "
        "wave coverage and where the first skywave signal returns to Earth. Don't confuse critical "
        "angle (highest angle for return) with critical frequency (highest frequency for return)."
    )

    E["G3C05"] = (
        "The D region absorbs lower HF frequencies during daylight hours — and 40m, 60m, 80m, and "
        "160m are all 'lower HF' frequencies that get hit hard. The D region is created by solar "
        "radiation and exists only during the day. It absorbs rather than refracts, and absorption "
        "is worse at lower frequencies (proportional to 1/f²). These bands pass through the D "
        "region on their way up to the F2 layer for refraction, but they lose so much energy in "
        "transit that long-distance signals arrive too weak to use. At night, the D region vanishes, "
        "these frequencies sail through to the F2 layer unmolested, and suddenly 80m and 40m come "
        "alive for DX. This is THE key insight of HF propagation: the D region is the daytime "
        "gatekeeper, and lower frequencies are its primary victims."
    )

    E["G3C06"] = (
        "HF scatter signals have a characteristic fluttering sound. This flutter comes from the "
        "signal being scattered off irregular ionospheric structures — the signal takes multiple "
        "slightly different paths that constantly shift, causing rapid fading and phase variations "
        "that your receiver hears as flutter. Unlike normal skywave (which can be a clean, stable "
        "signal), scatter is inherently messy because the scattering mechanism is chaotic. Phone "
        "signals via scatter have LOW intelligibility (not high), and scatter can occur during the "
        "day (not only at night). The large signal swings described in choice C are more "
        "characteristic of normal skip fading, not scatter's rapid flutter."
    )

    E["G3C07"] = (
        "HF scatter signals sound distorted because energy is scattered into the skip zone through "
        "several different paths simultaneously. Each path has a slightly different length and "
        "delay, so multiple copies of the signal arrive at your receiver slightly out of time "
        "with each other. These overlapping, time-shifted copies interfere with one another, "
        "creating the distortion and flutter characteristic of scatter signals. It's multipath "
        "distortion — the same phenomenon that causes ghosting on old analog TV sets, but worse "
        "because the scatter mechanism creates many more paths. The ionosphere isn't 'unstable' "
        "in the sense of choice A, ground waves don't cause scatter, and the E region's presence "
        "or absence isn't the issue."
    )

    E["G3C08"] = (
        "HF scatter signals in the skip zone are weak because only a small fraction of the "
        "transmitted energy gets scattered into that zone. In normal skywave propagation, the "
        "ionosphere refracts most of the signal energy in a coherent beam back to Earth. Scatter "
        "is different — it's energy being diffused in many directions by irregularities in the "
        "ionosphere, and only a tiny portion of that scattered energy happens to land in the "
        "skip zone. Think of it like a spotlight (normal skywave) versus a disco ball (scatter) — "
        "the disco ball sends light everywhere, but very little hits any one spot. Scatter is NOT "
        "from the magnetosphere, NOT via ground waves, and NOT through F-region ducts."
    )

    E["G3C09"] = (
        "Scatter propagation is what allows signals to be heard in the skip zone. The skip zone is "
        "the 'dead zone' between the edge of ground wave coverage and where the first skywave "
        "signal returns to Earth. Normally, no signal reaches this area — ground wave has faded "
        "out and skywave overshoots. But scatter can fill in the gap: ionospheric irregularities "
        "scatter some energy downward into the zone. The signals are weak and distorted (G3C06, "
        "G3C07, G3C08), but they're there. Faraday rotation is polarization rotation (relevant "
        "to satellite signals, not skip zones). Chordal hop is a rare propagation mode, not the "
        "primary mechanism for skip-zone reception. Short-path is normal skywave, which BY "
        "DEFINITION doesn't reach the skip zone."
    )

    E["G3C10"] = (
        "NVIS (Near Vertical Incidence Skywave) is short-distance MF or HF propagation using high "
        "elevation angles — essentially shooting the signal nearly straight up, where it refracts "
        "off the F layer and comes back down in a relatively small area around the transmitter. "
        "NVIS fills the 'gap' between ground wave (which fades out at 50-100 miles) and normal "
        "skywave (which starts at 500+ miles). Frequencies typically used are 40m, 60m, and 80m — "
        "low enough that the F layer will refract them even at near-vertical incidence. NVIS "
        "antennas are mounted low and horizontally to maximize the straight-up radiation pattern. "
        "It's invaluable for regional emergency communications — covering a 300-mile radius "
        "regardless of terrain. It is NOT about operating near the MUF, NOT long-path propagation, "
        "and NOT double-hop near the LUF."
    )

    E["G3C11"] = (
        "The D region is the most absorbent of signals below 10 MHz during daylight hours. This "
        "ties together multiple G3 concepts: the D region is the lowest layer (G3C01), it exists "
        "only during daylight, and it absorbs lower frequencies disproportionately (the 1/f² "
        "relationship means 3.5 MHz signals suffer roughly 8× more absorption than 10 MHz signals). "
        "The F1 and F2 regions refract signals rather than absorbing them — they're the layers you "
        "WANT your signal to reach. The E region refracts some signals too. But the D region just "
        "eats RF energy, converting it to heat through collisions between free electrons and neutral "
        "gas molecules. After sunset, the D region disappears and the lower HF bands open up for "
        "long-distance propagation — connecting directly to G3C05."
    )

    # ── G4A — Station Operation and Setup ────────────────────────────

    E["G4A01"] = (
        "A notch filter removes a single interfering carrier from the receiver passband. Imagine "
        "you're listening on 14.250 MHz and someone has an unmodulated carrier sitting right on top "
        "of the signal you want to hear — a steady tone in your headphones. The notch filter is a "
        "very narrow, very deep rejection filter you can tune to that exact frequency and surgically "
        "remove it without affecting the rest of the passband. It does NOT affect your transmitter "
        "bandwidth (that's the mic EQ or filter settings), it doesn't handle impulse noise (that's "
        "the noise blanker — G4A03), and it doesn't remove splatter (that's the IF passband filter). "
        "Think of it as a sniper rifle, not a shotgun — it takes out one specific interference source."
    )

    E["G4A02"] = (
        "When receiving CW, the receiver converts the incoming carrier to an audible tone using the "
        "BFO (beat frequency oscillator). Normally you listen in the 'normal' sideband, but if "
        "there's an interfering signal close to the one you want, switching to the opposite sideband "
        "moves the BFO to the other side of the IF passband. This changes which signals fall inside "
        "your passband and which fall outside, potentially moving the interferer out while keeping "
        "the desired signal in. It's like looking through a window from a different angle — the same "
        "signals are out there, but your 'view' shifts. It won't eliminate impulse noise (that's "
        "hardware-level), doesn't affect station capacity, and has nothing to do with band edges."
    )

    E["G4A03"] = (
        "A noise blanker works by detecting short-duration noise pulses (like ignition noise from a "
        "car engine or electric fence controllers) and briefly reducing the receiver gain during "
        "each pulse. The key insight: impulse noise is very short in time but very broad in "
        "frequency — it hits all at once and disappears. The noise blanker has a fast-acting gate "
        "that senses these spikes and essentially 'mutes' the receiver for that microsecond. Your "
        "brain fills in the tiny gap, and the noise disappears. It does NOT increase bandwidth "
        "(that would make things worse), doesn't use a filter capacitor (that's an audio filter "
        "approach), and doesn't clip peaks (that's a limiter, which causes distortion). The noise "
        "blanker is the surgical approach — G4A07 covers what happens when noise reduction is "
        "set too aggressively."
    )

    E["G4A04"] = (
        "When tuning a vacuum-tube RF power amplifier, you adjust the TUNE (or PLATE) control to "
        "find a pronounced dip in plate current. Here's why: the TUNE control adjusts the plate "
        "tank circuit to resonance. At resonance, the tank circuit's impedance is maximum, which "
        "means minimum current flows through the tube for a given amount of RF output. A dip in "
        "plate current tells you the tank is resonant and the tube is working efficiently. A peak "
        "would mean you're way off resonance and the tube is drawing maximum current while producing "
        "minimum output — wasting power as heat. This is basic tube amplifier operation, and even "
        "if you never touch a tube amp, the concept of resonance = maximum impedance = minimum "
        "current is the same principle behind matching networks everywhere (G5A01)."
    )

    E["G4A05"] = (
        "ALC (Automatic Level Control) prevents excessive drive to an RF power amplifier. When you "
        "feed too much drive signal into an amplifier, it goes into saturation and produces "
        "distortion, splatter, and harmonics — making your signal wide and ugly. ALC is a feedback "
        "loop: the amplifier samples its output, and if drive is too high, it sends a control "
        "voltage back to the exciter telling it to reduce output. Think of it as a governor on an "
        "engine. It doesn't balance audio response, doesn't directly reduce harmonics (though "
        "preventing overdrive indirectly helps), and doesn't increase efficiency. Its job is purely "
        "to keep the amplifier operating within its linear range. See G4A11 for why ALC and digital "
        "modes don't mix well."
    )

    E["G4A06"] = (
        "An antenna tuner (more accurately called a transmatch) increases power transfer from the "
        "transmitter to the feed line by presenting the correct impedance to the transmitter's "
        "output. This is a common misconception question: the antenna tuner does NOT reduce the "
        "SWR on the feed line between the tuner and the antenna — that SWR stays the same. What "
        "it does is transform the impedance at the shack end of the feed line to match the "
        "transmitter's 50-ohm output. The transmitter 'sees' a 50-ohm load and happily delivers "
        "full power. The SWR between tuner and antenna hasn't changed, but the power reaching "
        "the tuner is maximized. This ties directly to impedance matching concepts from G5A "
        "and the SWR concepts from G9B — the tuner is the matching device between two mismatched "
        "impedances."
    )

    E["G4A07"] = (
        "As you increase the noise reduction level, received signals can become distorted. Noise "
        "reduction algorithms (DSP-based in modern rigs) try to separate signal from noise by "
        "analyzing patterns. But push it too far and the algorithm starts chewing on the desired "
        "signal too, creating artifacts and distortion. It's a tradeoff: more noise reduction = "
        "cleaner background but potentially mangled audio. The receiver frequency stays stable "
        "(noise reduction doesn't affect the local oscillator), CW signals aren't specifically "
        "attenuated (that would be a notch filter — G4A01), and frequency shift isn't a thing. "
        "The practical lesson: use only as much noise reduction as you need, and back off when "
        "signals start sounding weird."
    )

    E["G4A08"] = (
        "The LOAD or COUPLING control on a tube amplifier should be adjusted for desired power "
        "output without exceeding maximum allowable plate current. This control adjusts how tightly "
        "the output tank circuit is coupled to the antenna — more coupling = more power transferred "
        "but also more current through the tube. You increase LOAD until you get the output you "
        "want, watching the plate current meter to make sure you don't exceed the tube's rating. "
        "The correct procedure: first dip the plate current with TUNE (G4A04), then increase LOAD "
        "for desired output, then re-dip TUNE, and iterate. You're NOT tuning for minimum SWR "
        "directly, and NOT trying to maximize plate voltage. You're balancing output power against "
        "tube ratings — a practical application of the impedance matching principles from G5."
    )

    E["G4A09"] = (
        "The delay between keying the amplifier and sending RF output gives the amplifier's T/R "
        "(transmit/receive) relay time to switch the antenna from the transceiver's receiver to the "
        "amplifier's output. Without this delay, RF power would be applied while the relay is still "
        "moving — potentially sending high power back into the transceiver's receiver front end "
        "(very bad) or arcing across the relay contacts. The sequencing goes: key line activates → "
        "amplifier relay switches antenna to amplifier output → delay completes → RF drive begins. "
        "This is NOT about key clicks (that's waveform shaping), NOT about overmodulation, and NOT "
        "about power supply startup time (tube amps do have warmup, but that's handled differently)."
    )

    E["G4A10"] = (
        "An electronic keyer automatically generates properly-timed dots and dashes for CW "
        "operation. You squeeze a paddle left for dashes, right for dots (or vice versa), and the "
        "keyer handles the timing — dot length, dash length (3× dot), inter-element spacing, and "
        "inter-character spacing. A good keyer lets you send clean, consistent CW at any speed "
        "without having to manually time each element. It's NOT a T/R switch (that's separate), "
        "NOT a computer interface for digital modes (that's a sound card or TNC), and NOT an "
        "antenna switching delay (G4A09). Keyers range from simple analog circuits to "
        "microprocessor-based units with memories and contest features."
    )

    E["G4A11"] = (
        "ALC should be inactive during AFSK data transmission because ALC action distorts the "
        "signal. Here's why: AFSK (Audio Frequency Shift Keying) uses constant-amplitude audio "
        "tones to represent data. The transmitter should produce a constant-envelope RF output. "
        "But ALC is designed for voice — it compresses dynamic peaks. When ALC reacts to the "
        "constant AFSK tones, it creates gain variations that distort the waveform, generating "
        "intermodulation products and splatter. The fix: set your drive level so the transmitter "
        "never needs ALC action (typically 50% or less of max power), and verify zero ALC deflection "
        "on the meter. This connects to the broader topic of transmitter linearity tested in G4B08."
    )

    E["G4A12"] = (
        "The dual-VFO feature lets you transmit on one frequency and listen on another — commonly "
        "called 'split' operation. This is essential for working DX stations who are listening "
        "'up' (e.g., the DX station transmits on 14.195 but listens on 14.200-14.210). You set "
        "VFO-A to their transmit frequency to hear them, and VFO-B to the frequency where they're "
        "listening to call them. You cannot transmit on two frequencies simultaneously (that would "
        "require two transmitters), it doesn't enable full duplex (amateur HF is simplex or split, "
        "not duplex), and it has nothing to do with frequency accuracy. Split operation is a "
        "fundamental operating technique tested in G2 as well."
    )

    E["G4A13"] = (
        "A receive attenuator reduces the signal strength arriving at the receiver's front end "
        "to prevent overload from strong signals. If you're near a high-power station or have a "
        "very large antenna, the incoming signals can be strong enough to overdrive the receiver's "
        "first mixer or RF amplifier stage, causing distortion, intermod, and phantom signals that "
        "aren't really there. The attenuator (typically -10, -20, or -30 dB) pads everything down "
        "to a level the receiver can handle cleanly. It's NOT for reducing transmitter drive (that's "
        "a different control), NOT for saving battery power, and NOT for controlling audio volume "
        "(use the AF gain for that). Think of it as sunglasses for your receiver on a bright day."
    )

    # ── G4B — Test and Monitoring Equipment; Two-Tone Test ───────────

    E["G4B01"] = (
        "An oscilloscope contains horizontal and vertical channel amplifiers. The vertical amplifier "
        "boosts the signal you're measuring and deflects the electron beam (or drives the display) "
        "up and down. The horizontal amplifier drives the time base — sweeping the beam left to "
        "right. Together, they create the voltage-vs-time display that makes the oscilloscope "
        "uniquely useful for visualizing waveforms. An ohmmeter just measures resistance, a signal "
        "generator creates signals (no display amplifiers), and an ammeter measures current. Only "
        "the scope has both H and V channel amplifiers — that's what makes it a scope."
    )

    E["G4B02"] = (
        "An oscilloscope can display complex waveforms that a digital voltmeter (DVM) cannot. A DVM "
        "gives you a single number — the voltage at one instant (or its RMS/average). An "
        "oscilloscope shows you the complete shape of the waveform over time: you can see "
        "overshoot, ringing, distortion, noise riding on signals, rise times, and modulation "
        "envelopes. The scope doesn't use less power, can't directly measure complex impedance, "
        "and actually has LESS voltage precision than a good DVM. Its superpower is visualization "
        "— seeing the waveform's shape, not just its magnitude. That's why it's essential for the "
        "tests described in G4B03 and G4B04."
    )

    E["G4B03"] = (
        "An oscilloscope is the best instrument for checking CW keying waveform. When you key a CW "
        "transmitter, the RF output should ramp up and down smoothly — not snap on and off like a "
        "light switch. Too-fast transitions create key clicks (broadband interference that sounds "
        "like clicking to nearby stations). Only an oscilloscope lets you see the actual rise and "
        "fall times of the keying envelope. A field strength meter just shows signal presence, a "
        "sidetone monitor only lets you hear the audio, and a wavemeter only checks frequency. "
        "None of them show you the shape of the keying transitions — that requires the time-domain "
        "display only a scope provides."
    )

    E["G4B04"] = (
        "When checking the RF envelope pattern of a transmitted signal on an oscilloscope, you "
        "connect the attenuated RF output of the transmitter to the vertical input. You need an "
        "actual sample of the RF signal coming out of the transmitter, but at a level the scope "
        "can handle safely (hence 'attenuated' — you can't connect 100 watts directly to a scope "
        "input!). A directional coupler or a resistive tap provides this attenuated sample. You "
        "don't connect the local oscillator (that's an internal signal), an external oscillator "
        "(that's not your transmitted signal), or the balanced mixer output (that's an intermediate "
        "stage). You want to see what's actually leaving the transmitter."
    )

    E["G4B05"] = (
        "Voltmeters have high input impedance to decrease loading on the circuit being measured. "
        "This is fundamental test equipment design: when you connect a voltmeter across a circuit, "
        "you're adding a parallel resistance. If that resistance is low, it draws significant "
        "current, changing the voltage you're trying to measure — the act of measuring changes "
        "the result. A high-impedance voltmeter (10 MΩ is typical for a DMM) draws negligible "
        "current, so the circuit behaves the same with or without the meter connected. This is "
        "the same principle behind why we want high impedance at the input of a receiver — minimize "
        "the impact on the source. It's NOT about frequency response, safety, or display resolution."
    )

    E["G4B06"] = (
        "A digital multimeter (DMM) provides higher precision than an analog multimeter. A DMM "
        "displays exact numerical values — 4.372 volts, not 'somewhere between 4 and 4.5.' This "
        "precision comes from the analog-to-digital converter inside the DMM. Analog meters have "
        "their advantages too (see G4B09 — they're better for peaking/nulling adjustments), but "
        "precision isn't one of them. A DMM isn't necessarily better for computer circuits, isn't "
        "less prone to overload (both types can be damaged), and actually has SLOWER response than "
        "an analog needle for seeing trends. The DMM's strength is precision readings."
    )

    E["G4B07"] = (
        "A two-tone test uses two non-harmonically related audio signals. Typically these are "
        "around 700 Hz and 1900 Hz — chosen specifically so that neither is a harmonic of the "
        "other. Why non-harmonically related? Because if they were harmonically related (say 700 "
        "Hz and 1400 Hz), the intermodulation products would fall on the same frequencies as the "
        "test tones, making them impossible to distinguish. With non-harmonically related tones, "
        "the intermod products fall at predictable but DIFFERENT frequencies, so you can clearly "
        "see them on a scope or spectrum analyzer. They're not phase-shifted copies, not swept "
        "tones, and definitely not square waves (which are full of harmonics by definition)."
    )

    E["G4B08"] = (
        "A two-tone test analyzes transmitter linearity. SSB transmitters must be linear — the "
        "output power should be proportional to the input signal level. When you feed in two equal "
        "tones, a perfectly linear transmitter produces an output with only those two tones. Any "
        "nonlinearity creates intermodulation products — extra signals at frequencies like "
        "2f₁ - f₂ and 2f₂ - f₁ that appear as 'shoulders' on an oscilloscope display. On a scope, "
        "a good linear signal shows a clean envelope pattern; a nonlinear one shows flat tops or "
        "crossover distortion. This test is critical because nonlinearity causes splatter — the "
        "wide, distorted signals that interfere with adjacent channels. It doesn't measure carrier "
        "suppression, FM deviation, or phase shift. Linearity is the target — see G4A11 for why "
        "ALC must be off during this test."
    )

    E["G4B09"] = (
        "An analog multimeter is preferred when adjusting circuits for maximum or minimum values "
        "(peaking and nulling). The moving needle gives you instant visual feedback about the "
        "direction and rate of change — you can see it swinging toward the peak as you turn a "
        "knob, and you can tell immediately when you've passed it. A digital display is just "
        "numbers flickering — you can't easily tell if you're getting closer to or farther from "
        "the target. For logic circuits, high precision work, or frequency measurement, the digital "
        "meter wins (G4B06). But for the tactile, real-time feedback of tuning adjustments, nothing "
        "beats a needle. This is why many experienced hams keep both types on the bench."
    )

    E["G4B10"] = (
        "A directional wattmeter can determine standing wave ratio (SWR). It measures both forward "
        "power (going toward the antenna) and reflected power (coming back). From these two "
        "measurements, you can calculate SWR using the formula SWR = (1 + √(Pr/Pf)) / (1 - √(Pr/Pf)). "
        "This ties directly to the SWR concepts in G9B — the directional wattmeter is the practical "
        "instrument that measures what G9B teaches. It cannot measure front-to-back ratio (you'd "
        "need a field strength meter and the ability to walk around the antenna), can't identify "
        "RF interference sources, and doesn't measure propagation. It measures power in each "
        "direction on a feed line, from which SWR is derived."
    )

    E["G4B11"] = (
        "An antenna analyzer must be connected to the antenna and feed line when making SWR "
        "measurements — because that's what you're measuring! The analyzer generates a low-level "
        "test signal internally, sends it through the feed line to the antenna, and measures what "
        "comes back. It doesn't need a separate receiver or transmitter connected — it IS the "
        "signal source. If you connect a transmitter, you'll destroy the analyzer (it has sensitive "
        "receiver circuitry). If you connect only the analyzer with no antenna/feed line, you're "
        "just measuring the impedance of an open connector. The whole point is to characterize the "
        "antenna system — analyzer on one end, antenna on the other."
    )

    E["G4B12"] = (
        "Strong nearby transmitters can inject received power that interferes with SWR readings on "
        "an antenna analyzer. The analyzer works by sending out a small test signal and measuring "
        "the reflection. But if there's a nearby transmitter blasting RF into your antenna, that "
        "external power mixes with the analyzer's test signal and corrupts the measurement. The "
        "analyzer can't tell the difference between its own reflected signal and the external RF. "
        "This is why you should make antenna measurements when nearby stations aren't transmitting. "
        "It's not intermodulation in the traditional sense, not harmonic generation, and not all "
        "of the above — it's specifically received power corrupting the SWR measurement."
    )

    E["G4B13"] = (
        "An antenna analyzer can measure the impedance of coaxial cable. The analyzer measures "
        "complex impedance (resistance + reactance) at its port, so you can characterize a piece "
        "of coax by connecting it and measuring. You can determine the cable's characteristic "
        "impedance, electrical length, loss, and whether it has faults. What an antenna analyzer "
        "CANNOT measure: front-to-back ratio (requires field measurements around the antenna), "
        "transmitter power output (the analyzer IS the source, not a power meter), or antenna gain "
        "(requires calibrated field strength measurements). The analyzer lives in the impedance "
        "domain — it tells you about impedance, SWR, and related parameters."
    )

    # ── G4C — Interference, Grounding, and Shielding ─────────────────

    E["G4C01"] = (
        "A bypass capacitor reduces RF interference to audio circuits. When RF energy gets into "
        "audio wiring, it can be rectified by semiconductor junctions (diodes, transistor junctions) "
        "and appear as interference in the audio output. A bypass capacitor provides a low-impedance "
        "path to ground for RF frequencies while having negligible effect on audio frequencies — "
        "because capacitive reactance decreases with frequency (X_C = 1/2πfC from G5A). At RF "
        "frequencies (MHz), a small capacitor is essentially a short circuit to ground. At audio "
        "frequencies (kHz), it's nearly invisible. A 'bypass inductor' isn't a real thing in this "
        "context. Diodes (forward or reverse biased) wouldn't help — they'd make the problem "
        "worse since rectification is part of the interference mechanism."
    )

    E["G4C02"] = (
        "Arcing at a poor electrical connection causes interference covering a wide range of "
        "frequencies. An electrical arc is essentially a spark — and sparks generate broadband "
        "RF noise from very low frequencies up through VHF and beyond. Think of it as an "
        "unintentional spark-gap transmitter. Common culprits: loose connections on power lines, "
        "corroded antenna connections, poor contacts in switches. The interference sounds like a "
        "raspy buzz or harsh crackling across the entire HF spectrum. Not using a balun causes "
        "common-mode current issues (narrower interference), lack of rectification doesn't cause "
        "interference (it prevents it), and using a balun on an unbalanced antenna is a matching "
        "issue, not a broadband noise source."
    )

    E["G4C03"] = (
        "An audio device experiencing RF interference from an SSB phone transmitter produces "
        "distorted speech. Here's the mechanism: RF energy from your SSB signal gets into the "
        "audio device's wiring or circuits. Semiconductor junctions in the audio device "
        "(particularly op-amp inputs or transistor stages) act as crude detectors, rectifying "
        "the RF and recovering the modulation — your voice. But it's terrible 'reception' with "
        "no proper filtering, so the result is distorted, garbled speech. It won't be a steady "
        "hum (that's AC line interference), it won't be clicking (that's CW — see G4C04), and "
        "it won't be clearly audible speech (the detection is too crude for that). Distorted but "
        "recognizable speech is the telltale sign of SSB RFI."
    )

    E["G4C04"] = (
        "An audio device experiencing RF interference from a CW transmitter produces on-and-off "
        "humming or clicking. The same detection mechanism as G4C03 applies — semiconductor "
        "junctions rectify the incoming RF — but since CW is just a carrier being switched on "
        "and off (no voice modulation), the detected signal is just a series of pulses matching "
        "the keying pattern. These sound like clicking or buzzing that follows the rhythm of the "
        "CW transmission. You won't hear a pure CW tone (the detection process is too crude), "
        "it won't sound chirpy (chirp is a transmitter defect), and it won't be severely distorted "
        "audio (there's no audio to distort — CW has no modulation). The on-off clicking pattern "
        "matching the CW rhythm is the dead giveaway."
    )

    E["G4C05"] = (
        "High impedance in the ground wire on a particular frequency can cause high voltages that "
        "produce RF burns. Here's the physics: if your ground wire happens to be a significant "
        "fraction of a wavelength (like a quarter wavelength), it can present very high impedance "
        "at the operating frequency instead of the low impedance you expect from a ground connection. "
        "With high impedance and RF current flowing, V = I × Z produces high voltages — on the "
        "metal chassis you're touching. This connects to resonance concepts from G5A — a wire "
        "at a resonant length behaves as a high-impedance element. Flat vs. round wire, insulated "
        "vs. bare wire, and ground rod resonance are all distractors. The real issue is that any "
        "wire has impedance that depends on frequency, and at the wrong length, your 'ground' "
        "isn't grounded at all at RF."
    )

    E["G4C06"] = (
        "A resonant ground connection can cause high RF voltages on the enclosures of station "
        "equipment. This is the direct consequence of G4C05 — when the ground wire's impedance "
        "is high at your operating frequency, the equipment chassis 'floats' at RF even though "
        "it's connected to ground at DC. RF current flowing through the high-impedance ground "
        "creates voltage drops that appear on every metal surface connected to that ground "
        "system. Touch the chassis and you get an RF burn. The fix: keep ground leads short "
        "(much less than a quarter wavelength) and bond all equipment together (G4C09, G4C11). "
        "Resonant grounds don't cause overheating of ground straps, corrosion, or ground loops — "
        "they cause high RF voltages on things you don't want to be hot."
    )

    E["G4C07"] = (
        "Soldered joints should not be used in lightning protection ground connections because the "
        "heat of a lightning strike will destroy the solder joint. Lightning carries enormous "
        "current (tens of thousands of amps) for a very short time. Solder melts at a relatively "
        "low temperature (around 180-190°C for lead solder, 217°C for lead-free), and lightning "
        "generates enough heat to instantly melt solder joints, breaking the ground connection "
        "at the worst possible moment. Instead, use crimped, clamped, or brazed connections — "
        "copper-to-copper mechanical bonds that can survive the thermal shock. Solder flux, "
        "dielectric constant, and the 'all of the above' option are all nonsense in this context. "
        "The issue is purely thermal — solder melts, lightning is hot."
    )

    E["G4C08"] = (
        "A ferrite choke on the audio cable reduces RF interference caused by common-mode current. "
        "Common-mode current is RF flowing on the OUTSIDE of the cable shield (or equally on both "
        "conductors) — it rides along the cable like an antenna rather than being contained inside. "
        "A ferrite choke (snap-on ferrite bead or toroidal core with the cable wound through it) "
        "presents high impedance to common-mode RF without affecting the desired differential "
        "signal inside the cable. It's the same principle behind baluns and common-mode chokes on "
        "antenna feed lines (G9B). Shorting center to shield would kill your audio signal, "
        "grounding the center conductor makes no sense, and extra insulation doesn't help "
        "because the RF is traveling on the conductor, not through the insulation."
    )

    E["G4C09"] = (
        "Ground loops are minimized by bonding equipment enclosures together. A ground loop occurs "
        "when multiple paths to ground exist, creating a loop that acts as an antenna for induced "
        "currents (especially 60 Hz hum from nearby power wiring). The fix is to create a single-point "
        "ground system: bond all equipment chassis together with short, heavy conductors to one "
        "common ground bus, then run a single conductor from that bus to the station ground rod. "
        "This eliminates the loops. Connecting grounds in series creates different ground potentials "
        "(bad). Connecting neutral to ground is a code violation and dangerous. Avoiding lock washers "
        "is backwards — you WANT secure connections. Bonding everything together ensures all "
        "equipment is at the same ground potential."
    )

    E["G4C10"] = (
        "A ground loop in audio connections causes 'hum' on your transmitted signal. The loop acts "
        "as an antenna, picking up 60 Hz (or 120 Hz) from nearby AC power wiring. This hum gets "
        "into the audio path and is transmitted along with your voice — other stations hear a "
        "constant buzzing underneath your speech. This is NOT related to SWR (that's an antenna "
        "system issue), NOT excessive current draw (that's a power supply problem), and NOT "
        "harmonic interference (that's a transmitter filtering issue). If someone says 'you've "
        "got a hum on your signal,' check your audio ground connections and look for loops — "
        "the fix is bonding (G4C09)."
    )

    E["G4C11"] = (
        "Bonding all equipment enclosures together minimizes RF 'hot spots' in an amateur station. "
        "This is the same principle as G4C06 and G4C09 — when equipment chassis are at different "
        "RF potentials, you get voltage differences between them. Touch two pieces of equipment "
        "simultaneously and you complete the circuit through your body (RF burn). Bonding everything "
        "together with short, wide conductors ensures all chassis are at the same RF potential. "
        "Metal enclosures alone don't help if they're not bonded. Surge suppressors protect against "
        "power line spikes, not RF. Low-pass filters on feed lines address harmonic radiation, "
        "not station grounding. The keyword is 'bonding' — connecting all metal together."
    )

    E["G4C12"] = (
        "All metal enclosures must be grounded to ensure that hazardous voltages cannot appear on "
        "the chassis. This is fundamental electrical safety, not just RF practice. If an internal "
        "component fails and the hot wire contacts the chassis, a properly grounded enclosure will "
        "immediately provide a low-resistance path to ground, tripping the breaker or fuse and "
        "removing the danger. Without grounding, the chassis sits at line voltage (120V or more) "
        "waiting for someone to touch it and provide the path to ground through their body. This "
        "doesn't prevent blown fuses (fuses still blow), doesn't prevent signal overload (that's "
        "a receiver issue), and doesn't ground the neutral wire (that's done at the service panel). "
        "It's about preventing electrocution — period."
    )

    # ── G4D — Speech Processors, S Meters, Sideband Operation ────────

    E["G4D01"] = (
        "A speech processor increases the apparent loudness of transmitted voice signals. It does "
        "this by compressing the dynamic range of your voice — bringing up the quiet parts and "
        "limiting the loud parts. Your peak power stays the same, but the average power increases "
        "dramatically. To the receiving station, your signal sounds louder and 'punchier' even "
        "though your PEP hasn't changed. This is particularly useful when trying to punch through "
        "noise or pile-ups on HF. It doesn't increase bass response, doesn't prevent distortion "
        "(in fact, overprocessing causes distortion — G4D03), and doesn't specifically reduce "
        "high-frequency output. Its entire purpose is making you louder."
    )

    E["G4D02"] = (
        "A speech processor increases the average power of an SSB signal while keeping peak power "
        "the same. This is the technical version of G4D01. In SSB, your peak power occurs during "
        "the loudest syllables, but average power during normal speech is much lower — typically "
        "only 20-40% of peak. The speech processor compresses the dynamic range so that average "
        "power comes up closer to the peak. Since S meters respond to average power more than "
        "peaks, the receiving station sees a stronger signal. The processor does NOT increase peak "
        "power (that's set by your transmitter), and does NOT reduce distortion — in fact, "
        "overprocessing increases distortion and intermod (G4D03). Used correctly, a speech "
        "processor can make a 100-watt station sound like 400 watts."
    )

    E["G4D03"] = (
        "An incorrectly adjusted speech processor causes distorted speech, excess intermodulation "
        "products, AND excessive background noise — all of the above. When the compression is "
        "set too aggressively: (1) speech becomes clipped and distorted, (2) the nonlinear "
        "processing creates intermod products that splatter into adjacent frequencies, and (3) "
        "background noise between words gets amplified up to nearly the same level as speech "
        "(since the compressor can't distinguish between voice and noise). This is why you should "
        "set the processor carefully and get on-air reports from another station. More processing "
        "is NOT always better — there's a sweet spot, and going past it makes your signal worse, "
        "not better."
    )

    E["G4D04"] = (
        "An S meter measures received signal strength. It's a relative indicator built into "
        "most receivers and transceivers that gives you a visual reading of how strong the "
        "incoming signal is. The scale typically goes from S1 to S9, then continues in dB above "
        "S9 (e.g., 'S9 plus 20 dB'). It does NOT measure carrier suppression (that requires "
        "a spectrum analyzer), NOT impedance (that requires an impedance meter or antenna "
        "analyzer — G4B13), and NOT transmitter power output (that requires a wattmeter). "
        "The S meter responds to the AGC (automatic gain control) voltage in the receiver, "
        "which varies with signal strength. See G4D05-G4D07 for the math behind S-unit readings."
    )

    E["G4D05"] = (
        "A signal reading 20 dB over S9 is 100 times more powerful than one reading S9. This "
        "uses the fundamental decibel-to-power relationship from G5B: every 10 dB = 10× power. "
        "So 20 dB = 10 × 10 = 100× power. If S9 corresponds to 50 microvolts (the nominal "
        "calibration point on HF), then S9+20 corresponds to a signal that delivers 100 times "
        "more power to the receiver. Note that above S9, the meter reads in dB directly — "
        "not in S-units. Below S9, each S-unit represents 6 dB (G4D06). The dB math here is "
        "the same you learned in G5B — it just applies to received signal strength."
    )

    E["G4D06"] = (
        "One S-unit represents approximately 6 dB of change in signal strength. Since 6 dB "
        "corresponds to a 4× change in power (and a 2× change in voltage), moving from S5 to "
        "S6 means the signal power has quadrupled. The full S-meter scale from S1 to S9 spans "
        "48 dB (8 steps × 6 dB each). Above S9, the meter switches to direct dB readings. The "
        "6 dB per S-unit standard comes from the IARU recommendation, though in practice many "
        "S-meters aren't accurately calibrated. Remember: 6 dB per S-unit below S9, straight "
        "dB above S9. This ties directly to the power calculations in G4D07."
    )

    E["G4D07"] = (
        "To move the S meter from S8 to S9 — one S-unit — you need approximately 4 times the "
        "power. Here's the math: one S-unit = 6 dB (G4D06). A 6 dB increase in power means "
        "multiplying by 4 (since 10^(6/10) ≈ 3.98 ≈ 4). So if the distant station reads you at "
        "S8, you need to quadruple your power output to reach S9. If you're running 25 watts, "
        "you'd need 100 watts. This is why power alone is a poor way to improve your signal — "
        "quadrupling power (and the associated expense) gains you just one S-unit. A better "
        "antenna (G9) or better propagation (G3) often delivers more improvement per dollar "
        "than raw power."
    )

    E["G4D08"] = (
        "A 3 kHz LSB signal with the carrier displayed at 7.178 MHz occupies 7.175 MHz to "
        "7.178 MHz. In Lower Sideband (LSB), the audio information appears BELOW the carrier "
        "frequency. A 3 kHz wide audio signal extends from the carrier down by 3 kHz: "
        "7.178 - 0.003 = 7.175 MHz. So the signal occupies 7.175 to 7.178 MHz. This is critical "
        "for staying within band limits — on 40 meters, General class phone starts at 7.175 MHz, "
        "so setting your carrier to 7.178 with 3 kHz LSB puts your lower edge right at the band "
        "edge. Go any lower with your carrier and you'll be transmitting below your authorized "
        "frequencies. See G4D10 for the general rule about LSB and lower band edges."
    )

    E["G4D09"] = (
        "A 3 kHz USB signal with the carrier displayed at 14.347 MHz occupies 14.347 MHz to "
        "14.350 MHz. In Upper Sideband (USB), the audio information appears ABOVE the carrier "
        "frequency. A 3 kHz wide signal extends from the carrier up by 3 kHz: "
        "14.347 + 0.003 = 14.350 MHz. So the signal occupies 14.347 to 14.350 MHz. On 20 meters, "
        "the phone segment ends at 14.350 MHz, so this puts your upper edge right at the limit. "
        "Set the carrier any higher and you'll splatter above the band edge. See G4D11 for the "
        "general rule about USB and upper band edges. Notice the pattern: LSB extends downward "
        "from the carrier (G4D08), USB extends upward."
    )

    E["G4D10"] = (
        "When using 3 kHz LSB, your displayed carrier frequency should be at least 3 kHz ABOVE "
        "the lower edge of the phone segment. Since LSB extends downward from the displayed "
        "carrier by 3 kHz, you need at least 3 kHz of room below your carrier to keep the signal "
        "within the authorized segment. If the phone segment starts at 7.175 MHz and you're "
        "using 3 kHz LSB, your carrier must be at 7.178 MHz or higher — exactly the scenario "
        "in G4D08. Setting it below the edge, or only 1 kHz above, would put part of your "
        "transmitted signal outside your authorized frequency range. Remember: LSB goes DOWN, "
        "so you need room ABOVE the lower edge."
    )

    E["G4D11"] = (
        "When using 3 kHz USB, your displayed carrier frequency should be at least 3 kHz BELOW "
        "the upper edge of the phone segment. Since USB extends upward from the displayed carrier "
        "by 3 kHz, you need 3 kHz of room above your carrier. If the phone segment ends at "
        "14.350 MHz and you're using 3 kHz USB, your carrier must be at 14.347 MHz or lower — "
        "exactly the scenario in G4D09. The rule is the mirror image of G4D10: USB goes UP, "
        "so you need room BELOW the upper edge. These four questions (G4D08-G4D11) all test the "
        "same concept from different angles: know which direction each sideband extends, and "
        "keep your signal within the authorized bandwidth. This connects directly to the USB/LSB "
        "conventions covered in G2A."
    )

    # ── G4E — HF Mobile, Solar Panels, Alternative Energy ────────────

    E["G4E01"] = (
        "A capacitance hat electrically lengthens a physically short antenna. On HF, a full-size "
        "mobile antenna would be impractically tall (a quarter-wave on 40 meters is about 33 feet). "
        "Mobile antennas are physically shortened and use loading coils to add the missing "
        "electrical length. A capacitance hat — a set of radial wires or a disk at the top of "
        "the antenna — adds electrical 'end capacitance' that further lengthens the antenna "
        "electrically without adding physical height. This is closely related to the antenna "
        "efficiency concepts in G9A — a physically short antenna with loading and a cap hat can "
        "approach the performance of a full-size antenna. It does NOT increase power handling, "
        "reduce radiation resistance (it actually increases it), or lower the radiation angle."
    )

    E["G4E02"] = (
        "A corona ball reduces RF voltage discharge (corona) from the tip of the antenna while "
        "transmitting. At high RF voltages, sharp points concentrate the electric field enough "
        "to ionize the surrounding air, creating visible corona discharge and wasting power. "
        "On an HF mobile antenna running 100 watts with a high-Q loading coil, the voltage at "
        "the tip can reach several thousand volts. The corona ball spreads this voltage over a "
        "larger surface area, reducing the field concentration below the ionization threshold. "
        "It's the same physics behind why lightning rods have pointed tips (to encourage discharge) "
        "while antenna tips need balls (to prevent it). It doesn't narrow bandwidth, increase Q, "
        "or provide physical protection from striking objects."
    )

    E["G4E03"] = (
        "A 100-watt HF mobile installation should be powered directly from the battery using "
        "heavy-gauge wire with fusing. At 13.8V, a 100-watt transceiver draws about 20-22 amps "
        "on transmit. That requires a direct, short, heavy-gauge connection to handle the current "
        "without excessive voltage drop. Going directly to the battery (not the alternator) "
        "provides the most stable voltage and the battery acts as a massive filter capacitor, "
        "smoothing out alternator noise. The alternator's voltage fluctuates with RPM and load. "
        "Balanced transmission line is for antenna feed, not DC power. And fusing is essential — "
        "a short in 20 amps of unfused wire can start a fire. This is the practical application "
        "of the power distribution principles every mobile operator needs."
    )

    E["G4E04"] = (
        "The vehicle's auxiliary power socket (cigarette lighter) should not supply a 100-watt "
        "transceiver because the socket's wiring is inadequate for the current drawn. Most "
        "auxiliary sockets are wired with relatively thin gauge wire and fused at 10-15 amps — "
        "but a 100-watt transceiver draws 20+ amps on transmit. Even if you could plug in a "
        "high-current connector, the wiring between the socket and the fuse box would overheat "
        "and potentially melt. The socket isn't reverse-polarity, RF shielding isn't relevant "
        "for DC power, and engines don't overheat from electrical loads. The issue is simply "
        "that the wire gauge and fuse rating of the accessory circuit can't handle the current. "
        "See G4E03 for the correct approach."
    )

    E["G4E05"] = (
        "The biggest limitation of an HF mobile installation is the efficiency of the electrically "
        "short antenna. A full-size 40-meter quarter-wave vertical is about 33 feet — clearly "
        "impractical on a vehicle. Mobile antennas are physically short and use loading coils to "
        "compensate, but this comes at a cost: reduced efficiency, narrow bandwidth, and lower "
        "radiation resistance (G9A). A shortened antenna might radiate only 10-50% of the power "
        "fed to it, with the rest lost as heat in the loading coil and ground system. 'Picket "
        "fencing' is a VHF/UHF multipath effect (not HF), wire gauge matters but isn't the "
        "primary limitation, and there's no FCC rule specifically limiting mobile power on 75m. "
        "The antenna is always the weakest link in mobile HF."
    )

    E["G4E06"] = (
        "A shortened mobile antenna has very limited operating bandwidth compared to a full-size "
        "antenna. This is because shortened antennas are high-Q (G9A) — the loading coil needed "
        "to compensate for the missing length creates a narrow resonance peak. You might get only "
        "20-50 kHz of usable bandwidth on 40 meters before needing to re-tune. A full-size "
        "quarter-wave vertical might cover most of the band without retuning. The antenna doesn't "
        "distort signals, doesn't have low Q (it has HIGH Q, which is why bandwidth is narrow), "
        "and doesn't increase harmonic radiation. The tradeoff is simple: shorter antenna = "
        "narrower bandwidth = more retuning as you move around the band."
    )

    E["G4E07"] = (
        "All of the listed vehicle systems — the battery charging system, the fuel delivery system, "
        "AND the control computers — can cause receive interference to an HF transceiver. The "
        "alternator and voltage regulator generate switching noise, fuel injectors create impulse "
        "noise as they fire, and the various electronic control modules (ECM, BCM, etc.) have "
        "clock oscillators that radiate RF interference. Modern vehicles are essentially rolling "
        "RF noise generators. Bonding, filtering, and careful routing of antenna cables away from "
        "noise sources are all part of a good mobile installation. This connects to the interference "
        "principles in G4C — the same ferrite chokes (G4C08) and bypass capacitors (G4C01) that "
        "fix station RFI apply to mobile installations."
    )

    E["G4E08"] = (
        "Individual cells in a solar panel are connected in a series-parallel configuration. Each "
        "silicon photovoltaic cell produces about 0.5V (G4E09), so you need many cells in series "
        "to build up to a useful voltage (e.g., 36 cells in series for an 18V nominal panel). "
        "Multiple strings of series-connected cells are then connected in parallel to increase "
        "current capacity. This series-parallel arrangement is the same concept used in battery "
        "packs — series for voltage, parallel for current. 'Shunt,' 'bypass,' and 'full-wave "
        "bridge' are all circuit configurations but none describe how solar cells are interconnected "
        "within a panel."
    )

    E["G4E09"] = (
        "A single fully illuminated silicon photovoltaic cell produces approximately 0.5 VDC "
        "open-circuit. This is determined by the silicon bandgap energy — approximately 1.1 eV — "
        "which sets the maximum voltage a single junction can produce. In practice, you get about "
        "0.5-0.6V per cell. This is why solar panels need many cells in series (G4E08) to reach "
        "useful voltages: a 12V nominal panel uses about 36 cells (36 × 0.5V = 18V open-circuit, "
        "which drops to about 14-15V under load, enough to charge a 12V battery). The other "
        "voltages offered (0.02V, 0.2V, 1.38V) are either too low or too high for a silicon cell. "
        "1.38V is close to the theoretical maximum for a single-junction cell but not achievable "
        "in practice with silicon."
    )

    E["G4E10"] = (
        "A series diode between the solar panel and battery prevents the battery from discharging "
        "back through the panel when illumination is low or absent. At night or in heavy shade, "
        "the solar panel's voltage drops below the battery voltage. Without a blocking diode, "
        "current would flow backward from the battery through the panel's cells — essentially "
        "using the panel as a load and draining the battery. The diode allows current to flow "
        "only from panel to battery (forward direction) and blocks reverse flow. It's NOT a "
        "voltage regulator (that would be a charge controller — G4E11), NOT a current limiter, "
        "and NOT overvoltage protection. It's a one-way valve for current. There's a small "
        "voltage drop across the diode (about 0.3V for Schottky, 0.7V for silicon), which is "
        "why some modern systems use charge controllers with MOSFETs instead."
    )

    E["G4E11"] = (
        "When connecting a solar panel to a lithium iron phosphate (LiFePO4) battery, you must "
        "use a charge controller. LiFePO4 batteries require precise voltage regulation during "
        "charging — they have a narrow charging voltage window (typically 14.0-14.6V for a 12V "
        "battery) and can be damaged or become dangerous if overcharged. A solar panel's output "
        "voltage varies with illumination and can exceed safe charging levels. A charge controller "
        "regulates the voltage and current, implementing the proper charging profile (constant "
        "current → constant voltage → float). A simple series diode (G4E10) prevents backflow "
        "but provides NO voltage regulation. Grounding the frame is good practice but isn't the "
        "critical precaution here. Terminal orientation and series resistors don't address the "
        "core issue. With lithium batteries, a charge controller isn't optional — it's essential "
        "for safety."
    )

    # ── G5A — Reactance, Impedance, and Impedance Matching ──────────

    E["G5A01"] = (
        "In a series LC circuit, inductive reactance (X_L) and capacitive reactance (X_C) "
        "act in opposite directions — inductance resists current changes while capacitance "
        "resists voltage changes. When X_L equals X_C, they cancel each other out completely, "
        "leaving only the small residual resistance of the wire. This is series resonance, and "
        "it makes the impedance very low — essentially just the DC resistance of the components. "
        "This is the opposite of parallel resonance, where impedance goes very high."
    )

    E["G5A02"] = (
        "Reactance is the opposition to alternating current caused by capacitance or inductance. "
        "Unlike resistance, which opposes all current equally (DC and AC), reactance only affects "
        "AC and depends on frequency. An inductor has more reactance at higher frequencies; a "
        "capacitor has less. Reactance is measured in ohms (just like resistance), but it behaves "
        "differently because it stores and releases energy rather than dissipating it as heat."
    )

    E["G5A03"] = (
        "The opposition to AC current flow in an inductor is called reactance — specifically, "
        "inductive reactance (X_L). Don't confuse it with reluctance (opposition to magnetic flux "
        "in a magnetic circuit), conductance (the inverse of resistance), or admittance (the "
        "inverse of impedance). Reactance is the AC-specific opposition that depends on frequency."
    )

    E["G5A04"] = (
        "The opposition to AC current flow in a capacitor is also called reactance — specifically, "
        "capacitive reactance (X_C). Both inductors and capacitors create reactance, but in opposite "
        "directions: inductive reactance increases with frequency while capacitive reactance decreases. "
        "This opposing behavior is what makes resonant circuits possible."
    )

    E["G5A05"] = (
        "An inductor's reactance increases as frequency increases. The formula is X_L = 2πfL. "
        "Double the frequency and you double the reactance. This makes intuitive sense: an inductor "
        "opposes changes in current, and higher-frequency AC changes direction more rapidly, so the "
        "inductor pushes back harder. Note that reactance depends on frequency, not amplitude — "
        "changing the signal strength doesn't change the reactance."
    )

    E["G5A06"] = (
        "A capacitor's reactance decreases as frequency increases. The formula is X_C = 1/(2πfC). "
        "Double the frequency and the reactance drops to half. This is the opposite of an inductor. "
        "At very high frequencies, a capacitor looks almost like a short circuit (very low reactance). "
        "At DC (zero frequency), a capacitor is an open circuit (infinite reactance). This is why "
        "capacitors block DC but pass AC."
    )

    E["G5A07"] = (
        "Admittance is the inverse of impedance, just as conductance is the inverse of resistance. "
        "If impedance tells you how much a circuit opposes current flow, admittance tells you how "
        "easily current flows. It's measured in siemens (S). Susceptance is the inverse of reactance "
        "(not impedance), and reluctance relates to magnetic circuits, not electrical impedance."
    )

    E["G5A08"] = (
        "Impedance is the ratio of voltage to current in an AC circuit — essentially Ohm's Law "
        "extended to AC. Z = V/I. It combines both resistance (which dissipates energy as heat) and "
        "reactance (which stores and releases energy) into a single value measured in ohms. Impedance "
        "is the complete picture of how a circuit opposes AC current flow."
    )

    E["G5A09"] = (
        "Reactance is measured in ohms — the same unit as resistance and impedance. This makes the "
        "math work out cleanly: you can combine resistance and reactance (using vector addition) to "
        "get impedance, all in the same unit. Farads measure capacitance, amperes measure current, "
        "and siemens measure conductance or admittance."
    )

    E["G5A10"] = (
        "Transformers, Pi-networks, and lengths of transmission line can all be used for impedance "
        "matching at radio frequencies. A transformer matches impedance through its turns ratio. A "
        "Pi-network (named for its π shape) uses reactive components to transform impedance. And a "
        "specific length of transmission line acts as an impedance transformer — quarter-wave sections "
        "are especially useful. All three are standard tools in the amateur's matching toolkit."
    )

    E["G5A11"] = (
        "The letter X represents reactance. Z is impedance, R is resistance, B is susceptance, "
        "and Y is admittance. Specifically, X_L is inductive reactance and X_C is capacitive "
        "reactance. These letter conventions are universal in electronics and appear constantly "
        "in circuit analysis."
    )

    E["G5A12"] = (
        "At resonance in an LC circuit, inductive reactance and capacitive reactance are equal and "
        "cancel each other out. This is the defining condition of resonance: X_L = X_C. The resonant "
        "frequency is f = 1/(2π√(LC)). At resonance, current and voltage are NOT necessarily equal, "
        "resistance is NOT cancelled (only reactance cancels), and the circuit does NOT radiate its "
        "energy as radio waves — that would require an antenna."
    )

    # ── G5B — Decibels, Power Calculations, RMS, and PEP ───────────

    E["G5B01"] = (
        "A factor of two change in power is approximately 3 dB. This is the single most important "
        "decibel relationship to memorize. Double the power = +3 dB. Half the power = −3 dB. "
        "The other key relationship is that 10× power = +10 dB. With just these two rules, you "
        "can work out almost any dB problem on the exam."
    )

    E["G5B02"] = (
        "In a parallel resistor circuit, the total current equals the sum of the currents through "
        "each branch. Each branch draws current independently based on its own resistance (I = V/R), "
        "and the total current from the source is the sum of all branch currents. This is Kirchhoff's "
        "Current Law — current entering a node equals current leaving it. Adding more parallel branches "
        "increases total current, which is why parallel resistance is always less than any individual branch."
    )

    E["G5B03"] = (
        "Using P = E²/R: 400² ÷ 800 = 160,000 ÷ 800 = 200 watts. When you know voltage and "
        "resistance but not current, this form of the power equation is the fastest path. You could "
        "also find current first (I = 400/800 = 0.5A) then use P = E×I (400 × 0.5 = 200W) — same answer."
    )

    E["G5B04"] = (
        "Using P = E × I: 12V × 0.2A = 2.4 watts. This is the basic power formula — voltage times "
        "current gives power in watts. A small light bulb drawing 200 milliamps from a 12-volt source "
        "consumes 2.4 watts."
    )

    E["G5B05"] = (
        "Using P = I²R: (0.007A)² × 1250Ω = 0.000049 × 1250 = 0.06125 watts ≈ 61 milliwatts. "
        "First convert 7.0 milliamperes to 0.007 amperes. Then square the current and multiply by "
        "resistance. Watch the units — the answer is in milliwatts, not watts. Getting the metric "
        "prefix wrong is the trap here."
    )

    E["G5B06"] = (
        "PEP (Peak Envelope Power) uses the peak voltage, not peak-to-peak. For 200V peak-to-peak, "
        "the peak voltage is half: 100V. Then PEP = V_peak² / (2 × R) = 100² / (2 × 50) = "
        "10,000 / 100 = 100 watts. Alternatively, convert to RMS first: V_RMS = V_peak / √2 = "
        "100/1.414 = 70.7V, then P = V_RMS²/R = 5000/50 = 100W. Same answer either way."
    )

    E["G5B07"] = (
        "The RMS (Root Mean Square) value of an AC signal produces the same power dissipation as a "
        "DC voltage of equal value. RMS is the \"equivalent heating value\" — a 120V RMS AC signal "
        "heats a resistor exactly as much as 120V DC. This is why AC voltages are specified as RMS "
        "by default: your wall outlet is 120V RMS, which peaks at about 170V."
    )

    E["G5B08"] = (
        "To find peak-to-peak from RMS: first find peak voltage (V_peak = V_RMS × √2 = 120 × 1.414 "
        "= 169.7V), then double it for peak-to-peak (169.7 × 2 = 339.4V). The conversion chain is: "
        "RMS × 1.414 = peak, peak × 2 = peak-to-peak. So V_pp = V_RMS × 2.828. Your 120V RMS wall "
        "outlet actually swings 339 volts from positive peak to negative peak."
    )

    E["G5B09"] = (
        "V_RMS = V_peak × 0.707 (which is 1/√2). So 17V peak × 0.707 = 12.02V ≈ 12 volts RMS. "
        "The 0.707 factor converts peak to RMS for sine waves. Going the other direction, multiply "
        "RMS by 1.414 to get peak. These conversion factors only apply to sine waves — other "
        "waveforms have different relationships."
    )

    E["G5B10"] = (
        "A loss of 1 dB equals approximately 20.6% power loss. Here's the math: "
        "the power ratio for 1 dB is 10^(1/10) = 1.259, so 1/1.259 = 0.794, meaning 79.4% of "
        "power remains — a 20.6% loss. This is useful for evaluating feed line loss: each dB of "
        "loss in your coax costs you about one-fifth of your power."
    )

    E["G5B11"] = (
        "For an unmodulated carrier, the ratio of PEP to average power is 1.00 — they're identical. "
        "An unmodulated carrier has constant amplitude, so the peak envelope power equals the average "
        "power. PEP only differs from average power when the signal's amplitude varies over time, "
        "as in SSB voice or AM. A steady CW carrier or FM signal has a PEP-to-average ratio of 1:1."
    )

    E["G5B12"] = (
        "Using P = V²/R, rearrange to V = √(P × R) = √(1200 × 50) = √60,000 = 244.9 ≈ 245 volts RMS. "
        "This is the RMS voltage because we used the average (RMS) power in the formula. If the question "
        "asked for peak voltage, you'd multiply by 1.414: 245 × 1.414 = 346V peak."
    )

    E["G5B13"] = (
        "For an unmodulated carrier, PEP equals average power — the ratio is 1:1. So if the average "
        "power is 1060 watts, the PEP is also 1060 watts. An unmodulated carrier is a constant-amplitude "
        "signal; there's no variation in the envelope, so peak and average are the same thing."
    )

    E["G5B14"] = (
        "For 500V peak-to-peak: V_peak = 500/2 = 250V. PEP = V_peak² / (2R) = 250² / (2 × 50) = "
        "62,500 / 100 = 625 watts. Or equivalently, V_RMS = 250/√2 = 176.8V, then P = V_RMS²/R = "
        "31,250/50 = 625W. Remember: PEP is always calculated from the peak voltage (not peak-to-peak), "
        "so divide peak-to-peak by 2 first."
    )

    # ── G5C — Series/Parallel Components, Transformers ──────────────

    E["G5C01"] = (
        "A transformer works through mutual inductance — the changing magnetic field created by AC "
        "current in the primary winding induces a voltage in the secondary winding. No direct electrical "
        "connection is needed; the energy transfers through the shared magnetic field. This is why "
        "transformers only work with AC (or pulsating DC) — a steady DC current creates a constant "
        "magnetic field that can't induce voltage in the secondary."
    )

    E["G5C02"] = (
        "A 4:1 voltage step-down transformer has 4 times more turns on the primary than the secondary. "
        "If you reverse it — apply the signal to the secondary (fewer turns) — the transformer now steps "
        "UP by the same ratio: the output is 4 times the input. The turns ratio works both ways; reversing "
        "the input/output reverses the voltage transformation."
    )

    E["G5C03"] = (
        "For resistors in parallel, use the reciprocal formula: 1/R_total = 1/R₁ + 1/R₂ + 1/R₃ = "
        "1/10 + 1/20 + 1/50 = 0.1 + 0.05 + 0.02 = 0.17. R_total = 1/0.17 = 5.88 ≈ 5.9 ohms. "
        "Notice that the total is always less than the smallest individual resistor. Parallel paths "
        "always reduce total resistance because current has more ways to flow."
    )

    E["G5C04"] = (
        "For two resistors in parallel, there's a shortcut: R_total = (R₁ × R₂)/(R₁ + R₂) = "
        "(100 × 200)/(100 + 200) = 20,000/300 = 66.7 ≈ 67 ohms. This \"product over sum\" formula "
        "works for exactly two parallel resistors. The result is always less than the smaller resistor "
        "(67 < 100), which makes physical sense — adding a path reduces opposition."
    )

    E["G5C05"] = (
        "In a step-up transformer, the primary carries more current than the secondary (power in ≈ power out, "
        "so lower voltage side has higher current). Larger wire is needed to handle higher current without "
        "overheating. The secondary has higher voltage but less current, so it can use thinner wire. "
        "This is a direct consequence of conservation of energy: V₁×I₁ ≈ V₂×I₂."
    )

    E["G5C06"] = (
        "Transformer voltage ratio equals turns ratio: V_out/V_in = N_secondary/N_primary = 1500/500 = 3. "
        "So V_out = 120V × 3 = 360 volts. This is a 1:3 step-up transformer — three times as many "
        "secondary turns means three times the output voltage (with proportionally less current)."
    )

    E["G5C07"] = (
        "For impedance matching, the turns ratio equals the square root of the impedance ratio: "
        "N = √(Z₁/Z₂) = √(600/50) = √12 = 3.46 ≈ 3.5 to 1. Note that impedance ratio is the "
        "SQUARE of the turns ratio. A 3.5:1 turns ratio transforms impedance by 3.5² = 12.25:1, "
        "which maps 600Ω down to about 49Ω — close enough to 50Ω for a good match."
    )

    E["G5C08"] = (
        "Capacitors in parallel simply add: C_total = C₁ + C₂ + C₃ = 5.0nF + 5.0nF + 750pF. "
        "First convert to the same unit: 750 pF = 0.75 nF. So C_total = 5.0 + 5.0 + 0.75 = "
        "10.75 nF = 10,750 picofarads. Parallel capacitors add because you're increasing the total "
        "plate area — more area means more charge storage."
    )

    E["G5C09"] = (
        "Capacitors in series use the reciprocal formula (same as resistors in parallel): "
        "1/C_total = 1/100 + 1/100 + 1/100 = 3/100. C_total = 100/3 = 33.3 μF. For N identical "
        "capacitors in series, just divide one capacitor's value by N. Series capacitors always have "
        "LESS total capacitance than any individual capacitor."
    )

    E["G5C10"] = (
        "Inductors in parallel use the reciprocal formula (same as resistors in parallel): "
        "1/L_total = 1/10 + 1/10 + 1/10 = 3/10. L_total = 10/3 = 3.33 mH. Inductors behave like "
        "resistors: series values add directly, parallel values use the reciprocal formula. Three "
        "identical 10 mH inductors in parallel give 3.3 mH — not 30 mH (that would be series)."
    )

    E["G5C11"] = (
        "Inductors in series simply add: L_total = L₁ + L₂ = 20 mH + 50 mH = 70 mH. This is just "
        "like resistors in series — the values add directly. Series inductors increase total inductance "
        "because you're extending the magnetic field through a longer coil path."
    )

    E["G5C12"] = (
        "Two capacitors in series: C_total = (C₁ × C₂)/(C₁ + C₂) = (20 × 50)/(20 + 50) = "
        "1000/70 = 14.3 μF. Use the \"product over sum\" shortcut for two components. The result "
        "(14.3 μF) is less than the smaller capacitor (20 μF), confirming series capacitance is "
        "always reduced."
    )

    E["G5C13"] = (
        "To increase capacitance, add a capacitor in parallel. Parallel capacitors add: C_total = "
        "C₁ + C₂. Adding a capacitor in series would decrease the total capacitance (series "
        "capacitance is always less). Inductors don't add to capacitance at all. Think of it like "
        "adding more plate area — parallel = more area = more capacitance."
    )

    E["G5C14"] = (
        "To increase inductance, add an inductor in series. Series inductors add: L_total = L₁ + L₂. "
        "Adding an inductor in parallel would decrease the total inductance. Capacitors don't add to "
        "inductance. Think of it like extending a coil — series = longer coil = more inductance."
    )

    # ── G6A — Resistors, Capacitors, Inductors, Diodes, Transistors, Tubes, Batteries ──

    E["G6A01"] = (
        "A standard 12-volt lead-acid battery should never be discharged below 10.5 volts if you "
        "want maximum service life. Lead-acid batteries suffer permanent damage from deep discharge — "
        "the lead sulfate crystals that form on the plates during discharge become hard and crystalline "
        "(sulfation) if left too long or taken too low, and they won't convert back during recharging. "
        "10.5V is the widely accepted cutoff for a 12V battery (about 1.75V per cell for a 6-cell battery). "
        "Going to 8.5V or 6V is deep abuse that dramatically shortens battery life."
    )

    E["G6A02"] = (
        "A battery with low internal resistance can deliver high discharge current. Think of internal "
        "resistance as a bottleneck inside the battery — when you draw current, some voltage drops "
        "across this internal resistance (V_drop = I × R_internal), reducing what's available to your "
        "load. Low internal resistance means less voltage drop under load, so the battery can push "
        "more current without sagging. This is why lithium and AGM batteries (low internal resistance) "
        "are preferred for high-current applications like powering a 100W transceiver. Internal "
        "resistance doesn't directly affect battery life, voltage rating, or recharge speed."
    )

    E["G6A03"] = (
        "A germanium diode has a forward threshold voltage of approximately 0.3 volts. This is the "
        "voltage you need to apply across the diode before it starts conducting significantly. Compare "
        "this to silicon at 0.7V — germanium's lower threshold makes it useful in low-signal detector "
        "circuits where you can't afford to lose 0.7V. The tradeoff is that germanium diodes have "
        "higher reverse leakage current and are less thermally stable than silicon. Memorize the pair: "
        "germanium = 0.3V, silicon = 0.7V."
    )

    E["G6A04"] = (
        "Electrolytic capacitors pack a lot of capacitance into a small volume — that's their "
        "defining advantage. They achieve this by using an extremely thin oxide layer as the "
        "dielectric (the insulating layer between plates). The tradeoff: they're polarized (must be "
        "installed with correct polarity), have loose tolerances (±20% is typical), relatively high "
        "leakage current, and limited frequency response — making them unsuitable for RF work. "
        "You'll find them in power supply filtering where you need hundreds or thousands of "
        "microfarads in a reasonable size."
    )

    E["G6A05"] = (
        "A silicon junction diode has a forward threshold voltage of approximately 0.7 volts. This "
        "is the most common diode type in electronics and the voltage you'll encounter most often. "
        "Below 0.7V, the diode essentially blocks current; above 0.7V, it conducts freely. The "
        "0.7V drop remains roughly constant regardless of how much current flows (within limits). "
        "Pair this with the germanium value: silicon = 0.7V, germanium = 0.3V. The exam tests both."
    )

    E["G6A06"] = (
        "Wire-wound resistors are literally coils of resistance wire — and a coil of wire is an "
        "inductor. At DC or low frequencies, this parasitic inductance doesn't matter. But at radio "
        "frequencies, the inductance becomes significant and makes the resistor behave unpredictably — "
        "its impedance changes with frequency, it may resonate at certain frequencies, and it throws "
        "off the performance of tuned circuits. For RF work, use carbon composition, metal film, or "
        "metal oxide resistors instead — they have minimal parasitic inductance."
    )

    E["G6A07"] = (
        "When a bipolar transistor is used as a switch, it operates at two extremes: saturation "
        "(fully ON) and cutoff (fully OFF). In saturation, the transistor conducts as hard as it "
        "can — collector-to-emitter acts almost like a short circuit. In cutoff, no current flows — "
        "it acts like an open circuit. The active region (between these extremes) is used for "
        "linear amplification, not switching. Enhancement and depletion modes are MOSFET terms, "
        "not bipolar transistor terms. Peak and valley current points relate to tunnel diodes."
    )

    E["G6A08"] = (
        "Low-voltage ceramic capacitors are comparatively low cost — that's their standout "
        "characteristic. They're cheap to manufacture, widely available, and good enough for many "
        "general-purpose applications. However, they don't have tight tolerance (values can drift "
        "significantly with temperature and applied voltage), they're not particularly stable "
        "(especially Y5V and Z5U types), and they don't offer especially high capacitance for their "
        "size (electrolytics beat them there). For precision or stability, you'd choose an NP0/C0G "
        "ceramic or a mica capacitor — but those cost more."
    )

    E["G6A09"] = (
        "In a MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor), the gate is separated "
        "from the channel by a thin insulating layer — specifically, a silicon dioxide (SiO₂) layer. "
        "This is the 'oxide' in MOSFET and it's the defining feature of the device. Because the gate "
        "is insulated, virtually no current flows into the gate — MOSFETs have extremely high input "
        "impedance. Compare this to a JFET, where the gate IS a back-biased junction (not insulated), "
        "or a bipolar transistor, where base current is required. The insulated gate is why MOSFETs "
        "are so sensitive to static discharge — that thin oxide layer can be punctured by ESD."
    )

    E["G6A10"] = (
        "The control grid regulates electron flow in a vacuum tube. It sits between the cathode "
        "(which emits electrons when heated) and the plate (which collects them). By varying the "
        "voltage on the control grid, you control how many electrons get through — a small voltage "
        "change on the grid produces a large change in plate current, which is how tubes amplify. "
        "The screen grid (in tetrodes and pentodes) reduces plate-to-grid capacitance. The "
        "suppressor grid (in pentodes) reduces secondary emission. Don't confuse these — the "
        "control grid is the one that actually controls amplification."
    )

    E["G6A11"] = (
        "Every real inductor has some parasitic capacitance between its windings. At low frequencies, "
        "the inductance dominates and the component behaves as expected — like an inductor. But at "
        "the self-resonant frequency, the parasitic capacitance resonates with the inductance (just "
        "like an LC circuit). Above that frequency, the capacitance dominates and the inductor "
        "actually becomes capacitive — its reactance decreases with increasing frequency instead "
        "of increasing. This is why you must choose inductors rated for your operating frequency. "
        "An inductor used above its self-resonant frequency isn't really an inductor anymore."
    )

    E["G6A12"] = (
        "The screen grid's primary purpose is to reduce the capacitance between the control grid "
        "and the plate. In a triode (three-element tube), there's significant capacitance between "
        "the grid and plate, which causes unwanted feedback and oscillation — especially at higher "
        "frequencies. The screen grid, placed between the control grid and plate, acts as an "
        "electrostatic shield that dramatically reduces this coupling capacitance. This is why "
        "tetrodes (four-element tubes with a screen grid) were developed — they're much more "
        "stable at RF frequencies than triodes."
    )

    # ── G6B — ICs, MMICs, Connectors, Ferrite Cores ─────────────────

    E["G6B01"] = (
        "Ferrite core performance at different frequencies is determined by the composition or "
        "'mix' of materials used to make the core. Ferrite is a ceramic compound of iron oxide "
        "mixed with other metal oxides (like manganese, zinc, or nickel), and different recipes "
        "produce different magnetic properties. Mix 43, for example, works well from 10 MHz to "
        "1 GHz for EMI suppression, while Mix 61 is designed for 200 kHz to 10 MHz inductors. "
        "The physical dimensions (thickness, diameter ratios) affect inductance, but it's the "
        "material composition that determines which frequency range the core works best in."
    )

    E["G6B02"] = (
        "MMIC stands for Monolithic Microwave Integrated Circuit. 'Monolithic' means the entire "
        "circuit — transistors, resistors, capacitors, transmission lines — is fabricated on a "
        "single semiconductor chip (usually gallium arsenide, GaAs). These are designed specifically "
        "for microwave frequencies (typically above 1 GHz) where conventional ICs can't keep up. "
        "You'll find MMICs in satellite receivers, cell phones, and microwave amateur radio "
        "equipment. The other answer choices are made-up acronyms."
    )

    E["G6B03"] = (
        "CMOS (Complementary Metal-Oxide-Semiconductor) circuits consume very low power compared "
        "to TTL (Transistor-Transistor Logic). CMOS uses complementary pairs of MOSFETs that draw "
        "almost zero current when in a static state — power is only consumed during switching "
        "transitions. TTL circuits use bipolar transistors that draw continuous current even when "
        "not switching. This makes CMOS ideal for battery-powered devices and any application where "
        "power consumption matters. Neither CMOS nor TTL is designed for RF amplification or power "
        "supply regulation — those are analog tasks, not digital logic functions."
    )

    E["G6B04"] = (
        "BNC connectors maintain low SWR up to about 4 GHz. BNC (Bayonet Neill-Concelman) is a "
        "quick-connect bayonet-style RF connector commonly used on test equipment, lower-power "
        "transceivers, and lab instruments. The 4 GHz limit is where the connector's geometry "
        "starts to cause significant impedance mismatches and radiation losses. Below 4 GHz, it's "
        "a reliable 50-ohm connector. For higher frequencies, you'd move to SMA or Type N "
        "connectors. For HF through UHF amateur use, BNC is more than adequate."
    )

    E["G6B05"] = (
        "A ferrite core toroidal inductor offers all three listed advantages: large inductance "
        "values are obtainable, the core material can be optimized for specific frequency ranges "
        "(through different ferrite mixes), and the toroidal (donut) shape contains most of the "
        "magnetic field within the core — meaning less stray coupling to nearby components. The "
        "self-shielding property of toroids is especially valuable in amateur radio where multiple "
        "circuits live close together on a circuit board or inside a compact enclosure. This is "
        "why toroids are the go-to inductor form for homebrew projects."
    )

    E["G6B06"] = (
        "An operational amplifier (op-amp) is an analog device. It amplifies continuous signals "
        "with extremely high gain and is the workhorse of analog circuit design — used for "
        "amplification, filtering, buffering, and mathematical operations on signals. It's NOT "
        "digital (digital deals with discrete 0/1 states), NOT an MMIC (those are specifically "
        "for microwave frequencies), and NOT programmable logic (that's FPGAs and CPLDs). The "
        "classic 741 op-amp has been in production since the 1960s. Modern ham radio equipment "
        "uses op-amps in audio stages, AGC circuits, and active filters."
    )

    E["G6B07"] = (
        "The Type N connector is a moisture-resistant, threaded RF connector usable up to 10 GHz. "
        "It was designed by Paul Neill (the 'N') for military and professional applications where "
        "weatherproofing matters. The threaded coupling provides a reliable, vibration-resistant "
        "connection. It's a larger connector than BNC or SMA, commonly seen on commercial antenna "
        "systems and higher-quality amateur installations. It is NOT a bayonet connector (that's "
        "BNC), NOT a low-noise VHF connector (that's not a thing), and NOT a nickel-plated PL-259 "
        "(the PL-259/SO-239 is a completely different connector design)."
    )

    E["G6B08"] = (
        "An LED emits light when it is forward biased — meaning current flows from anode to cathode "
        "in the normal direction. When electrons cross the junction and recombine with holes, they "
        "release energy as photons (light). The color depends on the semiconductor material and the "
        "band gap energy. Reverse biasing an LED doesn't produce light (and too much reverse voltage "
        "damages it). Zener voltage is a property of Zener diodes operated in reverse breakdown, and "
        "the tunnel effect relates to tunnel diodes — neither applies to LED light emission."
    )

    E["G6B10"] = (
        "A ferrite bead or core reduces common-mode RF current by creating an impedance in the "
        "current's path. The ferrite material has high magnetic permeability — when common-mode "
        "current flows through the cable, it creates a magnetic field in the ferrite which opposes "
        "the current (impedance). For differential-mode signals (the desired signal), the magnetic "
        "fields from the two conductors cancel inside the ferrite, so the desired signal passes "
        "through unaffected. This selective impedance is why ferrite chokes are so effective at "
        "suppressing RF interference on cables without degrading the wanted signal. They don't "
        "convert modes, cancel currents, or expel fields — they simply add impedance."
    )

    E["G6B11"] = (
        "SMA (SubMiniature version A) is a small threaded connector designed for signals up to "
        "several GHz — typically rated to 18 GHz or higher depending on the variant. It's widely "
        "used on SDR dongles, handheld transceivers, VHF/UHF equipment, and test instruments where "
        "a compact, reliable microwave-capable connection is needed. The threaded coupling ensures "
        "a consistent 50-ohm impedance match. SMA is NOT an adaptor, NOT for serial data, and NOT "
        "a push-on high-voltage connector. You'll see SMA connectors everywhere in modern amateur "
        "radio equipment, especially anything above VHF."
    )

    E["G6B12"] = (
        "RCA phono connectors are commonly used for low-frequency or DC signal connections to "
        "transceivers — things like audio input/output, external speaker connections, and accessory "
        "ports. They're simple, cheap, and adequate for audio frequencies. They are NOT suitable "
        "for RF — they're unshielded and have poor impedance characteristics at radio frequencies. "
        "PL-259, BNC, and Type N are all RF connectors designed to maintain 50-ohm impedance. "
        "If you see an RCA jack on a radio, it's for audio or control signals, not antenna connections."
    )

    # ── G7A — Power Supplies and Schematic Symbols ──────────────

    E["G7A01"] = (
        "A bleeder resistor is connected across the filter capacitors in a power supply so that "
        "when you turn the supply off, the capacitors have a discharge path. Without it, those "
        "capacitors can hold a lethal charge for minutes or even hours — especially in high-voltage "
        "supplies used with vacuum tube amplifiers. The bleeder resistor slowly drains the stored "
        "energy to a safe level. It's a safety component, not a performance one. It doesn't act as "
        "a fuse, doesn't affect induction coils, and has nothing to do with ground loops."
    )

    E["G7A02"] = (
        "The filter network in a power supply smooths the pulsating DC that comes out of the "
        "rectifier into something closer to pure DC. It uses capacitors and inductors — the "
        "capacitors charge up during voltage peaks and release energy during dips, while inductors "
        "resist sudden current changes, further smoothing the output. This is a direct application "
        "of G5 reactance concepts: capacitors pass AC ripple to ground (low reactance at ripple "
        "frequency) while inductors block it (high reactance at ripple frequency). Diodes are "
        "rectifiers, not filters. Transformers change voltage levels but don't filter."
    )

    E["G7A03"] = (
        "A full-wave rectifier using a center-tapped transformer needs only two diodes. Here's "
        "how it works: the center tap provides a midpoint reference (ground). During one half of "
        "the AC cycle, current flows through the top half of the secondary and diode #1. During "
        "the other half, current flows through the bottom half and diode #2. Each diode handles "
        "one half-cycle, but the output sees BOTH halves — hence 'full-wave.' A full-wave bridge "
        "rectifier also produces full-wave output but uses four diodes and no center tap. A "
        "half-wave rectifier uses just one diode. Don't confuse the two full-wave types."
    )

    E["G7A04"] = (
        "A half-wave rectifier uses only one diode — that's its defining characteristic. The diode "
        "passes current during one half of the AC cycle and blocks it during the other half. This "
        "makes it the simplest possible rectifier circuit, but also the least efficient: half the "
        "input power is wasted. The ripple frequency equals the AC input frequency (not twice it — "
        "that's full-wave). Less current is available compared to full-wave designs, and the output "
        "voltage is NOT doubled. Half-wave rectifiers are used where simplicity matters more than "
        "performance — like low-current bias supplies."
    )

    E["G7A05"] = (
        "A half-wave rectifier converts 180 degrees of the AC cycle — exactly one half. The diode "
        "conducts during the positive half-cycle (0° to 180°) and blocks during the negative "
        "half-cycle (180° to 360°). That's where the name comes from: half the wave gets through, "
        "half is discarded. Think of a full AC cycle as 360°: half-wave uses 180°, full-wave uses "
        "all 360°."
    )

    E["G7A06"] = (
        "A full-wave rectifier converts 360 degrees — the entire AC cycle. Both the positive AND "
        "negative half-cycles contribute to the DC output. During the negative half, the rectifier "
        "circuit flips the polarity so it adds to the output rather than subtracting. Whether you "
        "use a center-tapped transformer with two diodes or a bridge with four diodes, the result "
        "is the same: every part of the input waveform contributes useful output. This doubles the "
        "ripple frequency compared to half-wave and produces smoother DC."
    )

    E["G7A07"] = (
        "An unfiltered full-wave rectifier produces DC pulses at TWICE the AC input frequency. "
        "Here's why: each half-cycle of the AC input produces one DC pulse. Since there are two "
        "half-cycles per full cycle, you get two pulses per AC cycle — double the frequency. If "
        "your AC input is 60 Hz, the unfiltered output has a 120 Hz ripple. This is actually an "
        "advantage of full-wave over half-wave: the higher ripple frequency is easier to filter "
        "out (capacitors and inductors are more effective at higher frequencies — remember X_C = "
        "1/(2πfC) from G5). The output is NOT steady DC (that requires filtering) and NOT a sine "
        "wave (the negative halves have been flipped positive)."
    )

    E["G7A08"] = (
        "Switchmode power supplies operate at high frequency (typically 50 kHz to several MHz), "
        "and this high-frequency operation allows the use of much smaller transformers and filter "
        "components. From G5, we know that a transformer's ability to transfer power depends on "
        "the rate of change of current (higher frequency = faster changes). At 60 Hz, you need a "
        "big, heavy iron-core transformer. At 100 kHz, a tiny ferrite-core transformer does the "
        "same job. Same principle applies to filter capacitors and inductors — at higher "
        "frequencies, smaller values provide the same filtering effect. That's why your laptop "
        "charger is small and light while old-school linear supplies were heavy bricks."
    )

    E["G7A09"] = (
        "Symbol 1 in Figure G7-1 represents a field-effect transistor (FET). The FET schematic "
        "symbol shows a channel with a gate electrode that doesn't directly touch it — reflecting "
        "the physical structure where the gate controls current flow through an electric field "
        "rather than direct contact. In a MOSFET, the gate is insulated by an oxide layer (as "
        "covered in G6). In a JFET, the gate is a reverse-biased junction. Either way, the "
        "symbol shows the gate offset from the channel. Look for the arrow on the gate or source "
        "to distinguish N-channel from P-channel."
    )

    E["G7A10"] = (
        "Symbol 5 in Figure G7-1 represents a Zener diode. The Zener symbol looks like a regular "
        "diode but with bent or 'kinked' ends on the bar (cathode). This distinguishes it from "
        "a standard rectifier diode, which has a straight bar. Zener diodes are designed to "
        "operate in reverse breakdown at a specific voltage — that's what makes them useful as "
        "voltage references and regulators. When reverse voltage reaches the Zener voltage, the "
        "diode conducts and clamps the voltage at that level. The bent cathode bar is the visual "
        "cue on schematics."
    )

    E["G7A11"] = (
        "Symbol 2 in Figure G7-1 represents an NPN junction transistor. The BJT schematic symbol "
        "shows three leads: base, collector, and emitter. The key to identifying NPN vs PNP is "
        "the arrow on the emitter: in an NPN transistor, the arrow points AWAY from the base "
        "(outward — 'Not Pointing iN'). In a PNP, the arrow points inward toward the base. "
        "From G6, remember that BJTs in switching mode operate in saturation (ON) and cutoff "
        "(OFF). The NPN is the most common transistor type in amateur radio circuits."
    )

    E["G7A12"] = (
        "Symbol 6 in Figure G7-1 represents a solid-core (iron-core) transformer. A transformer "
        "symbol shows two coils (inductors) side by side — the primary and secondary windings. "
        "What distinguishes a solid-core transformer from an air-core transformer is the lines "
        "drawn between the coils: solid lines indicate a solid (iron or ferrite) core. An "
        "air-core transformer has no lines between the coils, or dashed lines. From G5, recall "
        "that transformers work through mutual inductance and are used for impedance matching "
        "and voltage transformation."
    )

    E["G7A13"] = (
        "Symbol 7 in Figure G7-1 represents a tapped inductor. A tapped inductor looks like a "
        "regular inductor symbol (a coil) but with an additional connection point partway along "
        "the winding. This tap lets you access a fraction of the total inductance, which is "
        "useful for impedance matching and tuning. It's like a center-tapped transformer "
        "secondary but with just one winding. Don't confuse it with a transformer (two separate "
        "coils) or a full inductor (no tap point)."
    )

    # ── G7B — Digital Circuits, Amplifiers, Oscillators ─────────────

    E["G7B01"] = (
        "Neutralizing an amplifier eliminates self-oscillations. Self-oscillation happens when "
        "some of the amplifier's output feeds back to its input in phase — creating unintended "
        "positive feedback that makes the amplifier act like an oscillator instead of an amplifier. "
        "This is the same grid-to-plate capacitance problem that the screen grid addresses in "
        "vacuum tubes (from G6). Neutralization adds a deliberate canceling signal that's equal "
        "in amplitude but opposite in phase to the unwanted feedback. The result: the amplifier "
        "amplifies without oscillating. It has nothing to do with modulation index, standby "
        "control, or frequency stability."
    )

    E["G7B02"] = (
        "Class C has the highest efficiency of the standard amplifier classes — typically 60-80%. "
        "Here's the efficiency hierarchy: Class A (~25-50%) conducts 100% of the time but wastes "
        "a lot of power as heat. Class B (~50-65%) conducts 50% of the time. Class AB (between A "
        "and B) is a compromise. Class C conducts less than 50% of the time — the device is OFF "
        "for most of the cycle, only turning on for brief pulses. Less conduction time = less "
        "wasted power = higher efficiency. The tradeoff: Class C severely distorts the waveform, "
        "making it unsuitable for linear signals like SSB or AM. It's fine for FM and CW where "
        "amplitude doesn't carry information."
    )

    E["G7B03"] = (
        "A two-input AND gate outputs HIGH only when BOTH inputs are HIGH. Think of it as a "
        "series circuit with two switches — current only flows when switch A AND switch B are "
        "both closed. The truth table is simple: 0+0=0, 0+1=0, 1+0=0, 1+1=1. Compare with OR "
        "(output high when EITHER input is high) and NAND (output high UNLESS both inputs are "
        "high — the inverse of AND). Digital logic gates are the building blocks of the counters, "
        "shift registers, and PLDs that appear in amateur radio equipment."
    )

    E["G7B04"] = (
        "A Class A amplifier conducts 100% of the time — the amplifying device never turns off. "
        "It's biased at the center of its operating range, so the entire input waveform is "
        "reproduced faithfully at the output. This makes Class A the most linear amplifier class "
        "— it preserves the input waveform with minimal distortion. The tradeoff is efficiency: "
        "the device is always drawing current even with no signal, so at least half the DC input "
        "power is wasted as heat. Class A is used where signal quality matters more than "
        "efficiency — like low-level driver stages and audio preamplifiers."
    )

    E["G7B05"] = (
        "A 3-bit binary counter has 2³ = 8 states (0 through 7). Each bit can be 0 or 1, giving "
        "two possible values per bit. With 3 bits, you get 2 × 2 × 2 = 8 combinations: 000, 001, "
        "010, 011, 100, 101, 110, 111. The pattern is always 2^N states for N bits. A 4-bit "
        "counter would have 16 states, an 8-bit counter 256 states. Binary counters are essential "
        "in frequency dividers, digital displays, and timing circuits found in amateur radio "
        "equipment."
    )

    E["G7B06"] = (
        "A shift register is a clocked array of circuits that passes data in steps along the "
        "array. Each clock pulse shifts the data one position — like a bucket brigade where each "
        "person passes their bucket to the next. Shift registers are built from flip-flops "
        "connected in series. They're used for serial-to-parallel conversion (receiving serial "
        "data and outputting it in parallel), parallel-to-serial conversion, data buffering, and "
        "delay lines. They're fundamental components in digital communications equipment. They're "
        "NOT operational amplifiers, mixers, or arithmetic circuits."
    )

    E["G7B07"] = (
        "A sine wave oscillator has two essential components: a filter and an amplifier operating "
        "in a feedback loop. The amplifier provides gain, and the filter determines the frequency "
        "by selecting which frequency gets positive feedback. When the loop gain at the filter's "
        "frequency equals exactly 1 and the phase shift is 0° (or 360°), the circuit sustains "
        "oscillation at that frequency. This is the Barkhausen criterion. LC oscillators use an "
        "LC tank circuit as the filter. Crystal oscillators use a quartz crystal (which behaves "
        "like an extremely selective LC circuit). Without the feedback loop, you just have an "
        "amplifier. Without the filter, you'd get noise, not a sine wave."
    )

    E["G7B08"] = (
        "RF power amplifier efficiency is calculated by dividing the RF output power by the DC "
        "input power. Efficiency = P_RF_out / P_DC_in × 100%. If your amplifier draws 500W from "
        "the power supply and delivers 300W of RF, its efficiency is 300/500 = 60%. The remaining "
        "200W becomes heat — which is why amplifiers need heatsinks or fans. Higher efficiency "
        "means less wasted heat and a smaller power supply requirement. This is why Class C "
        "(60-80% efficient) is preferred over Class A (25-50%) when linearity isn't needed."
    )

    E["G7B09"] = (
        "The frequency of an LC oscillator is determined by the inductance and capacitance in "
        "the tank circuit — using the resonant frequency formula from G5: f = 1/(2π√(LC)). The "
        "tank circuit resonates at a specific frequency where inductive and capacitive reactance "
        "are equal (X_L = X_C), and that's the frequency the oscillator produces. Change L or C "
        "and you change the frequency. This is how variable-frequency oscillators (VFOs) work: a "
        "variable capacitor tunes the frequency by changing C in the tank circuit. Crystal "
        "oscillators use the crystal's equivalent LC values for extreme stability."
    )

    E["G7B10"] = (
        "A linear amplifier is one where the output preserves the input waveform — the output is "
        "an amplified but faithful copy of the input. 'Linear' means the output is directly "
        "proportional to the input at all amplitude levels. This is essential for SSB and AM "
        "signals where the amplitude carries information — any distortion of the waveform creates "
        "splatter (unwanted sideband energy that interferes with adjacent channels). Class A and "
        "Class AB amplifiers are linear. Class C is NOT linear — it clips the waveform severely. "
        "A frequency multiplier is the opposite of linear — it deliberately distorts the signal "
        "to generate harmonics."
    )

    E["G7B11"] = (
        "Class C is appropriate for amplifying FM signals because FM carries information in "
        "frequency changes, not amplitude changes. Since the amplitude of an FM signal is "
        "constant (it doesn't matter if the peaks get clipped), Class C's severe waveform "
        "distortion doesn't lose any information. The tuned output circuit of the Class C "
        "amplifier reconstructs the sine wave at the fundamental frequency. For SSB and AM, "
        "amplitude carries the information, so Class C's clipping would destroy the signal. "
        "That's why SSB transmitters use Class AB amplifiers — they're less efficient but "
        "preserve the amplitude envelope."
    )

    # ── G7C — Receivers, Transmitters, DSP, SDR, Filters ────────────

    E["G7C01"] = (
        "A filter selects one sideband from the output of a balanced modulator. The balanced "
        "modulator produces a double-sideband suppressed-carrier (DSB-SC) signal — both sidebands "
        "but no carrier. To get a single-sideband (SSB) signal, you need to remove one of the "
        "sidebands. A crystal or mechanical filter does this by having a very narrow passband that "
        "includes only the desired sideband while rejecting the other. The carrier oscillator "
        "generates the carrier frequency, the IF amplifier boosts the signal, and the RF amplifier "
        "handles the final output — but it's the filter that performs the sideband selection."
    )

    E["G7C02"] = (
        "A balanced modulator produces double-sideband (DSB) modulated RF with the carrier "
        "suppressed. It combines the audio signal with the carrier such that the carrier itself "
        "cancels out, leaving only the upper and lower sidebands. This is the first step in "
        "generating an SSB signal. The 'balanced' part refers to the circuit's symmetry, which "
        "causes the carrier to cancel. The output is NOT FM (that requires a different modulation "
        "method), NOT extracted audio (that's demodulation), and NOT equalized audio (that's "
        "an audio processing function). After the balanced modulator, a filter selects one "
        "sideband to complete the SSB generation process."
    )

    E["G7C03"] = (
        "An impedance matching transformer at a transmitter output presents the desired impedance "
        "to both the transmitter and the feed line. From G5, you know that maximum power transfer "
        "occurs when impedances are matched, and mismatched impedances cause reflections (high "
        "SWR). If your antenna feed line is 50 ohms but the transmitter output stage wants to see "
        "a different impedance, a matching transformer bridges the gap using the turns ratio "
        "relationship: Z_ratio = (N₁/N₂)². The goal is NOT to minimize power output, reduce "
        "ripple, or minimize radiation resistance — it's to ensure efficient power transfer by "
        "presenting the right impedance to each side of the connection."
    )

    E["G7C04"] = (
        "A product detector is used in an SSB receiver to extract the modulated signal. SSB "
        "signals have no carrier — the carrier was suppressed during transmission. To demodulate "
        "SSB, the receiver must reinsert a replacement carrier (called the beat frequency oscillator "
        "or BFO) and mix it with the received signal. The product detector does this mixing. "
        "Without a product detector (or equivalent), an SSB signal sounds like unintelligible "
        "quacking. The term 'product' comes from the mathematical operation — multiplying (taking "
        "the product of) two signals. It's not test equipment, not a frequency multiplier, and "
        "not an FM filter."
    )

    E["G7C05"] = (
        "A direct digital synthesizer (DDS) produces a variable output frequency with the stability "
        "of a crystal oscillator. A DDS works by using a digital counter and lookup table to "
        "generate a sine wave sample-by-sample, clocked by a crystal oscillator reference. Since "
        "every output frequency is derived from the same crystal reference, they all share its "
        "stability. The frequency can be changed almost instantaneously by changing a digital "
        "value — no mechanical tuning or PLL lock time needed. DDS does NOT have a narrow tuning "
        "range (it can cover a wide range), doesn't produce high power (it's a signal source, not "
        "an amplifier), and the output isn't a perfectly pure sine wave (it has quantization "
        "artifacts that need filtering)."
    )

    E["G7C06"] = (
        "The key advantage of DSP (Digital Signal Processing) filters over analog filters is that "
        "a wide range of filter bandwidths and shapes can be created — all in software. An analog "
        "filter is fixed by its physical components: changing bandwidth means swapping crystals or "
        "adjusting LC networks. A DSP filter is just math — change the algorithm's parameters and "
        "you instantly have a different bandwidth, different shape factor, or even a completely "
        "different filter type (low-pass, band-pass, notch). Modern SDR transceivers exploit this "
        "to give operators continuously variable bandwidth — something that's impractical with "
        "analog filters. DSP doesn't reduce mixing products, isn't more effective at VHF, and "
        "doesn't use fewer components."
    )

    E["G7C07"] = (
        "Insertion loss specifies a filter's attenuation inside its passband — the amount of "
        "desired signal that's lost just by passing through the filter. An ideal filter would "
        "have zero insertion loss (no signal lost in the passband) and infinite rejection outside "
        "it. Real filters always lose something. Insertion loss of 1-2 dB is typical for a good "
        "crystal filter. Return loss measures reflected power (related to impedance matching). "
        "Q describes a component's or circuit's selectivity. Ultimate rejection is the maximum "
        "attenuation outside the passband. Know all four terms, but insertion loss is specifically "
        "about loss INSIDE the passband."
    )

    E["G7C08"] = (
        "All three factors — input amplifier gain, demodulator bandwidth, and input amplifier "
        "noise figure — affect receiver sensitivity. Sensitivity is about detecting weak signals, "
        "and weak signals must compete with noise. The noise figure tells you how much noise the "
        "amplifier adds (lower is better). The gain determines how much the signal gets boosted. "
        "The bandwidth determines how much noise enters the system (wider bandwidth = more noise). "
        "Together, these determine the minimum detectable signal (MDS). This is why narrowing "
        "your IF filter bandwidth improves sensitivity — you're reducing the noise that competes "
        "with the signal."
    )

    E["G7C09"] = (
        "The I and Q signals in SDR (Software-Defined Radio) are 90 degrees apart in phase. "
        "I stands for In-phase and Q stands for Quadrature (which literally means 'quarter turn' "
        "= 90°). By sampling the incoming RF at two points exactly 90° apart, the SDR captures "
        "complete information about both the amplitude and phase of the signal. This is critical "
        "because a single sample stream can't distinguish between positive and negative frequencies "
        "(images). The 90° I/Q pair eliminates this ambiguity. Without the quadrature relationship, "
        "SDR demodulation wouldn't work correctly."
    )

    E["G7C10"] = (
        "The advantage of I/Q modulation in SDRs is that all types of modulation can be created "
        "with appropriate processing. Because I/Q represents the signal completely — both amplitude "
        "and phase at every instant — you can mathematically construct any modulation scheme: AM, "
        "FM, SSB, PSK, QAM, or anything else. It's a universal modulation/demodulation framework. "
        "Change the software algorithm and you change the modulation type — no hardware changes "
        "needed. This is the fundamental power of SDR: the radio's capabilities are defined by "
        "software rather than fixed hardware. I/Q doesn't eliminate the need for ADCs (it requires "
        "them), doesn't reduce minimum signal level, and doesn't automatically convert digital to analog."
    )

    E["G7C11"] = (
        "In a software-defined radio, ALL of the listed functions — filtering, detection, and "
        "modulation — are performed by software. That's the entire point of SDR: replace dedicated "
        "hardware circuits with software algorithms running on a processor. Traditional radios use "
        "physical crystal filters, diode detectors, and balanced modulators. An SDR does the same "
        "jobs mathematically. The hardware is reduced to an antenna, an analog-to-digital converter "
        "(ADC), and a processor. Everything between the ADC and the speaker/display is software. "
        "This makes SDRs incredibly flexible — update the software and you've upgraded your radio."
    )

    E["G7C12"] = (
        "The cutoff frequency is the frequency above which a low-pass filter's output power drops "
        "below half the input power. This is also called the -3 dB point (from G5: a 3 dB loss = "
        "half power). Below the cutoff frequency, signals pass through with minimal loss. Above "
        "it, signals are increasingly attenuated. The cutoff frequency defines the boundary of the "
        "filter's passband. It's not the notch frequency (that's for a band-stop filter), not the "
        "neper frequency (a rarely-used attenuation unit), and rolloff describes the steepness of "
        "attenuation beyond cutoff, not the cutoff point itself."
    )

    E["G7C13"] = (
        "Ultimate rejection specifies a filter's maximum ability to reject signals outside its "
        "passband. It's the deepest attenuation the filter can achieve — the floor of the "
        "stopband. For example, a crystal filter might have 80 dB of ultimate rejection, meaning "
        "signals far from the passband are reduced by a factor of 100 million. Insertion loss is "
        "about loss INSIDE the passband (the opposite concept). Rolloff describes how quickly "
        "attenuation increases at the passband edges. Notch depth applies to notch (band-reject) "
        "filters specifically, not to the general stopband performance of any filter."
    )

    E["G7C14"] = (
        "A band-pass filter's bandwidth is measured between the upper and lower half-power points "
        "(-3 dB points). These are the frequencies where the output power drops to half the peak "
        "passband power. The bandwidth is simply the difference: BW = f_upper - f_lower. For "
        "example, if a filter passes signals from 9.000 MHz to 9.003 MHz at the half-power points, "
        "its bandwidth is 3 kHz — typical for an SSB crystal filter. This connects to the receiver "
        "sensitivity concept in G7C08: narrower bandwidth means less noise and better sensitivity "
        "for narrow-band signals."
    )

    # ── G8A — Modulation Types, Signals, and Overmodulation ──────

    E["G8A01"] = (
        "Direct binary FSK (Frequency Shift Keying) works by changing an oscillator's frequency "
        "directly with a digital control signal. When the digital input is a '1' (mark), the "
        "oscillator sits at one frequency; when it's a '0' (space), the oscillator shifts to a "
        "different frequency. The key word is 'direct' — the digital signal controls the oscillator "
        "without going through an audio tone stage first. This is simpler and more precise than "
        "generating an audio tone and feeding it into an FM modulator. It's not about sub-audible "
        "tones (that's CTCSS), not about computer interface protocols, and not about repurposing "
        "CW keying inputs."
    )

    E["G8A02"] = (
        "Phase modulation (PM) changes the phase angle of the RF carrier to convey information. "
        "While FM varies the frequency and AM varies the amplitude, PM shifts the carrier's phase "
        "— advancing or retarding it relative to its unmodulated position. Phase modulation and "
        "frequency modulation are closely related: varying the phase also affects the instantaneous "
        "frequency and vice versa. A reactance modulator connected to an RF amplifier stage "
        "actually produces phase modulation (see G8A04). The other answer choices — 'phase "
        "convolution,' 'phase transformation,' and 'phase inversion' — are not standard "
        "modulation terms."
    )

    E["G8A03"] = (
        "Frequency modulation (FM) changes the instantaneous frequency of the RF wave to convey "
        "information. When the modulating audio signal goes positive, the carrier frequency increases; "
        "when it goes negative, the carrier frequency decreases. The amount of frequency shift "
        "(deviation) is proportional to the audio amplitude, and the rate of shift follows the audio "
        "frequency. FM is widely used on VHF/UHF for voice because it's resistant to amplitude noise "
        "— since the information is in the frequency, not the amplitude, the receiver can clip off "
        "amplitude noise with a limiter stage. Don't confuse FM with frequency conversion (changing "
        "one frequency to another in a mixer) or frequency transformation (not a standard term)."
    )

    E["G8A04"] = (
        "A reactance modulator connected to a transmitter RF amplifier stage produces phase "
        "modulation. Here's why: a reactance modulator is a circuit that varies its apparent "
        "reactance (capacitive or inductive) in response to an audio signal. When you connect it "
        "to an RF amplifier stage (not the oscillator), it shifts the phase of the signal passing "
        "through that stage — the audio modulates the phase, not the frequency directly. If you "
        "connected the same reactance modulator to the oscillator instead, it would produce FM by "
        "pulling the oscillator frequency. The distinction matters: same circuit, different results "
        "depending on WHERE in the transmitter chain it's connected. From G7, recall that "
        "oscillator frequency is set by the LC tank — modulating the tank produces FM, modulating "
        "a downstream amplifier produces PM."
    )

    E["G8A05"] = (
        "Amplitude modulation (AM) varies the instantaneous power level of the RF signal. The "
        "carrier's amplitude — and therefore its power — changes in proportion to the modulating "
        "audio signal. When the audio goes positive, the carrier amplitude increases (more power); "
        "when the audio goes negative, the amplitude decreases (less power). This is fundamentally "
        "different from FM (which varies frequency at constant power) and PM (which varies phase "
        "at constant power). 'Power modulation' is not a real modulation type — it's a distractor."
    )

    E["G8A06"] = (
        "QPSK31 (Quadrature Phase Shift Keying at 31.25 baud) has all three listed characteristics: "
        "it IS sideband-sensitive (you must use the correct sideband — USB or LSB — for proper "
        "decoding), its encoding provides error correction (unlike BPSK31 which has no error "
        "correction), and its bandwidth is approximately the same as BPSK31 (about 31 Hz). QPSK31 "
        "achieves error correction by using the extra phase states — BPSK uses 2 phase states to "
        "send 1 bit per symbol, while QPSK uses 4 phase states to send 2 bits per symbol. One "
        "bit carries data, the other carries error correction information. The tradeoff: QPSK31 "
        "requires more precise phase tracking and is more sensitive to propagation distortion than "
        "BPSK31."
    )

    E["G8A07"] = (
        "Single sideband (SSB) uses the narrowest bandwidth of the listed phone emissions — "
        "typically about 2.4 kHz. SSB achieves this by transmitting only ONE sideband and "
        "suppressing both the carrier and the other sideband. Compare: conventional AM transmits "
        "carrier plus both sidebands (~6 kHz), vestigial sideband transmits one full sideband plus "
        "a portion of the other, and FM typically uses 10-16 kHz depending on deviation. SSB's "
        "narrow bandwidth is a huge advantage on crowded HF bands — more stations fit in the same "
        "spectrum space. It also concentrates all transmitter power into the information-carrying "
        "sideband rather than wasting most of it on a carrier."
    )

    E["G8A08"] = (
        "Overmodulation causes excessive bandwidth — the signal splashes beyond its normal "
        "frequency allocation and interferes with stations on adjacent frequencies. When you "
        "overdrive any modulator, the signal distorts, and distortion creates harmonics and "
        "spurious energy that spread the signal wider than it should be. In AM, overmodulation "
        "happens when the modulating signal tries to drive the carrier below zero (causing "
        "flat-topping or carrier pinch-off). In FM, excessive deviation spreads the signal "
        "beyond its allowed bandwidth. Either way, the result is the same: your signal gets "
        "wider and starts causing interference. This is why ALC (Automatic Level Control) and "
        "proper mic gain settings matter."
    )

    E["G8A09"] = (
        "FT8 uses 8-tone frequency shift keying (8-FSK). The '8' in FT8 stands for 8 tones — "
        "the mode uses 8 different audio frequencies to encode data, with each tone representing "
        "3 bits (2³ = 8 combinations). The tones are spaced 6.25 Hz apart, fitting the entire "
        "signal into about 50 Hz of bandwidth. FT8 was designed by Joe Taylor (K1JT) and Steve "
        "Franke (K9AN) for weak-signal communication — it can decode signals buried 20+ dB below "
        "the noise floor. It's NOT vestigial sideband (that's an analog TV technique), NOT "
        "compressed AM, and NOT spread spectrum. FT8 has revolutionized amateur radio by enabling "
        "contacts that would be impossible with voice modes."
    )

    E["G8A10"] = (
        "Flat-topping is signal distortion caused by excessive drive or speech levels in an AM or "
        "SSB transmitter. On an oscilloscope, the modulation envelope looks like it has flat tops "
        "instead of rounded peaks — the amplifier has run out of headroom and is clipping the "
        "waveform. This is a form of overmodulation that generates splatter (excessive bandwidth) "
        "and interference to nearby stations. Flat-topping is typically caused by too much mic gain, "
        "too much speech processor compression, or insufficient ALC action. It does NOT mean the "
        "ALC is properly adjusted (that would PREVENT flat-topping), and it's not about insufficient "
        "collector current or carrier suppression. Watch for flat-topping on your ALC meter and "
        "waterfall display."
    )

    E["G8A11"] = (
        "The modulation envelope of an AM signal is the waveform created by connecting the peak "
        "values of the modulated signal. Picture an AM signal on an oscilloscope: you see the RF "
        "carrier oscillating rapidly, but its amplitude rises and falls with the audio. If you "
        "draw a line connecting all the positive peaks and another connecting all the negative "
        "peaks, those lines trace out the modulation envelope — and that envelope IS the audio "
        "waveform. An AM demodulator (detector) works by extracting this envelope. The envelope "
        "is NOT the carrier frequency itself, NOT spurious signals, and NOT the bandwidth. It's "
        "the outline of the amplitude variations — the 'shape' of the modulated signal."
    )

    E["G8A12"] = (
        "QPSK (Quadrature Phase Shift Keying) transmits digital data using four phase states: "
        "0°, 90°, 180°, and 270°. Each phase state represents a pair of bits (00, 01, 10, 11), "
        "so QPSK sends 2 bits per symbol — twice the data rate of BPSK at the same symbol rate "
        "and bandwidth. The four phases are evenly spaced around a circle (360°/4 = 90° apart). "
        "From G8A06, remember that QPSK31 uses these extra bits for error correction rather than "
        "doubling throughput. The wrong answers are made-up terms — there's no 'quasi-parallel to "
        "serial conversion,' no 'quadra-pole sideband keying,' and no 'Fast Fourier Transform "
        "harmonic generation' scheme. QPSK is a real, well-defined digital modulation technique "
        "used across telecommunications."
    )

    E["G8A13"] = (
        "A link budget is the sum of transmit power and antenna gains minus system losses as seen "
        "at the receiver. It's an accounting exercise: start with your transmitter power (in dBm), "
        "add your transmitting antenna gain (in dBi), subtract all losses (feed line, free-space "
        "path loss, atmospheric absorption, polarization mismatch), and add the receiving antenna "
        "gain. The result tells you the signal power arriving at the receiver. If this number "
        "exceeds the receiver's minimum sensitivity, communication is possible. It's NOT about "
        "financial costs (despite the word 'budget'), and it includes more than just antenna gains "
        "minus losses — the transmit power is a critical starting term. Link budgets are essential "
        "for satellite work, EME (moonbounce), and microwave links."
    )

    E["G8A14"] = (
        "Link margin is the difference between the received power level and the minimum required "
        "signal level at the receiver's input. Think of it as your safety cushion: if your link "
        "budget shows -100 dBm arriving at the receiver and the receiver needs -120 dBm to decode, "
        "you have 20 dB of link margin. That margin accounts for fading, atmospheric variations, "
        "and other unpredictable losses. More margin = more reliable link. It's NOT the opposite "
        "of fade margin (they're related concepts, not opposites), NOT simply transmit power minus "
        "sensitivity (that ignores path loss and antenna gains), and NOT receiver sensitivity "
        "plus 3 dB. Link margin and link budget work together: the budget calculates received "
        "power, and the margin tells you how far above minimum you are."
    )

    # ── G8B — Mixing, Multiplication, Bandwidth, Intermodulation ────

    E["G8B01"] = (
        "The local oscillator (LO) is the mixer input that is varied or tuned to convert different "
        "incoming frequencies to the intermediate frequency (IF). From G7, recall that a "
        "superheterodyne receiver uses a mixer to combine the incoming RF signal with the LO to "
        "produce sum and difference frequencies. By tuning the LO, you select which incoming "
        "frequency gets converted to the fixed IF. The RF input carries the signal you want to "
        "receive, the image frequency is an unwanted signal (covered in G8B02), and the BFO "
        "(beat frequency oscillator) is used later in the receive chain for SSB/CW demodulation "
        "— not for frequency conversion in the mixer."
    )

    E["G8B02"] = (
        "Image response is interference from a signal at twice the IF frequency away from the "
        "desired signal. Here's the mechanism: a mixer produces both sum and difference frequencies. "
        "If your IF is 10 MHz and you're tuned to 14.2 MHz (LO at 24.2 MHz), both 14.2 MHz AND "
        "34.2 MHz will produce a 10 MHz difference with the LO. That 34.2 MHz signal is the "
        "'image' — it's exactly 2×IF (20 MHz) away from your desired frequency. The front-end "
        "bandpass filter is supposed to reject the image frequency, but if it leaks through, "
        "you hear the image signal mixed on top of your desired signal. Higher IF frequencies "
        "push the image further away, making it easier to filter — one reason modern receivers "
        "use high first-IF frequencies."
    )

    E["G8B03"] = (
        "Heterodyning is another term for mixing two RF signals. The word comes from Greek: "
        "'hetero' (different) + 'dyne' (force/power). When you combine two different frequencies "
        "in a non-linear device (mixer), you get sum and difference frequencies — that's "
        "heterodyning. The superheterodyne receiver is named for this process: 'super' (above "
        "audible) + 'heterodyne.' Heterodyning is the foundational principle of virtually every "
        "receiver design since the 1920s. Synthesizing means building up, frequency inversion "
        "means flipping a spectrum, and phase inversion means a 180° shift — none of these "
        "describe the mixing of two signals."
    )

    E["G8B04"] = (
        "A frequency multiplier generates a harmonic of a lower frequency signal to reach the "
        "desired operating frequency. In a VHF FM transmitter, it's often easier to generate "
        "a stable, well-modulated signal at a lower frequency and then multiply it up. A "
        "multiplier stage uses a non-linear amplifier (like Class C from G7) to deliberately "
        "generate harmonics, then a tuned output circuit selects the desired harmonic. For "
        "example, a 12 MHz oscillator multiplied by 12 produces 144 MHz for the 2-meter band. "
        "Frequency multiplication also multiplies the FM deviation by the same factor — this is "
        "how the small deviation at the oscillator becomes the full 5 kHz deviation at the output "
        "frequency (see G8B07). A mixer combines two different frequencies; a multiplier generates "
        "harmonics of one frequency."
    )

    E["G8B05"] = (
        "Odd-order intermodulation products are closest to the original signal frequencies — and "
        "that's what makes them so problematic. When two signals (F1 and F2) mix in a non-linear "
        "device, they produce intermodulation products at various combinations: 2F1-F2, 2F2-F1 "
        "(3rd order), 3F1-2F2, 3F2-2F1 (5th order), etc. These odd-order products fall NEAR the "
        "original frequencies, making them very difficult to filter out. Even-order products "
        "(F1+F2, F1-F2, 2F1, 2F2) land far from the originals and are easily filtered. This is "
        "why receiver specs emphasize odd-order intercept points (IP3, IP5) — those products are "
        "the ones that actually cause interference on adjacent channels. Second harmonics are a "
        "specific even-order product, and intercept point is a measurement parameter, not a "
        "type of product."
    )

    E["G8B06"] = (
        "Use Carson's Rule: bandwidth = 2 × (deviation + maximum modulating frequency) = "
        "2 × (5 kHz + 3 kHz) = 2 × 8 kHz = 16 kHz. Carson's Rule gives you the approximate "
        "bandwidth that contains about 98% of the FM signal's power. Note that it's NOT just "
        "twice the deviation (10 kHz) and NOT just twice the modulating frequency (6 kHz) — you "
        "need both terms added together, then doubled. The deviation determines how far the "
        "carrier swings, and the modulating frequency determines how fast it swings. Both "
        "contribute to the total bandwidth occupied."
    )

    E["G8B07"] = (
        "The oscillator deviation is 416.7 Hz. Here's the math: the transmitter uses frequency "
        "multiplication to get from 12.21 MHz to 146.52 MHz. The multiplication factor is "
        "146.52 / 12.21 = 12. Since frequency multiplication multiplies deviation by the same "
        "factor, the oscillator deviation must be the final deviation divided by the multiplication "
        "factor: 5000 Hz / 12 = 416.7 Hz. This is why FM transmitters using multiplier chains "
        "start with very small deviations at the oscillator — the multiplication process amplifies "
        "the deviation along with the frequency. If the oscillator had the full 5 kHz deviation, "
        "the output would have 60 kHz deviation (5 kHz × 12) — way too wide."
    )

    E["G8B08"] = (
        "Knowing the duty cycle of your operating mode matters because some modes have high duty "
        "cycles that could exceed the transmitter's average power rating. Duty cycle is the "
        "percentage of time your transmitter is actually producing RF output. CW has a low duty "
        "cycle — key down some, key up some. SSB voice varies. But digital modes like FT8, RTTY, "
        "and PSK31 can be 100% duty cycle — the transmitter is producing full output continuously "
        "during a transmission. A transmitter rated at 100W PEP for SSB might overheat at 100W "
        "continuous digital modes because its cooling system was designed for a lower average power. "
        "Many transceivers require you to reduce power for high-duty-cycle digital modes. This is "
        "a practical safety consideration, not about tuning, break-in, or overmodulation."
    )

    E["G8B09"] = (
        "Matching receiver bandwidth to the operating mode's bandwidth gives the best "
        "signal-to-noise ratio (SNR). From G7C08, recall that wider bandwidth admits more noise. "
        "If you're receiving a 200 Hz CW signal through a 2.4 kHz SSB filter, you're letting in "
        "12× more noise than necessary — every hertz of bandwidth beyond what the signal needs "
        "is just admitting more noise without adding more signal. But making the filter TOO narrow "
        "clips the signal edges. The sweet spot is matching: a 500 Hz filter for CW, 2.4 kHz for "
        "SSB, 200 Hz or less for PSK31. This isn't an FCC requirement, doesn't affect power "
        "consumption or antenna impedance — it's purely about optimizing the signal-to-noise ratio."
    )

    E["G8B10"] = (
        "Higher symbol rates require wider bandwidth. This is a fundamental principle of "
        "digital communications — you can't send symbols faster without using more spectrum. "
        "Each symbol transition occupies bandwidth; more transitions per second means more "
        "bandwidth. The Nyquist theorem sets the lower bound: the minimum bandwidth in Hz equals "
        "half the symbol rate in symbols/second. In practice, real filters and pulse shaping "
        "require somewhat more. This is the tradeoff in digital mode design: PSK31 uses a slow "
        "31.25 baud rate and fits in ~31 Hz, while high-speed modes like PACTOR IV need thousands "
        "of hertz. FT8 achieves its narrow bandwidth by using a very slow symbol rate (6.25 baud) "
        "with multiple tones."
    )

    E["G8B11"] = (
        "A mixer's output contains the sum and difference of the LO and RF input frequencies. "
        "This is the fundamental mixer equation: if you feed in F_RF and F_LO, you get F_RF + F_LO "
        "and F_RF − F_LO (or F_LO − F_RF) at the output. The desired frequency (usually the "
        "difference) becomes the IF, and the unwanted product (usually the sum) is filtered out. "
        "For example, 14.2 MHz RF + 24.2 MHz LO produces 38.4 MHz (sum) and 10.0 MHz (difference). "
        "The 10.0 MHz difference becomes your IF. The output is NOT the ratio, NOT the average, "
        "and NOT the arithmetic product (multiplication) — it's the sum AND difference, created by "
        "the non-linear mixing process."
    )

    E["G8B12"] = (
        "Intermodulation is the process where two signals combine in a non-linear circuit to "
        "produce unwanted spurious outputs. The key word is 'unwanted' — this distinguishes "
        "intermodulation from heterodyning (G8B03), which is intentional mixing. Intermodulation "
        "happens when strong signals overload an amplifier, mixer, or any non-linear element. "
        "The resulting spurious signals (intermodulation products or IMD) appear at various "
        "combinations of the input frequencies and can fall on top of weak desired signals, "
        "causing interference. From G8B05, recall that odd-order products are the most troublesome "
        "because they fall close to the original frequencies. Detection is extracting information "
        "from a modulated signal, and rolloff describes filter attenuation — neither produces "
        "spurious outputs."
    )

    E["G8B13"] = (
        "2F1 − F2 is a third-order intermodulation product — and the order is 3 because the "
        "coefficients add up to 3 (2 + 1 = 3). To determine the order: add the absolute values "
        "of all the frequency multipliers. For 2F1 − F2: |2| + |−1| = 3 (third order, odd). "
        "For 3F1 − F2: |3| + |−1| = 4 (fourth order, even — NOT odd). For 5F1 − 3F2: |5| + |−3| = 8 "
        "(eighth order, even — NOT odd). So among the choices, only 2F1 − F2 is actually odd-order. "
        "This is a tricky question because 'All these choices' sounds tempting, but you have to "
        "check the math for each one. Third-order products (2F1−F2 and 2F2−F1) are the strongest "
        "and closest to the original signals, making them the most important for receiver design."
    )

    # ── G8C — Digital Modes, Error Correction, Protocols ────────────

    E["G8C01"] = (
        "Amateurs share the 2.4 GHz band with unlicensed Wi-Fi services. The 2.4 GHz band "
        "(2400-2450 MHz) is allocated to both amateur radio (secondary) and industrial/scientific/medical "
        "(ISM) uses — which includes Wi-Fi (802.11b/g/n). This shared allocation means amateur "
        "microwave operations and mesh networking projects on 2.4 GHz must coexist with the "
        "massive amount of Wi-Fi traffic from every home router, smartphone, and IoT device. "
        "The 432 MHz, 902 MHz, and 10.7 GHz bands don't have Wi-Fi sharing. Amateur operators "
        "on 2.4 GHz sometimes repurpose commercial Wi-Fi hardware (like Ubiquiti or Mikrotik "
        "radios) for amateur mesh networking — which is legal since amateurs have privileges on "
        "the band."
    )

    E["G8C02"] = (
        "WSPR (Weak Signal Propagation Reporter, pronounced 'whisper') is the digital mode used "
        "as a low-power beacon for assessing HF propagation. WSPR stations transmit their callsign, "
        "grid locator, and power level (typically 1-5 watts) using a very narrow bandwidth signal "
        "(about 6 Hz). Receiving stations upload reception reports to a central database (wsprnet.org), "
        "creating a real-time map of propagation paths. WSPR can decode signals as weak as -28 dB "
        "SNR. It's specifically designed for propagation assessment — you set it and forget it. "
        "MFSK16 and PSK31 are keyboard-to-keyboard chat modes, not beacons. SSB-SC is a voice "
        "mode. WSPR is the go-to tool for understanding what bands are open and to where."
    )

    E["G8C03"] = (
        "The header of a packet radio frame contains the routing and handling information — "
        "source callsign, destination callsign, digipeater path, and protocol control fields. "
        "Think of it like the envelope of a letter: the header tells the network where the packet "
        "came from, where it's going, and how to handle it. The preamble is a synchronization "
        "sequence that lets the receiver lock onto the signal timing. The trailer marks the end "
        "of the frame and typically contains an error-checking checksum. 'Directory' is not a "
        "standard packet radio frame component. The header/preamble/data/trailer structure is "
        "common across most digital communication protocols."
    )

    E["G8C04"] = (
        "Baudot code is a 5-bit code with additional start and stop bits. Developed in 1870 by "
        "Émile Baudot, it's one of the oldest digital character encoding systems and is still used "
        "in amateur RTTY (Radio Teletype). With 5 bits, Baudot can represent 2⁵ = 32 characters "
        "per shift — but that's not enough for letters, numbers, and punctuation. So Baudot uses "
        "two shift states (LETTERS and FIGURES) to double the available characters to 64. The "
        "start and stop bits frame each character for asynchronous transmission. Baudot is NOT "
        "7-bit (that's ASCII), does NOT include error detection/correction (errors just produce "
        "garbled text), and has nothing to do with SELCAL or LISTEN. It's simple, old, and still "
        "works."
    )

    E["G8C05"] = (
        "In an ARQ (Automatic Repeat reQuest) mode, a NAK (Negative Acknowledgment) response "
        "means 'I received the packet but it contained errors — please retransmit.' ARQ is an "
        "error-correction protocol where the receiver checks each incoming packet (typically using "
        "a CRC checksum) and responds with either ACK (Acknowledgment — packet OK) or NAK "
        "(errors detected — send again). This back-and-forth continues until the packet gets "
        "through cleanly or too many attempts fail (see G8C06). NAK does NOT mean the packet was "
        "received without error (that's ACK), doesn't indicate a connection is established, and "
        "doesn't mean the entire file was received. ARQ modes include PACTOR, WINMOR, and ARDOP "
        "— all used in Winlink email systems."
    )

    E["G8C06"] = (
        "When an ARQ mode fails to exchange information after excessive transmission attempts, "
        "the connection is dropped. Every ARQ protocol has a retry limit — if a packet can't get "
        "through after a certain number of retransmission attempts (because the channel is too "
        "noisy, interference is too strong, or the other station has disappeared), the protocol "
        "gives up and disconnects. This prevents stations from endlessly retransmitting into the "
        "void and tying up the frequency. The checksum doesn't 'overflow' (it's a fixed-size "
        "value), packets aren't routed incorrectly (they just fail), and the encoding doesn't "
        "revert to a default set. The connection simply terminates, and you'd need to reinitiate "
        "it when conditions improve."
    )

    E["G8C07"] = (
        "FT8 can receive signals with very low signal-to-noise ratios — down to about -20 dB SNR "
        "in a 2.5 kHz bandwidth. This extraordinary weak-signal capability comes from its narrow "
        "bandwidth (~50 Hz), long integration time (12.64 seconds per transmission), and powerful "
        "forward error correction (LDPC coding). FT8 achieves this by trading speed for "
        "sensitivity — each transmission carries very little information (13 characters maximum), "
        "but it gets through when nothing else can. MSK144 is designed for meteor scatter (short "
        "bursts, not weak signals). AMTOR is an older ARQ mode without exceptional weak-signal "
        "capability. MFSK32 has decent performance but doesn't match FT8's ability to pull "
        "signals from the noise."
    )

    E["G8C08"] = (
        "In PSK31, upper case letters use longer Varicode bit sequences and thus slow down "
        "transmission. PSK31 uses Varicode encoding (see G8C12) where common characters get "
        "short bit sequences and rare characters get longer ones. Lower case 'e' is encoded "
        "as just 11 (2 bits), while upper case 'E' is 1110111 (7 bits) — more than 3× longer. "
        "This means typing in ALL CAPS literally slows your throughput. Upper case letters are "
        "NOT sent with more power (power is constant in PSK31). PSK31 does NOT use error "
        "correction — that's QPSK31 (see G8A06). And PSK31 is actually more power-efficient "
        "than RTTY, not less. The practical lesson: use lower case in PSK31 for faster throughput."
    )

    E["G8C09"] = (
        "The key characteristic of mesh network microwave nodes is redundancy: if one node fails, "
        "a packet may still reach its target station via an alternate node. That's the entire "
        "point of a mesh topology — multiple interconnected paths mean no single point of failure. "
        "Each node can route traffic through any available neighbor, and routing protocols "
        "automatically find alternate paths when one goes down. More nodes don't increase signal "
        "strength (each link has its own path loss). Links between nodes in a mesh DO typically "
        "use the same frequency and bandwidth (that's how they mesh). And more nodes don't reduce "
        "out-of-band interference. The resilience and self-healing nature of mesh is what makes "
        "it valuable for amateur emergency communications networks."
    )

    E["G8C10"] = (
        "Forward error correction (FEC) works by transmitting redundant information with the data. "
        "The transmitter adds extra bits (calculated from the original data using mathematical "
        "algorithms) that the receiver uses to detect AND correct errors — without needing "
        "retransmission. This is fundamentally different from ARQ (G8C05-06), which detects "
        "errors and requests retransmission. FEC trades bandwidth for reliability: you're sending "
        "more bits than the actual message requires, but the receiver can fix errors on its own. "
        "FEC does NOT control transmitter power, does NOT use Varicode (that's a character "
        "encoding), and is more sophisticated than simple parity bits. Modern FEC codes like LDPC "
        "(used in FT8) and turbo codes approach the theoretical limits of error correction. FEC "
        "is essential for one-way broadcasts and situations where retransmission isn't practical."
    )

    E["G8C11"] = (
        "The two frequencies of an FSK signal are called mark and space. These terms come from "
        "telegraphy: 'mark' was when the pen made a mark on the paper tape (current flowing), "
        "and 'space' was when it didn't (no current). In FSK, mark typically represents a binary "
        "1 and space represents binary 0, each at its own distinct frequency. For amateur RTTY, "
        "the standard shift between mark and space is 170 Hz. 'Dot and dash' refers to Morse "
        "code (CW), 'on and off' describes on-off keying (OOK), and 'high and low' is too "
        "generic. Mark and space are the specific, correct terms for FSK frequency identification. "
        "You'll see these terms in every RTTY and FSK-related discussion."
    )

    E["G8C12"] = (
        "PSK31 uses Varicode to encode characters. Varicode is a variable-length code where "
        "common characters (like 'e' and 't') get short bit sequences and uncommon characters "
        "(like 'Z' and uppercase letters) get longer ones — similar in concept to Morse code, "
        "where 'E' is a single dit. This makes PSK31 efficient for typical English text. "
        "Characters are separated by two or more consecutive zeros (00). Viterbi is a decoding "
        "algorithm for convolutional codes (error correction), not a character encoding. "
        "'Volumetric' is not a real coding term. And while all digital codes are ultimately "
        "binary, 'binary' doesn't describe the specific variable-length encoding scheme that "
        "makes PSK31 work. Varicode is the defining character set of PSK31."
    )

    E["G8C13"] = (
        "Vertical lines on either side of a data mode or RTTY signal on a waterfall display "
        "indicate overmodulation. These lines are spurious emissions — harmonics and "
        "intermodulation products created when the signal is driven too hard. A clean digital "
        "signal should appear as a narrow, well-defined trace on the waterfall. When overmodulated, "
        "the signal distorts and splatters energy into adjacent frequencies, showing up as "
        "additional vertical lines flanking the main signal. This is the digital equivalent of "
        "flat-topping in SSB (G8A10) — too much drive creates excessive bandwidth (G8A08). The "
        "fix is to reduce your audio drive level or transmitter power. These lines do NOT indicate "
        "propagation effects (long path or backscatter) or insufficient modulation — they "
        "specifically indicate excessive modulation."
    )

    E["G8C14"] = (
        "A waterfall display shows frequency on the horizontal axis, signal strength as intensity "
        "(brightness or color), and time on the vertical axis (scrolling downward). Imagine "
        "stacking spectrum snapshots on top of each other over time — each horizontal line is "
        "one moment's spectrum, and time flows downward like a waterfall. Stronger signals appear "
        "brighter or in different colors. This format lets you see signals, their bandwidth, and "
        "how they change over time simultaneously. It's invaluable for digital modes — you can "
        "visually identify mode types, spot interference, detect overmodulation (G8C13), and "
        "click on signals to tune to them. The three axes (frequency, intensity, time) and their "
        "orientations are the key to this question."
    )

    E["G8C15"] = (
        "An FT8 signal report of +3 means the signal-to-noise ratio is equivalent to +3 dB in "
        "a 2.5 kHz bandwidth. FT8 reports SNR rather than traditional S-meter readings because "
        "FT8 routinely works with signals far below the noise floor. The reference bandwidth of "
        "2.5 kHz was chosen because it's the approximate bandwidth of an SSB receiver — so "
        "the report tells you how the signal compares to the noise you'd hear in a normal SSB "
        "passband. A report of +3 means the signal is 3 dB above the noise floor in that "
        "bandwidth — audible but not strong. FT8 reports typically range from about -24 dB (barely "
        "decodable) to +20 dB or higher (very strong). The report is NOT in S-units, NOT relative "
        "to S9, and NOT a comparison to an SSB signal's strength."
    )

    E["G8C16"] = (
        "DMR (Digital Mobile Radio), D-STAR (Digital Smart Technologies for Amateur Radio), and "
        "System Fusion provide digital voice modes. These are the three major digital voice "
        "systems used in amateur radio, each using different vocoder technology to compress voice "
        "into a digital stream. DMR uses AMBE+2 codec, D-STAR uses AMBE codec, and System "
        "Fusion (Yaesu's system) uses either C4FM digital voice or conventional analog FM. "
        "WSPR, MFSK16, and EasyPAL are data/image modes, not voice. FT8, FT4, and FST4 are "
        "weak-signal data modes. Winlink, PACTOR II, and PACTOR III are email/data transfer "
        "protocols. Only DMR, D-STAR, and System Fusion are designed specifically to carry "
        "digitized voice over radio."
    )

    # ── G9A — Feed Lines, SWR, Impedance Matching ───────────────────

    E["G9A01"] = (
        "The characteristic impedance of a parallel conductor feed line (like ladder line or "
        "window line) is determined by the distance between the centers of the conductors and "
        "the radius of the conductors. The formula involves the ratio of spacing to conductor "
        "radius: Z₀ = 276 × log(D/r), where D is the center-to-center distance and r is the "
        "conductor radius. Wider spacing increases impedance; fatter conductors decrease it. "
        "Notice what's NOT in the formula: frequency and length. Characteristic impedance is a "
        "property of the line's geometry and the dielectric between conductors — it doesn't change "
        "with how long the line is or what frequency you're using. This is a fundamental concept "
        "from G5: impedance is about the ratio of voltage to current, and in a transmission line "
        "that ratio is set by physical dimensions."
    )

    E["G9A02"] = (
        "High SWR increases loss in a lossy transmission line. Here's the mechanism: when SWR is "
        "high, reflected power bounces back and forth between the antenna and transmitter. Each "
        "time the signal travels through the feed line, it loses some energy to the line's inherent "
        "attenuation. With high SWR, the signal makes multiple passes through the line (forward and "
        "reflected), so the total loss adds up. A perfect 1:1 SWR means the signal passes through "
        "the line once and is fully absorbed by the antenna — minimum loss. At 5:1 SWR, a significant "
        "portion of the power bounces back and forth, and each pass through the lossy line eats more "
        "energy. The key insight: SWR loss is proportional to BOTH the SWR ratio AND the line's "
        "matched-line loss. Low-loss line (like ladder line) can tolerate high SWR much better than "
        "lossy coax because there's less attenuation per pass."
    )

    E["G9A03"] = (
        "Window line (also called ladder line or open-wire line) has a nominal characteristic "
        "impedance of 450 ohms. The 'windows' are the rectangular cutouts in the plastic spacer "
        "between the two conductors — they reduce the amount of dielectric material, which lowers "
        "loss. At 450 ohms, window line has much higher impedance than coax (50 or 75 ohms), but "
        "it also has much lower loss. The tradeoff: you can't run it near metal objects, it's harder "
        "to route through walls, and it needs an antenna tuner to match to a 50-ohm radio. But for "
        "multiband wire antennas, window line's low loss makes it an excellent choice — especially "
        "when the SWR may be high on some bands (see G9A02 for why low-loss line handles high SWR "
        "better)."
    )

    E["G9A04"] = (
        "Reflected power at an antenna's feed point is caused by a difference between the feed line "
        "impedance and the antenna feed point impedance. This is the fundamental impedance mismatch "
        "concept from G5: when a traveling wave hits a boundary where impedance changes, some energy "
        "reflects back. If the feed line is 50 ohms and the antenna presents 50 ohms, all the power "
        "is absorbed — no reflection, SWR 1:1. If the antenna presents 200 ohms to a 50-ohm line, "
        "there's a mismatch, power reflects, and SWR rises (to 4:1 in this case — see G9A09). "
        "Operating at resonance minimizes this mismatch for a dipole, but resonance alone doesn't "
        "guarantee a match if the antenna's natural impedance differs from the line. The fix: "
        "impedance matching networks, antenna tuners, or choosing an antenna design with a feed "
        "point impedance close to the line impedance."
    )

    E["G9A05"] = (
        "Coaxial cable attenuation increases with frequency. This happens because of two mechanisms: "
        "conductor loss (skin effect forces RF current into a thinner surface layer at higher "
        "frequencies, increasing resistance) and dielectric loss (the insulating material between "
        "center conductor and shield absorbs more energy at higher frequencies). The increase follows "
        "roughly a square-root relationship — doubling the frequency increases loss by about 40%. "
        "This is why coax that works great on 80 meters may be unacceptably lossy on 2 meters. "
        "For example, RG-8 might lose 1 dB per 100 feet at 10 MHz but 3+ dB at 150 MHz. Always "
        "check your coax loss at the highest frequency you'll use, not the lowest. Feed line loss "
        "is expressed in dB per 100 feet (G9A06)."
    )

    E["G9A06"] = (
        "RF feed line loss is expressed in decibels per 100 feet. Decibels (from G5B) give you a "
        "logarithmic ratio that makes it easy to calculate total loss: if your coax loses 2 dB per "
        "100 feet and you have 50 feet, you lose about 1 dB. If you have 200 feet, you lose about "
        "4 dB. The 'per 100 feet' convention makes it easy to scale. Remember from G5B10 that each "
        "dB of loss costs you about 20% of your power — so 3 dB of feed line loss means half your "
        "transmitter power is heating your coax instead of radiating from your antenna. The unit is "
        "NOT ohms per anything (that would be resistance, not attenuation) — it's decibels, which "
        "express a power ratio."
    )

    E["G9A07"] = (
        "To prevent standing waves on a feed line, the antenna feed point impedance must be matched "
        "to the characteristic impedance of the feed line. Standing waves are created by reflected "
        "power — and reflected power comes from impedance mismatch (G9A04). When the impedances "
        "match perfectly, all power flows from the source to the load with no reflection, and the "
        "voltage and current are uniform along the line — no standing waves. The feed line length "
        "doesn't matter (neither odd quarter wavelengths nor even half wavelengths will fix a "
        "mismatch), and DC ground potential is irrelevant to RF impedance matching. The impedance "
        "match is what matters — everything else is a distractor."
    )

    E["G9A08"] = (
        "The SWR on the feed line remains 5:1 even if a matching network at the transmitter presents "
        "1:1 to the transmitter. This is a critical concept that trips people up: a matching network "
        "at the transmitter end (like an antenna tuner) transforms the impedance so the transmitter "
        "sees 50 ohms and is happy — but it does NOTHING to change the mismatch between the feed "
        "line and the antenna at the other end. The standing waves on the line are still there. The "
        "reflected power still bounces back and forth. The tuner just ensures the transmitter can "
        "deliver power into the system without folding back. This is why an antenna tuner doesn't "
        "reduce feed line loss from SWR (G9A02) — the line still carries reflected power. The only "
        "way to reduce SWR on the feed line is to fix the mismatch at the antenna end."
    )

    E["G9A09"] = (
        "SWR = Z_load / Z_line (when load > line) = 200/50 = 4:1. SWR is always expressed as a "
        "ratio greater than or equal to 1:1 — you always divide the larger impedance by the smaller "
        "one. It doesn't matter which is bigger; the mismatch is the same whether the load is 4× "
        "the line impedance or 1/4 of it. A 200-ohm load on a 50-ohm line gives 4:1. A 12.5-ohm "
        "load on a 50-ohm line also gives 4:1. SWR tells you HOW MUCH mismatch exists, not which "
        "direction. The '1:4' option would imply the SWR is less than 1:1, which isn't physically "
        "possible. Always put the bigger number first."
    )

    E["G9A10"] = (
        "SWR = Z_line / Z_load (when line > load) = 50/10 = 5:1. Same principle as G9A09 — divide "
        "the larger impedance by the smaller one. Here the 50-ohm line is higher than the 10-ohm "
        "load, so SWR = 50/10 = 5:1. Whether the load is too high or too low relative to the line, "
        "SWR just measures the ratio of mismatch. A 5:1 SWR means significant mismatch — most "
        "transmitters would reduce power or refuse to transmit at this SWR level. You'd need a "
        "matching network or antenna adjustment to bring this down to a usable level."
    )

    E["G9A11"] = (
        "Higher transmission line loss reduces the SWR measured at the input to the line. This "
        "sounds counterintuitive but makes sense: the SWR meter at the input sees both forward "
        "power (going to the antenna) and reflected power (coming back from the antenna). The "
        "reflected power has to travel all the way to the antenna AND all the way back — passing "
        "through the lossy line twice. By the time it gets back to the meter, it's been attenuated "
        "by twice the line loss. Less reflected power at the meter means lower apparent SWR. This "
        "is why a long run of lossy coax can 'hide' a bad SWR — the meter shows 2:1 while the "
        "actual SWR at the antenna is 10:1. The loss masks the problem. Extremely lossy line "
        "(like a dummy load) would show 1:1 SWR regardless of what's at the other end — because "
        "no reflected power survives the round trip. This is a trap, not a feature."
    )

    # ── G9B — Dipoles, Verticals, Radiation Patterns ────────────────

    E["G9B01"] = (
        "A random-wire antenna connected directly to the transmitter can cause station equipment "
        "to carry significant RF current. Without a proper ground plane or balanced feed system, "
        "the antenna uses whatever is available as the 'other half' — your radio chassis, power "
        "supply, mic cable, and even you. RF current flows on equipment cases, through audio "
        "cables, and across your operating desk, causing RFI (radio frequency interference), "
        "hot microphone shells, and erratic transceiver behavior. This is why antenna tuners "
        "and proper grounding are essential with random-wire antennas. The wire doesn't need to "
        "be any specific length, doesn't produce only vertical polarization, and isn't inherently "
        "better on lower bands. The defining characteristic is the RF-in-the-shack problem."
    )

    E["G9B02"] = (
        "Sloping the radials downward adjusts an elevated quarter-wave ground-plane vertical's "
        "feed point impedance to approximately 50 ohms. A quarter-wave vertical with horizontal "
        "radials has a feed point impedance of about 36 ohms — too low for a good match to 50-ohm "
        "coax. Angling the radials downward (typically 30-45°) increases the impedance by "
        "changing the geometry of the current distribution and the angle between the radiating "
        "element and the ground plane. Think of it as stretching the antenna's effective "
        "dimensions. Sloping radials upward would decrease the impedance further. Lengthening "
        "or coiling the radials changes their resonant frequency, not the feed point impedance "
        "in the way needed here. This drooping-radial trick is one of the simplest impedance "
        "matching techniques in antenna design."
    )

    E["G9B03"] = (
        "A quarter-wave ground-plane vertical antenna has an omnidirectional radiation pattern "
        "in azimuth — it radiates equally in all horizontal directions. This makes sense "
        "physically: a vertical antenna is symmetrical around its axis, so there's no preferred "
        "horizontal direction. The radiation pattern is shaped like a donut around the antenna, "
        "with maximum radiation at low elevation angles (good for DX) and a null straight up. "
        "It is NOT bi-directional (that's a dipole in free space), NOT isotropic (an isotropic "
        "antenna is a theoretical point source radiating equally in ALL directions including up "
        "and down), and NOT hemispherical. Omnidirectional means equal in all horizontal "
        "directions — but the elevation pattern is NOT uniform."
    )

    E["G9B04"] = (
        "A dipole's radiation pattern in free space, in the plane containing the conductor, is a "
        "figure-eight at right angles to the antenna. Maximum radiation is broadside — perpendicular "
        "to the wire. Minimum radiation (nulls) are off the ends of the wire. This figure-eight "
        "pattern is one of the most fundamental concepts in antenna theory. The key phrase in the "
        "question is 'in a plane containing the conductor' — this is asking for the H-plane (or "
        "azimuthal) pattern. Looking down at a dipole oriented north-south, you'd see maximum "
        "radiation east and west, nulls north and south. In three dimensions, the free-space dipole "
        "pattern looks like a donut around the wire. It is NOT a circle (that would mean equal "
        "radiation off the ends, which doesn't happen), and it doesn't have asymmetric lobes."
    )

    E["G9B05"] = (
        "When a horizontal dipole is less than 1/2 wavelength above ground, the azimuthal radiation "
        "pattern at high elevation angles (above about 45°) becomes almost omnidirectional. At low "
        "heights, ground reflections fill in the nulls off the ends of the dipole. The figure-eight "
        "pattern that exists in free space gets blurred by ground interactions until the antenna "
        "radiates nearly equally in all horizontal directions — at high angles. This is actually "
        "useful for NVIS (Near Vertical Incidence Skywave, G9D01) communication where you want "
        "high-angle radiation for short-skip contacts within a few hundred miles. The pattern "
        "doesn't become unpredictable (it follows well-understood physics), height definitely "
        "affects it, and the end-fire nulls don't vanish completely at all angles — they fill in "
        "specifically at higher elevation angles."
    )

    E["G9B06"] = (
        "The radials of a ground-mounted vertical antenna should be placed on the surface of the "
        "ground or buried a few inches below it. Ground-mounted radials serve as the antenna's "
        "ground plane, providing a low-loss return path for RF currents. They work best when "
        "they're at or just below the surface — close enough to interact with the ground's "
        "conduction currents. Unlike elevated radials (where a few work well), ground-mounted "
        "radial systems benefit from quantity — 32 to 120 radials, each about 1/4 wavelength "
        "long, create an effective ground screen. They should NOT be elevated high (that changes "
        "the antenna type), NOT parallel to the vertical element (useless orientation), and NOT "
        "at the center of the antenna (they radiate outward from the base). Bury them just under "
        "the lawn and forget about them."
    )

    E["G9B07"] = (
        "The feed point impedance of a horizontal half-wave dipole steadily decreases as the "
        "antenna height is reduced to 1/10 wavelength above ground. In free space, a half-wave "
        "dipole has about 73 ohms feed point impedance. As you lower it toward the ground, ground "
        "reflections change the current distribution on the antenna, and the impedance drops. "
        "At 1/4 wavelength height, it's around 50-60 ohms (convenient for coax!). Below that, it "
        "keeps dropping — at 1/10 wavelength, it can be as low as 15-20 ohms. This happens because "
        "the antenna's image in the ground (from reflection) couples to the real antenna and "
        "modifies its impedance. The closer to ground, the stronger the coupling, the lower the "
        "impedance. This is one reason very low dipoles are harder to match to 50-ohm coax."
    )

    E["G9B08"] = (
        "The feed point impedance of a half-wave dipole steadily increases as the feed point moves "
        "from the center toward the ends. At the center, impedance is about 73 ohms (in free "
        "space). At the ends, the impedance approaches several thousand ohms. This is because "
        "current is maximum at the center and decreases toward the ends, while voltage is minimum "
        "at the center and increases toward the ends. Since impedance = voltage/current (from G5), "
        "moving the feed point toward the ends means more voltage and less current — higher "
        "impedance. This principle is used in off-center-fed dipoles (like the Windom antenna) to "
        "achieve specific impedance values for matching purposes. An end-fed half-wave antenna "
        "(G9D02) has very high impedance because you're feeding at the voltage maximum."
    )

    E["G9B09"] = (
        "Horizontally polarized HF antennas have lower ground losses compared to vertically "
        "polarized antennas. A vertical antenna requires current flow in the ground (or radial "
        "system) to complete the circuit — and real ground has significant resistance, which "
        "dissipates power as heat. A horizontal antenna's currents are in the wire above ground, "
        "and while it uses ground reflections, the ground currents are less intense and less "
        "critical. This means a horizontal dipole strung up in the trees can be very efficient "
        "even without a ground system, while a vertical antenna without a good radial system can "
        "lose 50% or more of its power to ground losses. The practical takeaway: if you can't "
        "install a proper radial system, a horizontal antenna may be more efficient."
    )

    E["G9B10"] = (
        "For a half-wave dipole at 14.250 MHz: length (feet) = 468 / frequency (MHz) = 468 / 14.250 "
        "= 32.8 ≈ 33 feet. The formula 468/f gives the approximate length of a half-wave dipole in "
        "feet. The 468 constant accounts for the velocity factor of a wire in free space (the wave "
        "travels slightly slower on a wire than in free space, making the antenna about 5% shorter "
        "than a true half wavelength). 14.250 MHz is in the middle of the 20-meter band — the "
        "workhorse DX band (G3A07). A 33-foot dipole is a manageable size for most backyards, "
        "which is one reason 20 meters is so popular for new General class operators."
    )

    E["G9B11"] = (
        "For a half-wave dipole at 3.550 MHz: length (feet) = 468 / 3.550 = 131.8 ≈ 132 feet. "
        "Same formula as G9B10, but at 80 meters the antenna is MUCH longer. 132 feet of wire is a "
        "serious span — you need a big yard or creative installation to fit an 80-meter dipole. "
        "This is why the lower HF bands are sometimes called 'real estate bands' — the antennas "
        "are physically large. Many operators use inverted-V configurations (G9D12) or shortened "
        "(loaded) antennas when space is limited. Compare the 33-foot 20m dipole to this 132-foot "
        "80m dipole — four times the frequency means four times shorter."
    )

    E["G9B12"] = (
        "For a quarter-wave monopole at 28.5 MHz: length (feet) = 234 / frequency (MHz) = 234 / 28.5 "
        "= 8.2 ≈ 8 feet. The formula 234/f gives the approximate quarter-wave length in feet — it's "
        "exactly half of the 468/f dipole formula because a quarter wave is half of a half wave. "
        "28.5 MHz is in the 10-meter band, so an 8-foot vertical for 10 meters is very manageable — "
        "it could even be a mobile whip antenna. Compare this to an 80-meter quarter-wave vertical "
        "which would be about 66 feet tall (234/3.55). Frequency and physical size are inversely "
        "proportional — higher frequency means smaller antennas."
    )

    # ── G9C — Yagi Antennas, Gain, and Matching ─────────────────────

    E["G9C01"] = (
        "Larger-diameter elements increase the bandwidth of a Yagi antenna. Thicker elements have "
        "a lower Q (quality factor), which from G5 means a broader resonance curve — the antenna's "
        "impedance and pattern change more slowly across frequency. Think of a thin wire resonator "
        "as a sharp tuning fork (narrow bandwidth, high Q) and a fat tube resonator as a dull thud "
        "(wide bandwidth, low Q). This is why commercial Yagi antennas use aluminum tubing rather "
        "than wire for elements. Closer element spacing actually narrows bandwidth. Loading coils "
        "add narrowband resonances. Tapered-diameter elements (thinner at the tips) are used to "
        "reduce weight and wind load, not specifically to increase bandwidth."
    )

    E["G9C02"] = (
        "The driven element of a Yagi antenna is approximately 1/2 wavelength long. The driven "
        "element is essentially a dipole — it's the element connected to the feed line, and it "
        "resonates at approximately a half wavelength, just like any center-fed dipole. The "
        "reflector behind it is slightly longer than 1/2 wavelength (about 5% longer), and the "
        "director(s) in front are slightly shorter (about 5% shorter). But the driven element "
        "itself is close to 1/2 wavelength — the same dipole antenna you'd calculate using 468/f "
        "(from G9B10-11). It's not 1/4 wavelength (that's a vertical monopole), not 3/4 wavelength "
        "(that's a different, less common antenna type), and not a full wavelength."
    )

    E["G9C03"] = (
        "In a three-element Yagi, the reflector is longer and the director is shorter than the "
        "driven element. The mnemonic: reflectors are 'fat and lazy' (longer, behind the action) "
        "and directors are 'lean and eager' (shorter, pointing toward the target). The reflector is "
        "about 5% longer than the driven element and sits behind it. The director is about 5% "
        "shorter and sits in front. This length relationship is what creates the Yagi's directional "
        "pattern — the reflector acts like a mirror behind the driven element, and the director acts "
        "like a lens focusing energy forward. If you reverse the lengths, you reverse the "
        "direction of maximum radiation. The lengths are NOT all the same, and they don't depend "
        "on operating frequency in terms of their relative proportions."
    )

    E["G9C04"] = (
        "Gain expressed in dBi is 2.15 dB higher than the same gain expressed in dBd. The 'd' in "
        "dBd means 'relative to a dipole' and the 'i' in dBi means 'relative to an isotropic "
        "(theoretical point source) radiator.' A dipole already has 2.15 dBi of gain over an "
        "isotropic source, so any antenna measured against the dipole reference starts 2.15 dB "
        "lower. Example: a Yagi with 7 dBd gain is 9.15 dBi gain — it's the same antenna, just "
        "measured against a different reference. Watch for this in antenna advertisements: "
        "manufacturers sometimes quote gain in dBi to make numbers look bigger. When comparing "
        "antennas, make sure you're using the same reference. Always add 2.15 to convert dBd to "
        "dBi, or subtract 2.15 to go from dBi to dBd."
    )

    E["G9C05"] = (
        "Increasing boom length and adding directors to a Yagi antenna increases gain. More directors "
        "mean more elements focusing RF energy forward into a narrower beam — like adding more lenses "
        "to a telescope. A longer boom spaces these elements further apart, allowing more efficient "
        "interaction between them. Each additional director typically adds less gain than the "
        "previous one (diminishing returns), but a long-boom Yagi with many directors can achieve "
        "impressive gain — 10-15+ dBd for VHF/UHF designs. Beamwidth actually DECREASES (narrows), "
        "not increases, because the energy is more concentrated. Front-to-back ratio generally "
        "improves (increases), not decreases. And the resonant frequency is set by element lengths, "
        "not boom length — adding directors doesn't lower it."
    )

    E["G9C07"] = (
        "Front-to-back ratio is the power radiated in the major (forward) lobe compared to the "
        "power radiated in the opposite direction. It's expressed in dB. A Yagi with 20 dB "
        "front-to-back ratio radiates 100 times more power forward than backward. This is "
        "important for two reasons: it concentrates your signal toward the target (gain), and it "
        "reduces interference from behind you (quieter receive). Front-to-back ratio is NOT about "
        "the number of directors vs. reflectors (that describes element count), NOT about element "
        "positioning relative to the driven element (that's the physical layout), and NOT the "
        "ratio of forward gain to dipole gain (that's just gain in dBd). It's specifically about "
        "forward-to-backward power comparison."
    )

    E["G9C08"] = (
        "The main lobe of a directive antenna is the direction of maximum radiated field strength "
        "from the antenna. It's the primary beam — where most of the antenna's energy goes. For a "
        "Yagi, the main lobe points from the reflector through the directors (forward). The main "
        "lobe is NOT a voltage or current maximum on the elements (that's a standing wave concept "
        "from G9A, not a radiation pattern concept), and it's NOT the maximum vertical angle (the "
        "main lobe can be at any elevation angle depending on antenna design and height). When "
        "someone says 'point your beam at Europe,' they mean aim the main lobe toward Europe."
    )

    E["G9C09"] = (
        "Two Yagis stacked vertically 1/2 wavelength apart produce approximately 3 dB more gain "
        "than a single Yagi. From G5B01, doubling power equals +3 dB. Two identical antennas "
        "properly phased and fed equally each contribute their full gain, and the combined aperture "
        "is twice as large — effectively doubling the power density in the main lobe direction. "
        "The 3 dB rule applies whenever you double the effective antenna aperture. It's not 1.5 dB "
        "(that would be for improperly phased or spaced arrays), not 6 dB (you'd need four antennas "
        "for that — double the doubling), and not 9 dB (that would require eight antennas). Each "
        "doubling of antenna count adds about 3 dB, assuming proper phasing and spacing."
    )

    E["G9C10"] = (
        "ALL of the listed factors — physical boom length, number of elements, and element spacing — "
        "can be adjusted to optimize a Yagi's forward gain, front-to-back ratio, or SWR bandwidth. "
        "Yagi design is a complex optimization problem where all these parameters interact. Longer "
        "boom → more gain but harder to manage mechanically. More elements → more gain but with "
        "diminishing returns. Spacing affects the coupling between elements, which determines the "
        "balance between gain, front-to-back ratio, and impedance bandwidth. Professional Yagi "
        "designers use computer modeling to find the best combination for their goals. You can't "
        "optimize one parameter without affecting the others — it's always a set of tradeoffs."
    )

    E["G9C11"] = (
        "A beta match (also called a hairpin match) is a shorted transmission line stub placed at "
        "the feed point of a Yagi antenna to provide impedance matching. A Yagi's driven element "
        "typically has a lower impedance than 50 ohms (often 20-30 ohms) due to the mutual coupling "
        "from nearby parasitic elements. The hairpin match is a short piece of transmission line "
        "(bent into a U or 'hairpin' shape) that acts as a shunt inductor. When combined with the "
        "slightly capacitive reactance of a shortened driven element, this inductor provides an "
        "impedance transformation to 50 ohms. It's a simple, elegant solution — just a piece of "
        "wire bent into a U, no separate components needed. It's NOT a quarter-wave coax section "
        "(that's a different matching technique) and NOT a series capacitor."
    )

    E["G9C12"] = (
        "A gamma match allows the driven element to remain electrically connected to (not insulated "
        "from) the boom. This is a significant practical advantage because it simplifies mechanical "
        "construction — the element can be clamped directly to the boom without insulating hardware. "
        "The gamma match uses a parallel rod alongside the driven element, connected at one end to "
        "the element and at the other to the feed line through a series capacitor. It works by "
        "tapping the element off-center (similar in concept to moving the feed point of a dipole, "
        "as in G9B08) to find a point where the impedance matches the feed line. The gamma match "
        "DOES require components (a capacitor for tuning), so it's NOT component-free. And it's "
        "designed for single-band use, NOT multiband matching."
    )

    # ── G9D — Specialized Antennas ──────────────────────────────────

    E["G9D01"] = (
        "A horizontal dipole placed between 1/10 and 1/4 wavelength above ground is most effective "
        "for NVIS (Near Vertical Incidence Skywave) on 40 meters. NVIS works by launching signals "
        "nearly straight up, where they reflect off the F layer and come back down within a few "
        "hundred miles — filling the gap between ground wave and long-distance skip (see G3C10). "
        "A LOW horizontal antenna radiates most of its energy at high angles (nearly straight up), "
        "which is exactly what NVIS needs. At 1/10 to 1/4 wavelength height on 40 meters, that's "
        "roughly 4-10 meters (13-33 feet) above ground. A vertical antenna is wrong for NVIS "
        "because verticals radiate at LOW angles (good for DX, terrible for NVIS). A dipole at "
        "1/2 wavelength height also has too much low-angle radiation. Keep it low and horizontal "
        "for NVIS."
    )

    E["G9D02"] = (
        "An end-fed half-wave antenna has very high feed point impedance — typically several thousand "
        "ohms. From G9B08, we know that impedance increases as you move the feed point from the "
        "center toward the end of a dipole. At the very end, you're feeding at the voltage maximum "
        "and current minimum — that's the definition of high impedance (Z = V/I from G5). This "
        "is why end-fed half-wave (EFHW) antennas always need a matching transformer (typically a "
        "49:1 or 64:1 ratio) to bring the impedance down to 50 ohms for the feed line. The high "
        "impedance is NOT 'approximately 50 ohms' and NOT 'approximately 300 ohms' — it's "
        "thousands of ohms. An EFHW is basically a center-fed dipole where you've slid the feed "
        "point all the way to one end."
    )

    E["G9D03"] = (
        "A VHF/UHF halo antenna radiates omnidirectionally in the plane of the halo. A halo is "
        "essentially a dipole bent into a circular loop (not a full loop — the ends don't touch), "
        "mounted horizontally. Because it's a bent dipole, it maintains horizontal polarization, "
        "but bending it into a circle makes the radiation pattern omnidirectional in the horizontal "
        "plane — unlike a straight dipole's figure-eight pattern (G9B04). This makes halos useful "
        "for horizontally polarized omnidirectional coverage on VHF/UHF, where satellite and SSB "
        "work uses horizontal polarization. The radiation is NOT broadside to the halo plane "
        "(that would be like a full loop), NOT only opposite the feed point, and NOT only on "
        "the feed point side."
    )

    E["G9D04"] = (
        "Antenna traps enable multiband operation. A trap is a parallel LC circuit inserted into "
        "an antenna element at a specific point. At the trap's resonant frequency, it presents "
        "very high impedance — effectively cutting the antenna at that point, making it shorter "
        "for that frequency. At frequencies below resonance, the trap acts as a loading coil, "
        "electrically lengthening the antenna. This allows a single antenna to work on multiple "
        "bands: for example, a trapped dipole might be 33 feet for 20 meters (traps isolating "
        "the outer sections) and use the full length with loading for 40 meters. Traps don't "
        "notch out spurious frequencies (that's a filter's job), don't provide balanced impedance, "
        "and don't prevent out-of-band operation — they enable multi-frequency resonance."
    )

    E["G9D05"] = (
        "Vertically stacking horizontally polarized Yagi antennas narrows the main lobe in elevation. "
        "When you stack antennas vertically, you're increasing the antenna array's vertical aperture. "
        "A larger vertical aperture produces a narrower elevation beam — the same physics that makes "
        "a longer Yagi have a narrower azimuthal beam (G9C05). Narrowing the elevation pattern "
        "concentrates more energy at lower takeoff angles, which is ideal for DX on HF or for "
        "reducing QRM from high-angle signals. The azimuthal pattern stays roughly the same (the "
        "horizontal aperture hasn't changed). Stacking does NOT allow polarization switching (both "
        "antennas are the same polarization), doesn't provide simultaneous V and H polarization, "
        "and doesn't narrow the azimuthal pattern — it specifically narrows elevation."
    )

    E["G9D06"] = (
        "The primary advantage of a log-periodic antenna is wide bandwidth. A log-periodic dipole "
        "array (LPDA) can cover a frequency range of 2:1 or more — for example, 14-30 MHz in a "
        "single antenna. It achieves this because at any given frequency, only a portion of the "
        "array's elements are active (those close to resonance at that frequency). As you change "
        "frequency, a different set of elements becomes active. The tradeoff: a log-periodic has "
        "LESS gain per element than a Yagi because many of its elements are not contributing at "
        "any given frequency. It doesn't suppress harmonics, doesn't provide polarization diversity, "
        "and it has lower gain than a comparable-sized Yagi on any single frequency. But if you "
        "need one antenna to cover many bands, a log-periodic is hard to beat."
    )

    E["G9D07"] = (
        "A log-periodic antenna has element lengths and spacing that vary logarithmically along the "
        "boom. Each successive element is longer than the previous one by a constant ratio (called "
        "tau, τ), and the spacing between elements also increases by the same ratio. This "
        "logarithmic progression is what gives the antenna its name and its wideband characteristic "
        "— the structure is self-similar at different scales, so it behaves similarly across a wide "
        "frequency range. The impedance does NOT vary periodically (it stays relatively constant — "
        "that's the whole point), gain does NOT vary logarithmically with frequency (it stays "
        "roughly constant), and SWR doesn't vary periodically with boom length. The defining "
        "feature is the logarithmic scaling of physical dimensions."
    )

    E["G9D08"] = (
        "A 'screwdriver' mobile antenna adjusts its feed point impedance by varying the base loading "
        "inductance. The name comes from the motorized mechanism that adjusts the inductance — a "
        "motor (originally operated by an electric screwdriver) moves a contact along a coil, "
        "changing how much inductance is in the circuit. More inductance = lower resonant frequency "
        "(tunes to lower bands). Less inductance = higher resonant frequency (tunes to higher "
        "bands). The coil is at the base of the antenna, making it a base-loaded vertical. It "
        "doesn't vary body capacitance (that's not adjustable), doesn't extend/retract the whip "
        "(though some designs combine both), and a capacitance hat is a fixed top-loading device, "
        "not the primary tuning mechanism. The variable inductor is the screwdriver antenna's "
        "defining feature."
    )

    E["G9D09"] = (
        "A Beverage antenna is primarily used for directional receiving on the MF and low HF bands. "
        "It's a very long wire (typically 1-8 wavelengths) suspended low over the ground, terminated "
        "with a resistor at the far end. The Beverage works as a traveling-wave antenna — it "
        "absorbs signals arriving from the terminated end and receives signals from the unterminated "
        "end, giving it a directional pattern. It's an excellent receive antenna because its long "
        "length provides gain and directivity on the lower bands where noise is the limiting factor. "
        "However, it's a poor transmitting antenna because most of the power is absorbed by the "
        "termination resistor and ground losses. It's NOT for directional transmitting, and NOT "
        "for direction finding (loop antennas are used for DF — see G9D10). Beverage antennas "
        "are favorites among low-band DXers who have the acreage."
    )

    E["G9D10"] = (
        "An electrically small loop (less than 1/10 wavelength in circumference) has nulls broadside "
        "to the loop — meaning signals arriving perpendicular to the plane of the loop are rejected. "
        "Maximum reception is in the plane of the loop (off the edges). This is the opposite of a "
        "full-wavelength loop, where maximum radiation IS broadside. The small loop's pattern is "
        "similar to a dipole's figure-eight (G9B04), but rotated: where a dipole has nulls off its "
        "ends, a small loop has nulls perpendicular to its face. These sharp nulls make small loops "
        "excellent for direction finding — rotate the loop until the signal disappears (you've found "
        "the null, and the signal source is perpendicular to the loop plane). Small loops are NOT "
        "omnidirectional — their directional properties are their most useful feature."
    )

    E["G9D11"] = (
        "Multiband antennas have poor harmonic rejection. Because a multiband antenna is designed to "
        "resonate on multiple frequencies, it naturally resonates on harmonics too. A single-band "
        "antenna for 40 meters might present a high SWR on 20 meters (the second harmonic), naturally "
        "suppressing harmonic radiation. But a multiband antenna designed for both 40m AND 20m will "
        "happily radiate on both — including any harmonic energy from your transmitter. This means "
        "you're more reliant on your transmitter's low-pass filtering to suppress harmonics. "
        "Multiband antennas don't necessarily present low impedance on all frequencies (impedance "
        "varies), don't require an antenna tuner (they're designed to match without one), and don't "
        "require open-wire feed line (most use coax). Their downside is specifically harmonic "
        "radiation."
    )

    E["G9D12"] = (
        "A dipole with a single central support is called an inverted V. Instead of being supported "
        "at both ends with a horizontal run between them, an inverted-V dipole hangs from a single "
        "center point (the apex), with the wire sloping downward on both sides — forming a V shape "
        "when viewed from the side (inverted because the point is up). This is one of the most "
        "popular amateur antennas because it needs only one support — a single mast, tree, or "
        "flagpole at the center. The legs droop at 30-45° angles. The radiation pattern is similar "
        "to a flat dipole but slightly more omnidirectional (the drooping fills in the nulls "
        "somewhat, similar to the low-height effect in G9B05). An inverted L is a different "
        "antenna (vertical section plus horizontal), a sloper is a single tilted wire, and a "
        "Lazy H is a stacked pair of horizontal dipoles."
    )

    # fmt: on


RULE_CITATION_RE = re.compile(r"^\[[^\]]+\]\s*")


def build_fallback_explanation(q: dict) -> str:
    """Generate a safe explanation that always matches the current question."""
    answer = q["answers"][q["correct"]]
    question = RULE_CITATION_RE.sub("", q["question"]).strip()
    q_lower = question.lower()

    if answer == "All these choices are correct":
        return f"All of the listed choices are correct for this question."

    if q["group"].startswith("G5B"):
        return f"This is a power or decibel calculation question. Work through the math and you get {answer}."

    if q["group"].startswith(("G5C",)) and any(ch.isdigit() for ch in question):
        return f"Apply the appropriate circuit formula and you get {answer}."

    if q_lower.startswith(("what is ", "what are ")):
        return f"The correct answer is {answer}."

    if q_lower.startswith(("what does ", "which term", "what term")):
        return f"{answer} is the correct term or definition for this question."

    if q_lower.startswith(("which of the following", "which frequency", "which band", "what type")):
        return f"The correct choice here is {answer}."

    if q_lower.startswith(("where ", "when ", "how ", "why ")):
        return f"The correct answer is {answer}."

    return f"The correct answer is {q['correct']}) {answer}."


def validate_explanations(questions: list[dict]) -> None:
    """Fail fast if the explanation map drifts from the question pool."""
    question_ids = {q["id"] for q in questions}
    explanation_ids = set(EXPLANATIONS)
    missing = sorted(question_ids - explanation_ids)
    orphaned = sorted(explanation_ids - question_ids)

    if missing or orphaned:
        issues = []
        if missing:
            issues.append(f"missing explanation keys: {', '.join(missing)}")
        if orphaned:
            issues.append(f"orphan explanation keys: {', '.join(orphaned)}")
        raise SystemExit("; ".join(issues))


def load_pool() -> dict:
    """Load the 2023-2027 pool JSON."""
    with open(POOL_PATH) as f:
        return json.load(f)


def group_questions(questions: list[dict]) -> dict[str, dict[str, list[dict]]]:
    """Group questions by subelement and then by group.

    Returns: {subelement: {group: [question, ...]}}
    """
    result: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for q in questions:
        result[q["subelement"]][q["group"]].append(q)
    return result


def format_question(q: dict) -> str:
    """Format a single question as markdown."""
    lines = [f"### {q['id']}"]
    # Strip rule citations from question text for cleaner display
    question_text = RULE_CITATION_RE.sub("", q["question"]).strip()
    lines.append(f"**{question_text}**")

    for letter in ("A", "B", "C", "D"):
        text = q["answers"].get(letter, "")
        if not text:
            continue
        if letter == q["correct"]:
            lines.append(f"- **{letter}) {text}** ✅")
        else:
            lines.append(f"- {letter}) {text}")

    explanation = EXPLANATIONS.get(q["id"], "")
    if not explanation:
        explanation = build_fallback_explanation(q)
    lines.append("")
    lines.append(f"> {explanation}")

    return "\n".join(lines)


def generate_subelement_file(
    subelement: str,
    name: str,
    exam_questions: int,
    pool_size: int,
    groups: dict[str, list[dict]],
) -> str:
    """Generate the full markdown file for one subelement."""
    lines = [f"# {subelement} — {name}"]
    lines.append(f"*{exam_questions} questions on the exam from a pool of {pool_size}*")
    lines.append("")

    for group_id in sorted(groups.keys()):
        desc = GROUP_DESCRIPTIONS.get(group_id, group_id)
        lines.append(f"## Group {group_id} — {desc}")
        lines.append("")

        for q in groups[group_id]:
            lines.append(format_question(q))
            lines.append("")

    return "\n".join(lines)


def main() -> None:
    _load_explanations()
    pool = load_pool()

    # Only validate explanations for subelements that have been written
    all_questions = pool["questions"]
    written_subelements = {qid[:2] for qid in EXPLANATIONS}
    if written_subelements:
        questions_to_validate = [q for q in all_questions if q["subelement"] in written_subelements]
        validate_explanations(questions_to_validate)

    subelements_meta = pool["subelements"]
    grouped = group_questions(all_questions)

    OUTPUT_DIR.mkdir(exist_ok=True)

    generated = 0
    for sub_id, groups in sorted(grouped.items()):
        meta = subelements_meta.get(sub_id, {})
        name = meta.get("name", sub_id)
        exam_qs = meta.get("exam_questions", 0)
        pool_size = meta.get("pool_size", sum(len(qs) for qs in groups.values()))

        file_stem = SUBELEMENT_FILES.get(sub_id)
        if not file_stem:
            print(f"WARNING: No file mapping for subelement {sub_id}", file=sys.stderr)
            continue

        # Only generate question files for subelements with explanations written
        if sub_id not in written_subelements and written_subelements:
            print(f"  ⏭ {sub_id} — no explanations yet, skipping")
            continue

        content = generate_subelement_file(sub_id, name, exam_qs, pool_size, groups)
        out_path = OUTPUT_DIR / f"{file_stem}-questions.md"
        out_path.write_text(content)
        print(f"  ✓ {out_path.name} ({pool_size} questions)")
        generated += 1

    print(f"\nDone — {generated} subelement file(s) generated.")


if __name__ == "__main__":
    main()
