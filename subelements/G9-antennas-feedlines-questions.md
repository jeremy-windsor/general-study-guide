# G9 — Antennas and Feed Lines
*4 questions on the exam from a pool of 46*

## Group G9A — Antenna feed point impedance; antenna efficiency; half-wavelength dipole; quarter-wavelength vertical; radiation patterns; polarization; effect of ground

### G9A01
**Which of the following factors determine the characteristic impedance of a parallel conductor feed line?**
- **A) The distance between the centers of the conductors and the radius of the conductors** ✅
- B) The distance between the centers of the conductors and the length of the line
- C) The radius of the conductors and the frequency of the signal
- D) The frequency of the signal and the length of the line

> The characteristic impedance of a parallel conductor feed line (like ladder line or window line) is determined by the distance between the centers of the conductors and the radius of the conductors. The formula involves the ratio of spacing to conductor radius: Z₀ = 276 × log(D/r), where D is the center-to-center distance and r is the conductor radius. Wider spacing increases impedance; fatter conductors decrease it. Notice what's NOT in the formula: frequency and length. Characteristic impedance is a property of the line's geometry and the dielectric between conductors — it doesn't change with how long the line is or what frequency you're using. This is a fundamental concept from G5: impedance is about the ratio of voltage to current, and in a transmission line that ratio is set by physical dimensions.

### G9A02
**What is the relationship between high standing wave ratio (SWR) and transmission line loss?**
- A) There is no relationship between transmission line loss and SWR
- **B) High SWR increases loss in a lossy transmission line** ✅
- C) High SWR makes it difficult to measure transmission line loss
- D) High SWR reduces the relative effect of transmission line loss

> High SWR increases loss in a lossy transmission line. Here's the mechanism: when SWR is high, reflected power bounces back and forth between the antenna and transmitter. Each time the signal travels through the feed line, it loses some energy to the line's inherent attenuation. With high SWR, the signal makes multiple passes through the line (forward and reflected), so the total loss adds up. A perfect 1:1 SWR means the signal passes through the line once and is fully absorbed by the antenna — minimum loss. At 5:1 SWR, a significant portion of the power bounces back and forth, and each pass through the lossy line eats more energy. The key insight: SWR loss is proportional to BOTH the SWR ratio AND the line's matched-line loss. Low-loss line (like ladder line) can tolerate high SWR much better than lossy coax because there's less attenuation per pass.

### G9A03
**What is the nominal characteristic impedance of “window line” transmission line?**
- A) 50 ohms
- B) 75 ohms
- C) 100 ohms
- **D) 450 ohms** ✅

> Window line (also called ladder line or open-wire line) has a nominal characteristic impedance of 450 ohms. The 'windows' are the rectangular cutouts in the plastic spacer between the two conductors — they reduce the amount of dielectric material, which lowers loss. At 450 ohms, window line has much higher impedance than coax (50 or 75 ohms), but it also has much lower loss. The tradeoff: you can't run it near metal objects, it's harder to route through walls, and it needs an antenna tuner to match to a 50-ohm radio. But for multiband wire antennas, window line's low loss makes it an excellent choice — especially when the SWR may be high on some bands (see G9A02 for why low-loss line handles high SWR better).

### G9A04
**What causes reflected power at an antenna’s feed point?**
- A) Operating an antenna at its resonant frequency
- B) Using more transmitter power than the antenna can handle
- **C) A difference between feed line impedance and antenna feed point impedance** ✅
- D) Feeding the antenna with unbalanced feed line

> Reflected power at an antenna's feed point is caused by a difference between the feed line impedance and the antenna feed point impedance. This is the fundamental impedance mismatch concept from G5: when a traveling wave hits a boundary where impedance changes, some energy reflects back. If the feed line is 50 ohms and the antenna presents 50 ohms, all the power is absorbed — no reflection, SWR 1:1. If the antenna presents 200 ohms to a 50-ohm line, there's a mismatch, power reflects, and SWR rises (to 4:1 in this case — see G9A09). Operating at resonance minimizes this mismatch for a dipole, but resonance alone doesn't guarantee a match if the antenna's natural impedance differs from the line. The fix: impedance matching networks, antenna tuners, or choosing an antenna design with a feed point impedance close to the line impedance.

### G9A05
**How does the attenuation of coaxial cable change with increasing frequency?**
- A) Attenuation is independent of frequency
- **B) Attenuation increases** ✅
- C) Attenuation decreases
- D) Attenuation follows Marconi’s Law of Attenuation

> Coaxial cable attenuation increases with frequency. This happens because of two mechanisms: conductor loss (skin effect forces RF current into a thinner surface layer at higher frequencies, increasing resistance) and dielectric loss (the insulating material between center conductor and shield absorbs more energy at higher frequencies). The increase follows roughly a square-root relationship — doubling the frequency increases loss by about 40%. This is why coax that works great on 80 meters may be unacceptably lossy on 2 meters. For example, RG-8 might lose 1 dB per 100 feet at 10 MHz but 3+ dB at 150 MHz. Always check your coax loss at the highest frequency you'll use, not the lowest. Feed line loss is expressed in dB per 100 feet (G9A06).

### G9A06
**In what units is RF feed line loss usually expressed?**
- A) Ohms per 1,000 feet
- B) Decibels per 1,000 feet
- C) Ohms per 100 feet
- **D) Decibels per 100 feet** ✅

> RF feed line loss is expressed in decibels per 100 feet. Decibels (from G5B) give you a logarithmic ratio that makes it easy to calculate total loss: if your coax loses 2 dB per 100 feet and you have 50 feet, you lose about 1 dB. If you have 200 feet, you lose about 4 dB. The 'per 100 feet' convention makes it easy to scale. Remember from G5B10 that each dB of loss costs you about 20% of your power — so 3 dB of feed line loss means half your transmitter power is heating your coax instead of radiating from your antenna. The unit is NOT ohms per anything (that would be resistance, not attenuation) — it's decibels, which express a power ratio.

### G9A07
**What must be done to prevent standing waves on a feed line connected to an antenna?**
- A) The antenna feed point must be at DC ground potential
- B) The feed line must be an odd number of electrical quarter wavelengths long
- C) The feed line must be an even number of physical half wavelengths long
- **D) The antenna feed point impedance must be matched to the characteristic impedance of the feed line** ✅

> To prevent standing waves on a feed line, the antenna feed point impedance must be matched to the characteristic impedance of the feed line. Standing waves are created by reflected power — and reflected power comes from impedance mismatch (G9A04). When the impedances match perfectly, all power flows from the source to the load with no reflection, and the voltage and current are uniform along the line — no standing waves. The feed line length doesn't matter (neither odd quarter wavelengths nor even half wavelengths will fix a mismatch), and DC ground potential is irrelevant to RF impedance matching. The impedance match is what matters — everything else is a distractor.

### G9A08
**If the SWR on an antenna feed line is 5:1, and a matching network at the transmitter end of the feed line is adjusted to present a 1:1 SWR to the transmitter, what is the resulting SWR on the feed line?**
- A) 1:1
- **B) 5:1** ✅
- C) Between 1:1 and 5:1 depending on the characteristic impedance of the line
- D) Between 1:1 and 5:1 depending on the reflected power at the transmitter

> The SWR on the feed line remains 5:1 even if a matching network at the transmitter presents 1:1 to the transmitter. This is a critical concept that trips people up: a matching network at the transmitter end (like an antenna tuner) transforms the impedance so the transmitter sees 50 ohms and is happy — but it does NOTHING to change the mismatch between the feed line and the antenna at the other end. The standing waves on the line are still there. The reflected power still bounces back and forth. The tuner just ensures the transmitter can deliver power into the system without folding back. This is why an antenna tuner doesn't reduce feed line loss from SWR (G9A02) — the line still carries reflected power. The only way to reduce SWR on the feed line is to fix the mismatch at the antenna end.

### G9A09
**What standing wave ratio results from connecting a 50-ohm feed line to a 200-ohm resistive load?**
- **A) 4:1** ✅
- B) 1:4
- C) 2:1
- D) 1:2

> SWR = Z_load / Z_line (when load > line) = 200/50 = 4:1. SWR is always expressed as a ratio greater than or equal to 1:1 — you always divide the larger impedance by the smaller one. It doesn't matter which is bigger; the mismatch is the same whether the load is 4× the line impedance or 1/4 of it. A 200-ohm load on a 50-ohm line gives 4:1. A 12.5-ohm load on a 50-ohm line also gives 4:1. SWR tells you HOW MUCH mismatch exists, not which direction. The '1:4' option would imply the SWR is less than 1:1, which isn't physically possible. Always put the bigger number first.

### G9A10
**What standing wave ratio results from connecting a 50-ohm feed line to a 10-ohm resistive load?**
- A) 2:1
- B) 1:2
- C) 1:5
- **D) 5:1** ✅

> SWR = Z_line / Z_load (when line > load) = 50/10 = 5:1. Same principle as G9A09 — divide the larger impedance by the smaller one. Here the 50-ohm line is higher than the 10-ohm load, so SWR = 50/10 = 5:1. Whether the load is too high or too low relative to the line, SWR just measures the ratio of mismatch. A 5:1 SWR means significant mismatch — most transmitters would reduce power or refuse to transmit at this SWR level. You'd need a matching network or antenna adjustment to bring this down to a usable level.

### G9A11
**What is the effect of transmission line loss on SWR measured at the input to the line?**
- **A) Higher loss reduces SWR measured at the input to the line** ✅
- B) Higher loss increases SWR measured at the input to the line
- C) Higher loss increases the accuracy of SWR measured at the input to the line
- D) Transmission line loss does not affect the SWR measurement

> Higher transmission line loss reduces the SWR measured at the input to the line. This sounds counterintuitive but makes sense: the SWR meter at the input sees both forward power (going to the antenna) and reflected power (coming back from the antenna). The reflected power has to travel all the way to the antenna AND all the way back — passing through the lossy line twice. By the time it gets back to the meter, it's been attenuated by twice the line loss. Less reflected power at the meter means lower apparent SWR. This is why a long run of lossy coax can 'hide' a bad SWR — the meter shows 2:1 while the actual SWR at the antenna is 10:1. The loss masks the problem. Extremely lossy line (like a dummy load) would show 1:1 SWR regardless of what's at the other end — because no reflected power survives the round trip. This is a trap, not a feature.

## Group G9B — Feed lines: types; attenuation vs. frequency; SWR concepts; SWR protection; weather protection; coaxial cable connectors

### G9B01
**What is a characteristic of a random-wire HF antenna connected directly to the transmitter?**
- A) It must be longer than 1 wavelength
- **B) Station equipment may carry significant RF current** ✅
- C) It produces only vertically polarized radiation
- D) It is more effective on the lower HF bands than on the higher bands

> A random-wire antenna connected directly to the transmitter can cause station equipment to carry significant RF current. Without a proper ground plane or balanced feed system, the antenna uses whatever is available as the 'other half' — your radio chassis, power supply, mic cable, and even you. RF current flows on equipment cases, through audio cables, and across your operating desk, causing RFI (radio frequency interference), hot microphone shells, and erratic transceiver behavior. This is why antenna tuners and proper grounding are essential with random-wire antennas. The wire doesn't need to be any specific length, doesn't produce only vertical polarization, and isn't inherently better on lower bands. The defining characteristic is the RF-in-the-shack problem.

### G9B02
**Which of the following is a common way to adjust the feed point impedance of an elevated quarter-wave ground-plane vertical antenna to be approximately 50 ohms?**
- A) Slope the radials upward
- **B) Slope the radials downward** ✅
- C) Lengthen the radials beyond one wavelength
- D) Coil the radials

> Sloping the radials downward adjusts an elevated quarter-wave ground-plane vertical's feed point impedance to approximately 50 ohms. A quarter-wave vertical with horizontal radials has a feed point impedance of about 36 ohms — too low for a good match to 50-ohm coax. Angling the radials downward (typically 30-45°) increases the impedance by changing the geometry of the current distribution and the angle between the radiating element and the ground plane. Think of it as stretching the antenna's effective dimensions. Sloping radials upward would decrease the impedance further. Lengthening or coiling the radials changes their resonant frequency, not the feed point impedance in the way needed here. This drooping-radial trick is one of the simplest impedance matching techniques in antenna design.

### G9B03
**Which of the following best describes the radiation pattern of a quarter-wave ground-plane vertical antenna?**
- A) Bi-directional in azimuth
- B) Isotropic
- C) Hemispherical
- **D) Omnidirectional in azimuth** ✅

> A quarter-wave ground-plane vertical antenna has an omnidirectional radiation pattern in azimuth — it radiates equally in all horizontal directions. This makes sense physically: a vertical antenna is symmetrical around its axis, so there's no preferred horizontal direction. The radiation pattern is shaped like a donut around the antenna, with maximum radiation at low elevation angles (good for DX) and a null straight up. It is NOT bi-directional (that's a dipole in free space), NOT isotropic (an isotropic antenna is a theoretical point source radiating equally in ALL directions including up and down), and NOT hemispherical. Omnidirectional means equal in all horizontal directions — but the elevation pattern is NOT uniform.

### G9B04
**What is the radiation pattern of a dipole antenna in free space in a plane containing the conductor?**
- **A) It is a figure-eight at right angles to the antenna** ✅
- B) It is a figure-eight off both ends of the antenna
- C) It is a circle (equal radiation in all directions)
- D) It has a pair of lobes on one side of the antenna and a single lobe on the other side

> A dipole's radiation pattern in free space, in the plane containing the conductor, is a figure-eight at right angles to the antenna. Maximum radiation is broadside — perpendicular to the wire. Minimum radiation (nulls) are off the ends of the wire. This figure-eight pattern is one of the most fundamental concepts in antenna theory. The key phrase in the question is 'in a plane containing the conductor' — this is asking for the H-plane (or azimuthal) pattern. Looking down at a dipole oriented north-south, you'd see maximum radiation east and west, nulls north and south. In three dimensions, the free-space dipole pattern looks like a donut around the wire. It is NOT a circle (that would mean equal radiation off the ends, which doesn't happen), and it doesn't have asymmetric lobes.

### G9B05
**How does antenna height affect the azimuthal radiation pattern of a horizontal dipole HF antenna at elevation angles higher than about 45 degrees?**
- A) If the antenna is too high, the pattern becomes unpredictable
- B) Antenna height has no effect on the pattern
- **C) If the antenna is less than 1/2 wavelength high, the azimuthal pattern is almost omnidirectional** ✅
- D) If the antenna is less than 1/2 wavelength high, radiation off the ends of the wire is eliminated

> When a horizontal dipole is less than 1/2 wavelength above ground, the azimuthal radiation pattern at high elevation angles (above about 45°) becomes almost omnidirectional. At low heights, ground reflections fill in the nulls off the ends of the dipole. The figure-eight pattern that exists in free space gets blurred by ground interactions until the antenna radiates nearly equally in all horizontal directions — at high angles. This is actually useful for NVIS (Near Vertical Incidence Skywave, G9D01) communication where you want high-angle radiation for short-skip contacts within a few hundred miles. The pattern doesn't become unpredictable (it follows well-understood physics), height definitely affects it, and the end-fire nulls don't vanish completely at all angles — they fill in specifically at higher elevation angles.

### G9B06
**Where should the radial wires of a ground-mounted vertical antenna system be placed?**
- A) As high as possible above the ground
- B) Parallel to the antenna element
- **C) On the surface or buried a few inches below the ground** ✅
- D) At the center of the antenna

> The radials of a ground-mounted vertical antenna should be placed on the surface of the ground or buried a few inches below it. Ground-mounted radials serve as the antenna's ground plane, providing a low-loss return path for RF currents. They work best when they're at or just below the surface — close enough to interact with the ground's conduction currents. Unlike elevated radials (where a few work well), ground-mounted radial systems benefit from quantity — 32 to 120 radials, each about 1/4 wavelength long, create an effective ground screen. They should NOT be elevated high (that changes the antenna type), NOT parallel to the vertical element (useless orientation), and NOT at the center of the antenna (they radiate outward from the base). Bury them just under the lawn and forget about them.

### G9B07
**How does the feed point impedance of a horizontal 1/2 wave dipole antenna change as the antenna height is reduced to 1/10 wavelength above ground?**
- A) It steadily increases
- **B) It steadily decreases** ✅
- C) It peaks at about 1/8 wavelength above ground
- D) It is unaffected by the height above ground

> The feed point impedance of a horizontal half-wave dipole steadily decreases as the antenna height is reduced to 1/10 wavelength above ground. In free space, a half-wave dipole has about 73 ohms feed point impedance. As you lower it toward the ground, ground reflections change the current distribution on the antenna, and the impedance drops. At 1/4 wavelength height, it's around 50-60 ohms (convenient for coax!). Below that, it keeps dropping — at 1/10 wavelength, it can be as low as 15-20 ohms. This happens because the antenna's image in the ground (from reflection) couples to the real antenna and modifies its impedance. The closer to ground, the stronger the coupling, the lower the impedance. This is one reason very low dipoles are harder to match to 50-ohm coax.

### G9B08
**How does the feed point impedance of a 1/2 wave dipole change as the feed point is moved from the center toward the ends?**
- **A) It steadily increases** ✅
- B) It steadily decreases
- C) It peaks at about 1/8 wavelength from the end
- D) It is unaffected by the location of the feed point

> The feed point impedance of a half-wave dipole steadily increases as the feed point moves from the center toward the ends. At the center, impedance is about 73 ohms (in free space). At the ends, the impedance approaches several thousand ohms. This is because current is maximum at the center and decreases toward the ends, while voltage is minimum at the center and increases toward the ends. Since impedance = voltage/current (from G5), moving the feed point toward the ends means more voltage and less current — higher impedance. This principle is used in off-center-fed dipoles (like the Windom antenna) to achieve specific impedance values for matching purposes. An end-fed half-wave antenna (G9D02) has very high impedance because you're feeding at the voltage maximum.

### G9B09
**Which of the following is an advantage of using a horizontally polarized as compared to a vertically polarized HF antenna?**
- **A) Lower ground losses** ✅
- B) Lower feed point impedance
- C) Shorter radials
- D) Lower radiation resistance

> Horizontally polarized HF antennas have lower ground losses compared to vertically polarized antennas. A vertical antenna requires current flow in the ground (or radial system) to complete the circuit — and real ground has significant resistance, which dissipates power as heat. A horizontal antenna's currents are in the wire above ground, and while it uses ground reflections, the ground currents are less intense and less critical. This means a horizontal dipole strung up in the trees can be very efficient even without a ground system, while a vertical antenna without a good radial system can lose 50% or more of its power to ground losses. The practical takeaway: if you can't install a proper radial system, a horizontal antenna may be more efficient.

### G9B10
**What is the approximate length for a 1/2 wave dipole antenna cut for 14.250 MHz?**
- A) 8 feet
- B) 16 feet
- C) 24 feet
- **D) 33 feet** ✅

> For a half-wave dipole at 14.250 MHz: length (feet) = 468 / frequency (MHz) = 468 / 14.250 = 32.8 ≈ 33 feet. The formula 468/f gives the approximate length of a half-wave dipole in feet. The 468 constant accounts for the velocity factor of a wire in free space (the wave travels slightly slower on a wire than in free space, making the antenna about 5% shorter than a true half wavelength). 14.250 MHz is in the middle of the 20-meter band — the workhorse DX band (G3A07). A 33-foot dipole is a manageable size for most backyards, which is one reason 20 meters is so popular for new General class operators.

### G9B11
**What is the approximate length for a 1/2 wave dipole antenna cut for 3.550 MHz?**
- A) 42 feet
- B) 84 feet
- **C) 132 feet** ✅
- D) 263 feet

> For a half-wave dipole at 3.550 MHz: length (feet) = 468 / 3.550 = 131.8 ≈ 132 feet. Same formula as G9B10, but at 80 meters the antenna is MUCH longer. 132 feet of wire is a serious span — you need a big yard or creative installation to fit an 80-meter dipole. This is why the lower HF bands are sometimes called 'real estate bands' — the antennas are physically large. Many operators use inverted-V configurations (G9D12) or shortened (loaded) antennas when space is limited. Compare the 33-foot 20m dipole to this 132-foot 80m dipole — four times the frequency means four times shorter.

### G9B12
**What is the approximate length for a 1/4 wave monopole antenna cut for 28.5 MHz?**
- **A) 8 feet** ✅
- B) 11 feet
- C) 16 feet
- D) 21 feet

> For a quarter-wave monopole at 28.5 MHz: length (feet) = 234 / frequency (MHz) = 234 / 28.5 = 8.2 ≈ 8 feet. The formula 234/f gives the approximate quarter-wave length in feet — it's exactly half of the 468/f dipole formula because a quarter wave is half of a half wave. 28.5 MHz is in the 10-meter band, so an 8-foot vertical for 10 meters is very manageable — it could even be a mobile whip antenna. Compare this to an 80-meter quarter-wave vertical which would be about 66 feet tall (234/3.55). Frequency and physical size are inversely proportional — higher frequency means smaller antennas.

## Group G9C — Directional antennas: Yagi; quad; stacking; NVIS; mobile; effects of ground; portable HF antennas

### G9C01
**Which of the following would increase the bandwidth of a Yagi antenna?**
- **A) Larger-diameter elements** ✅
- B) Closer element spacing
- C) Loading coils in series with the element
- D) Tapered-diameter elements

> Larger-diameter elements increase the bandwidth of a Yagi antenna. Thicker elements have a lower Q (quality factor), which from G5 means a broader resonance curve — the antenna's impedance and pattern change more slowly across frequency. Think of a thin wire resonator as a sharp tuning fork (narrow bandwidth, high Q) and a fat tube resonator as a dull thud (wide bandwidth, low Q). This is why commercial Yagi antennas use aluminum tubing rather than wire for elements. Closer element spacing actually narrows bandwidth. Loading coils add narrowband resonances. Tapered-diameter elements (thinner at the tips) are used to reduce weight and wind load, not specifically to increase bandwidth.

### G9C02
**What is the approximate length of the driven element of a Yagi antenna?**
- A) 1/4 wavelength
- **B) 1/2 wavelength** ✅
- C) 3/4 wavelength
- D) 1 wavelength

> The driven element of a Yagi antenna is approximately 1/2 wavelength long. The driven element is essentially a dipole — it's the element connected to the feed line, and it resonates at approximately a half wavelength, just like any center-fed dipole. The reflector behind it is slightly longer than 1/2 wavelength (about 5% longer), and the director(s) in front are slightly shorter (about 5% shorter). But the driven element itself is close to 1/2 wavelength — the same dipole antenna you'd calculate using 468/f (from G9B10-11). It's not 1/4 wavelength (that's a vertical monopole), not 3/4 wavelength (that's a different, less common antenna type), and not a full wavelength.

### G9C03
**How do the lengths of a three-element Yagi reflector and director compare to that of the driven element?**
- **A) The reflector is longer, and the director is shorter** ✅
- B) The reflector is shorter, and the director is longer
- C) They are all the same length
- D) Relative length depends on the frequency of operation

> In a three-element Yagi, the reflector is longer and the director is shorter than the driven element. The mnemonic: reflectors are 'fat and lazy' (longer, behind the action) and directors are 'lean and eager' (shorter, pointing toward the target). The reflector is about 5% longer than the driven element and sits behind it. The director is about 5% shorter and sits in front. This length relationship is what creates the Yagi's directional pattern — the reflector acts like a mirror behind the driven element, and the director acts like a lens focusing energy forward. If you reverse the lengths, you reverse the direction of maximum radiation. The lengths are NOT all the same, and they don't depend on operating frequency in terms of their relative proportions.

### G9C04
**How does antenna gain in dBi compare to gain stated in dBd for the same antenna?**
- A) Gain in dBi is 2.15 dB lower
- **B) Gain in dBi is 2.15 dB higher** ✅
- C) Gain in dBd is 1.25 dBd lower
- D) Gain in dBd is 1.25 dBd higher

> Gain expressed in dBi is 2.15 dB higher than the same gain expressed in dBd. The 'd' in dBd means 'relative to a dipole' and the 'i' in dBi means 'relative to an isotropic (theoretical point source) radiator.' A dipole already has 2.15 dBi of gain over an isotropic source, so any antenna measured against the dipole reference starts 2.15 dB lower. Example: a Yagi with 7 dBd gain is 9.15 dBi gain — it's the same antenna, just measured against a different reference. Watch for this in antenna advertisements: manufacturers sometimes quote gain in dBi to make numbers look bigger. When comparing antennas, make sure you're using the same reference. Always add 2.15 to convert dBd to dBi, or subtract 2.15 to go from dBi to dBd.

### G9C05
**What is the primary effect of increasing boom length and adding directors to a Yagi antenna?**
- **A) Gain increases** ✅
- B) Beamwidth increases
- C) Front-to-back ratio decreases
- D) Resonant frequency is lower

> Increasing boom length and adding directors to a Yagi antenna increases gain. More directors mean more elements focusing RF energy forward into a narrower beam — like adding more lenses to a telescope. A longer boom spaces these elements further apart, allowing more efficient interaction between them. Each additional director typically adds less gain than the previous one (diminishing returns), but a long-boom Yagi with many directors can achieve impressive gain — 10-15+ dBd for VHF/UHF designs. Beamwidth actually DECREASES (narrows), not increases, because the energy is more concentrated. Front-to-back ratio generally improves (increases), not decreases. And the resonant frequency is set by element lengths, not boom length — adding directors doesn't lower it.

### G9C07
**What does “front-to-back ratio” mean in reference to a Yagi antenna?**
- A) The number of directors versus the number of reflectors
- B) The relative position of the driven element with respect to the reflectors and directors
- **C) The power radiated in the major lobe compared to that in the opposite direction** ✅
- D) The ratio of forward gain to dipole gain

> Front-to-back ratio is the power radiated in the major (forward) lobe compared to the power radiated in the opposite direction. It's expressed in dB. A Yagi with 20 dB front-to-back ratio radiates 100 times more power forward than backward. This is important for two reasons: it concentrates your signal toward the target (gain), and it reduces interference from behind you (quieter receive). Front-to-back ratio is NOT about the number of directors vs. reflectors (that describes element count), NOT about element positioning relative to the driven element (that's the physical layout), and NOT the ratio of forward gain to dipole gain (that's just gain in dBd). It's specifically about forward-to-backward power comparison.

### G9C08
**What is meant by the “main lobe” of a directive antenna?**
- A) The magnitude of the maximum vertical angle of radiation
- B) The point of maximum current in a radiating antenna element
- C) The maximum voltage standing wave point on a radiating element
- **D) The direction of maximum radiated field strength from the antenna** ✅

> The main lobe of a directive antenna is the direction of maximum radiated field strength from the antenna. It's the primary beam — where most of the antenna's energy goes. For a Yagi, the main lobe points from the reflector through the directors (forward). The main lobe is NOT a voltage or current maximum on the elements (that's a standing wave concept from G9A, not a radiation pattern concept), and it's NOT the maximum vertical angle (the main lobe can be at any elevation angle depending on antenna design and height). When someone says 'point your beam at Europe,' they mean aim the main lobe toward Europe.

### G9C09
**In free space, how does the gain of two three-element, horizontally polarized Yagi antennas spaced vertically 1/2 wavelength apart typically compare to the gain of a single three-element Yagi?**
- A) Approximately 1.5 dB higher
- **B) Approximately 3 dB higher** ✅
- C) Approximately 6 dB higher
- D) Approximately 9 dB higher

> Two Yagis stacked vertically 1/2 wavelength apart produce approximately 3 dB more gain than a single Yagi. From G5B01, doubling power equals +3 dB. Two identical antennas properly phased and fed equally each contribute their full gain, and the combined aperture is twice as large — effectively doubling the power density in the main lobe direction. The 3 dB rule applies whenever you double the effective antenna aperture. It's not 1.5 dB (that would be for improperly phased or spaced arrays), not 6 dB (you'd need four antennas for that — double the doubling), and not 9 dB (that would require eight antennas). Each doubling of antenna count adds about 3 dB, assuming proper phasing and spacing.

### G9C10
**Which of the following can be adjusted to optimize forward gain, front-to-back ratio, or SWR bandwidth of a Yagi antenna?**
- A) The physical length of the boom
- B) The number of elements on the boom
- C) The spacing of each element along the boom
- **D) All these choices are correct** ✅

> ALL of the listed factors — physical boom length, number of elements, and element spacing — can be adjusted to optimize a Yagi's forward gain, front-to-back ratio, or SWR bandwidth. Yagi design is a complex optimization problem where all these parameters interact. Longer boom → more gain but harder to manage mechanically. More elements → more gain but with diminishing returns. Spacing affects the coupling between elements, which determines the balance between gain, front-to-back ratio, and impedance bandwidth. Professional Yagi designers use computer modeling to find the best combination for their goals. You can't optimize one parameter without affecting the others — it's always a set of tradeoffs.

### G9C11
**What is a beta or hairpin match?**
- **A) A shorted transmission line stub placed at the feed point of a Yagi antenna to provide impedance matching** ✅
- B) A 1/4 wavelength section of 75-ohm coax in series with the feed point of a Yagi to provide impedance matching
- C) A series capacitor selected to cancel the inductive reactance of a folded dipole antenna
- D) A section of 300-ohm twin-lead transmission line used to match a folded dipole antenna

> A beta match (also called a hairpin match) is a shorted transmission line stub placed at the feed point of a Yagi antenna to provide impedance matching. A Yagi's driven element typically has a lower impedance than 50 ohms (often 20-30 ohms) due to the mutual coupling from nearby parasitic elements. The hairpin match is a short piece of transmission line (bent into a U or 'hairpin' shape) that acts as a shunt inductor. When combined with the slightly capacitive reactance of a shortened driven element, this inductor provides an impedance transformation to 50 ohms. It's a simple, elegant solution — just a piece of wire bent into a U, no separate components needed. It's NOT a quarter-wave coax section (that's a different matching technique) and NOT a series capacitor.

### G9C12
**Which of the following is a characteristic of using a gamma match with a Yagi antenna?**
- **A) It does not require the driven element to be insulated from the boom** ✅
- B) It does not require any inductors or capacitors
- C) It is useful for matching multiband antennas
- D) All these choices are correct

> A gamma match allows the driven element to remain electrically connected to (not insulated from) the boom. This is a significant practical advantage because it simplifies mechanical construction — the element can be clamped directly to the boom without insulating hardware. The gamma match uses a parallel rod alongside the driven element, connected at one end to the element and at the other to the feed line through a series capacitor. It works by tapping the element off-center (similar in concept to moving the feed point of a dipole, as in G9B08) to find a point where the impedance matches the feed line. The gamma match DOES require components (a capacitor for tuning), so it's NOT component-free. And it's designed for single-band use, NOT multiband matching.

## Group G9D — Specialized antennas: loop; Beverage; phased; multi-band; stealth; mobile and receive-only

### G9D01
**Which of the following antenna types will be most effective as a near vertical incidence skywave (NVIS) antenna for short-skip communications on 40 meters during the day?**
- **A) A horizontal dipole placed between 1/10 and 1/4 wavelength above the ground** ✅
- B) A vertical antenna placed between 1/4 and 1/2 wavelength above the ground
- C) A horizontal dipole placed at approximately 1/2 wavelength above the ground
- D) A vertical dipole placed at approximately 1/2 wavelength above the ground

> A horizontal dipole placed between 1/10 and 1/4 wavelength above ground is most effective for NVIS (Near Vertical Incidence Skywave) on 40 meters. NVIS works by launching signals nearly straight up, where they reflect off the F layer and come back down within a few hundred miles — filling the gap between ground wave and long-distance skip (see G3C10). A LOW horizontal antenna radiates most of its energy at high angles (nearly straight up), which is exactly what NVIS needs. At 1/10 to 1/4 wavelength height on 40 meters, that's roughly 4-10 meters (13-33 feet) above ground. A vertical antenna is wrong for NVIS because verticals radiate at LOW angles (good for DX, terrible for NVIS). A dipole at 1/2 wavelength height also has too much low-angle radiation. Keep it low and horizontal for NVIS.

### G9D02
**What is the feed point impedance of an end-fed half-wave antenna?**
- A) Very low
- B) Approximately 50 ohms
- C) Approximately 300 ohms
- **D) Very high** ✅

> An end-fed half-wave antenna has very high feed point impedance — typically several thousand ohms. From G9B08, we know that impedance increases as you move the feed point from the center toward the end of a dipole. At the very end, you're feeding at the voltage maximum and current minimum — that's the definition of high impedance (Z = V/I from G5). This is why end-fed half-wave (EFHW) antennas always need a matching transformer (typically a 49:1 or 64:1 ratio) to bring the impedance down to 50 ohms for the feed line. The high impedance is NOT 'approximately 50 ohms' and NOT 'approximately 300 ohms' — it's thousands of ohms. An EFHW is basically a center-fed dipole where you've slid the feed point all the way to one end.

### G9D03
**In which direction is the maximum radiation from a VHF/UHF “halo” antenna?**
- A) Broadside to the plane of the halo
- B) Opposite the feed point
- **C) Omnidirectional in the plane of the halo** ✅
- D) On the same side as the feed point

> A VHF/UHF halo antenna radiates omnidirectionally in the plane of the halo. A halo is essentially a dipole bent into a circular loop (not a full loop — the ends don't touch), mounted horizontally. Because it's a bent dipole, it maintains horizontal polarization, but bending it into a circle makes the radiation pattern omnidirectional in the horizontal plane — unlike a straight dipole's figure-eight pattern (G9B04). This makes halos useful for horizontally polarized omnidirectional coverage on VHF/UHF, where satellite and SSB work uses horizontal polarization. The radiation is NOT broadside to the halo plane (that would be like a full loop), NOT only opposite the feed point, and NOT only on the feed point side.

### G9D04
**What is the primary function of antenna traps?**
- **A) To enable multiband operation** ✅
- B) To notch spurious frequencies
- C) To provide balanced feed point impedance
- D) To prevent out-of-band operation

> Antenna traps enable multiband operation. A trap is a parallel LC circuit inserted into an antenna element at a specific point. At the trap's resonant frequency, it presents very high impedance — effectively cutting the antenna at that point, making it shorter for that frequency. At frequencies below resonance, the trap acts as a loading coil, electrically lengthening the antenna. This allows a single antenna to work on multiple bands: for example, a trapped dipole might be 33 feet for 20 meters (traps isolating the outer sections) and use the full length with loading for 40 meters. Traps don't notch out spurious frequencies (that's a filter's job), don't provide balanced impedance, and don't prevent out-of-band operation — they enable multi-frequency resonance.

### G9D05
**What is an advantage of vertically stacking horizontally polarized Yagi antennas?**
- A) It allows quick selection of vertical or horizontal polarization
- B) It allows simultaneous vertical and horizontal polarization
- C) It narrows the main lobe in azimuth
- **D) It narrows the main lobe in elevation** ✅

> Vertically stacking horizontally polarized Yagi antennas narrows the main lobe in elevation. When you stack antennas vertically, you're increasing the antenna array's vertical aperture. A larger vertical aperture produces a narrower elevation beam — the same physics that makes a longer Yagi have a narrower azimuthal beam (G9C05). Narrowing the elevation pattern concentrates more energy at lower takeoff angles, which is ideal for DX on HF or for reducing QRM from high-angle signals. The azimuthal pattern stays roughly the same (the horizontal aperture hasn't changed). Stacking does NOT allow polarization switching (both antennas are the same polarization), doesn't provide simultaneous V and H polarization, and doesn't narrow the azimuthal pattern — it specifically narrows elevation.

### G9D06
**Which of the following is an advantage of a log-periodic antenna?**
- **A) Wide bandwidth** ✅
- B) Higher gain per element than a Yagi antenna
- C) Harmonic suppression
- D) Polarization diversity

> The primary advantage of a log-periodic antenna is wide bandwidth. A log-periodic dipole array (LPDA) can cover a frequency range of 2:1 or more — for example, 14-30 MHz in a single antenna. It achieves this because at any given frequency, only a portion of the array's elements are active (those close to resonance at that frequency). As you change frequency, a different set of elements becomes active. The tradeoff: a log-periodic has LESS gain per element than a Yagi because many of its elements are not contributing at any given frequency. It doesn't suppress harmonics, doesn't provide polarization diversity, and it has lower gain than a comparable-sized Yagi on any single frequency. But if you need one antenna to cover many bands, a log-periodic is hard to beat.

### G9D07
**Which of the following describes a log-periodic antenna?**
- **A) Element length and spacing vary logarithmically along the boom** ✅
- B) Impedance varies periodically as a function of frequency
- C) Gain varies logarithmically as a function of frequency
- D) SWR varies periodically as a function of boom length

> A log-periodic antenna has element lengths and spacing that vary logarithmically along the boom. Each successive element is longer than the previous one by a constant ratio (called tau, τ), and the spacing between elements also increases by the same ratio. This logarithmic progression is what gives the antenna its name and its wideband characteristic — the structure is self-similar at different scales, so it behaves similarly across a wide frequency range. The impedance does NOT vary periodically (it stays relatively constant — that's the whole point), gain does NOT vary logarithmically with frequency (it stays roughly constant), and SWR doesn't vary periodically with boom length. The defining feature is the logarithmic scaling of physical dimensions.

### G9D08
**How does a “screwdriver” mobile antenna adjust its feed point impedance?**
- A) By varying its body capacitance
- **B) By varying the base loading inductance** ✅
- C) By extending and retracting the whip
- D) By deploying a capacitance hat

> A 'screwdriver' mobile antenna adjusts its feed point impedance by varying the base loading inductance. The name comes from the motorized mechanism that adjusts the inductance — a motor (originally operated by an electric screwdriver) moves a contact along a coil, changing how much inductance is in the circuit. More inductance = lower resonant frequency (tunes to lower bands). Less inductance = higher resonant frequency (tunes to higher bands). The coil is at the base of the antenna, making it a base-loaded vertical. It doesn't vary body capacitance (that's not adjustable), doesn't extend/retract the whip (though some designs combine both), and a capacitance hat is a fixed top-loading device, not the primary tuning mechanism. The variable inductor is the screwdriver antenna's defining feature.

### G9D09
**What is the primary use of a Beverage antenna?**
- **A) Directional receiving for MF and low HF bands** ✅
- B) Directional transmitting for low HF bands
- C) Portable direction finding at higher HF frequencies
- D) Portable direction finding at lower HF frequencies

> A Beverage antenna is primarily used for directional receiving on the MF and low HF bands. It's a very long wire (typically 1-8 wavelengths) suspended low over the ground, terminated with a resistor at the far end. The Beverage works as a traveling-wave antenna — it absorbs signals arriving from the terminated end and receives signals from the unterminated end, giving it a directional pattern. It's an excellent receive antenna because its long length provides gain and directivity on the lower bands where noise is the limiting factor. However, it's a poor transmitting antenna because most of the power is absorbed by the termination resistor and ground losses. It's NOT for directional transmitting, and NOT for direction finding (loop antennas are used for DF — see G9D10). Beverage antennas are favorites among low-band DXers who have the acreage.

### G9D10
**In which direction or directions does an electrically small loop (less than 1/10 wavelength in circumference) have nulls in its radiation pattern?**
- A) In the plane of the loop
- **B) Broadside to the loop** ✅
- C) Broadside and in the plane of the loop
- D) Electrically small loops are omnidirectional

> An electrically small loop (less than 1/10 wavelength in circumference) has nulls broadside to the loop — meaning signals arriving perpendicular to the plane of the loop are rejected. Maximum reception is in the plane of the loop (off the edges). This is the opposite of a full-wavelength loop, where maximum radiation IS broadside. The small loop's pattern is similar to a dipole's figure-eight (G9B04), but rotated: where a dipole has nulls off its ends, a small loop has nulls perpendicular to its face. These sharp nulls make small loops excellent for direction finding — rotate the loop until the signal disappears (you've found the null, and the signal source is perpendicular to the loop plane). Small loops are NOT omnidirectional — their directional properties are their most useful feature.

### G9D11
**Which of the following is a disadvantage of multiband antennas?**
- A) They present low impedance on all design frequencies
- B) They must be used with an antenna tuner
- C) They must be fed with open wire line
- **D) They have poor harmonic rejection** ✅

> Multiband antennas have poor harmonic rejection. Because a multiband antenna is designed to resonate on multiple frequencies, it naturally resonates on harmonics too. A single-band antenna for 40 meters might present a high SWR on 20 meters (the second harmonic), naturally suppressing harmonic radiation. But a multiband antenna designed for both 40m AND 20m will happily radiate on both — including any harmonic energy from your transmitter. This means you're more reliant on your transmitter's low-pass filtering to suppress harmonics. Multiband antennas don't necessarily present low impedance on all frequencies (impedance varies), don't require an antenna tuner (they're designed to match without one), and don't require open-wire feed line (most use coax). Their downside is specifically harmonic radiation.

### G9D12
**What is the common name of a dipole with a single central support?**
- **A) Inverted V** ✅
- B) Inverted L
- C) Sloper
- D) Lazy H

> A dipole with a single central support is called an inverted V. Instead of being supported at both ends with a horizontal run between them, an inverted-V dipole hangs from a single center point (the apex), with the wire sloping downward on both sides — forming a V shape when viewed from the side (inverted because the point is up). This is one of the most popular amateur antennas because it needs only one support — a single mast, tree, or flagpole at the center. The legs droop at 30-45° angles. The radiation pattern is similar to a flat dipole but slightly more omnidirectional (the drooping fills in the nulls somewhat, similar to the low-height effect in G9B05). An inverted L is a different antenna (vertical section plus horizontal), a sloper is a single tilted wire, and a Lazy H is a stacked pair of horizontal dipoles.
