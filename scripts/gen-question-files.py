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
