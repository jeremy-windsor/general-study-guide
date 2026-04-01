# G4 — Amateur Radio Practices

This subelement is where everything comes together. You've learned about regulations (G1), operating procedures (G2), propagation (G3), electrical principles (G5), components (G6), circuits (G7), signals (G8), and antennas (G9). Now it's time to actually set up and run a station — dealing with the real-world problems that come with putting all those pieces together.

G4 covers five groups: station setup, test equipment, interference and grounding, speech processing and S meters, and mobile/alternative energy installations. You'll see **5 questions** on your exam from a pool of 60, making this tied for the biggest exam weight. The good news is that most of these questions test practical knowledge — the kind of thing that makes sense once you understand what's actually happening in the shack.

---

## Station Setup: Making Your Rig Work Right

### Receiver Controls That Actually Matter

Modern HF transceivers have a dizzying array of knobs, buttons, and menus. The exam focuses on a handful that you'll use constantly:

**The Notch Filter** removes a single interfering carrier. Imagine you're listening to a QSO on 14.250 MHz and there's an annoying steady tone — an unmodulated carrier sitting right in the middle of the passband. The notch filter is a surgically narrow, deep rejection filter you can tune to that exact frequency and eliminate it without affecting the signal you're trying to hear. It's a sniper rifle, not a shotgun — it takes out one specific carrier and leaves everything else alone.

**The Noise Blanker** handles a completely different kind of interference: impulse noise from sources like ignition systems, electric fences, and power line arcing. These create extremely short bursts that are broad in frequency. The noise blanker detects these spikes and briefly reduces receiver gain during each pulse — essentially muting the receiver for a microsecond. Your brain fills in the gap, and the noise vanishes.

**Noise Reduction** (DSP-based in modern rigs) works differently — it uses algorithms to separate signal from noise. But there's a catch: push the noise reduction level too high and the algorithm starts distorting the desired signal too. Use only as much as you need.

**The Receive Attenuator** pads down all incoming signals when they're strong enough to overload the receiver's front end. If you're near a high-power station or have a big antenna, incoming signals can overdrive the first mixer, creating phantom signals and intermodulation products. The attenuator (-10, -20, or -30 dB) brings everything down to a manageable level. Think of it as sunglasses for your receiver.

**Reverse Sideband for CW**: When receiving CW with an interfering signal nearby, switching from the normal sideband to the opposite sideband moves the BFO to the other side of the IF passband. This shifts which signals fall inside your passband, potentially moving the interferer out while keeping the desired signal in.

### The Dual-VFO and Split Operation

The dual-VFO feature lets you transmit on one frequency and listen on another — called "split" operation. This is essential for working DX stations who transmit on one frequency but listen "up" or "down." Set VFO-A to hear the DX station, set VFO-B to transmit where they're listening. You're not transmitting on two frequencies simultaneously — you're just separating your transmit and receive frequencies.

### Tube Amplifier Tuning

Even if you never touch a vacuum tube amplifier, the exam expects you to know the basics:

**The TUNE (PLATE) control** adjusts the plate tank circuit to resonance. You're looking for a **pronounced dip** in plate current. At resonance, the tank circuit's impedance is maximum, so minimum current flows through the tube for a given RF output — the dip tells you you're at the sweet spot. A current peak means you're way off resonance, wasting power as heat. This is the same resonance principle from G5A applied to a real circuit.

**The LOAD (COUPLING) control** adjusts how tightly the tank circuit couples to the antenna. Increase coupling for more power output, but watch the plate current meter — don't exceed the tube's maximum rated current. The procedure: dip plate current with TUNE, increase LOAD for desired output, re-dip TUNE, and iterate.

### ALC: The Amplifier's Governor

Automatic Level Control (ALC) prevents excessive drive to an RF power amplifier. When drive is too high, the amplifier saturates and produces distortion, splatter, and harmonics. ALC is a feedback loop — the amplifier sends a control voltage back to the exciter saying "turn it down." It's crucial for clean voice operation.

**But ALC must be inactive when transmitting AFSK data signals.** Here's why: AFSK uses constant-amplitude audio tones. The transmitter should produce a constant-envelope output. ALC is designed for voice dynamics — when it reacts to constant-level AFSK tones, it creates gain variations that distort the waveform and generate intermodulation products. The fix: set drive low enough that ALC never activates during data operation.

### Amplifier Keying Delay

When your transceiver keys an external amplifier, there's a deliberate delay before RF output begins. This gives the amplifier's T/R relay time to switch the antenna from the receiver input to the amplifier output. Without this delay, RF power would be applied while the relay is still moving — potentially sending power back into the transceiver's receiver or arcing across relay contacts.

### The Electronic Keyer

An electronic keyer automatically generates properly timed dots and dashes for CW operation. You squeeze a paddle and the keyer handles the timing — dot length, dash length (3× dot), inter-element spacing. It produces clean, consistent CW at any speed without manual timing of each element.

---

## Test Equipment: Measuring What Matters

### The Oscilloscope

The oscilloscope is the king of test equipment for radio work, and the exam wants you to know why. An oscilloscope contains horizontal and vertical channel amplifiers — the vertical amplifier displays the signal magnitude, the horizontal drives the time base. Together they create a voltage-versus-time display that shows you the **shape** of waveforms.

A digital voltmeter gives you a number. An oscilloscope shows you the complete waveform: rise times, overshoot, distortion, modulation envelopes, noise riding on signals. That's why it's the best instrument for:

- **Checking CW keying waveform** — you can see whether the transitions are smooth (good) or abrupt (causes key clicks)
- **Checking RF envelope patterns** — connect the attenuated RF output of the transmitter to the vertical input and observe the modulation envelope

When checking transmitted RF, connect an **attenuated** sample of the transmitter output. You cannot connect 100 watts directly to a scope input — you'd destroy it. Use a directional coupler or resistive tap.

### The Two-Tone Test

The two-tone test is the definitive test of SSB transmitter **linearity**. You feed two non-harmonically related audio signals (typically around 700 Hz and 1900 Hz) into the transmitter's microphone input and observe the output on an oscilloscope.

Why non-harmonically related? Because if the tones were harmonics of each other, the intermodulation products would fall at the same frequencies as the test tones, making them impossible to measure. With non-harmonically related tones, intermod products appear at different, predictable frequencies.

A perfectly linear transmitter produces an output containing only the two original tones. Nonlinearity creates extra signals (intermodulation products) that appear as distortion in the envelope pattern on the scope. This is critical because nonlinearity causes splatter — the wide, messy signals that interfere with adjacent channels.

### Multimeters: Digital vs. Analog

A **digital multimeter** wins on precision — it displays exact numbers (4.372V, not "about 4.3"). A **analog multimeter** wins when you're adjusting circuits for a peak or null — the moving needle gives instant visual feedback about direction and rate of change. You can see the needle swinging toward the peak as you turn a knob. A digital display just flickers between numbers.

**Voltmeter input impedance**: Voltmeters have high input impedance (typically 10 MΩ) to avoid loading the circuit being measured. If the meter draws significant current, it changes the voltage you're trying to measure — the act of measuring changes the result.

### Directional Wattmeters and Antenna Analyzers

A **directional wattmeter** measures forward and reflected power on a feed line. From those two numbers, you can calculate SWR. It's the practical instrument behind the SWR concepts from G9B.

An **antenna analyzer** generates its own test signal and measures impedance — it doesn't need a transmitter connected. Connect it to your antenna and feed line (that's what you're measuring), and it tells you SWR, impedance, and resonant frequency. It can also measure the impedance of coaxial cable. It cannot measure antenna gain, front-to-back ratio, or transmitter power.

**Caution**: Strong signals from nearby transmitters can corrupt antenna analyzer readings by injecting received power that interferes with the analyzer's own test signal. Make your measurements when nearby stations aren't transmitting.

---

## Interference, Grounding, and Shielding

This is where your station interacts (sometimes badly) with the world around it. Understanding interference mechanisms and grounding is essential for both the exam and real-world operation.

### RF Interference to Consumer Electronics

When your SSB signal gets into a neighbor's audio equipment, the semiconductor junctions in their device act as crude detectors, rectifying your RF and recovering the modulation. The result:

- **From an SSB transmitter**: Distorted speech — recognizable but garbled
- **From a CW transmitter**: On-and-off humming or clicking matching the keying rhythm

The fix: **bypass capacitors** provide a low-impedance path to ground for RF frequencies while being invisible at audio frequencies. This works because capacitive reactance decreases with frequency (X_C = 1/2πfC, from G5A) — at RF, a small cap is essentially a short to ground.

**Broadband interference** (covering a wide range of frequencies) is usually caused by arcing at a poor electrical connection — a loose connection on a power line, corroded antenna connector, or bad switch contact. An electrical arc is essentially an unintentional spark-gap transmitter.

### Common-Mode Current

When RF rides on the outside of cable shields or equally on both conductors — instead of being contained inside the cable — that's common-mode current. A **ferrite choke** (snap-on bead or toroidal core) on the cable presents high impedance to common-mode RF without affecting the desired signal inside. This is the same principle behind baluns and common-mode chokes on antenna feed lines from G9B.

### Grounding: The Big Three Problems

**Problem 1: Resonant Ground Connections.** If your ground wire happens to be a resonant length (like a quarter wavelength on your operating frequency), it presents high impedance instead of low impedance. RF current through a high-impedance ground wire creates high voltages on your equipment chassis — touch it and you get an RF burn. The fix: keep ground leads short (much less than a quarter wavelength) and use multiple ground paths.

**Problem 2: Ground Loops.** When multiple paths to ground create a loop, that loop acts as an antenna for induced currents — especially 60 Hz hum from AC wiring. If hum gets into your audio path, other stations hear buzzing on your signal. The fix: **bond all equipment enclosures together** with short, heavy conductors to a single common ground bus, then run one conductor to the ground rod. No loops, no hum.

**Problem 3: RF Hot Spots.** When equipment chassis are at different RF potentials, touching two pieces of equipment simultaneously completes the circuit through your body. The fix: again, **bonding** — connecting all metal enclosures together ensures everything is at the same RF potential.

### Safety Grounding

All metal enclosures must be grounded to ensure hazardous voltages can't appear on the chassis. If an internal component fails and a hot wire contacts the chassis, the ground path provides low resistance to earth, tripping the breaker immediately instead of waiting for someone to touch the chassis and complete the circuit through their body.

**Lightning protection**: Don't use solder on ground connections. Lightning carries tens of thousands of amps — the heat will melt solder joints instantly. Use crimped, clamped, or brazed connections that survive the thermal shock.

---

## Speech Processors and S Meters

### Speech Processing

A speech processor increases the **apparent loudness** of your transmitted voice by compressing the dynamic range — quiet parts come up, loud parts get limited. Your peak power stays the same, but **average power increases** significantly. Since S meters respond more to average power than peaks, the receiving station sees a stronger signal.

Used correctly, a speech processor can make a 100-watt station sound like 400 watts. Used incorrectly, it produces:
- Distorted speech
- Excess intermodulation products (splatter)
- Excessive background noise (the compressor amplifies everything between words)

All three happen when the processor is set too aggressively — more processing is not always better.

### S Meters and Decibels

The S meter measures received signal strength. Below S9, each S-unit represents approximately **6 dB** of signal change. Above S9, readings switch to direct dB notation (e.g., "20 dB over S9").

The practical math:
- **One S-unit = 6 dB = 4× power change**. To go from S8 to S9, you need approximately 4 times the power output. Running 25 watts and want to be S9 instead of S8? You need 100 watts. This is why antenna improvements (G9) often beat raw power.
- **20 dB over S9 = 100× more powerful** than an S9 signal. This uses the same dB-to-power relationship from G5B: every 10 dB = 10× power, so 20 dB = 100×.

### Sideband and Band Edges

Four questions (G4D08-G4D11) all test the same concept: **know which direction your sideband extends and don't transmit outside your authorized frequencies.**

- **LSB extends BELOW the displayed carrier frequency.** A 3 kHz LSB signal at 7.178 MHz occupies 7.175–7.178 MHz.
- **USB extends ABOVE the displayed carrier frequency.** A 3 kHz USB signal at 14.347 MHz occupies 14.347–14.350 MHz.

The rules follow logically:
- When using LSB, your carrier must be at least **3 kHz above** the lower band edge (room below for the sideband to extend into)
- When using USB, your carrier must be at least **3 kHz below** the upper band edge (room above for the sideband)

This connects directly to the USB/LSB conventions covered in G2A — below 10 MHz you use LSB, above 10 MHz you use USB.

---

## HF Mobile and Alternative Energy

### Mobile Antenna Challenges

The biggest limitation of an HF mobile installation is **antenna efficiency**. A full-size 40-meter quarter-wave vertical is about 33 feet — you can't put that on a car. Mobile antennas are physically shortened and use loading coils to compensate. The tradeoffs:

- **Reduced efficiency** — a shortened antenna might radiate only 10-50% of input power, the rest lost as heat in the loading coil
- **Very narrow bandwidth** — high Q from the loading coil means you might get only 20-50 kHz of usable bandwidth before needing to retune
- **Lower radiation resistance** — making the antenna more sensitive to ground system losses

Two devices help with shortened mobile antennas:
- A **capacitance hat** (radial wires or disk at the top) electrically lengthens the antenna without adding physical height
- A **corona ball** at the tip reduces RF voltage discharge — at high power with a high-Q coil, tip voltages can reach several thousand volts, and a sharp point would ionize the surrounding air

### Mobile Power

A 100-watt HF transceiver draws about 20-22 amps at 13.8V on transmit. This requires:
- **Heavy-gauge wire directly to the battery** — not the alternator (voltage fluctuates with RPM), not the cigarette lighter socket (wired for maybe 10-15 amps max)
- **Fusing** — a short circuit in 20 amps of unfused wire starts fires
- The battery acts as a massive filter capacitor, smoothing alternator noise

All vehicle systems — charging, fuel injection, and control computers — can cause receive interference. Modern vehicles are rolling RF noise generators.

### Solar Panels

Individual solar cells produce approximately **0.5 VDC** each (set by the silicon bandgap). Cells are connected in **series-parallel** within a panel — series strings build voltage, parallel strings increase current capacity. A 12V nominal panel typically uses 36 cells in series (36 × 0.5V = 18V open-circuit, dropping to ~14V under load).

A **series diode** between panel and battery prevents the battery from discharging backward through the panel at night when panel voltage drops below battery voltage. It's a one-way valve for current.

For **lithium iron phosphate (LiFePO4) batteries**, a charge controller is mandatory — not optional. LiFePO4 cells require precise voltage regulation and can be damaged or become dangerous if overcharged. A simple blocking diode provides no voltage regulation. The charge controller implements the proper charging profile (constant current → constant voltage → float) and protects the battery.

---

## Study Strategy for G4

This subelement rewards practical understanding. The questions test whether you know:

1. **What each station control does** — notch filter vs. noise blanker vs. attenuator vs. noise reduction
2. **Which test instrument measures what** — oscilloscope for waveforms, DMM for precision, analog meter for peaking/nulling
3. **How interference works and how to fix it** — bypass caps for RF, ferrite chokes for common mode, bonding for ground issues
4. **The math behind S meters** — 6 dB per S-unit, 4× power per S-unit, dB-to-power conversions
5. **Sideband direction** — LSB goes down, USB goes up, stay within band edges
6. **Mobile and solar basics** — shortened antenna limitations, direct battery connection, charge controllers for lithium

The concepts connect directly to material from G5 (impedance, reactance), G7 (receiver circuits), G8 (modulation), and G9 (antennas and SWR). If you've studied those subelements first, G4 is where it all clicks into practical application.
