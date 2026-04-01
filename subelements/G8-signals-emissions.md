# G8 — Signals and Emissions

This subelement is where you learn how information actually rides on radio waves. G5 gave you the electrical theory — impedance, reactance, power calculations. G7 showed you the circuits — modulators, mixers, filters, oscillators. Now G8 connects the dots: how those circuits create, shape, and process the signals that carry your voice, data, and digital modes across the bands. You'll see 3 questions on your exam drawn from a pool of 43.

If G5 was the physics and G7 was the plumbing, G8 is what flows through the pipes.

---

## Modulation: How Information Gets On the Wave

An unmodulated RF carrier is useless for communication — it's just a steady sine wave. Modulation is the process of varying some property of that carrier to encode information. There are three properties you can change:

1. **Amplitude** → Amplitude Modulation (AM)
2. **Frequency** → Frequency Modulation (FM)
3. **Phase** → Phase Modulation (PM)

Every modulation scheme in amateur radio is a variation on one (or more) of these three.

### Amplitude Modulation (AM)

AM varies the instantaneous power level of the RF signal. When the audio goes positive, the carrier amplitude goes up (more power). When the audio goes negative, the amplitude goes down (less power). The resulting waveform has an **envelope** — if you draw a line connecting the positive peaks of the modulated signal, that line traces out the audio waveform. This is the **modulation envelope**, and it's how an AM detector works: it simply extracts the envelope.

Conventional AM transmits the carrier plus both sidebands — upper sideband (USB) and lower sideband (LSB). This is inefficient because at least half the transmitter power goes into the carrier, which carries no information. The actual information is entirely in the sidebands.

#### Single Sideband (SSB)

SSB solves AM's efficiency problem by transmitting only ONE sideband and suppressing both the carrier and the other sideband. From G7, recall that a balanced modulator produces double-sideband suppressed-carrier (DSB-SC) signal, and then a filter selects one sideband. The result: all your transmitter power goes into the information-carrying sideband.

SSB uses the **narrowest bandwidth** of any phone emission — about 2.4 kHz. Compare that to conventional AM (~6 kHz), vestigial sideband (more than SSB), or FM (10-16 kHz). This narrow bandwidth is why SSB dominates HF voice: more stations fit in the band, and the concentrated power punches through noise better.

### Frequency Modulation (FM)

FM varies the instantaneous frequency of the carrier. When the audio goes positive, the frequency increases; when it goes negative, the frequency decreases. The amount of frequency shift — called **deviation** — is proportional to the audio amplitude. The rate of frequency shift follows the audio frequency.

FM's big advantage: it's resistant to amplitude noise. Since the information is in the frequency changes, not the amplitude, the receiver can hard-limit the signal (clip all amplitude variations) without losing any information. This is why FM sounds so clean on VHF/UHF — the limiter stage strips off electrical noise, atmospheric static, and ignition interference.

### Phase Modulation (PM)

PM changes the phase angle of the carrier. It's closely related to FM — varying the phase necessarily affects the instantaneous frequency, and varying the frequency necessarily affects the phase. The difference is subtle: a reactance modulator connected to an **oscillator** produces FM (it pulls the oscillator frequency). The same reactance modulator connected to an **RF amplifier stage** produces PM (it shifts the phase of the signal passing through without changing the oscillator frequency).

This distinction matters for the exam: a reactance modulator on an RF amplifier stage = phase modulation.

### Overmodulation and Flat-Topping

Overmodulation is what happens when you push any modulation scheme too hard. The result is always the same: **excessive bandwidth**. The distorted signal splatters energy into adjacent frequencies, interfering with other stations.

In AM/SSB, overmodulation causes **flat-topping** — the peaks of the modulation envelope get clipped flat because the amplifier has run out of headroom. On an oscilloscope, the envelope has flat tops instead of rounded peaks. On a waterfall display, you see vertical lines flanking the signal (spurious emissions spreading into adjacent frequencies).

Flat-topping is caused by excessive drive or speech levels — too much mic gain, too much speech processor compression, or insufficient ALC action. It does NOT mean the ALC is working properly (properly working ALC would PREVENT flat-topping).

> **Exam tip:** Overmodulation → excessive bandwidth. Flat-topping → excessive drive. Both mean your signal is too wide and you're causing interference.

---

## Digital Modulation: Beyond Voice

Digital modes encode data as discrete symbols rather than continuous audio waveforms. The main digital modulation techniques tested on the exam are FSK, PSK, and multi-tone FSK.

### Frequency Shift Keying (FSK)

FSK represents digital data by switching between two (or more) frequencies. The two frequencies are called **mark** and **space** — terms inherited from telegraphy, where "mark" meant the pen was making a mark on paper tape (current flowing = binary 1) and "space" meant it wasn't (no current = binary 0).

**Direct binary FSK** changes an oscillator's frequency directly with a digital control signal — no intermediate audio tone stage. The digital input directly controls which frequency the oscillator produces.

Standard amateur RTTY uses FSK with a 170 Hz shift between mark and space, running Baudot code at 45.45 baud.

### Phase Shift Keying (PSK)

PSK encodes data by shifting the carrier's phase. **BPSK** (Binary PSK) uses two phase states — 0° and 180° — to represent 1 and 0. **QPSK** (Quadrature PSK) uses four phase states — 0°, 90°, 180°, and 270° — each representing a pair of bits (00, 01, 10, 11).

**PSK31** is the most popular PSK mode in amateur radio, running at 31.25 baud. It uses:
- **Varicode** character encoding — a variable-length code where common characters (like 'e') get short bit sequences and rare characters (like uppercase 'E') get long ones. This is similar in concept to Morse code, where common letters are shorter. The practical consequence: **typing in ALL CAPS slows your throughput** because uppercase letters have longer Varicode sequences.
- **BPSK** modulation in its basic form. **QPSK31** adds error correction by using the extra phase states — one bit for data, one for error correction — while maintaining the same ~31 Hz bandwidth.

### FT8: Modern Weak-Signal Communication

FT8 uses **8-tone frequency shift keying** (8-FSK). The "8" in FT8 refers to 8 different audio tones, each representing 3 bits (2³ = 8). The tones are spaced 6.25 Hz apart, fitting the entire signal into about 50 Hz of bandwidth.

FT8 can decode signals with very **low signal-to-noise ratios** — down to about -20 dB SNR in a 2.5 kHz bandwidth. It achieves this by:
- Using LDPC (Low-Density Parity-Check) forward error correction
- Long integration times (12.64 seconds per transmission)
- Narrow bandwidth (~50 Hz)
- Structured message format (13 characters maximum)

An FT8 signal report of +3 means the SNR is +3 dB in a 2.5 kHz reference bandwidth. Reports typically range from about -24 dB (barely decodable) to +20 dB or more. These are NOT S-meter units and NOT relative to S9.

### WSPR: Propagation Beacons

**WSPR** (Weak Signal Propagation Reporter, pronounced "whisper") is specifically designed as a low-power beacon for assessing HF propagation. WSPR stations transmit callsign, grid locator, and power level (usually 1-5 watts) in a signal about 6 Hz wide. Receiving stations upload reports to wsprnet.org, creating a real-time worldwide propagation map.

### Baudot Code and RTTY

**Baudot code** is a 5-bit code with start and stop bits, used in RTTY. With only 5 bits, it can represent 32 characters per shift — not enough for all letters, numbers, and punctuation. So it uses two shift states (LETTERS and FIGURES) to double the available characters. Baudot has NO error correction — errors produce garbled text.

---

## Bandwidth: How Wide Is Your Signal?

Every modulated signal occupies bandwidth — and different modes occupy very different amounts. Understanding bandwidth relationships is crucial for both the exam and good operating practice.

### Symbol Rate and Bandwidth

**Higher symbol rates require wider bandwidth.** This is a fundamental tradeoff in digital communications — you can't send symbols faster without using more spectrum. Each symbol transition occupies bandwidth; faster transitions need more bandwidth. The Nyquist theorem sets the minimum: bandwidth in Hz ≥ half the symbol rate in symbols/second.

This is why PSK31 (31.25 baud) fits in ~31 Hz while high-speed modes need thousands of hertz. FT8 achieves its narrow 50 Hz bandwidth with a slow 6.25 baud symbol rate combined with 8 tones.

### FM Bandwidth: Carson's Rule

For FM signals, Carson's Rule calculates bandwidth:

**BW = 2 × (deviation + maximum modulating frequency)**

Example: 5 kHz deviation with 3 kHz modulating frequency → 2 × (5 + 3) = **16 kHz**

Note it's NOT just twice the deviation and NOT just twice the modulating frequency. Both terms contribute.

### Matching Receiver Bandwidth

**Matching receiver bandwidth to the operating mode gives the best signal-to-noise ratio.** From G7, recall that wider bandwidth admits more noise. If you're receiving a 200 Hz CW signal through a 2.4 kHz SSB filter, you're letting in 12× more noise than necessary. But too narrow clips the signal. The sweet spot is matching: ~500 Hz for CW, ~2.4 kHz for SSB, ~200 Hz or less for PSK31.

### Duty Cycle Matters

**Duty cycle** is the percentage of time your transmitter is producing RF output. CW has low duty cycle (key up part of the time), SSB voice varies, but digital modes like FT8, RTTY, and PSK31 can be **100% duty cycle** — the transmitter outputs continuously during a transmission. A transmitter rated at 100W PEP for SSB might overheat at 100W continuous digital output. Many transceivers require you to reduce power for high-duty-cycle modes.

---

## Frequency Mixing and Multiplication

These concepts build directly on the mixer and oscillator circuits from G7.

### Heterodyning (Mixing)

**Heterodyning** is the mixing of two RF signals — and it's the foundational principle of the superheterodyne receiver. When two signals combine in a non-linear device (mixer), the output contains the **sum and difference** of the input frequencies.

If F_RF = 14.2 MHz and F_LO = 24.2 MHz:
- Sum: 14.2 + 24.2 = 38.4 MHz
- Difference: 24.2 - 14.2 = 10.0 MHz (this becomes the IF)

The **local oscillator (LO)** is the mixer input that gets tuned to select different incoming frequencies. By changing the LO frequency, you change which RF input frequency gets converted to the fixed IF.

### Image Response

**Image response** is interference from a signal at twice the IF frequency away from the desired signal. It's an inherent problem with mixers: both the desired signal and its "image" produce the same IF when mixed with the LO. A front-end bandpass filter rejects the image frequency, but strong signals can leak through. Higher IF frequencies push the image further away, making filtering easier.

### Frequency Multiplication

A **frequency multiplier** generates harmonics of a lower frequency signal. VHF FM transmitters often generate a stable signal at a lower frequency and multiply it up — a 12 MHz oscillator × 12 = 144 MHz for the 2-meter band.

Critical detail: **frequency multiplication also multiplies the FM deviation by the same factor.** If the final output needs 5 kHz deviation at 146.52 MHz, and the oscillator runs at 12.21 MHz (multiplication factor = 146.52/12.21 = 12), the oscillator deviation must be only 5000/12 = **416.7 Hz**. The multiplication amplifies the tiny oscillator deviation to the required output deviation.

### Intermodulation

**Intermodulation** is the unwanted mixing of two signals in a non-linear circuit (as opposed to heterodyning, which is intentional). It produces spurious outputs called intermodulation products at various frequency combinations.

The critical distinction: **odd-order** intermodulation products fall close to the original frequencies, making them the most troublesome. Even-order products land far away and are easily filtered.

To determine the order: add the absolute values of the frequency multipliers.
- **2F1 − F2:** |2| + |−1| = 3 → 3rd order (odd) — this is the most problematic
- **3F1 − F2:** |3| + |−1| = 4 → 4th order (even)
- **5F1 − 3F2:** |5| + |−3| = 8 → 8th order (even)

Third-order products (2F1−F2 and 2F2−F1) are the strongest and closest to the original signals, which is why receiver specs emphasize the third-order intercept point (IP3).

---

## Link Budgets and Margin

These concepts apply whenever you're planning a communication path — satellite links, EME, microwave point-to-point, or even long-distance HF.

### Link Budget

A **link budget** is an accounting of all gains and losses in a communication path:

**Link budget = Transmit power + Antenna gains − System losses**

Start with transmitter power (dBm), add transmitting antenna gain (dBi), subtract all losses (feed line, free-space path loss, atmospheric absorption, polarization mismatch), add receiving antenna gain. The result is the signal power at the receiver input.

### Link Margin

**Link margin** is your safety cushion — the difference between the received power level and the minimum required signal level at the receiver. If your link budget shows −100 dBm arriving and the receiver needs −120 dBm, you have 20 dB of link margin.

More margin = more reliable link, because it absorbs fading, atmospheric variations, and other unpredictable losses.

---

## Digital Protocols and Error Handling

### ARQ: Automatic Repeat reQuest

ARQ is an error-correction protocol where the receiver checks each packet and responds:
- **ACK** (Acknowledgment) → packet received OK
- **NAK** (Negative Acknowledgment) → errors detected, retransmit

If too many retransmission attempts fail, the **connection is dropped**. ARQ modes include PACTOR, WINMOR, and ARDOP — all used in Winlink email systems.

### FEC: Forward Error Correction

FEC works differently from ARQ: instead of requesting retransmission, it **transmits redundant information with the data** that allows the receiver to correct errors on its own. FEC trades bandwidth for reliability — more bits are sent than the message requires, but no back-channel is needed.

FEC is essential for one-way broadcasts and situations where retransmission isn't practical. Modern FEC codes like LDPC (used in FT8) approach the theoretical limits of error correction.

### Packet Radio

Packet radio frames have a defined structure:
- **Preamble** — synchronization sequence
- **Header** — routing and handling information (source/destination callsigns, digipeater path)
- **Data** — the actual message content
- **Trailer** — error-checking checksum

### Mesh Networks

Mesh network nodes provide **redundancy** — if one node fails, packets can still reach their destination via alternate nodes. This self-healing property makes mesh valuable for emergency communications. Amateur mesh networks often operate on 2.4 GHz (the same band shared with Wi-Fi — see below).

---

## Waterfall Displays

A waterfall display shows three dimensions simultaneously:
- **Horizontal axis** → Frequency
- **Vertical axis** → Time (scrolling downward)
- **Brightness/color** → Signal strength (intensity)

Each horizontal line is one moment's spectrum snapshot. Stacked over time, they create the "waterfall" effect. This format lets you visually identify signals, spot interference, detect overmodulation (those telltale vertical side-lines from G8C13), and click on signals to tune.

---

## Digital Voice Modes

Three systems provide digital voice in amateur radio:
- **DMR** (Digital Mobile Radio) — uses AMBE+2 vocoder, TDMA (two time slots per channel)
- **D-STAR** (Digital Smart Technologies for Amateur Radio) — uses AMBE vocoder, Icom ecosystem
- **System Fusion** (Yaesu) — uses C4FM, can switch between digital voice and analog FM

These are NOT the same as data modes like FT8, PSK31, or Winlink — those carry text or files, not digitized voice.

---

## Shared Spectrum: The 2.4 GHz Band

Amateurs share the **2.4 GHz** band with unlicensed Wi-Fi services (802.11b/g/n). This ISM (Industrial, Scientific, Medical) band allocation means amateur microwave operations coexist with every home router, smartphone, and IoT device. Amateur operators sometimes repurpose commercial Wi-Fi hardware for mesh networking on this band — legal since amateurs have allocations there.

---

## Quick-Reference: Connecting to Prior Subelements

| G8 Concept | Built On |
|---|---|
| Overmodulation → excessive bandwidth | G5: decibels, power relationships |
| Reactance modulator → PM vs FM | G5: reactance; G7: oscillators, amplifiers |
| Mixer sum/difference frequencies | G7: superheterodyne receivers |
| Frequency multiplication × deviation | G7: multiplier stages, Class C amplifiers |
| Bandwidth matching → SNR | G7: receiver sensitivity, filter bandwidth |
| Link budget calculations | G5: decibels, power |
| I/Q and SDR modulation | G7: SDR fundamentals, DSP |
| FEC and error correction | G7: digital circuits |

> **Study strategy:** G8 is the payoff for everything you learned in G5 and G7. If a concept here feels fuzzy, go back and review the underlying circuit or calculation — the connection will click.
