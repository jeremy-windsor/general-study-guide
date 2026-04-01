# G8 — Signals and Emissions
*3 questions on the exam from a pool of 43*

## Group G8A — carriers and signals; modulation; AM; FM; single sideband; modulation envelope; digital modulation; overmodulation

### G8A01
**How is direct binary FSK modulation generated?**
- A) By keying an FM transmitter with a sub-audible tone
- **B) By changing an oscillator’s frequency directly with a digital control signal** ✅
- C) By using a transceiver’s computer data interface protocol to change frequencies
- D) By reconfiguring the CW keying input to act as a tone generator

> Direct binary FSK (Frequency Shift Keying) works by changing an oscillator's frequency directly with a digital control signal. When the digital input is a '1' (mark), the oscillator sits at one frequency; when it's a '0' (space), the oscillator shifts to a different frequency. The key word is 'direct' — the digital signal controls the oscillator without going through an audio tone stage first. This is simpler and more precise than generating an audio tone and feeding it into an FM modulator. It's not about sub-audible tones (that's CTCSS), not about computer interface protocols, and not about repurposing CW keying inputs.

### G8A02
**What is the name of the process that changes the phase angle of an RF signal to convey information?**
- A) Phase convolution
- **B) Phase modulation** ✅
- C) Phase transformation
- D) Phase inversion

> Phase modulation (PM) changes the phase angle of the RF carrier to convey information. While FM varies the frequency and AM varies the amplitude, PM shifts the carrier's phase — advancing or retarding it relative to its unmodulated position. Phase modulation and frequency modulation are closely related: varying the phase also affects the instantaneous frequency and vice versa. A reactance modulator connected to an RF amplifier stage actually produces phase modulation (see G8A04). The other answer choices — 'phase convolution,' 'phase transformation,' and 'phase inversion' — are not standard modulation terms.

### G8A03
**What is the name of the process that changes the instantaneous frequency of an RF wave to convey information?**
- A) Frequency convolution
- B) Frequency transformation
- C) Frequency conversion
- **D) Frequency modulation** ✅

> Frequency modulation (FM) changes the instantaneous frequency of the RF wave to convey information. When the modulating audio signal goes positive, the carrier frequency increases; when it goes negative, the carrier frequency decreases. The amount of frequency shift (deviation) is proportional to the audio amplitude, and the rate of shift follows the audio frequency. FM is widely used on VHF/UHF for voice because it's resistant to amplitude noise — since the information is in the frequency, not the amplitude, the receiver can clip off amplitude noise with a limiter stage. Don't confuse FM with frequency conversion (changing one frequency to another in a mixer) or frequency transformation (not a standard term).

### G8A04
**What emission is produced by a reactance modulator connected to a transmitter RF amplifier stage?**
- A) Multiplex modulation
- **B) Phase modulation** ✅
- C) Amplitude modulation
- D) Pulse modulation

> A reactance modulator connected to a transmitter RF amplifier stage produces phase modulation. Here's why: a reactance modulator is a circuit that varies its apparent reactance (capacitive or inductive) in response to an audio signal. When you connect it to an RF amplifier stage (not the oscillator), it shifts the phase of the signal passing through that stage — the audio modulates the phase, not the frequency directly. If you connected the same reactance modulator to the oscillator instead, it would produce FM by pulling the oscillator frequency. The distinction matters: same circuit, different results depending on WHERE in the transmitter chain it's connected. From G7, recall that oscillator frequency is set by the LC tank — modulating the tank produces FM, modulating a downstream amplifier produces PM.

### G8A05
**What type of modulation varies the instantaneous power level of the RF signal?**
- A) Power modulation
- B) Phase modulation
- C) Frequency modulation
- **D) Amplitude modulation** ✅

> Amplitude modulation (AM) varies the instantaneous power level of the RF signal. The carrier's amplitude — and therefore its power — changes in proportion to the modulating audio signal. When the audio goes positive, the carrier amplitude increases (more power); when the audio goes negative, the amplitude decreases (less power). This is fundamentally different from FM (which varies frequency at constant power) and PM (which varies phase at constant power). 'Power modulation' is not a real modulation type — it's a distractor.

### G8A06
**Which of the following is characteristic of QPSK31?**
- A) It is sideband sensitive
- B) Its encoding provides error correction
- C) Its bandwidth is approximately the same as BPSK31
- **D) All these choices are correct** ✅

> QPSK31 (Quadrature Phase Shift Keying at 31.25 baud) has all three listed characteristics: it IS sideband-sensitive (you must use the correct sideband — USB or LSB — for proper decoding), its encoding provides error correction (unlike BPSK31 which has no error correction), and its bandwidth is approximately the same as BPSK31 (about 31 Hz). QPSK31 achieves error correction by using the extra phase states — BPSK uses 2 phase states to send 1 bit per symbol, while QPSK uses 4 phase states to send 2 bits per symbol. One bit carries data, the other carries error correction information. The tradeoff: QPSK31 requires more precise phase tracking and is more sensitive to propagation distortion than BPSK31.

### G8A07
**Which of the following phone emissions uses the narrowest bandwidth?**
- **A) Single sideband** ✅
- B) Vestigial sideband
- C) Phase modulation
- D) Frequency modulation

> Single sideband (SSB) uses the narrowest bandwidth of the listed phone emissions — typically about 2.4 kHz. SSB achieves this by transmitting only ONE sideband and suppressing both the carrier and the other sideband. Compare: conventional AM transmits carrier plus both sidebands (~6 kHz), vestigial sideband transmits one full sideband plus a portion of the other, and FM typically uses 10-16 kHz depending on deviation. SSB's narrow bandwidth is a huge advantage on crowded HF bands — more stations fit in the same spectrum space. It also concentrates all transmitter power into the information-carrying sideband rather than wasting most of it on a carrier.

### G8A08
**Which of the following is an effect of overmodulation?**
- A) Insufficient audio
- B) Insufficient bandwidth
- C) Frequency drift
- **D) Excessive bandwidth** ✅

> Overmodulation causes excessive bandwidth — the signal splashes beyond its normal frequency allocation and interferes with stations on adjacent frequencies. When you overdrive any modulator, the signal distorts, and distortion creates harmonics and spurious energy that spread the signal wider than it should be. In AM, overmodulation happens when the modulating signal tries to drive the carrier below zero (causing flat-topping or carrier pinch-off). In FM, excessive deviation spreads the signal beyond its allowed bandwidth. Either way, the result is the same: your signal gets wider and starts causing interference. This is why ALC (Automatic Level Control) and proper mic gain settings matter.

### G8A09
**What type of modulation is used by FT8?**
- **A) 8-tone frequency shift keying** ✅
- B) Vestigial sideband
- C) Amplitude compressed AM
- D) 8-bit direct sequence spread spectrum

> FT8 uses 8-tone frequency shift keying (8-FSK). The '8' in FT8 stands for 8 tones — the mode uses 8 different audio frequencies to encode data, with each tone representing 3 bits (2³ = 8 combinations). The tones are spaced 6.25 Hz apart, fitting the entire signal into about 50 Hz of bandwidth. FT8 was designed by Joe Taylor (K1JT) and Steve Franke (K9AN) for weak-signal communication — it can decode signals buried 20+ dB below the noise floor. It's NOT vestigial sideband (that's an analog TV technique), NOT compressed AM, and NOT spread spectrum. FT8 has revolutionized amateur radio by enabling contacts that would be impossible with voice modes.

### G8A10
**What is meant by the term “flat-topping,” when referring to an amplitude-modulated phone signal?**
- A) Signal distortion caused by insufficient collector current
- B) The transmitter’s automatic level control (ALC) is properly adjusted
- **C) Signal distortion caused by excessive drive or speech levels** ✅
- D) The transmitter’s carrier is properly suppressed

> Flat-topping is signal distortion caused by excessive drive or speech levels in an AM or SSB transmitter. On an oscilloscope, the modulation envelope looks like it has flat tops instead of rounded peaks — the amplifier has run out of headroom and is clipping the waveform. This is a form of overmodulation that generates splatter (excessive bandwidth) and interference to nearby stations. Flat-topping is typically caused by too much mic gain, too much speech processor compression, or insufficient ALC action. It does NOT mean the ALC is properly adjusted (that would PREVENT flat-topping), and it's not about insufficient collector current or carrier suppression. Watch for flat-topping on your ALC meter and waterfall display.

### G8A11
**What is the modulation envelope of an AM signal?**
- **A) The waveform created by connecting the peak values of the modulated signal** ✅
- B) The carrier frequency that contains the signal
- C) Spurious signals that envelop nearby frequencies
- D) The bandwidth of the modulated signal

> The modulation envelope of an AM signal is the waveform created by connecting the peak values of the modulated signal. Picture an AM signal on an oscilloscope: you see the RF carrier oscillating rapidly, but its amplitude rises and falls with the audio. If you draw a line connecting all the positive peaks and another connecting all the negative peaks, those lines trace out the modulation envelope — and that envelope IS the audio waveform. An AM demodulator (detector) works by extracting this envelope. The envelope is NOT the carrier frequency itself, NOT spurious signals, and NOT the bandwidth. It's the outline of the amplitude variations — the 'shape' of the modulated signal.

### G8A12
**What is QPSK modulation?**
- A) Modulation using quasi-parallel to serial conversion to reduce bandwidth
- B) Modulation using quadra-pole sideband keying to generate spread spectrum signals
- C) Modulation using Fast Fourier Transforms to generate frequencies at the first, second, third, and fourth harmonics of the carrier frequency to improve noise immunity
- **D) Modulation in which digital data is transmitted using 0-, 90-, 180- and 270-degrees phase shift to represent pairs of bits** ✅

> QPSK (Quadrature Phase Shift Keying) transmits digital data using four phase states: 0°, 90°, 180°, and 270°. Each phase state represents a pair of bits (00, 01, 10, 11), so QPSK sends 2 bits per symbol — twice the data rate of BPSK at the same symbol rate and bandwidth. The four phases are evenly spaced around a circle (360°/4 = 90° apart). From G8A06, remember that QPSK31 uses these extra bits for error correction rather than doubling throughput. The wrong answers are made-up terms — there's no 'quasi-parallel to serial conversion,' no 'quadra-pole sideband keying,' and no 'Fast Fourier Transform harmonic generation' scheme. QPSK is a real, well-defined digital modulation technique used across telecommunications.

### G8A13
**What is a link budget?**
- A) The financial costs associated with operating a radio link
- B) The sum of antenna gains minus system losses
- **C) The sum of transmit power and antenna gains minus system losses as seen at the receiver** ✅
- D) The difference between transmit power and receiver sensitivity

> A link budget is the sum of transmit power and antenna gains minus system losses as seen at the receiver. It's an accounting exercise: start with your transmitter power (in dBm), add your transmitting antenna gain (in dBi), subtract all losses (feed line, free-space path loss, atmospheric absorption, polarization mismatch), and add the receiving antenna gain. The result tells you the signal power arriving at the receiver. If this number exceeds the receiver's minimum sensitivity, communication is possible. It's NOT about financial costs (despite the word 'budget'), and it includes more than just antenna gains minus losses — the transmit power is a critical starting term. Link budgets are essential for satellite work, EME (moonbounce), and microwave links.

### G8A14
**What is link margin?**
- A) The opposite of fade margin
- **B) The difference between received power level and minimum required signal level at the input to the receiver** ✅
- C) Transmit power minus receiver sensitivity
- D) Receiver sensitivity plus 3 dB

> Link margin is the difference between the received power level and the minimum required signal level at the receiver's input. Think of it as your safety cushion: if your link budget shows -100 dBm arriving at the receiver and the receiver needs -120 dBm to decode, you have 20 dB of link margin. That margin accounts for fading, atmospheric variations, and other unpredictable losses. More margin = more reliable link. It's NOT the opposite of fade margin (they're related concepts, not opposites), NOT simply transmit power minus sensitivity (that ignores path loss and antenna gains), and NOT receiver sensitivity plus 3 dB. Link margin and link budget work together: the budget calculates received power, and the margin tells you how far above minimum you are.

## Group G8B — Frequency mixing; multiplication; bandwidths of various modes; deviation; duty cycle; intermodulation

### G8B01
**Which mixer input is varied or tuned to convert signals of different frequencies to an intermediate frequency (IF)?**
- A) Image frequency
- **B) Local oscillator** ✅
- C) RF input
- D) Beat frequency oscillator

> The local oscillator (LO) is the mixer input that is varied or tuned to convert different incoming frequencies to the intermediate frequency (IF). From G7, recall that a superheterodyne receiver uses a mixer to combine the incoming RF signal with the LO to produce sum and difference frequencies. By tuning the LO, you select which incoming frequency gets converted to the fixed IF. The RF input carries the signal you want to receive, the image frequency is an unwanted signal (covered in G8B02), and the BFO (beat frequency oscillator) is used later in the receive chain for SSB/CW demodulation — not for frequency conversion in the mixer.

### G8B02
**What is the term for interference from a signal at twice the IF frequency from the desired signal?**
- A) Quadrature response
- **B) Image response** ✅
- C) Mixer interference
- D) Intermediate interference

> Image response is interference from a signal at twice the IF frequency away from the desired signal. Here's the mechanism: a mixer produces both sum and difference frequencies. If your IF is 10 MHz and you're tuned to 14.2 MHz (LO at 24.2 MHz), both 14.2 MHz AND 34.2 MHz will produce a 10 MHz difference with the LO. That 34.2 MHz signal is the 'image' — it's exactly 2×IF (20 MHz) away from your desired frequency. The front-end bandpass filter is supposed to reject the image frequency, but if it leaks through, you hear the image signal mixed on top of your desired signal. Higher IF frequencies push the image further away, making it easier to filter — one reason modern receivers use high first-IF frequencies.

### G8B03
**What is another term for the mixing of two RF signals?**
- **A) Heterodyning** ✅
- B) Synthesizing
- C) Frequency inversion
- D) Phase inversion

> Heterodyning is another term for mixing two RF signals. The word comes from Greek: 'hetero' (different) + 'dyne' (force/power). When you combine two different frequencies in a non-linear device (mixer), you get sum and difference frequencies — that's heterodyning. The superheterodyne receiver is named for this process: 'super' (above audible) + 'heterodyne.' Heterodyning is the foundational principle of virtually every receiver design since the 1920s. Synthesizing means building up, frequency inversion means flipping a spectrum, and phase inversion means a 180° shift — none of these describe the mixing of two signals.

### G8B04
**What is the stage in a VHF FM transmitter that generates a harmonic of a lower frequency signal to reach the desired operating frequency?**
- A) Mixer
- B) Reactance modulator
- C) Balanced converter
- **D) Multiplier** ✅

> A frequency multiplier generates a harmonic of a lower frequency signal to reach the desired operating frequency. In a VHF FM transmitter, it's often easier to generate a stable, well-modulated signal at a lower frequency and then multiply it up. A multiplier stage uses a non-linear amplifier (like Class C from G7) to deliberately generate harmonics, then a tuned output circuit selects the desired harmonic. For example, a 12 MHz oscillator multiplied by 12 produces 144 MHz for the 2-meter band. Frequency multiplication also multiplies the FM deviation by the same factor — this is how the small deviation at the oscillator becomes the full 5 kHz deviation at the output frequency (see G8B07). A mixer combines two different frequencies; a multiplier generates harmonics of one frequency.

### G8B05
**Which intermodulation products are closest to the original signal frequencies?**
- A) Second harmonics
- B) Even-order
- **C) Odd-order** ✅
- D) Intercept point

> Odd-order intermodulation products are closest to the original signal frequencies — and that's what makes them so problematic. When two signals (F1 and F2) mix in a non-linear device, they produce intermodulation products at various combinations: 2F1-F2, 2F2-F1 (3rd order), 3F1-2F2, 3F2-2F1 (5th order), etc. These odd-order products fall NEAR the original frequencies, making them very difficult to filter out. Even-order products (F1+F2, F1-F2, 2F1, 2F2) land far from the originals and are easily filtered. This is why receiver specs emphasize odd-order intercept points (IP3, IP5) — those products are the ones that actually cause interference on adjacent channels. Second harmonics are a specific even-order product, and intercept point is a measurement parameter, not a type of product.

### G8B06
**What is the total bandwidth of an FM phone transmission having 5 kHz deviation and 3 kHz modulating frequency?**
- A) 3 kHz
- B) 5 kHz
- C) 8 kHz
- **D) 16 kHz** ✅

> Use Carson's Rule: bandwidth = 2 × (deviation + maximum modulating frequency) = 2 × (5 kHz + 3 kHz) = 2 × 8 kHz = 16 kHz. Carson's Rule gives you the approximate bandwidth that contains about 98% of the FM signal's power. Note that it's NOT just twice the deviation (10 kHz) and NOT just twice the modulating frequency (6 kHz) — you need both terms added together, then doubled. The deviation determines how far the carrier swings, and the modulating frequency determines how fast it swings. Both contribute to the total bandwidth occupied.

### G8B07
**What is the frequency deviation for a 12.21 MHz reactance modulated oscillator in a 5 kHz deviation, 146.52 MHz FM phone transmitter?**
- A) 101.75 Hz
- **B) 416.7 Hz** ✅
- C) 5 kHz
- D) 60 kHz

> The oscillator deviation is 416.7 Hz. Here's the math: the transmitter uses frequency multiplication to get from 12.21 MHz to 146.52 MHz. The multiplication factor is 146.52 / 12.21 = 12. Since frequency multiplication multiplies deviation by the same factor, the oscillator deviation must be the final deviation divided by the multiplication factor: 5000 Hz / 12 = 416.7 Hz. This is why FM transmitters using multiplier chains start with very small deviations at the oscillator — the multiplication process amplifies the deviation along with the frequency. If the oscillator had the full 5 kHz deviation, the output would have 60 kHz deviation (5 kHz × 12) — way too wide.

### G8B08
**Why is it important to know the duty cycle of the mode you are using when transmitting?**
- A) To aid in tuning your transmitter
- **B) Some modes have high duty cycles that could exceed the transmitter’s average power rating** ✅
- C) To allow time for the other station to break in during a transmission
- D) To prevent overmodulation

> Knowing the duty cycle of your operating mode matters because some modes have high duty cycles that could exceed the transmitter's average power rating. Duty cycle is the percentage of time your transmitter is actually producing RF output. CW has a low duty cycle — key down some, key up some. SSB voice varies. But digital modes like FT8, RTTY, and PSK31 can be 100% duty cycle — the transmitter is producing full output continuously during a transmission. A transmitter rated at 100W PEP for SSB might overheat at 100W continuous digital modes because its cooling system was designed for a lower average power. Many transceivers require you to reduce power for high-duty-cycle digital modes. This is a practical safety consideration, not about tuning, break-in, or overmodulation.

### G8B09
**Why is it good to match receiver bandwidth to the bandwidth of the operating mode?**
- A) It is required by FCC rules
- B) It minimizes power consumption in the receiver
- C) It improves impedance matching of the antenna
- **D) It results in the best signal-to-noise ratio** ✅

> Matching receiver bandwidth to the operating mode's bandwidth gives the best signal-to-noise ratio (SNR). From G7C08, recall that wider bandwidth admits more noise. If you're receiving a 200 Hz CW signal through a 2.4 kHz SSB filter, you're letting in 12× more noise than necessary — every hertz of bandwidth beyond what the signal needs is just admitting more noise without adding more signal. But making the filter TOO narrow clips the signal edges. The sweet spot is matching: a 500 Hz filter for CW, 2.4 kHz for SSB, 200 Hz or less for PSK31. This isn't an FCC requirement, doesn't affect power consumption or antenna impedance — it's purely about optimizing the signal-to-noise ratio.

### G8B10
**What is the relationship between transmitted symbol rate and bandwidth?**
- A) Symbol rate and bandwidth are not related
- **B) Higher symbol rates require wider bandwidth** ✅
- C) Lower symbol rates require wider bandwidth
- D) Bandwidth is half the symbol rate

> Higher symbol rates require wider bandwidth. This is a fundamental principle of digital communications — you can't send symbols faster without using more spectrum. Each symbol transition occupies bandwidth; more transitions per second means more bandwidth. The Nyquist theorem sets the lower bound: the minimum bandwidth in Hz equals half the symbol rate in symbols/second. In practice, real filters and pulse shaping require somewhat more. This is the tradeoff in digital mode design: PSK31 uses a slow 31.25 baud rate and fits in ~31 Hz, while high-speed modes like PACTOR IV need thousands of hertz. FT8 achieves its narrow bandwidth by using a very slow symbol rate (6.25 baud) with multiple tones.

### G8B11
**What combination of a mixer’s Local Oscillator (LO) and RF input frequencies is found in the output?**
- A) The ratio
- B) The average
- **C) The sum and difference** ✅
- D) The arithmetic product

> A mixer's output contains the sum and difference of the LO and RF input frequencies. This is the fundamental mixer equation: if you feed in F_RF and F_LO, you get F_RF + F_LO and F_RF − F_LO (or F_LO − F_RF) at the output. The desired frequency (usually the difference) becomes the IF, and the unwanted product (usually the sum) is filtered out. For example, 14.2 MHz RF + 24.2 MHz LO produces 38.4 MHz (sum) and 10.0 MHz (difference). The 10.0 MHz difference becomes your IF. The output is NOT the ratio, NOT the average, and NOT the arithmetic product (multiplication) — it's the sum AND difference, created by the non-linear mixing process.

### G8B12
**What process combines two signals in a non-linear circuit to produce unwanted spurious outputs?**
- **A) Intermodulation** ✅
- B) Heterodyning
- C) Detection
- D) Rolloff

> Intermodulation is the process where two signals combine in a non-linear circuit to produce unwanted spurious outputs. The key word is 'unwanted' — this distinguishes intermodulation from heterodyning (G8B03), which is intentional mixing. Intermodulation happens when strong signals overload an amplifier, mixer, or any non-linear element. The resulting spurious signals (intermodulation products or IMD) appear at various combinations of the input frequencies and can fall on top of weak desired signals, causing interference. From G8B05, recall that odd-order products are the most troublesome because they fall close to the original frequencies. Detection is extracting information from a modulated signal, and rolloff describes filter attenuation — neither produces spurious outputs.

### G8B13
**Which of the following is an odd-order intermodulation product of frequencies F1 and F2?**
- A) 5F1-3F2
- B) 3F1-F2
- **C) 2F1-F2** ✅
- D) All these choices are correct

> 2F1 − F2 is a third-order intermodulation product — and the order is 3 because the coefficients add up to 3 (2 + 1 = 3). To determine the order: add the absolute values of all the frequency multipliers. For 2F1 − F2: |2| + |−1| = 3 (third order, odd). For 3F1 − F2: |3| + |−1| = 4 (fourth order, even — NOT odd). For 5F1 − 3F2: |5| + |−3| = 8 (eighth order, even — NOT odd). So among the choices, only 2F1 − F2 is actually odd-order. This is a tricky question because 'All these choices' sounds tempting, but you have to check the math for each one. Third-order products (2F1−F2 and 2F2−F1) are the strongest and closest to the original signals, making them the most important for receiver design.

## Group G8C — Digital emission modes; information rate vs bandwidth; error correction

### G8C01
**On what band do amateurs share channels with the unlicensed Wi-Fi service?**
- A) 432 MHz
- B) 902 MHz
- **C) 2.4 GHz** ✅
- D) 10.7 GHz

> Amateurs share the 2.4 GHz band with unlicensed Wi-Fi services. The 2.4 GHz band (2400-2450 MHz) is allocated to both amateur radio (secondary) and industrial/scientific/medical (ISM) uses — which includes Wi-Fi (802.11b/g/n). This shared allocation means amateur microwave operations and mesh networking projects on 2.4 GHz must coexist with the massive amount of Wi-Fi traffic from every home router, smartphone, and IoT device. The 432 MHz, 902 MHz, and 10.7 GHz bands don't have Wi-Fi sharing. Amateur operators on 2.4 GHz sometimes repurpose commercial Wi-Fi hardware (like Ubiquiti or Mikrotik radios) for amateur mesh networking — which is legal since amateurs have privileges on the band.

### G8C02
**Which digital mode is used as a low-power beacon for assessing HF propagation?**
- **A) WSPR** ✅
- B) MFSK16
- C) PSK31
- D) SSB-SC

> WSPR (Weak Signal Propagation Reporter, pronounced 'whisper') is the digital mode used as a low-power beacon for assessing HF propagation. WSPR stations transmit their callsign, grid locator, and power level (typically 1-5 watts) using a very narrow bandwidth signal (about 6 Hz). Receiving stations upload reception reports to a central database (wsprnet.org), creating a real-time map of propagation paths. WSPR can decode signals as weak as -28 dB SNR. It's specifically designed for propagation assessment — you set it and forget it. MFSK16 and PSK31 are keyboard-to-keyboard chat modes, not beacons. SSB-SC is a voice mode. WSPR is the go-to tool for understanding what bands are open and to where.

### G8C03
**What part of a packet radio frame contains the routing and handling information?**
- A) Directory
- B) Preamble
- **C) Header** ✅
- D) Trailer

> The header of a packet radio frame contains the routing and handling information — source callsign, destination callsign, digipeater path, and protocol control fields. Think of it like the envelope of a letter: the header tells the network where the packet came from, where it's going, and how to handle it. The preamble is a synchronization sequence that lets the receiver lock onto the signal timing. The trailer marks the end of the frame and typically contains an error-checking checksum. 'Directory' is not a standard packet radio frame component. The header/preamble/data/trailer structure is common across most digital communication protocols.

### G8C04
**Which of the following describes Baudot code?**
- A) A 7-bit code with start, stop, and parity bits
- B) A code using error detection and correction
- **C) A 5-bit code with additional start and stop bits** ✅
- D) A code using SELCAL and LISTEN

> Baudot code is a 5-bit code with additional start and stop bits. Developed in 1870 by Émile Baudot, it's one of the oldest digital character encoding systems and is still used in amateur RTTY (Radio Teletype). With 5 bits, Baudot can represent 2⁵ = 32 characters per shift — but that's not enough for letters, numbers, and punctuation. So Baudot uses two shift states (LETTERS and FIGURES) to double the available characters to 64. The start and stop bits frame each character for asynchronous transmission. Baudot is NOT 7-bit (that's ASCII), does NOT include error detection/correction (errors just produce garbled text), and has nothing to do with SELCAL or LISTEN. It's simple, old, and still works.

### G8C05
**In an ARQ mode, what is meant by a NAK response to a transmitted packet?**
- **A) Request retransmission of the packet** ✅
- B) Packet was received without error
- C) Receiving station connected and ready for transmissions
- D) Entire file received correctly

> In an ARQ (Automatic Repeat reQuest) mode, a NAK (Negative Acknowledgment) response means 'I received the packet but it contained errors — please retransmit.' ARQ is an error-correction protocol where the receiver checks each incoming packet (typically using a CRC checksum) and responds with either ACK (Acknowledgment — packet OK) or NAK (errors detected — send again). This back-and-forth continues until the packet gets through cleanly or too many attempts fail (see G8C06). NAK does NOT mean the packet was received without error (that's ACK), doesn't indicate a connection is established, and doesn't mean the entire file was received. ARQ modes include PACTOR, WINMOR, and ARDOP — all used in Winlink email systems.

### G8C06
**What action results from a failure to exchange information due to excessive transmission attempts when using an ARQ mode?**
- A) The checksum overflows
- **B) The connection is dropped** ✅
- C) Packets will be routed incorrectly
- D) Encoding reverts to the default character set

> When an ARQ mode fails to exchange information after excessive transmission attempts, the connection is dropped. Every ARQ protocol has a retry limit — if a packet can't get through after a certain number of retransmission attempts (because the channel is too noisy, interference is too strong, or the other station has disappeared), the protocol gives up and disconnects. This prevents stations from endlessly retransmitting into the void and tying up the frequency. The checksum doesn't 'overflow' (it's a fixed-size value), packets aren't routed incorrectly (they just fail), and the encoding doesn't revert to a default set. The connection simply terminates, and you'd need to reinitiate it when conditions improve.

### G8C07
**Which of the following narrow-band digital modes can receive signals with very low signal-to-noise ratios?**
- A) MSK144
- **B) FT8** ✅
- C) AMTOR
- D) MFSK32

> FT8 can receive signals with very low signal-to-noise ratios — down to about -20 dB SNR in a 2.5 kHz bandwidth. This extraordinary weak-signal capability comes from its narrow bandwidth (~50 Hz), long integration time (12.64 seconds per transmission), and powerful forward error correction (LDPC coding). FT8 achieves this by trading speed for sensitivity — each transmission carries very little information (13 characters maximum), but it gets through when nothing else can. MSK144 is designed for meteor scatter (short bursts, not weak signals). AMTOR is an older ARQ mode without exceptional weak-signal capability. MFSK32 has decent performance but doesn't match FT8's ability to pull signals from the noise.

### G8C08
**Which of the following statements is true about PSK31?**
- A) Upper case letters are sent with more power
- **B) Upper case letters use longer Varicode bit sequences and thus slow down transmission** ✅
- C) Error correction is used to ensure accurate message reception
- D) Higher power is needed as compared to RTTY for similar error rates

> In PSK31, upper case letters use longer Varicode bit sequences and thus slow down transmission. PSK31 uses Varicode encoding (see G8C12) where common characters get short bit sequences and rare characters get longer ones. Lower case 'e' is encoded as just 11 (2 bits), while upper case 'E' is 1110111 (7 bits) — more than 3× longer. This means typing in ALL CAPS literally slows your throughput. Upper case letters are NOT sent with more power (power is constant in PSK31). PSK31 does NOT use error correction — that's QPSK31 (see G8A06). And PSK31 is actually more power-efficient than RTTY, not less. The practical lesson: use lower case in PSK31 for faster throughput.

### G8C09
**Which is true of mesh network microwave nodes?**
- A) Having more nodes increases signal strengths
- **B) If one node fails, a packet may still reach its target station via an alternate node** ✅
- C) Links between two nodes in a network may have different frequencies and bandwidths
- D) More nodes reduce overall microwave out of band interference

> The key characteristic of mesh network microwave nodes is redundancy: if one node fails, a packet may still reach its target station via an alternate node. That's the entire point of a mesh topology — multiple interconnected paths mean no single point of failure. Each node can route traffic through any available neighbor, and routing protocols automatically find alternate paths when one goes down. More nodes don't increase signal strength (each link has its own path loss). Links between nodes in a mesh DO typically use the same frequency and bandwidth (that's how they mesh). And more nodes don't reduce out-of-band interference. The resilience and self-healing nature of mesh is what makes it valuable for amateur emergency communications networks.

### G8C10
**How does forward error correction (FEC) allow the receiver to correct data errors?**
- A) By controlling transmitter output power for optimum signal strength
- B) By using the Varicode character set
- **C) By transmitting redundant information with the data** ✅
- D) By using a parity bit with each character

> Forward error correction (FEC) works by transmitting redundant information with the data. The transmitter adds extra bits (calculated from the original data using mathematical algorithms) that the receiver uses to detect AND correct errors — without needing retransmission. This is fundamentally different from ARQ (G8C05-06), which detects errors and requests retransmission. FEC trades bandwidth for reliability: you're sending more bits than the actual message requires, but the receiver can fix errors on its own. FEC does NOT control transmitter power, does NOT use Varicode (that's a character encoding), and is more sophisticated than simple parity bits. Modern FEC codes like LDPC (used in FT8) and turbo codes approach the theoretical limits of error correction. FEC is essential for one-way broadcasts and situations where retransmission isn't practical.

### G8C11
**How are the two separate frequencies of a Frequency Shift Keyed (FSK) signal identified?**
- A) Dot and dash
- B) On and off
- C) High and low
- **D) Mark and space** ✅

> The two frequencies of an FSK signal are called mark and space. These terms come from telegraphy: 'mark' was when the pen made a mark on the paper tape (current flowing), and 'space' was when it didn't (no current). In FSK, mark typically represents a binary 1 and space represents binary 0, each at its own distinct frequency. For amateur RTTY, the standard shift between mark and space is 170 Hz. 'Dot and dash' refers to Morse code (CW), 'on and off' describes on-off keying (OOK), and 'high and low' is too generic. Mark and space are the specific, correct terms for FSK frequency identification. You'll see these terms in every RTTY and FSK-related discussion.

### G8C12
**Which type of code is used for sending characters in a PSK31 signal?**
- **A) Varicode** ✅
- B) Viterbi
- C) Volumetric
- D) Binary

> PSK31 uses Varicode to encode characters. Varicode is a variable-length code where common characters (like 'e' and 't') get short bit sequences and uncommon characters (like 'Z' and uppercase letters) get longer ones — similar in concept to Morse code, where 'E' is a single dit. This makes PSK31 efficient for typical English text. Characters are separated by two or more consecutive zeros (00). Viterbi is a decoding algorithm for convolutional codes (error correction), not a character encoding. 'Volumetric' is not a real coding term. And while all digital codes are ultimately binary, 'binary' doesn't describe the specific variable-length encoding scheme that makes PSK31 work. Varicode is the defining character set of PSK31.

### G8C13
**What is indicated on a waterfall display by one or more vertical lines on either side of a data mode or RTTY signal?**
- A) Long path propagation
- B) Backscatter propagation
- C) Insufficient modulation
- **D) Overmodulation** ✅

> Vertical lines on either side of a data mode or RTTY signal on a waterfall display indicate overmodulation. These lines are spurious emissions — harmonics and intermodulation products created when the signal is driven too hard. A clean digital signal should appear as a narrow, well-defined trace on the waterfall. When overmodulated, the signal distorts and splatters energy into adjacent frequencies, showing up as additional vertical lines flanking the main signal. This is the digital equivalent of flat-topping in SSB (G8A10) — too much drive creates excessive bandwidth (G8A08). The fix is to reduce your audio drive level or transmitter power. These lines do NOT indicate propagation effects (long path or backscatter) or insufficient modulation — they specifically indicate excessive modulation.

### G8C14
**Which of the following describes a waterfall display?**
- A) Frequency is horizontal, signal strength is vertical, time is intensity
- B) Frequency is vertical, signal strength is intensity, time is horizontal
- **C) Frequency is horizontal, signal strength is intensity, time is vertical** ✅
- D) Frequency is vertical, signal strength is horizontal, time is intensity

> A waterfall display shows frequency on the horizontal axis, signal strength as intensity (brightness or color), and time on the vertical axis (scrolling downward). Imagine stacking spectrum snapshots on top of each other over time — each horizontal line is one moment's spectrum, and time flows downward like a waterfall. Stronger signals appear brighter or in different colors. This format lets you see signals, their bandwidth, and how they change over time simultaneously. It's invaluable for digital modes — you can visually identify mode types, spot interference, detect overmodulation (G8C13), and click on signals to tune to them. The three axes (frequency, intensity, time) and their orientations are the key to this question.

### G8C15
**What does an FT8 signal report of +3 mean?**
- A) The signal is 3 times the noise level of an equivalent SSB signal
- B) The signal is S3 (weak signals)
- **C) The signal-to-noise ratio is equivalent to +3dB in a 2.5 kHz bandwidth** ✅
- D) The signal is 3 dB over S9

> An FT8 signal report of +3 means the signal-to-noise ratio is equivalent to +3 dB in a 2.5 kHz bandwidth. FT8 reports SNR rather than traditional S-meter readings because FT8 routinely works with signals far below the noise floor. The reference bandwidth of 2.5 kHz was chosen because it's the approximate bandwidth of an SSB receiver — so the report tells you how the signal compares to the noise you'd hear in a normal SSB passband. A report of +3 means the signal is 3 dB above the noise floor in that bandwidth — audible but not strong. FT8 reports typically range from about -24 dB (barely decodable) to +20 dB or higher (very strong). The report is NOT in S-units, NOT relative to S9, and NOT a comparison to an SSB signal's strength.

### G8C16
**Which of the following provide digital voice modes?**
- A) WSPR, MFSK16, and EasyPAL
- B) FT8, FT4, and FST4
- C) Winlink, PACTOR II, and PACTOR III
- **D) DMR, D-STAR, and SystemFusion** ✅

> DMR (Digital Mobile Radio), D-STAR (Digital Smart Technologies for Amateur Radio), and System Fusion provide digital voice modes. These are the three major digital voice systems used in amateur radio, each using different vocoder technology to compress voice into a digital stream. DMR uses AMBE+2 codec, D-STAR uses AMBE codec, and System Fusion (Yaesu's system) uses either C4FM digital voice or conventional analog FM. WSPR, MFSK16, and EasyPAL are data/image modes, not voice. FT8, FT4, and FST4 are weak-signal data modes. Winlink, PACTOR II, and PACTOR III are email/data transfer protocols. Only DMR, D-STAR, and System Fusion are designed specifically to carry digitized voice over radio.
