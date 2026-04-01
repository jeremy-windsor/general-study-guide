# G9 — Antennas and Feed Lines

This is where the rubber meets the road — or rather, where the RF meets the air. Everything you've learned about impedance (G5), circuits (G7), and signals (G8) converges at the antenna system. You'll see 4 questions from a pool of 46 on your exam, covering feed lines, SWR, dipoles, verticals, Yagis, and specialized antennas. This is one of the larger subelements, and for good reason: antennas are the most important part of any station. A $5,000 radio connected to a mediocre antenna will be outperformed by a $500 radio connected to a great one.

The good news: antenna theory is physical and intuitive. You can see antennas, measure them with a tape measure, and build them from hardware store wire. The math is minimal — mostly 468/f and some SWR ratios. The concepts connect directly to what you already know from G5 (impedance, reactance, matching) and G3 (propagation, takeoff angles, NVIS).

---

## Feed Lines: Getting Power to the Antenna

Before we talk about antennas themselves, we need to talk about the pipe that carries RF from your radio to the antenna. A feed line's job is simple: deliver power from the transmitter to the antenna with minimum loss. But the details matter enormously.

### Characteristic Impedance

Every feed line has a **characteristic impedance** (Z₀) — the ratio of voltage to current for a wave traveling along the line. From G5, you know impedance is measured in ohms. For coaxial cable, the characteristic impedance is determined by the ratio of the inner conductor diameter to the outer shield diameter, plus the dielectric material between them. Most amateur coax is either **50 ohms** (standard for transmitting) or **75 ohms** (used for receive-only applications and cable TV).

For **parallel conductor feed lines** (like ladder line or window line), the characteristic impedance depends on the **distance between the centers of the conductors** and the **radius of the conductors**. The formula is Z₀ = 276 × log(D/r). Notice what's NOT in that formula: frequency and length. Characteristic impedance is a property of the line's physical geometry — it doesn't change whether you have 10 feet or 100 feet of line, and it doesn't change from 3.5 MHz to 28 MHz.

**Window line** (also called ladder line) has a characteristic impedance of about **450 ohms**. Those rectangular "windows" cut into the plastic spacer reduce dielectric material and lower loss. Window line is much lossier-looking on paper (450 ohms vs. 50 ohms), but it actually has *much lower loss* than coax — and that matters more than you'd think.

### Attenuation and Frequency

Coaxial cable attenuation **increases with frequency**. Two mechanisms drive this:

1. **Skin effect** — at higher frequencies, RF current crowds into a thinner surface layer of the conductor, increasing effective resistance
2. **Dielectric loss** — the insulating material between center conductor and shield absorbs more energy at higher frequencies

The loss increase follows roughly a square-root relationship — double the frequency and loss goes up about 40%. This is why you need to check your coax specifications at the *highest* frequency you'll use, not the lowest. RG-8 that loses 1 dB per 100 feet at 10 MHz might lose 3+ dB at 150 MHz.

Feed line loss is expressed in **decibels per 100 feet** — not ohms, not per 1,000 feet. The dB unit makes scaling easy: 50 feet of cable that loses 2 dB per 100 feet loses about 1 dB. And from G5B, remember that each dB of loss costs about 20% of your power. Three dB of feed line loss means half your transmitter power is heating coax instead of radiating.

### SWR: When Impedances Don't Match

SWR (Standing Wave Ratio) is the most discussed number in amateur radio, and it all comes down to **impedance mismatch**. When a wave traveling down a feed line hits the antenna and finds a different impedance, some power reflects back. That reflected power creates standing waves — fixed patterns of voltage and current maxima and minima along the line.

**What causes reflected power?** A difference between the feed line impedance and the antenna feed point impedance. If they match (50-ohm line to 50-ohm antenna), SWR is 1:1 — no reflection, all power absorbed. If they differ, SWR rises.

**Calculating SWR** is straightforward: divide the larger impedance by the smaller one.

- 50-ohm line to 200-ohm load: SWR = 200/50 = **4:1**
- 50-ohm line to 10-ohm load: SWR = 50/10 = **5:1**

SWR is always ≥ 1:1. It doesn't matter whether the load is higher or lower than the line — the mismatch is symmetric.

**To prevent standing waves**, you must match the antenna feed point impedance to the characteristic impedance of the feed line. Line length doesn't fix a mismatch. DC grounding doesn't fix it. Only impedance matching fixes it.

### The Antenna Tuner Trap

Here's a concept that trips up many people: **an antenna tuner at the transmitter does NOT reduce SWR on the feed line**. If your antenna presents 5:1 SWR to the feed line and you put a tuner at the transmitter end, the tuner transforms the impedance so the *transmitter* sees 50 ohms and is happy. But the feed line still has 5:1 SWR. The reflected power still bounces back and forth. The tuner just prevents the transmitter from folding back its power.

This matters because **high SWR increases loss in a lossy feed line**. Each time reflected power travels through the line, it loses energy. With high SWR, the signal makes multiple passes, and the total loss compounds. This is why **low-loss feed line can tolerate high SWR** much better than lossy coax — if your line only loses 0.1 dB per pass (like ladder line), even multiple passes add up to very little. But if your coax loses 2 dB per pass, the round trips get expensive fast.

### The SWR Masking Effect

Here's a subtle but important point: **higher transmission line loss reduces the SWR measured at the input to the line**. The reflected power has to travel the full length of the line *twice* (to the antenna and back), getting attenuated both ways. By the time it reaches your SWR meter at the transmitter, it's much weaker — making the SWR look better than it really is. A long run of lossy coax can "hide" a terrible antenna mismatch. Your meter reads 2:1 while the actual SWR at the antenna is 10:1. This is a trap, not a feature.

> **Exam tip:** Memorize the SWR calculation (bigger impedance ÷ smaller impedance), know that tuners don't fix feed line SWR, and remember that lossy line masks real SWR readings.

---

## Dipoles and Verticals: The Foundation Antennas

### The Half-Wave Dipole

The half-wave dipole is the reference antenna of amateur radio. It's simple — two wires, each about a quarter wavelength long, fed at the center. The formula for the total length in feet is:

**Length (feet) = 468 / frequency (MHz)**

This gives you physical numbers you can work with:
- **20 meters (14.250 MHz):** 468 / 14.25 = **33 feet** — manageable for most backyards
- **80 meters (3.550 MHz):** 468 / 3.55 = **132 feet** — you need a big yard or creative installation

The 468 constant (rather than the theoretical 492 for a half wavelength in free space) accounts for the velocity factor of the wire — electromagnetic waves travel slightly slower along a conductor than in free space, making the antenna about 5% shorter than a theoretical half wavelength.

#### Dipole Radiation Pattern

In free space, a dipole's radiation pattern in the plane of the wire is a **figure-eight at right angles to the antenna**. Maximum radiation is broadside (perpendicular to the wire). Nulls are off the ends. This is the classic dipole pattern you'll see drawn everywhere.

But **height above ground changes things**. When a horizontal dipole is less than 1/2 wavelength high, the azimuthal pattern at high elevation angles becomes **almost omnidirectional**. Ground reflections fill in the end-fire nulls. This is relevant for NVIS operation (more on that later) where a low dipole radiates upward nearly equally in all directions.

#### Feed Point Impedance

A center-fed half-wave dipole in free space has about **73 ohms** feed point impedance. But this changes with height and feed point location:

- **Lower height → lower impedance.** As you bring a dipole closer to ground, the feed point impedance steadily decreases. At 1/4 wavelength height, it's around 50-60 ohms (conveniently close to 50-ohm coax). At 1/10 wavelength, it can drop to 15-20 ohms. The ground's image of the antenna couples to the real antenna and reduces impedance.

- **Off-center feed → higher impedance.** Moving the feed point from center toward the ends steadily increases impedance. At the center: ~73 ohms. Near the end: several thousand ohms. This is because current is maximum at the center (low impedance = lots of current for a given voltage) and minimum at the ends (high impedance = lots of voltage for a given current). This principle explains why **end-fed half-wave antennas have very high impedance** — they need a matching transformer (49:1 or 64:1).

#### Horizontal vs. Vertical Polarization

Horizontally polarized antennas have **lower ground losses** than verticals. A vertical requires current flow in the ground (or radial system) to complete the circuit, and real ground has resistance that wastes power as heat. A horizontal dipole's currents stay in the wire above ground. The practical takeaway: if you can't install a good radial system, a horizontal antenna may be more efficient.

### The Inverted V

A dipole with a **single central support** is called an **inverted V**. Instead of needing two tall supports, the wire hangs from one center point with the legs sloping downward at 30-45° angles. It's one of the most popular amateur antennas because it needs only one mast, tree, or flagpole. The radiation pattern is similar to a flat dipole but slightly more omnidirectional — the drooping legs fill in the nulls, similar to the low-height effect.

Don't confuse it with:
- **Inverted L** — a vertical section plus a horizontal section (different antenna entirely)
- **Sloper** — a single tilted wire
- **Lazy H** — a stacked pair of horizontal dipoles

### The Quarter-Wave Vertical

The quarter-wave monopole is the other fundamental antenna. Its length formula is:

**Length (feet) = 234 / frequency (MHz)**

That's exactly half the dipole formula (because a quarter wave is half of a half wave). At **28.5 MHz (10 meters)**, a quarter-wave vertical is about **8 feet** — perfect for mobile or a small backyard installation.

A vertical's radiation pattern is **omnidirectional in azimuth** — equal in all horizontal directions. This makes it ideal for general coverage (you don't need to point it), but it has no directional gain. Its main advantage for HF is low-angle radiation, which is good for DX.

#### Radials: The Other Half

A vertical antenna needs a ground plane. For **ground-mounted verticals**, radials should be placed **on the surface or buried a few inches below ground**. More radials are better — 32 to 120, each about 1/4 wavelength long. They form a ground screen that provides a low-loss return path for RF currents.

For **elevated quarter-wave ground-plane verticals** (mounted above ground), only 3-4 radials are needed. With horizontal radials, the feed point impedance is about 36 ohms — too low for 50-ohm coax. **Sloping the radials downward** (30-45°) raises the impedance to approximately **50 ohms**. This drooping-radial trick is one of the simplest impedance matching techniques.

### Random-Wire Antennas

A random-wire antenna connected directly to a transmitter has a characteristic problem: **station equipment may carry significant RF current**. Without a balanced feed or proper ground system, the antenna uses your radio chassis, power supply, mic cable, and even your body as the "other half" of the antenna. This causes RFI, hot mic shells, and erratic transceiver behavior. Random wires need antenna tuners and proper grounding to manage this.

---

## Yagi Antennas: Directional Gain

The Yagi-Uda antenna is the go-to directional antenna for HF and VHF/UHF. It consists of a driven element (the one connected to the feed line) plus one or more parasitic elements that shape the radiation pattern.

### Element Sizes and Roles

The driven element is approximately **1/2 wavelength** long — it's basically a dipole. The parasitic elements create the directional pattern:

- **Reflector** — slightly **longer** than the driven element (about 5% longer), mounted **behind** it
- **Director(s)** — slightly **shorter** than the driven element (about 5% shorter), mounted **in front**

A useful mnemonic: reflectors are "fat and lazy" (longer, behind), directors are "lean and eager" (shorter, in front). In a three-element Yagi, the reflector is longest, the driven element is middle, and the director is shortest.

### Gain, Bandwidth, and the Boom

**Adding directors and increasing boom length increases gain.** Each additional director focuses the beam further, like adding lenses to a telescope. However, there are diminishing returns — each new director adds less gain than the previous one. A long-boom Yagi with many directors can achieve 10-15+ dBd on VHF/UHF.

**Larger-diameter elements increase bandwidth.** Thicker elements have lower Q (from G5, lower Q = broader resonance), so the antenna's performance stays consistent across a wider frequency range. This is why commercial Yagis use aluminum tubing, not wire.

**ALL of these factors** — boom length, number of elements, and element spacing — can be adjusted to optimize gain, front-to-back ratio, and SWR bandwidth. Yagi design is always a tradeoff between these parameters.

### Understanding Gain Numbers

Antenna gain is expressed in either **dBd** (relative to a dipole) or **dBi** (relative to an isotropic radiator). A dipole has 2.15 dBi of gain, so:

**dBi = dBd + 2.15**

A Yagi advertised at 9.15 dBi has the same gain as one advertised at 7 dBd — same antenna, different reference. Always check which reference is being used when comparing antennas. Manufacturers sometimes use dBi to make numbers look bigger.

### Radiation Pattern Concepts

- **Main lobe** — the direction of maximum radiated field strength. When you "point your beam at Europe," you're aiming the main lobe.
- **Front-to-back ratio** — the power in the main lobe compared to the power radiated in the opposite direction, in dB. A 20 dB front-to-back means 100× more power forward than backward.

### Stacking Yagis

Two identical Yagis stacked vertically 1/2 wavelength apart produce approximately **3 dB more gain** than a single Yagi. From G5B, doubling power = +3 dB. Two antennas properly phased double the effective aperture. The stacking specifically **narrows the main lobe in elevation** — concentrating energy at lower takeoff angles (good for DX). The azimuthal pattern stays roughly the same.

### Matching the Yagi

Yagi driven elements typically have lower impedance than 50 ohms (often 20-30 ohms) due to mutual coupling from the parasitic elements. Two common matching methods:

- **Beta (hairpin) match** — a shorted transmission line stub at the feed point that acts as a shunt inductor, transforming impedance to 50 ohms. Simple and elegant — just a piece of wire bent into a U shape.
- **Gamma match** — a parallel rod alongside the driven element with a series capacitor. Its key advantage: the driven element does NOT need to be insulated from the boom, simplifying mechanical construction. However, it requires a tuning capacitor and is a single-band solution.

> **Exam tip:** Know the three element lengths (reflector longest, director shortest), the dBi vs. dBd relationship (+2.15), and the 3 dB gain from stacking. These are the most commonly tested Yagi concepts.

---

## Specialized Antennas

### NVIS Antennas

Near Vertical Incidence Skywave (NVIS) fills the gap between ground wave and long-distance skip — covering 0-300 miles by bouncing signals off the F layer at near-vertical angles (see G3C10). The ideal NVIS antenna for 40 meters during the day is a **horizontal dipole placed between 1/10 and 1/4 wavelength above ground**. On 40 meters, that's roughly 13-33 feet.

Why low and horizontal? A low horizontal antenna radiates most of its energy at high angles (nearly straight up) — exactly what NVIS needs. A vertical antenna is wrong for NVIS because verticals radiate at low angles. A dipole at 1/2 wavelength height also has too much low-angle radiation. Keep it low and horizontal.

### Log-Periodic Antennas

A log-periodic dipole array (LPDA) has one killer advantage: **wide bandwidth**. It can cover a 2:1 frequency range (or more) in a single antenna — for example, 14-30 MHz. Element lengths and spacing **vary logarithmically along the boom**, giving the antenna its name.

At any given frequency, only a subset of elements is active (those near resonance). Change frequency and a different group becomes active. The tradeoff: **less gain per element than a Yagi** because many elements aren't contributing at any given frequency. But if you need one antenna to cover many bands, a log-periodic is hard to beat.

### Antenna Traps

Traps are parallel LC circuits inserted into antenna elements to **enable multiband operation**. At the trap's resonant frequency, it presents high impedance — effectively cutting the antenna shorter for that band. Below resonance, the trap acts as a loading coil, electrically lengthening the antenna. A trapped dipole might work 20 meters with a 33-foot active section and use the full wire length for 40 meters.

The downside of multiband antennas: **poor harmonic rejection**. Because they're designed to work on multiple bands (including harmonics), they'll happily radiate harmonic energy from your transmitter. You're more reliant on your transmitter's filtering.

### Loop Antennas

An **electrically small loop** (less than 1/10 wavelength circumference) has nulls **broadside to the loop** — perpendicular to its plane. Maximum reception is in the plane of the loop (off the edges). This is the opposite of a full-wavelength loop. The sharp nulls make small loops excellent for direction finding — rotate until the signal disappears, and the source is perpendicular to the loop plane.

### The Beverage Antenna

A Beverage antenna is used for **directional receiving on MF and low HF bands**. It's a very long wire (1-8 wavelengths), suspended low over ground, terminated with a resistor at the far end. It's a traveling-wave antenna with good directivity — but a poor transmitting antenna because most power goes into the termination resistor and ground losses. Beverage antennas are favorites among low-band DXers with lots of acreage.

### The Halo Antenna

A VHF/UHF halo is a dipole bent into a circle, mounted horizontally. It provides **omnidirectional radiation in the plane of the halo** with horizontal polarization — combining the omnidirectional coverage of a vertical with the horizontal polarization needed for SSB and satellite work.

### Mobile Antennas

A **"screwdriver" mobile antenna** adjusts its feed point impedance by **varying the base loading inductance**. A motor moves a contact along a coil — more inductance tunes lower, less inductance tunes higher. The name comes from the electric screwdriver motor originally used. The variable inductor is its defining feature.

### End-Fed Half-Wave (EFHW)

The end-fed half-wave has **very high feed point impedance** — several thousand ohms. This follows directly from G9B08: impedance increases as you move the feed point toward the end. You're feeding at the voltage maximum and current minimum. EFHW antennas always need a matching transformer (49:1 or 64:1) to work with 50-ohm coax. They're popular because only one support is needed and no radials are required.

---

## Key Formulas and Numbers

| Formula | Use | Example |
|---------|-----|---------|
| **468 / f(MHz)** | Half-wave dipole length in feet | 468/14.25 = 33 ft (20m) |
| **234 / f(MHz)** | Quarter-wave vertical length in feet | 234/28.5 = 8 ft (10m) |
| **SWR = Z_big / Z_small** | Calculate SWR from impedance mismatch | 200/50 = 4:1 |
| **dBi = dBd + 2.15** | Convert between gain references | 7 dBd = 9.15 dBi |

## Quick Reference: Key Numbers

- **Window line impedance:** 450 ohms
- **Free-space dipole impedance:** ~73 ohms
- **Dipole at 1/4λ height:** ~50-60 ohms
- **Elevated vertical with horizontal radials:** ~36 ohms
- **End-fed half-wave impedance:** very high (thousands of ohms)
- **Stacking gain:** +3 dB per doubling of antennas
- **Coax loss units:** dB per 100 feet

> **Test strategy:** G9 gives you 4 exam questions from 46 in the pool. The most frequently tested concepts are SWR calculations, dipole length formulas, Yagi element relationships, and feed point impedance behavior. Master the formulas and the impedance concepts, and this section becomes easy points.
