# G2 — Operating Procedures
*5 questions on the exam from a pool of 60*

## Group G2A — Phone operating procedures; USB/LSB conventions; procedural signals; breaking into a contact; VOX operation

### G2A01
**Which mode is most commonly used for voice communications on frequencies of 14 MHz or higher?**
- **A) Upper sideband** ✅
- B) Lower sideband
- C) Suppressed sideband
- D) Double sideband

> Upper sideband (USB) is the standard mode for voice on frequencies of 14 MHz and higher. This is one of the most fundamental operating conventions in amateur radio — it's not a regulation, just universally accepted practice (G2A09). The dividing line is roughly 10 MHz: above that, use USB. Below that (160m, 75/80m, 40m), use LSB (G2A02). The 17-meter and 12-meter bands (G2A04) are above 14 MHz, so they follow the USB convention too. VHF and UHF SSB also uses USB (G2A03). Memory trick: Upper bands = Upper sideband.

### G2A02
**Which mode is most commonly used for voice communications on the 160-, 75-, and 40-meter bands?**
- A) Upper sideband
- **B) Lower sideband** ✅
- C) Suppressed sideband
- D) Double sideband

> Lower sideband (LSB) is the standard mode for voice on the 160-, 75-, and 40-meter bands. These are the low HF bands — below 10 MHz — and the convention is LSB. Why? It's purely historical tradition (G2A09), not a technical requirement. Early SSB equipment on these bands happened to use LSB, and the convention stuck. The key dividing line: below 10 MHz = LSB, above 10 MHz = USB. Both sidebands work equally well technically — it's just that everyone needs to agree so you can actually understand each other.

### G2A03
**Which mode is most commonly used for SSB voice communications in the VHF and UHF bands?**
- **A) Upper sideband** ✅
- B) Lower sideband
- C) Suppressed sideband
- D) Double sideband

> Upper sideband (USB) is the standard for SSB voice on VHF and UHF. Since VHF starts at 50 MHz and UHF at 420 MHz, these are well above the 10 MHz dividing line, so USB is the convention. VHF/UHF SSB is used primarily for weak-signal work — mountaintopping, meteor scatter, EME (moonbounce), and tropospheric ducting contacts. FM dominates VHF/UHF for local repeater work, but when you switch to SSB for weak signals, it's always USB.

### G2A04
**Which mode is most commonly used for voice communications on the 17- and 12-meter bands?**
- **A) Upper sideband** ✅
- B) Lower sideband
- C) Suppressed sideband
- D) Double sideband

> Upper sideband (USB) is the standard for voice on the 17- and 12-meter bands. The 17-meter band is at 18.068 MHz and 12 meters is at 24.890 MHz — both well above the 10 MHz dividing line. These WARC bands (named for the 1979 World Administrative Radio Conference that created them) follow the same USB convention as 20 meters and above. Quick summary: 160m, 75/80m, 40m = LSB. Everything else (20m and up, plus VHF/UHF) = USB.

### G2A05
**Which mode of voice communication is most commonly used on the HF amateur bands?**
- A) Frequency modulation
- B) Double sideband
- **C) Single sideband** ✅
- D) Single phase modulation

> Single sideband (SSB) is the most commonly used voice mode on HF. Not AM, not FM — SSB. From G2A06 and G8A07, SSB uses less bandwidth than AM or FM and is more power-efficient (all the transmitter power goes into the information-carrying sideband rather than being wasted on a carrier). On HF, where spectrum is scarce and every decibel counts for DX, SSB is king. FM is used for VHF/UHF repeaters. AM has a small following among enthusiasts but isn't mainstream. 'Single phase modulation' isn't a real mode.

### G2A06
**Which of the following is an advantage of using single sideband, as compared to other analog voice modes on the HF amateur bands?**
- A) Very high-fidelity voice modulation
- B) Less subject to interference from atmospheric static crashes
- C) Ease of tuning on receive and immunity to impulse noise
- **D) Less bandwidth used and greater power efficiency** ✅

> The key advantages of SSB over other analog voice modes on HF are less bandwidth used AND greater power efficiency. SSB occupies about 2.4 kHz — less than half of AM's ~6 kHz (G8A07). And since SSB suppresses the carrier (which contains no information), ALL of the transmitter power goes into the sideband carrying your voice. In AM, roughly 2/3 of the power is wasted on the carrier. SSB is NOT higher fidelity than AM (it's actually lower), NOT less subject to static (static affects all modes similarly), and NOT easier to tune (SSB requires more careful tuning than AM). It wins on efficiency, not audio quality.

### G2A07
**Which of the following statements is true of single sideband (SSB)?**
- A) Only one sideband and the carrier are transmitted; the other sideband is suppressed
- **B) Only one sideband is transmitted; the other sideband and carrier are suppressed** ✅
- C) SSB is the only voice mode authorized on the 20-, 15-, and 10-meter amateur bands
- D) SSB is the only voice mode authorized on the 160-, 75-, and 40-meter amateur bands

> In SSB, only one sideband is transmitted — the other sideband AND the carrier are both suppressed. This is the definition of single sideband: you take the output of a balanced modulator (which produces both sidebands with no carrier, from G7C02) and filter out one sideband (G7C01), leaving just one sideband. The receiver reinserts the carrier using a BFO/product detector (G7C04) to make the audio intelligible. Choice A is wrong because the carrier is NOT transmitted — if it were, that would be a different mode. SSB is also not the 'only voice mode authorized' on any band — AM and FM are also permitted.

### G2A08
**What is the recommended way to break into a phone contact?**
- A) Say “QRZ” several times, followed by your call sign
- **B) Say your call sign once** ✅
- C) Say “Breaker Breaker”
- D) Say “CQ” followed by the call sign of either station

> To break into an ongoing phone contact, simply say your call sign once. That's it — clean, professional, and minimally disruptive. The stations in the QSO will hear you, acknowledge you when there's a natural pause, and invite you in. 'QRZ' means 'who is calling me?' — that's what you send when YOU hear someone calling, not when you want to break in. 'Breaker Breaker' is CB radio culture, not amateur radio. And calling CQ is for initiating new contacts, not breaking into existing ones. One call sign, once. Done.

### G2A09
**Why do most amateur stations use lower sideband on the 160-, 75-, and 40-meter bands?**
- A) Lower sideband is more efficient than upper sideband at these frequencies
- B) Lower sideband is the only sideband legal on these frequency bands
- C) Because it is fully compatible with an AM detector
- **D) It is commonly accepted amateur practice** ✅

> The reason for using LSB on 160/75/40 meters is simply commonly accepted amateur practice — it's convention, not regulation. There's no law requiring LSB on these bands, and LSB isn't technically 'better' at lower frequencies. The convention dates back to early SSB equipment designs in the 1950s-60s. Some early filter-type SSB generators on the lower bands produced LSB more conveniently, and the practice became universal. The FCC doesn't mandate which sideband to use — but if you transmit USB on 75 meters, nobody will understand you because they're all listening on LSB.

### G2A10
**Which of the following statements is true of VOX operation versus PTT operation?**
- A) The received signal is more natural sounding
- **B) It allows “hands free” operation** ✅
- C) It occupies less bandwidth
- D) It provides more power output

> VOX (Voice-Operated Transmit) allows 'hands free' operation — the transmitter keys automatically when you speak into the microphone. With PTT (Push-To-Talk), you press a button to transmit and release it to receive. VOX frees your hands for logging, tuning, or adjusting controls while talking. It does NOT make received audio more natural, does NOT reduce bandwidth, and does NOT provide more power output. The tradeoff: VOX can be triggered by background noise or receiver audio (unless the VOX delay and anti-VOX are properly adjusted). Many operators use VOX for ragchewing and PTT for contests.

### G2A11
**Generally, who should respond to a station in the contiguous 48 states calling “CQ DX”?**
- A) Any caller is welcome to respond
- B) Only stations in Germany
- **C) Any stations outside the lower 48 states** ✅
- D) Only contest stations

> When a station in the contiguous 48 states calls 'CQ DX,' they're specifically looking for distant contacts — stations OUTSIDE the lower 48 states. 'DX' means distance, and from a US perspective, that includes Alaska, Hawaii, US territories, and all foreign countries. If you're also in the lower 48, don't answer a CQ DX call — the calling station isn't looking for you. It's not restricted to only Germany or only contest stations — any station outside the lower 48 qualifies. This is operating courtesy, not a regulation — but violating it will earn you no friends.

### G2A12
**What control is typically adjusted for proper ALC setting on a single sideband transceiver?**
- A) RF clipping level
- **B) Transmit audio or microphone gain** ✅
- C) Antenna inductance or capacitance
- D) Attenuator level

> The transmit audio or microphone gain control is what you adjust for proper ALC setting. ALC (Automatic Level Control) prevents your transmitter from being overdriven, which causes splatter and distortion (G8A08, G8A10). You set mic gain so the ALC meter shows activity on voice peaks but doesn't slam to maximum. Too much mic gain = ALC constantly pegged = flat-topping and excessive bandwidth. RF clipping is a speech processor function, not an ALC adjustment. Antenna tuning affects SWR, not ALC. And attenuator level is a receive function. The mic gain knob is your primary ALC control.

## Group G2B — Operating courtesy; band plans; emergencies, including distress calling and detecting communications; RACES

### G2B01
**Which of the following is true concerning access to frequencies?**
- A) Nets have priority
- B) QSOs in progress have priority
- **C) Except during emergencies, no amateur station has priority access to any frequency** ✅
- D) Contest operations should yield to non-contest use of frequencies

> Except during emergencies, no amateur station has priority access to any frequency. This is a foundational principle from Part 97.101 — the amateur bands are shared equally. Nets don't get priority. A QSO already in progress doesn't get priority. Contest stations don't yield to non-contest stations (or vice versa). Everyone shares. The only exception is emergencies — stations providing emergency communications DO get priority. This principle encourages cooperation and courtesy rather than turf wars over frequencies.

### G2B02
**What is the first thing you should do if you are communicating with another amateur station and hear a station in distress break in?**
- A) Inform your local emergency coordinator
- **B) Acknowledge the station in distress and determine what assistance may be needed** ✅
- C) Immediately decrease power to avoid interfering with the station in distress
- D) Immediately cease all transmissions

> If you hear a station in distress break into your contact, the FIRST thing to do is acknowledge the station in distress and determine what assistance may be needed. Don't go off to call the emergency coordinator (the distressed station needs help NOW). Don't decrease power (they need to hear you). Don't cease all transmissions (silence doesn't help anyone). You acknowledge them, find out what's happening, and then coordinate whatever assistance is needed — which might include relaying to emergency services, clearing the frequency for emergency traffic, or providing direct assistance.

### G2B03
**What is good amateur practice if propagation changes during a contact creating interference from other stations using the frequency?**
- A) Advise the interfering stations that you are on the frequency and that you have priority
- B) Decrease power and continue to transmit
- **C) Attempt to resolve the interference problem with the other stations in a mutually acceptable manner** ✅
- D) Switch to the opposite sideband

> If propagation changes cause interference with other stations on your frequency, good practice is to attempt to resolve the problem in a mutually acceptable manner. This means talking it out — maybe one station moves, maybe you take turns, maybe you find a compromise. You do NOT claim priority and tell others to leave (G2B01 — no one has priority). Decreasing power might help but doesn't address the core issue. Switching sidebands is impractical because everyone on the band uses the same sideband convention. Amateur radio is built on cooperation, and this question tests that philosophy.

### G2B04
**When selecting a CW transmitting frequency, what minimum separation from other stations should be used to minimize interference to stations on adjacent frequencies?**
- A) 5 Hz to 50 Hz
- **B) 150 Hz to 500 Hz** ✅
- C) 1 kHz to 3 kHz
- D) 3 kHz to 6 kHz

> When selecting a CW frequency, maintain 150 Hz to 500 Hz separation from other stations. CW signals are narrow — a typical CW signal occupies about 100-150 Hz of bandwidth. So 150 Hz minimum separation prevents direct overlap, and up to 500 Hz gives comfortable breathing room. Compare this to SSB, which needs 2-3 kHz separation (G2B05) because SSB signals are much wider. The 5-50 Hz range would cause constant interference. The 1-3 kHz and 3-6 kHz ranges are overkill for CW and would waste valuable spectrum space.

### G2B05
**When selecting an SSB transmitting frequency, what minimum separation should be used to minimize interference to stations on adjacent frequencies?**
- A) 5 Hz to 50 Hz
- B) 150 Hz to 500 Hz
- **C) 2 kHz to 3 kHz** ✅
- D) Approximately 6 kHz

> When selecting an SSB transmitting frequency, maintain 2 kHz to 3 kHz separation from other stations. An SSB signal occupies about 2.4 kHz of bandwidth (G8A07), so 2-3 kHz separation prevents the signals from overlapping. Compare this to CW's 150-500 Hz (G2B04) — SSB needs roughly 10× more spacing because the signals are roughly 10× wider. 5-50 Hz is way too close, 150-500 Hz is CW spacing, and 6 kHz is unnecessarily wide (you'd be wasting half the band).

### G2B06
**How can you avoid harmful interference on an apparently clear frequency before calling CQ on CW or phone?**
- **A) Send “QRL?” on CW, followed by your call sign; or, if using phone, ask if the frequency is in use, followed by your call sign** ✅
- B) Listen for 2 minutes before calling CQ
- C) Send the letter “V” in Morse code several times and listen for a response, or say “test” several times and listen for a response
- D) Send “QSY” on CW or if using phone, announce “the frequency is in use,” then give your call sign and listen for a response

> Before calling CQ on an apparently clear frequency, ask 'QRL?' on CW or 'Is this frequency in use?' on phone, followed by your call sign. This is essential operating courtesy — a frequency may sound clear because the station you can't hear is between transmissions, or because propagation only carries their signal one way. By asking first, you give any stations already using the frequency a chance to respond before you start transmitting on top of them. Just listening for 2 minutes isn't enough (you might miss a pause). Sending 'V' or 'test' is not standard practice. And 'QSY' means 'change frequency' — that's what you tell someone ELSE to do, not what you send when checking.

### G2B07
**Which of the following complies with commonly accepted amateur practice when choosing a frequency on which to initiate a call?**
- A) Listen on the frequency for at least two minutes to be sure it is clear
- B) Identify your station by transmitting your call sign at least 3 times
- **C) Follow the voluntary band plan** ✅
- D) All these choices are correct

> Following the voluntary band plan is good amateur practice when choosing a frequency to initiate a call. Band plans designate which modes and activities go where — CW at the bottom, digital modes in the middle, phone at the top (roughly). They're voluntary (not enforceable by law, with a few exceptions), but following them keeps the bands organized and reduces interference. Listening for 2 minutes isn't the accepted practice (you ask if the frequency is in use — G2B06). Identifying 3 times isn't required. And 'all these choices' is wrong because the other options aren't correct. The band plan is the answer.

### G2B08
**What is the voluntary band plan restriction for US stations transmitting within the 48 contiguous states in the 50.1 MHz to 50.125 MHz band segment?**
- **A) Only contacts with stations not within the 48 contiguous states** ✅
- B) Only contacts with other stations within the 48 contiguous states
- C) Only digital contacts
- D) Only SSTV contacts

> The voluntary band plan restriction for 50.1-50.125 MHz is contacts with stations NOT within the 48 contiguous states only. This segment of the 6-meter band is reserved by band plan for DX — intercontinental contacts, contacts with Hawaii, Alaska, Caribbean stations, etc. It's the 6-meter equivalent of 'CQ DX' territory. During band openings, this narrow segment can be packed with DX signals, and local contacts would cause harmful interference. Below 50.1 MHz is CW/beacon territory; above 50.125 MHz is available for all contacts including domestic. This is voluntary but widely respected.

### G2B09
**Who may be the control operator of an amateur station transmitting in RACES to assist relief operations during a disaster?**
- **A) Only a person holding an FCC-issued amateur operator license** ✅
- B) Only a RACES net control operator
- C) A person holding an FCC-issued amateur operator license or an appropriate government official
- D) Any control operator when normal communication systems are operational

> Only a person holding an FCC-issued amateur operator license may be the control operator of a station transmitting in RACES. RACES (Radio Amateur Civil Emergency Service) operates under Part 97.407 with strict rules — the control operator must hold a real amateur license. It's not enough to be a 'RACES net control operator' without a license, and government officials without amateur licenses can't be control operators. RACES is specifically for amateurs who are registered with their local civil defense organization to provide emergency communications.

### G2B10
**Which of the following is good amateur practice for net management?**
- A) Always use multiple sets of phonetics during check-in
- **B) Have a backup frequency in case of interference or poor conditions** ✅
- C) Transmit the full net roster at the beginning of every session
- D) All these choices are correct

> Good practice for net management includes having a backup frequency in case of interference or poor conditions. When your primary frequency gets clobbered by QRM, atmospheric noise, or propagation changes, a pre-arranged backup frequency lets the net move quickly without losing participants. Multiple sets of phonetics during check-in is annoying and wastes time — one set is enough. Transmitting the full roster at the start is impractical for large nets and also wastes airtime. The backup frequency is the genuinely useful practice that keeps a net running smoothly.

### G2B11
**How often may RACES training drills and tests be routinely conducted without special authorization?**
- A) No more than 1 hour per month
- B) No more than 2 hours per month
- **C) No more than 1 hour per week** ✅
- D) No more than 2 hours per week

> RACES training drills and tests may be conducted routinely for no more than 1 hour per week without special authorization. This is straight from Part 97.407(d)(4). RACES stations are only authorized to transmit during actual emergencies and during authorized drills — they can't just chat whenever they want. The 1-hour-per-week limit keeps training regular while minimizing non-emergency use of RACES frequencies. More frequent or longer drills require special authorization from the responsible civil defense organization. Memorize: 1 hour, per week.

## Group G2C — CW operating procedures and prosigns; Q signals and common abbreviations; full break-in

### G2C01
**Which of the following describes full break-in CW operation (QSK)?**
- A) Breaking stations send the Morse code prosign “BK”
- B) Automatic keyers, instead of hand keys, are used to send Morse code
- C) An operator must activate a manual send/receive switch before and after every transmission
- **D) Transmitting stations can receive between code characters and elements** ✅

> Full break-in CW (QSK) means the transmitting station can receive between code characters and even between individual elements (dits and dahs). The transmitter switches from transmit to receive so rapidly that you can hear other stations in the gaps between your own code elements. This lets you know immediately if someone is trying to break in, if conditions change, or if you need to stop. It's like having a full-duplex conversation. Without QSK (semi break-in), you can only hear during longer pauses between words or sentences. QSK requires fast T/R switching hardware — it's not about sending 'BK,' using automatic keyers, or manual switching.

### G2C02
**What should you do if a CW station sends “QRS?”**
- **A) Send slower** ✅
- B) Change frequency
- C) Increase your power
- D) Repeat everything twice

> If a CW station sends 'QRS,' you should send slower. QRS literally means 'Send more slowly' — it's a request from the other operator who's having trouble copying at your speed. It's one of the most practical Q signals for CW operation. Don't change frequency (QSY is for that), don't increase power (QRO is for that), and don't repeat everything twice (that's just annoying if they can't copy your speed). Slow down to match their ability. Good CW practice means being considerate of the other operator's skill level.

### G2C03
**What does it mean when a CW operator sends “KN” at the end of a transmission?**
- A) No US stations should call
- B) Operating full break-in
- **C) Listening only for a specific station or stations** ✅
- D) Closing station now

> KN at the end of a CW transmission means 'listening only for a specific station or stations.' The K alone means 'go ahead, anyone can respond.' Adding the N makes it exclusive — 'only the station I'm in contact with should respond.' It's the CW equivalent of a private conversation. If you hear a station end with KN and you're not the station they're talking to, don't call them. Other prosigns: SK means 'end of contact,' BK means 'break' (back to you quickly), AR means 'end of message' (G2C08).

### G2C04
**What does the Q signal “QRL?” mean?**
- A) “Will you keep the frequency clear?”
- B) “Are you operating full break-in?” or “Can you operate full break-in?”
- C) “Are you listening only for a specific station?”
- **D) “Are you busy?” or “Is this frequency in use?”** ✅

> QRL? means 'Are you busy?' or 'Is this frequency in use?' This is the CW equivalent of asking if a frequency is clear before calling CQ (G2B06). You send QRL? and listen — if someone responds with 'C' (yes), 'QRL,' or 'YES,' the frequency is occupied and you should move. If silence, it's probably clear. QRL is one of the most commonly used Q signals in everyday CW operating. Don't confuse it with QSK (full break-in, G2C01), QRN (static, G2C10), or QSL (received and understood, G2C09).

### G2C05
**What is the best speed to use when answering a CQ in Morse code?**
- A) The fastest speed at which you are comfortable copying, but no slower than the CQ
- **B) The fastest speed at which you are comfortable copying, but no faster than the CQ** ✅
- C) At the standard calling speed of 10 wpm
- D) At the standard calling speed of 5 wpm

> When answering a CQ in Morse code, send at the fastest speed you can comfortably copy, but no faster than the CQ. If someone calls CQ at 15 WPM, don't answer at 25 WPM — they probably can't copy that fast, which is why they're calling at 15. Match or go slower than their speed, never faster. If you can copy 20 WPM but they called at 12, answer at 12. There's no 'standard calling speed' of 5 or 10 WPM — you match the other station. This is basic CW courtesy and ensures both stations can actually communicate.

### G2C06
**What does the term “zero beat” mean in CW operation?**
- A) Matching the speed of the transmitting station
- B) Operating split to avoid interference on frequency
- C) Sending without error
- **D) Matching the transmit frequency to the frequency of a received signal** ✅

> 'Zero beat' means matching your transmit frequency to the frequency of a received signal. The term comes from the audio beat note you hear when two frequencies are close but not identical — as you tune closer, the beat note drops in pitch until it reaches zero Hz (silence) when the frequencies match exactly. In CW, zero-beating ensures you're transmitting on the same frequency as the station you're trying to work, so they hear you in their receiver passband. It's NOT about matching speed, operating split, or sending without errors. Zero beat = same frequency.

### G2C07
**When sending CW, what does a “C” mean when added to the RST report?**
- **A) Chirpy or unstable signal** ✅
- B) Report was read from an S meter rather than estimated
- C) 100 percent copy
- D) Key clicks

> A 'C' added to a CW RST report indicates a chirpy or unstable signal. The standard RST report has three numbers: Readability (1-5), Signal Strength (1-9), and Tone (1-9). The 'C' suffix is an additional qualifier meaning the signal's frequency is drifting or chirping — the tone shifts noticeably, usually due to an unstable oscillator or power supply issue. Getting a report of '579C' means 'I can read you fine and you're strong, but your signal sounds chirpy — check your rig.' It does NOT mean 100% copy or S-meter reading. 'K' suffix would indicate key clicks (if used).

### G2C08
**What prosign is sent to indicate the end of a formal message when using CW?**
- A) SK
- B) BK
- **C) AR** ✅
- D) KN

> AR is the prosign sent to indicate the end of a formal message in CW. AR means 'end of message' — it tells the receiving station that the formal message (like a radiogram or NTS traffic) is complete. Don't confuse it with: SK (end of contact — signing off), BK (break — quick back-and-forth), or KN (go ahead, specific station only — G2C03). AR is specifically for formal traffic handling. In casual CW contacts, you might use K, KN, BK, or SK, but AR is the formal 'message complete' prosign.

### G2C09
**What does the Q signal “QSL” mean?**
- A) Send slower
- B) We have already confirmed the contact
- **C) I have received and understood** ✅
- D) We have worked before

> QSL means 'I have received and understood.' It's an acknowledgment — 'I copy, message received.' In everyday ham radio, 'QSL' is most famously associated with QSL cards (confirmation cards exchanged after contacts), but the Q signal itself simply means 'received and understood.' It does NOT mean 'send slower' (that's QRS — G2C02), doesn't mean 'we've confirmed the contact' (though QSL cards serve that purpose), and doesn't mean 'we've worked before.' It's a simple acknowledgment.

### G2C10
**What does the Q signal “QRN” mean?**
- A) Send more slowly
- B) Stop sending
- C) Zero beat my signal
- **D) I am troubled by static** ✅

> QRN means 'I am troubled by static.' Static — atmospheric noise from thunderstorms, power line noise, or other natural/man-made interference. When a CW operator sends QRN, they're telling you the band is noisy at their end and they're having trouble copying. This is especially common on the lower bands during summer (G3B12). Don't confuse QRN (static/noise) with QRM (man-made interference from other stations) or QRS (send more slowly — G2C02). QRN is about atmospheric noise specifically.

### G2C11
**What does the Q signal “QRV” mean?**
- A) You are sending too fast
- B) There is interference on the frequency
- C) I am quitting for the day
- **D) I am ready to receive** ✅

> QRV means 'I am ready to receive.' It's a simple status signal — 'I'm here, I'm listening, go ahead and send.' You might hear QRV at the beginning of a contact or during traffic handling when one station is ready for the next message. It doesn't mean 'you're sending too fast' (QRS handles speed requests), doesn't indicate interference (QRM or QRN), and doesn't mean signing off for the day. QRV = ready.

## Group G2D — Amateur satellite operation; Doppler shift; spin fading; LEO; HEO; orbital; telemetry

### G2D01
**What is the Volunteer Monitor Program?**
- **A) Amateur volunteers who are formally enlisted to monitor the airwaves for rules violations** ✅
- B) Amateur volunteers who conduct amateur licensing examinations
- C) Amateur volunteers who conduct frequency coordination for amateur VHF repeaters
- D) Amateur volunteers who use their station equipment to help civil defense organizations in times of emergency

> The Volunteer Monitor Program consists of amateur volunteers who are formally enlisted to monitor the airwaves for rules violations. Think of them as the amateur radio neighborhood watch — they listen for out-of-band operation, excessive bandwidth, unlicensed operators, and other Part 97 violations, then report their findings to the FCC. The VM Program replaced the older Official Observer (OO) program in 2019. VMs are NOT Volunteer Examiners (that's the VE program for licensing — G1D), NOT frequency coordinators (that's for repeaters), and NOT ARES/RACES emergency volunteers.

### G2D02
**Which of the following are objectives of the Volunteer Monitor Program?**
- A) To conduct efficient and orderly amateur licensing examinations
- B) To provide emergency and public safety communications
- C) To coordinate repeaters for efficient and orderly spectrum usage
- **D) To encourage amateur radio operators to self-regulate and comply with the rules** ✅

> The objectives of the Volunteer Monitor Program are to encourage amateur radio operators to self-regulate and comply with the rules. The program is about self-policing — the amateur community monitoring itself rather than relying solely on the FCC's limited enforcement resources. VMs can issue advisory notices for minor violations and refer serious cases to the FCC. The VM program is NOT about licensing exams (that's VEs), NOT about emergency communications (that's ARES/RACES), and NOT about repeater coordination. It's specifically about rules compliance and self-regulation.

### G2D03
**What procedure may be used by Volunteer Monitors to localize a station whose continuous carrier is holding a repeater on in their area?**
- A) Compare vertical and horizontal signal strengths on the input frequency
- **B) Compare beam headings on the repeater input from their home locations with that of other Volunteer Monitors** ✅
- C) Compare signal strengths between the input and output of the repeater
- D) All these choices are correct

> Volunteer Monitors can localize a station holding a repeater open by comparing beam headings from their home locations with those of other Volunteer Monitors. This is basic radio direction finding (triangulation) — if one VM determines the signal is coming from the northeast and another VM 20 miles away determines it's coming from the northwest, the source is where those two bearings intersect on a map. This requires directional antennas (beams) at multiple locations. It's NOT about comparing vertical vs. horizontal signal strengths, and NOT about comparing repeater input vs. output. Triangulation from multiple bearings is the standard technique.

### G2D04
**Which of the following describes an azimuthal projection map?**
- A) A map that shows accurate land masses
- **B) A map that shows true bearings and distances from a specific location** ✅
- C) A map that shows the angle at which an amateur satellite crosses the equator
- D) A map that shows the number of degrees longitude that an amateur satellite appears to move westward at the equator with each orbit

> An azimuthal projection map shows true bearings and distances from a specific location. It's centered on YOUR location, and every point on the map shows the correct compass bearing (azimuth) and great-circle distance from the center. This is invaluable for pointing directional antennas — look up the DX station's location on your azimuthal map and you instantly know which direction to point your beam. Regular Mercator maps distort bearings and distances at high latitudes. An azimuthal map is only accurate from its center point — a map centered on New York is useless for someone in Tokyo. It has nothing to do with satellite orbits or equator crossings.

### G2D05
**Which of the following indicates that you are looking for an HF contact with any station?**
- A) Sign your call sign once, followed by the words “listening for a call” -- if no answer, change frequency and repeat
- B) Say “QTC” followed by “this is” and your call sign -- if no answer, change frequency and repeat
- **C) Repeat “CQ” a few times, followed by “this is,” then your call sign a few times, then pause to listen, repeat as necessary** ✅
- D) Transmit an unmodulated carried for approximately 10 seconds, followed by “this is” and your call sign, and pause to listen -- repeat as necessary

> To look for an HF contact with any station, you call CQ: repeat 'CQ' a few times, followed by 'this is,' then your call sign a few times, pause to listen, and repeat as necessary. CQ is the universal 'calling any station' signal. The format is: 'CQ CQ CQ, this is [callsign] [callsign] [callsign], standing by.' A few CQs (not too many — nobody wants to listen to 30 seconds of CQ), your call sign clearly, then LISTEN. Too many people call CQ endlessly without pausing to hear replies. The other choices describe incorrect or non-standard procedures — transmitting an unmodulated carrier is never appropriate.

### G2D06
**How is a directional antenna pointed when making a “long-path” contact with another station?**
- A) Toward the rising sun
- B) Along the gray line
- **C) 180 degrees from the station’s short-path heading** ✅
- D) Toward the north

> For a long-path contact, point your directional antenna 180 degrees from the short-path heading. The short path is the direct great-circle route to the other station. The long path goes the other way around the globe — exactly opposite direction. If the short path to Japan from the US east coast is northwest (~330°), the long path is southeast (~150°). Long-path propagation can sometimes provide better signals than short path, especially when the short path crosses the polar regions during geomagnetic storms (G3A08) or when the long path follows the gray line. It's 180° opposite — not toward the rising sun, not along the gray line specifically, and not toward the north.

### G2D07
**Which of the following are examples of the NATO Phonetic Alphabet?**
- A) Able, Baker, Charlie, Dog
- B) Adam, Boy, Charles, David
- C) America, Boston, Canada, Denmark
- **D) Alpha, Bravo, Charlie, Delta** ✅

> Alpha, Bravo, Charlie, Delta are examples of the NATO Phonetic Alphabet. The NATO alphabet is the international standard used in amateur radio for spelling out call signs clearly: Alpha, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliet, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu. 'Able, Baker, Charlie, Dog' is the old US military phonetic alphabet (pre-NATO). 'Adam, Boy, Charles, David' and 'America, Boston, Canada, Denmark' are informal alternatives sometimes heard but are NOT the NATO standard.

### G2D08
**Why do many amateurs keep a station log?**
- A) The FCC requires a log of all international contacts
- B) The FCC requires a log of all international third-party traffic
- C) The log provides evidence of operation needed to renew a license without retest
- **D) To help with a reply if the FCC requests information about your station** ✅

> Many amateurs keep a station log to help with a reply if the FCC requests information about their station. While the FCC no longer requires a mandatory station log, keeping one is still excellent practice. If the FCC investigates an interference complaint or questions your operating activities, a detailed log provides evidence of what you were doing, when, and on what frequency. Logs are also valuable for award tracking, contest submissions, and personal records. The FCC does NOT require logs of international contacts (choice A) or third-party traffic (choice B) — those mandatory logging requirements were eliminated years ago. And logs are NOT needed for license renewal.

### G2D09
**Which of the following is required when participating in a contest on HF frequencies?**
- A) Submit a log to the contest sponsor
- B) Send a QSL card to the stations worked, or QSL via Logbook of The World
- **C) Identify your station according to normal FCC regulations** ✅
- D) All these choices are correct

> When participating in a contest on HF, the only thing REQUIRED is to identify your station according to normal FCC regulations — every 10 minutes during a contact and at the end. Contest operation doesn't create any special requirements beyond normal Part 97 rules. Submitting a log to the contest sponsor is voluntary (you're encouraged to, but it's not an FCC requirement). Sending QSL cards is optional courtesy. The FCC doesn't care about your contest score — they care that you identify properly, stay in band, and follow the rules. Normal identification rules apply in contests just like any other operating activity.

### G2D10
**What is QRP operation?**
- A) Remote piloted model control
- **B) Low-power transmit operation** ✅
- C) Transmission using Quick Response Protocol
- D) Traffic relay procedure net operation

> QRP means low-power transmit operation. The generally accepted definition is 5 watts or less on CW and 10 watts or less on SSB (PEP). QRP operators intentionally limit their power to challenge themselves — making contacts with minimal power tests your skills, antenna, and propagation knowledge. It's a popular operating style with its own contests, clubs (QRP ARCI, for example), and award programs. QRP is NOT remote piloted model control, NOT 'Quick Response Protocol' (made-up), and NOT a traffic relay procedure. The Q signal QRP literally means 'reduce power' — and QRP operators take that to heart.

### G2D11
**Why are signal reports typically exchanged at the beginning of an HF contact?**
- **A) To allow each station to operate according to conditions** ✅
- B) To be sure the contact will count for award programs
- C) To follow standard radiogram structure
- D) To allow each station to calibrate their frequency display

> Signal reports are exchanged at the beginning of an HF contact so each station can operate according to conditions. If you give me a 59 report, I know conditions are great and we can have a leisurely conversation. If you give me a 33 report, I know to keep it short, speak slowly and clearly, and maybe repeat key information. The signal report sets expectations for the entire contact. It's NOT primarily for award programs (though some awards require signal reports), NOT related to radiogram format, and NOT for calibrating frequency displays. It's practical information that helps both operators adjust their operating style to match actual conditions.

## Group G2E — Digital operating: procedures,  modes, andடperformance; monitoring digital transmissions; digital message forwarding; Winlink

### G2E01
**Which mode is normally used when sending RTTY signals via AFSK with an SSB transmitter?**
- A) USB
- B) DSB
- C) CW
- **D) LSB** ✅

> LSB (Lower Sideband) is normally used when sending RTTY via AFSK with an SSB transmitter. This seems backwards since most digital modes use USB, but RTTY via AFSK on LSB is the long-established convention. When using Audio Frequency Shift Keying (AFSK), the audio tones fed into the SSB transmitter's mic input shift the RF output — and the mark/space relationship comes out correctly on LSB. If you used USB, the mark and space frequencies would be reversed (which can actually be compensated for in software, but LSB is the standard). Note: when using direct FSK (keying the transmitter directly), the sideband setting doesn't matter the same way. AFSK + RTTY = LSB.

### G2E02
**What is VARA?**
- A) A low signal-to-noise digital mode used for EME (moonbounce)
- **B) A digital protocol used with Winlink** ✅
- C) A radio direction finding system used on VHF and UHF
- D) A DX spotting system using a network of software defined radios

> VARA is a digital protocol used with Winlink. VARA (developed by EA5HVK) provides high-speed data transfer for Winlink email operations on both HF and VHF/UHF. It automatically adjusts its speed based on channel conditions — starting slow and ramping up as conditions allow, or slowing down when conditions degrade. VARA has largely replaced older protocols like WINMOR and PACTOR for Winlink gateway connections because it offers good performance with just a sound card interface (no expensive PACTOR modem required). It's NOT a moon-bounce mode, NOT a direction-finding system, and NOT a DX spotting network.

### G2E03
**What symptoms may result from other signals interfering with a PACTOR or VARA transmission?**
- A) Frequent retries or timeouts
- B) Long pauses in message transmission
- C) Failure to establish a connection between stations
- **D) All these choices are correct** ✅

> ALL of the listed symptoms can result from interference with a PACTOR or VARA transmission: frequent retries or timeouts, long pauses, and failure to establish a connection. These are ARQ (Automatic Repeat reQuest) protocols — they request retransmission when packets are corrupted (G8C05). Interference corrupts packets, triggering retries. If retries keep failing, the protocol pauses and eventually times out. If the interference is bad enough from the start, the initial handshake fails and no connection is established at all. This is why choosing a clear frequency is especially important for digital modes — interference doesn't just degrade quality like it does with voice, it can completely prevent communication.

### G2E04
**Which of the following is good practice when choosing a transmitting frequency to answer a station calling CQ using FT8?**
- A) Always call on the station’s frequency
- B) Call on any frequency in the waterfall except the station’s frequency
- C) Find a clear frequency during the same time slot as the calling station
- **D) Find a clear frequency during the alternate time slot to the calling station** ✅

> When answering a CQ on FT8, good practice is to find a clear frequency during the alternate time slot to the calling station. FT8 operates in strict 15-second time slots — even slots (0, 15, 30, 45 seconds) and odd slots. If the calling station transmitted in an even slot, you respond in the next odd slot, and vice versa. You should also choose a different audio frequency (a clear spot on the waterfall) rather than calling on the station's own frequency. Calling on their exact frequency would collide with their transmissions. The WSJT-X software handles much of this automatically, but understanding the principle matters for the exam.

### G2E05
**What is the standard sideband for JT65, JT9, FT4, or FT8 digital signal when using AFSK?**
- A) LSB
- **B) USB** ✅
- C) DSB
- D) SSB

> USB (Upper Sideband) is the standard for JT65, JT9, FT4, and FT8 when using AFSK. This follows the modern digital mode convention — virtually all newer digital modes use USB. RTTY via AFSK is the notable exception that uses LSB (G2E01), but that's a legacy convention. The WSJT-X suite (which runs FT8, FT4, JT65, JT9) is designed for USB operation. Using the wrong sideband would invert the audio spectrum and make decoding impossible. When your software says 'USB,' believe it.

### G2E06
**What is the most common frequency shift for RTTY emissions in the amateur HF bands?**
- A) 85 Hz
- **B) 170 Hz** ✅
- C) 425 Hz
- D) 850 Hz

> The most common RTTY frequency shift on amateur HF is 170 Hz. This is the spacing between the mark and space tones (G8C11). The 170 Hz shift is an amateur convention — commercial RTTY often uses 425 Hz or 850 Hz shifts, but amateur RTTY standardized on 170 Hz because it keeps the signal narrow and allows more stations to fit in the band. Standard amateur RTTY uses 45.45 baud with 170 Hz shift on a 2125/2295 Hz tone pair (for AFSK). The 85 Hz option is too narrow for standard RTTY, and 425/850 Hz are commercial standards, not amateur.

### G2E07
**Which of the following is required when using FT8?**
- A) A special hardware modem
- **B) Computer time accurate to within approximately 1 second** ✅
- C) Receiver attenuator set to -12 dB
- D) A vertically polarized antenna

> FT8 requires computer time accurate to within approximately 1 second. FT8's structured protocol depends on precise 15-second time slots — all stations worldwide must be synchronized so transmissions start and stop at the same moment. If your computer clock is off by more than about a second, your transmissions won't align with the time slots and other stations won't decode you. Use NTP (Network Time Protocol) or GPS to keep your clock accurate. FT8 does NOT require a special hardware modem (just a sound card), does NOT need receiver attenuation set to -12 dB, and does NOT require vertical polarization. Time accuracy is the critical requirement.

### G2E08
**In what segment of the 20-meter band are most digital mode operations commonly found?**
- A) At the bottom of the slow-scan TV segment, near 14.230 MHz
- B) At the top of the SSB phone segment, near 14.325 MHz
- C) In the middle of the CW segment, near 14.100 MHz
- **D) Between 14.070 MHz and 14.100 MHz** ✅

> Most digital mode operations on the 20-meter band are found between 14.070 MHz and 14.100 MHz. This segment sits between the CW portion (below 14.070) and the voice portion (above 14.150) of the band. Within this range, you'll find FT8 around 14.074 MHz (G2E15), RTTY near 14.080-14.090 MHz, PSK31 around 14.070 MHz, and various other digital modes. It's NOT near 14.230 MHz (that's SSTV), NOT near 14.325 MHz (that's the middle of the phone band), and NOT near 14.100 MHz (that's a beacon frequency — G1E10, stay away). Know where digital modes live on 20 meters.

### G2E09
**How do you join a contact between two stations using the PACTOR protocol?**
- A) Send broadcast packets containing your call sign while in MONITOR mode
- B) Transmit a steady carrier until the PACTOR protocol times out and disconnects
- **C) Joining an existing contact is not possible, PACTOR connections are limited to two stations** ✅
- D) Send a NAK code

> You cannot join an existing PACTOR contact — PACTOR connections are limited to two stations. PACTOR is a point-to-point ARQ protocol; it establishes a dedicated link between exactly two stations that exchange data packets with acknowledgments (G8C05-06). There's no provision for a third station to jump in. This is fundamentally different from a phone QSO or packet radio net where multiple stations can participate. If you need to contact one of the stations, you have to wait until their PACTOR session ends. Sending broadcast packets, transmitting a carrier, or sending NAK won't get you into an active PACTOR link.

### G2E10
**Which of the following is a way to establish contact with a digital messaging system gateway station?**
- A) Send an email to the system control operator
- B) Send QRL in Morse code
- C) Respond when the station broadcasts its SSID
- **D) Transmit a connect message on the station’s published frequency** ✅

> To establish contact with a digital messaging system gateway station, transmit a connect message on the station's published frequency. Gateway stations (like Winlink RMS gateways — G2E13) publish their operating frequencies in directories. You tune to their frequency and initiate a connection using the appropriate protocol (VARA, PACTOR, or packet). You don't email the operator, don't send QRL in Morse code, and gateways don't broadcast SSIDs like Wi-Fi access points. The connection process is protocol-specific: your Winlink client software handles the connect sequence once you select the gateway and frequency.

### G2E11
**What is the primary purpose of an Amateur Radio Emergency Data Network (AREDN) mesh network?**
- A) To provide FM repeater coverage in remote areas
- B) To provide real time propagation data by monitoring amateur radio transmissions worldwide
- **C) To provide high-speed data services during an emergency or community event** ✅
- D) To provide DX spotting reports to aid contesters and DXers

> AREDN (Amateur Radio Emergency Data Network) mesh networks provide high-speed data services during emergencies or community events. AREDN uses repurposed commercial Wi-Fi hardware on amateur microwave bands (900 MHz, 2.4 GHz, 5.8 GHz) to create self-healing mesh networks (G8C09) that can carry IP-based services — VoIP phones, video feeds, email, situational awareness maps, and other data-heavy applications. It's NOT for FM repeater coverage, NOT for propagation monitoring (that's WSPR — G8C02), and NOT for DX spotting. AREDN fills the gap when internet infrastructure fails during disasters.

### G2E12
**Which of the following describes Winlink?**
- A) An amateur radio wireless network to send and receive email on the internet
- B) A form of Packet Radio
- C) A wireless network capable of both VHF and HF band operation
- **D) All of the above** ✅

> Winlink is ALL of the described things: an amateur radio wireless network for sending and receiving email on the internet, a form of packet radio (at its core, it uses packet-based digital protocols), and capable of operating on both VHF and HF bands. Winlink connects amateur stations to the internet email system through gateway stations (G2E13). You can send email from a remote location with no internet access by connecting via HF radio to a Winlink gateway, which forwards your message to the internet. It supports multiple connection protocols: VARA, PACTOR, packet, and ARDOP. All three descriptions are accurate, so the answer is 'All of the above.'

### G2E13
**What is another name for a Winlink Remote Message Server?**
- A) Terminal Node Controller
- **B) Gateway** ✅
- C) RJ-45
- D) Printer/Server

> A Winlink Remote Message Server is also called a gateway. The RMS (Remote Message Server) is the station that bridges between amateur radio and the internet — it receives your radio-transmitted email and forwards it to the internet, and vice versa. The term 'gateway' makes sense because it's literally the gateway between the radio world and the internet world. It's NOT a Terminal Node Controller (TNC — that's a hardware device for packet radio), NOT an RJ-45 (that's an Ethernet connector), and definitely NOT a printer/server. Gateway = Winlink RMS.

### G2E14
**What could be wrong if you cannot decode an RTTY or other FSK signal even though it is apparently tuned in properly?**
- A) The mark and space frequencies may be reversed
- B) You may have selected the wrong baud rate
- C) You may be listening on the wrong sideband
- **D) All these choices are correct** ✅

> ALL of the listed problems could prevent decoding an RTTY or FSK signal: mark and space frequencies may be reversed (called 'inverted'), you may have selected the wrong baud rate, or you may be listening on the wrong sideband. Each of these would make the signal look correct on your waterfall but be undecodable. Reversed mark/space is common when one station uses USB and another uses LSB for RTTY. Wrong baud rate means the timing is off (G8C04 — Baudot code uses specific start/stop timing). Wrong sideband inverts the entire audio spectrum. All three are real troubleshooting steps when RTTY won't decode.

### G2E15
**Which of the following is a common location for FT8?**
- A) Anywhere in the voice portion of the band
- B) Anywhere in the CW portion of the band
- **C) Approximately 14.074 MHz to 14.077 MHz** ✅
- D) Approximately 14.110 MHz to 14.113 MHz

> FT8 on the 20-meter band is commonly found at approximately 14.074 MHz to 14.077 MHz. This is within the digital mode segment of 20 meters (G2E08: 14.070-14.100 MHz) and is the specific slice where FT8 activity is concentrated. FT8 signals are narrow (~50 Hz each) but there can be dozens active simultaneously in this 3 kHz window. It's NOT in the voice portion, NOT in the CW segment, and NOT near 14.110 MHz (which is above the digital segment). The 14.074 MHz frequency is worth memorizing — it's one of the most active frequencies in all of amateur radio, with thousands of contacts made there daily.
