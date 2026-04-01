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
