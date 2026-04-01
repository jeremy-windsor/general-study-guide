# G2 — Operating Procedures

This is the "how to actually use your radio" section. You passed the Technician exam knowing the theory — now you need to know the conventions, etiquette, and procedures that make HF communications work. Subelement G2 pulls **5 questions** from a pool of **60**, making it tied for the largest exam weight. These questions cover phone (voice), CW (Morse code), digital modes, and general operating practices.

The good news: most of this is common sense wrapped in ham radio tradition. The tricky part is that many conventions aren't regulations — they're "the way it's done" — and the exam tests whether you know the difference.

---

## SSB Sideband Conventions: USB vs. LSB

The most fundamental operating convention on HF is which sideband to use for voice. It's not in the rules — it's tradition — but breaking it means nobody can understand you.

### The Simple Rule

| Band | Sideband | Why? |
|------|----------|------|
| 160m, 75/80m, 40m | **LSB** (Lower Sideband) | Historical convention |
| 20m and above (17m, 15m, 12m, 10m) | **USB** (Upper Sideband) | Historical convention |
| VHF/UHF (all SSB) | **USB** | Same as 20m+ |

The dividing line is roughly **10 MHz**: below it, use LSB. Above it, use USB. The 17- and 12-meter WARC bands are above 10 MHz, so USB. VHF and UHF are way above, so USB.

**Why LSB on the low bands?** Purely historical accident. Early SSB equipment on the lower bands happened to produce LSB more conveniently, and the practice stuck. There's no technical advantage to either sideband — they work identically. It's just that if you transmit USB on 75 meters, everyone listening on LSB will hear you as unintelligible garble.

> **Memory trick:** "Upper bands = Upper sideband." Everything below 10 MHz is LSB. Everything above is USB.

### SSB: The Dominant HF Voice Mode

Single sideband isn't just a convention — it's the most commonly used voice mode on HF, period. Why SSB dominates:

- **Less bandwidth** — SSB occupies about 2.4 kHz vs. ~6 kHz for AM. More stations fit on the band.
- **Greater power efficiency** — All transmitter power goes into the one sideband carrying your voice. AM wastes roughly 2/3 of its power on the carrier, which carries no information.
- **Only one sideband and NO carrier transmitted** — The carrier and the other sideband are completely suppressed. The receiver reinserts a replacement carrier to make the audio intelligible.

SSB isn't perfect — it's lower fidelity than AM, harder to tune, and just as susceptible to atmospheric noise. But the bandwidth and power advantages make it the clear winner for HF voice.

---

## Phone Operating Procedures

### Breaking Into a Contact

Want to join an ongoing phone QSO? **Say your call sign once.** That's it. The stations in the contact will hear you and invite you in when there's a natural pause.

- ❌ Don't say "QRZ" (that means "who is calling me?" — the opposite of what you want)
- ❌ Don't say "Breaker Breaker" (CB radio culture, not ham radio)
- ❌ Don't call CQ (that's for starting new contacts, not joining existing ones)

### VOX vs. PTT

**VOX** (Voice-Operated Transmit) keys your transmitter automatically when you speak. **PTT** (Push-To-Talk) requires you to press a button.

VOX advantage: **hands-free operation**. You can log contacts, tune an antenna tuner, or flip through a logbook while talking. The tradeoff: VOX can be triggered by background noise, coughing, or receiver audio if not adjusted properly.

### ALC and Mic Gain

The **transmit audio (microphone gain)** control is what you adjust for proper ALC setting. ALC (Automatic Level Control) prevents overdriving your transmitter, which causes splatter — excessive bandwidth that interferes with adjacent stations. Set mic gain so the ALC meter shows action on voice peaks but doesn't peg. Too much = flat-topping and angry neighbors.

### CQ DX

When a US station in the lower 48 calls "CQ DX," they want to contact stations **outside the contiguous 48 states** — Alaska, Hawaii, Caribbean, and foreign countries. If you're also in the lower 48, don't answer. It's not a regulation — it's operating courtesy.

---

## Operating Courtesy and Band Plans

### The Sharing Principle

**Except during emergencies, no amateur station has priority access to any frequency.** This is Part 97.101 — the golden rule of spectrum sharing. Nets don't get priority. QSOs in progress don't get priority. Contest stations don't outrank non-contest stations. Everyone shares equally.

The only exception: **emergency communications get priority.** If you hear a station in distress break into your contact, **acknowledge them immediately** and determine what assistance is needed. Don't reduce power, don't go silent, don't call the emergency coordinator first — respond directly to the station in distress.

### Before You Call CQ

Before transmitting on a "clear" frequency:

1. **On CW:** Send "QRL?" followed by your call sign
2. **On Phone:** Ask "Is this frequency in use?" followed by your call sign
3. **Listen for a response** — if someone replies, move on

A frequency can sound clear because the other station is between transmissions, or because propagation only carries their signal in one direction. Always ask first.

### Band Plans

Band plans are **voluntary** (with rare exceptions) but following them is good practice. They designate where different modes and activities belong — CW at the bottom of each band, digital modes in the middle, phone at the top. Following the band plan keeps the bands organized and reduces interference.

**Special case:** The 50.1–50.125 MHz segment of 6 meters is voluntarily reserved for DX contacts only for stations within the contiguous 48 states. During 6-meter band openings, this narrow slice fills with DX signals, and local contacts would cause interference.

### Frequency Separation

| Mode | Minimum Separation |
|------|-------------------|
| CW | 150 Hz – 500 Hz |
| SSB | 2 kHz – 3 kHz |

CW signals are narrow (~150 Hz bandwidth), so they need much less spacing. SSB signals are about 2.4 kHz wide, so you need 2-3 kHz between them.

### If Propagation Changes

If conditions shift and other stations suddenly appear on your frequency, the right approach is to **work out a mutually acceptable resolution** — maybe one station moves, maybe you take turns, maybe you coordinate. Don't claim priority (nobody has it). Amateur radio is built on cooperation.

---

## RACES

**RACES** (Radio Amateur Civil Emergency Service) is a specific emergency communications program under Part 97.407:

- **Control operator:** Must hold an FCC-issued amateur license (no exceptions for government officials)
- **Training drills:** Limited to **1 hour per week** without special authorization
- **Purpose:** Provide emergency communications in coordination with civil defense organizations

RACES is not the same as ARES (Amateur Radio Emergency Service), which is voluntary and has no FCC-specific rules. RACES has specific regulatory requirements.

---

## CW Operating Procedures

### Full Break-In (QSK)

**Full break-in CW (QSK)** means you can **receive between code characters and even between individual elements** (dits and dahs). The transmitter switches between send and receive so rapidly that you hear the band in every gap in your transmission. This lets you know immediately if someone wants to break in or if conditions change.

Without QSK (semi break-in), you only hear during longer pauses between words or transmissions. QSK requires fast T/R switching hardware.

### Q Signals for the Exam

| Q Signal | Meaning |
|----------|---------|
| **QRL?** | "Is this frequency in use?" |
| **QRS** | "Send more slowly" |
| **QRN** | "I am troubled by static" |
| **QRV** | "I am ready to receive" |
| **QSL** | "I have received and understood" |

These come up repeatedly on the exam. QRL? is what you send before calling CQ on a frequency. QRS is a polite request to slow down. QRN tells your contact that atmospheric noise is making copy difficult. QRV means you're ready. QSL is an acknowledgment.

### CW Prosigns

| Prosign | Meaning | When to use |
|---------|---------|-------------|
| **AR** | End of message | End of a formal message (radiogram) |
| **SK** | End of contact | Signing off |
| **BK** | Break | Quick back-and-forth |
| **KN** | Go ahead (specific station only) | Private conversation — only the station you're talking to should respond |
| **K** | Go ahead (anyone) | Open invitation for anyone to respond |

**KN** is the "private conversation" prosign. If you hear a station end with KN and you're not the station they're talking to, don't call.

### CW Courtesies

- **Match speed:** When answering a CQ, send at the fastest speed you can copy, but **no faster than the CQ station**. If they called at 15 WPM, don't answer at 25. Match or go slower.
- **Zero beat:** Match your transmit frequency to the received signal. The term comes from the beat note dropping to zero Hz when frequencies match exactly.
- **RST "C" suffix:** A "C" added to an RST report means your signal is chirpy or unstable — your frequency is drifting. Check your rig.

---

## DX and General Operating Practices

### The Volunteer Monitor Program

The VM Program consists of amateur volunteers formally enlisted to **monitor the airwaves for rules violations**. They're the ham radio neighborhood watch — listening for out-of-band operation, unlicensed operators, and other Part 97 violations.

VMs can **localize an interfering station** by comparing beam headings from multiple locations — basic triangulation. If VM #1 in location A gets a bearing to the northeast and VM #2 in location B gets a bearing to the northwest, the intersection of those bearings is the approximate source location.

### Azimuthal Projection Maps

An azimuthal map shows **true bearings and distances from a specific location**. It's centered on YOUR QTH, and every point on the map shows the correct compass heading and great-circle distance. Essential for pointing directional antennas — look up your target's location and read the bearing directly.

Regular Mercator maps distort bearings (the "straight line on a Mercator is NOT a great circle" problem). Azimuthal maps solve this, but they're only accurate from their center point.

### Long-Path Contacts

For a long-path contact, point your beam **180° from the short-path heading**. If the short path to Japan is 330° (northwest), the long path is 150° (southeast). Long-path propagation sometimes provides better signals, especially when the short path crosses disturbed polar regions.

### NATO Phonetic Alphabet

**Alpha, Bravo, Charlie, Delta** — the NATO Phonetic Alphabet is the international standard. Learn it. Use it. Don't use "Able, Baker, Charlie, Dog" (old military), "Adam, Boy, Charles, David" (informal), or city names (non-standard).

### Station Logging

The FCC no longer requires a mandatory station log, but keeping one helps **if the FCC ever requests information about your station**. If an interference complaint is investigated, a detailed log provides evidence of your operating activities. Logs are also valuable for awards, contests, and personal records.

### Contests

When participating in a contest, the only **FCC requirement** is to **identify your station according to normal regulations** — every 10 minutes during a contact and at the end. Submitting a log to the contest sponsor is voluntary. QSL cards are optional. Normal Part 97 rules apply.

### QRP and Signal Reports

**QRP** means low-power operation — generally 5 watts CW or 10 watts SSB or less. It's a deliberate challenge: make contacts with minimal power.

**Signal reports** are exchanged at the beginning of a contact so **each station can operate according to conditions**. A 59 report means conditions are great — have a relaxed conversation. A 33 report means keep it short and speak clearly.

---

## Digital Operating Procedures

### RTTY Conventions

- **AFSK RTTY uses LSB** — the long-established convention when sending RTTY audio tones through an SSB transmitter's microphone input
- **170 Hz frequency shift** — the standard mark/space spacing for amateur RTTY (commercial uses wider shifts)
- **Decoding problems** can come from reversed mark/space, wrong baud rate, or wrong sideband — all three should be checked if a signal won't decode

### FT8 and WSJT-X Modes

FT8 has become one of the most popular modes in amateur radio. Key operating practices:

- **USB is the standard sideband** for FT8, FT4, JT65, and JT9
- **Computer time must be accurate to within ~1 second** — FT8 uses precise 15-second time slots synchronized across all stations worldwide. Use NTP or GPS for time sync.
- **When answering a CQ**, find a clear frequency during the **alternate time slot** to the calling station. Don't transmit on their exact frequency.
- **Common location on 20 meters:** Approximately **14.074 MHz to 14.077 MHz** — one of the most active frequencies in all of amateur radio

### Digital Mode Band Segments

On 20 meters, most digital modes live between **14.070 MHz and 14.100 MHz**. FT8 is at ~14.074, RTTY clusters around 14.080-14.090, PSK31 sits near 14.070. Stay away from 14.100 MHz — that's a beacon frequency.

### ARQ Protocols: PACTOR and VARA

**PACTOR** is a point-to-point ARQ protocol — connections are limited to **exactly two stations**. You can't join an existing PACTOR contact. Wait for the session to end.

**VARA** is a newer digital protocol **used with Winlink** for email. It automatically adjusts speed based on channel conditions and works with just a sound card interface (no expensive PACTOR modem needed).

Interference with PACTOR or VARA can cause **all of:** frequent retries, long pauses, and failure to establish connections. ARQ protocols are especially sensitive to interference because corrupted packets trigger retransmission requests.

### Winlink and AREDN

**Winlink** is an amateur radio wireless email network that connects radio stations to the internet email system. It's:
- A wireless email network
- A form of packet radio
- Capable of both VHF and HF operation

A Winlink Remote Message Server is also called a **gateway** — it bridges between radio and the internet.

**AREDN** (Amateur Radio Emergency Data Network) provides **high-speed data services during emergencies** using mesh networking on microwave amateur bands. It carries IP-based services like VoIP, video, and situational awareness maps when internet infrastructure fails.

### Connecting to Digital Gateways

To contact a digital messaging system gateway, **transmit a connect message on the station's published frequency**. Gateways publish their frequencies in directories — tune there and your software handles the connection sequence.

---

## Quick-Reference: The G2 Essentials

| Topic | Key Fact |
|-------|----------|
| USB vs. LSB dividing line | ~10 MHz (below = LSB, above = USB) |
| VHF/UHF SSB | Always USB |
| Breaking into a contact | Say your call sign once |
| Frequency priority | Nobody has it (except emergencies) |
| Before calling CQ | Ask "QRL?" or "Is this frequency in use?" |
| CW separation | 150–500 Hz |
| SSB separation | 2–3 kHz |
| QSK (full break-in) | Receive between code elements |
| QRL? | "Is this frequency in use?" |
| QRS | "Send slower" |
| QSL | "Received and understood" |
| QRN | "I'm troubled by static" |
| QRV | "I'm ready to receive" |
| KN prosign | Go ahead (specific station only) |
| AR prosign | End of formal message |
| RACES drills | 1 hour/week max |
| FT8 time accuracy | Within ~1 second |
| FT8 sideband | USB |
| AFSK RTTY sideband | LSB |
| RTTY shift | 170 Hz |
| 20m digital segment | 14.070–14.100 MHz |
| FT8 on 20m | ~14.074 MHz |
| 6m DX window | 50.1–50.125 MHz |
| NATO alphabet | Alpha, Bravo, Charlie, Delta... |
| QRP | Low-power operation (≤5W CW, ≤10W SSB) |
| PACTOR | Two stations only, can't join |
| Winlink RMS | Also called a "gateway" |
| Azimuthal map | True bearings and distances from your location |
| Long path | 180° from short-path heading |
