# G6 — Circuit Components

The General exam's Circuit Components subelement covers the building blocks of radio circuits — from basic passive parts like resistors and capacitors to semiconductors, vacuum tubes, integrated circuits, ferrite cores, and the connectors that tie it all together. You'll see 2 questions on your exam drawn from a pool of 23.

If you've worked through G5 (Electrical Principles), you already know how resistors, capacitors, and inductors behave in circuits. G6 shifts from *how they work* to *what they are* — the practical characteristics, limitations, and quirks of real-world components.

---

## Diodes: The One-Way Valve

A diode is the simplest semiconductor device — it conducts current in one direction and blocks it in the other. The critical number for any diode is its **forward threshold voltage** — the voltage needed before it starts conducting.

### Silicon vs. Germanium

Two numbers to memorize:

- **Silicon diode:** ~0.7 volts forward threshold
- **Germanium diode:** ~0.3 volts forward threshold

Silicon dominates modern electronics because it's thermally stable, cheap, and handles higher power. But germanium still shows up in low-signal detector circuits where that extra 0.4V drop matters — if your signal is only 0.5V, a silicon diode blocks it entirely while a germanium diode lets it through.

> **Exam tip:** The exam tests both values. Don't mix them up. Silicon = 0.7, Germanium = 0.3. Silicon is higher because it takes more energy to push electrons across a silicon junction.

### LEDs (Light-Emitting Diodes)

An LED emits light when **forward biased** — current flows from anode to cathode, and electrons recombine with holes at the junction, releasing energy as photons. The color depends on the semiconductor material and band gap energy.

Reverse biasing doesn't produce light. The exam specifically asks about the bias condition for light emission — the answer is always forward biased.

---

## Transistors: Amplifiers and Switches

### Bipolar Junction Transistors (BJTs)

When a BJT is used as a **switch**, it operates at two extremes:

- **Saturation** — fully ON. The transistor conducts as hard as it can. Collector-to-emitter looks like a short circuit.
- **Cutoff** — fully OFF. No current flows. Acts like an open circuit.

The **active region** (between saturation and cutoff) is where linear amplification happens — the transistor proportionally amplifies the input signal. But as a switch, you don't want proportional — you want all-or-nothing.

> **Exam trap:** "Enhancement and depletion modes" are MOSFET terms, not BJT terms. "Peak and valley current" relates to tunnel diodes. For BJT switches: saturation and cutoff.

### MOSFETs

The MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) has a defining structural feature: **the gate is separated from the channel by a thin insulating layer** — silicon dioxide (SiO₂).

This is the "oxide" in the name, and it's what makes MOSFETs special:

- The insulated gate draws virtually **zero current** — extremely high input impedance
- A voltage on the gate creates an electric field through the oxide that controls current flow in the channel
- This makes MOSFETs easy to drive and ideal for high-speed switching

The downside: that thin oxide layer is fragile. Static electricity can punch right through it and destroy the device. Always handle MOSFETs with ESD precautions.

Compare with JFETs, where the gate is a back-biased PN junction (not insulated), or BJTs, where base current is required to operate.

---

## Vacuum Tubes: Still on the Exam

Yes, vacuum tubes are on the General exam. Some amateur amplifiers still use them (especially at HF), and the concepts help you understand amplification in general.

### The Control Grid

A vacuum tube's cathode emits electrons (when heated), and the plate collects them. Between them sits the **control grid** — a wire mesh that regulates electron flow. A small voltage change on the grid produces a large change in plate current. This is amplification.

Think of it like a valve — the control grid doesn't supply the energy, it just controls how much flows through.

### The Screen Grid

In a simple triode (cathode, grid, plate), there's significant capacitance between the control grid and plate. At RF frequencies, this capacitance feeds output energy back to the input, causing unwanted oscillation.

The **screen grid** sits between the control grid and the plate, acting as an **electrostatic shield** that reduces grid-to-plate capacitance. A tube with a screen grid is called a tetrode (four elements). This was a major advance — tetrodes are far more stable at RF than triodes.

> **Don't confuse:** Control grid = controls amplification. Screen grid = reduces capacitance. Suppressor grid (in pentodes) = reduces secondary emission from the plate.

---

## Batteries

### Lead-Acid: The 10.5V Rule

A standard 12-volt lead-acid battery should never be discharged below **10.5 volts** for maximum service life. That's about 1.75V per cell (a 12V battery has 6 cells).

Deep discharge causes **sulfation** — lead sulfate crystals form on the plates and harden, permanently reducing the battery's capacity. Going to 8.5V or 6V is abusive and dramatically shortens life.

### Internal Resistance

A battery with low internal resistance can deliver **high discharge current**. Think of internal resistance as a bottleneck: when you draw current, voltage drops across it (V_drop = I × R_internal). Low internal resistance means less voltage sag under load.

This is why lithium and AGM batteries are preferred for powering transceivers — they maintain their voltage even when you key up a 100W transmitter and suddenly demand 20+ amps.

---

## Real-World Passive Components

G5 covered how resistors, capacitors, and inductors combine mathematically. G6 covers the practical realities of actual parts.

### Wire-Wound Resistors: Not for RF

A wire-wound resistor is literally a coil of resistance wire — and a coil is an inductor. At DC and low audio frequencies, the parasitic inductance is negligible. But at radio frequencies, it becomes significant and **makes circuit performance unpredictable**.

The resistor's impedance changes with frequency, may self-resonate, and throws off tuned circuits. For RF work, use carbon composition, metal film, or metal oxide resistors — they have minimal parasitic inductance.

### Electrolytic Capacitors: Big but Sloppy

Electrolytic capacitors offer **high capacitance for a given volume** — that's their superpower. They use an extremely thin oxide layer as the dielectric, packing hundreds or thousands of microfarads into a small can.

The tradeoffs:
- **Polarized** — install backwards and they can fail explosively
- **Loose tolerance** — ±20% is typical
- **High leakage current** — charge slowly drains even when nothing's connected
- **Poor at RF** — high equivalent series resistance and inductance

You'll find electrolytics in power supply filter circuits, not in RF signal paths.

### Ceramic Capacitors: Cheap and Everywhere

Low-voltage ceramic capacitors are characterized by **comparatively low cost**. They're the most common capacitor type in electronics — billions are manufactured annually.

However, basic ceramic caps (especially Y5V and Z5U types) have loose tolerances and poor stability — capacitance changes with temperature and applied voltage. For precision work, use NP0/C0G ceramics (stable but more expensive) or silver mica capacitors.

### Inductors Above Self-Resonance

Every real inductor has parasitic capacitance between its windings. At the **self-resonant frequency**, this capacitance resonates with the inductance. Above that frequency, the capacitance dominates and the inductor **becomes capacitive** — its reactance decreases with frequency instead of increasing.

This connects directly to G5's reactance concepts: an ideal inductor's reactance always increases with frequency (X_L = 2πfL). But a real inductor only follows this up to its self-resonant frequency. Above that, it's not really an inductor anymore.

> **Bottom line:** Always choose inductors rated for your operating frequency. An HF inductor used at microwave frequencies may behave like a capacitor.

---

## Ferrite Cores and Toroids

Ferrite materials are central to amateur radio — they're used in inductors, transformers, baluns, and EMI suppression.

### Ferrite Mix = Frequency Range

What determines how a ferrite core performs at different frequencies? **The composition, or "mix," of materials used.** Ferrite is a ceramic compound of iron oxide blended with other metal oxides (manganese, zinc, nickel, etc.), and different recipes optimize for different frequency ranges:

- **Mix 43** — 10 MHz to 1 GHz, great for EMI suppression
- **Mix 61** — 200 kHz to 10 MHz, designed for inductors
- **Mix 31** — 1 MHz to 300 MHz, popular for choking common-mode currents

The physical dimensions (diameter, thickness) affect inductance values, but it's the material composition that determines the useful frequency range.

### Toroidal Advantages

A ferrite core toroidal inductor has three key advantages — and the exam says **all of them are correct**:

1. **Large inductance values** are obtainable (the high-permeability core multiplies inductance)
2. **Core material can be optimized** for specific frequency ranges (through different mixes)
3. **Most of the magnetic field is contained in the core** — minimal stray coupling to nearby components

The self-shielding property is especially valuable in amateur radio where circuits live close together. Toroids are the go-to inductor for homebrew projects.

### Ferrite Beads: Common-Mode Chokes

A ferrite bead or core on a coaxial cable reduces common-mode RF current by **creating an impedance in the current's path**. The ferrite's high permeability converts the RF current's magnetic field into heat, presenting an impedance that discourages common-mode flow.

The clever part: the ferrite only affects **common-mode** current (flowing on the outside of the shield). The differential-mode signal inside the coax is unaffected because its magnetic fields cancel inside the ferrite. This is why ferrite chokes suppress interference without degrading your wanted signal.

---

## Integrated Circuits

### Op-Amps: Analog Workhorses

An operational amplifier is an **analog** device. It amplifies continuous signals with extremely high open-loop gain, and it's the foundation of analog circuit design — used for amplification, active filtering, buffering, and signal conditioning.

Don't confuse it with digital ICs, MMICs, or programmable logic. The classic 741 op-amp has been in production since the 1960s. In ham radio, op-amps appear in audio stages, AGC circuits, and active filters.

### MMICs: Microwave on a Chip

MMIC stands for **Monolithic Microwave Integrated Circuit**. "Monolithic" means the entire circuit — transistors, resistors, capacitors, transmission lines — is fabricated on a single semiconductor chip, usually gallium arsenide (GaAs).

MMICs are designed for microwave frequencies (typically above 1 GHz) where conventional silicon ICs struggle. You'll find them in satellite receivers, cell phones, and amateur microwave equipment.

### CMOS vs. TTL

CMOS (Complementary Metal-Oxide-Semiconductor) circuits have one standout advantage over TTL (Transistor-Transistor Logic): **low power consumption**.

CMOS uses complementary MOSFET pairs that draw almost zero current when static — power is only consumed during switching. TTL's bipolar transistors draw continuous current even when idle. This makes CMOS the default choice for battery-powered digital circuits.

---

## RF Connectors

The exam tests your knowledge of four connector types — know what each looks like and where it's used.

### BNC (Bayonet Neill-Concelman)
- **Bayonet quick-connect** (quarter-turn lock)
- **50-ohm impedance** (75-ohm versions exist for video)
- **Usable to ~4 GHz** with low SWR
- Common on test equipment, lower-power transceivers, lab instruments
- Good for HF through UHF amateur work

### Type N (Neill)
- **Threaded coupling** — weather-resistant and vibration-resistant
- **Moisture resistant**, designed for outdoor and military use
- **Usable to 10 GHz**
- Larger than BNC, found on commercial antenna systems and quality amateur installations
- NOT a nickel-plated PL-259 — it's a completely different design

### SMA (SubMiniature version A)
- **Small threaded connector** — compact but precise
- **Usable to several GHz** (typically rated to 18 GHz+)
- Common on SDR dongles, handheld radios, VHF/UHF equipment, test instruments
- The go-to connector for anything modern and above VHF

### RCA Phono
- Used for **low-frequency or DC signal connections** — audio in/out, external speakers, accessories
- **NOT suitable for RF** — no impedance control, poor shielding
- If you see an RCA jack on a transceiver, it's for audio or control signals, never antenna

> **Frequency hierarchy:** RCA (audio only) → PL-259 (HF) → BNC (to 4 GHz) → Type N (to 10 GHz) → SMA (to 18+ GHz)

---

## Quick Reference: Key Facts for G6

| Topic | Key Fact |
|-------|----------|
| Silicon diode threshold | 0.7 volts |
| Germanium diode threshold | 0.3 volts |
| LED bias for light | Forward biased |
| BJT switch modes | Saturation and cutoff |
| MOSFET gate construction | Insulated from channel by oxide layer |
| Vacuum tube control grid | Regulates electron flow (amplification) |
| Screen grid purpose | Reduces grid-to-plate capacitance |
| Lead-acid minimum voltage | 10.5V (for 12V battery) |
| Low internal resistance advantage | High discharge current |
| Wire-wound resistors + RF | Parasitic inductance = unpredictable |
| Electrolytic cap advantage | High capacitance per volume |
| Ceramic cap advantage | Low cost |
| Inductor above self-resonance | Becomes capacitive |
| Ferrite core frequency behavior | Determined by material mix |
| Toroidal inductor | All advantages correct |
| Ferrite bead mechanism | Creates impedance in current path |
| Op-amp type | Analog device |
| MMIC meaning | Monolithic Microwave Integrated Circuit |
| CMOS vs TTL advantage | Low power consumption |
| BNC upper limit | 4 GHz |
| Type N description | Moisture-resistant, to 10 GHz |
| SMA description | Small threaded, to several GHz |
| RCA Phono use | Low frequency / DC connections |

---

## Study Tips for G6

1. **Diode voltages:** Silicon = 0.7V, Germanium = 0.3V. These two numbers account for two exam questions.
2. **Connector frequency limits:** Know which connector goes how high. BNC = 4 GHz, Type N = 10 GHz, SMA = 18+ GHz, RCA = audio only.
3. **Ferrite mix = frequency:** It's always about the material composition, not the physical size.
4. **MOSFET = insulated gate:** The oxide layer is the defining feature. If the question mentions "insulating layer," it's describing a MOSFET.
5. **Real components have parasites:** Wire-wound resistors have inductance, inductors have capacitance, electrolytics have leakage. The exam tests your awareness of these real-world limitations.
6. **Vacuum tube grid functions:** Control grid controls, screen grid shields. Don't swap them.
