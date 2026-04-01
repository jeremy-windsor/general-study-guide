# G5 — Electrical Principles
*3 questions on the exam from a pool of 40*

## Group G5A — Reactance; inductance; capacitance; impedance; impedance matching

### G5A01
**What happens when inductive and capacitive reactance are equal in a series LC circuit?**
- A) Resonance causes impedance to be very high
- B) Impedance is equal to the geometric mean of the inductance and capacitance
- **C) Resonance causes impedance to be very low** ✅
- D) Impedance is equal to the arithmetic mean of the inductance and capacitance

> In a series LC circuit, inductive reactance (X_L) and capacitive reactance (X_C) act in opposite directions — inductance resists current changes while capacitance resists voltage changes. When X_L equals X_C, they cancel each other out completely, leaving only the small residual resistance of the wire. This is series resonance, and it makes the impedance very low — essentially just the DC resistance of the components. This is the opposite of parallel resonance, where impedance goes very high.

### G5A02
**What is reactance?**
- A) Opposition to the flow of direct current caused by resistance
- **B) Opposition to the flow of alternating current caused by capacitance or inductance** ✅
- C) Reinforcement of the flow of direct current caused by resistance
- D) Reinforcement of the flow of alternating current caused by capacitance or inductance

> Reactance is the opposition to alternating current caused by capacitance or inductance. Unlike resistance, which opposes all current equally (DC and AC), reactance only affects AC and depends on frequency. An inductor has more reactance at higher frequencies; a capacitor has less. Reactance is measured in ohms (just like resistance), but it behaves differently because it stores and releases energy rather than dissipating it as heat.

### G5A03
**Which of the following is opposition to the flow of alternating current in an inductor?**
- A) Conductance
- B) Reluctance
- C) Admittance
- **D) Reactance** ✅

> The opposition to AC current flow in an inductor is called reactance — specifically, inductive reactance (X_L). Don't confuse it with reluctance (opposition to magnetic flux in a magnetic circuit), conductance (the inverse of resistance), or admittance (the inverse of impedance). Reactance is the AC-specific opposition that depends on frequency.

### G5A04
**Which of the following is opposition to the flow of alternating current in a capacitor?**
- A) Conductance
- B) Reluctance
- **C) Reactance** ✅
- D) Admittance

> The opposition to AC current flow in a capacitor is also called reactance — specifically, capacitive reactance (X_C). Both inductors and capacitors create reactance, but in opposite directions: inductive reactance increases with frequency while capacitive reactance decreases. This opposing behavior is what makes resonant circuits possible.

### G5A05
**How does an inductor react to AC?**
- A) As the frequency of the applied AC increases, the reactance decreases
- B) As the amplitude of the applied AC increases, the reactance increases
- C) As the amplitude of the applied AC increases, the reactance decreases
- **D) As the frequency of the applied AC increases, the reactance increases** ✅

> An inductor's reactance increases as frequency increases. The formula is X_L = 2πfL. Double the frequency and you double the reactance. This makes intuitive sense: an inductor opposes changes in current, and higher-frequency AC changes direction more rapidly, so the inductor pushes back harder. Note that reactance depends on frequency, not amplitude — changing the signal strength doesn't change the reactance.

### G5A06
**How does a capacitor react to AC?**
- **A) As the frequency of the applied AC increases, the reactance decreases** ✅
- B) As the frequency of the applied AC increases, the reactance increases
- C) As the amplitude of the applied AC increases, the reactance increases
- D) As the amplitude of the applied AC increases, the reactance decreases

> A capacitor's reactance decreases as frequency increases. The formula is X_C = 1/(2πfC). Double the frequency and the reactance drops to half. This is the opposite of an inductor. At very high frequencies, a capacitor looks almost like a short circuit (very low reactance). At DC (zero frequency), a capacitor is an open circuit (infinite reactance). This is why capacitors block DC but pass AC.

### G5A07
**What is the term for the inverse of impedance?**
- A) Conductance
- B) Susceptance
- C) Reluctance
- **D) Admittance** ✅

> Admittance is the inverse of impedance, just as conductance is the inverse of resistance. If impedance tells you how much a circuit opposes current flow, admittance tells you how easily current flows. It's measured in siemens (S). Susceptance is the inverse of reactance (not impedance), and reluctance relates to magnetic circuits, not electrical impedance.

### G5A08
**What is impedance?**
- A) The ratio of current to voltage
- B) The product of current and voltage
- **C) The ratio of voltage to current** ✅
- D) The product of current and reactance

> Impedance is the ratio of voltage to current in an AC circuit — essentially Ohm's Law extended to AC. Z = V/I. It combines both resistance (which dissipates energy as heat) and reactance (which stores and releases energy) into a single value measured in ohms. Impedance is the complete picture of how a circuit opposes AC current flow.

### G5A09
**What unit is used to measure reactance?**
- A) Farad
- **B) Ohm** ✅
- C) Ampere
- D) Siemens

> Reactance is measured in ohms — the same unit as resistance and impedance. This makes the math work out cleanly: you can combine resistance and reactance (using vector addition) to get impedance, all in the same unit. Farads measure capacitance, amperes measure current, and siemens measure conductance or admittance.

### G5A10
**Which of the following devices can be used for impedance matching at radio frequencies?**
- A) A transformer
- B) A Pi-network
- C) A length of transmission line
- **D) All these choices are correct** ✅

> Transformers, Pi-networks, and lengths of transmission line can all be used for impedance matching at radio frequencies. A transformer matches impedance through its turns ratio. A Pi-network (named for its π shape) uses reactive components to transform impedance. And a specific length of transmission line acts as an impedance transformer — quarter-wave sections are especially useful. All three are standard tools in the amateur's matching toolkit.

### G5A11
**What letter is used to represent reactance?**
- A) Z
- **B) X** ✅
- C) B
- D) Y

> The letter X represents reactance. Z is impedance, R is resistance, B is susceptance, and Y is admittance. Specifically, X_L is inductive reactance and X_C is capacitive reactance. These letter conventions are universal in electronics and appear constantly in circuit analysis.

### G5A12
**What occurs in an LC circuit at resonance?**
- A) Current and voltage are equal
- B) Resistance is cancelled
- C) The circuit radiates all its energy in the form of radio waves
- **D) Inductive reactance and capacitive reactance cancel** ✅

> At resonance in an LC circuit, inductive reactance and capacitive reactance are equal and cancel each other out. This is the defining condition of resonance: X_L = X_C. The resonant frequency is f = 1/(2π√(LC)). At resonance, current and voltage are NOT necessarily equal, resistance is NOT cancelled (only reactance cancels), and the circuit does NOT radiate its energy as radio waves — that would require an antenna.

## Group G5B — The decibel; current and voltage dividers; electrical power calculations; sine wave root-mean-square (RMS) values; PEP calculations

### G5B01
**What dB change represents a factor of two increase or decrease in power?**
- A) Approximately 2 dB
- **B) Approximately 3 dB** ✅
- C) Approximately 6 dB
- D) Approximately 9 dB

> A factor of two change in power is approximately 3 dB. This is the single most important decibel relationship to memorize. Double the power = +3 dB. Half the power = −3 dB. The other key relationship is that 10× power = +10 dB. With just these two rules, you can work out almost any dB problem on the exam.

### G5B02
**How does the total current relate to the individual currents in a circuit of parallel resistors?**
- A) It equals the average of the branch currents
- B) It decreases as more parallel branches are added to the circuit
- **C) It equals the sum of the currents through each branch** ✅
- D) It is the sum of the reciprocal of each individual voltage drop

> In a parallel resistor circuit, the total current equals the sum of the currents through each branch. Each branch draws current independently based on its own resistance (I = V/R), and the total current from the source is the sum of all branch currents. This is Kirchhoff's Current Law — current entering a node equals current leaving it. Adding more parallel branches increases total current, which is why parallel resistance is always less than any individual branch.

### G5B03
**How many watts of electrical power are consumed if 400 VDC is supplied to an 800-ohm load?**
- A) 0.5 watts
- **B) 200 watts** ✅
- C) 400 watts
- D) 3200 watts

> Using P = E²/R: 400² ÷ 800 = 160,000 ÷ 800 = 200 watts. When you know voltage and resistance but not current, this form of the power equation is the fastest path. You could also find current first (I = 400/800 = 0.5A) then use P = E×I (400 × 0.5 = 200W) — same answer.

### G5B04
**How many watts of electrical power are consumed by a 12 VDC light bulb that draws 0.2 amperes?**
- **A) 2.4 watts** ✅
- B) 24 watts
- C) 6 watts
- D) 60 watts

> Using P = E × I: 12V × 0.2A = 2.4 watts. This is the basic power formula — voltage times current gives power in watts. A small light bulb drawing 200 milliamps from a 12-volt source consumes 2.4 watts.

### G5B05
**How many watts are consumed when a current of 7.0 milliamperes flows through a 1,250-ohm resistance?**
- **A) Approximately 61 milliwatts** ✅
- B) Approximately 61 watts
- C) Approximately 11 milliwatts
- D) Approximately 11 watts

> Using P = I²R: (0.007A)² × 1250Ω = 0.000049 × 1250 = 0.06125 watts ≈ 61 milliwatts. First convert 7.0 milliamperes to 0.007 amperes. Then square the current and multiply by resistance. Watch the units — the answer is in milliwatts, not watts. Getting the metric prefix wrong is the trap here.

### G5B06
**What is the PEP produced by 200 volts peak-to-peak across a 50-ohm dummy load?**
- A) 1.4 watts
- **B) 100 watts** ✅
- C) 353.5 watts
- D) 400 watts

> PEP (Peak Envelope Power) uses the peak voltage, not peak-to-peak. For 200V peak-to-peak, the peak voltage is half: 100V. Then PEP = V_peak² / (2 × R) = 100² / (2 × 50) = 10,000 / 100 = 100 watts. Alternatively, convert to RMS first: V_RMS = V_peak / √2 = 100/1.414 = 70.7V, then P = V_RMS²/R = 5000/50 = 100W. Same answer either way.

### G5B07
**What value of an AC signal produces the same power dissipation in a resistor as a DC voltage of the same value?**
- A) The peak-to-peak value
- B) The peak value
- **C) The RMS value** ✅
- D) The reciprocal of the RMS value

> The RMS (Root Mean Square) value of an AC signal produces the same power dissipation as a DC voltage of equal value. RMS is the "equivalent heating value" — a 120V RMS AC signal heats a resistor exactly as much as 120V DC. This is why AC voltages are specified as RMS by default: your wall outlet is 120V RMS, which peaks at about 170V.

### G5B08
**What is the peak-to-peak voltage of a sine wave with an RMS voltage of 120 volts?**
- A) 84.8 volts
- B) 169.7 volts
- C) 240.0 volts
- **D) 339.4 volts** ✅

> To find peak-to-peak from RMS: first find peak voltage (V_peak = V_RMS × √2 = 120 × 1.414 = 169.7V), then double it for peak-to-peak (169.7 × 2 = 339.4V). The conversion chain is: RMS × 1.414 = peak, peak × 2 = peak-to-peak. So V_pp = V_RMS × 2.828. Your 120V RMS wall outlet actually swings 339 volts from positive peak to negative peak.

### G5B09
**What is the RMS voltage of a sine wave with a value of 17 volts peak?**
- A) 8.5 volts
- **B) 12 volts** ✅
- C) 24 volts
- D) 34 volts

> V_RMS = V_peak × 0.707 (which is 1/√2). So 17V peak × 0.707 = 12.02V ≈ 12 volts RMS. The 0.707 factor converts peak to RMS for sine waves. Going the other direction, multiply RMS by 1.414 to get peak. These conversion factors only apply to sine waves — other waveforms have different relationships.

### G5B10
**What percentage of power loss is equivalent to a loss of 1 dB?**
- A) 10.9 percent
- B) 12.2 percent
- **C) 20.6 percent** ✅
- D) 25.9 percent

> A loss of 1 dB equals approximately 20.6% power loss. Here's the math: the power ratio for 1 dB is 10^(1/10) = 1.259, so 1/1.259 = 0.794, meaning 79.4% of power remains — a 20.6% loss. This is useful for evaluating feed line loss: each dB of loss in your coax costs you about one-fifth of your power.

### G5B11
**What is the ratio of PEP to average power for an unmodulated carrier?**
- A) 0.707
- **B) 1.00** ✅
- C) 1.414
- D) 2.00

> For an unmodulated carrier, the ratio of PEP to average power is 1.00 — they're identical. An unmodulated carrier has constant amplitude, so the peak envelope power equals the average power. PEP only differs from average power when the signal's amplitude varies over time, as in SSB voice or AM. A steady CW carrier or FM signal has a PEP-to-average ratio of 1:1.

### G5B12
**What is the RMS voltage across a 50-ohm dummy load dissipating 1200 watts?**
- A) 173 volts
- **B) 245 volts** ✅
- C) 346 volts
- D) 692 volts

> Using P = V²/R, rearrange to V = √(P × R) = √(1200 × 50) = √60,000 = 244.9 ≈ 245 volts RMS. This is the RMS voltage because we used the average (RMS) power in the formula. If the question asked for peak voltage, you'd multiply by 1.414: 245 × 1.414 = 346V peak.

### G5B13
**What is the output PEP of an unmodulated carrier if the average power is 1060 watts?**
- A) 530 watts
- **B) 1060 watts** ✅
- C) 1500 watts
- D) 2120 watts

> For an unmodulated carrier, PEP equals average power — the ratio is 1:1. So if the average power is 1060 watts, the PEP is also 1060 watts. An unmodulated carrier is a constant-amplitude signal; there's no variation in the envelope, so peak and average are the same thing.

### G5B14
**What is the output PEP of 500 volts peak-to-peak across a 50-ohm load?**
- A) 8.75 watts
- **B) 625 watts** ✅
- C) 2500 watts
- D) 5000 watts

> For 500V peak-to-peak: V_peak = 500/2 = 250V. PEP = V_peak² / (2R) = 250² / (2 × 50) = 62,500 / 100 = 625 watts. Or equivalently, V_RMS = 250/√2 = 176.8V, then P = V_RMS²/R = 31,250/50 = 625W. Remember: PEP is always calculated from the peak voltage (not peak-to-peak), so divide peak-to-peak by 2 first.

## Group G5C — Resistors, capacitors, and inductors in series and parallel; transformers

### G5C01
**What causes a voltage to appear across the secondary winding of a transformer when an AC voltage source is connected across its primary winding?**
- A) Capacitive coupling
- B) Displacement current coupling
- **C) Mutual inductance** ✅
- D) Mutual capacitance

> A transformer works through mutual inductance — the changing magnetic field created by AC current in the primary winding induces a voltage in the secondary winding. No direct electrical connection is needed; the energy transfers through the shared magnetic field. This is why transformers only work with AC (or pulsating DC) — a steady DC current creates a constant magnetic field that can't induce voltage in the secondary.

### G5C02
**What is the output voltage if an input signal is applied to the secondary winding of a 4:1 voltage step-down transformer instead of the primary winding?**
- **A) The input voltage is multiplied by 4** ✅
- B) The input voltage is divided by 4
- C) Additional resistance must be added in series with the primary to prevent overload
- D) Additional resistance must be added in parallel with the secondary to prevent overload

> A 4:1 voltage step-down transformer has 4 times more turns on the primary than the secondary. If you reverse it — apply the signal to the secondary (fewer turns) — the transformer now steps UP by the same ratio: the output is 4 times the input. The turns ratio works both ways; reversing the input/output reverses the voltage transformation.

### G5C03
**What is the total resistance of a 10-, a 20-, and a 50-ohm resistor connected in parallel?**
- **A) 5.9 ohms** ✅
- B) 0.17 ohms
- C) 17 ohms
- D) 80 ohms

> For resistors in parallel, use the reciprocal formula: 1/R_total = 1/R₁ + 1/R₂ + 1/R₃ = 1/10 + 1/20 + 1/50 = 0.1 + 0.05 + 0.02 = 0.17. R_total = 1/0.17 = 5.88 ≈ 5.9 ohms. Notice that the total is always less than the smallest individual resistor. Parallel paths always reduce total resistance because current has more ways to flow.

### G5C04
**What is the approximate total resistance of a 100- and a 200-ohm resistor in parallel?**
- A) 300 ohms
- B) 150 ohms
- C) 75 ohms
- **D) 67 ohms** ✅

> For two resistors in parallel, there's a shortcut: R_total = (R₁ × R₂)/(R₁ + R₂) = (100 × 200)/(100 + 200) = 20,000/300 = 66.7 ≈ 67 ohms. This "product over sum" formula works for exactly two parallel resistors. The result is always less than the smaller resistor (67 < 100), which makes physical sense — adding a path reduces opposition.

### G5C05
**Why is the primary winding wire of a voltage step-up transformer usually a larger size than that of the secondary winding?**
- A) To improve the coupling between the primary and secondary
- **B) To accommodate the higher current of the primary** ✅
- C) To prevent parasitic oscillations due to resistive losses in the primary
- D) To ensure that the volume of the primary winding is equal to the volume of the secondary winding

> In a step-up transformer, the primary carries more current than the secondary (power in ≈ power out, so lower voltage side has higher current). Larger wire is needed to handle higher current without overheating. The secondary has higher voltage but less current, so it can use thinner wire. This is a direct consequence of conservation of energy: V₁×I₁ ≈ V₂×I₂.

### G5C06
**What is the voltage output of a transformer with a 500-turn primary and a 1500-turn secondary when 120 VAC is applied to the primary?**
- **A) 360 volts** ✅
- B) 120 volts
- C) 40 volts
- D) 25.5 volts

> Transformer voltage ratio equals turns ratio: V_out/V_in = N_secondary/N_primary = 1500/500 = 3. So V_out = 120V × 3 = 360 volts. This is a 1:3 step-up transformer — three times as many secondary turns means three times the output voltage (with proportionally less current).

### G5C07
**What transformer turns ratio matches an antenna’s 600-ohm feed point impedance to a 50-ohm coaxial cable?**
- **A) 3.5 to 1** ✅
- B) 12 to 1
- C) 24 to 1
- D) 144 to 1

> For impedance matching, the turns ratio equals the square root of the impedance ratio: N = √(Z₁/Z₂) = √(600/50) = √12 = 3.46 ≈ 3.5 to 1. Note that impedance ratio is the SQUARE of the turns ratio. A 3.5:1 turns ratio transforms impedance by 3.5² = 12.25:1, which maps 600Ω down to about 49Ω — close enough to 50Ω for a good match.

### G5C08
**What is the equivalent capacitance of two 5.0-nanofarad capacitors and one 750-picofarad capacitor connected in parallel?**
- A) 576.9 nanofarads
- B) 1,733 picofarads
- C) 3,583 picofarads
- **D) 10.750 nanofarads** ✅

> Capacitors in parallel simply add: C_total = C₁ + C₂ + C₃ = 5.0nF + 5.0nF + 750pF. First convert to the same unit: 750 pF = 0.75 nF. So C_total = 5.0 + 5.0 + 0.75 = 10.75 nF = 10,750 picofarads. Parallel capacitors add because you're increasing the total plate area — more area means more charge storage.

### G5C09
**What is the capacitance of three 100-microfarad capacitors connected in series?**
- A) 0.33 microfarads
- B) 3.0 microfarads
- **C) 33.3 microfarads** ✅
- D) 300 microfarads

> Capacitors in series use the reciprocal formula (same as resistors in parallel): 1/C_total = 1/100 + 1/100 + 1/100 = 3/100. C_total = 100/3 = 33.3 μF. For N identical capacitors in series, just divide one capacitor's value by N. Series capacitors always have LESS total capacitance than any individual capacitor.

### G5C10
**What is the inductance of three 10-millihenry inductors connected in parallel?**
- A) 0.30 henries
- B) 3.3 henries
- **C) 3.3 millihenries** ✅
- D) 30 millihenries

> Inductors in parallel use the reciprocal formula (same as resistors in parallel): 1/L_total = 1/10 + 1/10 + 1/10 = 3/10. L_total = 10/3 = 3.33 mH. Inductors behave like resistors: series values add directly, parallel values use the reciprocal formula. Three identical 10 mH inductors in parallel give 3.3 mH — not 30 mH (that would be series).

### G5C11
**What is the inductance of a circuit with a 20-millihenry inductor connected in series with a 50-millihenry inductor?**
- A) 7 millihenries
- B) 14.3 millihenries
- **C) 70 millihenries** ✅
- D) 1,000 millihenries

> Inductors in series simply add: L_total = L₁ + L₂ = 20 mH + 50 mH = 70 mH. This is just like resistors in series — the values add directly. Series inductors increase total inductance because you're extending the magnetic field through a longer coil path.

### G5C12
**What is the capacitance of a 20-microfarad capacitor connected in series with a 50-microfarad capacitor?**
- A) 0.07 microfarads
- **B) 14.3 microfarads** ✅
- C) 70 microfarads
- D) 1,000 microfarads

> Two capacitors in series: C_total = (C₁ × C₂)/(C₁ + C₂) = (20 × 50)/(20 + 50) = 1000/70 = 14.3 μF. Use the "product over sum" shortcut for two components. The result (14.3 μF) is less than the smaller capacitor (20 μF), confirming series capacitance is always reduced.

### G5C13
**Which of the following components should be added to a capacitor to increase the capacitance?**
- A) An inductor in series
- B) An inductor in parallel
- **C) A capacitor in parallel** ✅
- D) A capacitor in series

> To increase capacitance, add a capacitor in parallel. Parallel capacitors add: C_total = C₁ + C₂. Adding a capacitor in series would decrease the total capacitance (series capacitance is always less). Inductors don't add to capacitance at all. Think of it like adding more plate area — parallel = more area = more capacitance.

### G5C14
**Which of the following components should be added to an inductor to increase the inductance?**
- A) A capacitor in series
- B) A capacitor in parallel
- C) An inductor in parallel
- **D) An inductor in series** ✅

> To increase inductance, add an inductor in series. Series inductors add: L_total = L₁ + L₂. Adding an inductor in parallel would decrease the total inductance. Capacitors don't add to inductance. Think of it like extending a coil — series = longer coil = more inductance.
