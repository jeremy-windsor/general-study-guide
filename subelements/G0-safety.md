# G0 — Electrical and RF Safety

You learned the basics in Technician: RF energy can be hazardous, towers are dangerous, and electricity kills. The General exam goes deeper — particularly on the regulatory side of RF exposure (MPE limits, time averaging, OET Bulletin 65) and on the practical electrical safety that comes with building a more serious station.

This is the final subelement on the exam, and you'll see 2 questions from a pool of 25. Don't let the low question count fool you — this material can save your life or keep you out of trouble with the FCC.

---

## RF Exposure: The Physics

Let's start with the fundamental question: **how does RF energy affect the human body?**

The answer is heating. That's it. RF energy is **non-ionizing radiation** — unlike X-rays or gamma rays, it doesn't have enough energy per photon to break molecular bonds or damage DNA directly. What it does is cause water molecules and other polar molecules in tissue to oscillate, generating heat through friction. It's the same mechanism as a microwave oven, just (hopefully) at much lower power levels.

This is an important distinction: RF doesn't cause "radiation poisoning" (that's nuclear radiation), doesn't affect blood counts (also nuclear), and obviously doesn't cool tissue. The biological effect is thermal — and all the safety regulations are designed to limit the amount of heating your body experiences.

Some body parts are more vulnerable than others. The **eyes and testes** are particularly susceptible because they have limited blood flow to carry heat away. Your brain is well-protected by blood flow, but your corneas aren't so lucky. This is why you never look directly into an active microwave feed horn.

> **From Technician:** You learned that RF energy is non-ionizing and can cause heating. The General exam expects you to understand *why* this matters for station compliance — which takes us to the FCC's RF exposure rules.

---

## FCC RF Exposure Rules

The FCC requires every amateur station with **time-averaged transmissions above one milliwatt** to comply with RF exposure regulations. That's virtually every station — even a QRP rig running 5 watts is 5,000 times above the threshold. Don't let anyone tell you amateurs are exempt — they're not.

### Three Things That Determine Exposure

When evaluating RF exposure from your station, three factors matter:

1. **Power density** — how much RF energy hits a given area (measured in mW/cm²)
2. **Frequency** — the body absorbs RF differently at different frequencies (worst in the 30-300 MHz range)
3. **Duty cycle** — how much of the time your transmitter is actually producing RF

All three matter. You can't just check one.

### Maximum Permissible Exposure (MPE)

The FCC sets MPE limits — the maximum RF power density a person can safely be exposed to. These limits vary by frequency because the body's absorption varies:

- **Below 30 MHz:** MPE limits are relatively generous because the body doesn't efficiently absorb these longer wavelengths
- **30-300 MHz:** Strictest limits — body dimensions (height, arm length) happen to match these wavelengths, maximizing absorption
- **Above 300 MHz:** Limits gradually relax again, but stay significant through the microwave bands

The FCC defines two tiers:
- **Controlled environment** (the operator, aware of the RF): higher exposure allowed, 30-minute time averaging
- **Uncontrolled environment** (neighbors, passersby): stricter limits, 6-minute time averaging

### Time Averaging

Time averaging is a key concept that comes up repeatedly. It means the **total RF exposure averaged over a specific period** — not a 24-hour average, not the cumulative lifetime dose, but the rolling average over the defined evaluation period.

Why does this matter? Because amateur transmissions are intermittent. You transmit, then listen, then transmit again. If you're transmitting 50% of the time, your time-averaged exposure is half the peak value. This means:

- **CW** at 40-50% duty cycle allows more peak power than FM at 100%
- **SSB voice** at 20-40% duty cycle allows even more
- **FM and RTTY** at or near 100% duty cycle get the least favorable treatment

The effect of duty cycle on RF exposure is that **a lower duty cycle permits greater power levels to be transmitted**. Less time on the air = less average energy = you can run more power during the time you are on.

### Performing an RF Exposure Evaluation

If your station doesn't meet the exemption criteria (and at 1 milliwatt, almost nobody qualifies for exemption), you must **perform an RF Exposure Evaluation in accordance with FCC OET Bulletin 65**.

OET Bulletin 65 is the FCC's official guidance document. Remember the name — it comes up on the exam. You have three valid methods to demonstrate compliance:

1. **Calculation based on OET Bulletin 65** — use the formulas and tables
2. **Computer modeling** — software tools (like the ARRL's online calculator) that do the math for you
3. **Measurement with calibrated equipment** — a calibrated field strength meter with a calibrated antenna

Most amateurs use the calculation method because calibrated measurement equipment is expensive. But any of these approaches is acceptable — the FCC doesn't mandate one specific method.

### What To Do When You Exceed Limits

If your evaluation shows that RF exposure exceeds permissible limits, you must **take action to prevent human exposure to the excessive RF fields**. Possible actions include:

- Reduce power
- Raise the antenna (more distance = less power density)
- Change antenna type or direction
- Restrict access to high-exposure areas (fencing, signage)
- Change to a lower duty-cycle mode
- Relocate the antenna away from occupied areas

There's no form to file, no special FCC permission needed. Just fix the problem.

### Indoor Antennas

Indoor transmitting antennas deserve special attention. An indoor antenna puts the radiating element very close to people — possibly in the same room. Distance is your best friend in RF safety (power density drops with the square of distance), and an indoor antenna eliminates most of that protective distance. HF waves pass right through walls and floors, so don't count on the structure for shielding.

The precaution is straightforward: **make sure that MPE limits are not exceeded in occupied areas**. Don't locate the antenna close to your operating position (that maximizes YOUR exposure), and don't kid yourself that positioning it against a wall helps — RF goes through drywall like it's not there.

### Directional Antennas and Neighbors

If your evaluation shows a neighbor might experience excessive exposure from your directional antenna's main lobe, **take precautions to ensure the antenna cannot be pointed in their direction when they are present**. A directional antenna concentrates energy — the main lobe is where the power is. Point it somewhere else and the problem disappears.

---

## Electrical Safety

The second half of G0 shifts from RF energy to the kind of electricity that comes out of your wall outlet — the kind that kills about 400 Americans every year.

### Wiring and Circuit Protection

A 240 VAC circuit has four conductors: two hots, one neutral, and one ground. **Only the hot wires** get fuses or circuit breakers. Never fuse the neutral (if the neutral fuse blows while the hots are still connected, the circuit looks dead but isn't — extremely dangerous). Never fuse the ground (it's the safety path for fault current).

Wire size must match the circuit breaker rating. The NEC specifies:

| Breaker Rating | Minimum Wire Size |
|---------------|------------------|
| 15 amps | AWG 14 |
| 20 amps | AWG 12 |
| 30 amps | AWG 10 |

Remember: **lower AWG numbers = thicker wire = higher current capacity**. If the wire is too thin for the breaker, the wire overheats before the breaker trips — that's a fire waiting to happen.

### Ground Fault Circuit Interrupters (GFCIs)

A GFCI monitors the difference between current on the hot wire and current on the neutral. In normal operation, these are equal — every electron that flows out on the hot wire returns on the neutral. But if current is leaking to ground through an unintended path (like through a person being electrocuted), the hot and neutral currents won't match, and the GFCI trips — typically in about 5 milliseconds, fast enough to prevent a fatal shock.

**Current flowing from hot to neutral is normal operation** — that won't trip a GFCI. The trigger is **current flowing from hot to ground** — bypassing the neutral return path.

### The National Electrical Code (NEC)

The NEC covers the **electrical safety of the station** — wiring, grounding, circuit protection, installation practices. It does NOT cover bandwidth limits, modulation limits, or RF exposure limits (those are FCC territory). The NEC is published by the National Fire Protection Association (NFPA) and adopted by local jurisdictions as the building electrical code. When you wire your ham shack, the NEC governs how you do it.

---

## Lightning Protection

Lightning is one of the most destructive forces your station will face. A single stroke carries tens of thousands of amps, and the electromagnetic pulse can destroy equipment even without a direct hit.

### Ground Rods and Location

The station's lightning protection ground system should be located **outside the building**. You want lightning current to reach ground by the shortest possible path WITHOUT passing through your building. Ground rods, bonding conductors, and the connection point for feed line grounds all belong outside.

### Bonding Is Everything

Lightning protection ground rods **must be bonded together with all other grounds** — electrical service ground, station RF ground, cable TV ground, telephone ground. If separate ground systems aren't bonded, a lightning strike can create enormous voltage differences between them, driving destructive currents through your equipment (which provides the path between the unconnected grounds). Bond everything together with heavy copper conductors so all grounds rise and fall together during a lightning event.

### Lightning Arrestors

Lightning arrestors should be located **where the feed lines enter the building**. This is the boundary between "expendable" and "expensive." The arrestor provides a path to ground for lightning energy before it enters the building. The arrestor's ground connects to the outside lightning ground system, which is bonded to all other grounds.

---

## Tower Safety

Tower climbing is inherently dangerous — falls are often fatal, and electrical hazards on towers add another layer of risk.

### Safety Harness

Before climbing, **confirm that the harness is rated for the weight of the climber and that it is within its allowable service life**. Harnesses have both a weight rating and an expiration date. The webbing degrades from UV exposure and age. A harness past its service life or underrated for the climber's weight is not a harness — it's a false sense of security.

### Lockout/Tagout

Before climbing a tower with electrically powered devices (rotators, amplifiers, obstruction lights), **make sure all circuits that supply power to the tower are locked out and tagged**. Lockout/tagout (LOTO) means physically locking the circuit breaker OFF and attaching a tag identifying who locked it and why. This prevents someone from accidentally energizing a circuit while you're on the tower.

---

## Generator Safety

Emergency generators produce carbon monoxide (CO) — an odorless, colorless, deadly gas. **Operate generators in well-ventilated areas only.** Running a generator in a garage, basement, or enclosed porch can build lethal CO concentrations in minutes. CO poisoning kills hundreds of people every year during power outages. Outside, away from windows and air intakes, is the only safe location.

---

## Soldering Safety

Lead-tin solder's primary danger is lead contamination — **lead can contaminate food if hands are not washed carefully after handling solder**. Lead is a cumulative neurotoxin that builds up in your body over time. Always wash your hands after soldering, and never eat or drink at the soldering bench. Solder flux also produces irritating fumes — use ventilation.

---

## Power Supply Safety

A power supply interlock **ensures that dangerous voltages are removed if the cabinet is opened**. This is critical for high-voltage supplies used with vacuum tube amplifiers, where plate voltages can exceed 2000V — instantly lethal. The interlock mechanically disconnects power when the cover is opened, so you can't accidentally touch energized components.

---

## Exam Strategy for G0

With only 2 questions from 25, G0 is the smallest subelement on the exam. But don't skip it — the questions are mostly common-sense safety with a few specific numbers to memorize:

**RF Safety Numbers:**
- 1 milliwatt time-averaged = threshold for RF exposure rules applying
- OET Bulletin 65 = the FCC's official RF exposure guidance document
- 6 minutes = uncontrolled environment time-averaging period
- 30 minutes = controlled environment time-averaging period
- Lower duty cycle = more peak power allowed

**Electrical Safety Numbers:**
- AWG 14 → 15A breaker
- AWG 12 → 20A breaker
- Only hot wires get fuses/breakers

**Lightning:**
- Ground system outside the building
- Bond all grounds together
- Arrestors at the building entry point

**Tower Safety:**
- Check harness weight rating AND service life
- Lockout/tagout all power circuits before climbing

**Generator:**
- Well-ventilated area (carbon monoxide kills)

Most G0 questions test practical safety judgment rather than obscure regulations. If an answer choice would keep people safe, it's probably correct. If an answer choice sounds bureaucratic or nonsensical, it's probably a distractor.

---

## Where These Concepts Apply Later

- **Grounding and bonding** → revisited in [G4 (Amateur Practices)](G4-amateur-practices.md) for station setup and mobile installations
- **RF exposure and antenna safety** → directly relevant to [G9 (Antennas)](G9-antennas-feedlines.md) when choosing antenna height and location
- **Electrical safety (fusing, wire gauge)** → connects to [G7 (Practical Circuits)](G7-practical-circuits.md) power supply design
