# G5 — Electrical Principles

You already know Ohm's Law and the power formula from your Technician study. The General exam builds on that foundation — you're going deeper into AC theory, impedance, reactance, resonance, transformers, and the math that ties it all together. This subelement has 40 questions in the pool and you'll see 3 on your exam.

The good news: the concepts connect logically. Master the underlying ideas and the exam questions answer themselves.

---

## Reactance: AC's Version of Resistance

At the Technician level, you learned that resistance opposes current flow and is measured in ohms. Reactance is the AC equivalent — it's the opposition to alternating current caused specifically by capacitors and inductors. Reactance is also measured in ohms, and we use the letter **X** to represent it.

Here's the key difference: resistance dissipates energy as heat. Reactance *stores and releases* energy — in an electric field (capacitors) or a magnetic field (inductors). No energy is lost to heat in an ideal reactive component.

There are two flavors:

### Inductive Reactance (X_L)

An inductor opposes *changes* in current. When AC tries to push current back and forth through an inductor, the inductor pushes back — and it pushes back harder at higher frequencies.

**Formula:** X_L = 2πfL

- f = frequency in hertz
- L = inductance in henrys
- X_L = inductive reactance in ohms

**Key relationship:** As frequency increases, inductive reactance increases. Double the frequency → double the reactance. At DC (f = 0), an inductor is just a piece of wire — zero reactance.

**Worked example:** What's the reactance of a 10 mH inductor at 1 MHz?
- X_L = 2π × 1,000,000 × 0.010 = 62,832 Ω ≈ 63 kΩ

### Capacitive Reactance (X_C)

A capacitor does the opposite — it opposes *changes in voltage*. At high frequencies, it lets AC pass easily. At low frequencies, it blocks.

**Formula:** X_C = 1 / (2πfC)

- f = frequency in hertz
- C = capacitance in farads
- X_C = capacitive reactance in ohms

**Key relationship:** As frequency increases, capacitive reactance *decreases*. Double the frequency → half the reactance. At DC (f = 0), a capacitor is an open circuit — infinite reactance.

**Worked example:** What's the reactance of a 100 pF capacitor at 7 MHz?
- X_C = 1 / (2π × 7,000,000 × 0.0000000001) = 1 / 0.0044 ≈ 227 Ω

### The Opposite Twins

Notice the symmetry:
- **Inductor:** Reactance goes UP with frequency (blocks high frequencies)
- **Capacitor:** Reactance goes DOWN with frequency (passes high frequencies)

This opposing behavior is what makes resonant circuits, filters, and impedance matching possible. The exam loves to test whether you know which direction each one goes — get these two relationships locked in.

> **Exam trap:** Reactance depends on *frequency*, not *amplitude*. Changing the signal strength doesn't change the reactance. The exam offers amplitude-based wrong answers.

---

## Impedance: The Complete Picture

Impedance (Z) combines resistance and reactance into a single measurement. It's the total opposition to AC current flow, measured in ohms.

**Impedance = Resistance + Reactance** (combined as vectors, not simple addition)

Technically, Z = √(R² + X²) for a series circuit. But for the exam, the key concept is:

- **Impedance** is the ratio of voltage to current: Z = V/I (Ohm's Law for AC)
- It's measured in **ohms** — same unit as resistance and reactance
- It includes both the energy-dissipating part (R) and the energy-storing part (X)

### Related Terms

The exam tests several related terms:

| Term | Symbol | Definition | Unit |
|------|--------|-----------|------|
| Impedance | Z | Total opposition to AC | Ohms (Ω) |
| Admittance | Y | Inverse of impedance (1/Z) | Siemens (S) |
| Reactance | X | Opposition from L or C | Ohms (Ω) |
| Susceptance | B | Inverse of reactance (1/X) | Siemens (S) |
| Resistance | R | Opposition (dissipative) | Ohms (Ω) |
| Conductance | G | Inverse of resistance (1/R) | Siemens (S) |

**Admittance** is the inverse of impedance — it tells you how *easily* current flows rather than how much it's opposed. Don't confuse it with conductance (inverse of resistance) or susceptance (inverse of reactance).

### Impedance Matching

Getting maximum power from your transmitter to your antenna requires matching impedance. If the source impedance doesn't match the load impedance, power gets reflected back. Three common matching devices work at radio frequencies:

1. **Transformers** — match impedance through turns ratio
2. **Pi-networks** — use capacitors and inductors in a π configuration
3. **Transmission line sections** — a quarter-wave section transforms impedance

All three are correct, and the exam asks about this. They're all standard tools in the amateur's matching toolkit.

---

## Resonance: When Reactances Cancel

Resonance occurs when inductive reactance equals capacitive reactance (X_L = X_C). At that frequency, the two reactances cancel each other out.

**Resonant frequency:** f = 1 / (2π√(LC))

What happens at resonance depends on the circuit type:

### Series Resonance
- X_L and X_C cancel → impedance drops to just the small DC resistance
- **Impedance is very low** at resonance
- Current is maximum
- Used in filters to pass a specific frequency

### Parallel Resonance
- X_L and X_C cancel → impedance goes very high
- Current from the source is minimum
- Used in filters to block a specific frequency

The exam asks about **series LC resonance** specifically — know that impedance goes very LOW.

At resonance, inductive reactance and capacitive reactance cancel. That's the defining condition. Current and voltage are NOT equal at resonance. Resistance is NOT cancelled. The circuit does NOT radiate its energy as radio waves.

---

## Decibels: The Power Ratio Language

You learned the basics at the Technician level. The General exam goes deeper with more calculations and the 1 dB loss figure.

### The Two Rules You Already Know

- **3 dB = double (or half) the power**
- **10 dB = 10× (or 1/10) the power**

### The New One: 1 dB Loss

A loss of **1 dB equals approximately 20.6% power loss**. This means 79.4% of your power survives each 1 dB of loss. This is useful for evaluating feed line loss — each dB of loss in your coax eats about one-fifth of your power.

**Worked example:** Your coax has 2 dB of loss and you're transmitting 100 watts.
- 1 dB loss: 100 × 0.794 = 79.4 watts
- 2 dB loss: 79.4 × 0.794 = 63 watts (or roughly: 2 dB ≈ 37% total loss)

---

## RMS, Peak, and Peak-to-Peak Voltages

A sine wave has three ways to measure its voltage, and the exam tests conversions between all of them.

### The Relationships

- **V_peak = V_RMS × 1.414** (multiply RMS by √2)
- **V_RMS = V_peak × 0.707** (multiply peak by 1/√2)
- **V_peak-to-peak = V_peak × 2** (it's just double the peak)

### Why RMS Matters

The **RMS (Root Mean Square)** value of an AC signal produces the same power dissipation as a DC voltage of equal value. A 120V RMS AC signal heats a resistor exactly as much as 120V DC. This is why AC voltages are specified as RMS by default — your wall outlet is 120V RMS.

### Worked Examples

**RMS to Peak-to-Peak:** 120V RMS → what's the peak-to-peak?
1. V_peak = 120 × 1.414 = 169.7V
2. V_pp = 169.7 × 2 = **339.4V**

Your wall outlet actually swings 339 volts from positive peak to negative peak.

**Peak to RMS:** 17V peak → what's the RMS?
- V_RMS = 17 × 0.707 = **12.0V**

**RMS from Power:** What's the RMS voltage across a 50Ω load dissipating 1200W?
- V_RMS = √(P × R) = √(1200 × 50) = √60,000 = **245 volts**

---

## PEP: Peak Envelope Power

PEP is the power calculated from the peak voltage of the signal envelope. It's the standard power measurement for SSB transmitters.

### The Formula

**PEP = V_peak² / (2R)**

Or equivalently, convert to RMS first: V_RMS = V_peak / √2, then P = V_RMS² / R.

### The Peak-to-Peak Trap

When the question gives you **peak-to-peak** voltage, you must divide by 2 first to get peak voltage before calculating PEP. This is the most common mistake.

### Worked Examples

**200V peak-to-peak across 50Ω:**
1. V_peak = 200 / 2 = 100V
2. PEP = 100² / (2 × 50) = 10,000 / 100 = **100 watts**

**500V peak-to-peak across 50Ω:**
1. V_peak = 500 / 2 = 250V
2. PEP = 250² / (2 × 50) = 62,500 / 100 = **625 watts**

### Unmodulated Carrier

For an unmodulated carrier (constant amplitude), PEP equals average power — the ratio is **1.00**. There's no variation in the envelope, so peak and average are identical. If someone tells you the average power of an unmodulated carrier is 1060 watts, the PEP is also 1060 watts.

---

## Power Calculations

The General exam includes several power calculation questions using formulas you already know, plus the I²R form.

### The Three Power Formulas

1. **P = E × I** (power = voltage × current)
2. **P = E² / R** (when you know voltage and resistance)
3. **P = I² × R** (when you know current and resistance)

These are all derived from Ohm's Law combined with P = EI.

### Worked Examples

**400 VDC across 800Ω:**
- P = E²/R = 400²/800 = 160,000/800 = **200 watts**

**12 VDC at 0.2A:**
- P = E × I = 12 × 0.2 = **2.4 watts**

**7.0 mA through 1,250Ω:**
- P = I²R = (0.007)² × 1250 = 0.000049 × 1250 = 0.061 watts = **61 milliwatts**
- Watch the metric prefix — the answer is in milliwatts, not watts.

### Parallel Circuits and Current

In a parallel circuit, the total current equals the sum of the branch currents. Each branch draws current independently (I = V/R for each branch), and the total from the source is the sum. Adding more parallel branches increases total current — which is why parallel resistance is always less than any individual branch.

---

## Transformers

Transformers transfer energy between circuits through mutual inductance — the changing magnetic field from AC in the primary winding induces a voltage in the secondary. They only work with AC (a steady DC creates a constant field that can't induce anything).

### Voltage Ratio = Turns Ratio

**V_out / V_in = N_secondary / N_primary**

**Worked example:** 500-turn primary, 1500-turn secondary, 120 VAC in:
- Turns ratio = 1500/500 = 3
- V_out = 120 × 3 = **360 volts**

### The Reversal Trick

A 4:1 step-down transformer applied in reverse (signal to the secondary) becomes a 1:4 step-up — the input voltage is multiplied by 4. The turns ratio works both ways.

### Why Primary Wire Is Bigger in Step-Up

Power in ≈ power out (V₁ × I₁ ≈ V₂ × I₂). In a step-up transformer, the primary has lower voltage and therefore higher current. Higher current needs larger wire to avoid overheating. The high-voltage secondary carries less current and can use thinner wire.

### Impedance Matching with Transformers

The turns ratio for impedance matching is:

**N = √(Z_high / Z_low)**

**Worked example:** Match 600Ω antenna to 50Ω coax:
- N = √(600/50) = √12 = 3.46 ≈ **3.5 to 1**

Note: impedance ratio is the *square* of the turns ratio. A 3.5:1 turns ratio gives a 12.25:1 impedance ratio.

---

## Series and Parallel Components

The rules for combining components in series and parallel are fundamental. The General exam tests these with specific calculations.

### Resistors

**Series:** R_total = R₁ + R₂ + R₃ (just add them)

**Parallel (reciprocal formula):** 1/R_total = 1/R₁ + 1/R₂ + 1/R₃

**Parallel shortcut (two resistors):** R_total = (R₁ × R₂) / (R₁ + R₂)

**Worked examples:**

10Ω, 20Ω, and 50Ω in parallel:
- 1/R = 1/10 + 1/20 + 1/50 = 0.1 + 0.05 + 0.02 = 0.17
- R = 1/0.17 = **5.9 ohms**

100Ω and 200Ω in parallel:
- R = (100 × 200)/(100 + 200) = 20,000/300 = **67 ohms**

**Rule of thumb:** Parallel resistance is always less than the smallest individual resistor.

### Capacitors (Opposite of Resistors!)

**Parallel:** C_total = C₁ + C₂ + C₃ (just add — more plate area = more capacitance)

**Series:** 1/C_total = 1/C₁ + 1/C₂ + 1/C₃ (reciprocal formula — like resistors in parallel)

**Worked examples:**

Two 5.0 nF and one 750 pF in parallel:
- Convert: 750 pF = 0.75 nF
- C = 5.0 + 5.0 + 0.75 = **10.75 nF**

Three 100 μF in series:
- 1/C = 1/100 + 1/100 + 1/100 = 3/100
- C = 100/3 = **33.3 μF**

20 μF and 50 μF in series:
- C = (20 × 50)/(20 + 50) = 1000/70 = **14.3 μF**

**Key:** To *increase* capacitance, add a capacitor in **parallel**. Series decreases it.

### Inductors (Same as Resistors)

**Series:** L_total = L₁ + L₂ (just add — extending the coil)

**Parallel:** 1/L_total = 1/L₁ + 1/L₂ + 1/L₃ (reciprocal formula)

**Worked examples:**

20 mH and 50 mH in series:
- L = 20 + 50 = **70 mH**

Three 10 mH in parallel:
- 1/L = 1/10 + 1/10 + 1/10 = 3/10
- L = 10/3 = **3.3 mH**

**Key:** To *increase* inductance, add an inductor in **series**. Parallel decreases it.

### The Pattern

| Component | Series | Parallel |
|-----------|--------|----------|
| Resistors | Add directly | Reciprocal formula |
| Capacitors | Reciprocal formula | Add directly |
| Inductors | Add directly | Reciprocal formula |

Capacitors are the odd one out — they use the reciprocal formula in series (opposite of resistors and inductors). This is because series capacitors reduce total plate area from the perspective of charge storage.

---

## Quick Reference: Key Formulas

| Formula | Use |
|---------|-----|
| X_L = 2πfL | Inductive reactance |
| X_C = 1/(2πfC) | Capacitive reactance |
| f = 1/(2π√(LC)) | Resonant frequency |
| Z = V/I | Impedance (Ohm's Law for AC) |
| V_RMS = V_peak × 0.707 | Peak to RMS conversion |
| V_peak = V_RMS × 1.414 | RMS to peak conversion |
| PEP = V_peak²/(2R) | Peak envelope power |
| P = E × I = E²/R = I²R | DC power |
| N = √(Z₁/Z₂) | Transformer impedance matching turns ratio |
| 3 dB = 2× power | Decibel rule |
| 10 dB = 10× power | Decibel rule |
| 1 dB loss ≈ 20.6% | Power loss per dB |

---

## Study Tips for G5

1. **Reactance direction:** Inductors go up with frequency, capacitors go down. This is the most tested concept.
2. **Series vs. parallel:** Capacitors are backwards from resistors and inductors. Memorize the pattern table.
3. **PEP calculations:** Always convert peak-to-peak to peak first (divide by 2).
4. **RMS conversions:** 0.707 and 1.414 — multiply peak by 0.707 to get RMS, multiply RMS by 1.414 to get peak.
5. **Transformer turns ratio for impedance:** Square root of the impedance ratio, not the impedance ratio itself.
6. **Resonance:** Series = low impedance. Know that reactances cancel (not resistance).
7. **1 dB ≈ 20.6% loss:** New for General. Each dB of feed line loss costs about one-fifth of your power.
