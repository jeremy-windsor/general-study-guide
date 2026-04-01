# G7 — Practical Circuits
*3 questions on the exam from a pool of 38*

## Group G7A — Power supplies; schematic symbols

### G7A01
**What is the function of a power supply bleeder resistor?**
- A) It acts as a fuse for excess voltage
- **B) It discharges the filter capacitors when power is removed** ✅
- C) It removes shock hazards from the induction coils
- D) It eliminates ground loop current

> A bleeder resistor is connected across the filter capacitors in a power supply so that when you turn the supply off, the capacitors have a discharge path. Without it, those capacitors can hold a lethal charge for minutes or even hours — especially in high-voltage supplies used with vacuum tube amplifiers. The bleeder resistor slowly drains the stored energy to a safe level. It's a safety component, not a performance one. It doesn't act as a fuse, doesn't affect induction coils, and has nothing to do with ground loops.

### G7A02
**Which of the following components are used in a power supply filter network?**
- A) Diodes
- B) Transformers and transducers
- **C) Capacitors and inductors** ✅
- D) All these choices are correct

> The filter network in a power supply smooths the pulsating DC that comes out of the rectifier into something closer to pure DC. It uses capacitors and inductors — the capacitors charge up during voltage peaks and release energy during dips, while inductors resist sudden current changes, further smoothing the output. This is a direct application of G5 reactance concepts: capacitors pass AC ripple to ground (low reactance at ripple frequency) while inductors block it (high reactance at ripple frequency). Diodes are rectifiers, not filters. Transformers change voltage levels but don't filter.

### G7A03
**Which type of rectifier circuit uses two diodes and a center-tapped transformer?**
- **A) Full-wave** ✅
- B) Full-wave bridge
- C) Half-wave
- D) Synchronous

> A full-wave rectifier using a center-tapped transformer needs only two diodes. Here's how it works: the center tap provides a midpoint reference (ground). During one half of the AC cycle, current flows through the top half of the secondary and diode #1. During the other half, current flows through the bottom half and diode #2. Each diode handles one half-cycle, but the output sees BOTH halves — hence 'full-wave.' A full-wave bridge rectifier also produces full-wave output but uses four diodes and no center tap. A half-wave rectifier uses just one diode. Don't confuse the two full-wave types.

### G7A04
**What is characteristic of a half-wave rectifier in a power supply?**
- **A) Only one diode is required** ✅
- B) The ripple frequency is twice that of a full-wave rectifier
- C) More current can be drawn from the half-wave rectifier
- D) The output voltage is two times the peak input voltage

> A half-wave rectifier uses only one diode — that's its defining characteristic. The diode passes current during one half of the AC cycle and blocks it during the other half. This makes it the simplest possible rectifier circuit, but also the least efficient: half the input power is wasted. The ripple frequency equals the AC input frequency (not twice it — that's full-wave). Less current is available compared to full-wave designs, and the output voltage is NOT doubled. Half-wave rectifiers are used where simplicity matters more than performance — like low-current bias supplies.

### G7A05
**What portion of the AC cycle is converted to DC by a half-wave rectifier?**
- A) 90 degrees
- **B) 180 degrees** ✅
- C) 270 degrees
- D) 360 degrees

> A half-wave rectifier converts 180 degrees of the AC cycle — exactly one half. The diode conducts during the positive half-cycle (0° to 180°) and blocks during the negative half-cycle (180° to 360°). That's where the name comes from: half the wave gets through, half is discarded. Think of a full AC cycle as 360°: half-wave uses 180°, full-wave uses all 360°.

### G7A06
**What portion of the AC cycle is converted to DC by a full-wave rectifier?**
- A) 90 degrees
- B) 180 degrees
- C) 270 degrees
- **D) 360 degrees** ✅

> A full-wave rectifier converts 360 degrees — the entire AC cycle. Both the positive AND negative half-cycles contribute to the DC output. During the negative half, the rectifier circuit flips the polarity so it adds to the output rather than subtracting. Whether you use a center-tapped transformer with two diodes or a bridge with four diodes, the result is the same: every part of the input waveform contributes useful output. This doubles the ripple frequency compared to half-wave and produces smoother DC.

### G7A07
**What is the output waveform of an unfiltered full-wave rectifier connected to a resistive load?**
- **A) A series of DC pulses at twice the frequency of the AC input** ✅
- B) A series of DC pulses at the same frequency as the AC input
- C) A sine wave at half the frequency of the AC input
- D) A steady DC voltage

> An unfiltered full-wave rectifier produces DC pulses at TWICE the AC input frequency. Here's why: each half-cycle of the AC input produces one DC pulse. Since there are two half-cycles per full cycle, you get two pulses per AC cycle — double the frequency. If your AC input is 60 Hz, the unfiltered output has a 120 Hz ripple. This is actually an advantage of full-wave over half-wave: the higher ripple frequency is easier to filter out (capacitors and inductors are more effective at higher frequencies — remember X_C = 1/(2πfC) from G5). The output is NOT steady DC (that requires filtering) and NOT a sine wave (the negative halves have been flipped positive).

### G7A08
**Which of the following is characteristic of a switchmode power supply as compared to a linear power supply?**
- A) Faster switching time makes higher output voltage possible
- B) Fewer circuit components are required
- **C) High-frequency operation allows the use of smaller components** ✅
- D) Inherently more stable

> Switchmode power supplies operate at high frequency (typically 50 kHz to several MHz), and this high-frequency operation allows the use of much smaller transformers and filter components. From G5, we know that a transformer's ability to transfer power depends on the rate of change of current (higher frequency = faster changes). At 60 Hz, you need a big, heavy iron-core transformer. At 100 kHz, a tiny ferrite-core transformer does the same job. Same principle applies to filter capacitors and inductors — at higher frequencies, smaller values provide the same filtering effect. That's why your laptop charger is small and light while old-school linear supplies were heavy bricks.

### G7A09
**Which symbol in figure G7-1 represents a field effect transistor?**
- A) Symbol 2
- B) Symbol 5
- **C) Symbol 1** ✅
- D) Symbol 4

> Symbol 1 in Figure G7-1 represents a field-effect transistor (FET). The FET schematic symbol shows a channel with a gate electrode that doesn't directly touch it — reflecting the physical structure where the gate controls current flow through an electric field rather than direct contact. In a MOSFET, the gate is insulated by an oxide layer (as covered in G6). In a JFET, the gate is a reverse-biased junction. Either way, the symbol shows the gate offset from the channel. Look for the arrow on the gate or source to distinguish N-channel from P-channel.

### G7A10
**Which symbol in figure G7-1 represents a Zener diode?**
- A) Symbol 4
- B) Symbol 1
- C) Symbol 11
- **D) Symbol 5** ✅

> Symbol 5 in Figure G7-1 represents a Zener diode. The Zener symbol looks like a regular diode but with bent or 'kinked' ends on the bar (cathode). This distinguishes it from a standard rectifier diode, which has a straight bar. Zener diodes are designed to operate in reverse breakdown at a specific voltage — that's what makes them useful as voltage references and regulators. When reverse voltage reaches the Zener voltage, the diode conducts and clamps the voltage at that level. The bent cathode bar is the visual cue on schematics.

### G7A11
**Which symbol in figure G7-1 represents an NPN junction transistor?**
- A) Symbol 1
- **B) Symbol 2** ✅
- C) Symbol 7
- D) Symbol 11

> Symbol 2 in Figure G7-1 represents an NPN junction transistor. The BJT schematic symbol shows three leads: base, collector, and emitter. The key to identifying NPN vs PNP is the arrow on the emitter: in an NPN transistor, the arrow points AWAY from the base (outward — 'Not Pointing iN'). In a PNP, the arrow points inward toward the base. From G6, remember that BJTs in switching mode operate in saturation (ON) and cutoff (OFF). The NPN is the most common transistor type in amateur radio circuits.

### G7A12
**Which symbol in Figure G7-1 represents a solid core transformer?**
- A) Symbol 4
- B) Symbol 7
- **C) Symbol 6** ✅
- D) Symbol 1

> Symbol 6 in Figure G7-1 represents a solid-core (iron-core) transformer. A transformer symbol shows two coils (inductors) side by side — the primary and secondary windings. What distinguishes a solid-core transformer from an air-core transformer is the lines drawn between the coils: solid lines indicate a solid (iron or ferrite) core. An air-core transformer has no lines between the coils, or dashed lines. From G5, recall that transformers work through mutual inductance and are used for impedance matching and voltage transformation.

### G7A13
**Which symbol in Figure G7-1 represents a tapped inductor?**
- **A) Symbol 7** ✅
- B) Symbol 11
- C) Symbol 6
- D) Symbol 1

> Symbol 7 in Figure G7-1 represents a tapped inductor. A tapped inductor looks like a regular inductor symbol (a coil) but with an additional connection point partway along the winding. This tap lets you access a fraction of the total inductance, which is useful for impedance matching and tuning. It's like a center-tapped transformer secondary but with just one winding. Don't confuse it with a transformer (two separate coils) or a full inductor (no tap point).

## Group G7B — Digital circuits; flip-flops; counters; logic gates; programmable logic devices (PLDs); solid-state switches; LC and crystal oscillators

### G7B01
**What is the purpose of neutralizing an amplifier?**
- A) To limit the modulation index
- **B) To eliminate self-oscillations** ✅
- C) To cut off the final amplifier during standby periods
- D) To keep the carrier on frequency

> Neutralizing an amplifier eliminates self-oscillations. Self-oscillation happens when some of the amplifier's output feeds back to its input in phase — creating unintended positive feedback that makes the amplifier act like an oscillator instead of an amplifier. This is the same grid-to-plate capacitance problem that the screen grid addresses in vacuum tubes (from G6). Neutralization adds a deliberate canceling signal that's equal in amplitude but opposite in phase to the unwanted feedback. The result: the amplifier amplifies without oscillating. It has nothing to do with modulation index, standby control, or frequency stability.

### G7B02
**Which of these classes of amplifiers has the highest efficiency?**
- A) Class A
- B) Class B
- C) Class AB
- **D) Class C** ✅

> Class C has the highest efficiency of the standard amplifier classes — typically 60-80%. Here's the efficiency hierarchy: Class A (~25-50%) conducts 100% of the time but wastes a lot of power as heat. Class B (~50-65%) conducts 50% of the time. Class AB (between A and B) is a compromise. Class C conducts less than 50% of the time — the device is OFF for most of the cycle, only turning on for brief pulses. Less conduction time = less wasted power = higher efficiency. The tradeoff: Class C severely distorts the waveform, making it unsuitable for linear signals like SSB or AM. It's fine for FM and CW where amplitude doesn't carry information.

### G7B03
**Which of the following describes the function of a two-input AND gate?**
- A) Output is high when either or both inputs are low
- **B) Output is high only when both inputs are high** ✅
- C) Output is low when either or both inputs are high
- D) Output is low only when both inputs are high

> A two-input AND gate outputs HIGH only when BOTH inputs are HIGH. Think of it as a series circuit with two switches — current only flows when switch A AND switch B are both closed. The truth table is simple: 0+0=0, 0+1=0, 1+0=0, 1+1=1. Compare with OR (output high when EITHER input is high) and NAND (output high UNLESS both inputs are high — the inverse of AND). Digital logic gates are the building blocks of the counters, shift registers, and PLDs that appear in amateur radio equipment.

### G7B04
**In a Class A amplifier, what percentage of the time does the amplifying device conduct?**
- **A) 100%** ✅
- B) More than 50% but less than 100%
- C) 50%
- D) Less than 50%

> A Class A amplifier conducts 100% of the time — the amplifying device never turns off. It's biased at the center of its operating range, so the entire input waveform is reproduced faithfully at the output. This makes Class A the most linear amplifier class — it preserves the input waveform with minimal distortion. The tradeoff is efficiency: the device is always drawing current even with no signal, so at least half the DC input power is wasted as heat. Class A is used where signal quality matters more than efficiency — like low-level driver stages and audio preamplifiers.

### G7B05
**How many states does a 3-bit binary counter have?**
- A) 3
- B) 6
- **C) 8** ✅
- D) 16

> A 3-bit binary counter has 2³ = 8 states (0 through 7). Each bit can be 0 or 1, giving two possible values per bit. With 3 bits, you get 2 × 2 × 2 = 8 combinations: 000, 001, 010, 011, 100, 101, 110, 111. The pattern is always 2^N states for N bits. A 4-bit counter would have 16 states, an 8-bit counter 256 states. Binary counters are essential in frequency dividers, digital displays, and timing circuits found in amateur radio equipment.

### G7B06
**What is a shift register?**
- **A) A clocked array of circuits that passes data in steps along the array** ✅
- B) An array of operational amplifiers used for tri-state arithmetic operations
- C) A digital mixer
- D) An analog mixer

> A shift register is a clocked array of circuits that passes data in steps along the array. Each clock pulse shifts the data one position — like a bucket brigade where each person passes their bucket to the next. Shift registers are built from flip-flops connected in series. They're used for serial-to-parallel conversion (receiving serial data and outputting it in parallel), parallel-to-serial conversion, data buffering, and delay lines. They're fundamental components in digital communications equipment. They're NOT operational amplifiers, mixers, or arithmetic circuits.

### G7B07
**Which of the following are basic components of a sine wave oscillator?**
- A) An amplifier and a divider
- B) A frequency multiplier and a mixer
- C) A circulator and a filter operating in a feed-forward loop
- **D) A filter and an amplifier operating in a feedback loop** ✅

> A sine wave oscillator has two essential components: a filter and an amplifier operating in a feedback loop. The amplifier provides gain, and the filter determines the frequency by selecting which frequency gets positive feedback. When the loop gain at the filter's frequency equals exactly 1 and the phase shift is 0° (or 360°), the circuit sustains oscillation at that frequency. This is the Barkhausen criterion. LC oscillators use an LC tank circuit as the filter. Crystal oscillators use a quartz crystal (which behaves like an extremely selective LC circuit). Without the feedback loop, you just have an amplifier. Without the filter, you'd get noise, not a sine wave.

### G7B08
**How is the efficiency of an RF power amplifier determined?**
- A) Divide the DC input power by the DC output power
- **B) Divide the RF output power by the DC input power** ✅
- C) Multiply the RF input power by the reciprocal of the RF output power
- D) Add the RF input power to the DC output power

> RF power amplifier efficiency is calculated by dividing the RF output power by the DC input power. Efficiency = P_RF_out / P_DC_in × 100%. If your amplifier draws 500W from the power supply and delivers 300W of RF, its efficiency is 300/500 = 60%. The remaining 200W becomes heat — which is why amplifiers need heatsinks or fans. Higher efficiency means less wasted heat and a smaller power supply requirement. This is why Class C (60-80% efficient) is preferred over Class A (25-50%) when linearity isn't needed.

### G7B09
**What determines the frequency of an LC oscillator?**
- A) The number of stages in the counter
- B) The number of stages in the divider
- **C) The inductance and capacitance in the tank circuit** ✅
- D) The time delay of the lag circuit

> The frequency of an LC oscillator is determined by the inductance and capacitance in the tank circuit — using the resonant frequency formula from G5: f = 1/(2π√(LC)). The tank circuit resonates at a specific frequency where inductive and capacitive reactance are equal (X_L = X_C), and that's the frequency the oscillator produces. Change L or C and you change the frequency. This is how variable-frequency oscillators (VFOs) work: a variable capacitor tunes the frequency by changing C in the tank circuit. Crystal oscillators use the crystal's equivalent LC values for extreme stability.

### G7B10
**Which of the following describes a linear amplifier?**
- A) Any RF power amplifier used in conjunction with an amateur transceiver
- **B) An amplifier in which the output preserves the input waveform** ✅
- C) A Class C high efficiency amplifier
- D) An amplifier used as a frequency multiplier

> A linear amplifier is one where the output preserves the input waveform — the output is an amplified but faithful copy of the input. 'Linear' means the output is directly proportional to the input at all amplitude levels. This is essential for SSB and AM signals where the amplitude carries information — any distortion of the waveform creates splatter (unwanted sideband energy that interferes with adjacent channels). Class A and Class AB amplifiers are linear. Class C is NOT linear — it clips the waveform severely. A frequency multiplier is the opposite of linear — it deliberately distorts the signal to generate harmonics.

### G7B11
**For which of the following modes is a Class C power stage appropriate for amplifying a modulated signal?**
- A) SSB
- **B) FM** ✅
- C) AM
- D) All these choices are correct

> Class C is appropriate for amplifying FM signals because FM carries information in frequency changes, not amplitude changes. Since the amplitude of an FM signal is constant (it doesn't matter if the peaks get clipped), Class C's severe waveform distortion doesn't lose any information. The tuned output circuit of the Class C amplifier reconstructs the sine wave at the fundamental frequency. For SSB and AM, amplitude carries the information, so Class C's clipping would destroy the signal. That's why SSB transmitters use Class AB amplifiers — they're less efficient but preserve the amplitude envelope.

## Group G7C — Receivers and transmitters;டlow-noise amplifiers; IF; mixing; oscillators; phase-locked loops; DSP; SDR fundamentals

### G7C01
**What circuit is used to select one of the sidebands from a balanced modulator?**
- A) Carrier oscillator
- **B) Filter** ✅
- C) IF amplifier
- D) RF amplifier

> A filter selects one sideband from the output of a balanced modulator. The balanced modulator produces a double-sideband suppressed-carrier (DSB-SC) signal — both sidebands but no carrier. To get a single-sideband (SSB) signal, you need to remove one of the sidebands. A crystal or mechanical filter does this by having a very narrow passband that includes only the desired sideband while rejecting the other. The carrier oscillator generates the carrier frequency, the IF amplifier boosts the signal, and the RF amplifier handles the final output — but it's the filter that performs the sideband selection.

### G7C02
**What output is produced by a balanced modulator?**
- A) Frequency modulated RF
- B) Audio with equalized frequency response
- C) Audio extracted from the modulation signal
- **D) Double-sideband modulated RF** ✅

> A balanced modulator produces double-sideband (DSB) modulated RF with the carrier suppressed. It combines the audio signal with the carrier such that the carrier itself cancels out, leaving only the upper and lower sidebands. This is the first step in generating an SSB signal. The 'balanced' part refers to the circuit's symmetry, which causes the carrier to cancel. The output is NOT FM (that requires a different modulation method), NOT extracted audio (that's demodulation), and NOT equalized audio (that's an audio processing function). After the balanced modulator, a filter selects one sideband to complete the SSB generation process.

### G7C03
**What is one reason to use an impedance matching transformer at a transmitter output?**
- A) To minimize transmitter power output
- **B) To present the desired impedance to the transmitter and feed line** ✅
- C) To reduce power supply ripple
- D) To minimize radiation resistance

> An impedance matching transformer at a transmitter output presents the desired impedance to both the transmitter and the feed line. From G5, you know that maximum power transfer occurs when impedances are matched, and mismatched impedances cause reflections (high SWR). If your antenna feed line is 50 ohms but the transmitter output stage wants to see a different impedance, a matching transformer bridges the gap using the turns ratio relationship: Z_ratio = (N₁/N₂)². The goal is NOT to minimize power output, reduce ripple, or minimize radiation resistance — it's to ensure efficient power transfer by presenting the right impedance to each side of the connection.

### G7C04
**How is a product detector used?**
- A) Used in test gear to detect spurious mixing products
- B) Used in transmitter to perform frequency multiplication
- C) Used in an FM receiver to filter out unwanted sidebands
- **D) Used in a single sideband receiver to extract the modulated signal** ✅

> A product detector is used in an SSB receiver to extract the modulated signal. SSB signals have no carrier — the carrier was suppressed during transmission. To demodulate SSB, the receiver must reinsert a replacement carrier (called the beat frequency oscillator or BFO) and mix it with the received signal. The product detector does this mixing. Without a product detector (or equivalent), an SSB signal sounds like unintelligible quacking. The term 'product' comes from the mathematical operation — multiplying (taking the product of) two signals. It's not test equipment, not a frequency multiplier, and not an FM filter.

### G7C05
**Which of the following is characteristic of a direct digital synthesizer (DDS)?**
- A) Extremely narrow tuning range
- B) Relatively high-power output
- C) Pure sine wave output
- **D) Variable output frequency with the stability of a crystal oscillator** ✅

> A direct digital synthesizer (DDS) produces a variable output frequency with the stability of a crystal oscillator. A DDS works by using a digital counter and lookup table to generate a sine wave sample-by-sample, clocked by a crystal oscillator reference. Since every output frequency is derived from the same crystal reference, they all share its stability. The frequency can be changed almost instantaneously by changing a digital value — no mechanical tuning or PLL lock time needed. DDS does NOT have a narrow tuning range (it can cover a wide range), doesn't produce high power (it's a signal source, not an amplifier), and the output isn't a perfectly pure sine wave (it has quantization artifacts that need filtering).

### G7C06
**Which of the following is an advantage of a digital signal processing (DSP) filter compared to an analog filter?**
- **A) A wide range of filter bandwidths and shapes can be created** ✅
- B) Fewer digital components are required
- C) Mixing products are greatly reduced
- D) The DSP filter is much more effective at VHF frequencies

> The key advantage of DSP (Digital Signal Processing) filters over analog filters is that a wide range of filter bandwidths and shapes can be created — all in software. An analog filter is fixed by its physical components: changing bandwidth means swapping crystals or adjusting LC networks. A DSP filter is just math — change the algorithm's parameters and you instantly have a different bandwidth, different shape factor, or even a completely different filter type (low-pass, band-pass, notch). Modern SDR transceivers exploit this to give operators continuously variable bandwidth — something that's impractical with analog filters. DSP doesn't reduce mixing products, isn't more effective at VHF, and doesn't use fewer components.

### G7C07
**What term specifies a filter’s attenuation inside its passband?**
- **A) Insertion loss** ✅
- B) Return loss
- C) Q
- D) Ultimate rejection

> Insertion loss specifies a filter's attenuation inside its passband — the amount of desired signal that's lost just by passing through the filter. An ideal filter would have zero insertion loss (no signal lost in the passband) and infinite rejection outside it. Real filters always lose something. Insertion loss of 1-2 dB is typical for a good crystal filter. Return loss measures reflected power (related to impedance matching). Q describes a component's or circuit's selectivity. Ultimate rejection is the maximum attenuation outside the passband. Know all four terms, but insertion loss is specifically about loss INSIDE the passband.

### G7C08
**Which parameter affects receiver sensitivity?**
- A) Input amplifier gain
- B) Demodulator stage bandwidth
- C) Input amplifier noise figure
- **D) All these choices are correct** ✅

> All three factors — input amplifier gain, demodulator bandwidth, and input amplifier noise figure — affect receiver sensitivity. Sensitivity is about detecting weak signals, and weak signals must compete with noise. The noise figure tells you how much noise the amplifier adds (lower is better). The gain determines how much the signal gets boosted. The bandwidth determines how much noise enters the system (wider bandwidth = more noise). Together, these determine the minimum detectable signal (MDS). This is why narrowing your IF filter bandwidth improves sensitivity — you're reducing the noise that competes with the signal.

### G7C09
**What is the phase difference between the I and Q RF signals that software-defined radio (SDR) equipment uses for modulation and demodulation?**
- A) Zero
- **B) 90 degrees** ✅
- C) 180 degrees
- D) 45 degrees

> The I and Q signals in SDR (Software-Defined Radio) are 90 degrees apart in phase. I stands for In-phase and Q stands for Quadrature (which literally means 'quarter turn' = 90°). By sampling the incoming RF at two points exactly 90° apart, the SDR captures complete information about both the amplitude and phase of the signal. This is critical because a single sample stream can't distinguish between positive and negative frequencies (images). The 90° I/Q pair eliminates this ambiguity. Without the quadrature relationship, SDR demodulation wouldn't work correctly.

### G7C10
**What is an advantage of using I-Q modulation with software-defined radios (SDRs)?**
- A) The need for high resolution analog-to-digital converters is eliminated
- **B) All types of modulation can be created with appropriate processing** ✅
- C) Minimum detectible signal level is reduced
- D) Automatic conversion of the signal from digital to analog

> The advantage of I/Q modulation in SDRs is that all types of modulation can be created with appropriate processing. Because I/Q represents the signal completely — both amplitude and phase at every instant — you can mathematically construct any modulation scheme: AM, FM, SSB, PSK, QAM, or anything else. It's a universal modulation/demodulation framework. Change the software algorithm and you change the modulation type — no hardware changes needed. This is the fundamental power of SDR: the radio's capabilities are defined by software rather than fixed hardware. I/Q doesn't eliminate the need for ADCs (it requires them), doesn't reduce minimum signal level, and doesn't automatically convert digital to analog.

### G7C11
**Which of these functions is performed by software in a software-defined radio (SDR)?**
- A) Filtering
- B) Detection
- C) Modulation
- **D) All these choices are correct** ✅

> In a software-defined radio, ALL of the listed functions — filtering, detection, and modulation — are performed by software. That's the entire point of SDR: replace dedicated hardware circuits with software algorithms running on a processor. Traditional radios use physical crystal filters, diode detectors, and balanced modulators. An SDR does the same jobs mathematically. The hardware is reduced to an antenna, an analog-to-digital converter (ADC), and a processor. Everything between the ADC and the speaker/display is software. This makes SDRs incredibly flexible — update the software and you've upgraded your radio.

### G7C12
**What is the frequency above which a low-pass filter’s output power is less than half the input power?**
- A) Notch frequency
- B) Neper frequency
- **C) Cutoff frequency** ✅
- D) Rolloff frequency

> The cutoff frequency is the frequency above which a low-pass filter's output power drops below half the input power. This is also called the -3 dB point (from G5: a 3 dB loss = half power). Below the cutoff frequency, signals pass through with minimal loss. Above it, signals are increasingly attenuated. The cutoff frequency defines the boundary of the filter's passband. It's not the notch frequency (that's for a band-stop filter), not the neper frequency (a rarely-used attenuation unit), and rolloff describes the steepness of attenuation beyond cutoff, not the cutoff point itself.

### G7C13
**What term specifies a filter’s maximum ability to reject signals outside its passband?**
- A) Notch depth
- B) Rolloff
- C) Insertion loss
- **D) Ultimate rejection** ✅

> Ultimate rejection specifies a filter's maximum ability to reject signals outside its passband. It's the deepest attenuation the filter can achieve — the floor of the stopband. For example, a crystal filter might have 80 dB of ultimate rejection, meaning signals far from the passband are reduced by a factor of 100 million. Insertion loss is about loss INSIDE the passband (the opposite concept). Rolloff describes how quickly attenuation increases at the passband edges. Notch depth applies to notch (band-reject) filters specifically, not to the general stopband performance of any filter.

### G7C14
**The bandwidth of a band-pass filter is measured between what two frequencies?**
- **A) Upper and lower half-power** ✅
- B) Cutoff and rolloff
- C) Pole and zero
- D) Image and harmonic

> A band-pass filter's bandwidth is measured between the upper and lower half-power points (-3 dB points). These are the frequencies where the output power drops to half the peak passband power. The bandwidth is simply the difference: BW = f_upper - f_lower. For example, if a filter passes signals from 9.000 MHz to 9.003 MHz at the half-power points, its bandwidth is 3 kHz — typical for an SSB crystal filter. This connects to the receiver sensitivity concept in G7C08: narrower bandwidth means less noise and better sensitivity for narrow-band signals.
