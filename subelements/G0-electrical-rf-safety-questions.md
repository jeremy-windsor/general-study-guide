# G0 — Electrical and RF Safety
*2 questions on the exam from a pool of 25*

## Group G0A — RF safety principles; rules and guidelines; routine station evaluation

### G0A01
**What is one way that RF energy can affect human body tissue?**
- **A) It heats body tissue** ✅
- B) It causes radiation poisoning
- C) It causes the blood count to reach a dangerously low level
- D) It cools body tissue

> RF energy heats body tissue — that's its primary biological effect at the power levels amateurs use. Radio waves are non-ionizing radiation, meaning they DON'T have enough energy per photon to break chemical bonds or damage DNA directly (that's ionizing radiation like X-rays and gamma rays). Instead, RF energy causes molecules in tissue to vibrate, generating heat — the same principle as a microwave oven. At amateur power levels, the concern isn't immediate burns but rather sustained exposure to levels that exceed the body's ability to dissipate heat. The eyes and testes are especially vulnerable because they have limited blood flow to carry heat away. RF does NOT cause radiation poisoning (that's nuclear radiation), doesn't affect blood counts, and doesn't cool tissue. Heating is the mechanism — and it's what all the MPE limits in G0A are designed to prevent.

### G0A02
**Which of the following is used to determine RF exposure from a transmitted signal?**
- A) Its duty cycle
- B) Its frequency
- C) Its power density
- **D) All these choices are correct** ✅

> All three factors — duty cycle, frequency, and power density — are used to determine RF exposure. Power density (measured in milliwatts per square centimeter) tells you how much RF energy is hitting a given area. Frequency matters because the body absorbs RF differently at different frequencies — absorption peaks in the 30-300 MHz range where body dimensions match the wavelength, which is why the MPE limits are strictest there. Duty cycle matters because a mode like SSB voice (maybe 20-40% duty cycle) delivers less average energy than a continuous-carrier mode like FM or RTTY at the same peak power (G0A07). The RF exposure evaluation must account for all three — you can't just check one and call it good.

### G0A03
**How can you determine that your station complies with FCC RF exposure regulations?**
- A) By calculation based on FCC OET Bulletin 65
- B) By calculation based on computer modeling
- C) By measurement of field strength using calibrated equipment
- **D) All these choices are correct** ✅

> You can verify compliance with FCC RF exposure regulations using any of these methods: calculation based on FCC OET Bulletin 65, computer modeling, or measurement with calibrated equipment. OET Bulletin 65 provides lookup tables and formulas that let you calculate exposure based on your power, frequency, antenna gain, and distance. Computer modeling (like the ARRL's RF exposure calculator) does the same math automatically. And a calibrated field strength meter with a calibrated antenna (G0A09) gives you actual measured values. Most amateurs use the calculation method because calibrated measurement equipment is expensive. The FCC doesn't mandate one specific method — any valid approach that demonstrates compliance works.

### G0A04
**What does “time averaging” mean when evaluating RF radiation exposure?**
- A) The average amount of power developed by the transmitter over a specific 24-hour period
- B) The average time it takes RF radiation to have any long-term effect on the body
- C) The total time of the exposure
- **D) The total RF exposure averaged over a certain period** ✅

> Time averaging means the total RF exposure is averaged over a specific time period — typically 6 minutes for 'uncontrolled' (general public) environments and 30 minutes for 'controlled' (amateur operator) environments. This matters because amateur transmissions are intermittent: you transmit, then listen, then transmit again. Your peak power during a transmission might exceed MPE limits at a certain distance, but if you're only transmitting 50% of the time (listening the other 50%), the time-averaged exposure is half the peak value. Time averaging recognizes that brief exposures above the limit are acceptable as long as the average over the defined period stays within bounds. It's NOT a 24-hour average, NOT about long-term cumulative effects, and NOT just the total exposure time.

### G0A05
**What must you do if an evaluation of your station shows that the RF energy radiated by your station exceeds permissible limits for possible human absorption?**
- **A) Take action to prevent human exposure to the excessive RF fields** ✅
- B) File an Environmental Impact Statement (EIS-97) with the FCC
- C) Secure written permission from your neighbors to operate above the controlled MPE limits
- D) All these choices are correct

> If your station exceeds permissible RF exposure limits, you must take action to prevent human exposure to the excessive RF fields. This is straightforward and practical — the FCC isn't looking for paperwork, they're looking for results. Actions might include: reducing power, changing antenna location or height, restricting access to high-exposure areas (fencing around the antenna base), changing operating modes to lower duty cycle, or adjusting antenna direction. There's no 'Environmental Impact Statement EIS-97' form (that's made up), and you don't need written permission from neighbors — you need to actually prevent the exposure. The obligation is on YOU to ensure people aren't exposed to excessive RF, not just to document the problem.

### G0A06
**What must you do if your station fails to meet the FCC RF exposure exemption criteria?**
- **A) Perform an RF Exposure Evaluation in accordance with FCC OET Bulletin 65** ✅
- B) Contact the FCC for permission to transmit
- C) Perform an RF exposure evaluation in accordance with World Meteorological Organization guidelines
- D) Use an FCC-approved band-pass filter

> If your station doesn't meet the RF exposure exemption criteria, you must perform an RF Exposure Evaluation in accordance with FCC OET Bulletin 65. The FCC exempts very low-power stations from the evaluation requirement (G0A12 — the threshold is 1 milliwatt time-averaged). If you're above that threshold and don't qualify for exemption, you must do the evaluation. OET Bulletin 65 is the FCC's official guidance document for RF exposure evaluation — it contains the procedures, tables, and formulas. You don't need to contact the FCC for permission, the World Meteorological Organization has nothing to do with RF safety regulations, and a band-pass filter doesn't address RF exposure. OET Bulletin 65 is the answer — memorize it.

### G0A07
**What is the effect of modulation duty cycle on RF exposure?**
- **A) A lower duty cycle permits greater power levels to be transmitted** ✅
- B) A higher duty cycle permits greater power levels to be transmitted
- C) Low duty cycle transmitters are exempt from RF exposure evaluation requirements
- D) High duty cycle transmitters are exempt from RF exposure requirements

> A lower duty cycle permits greater peak power levels because the time-averaged exposure is what matters (G0A04). If you're transmitting 100% of the time (like FM or RTTY), your average power equals your peak power. But if your duty cycle is only 40% (like typical SSB voice — transmit during speech, silent during pauses and listening), the average power is only 40% of peak. Since the MPE limits are based on time-averaged exposure, a lower duty cycle means you can run more peak power while staying within the same average exposure limit. CW has a duty cycle around 40-50%. SSB voice is 20-40%. FM and digital modes like FT8 are near 50% (transmit/receive alternation) or even 100% during the transmit period. Mode choice directly affects your allowed power level.

### G0A08
**Which of the following steps must an amateur operator take to ensure compliance with RF safety regulations?**
- A) Post a copy of FCC Part 97.13 in the station
- B) Notify neighbors within a 100-foot radius of the antenna of the existence of the station and power levels
- **C) Perform a routine RF exposure evaluation and prevent access to any identified high exposure areas** ✅
- D) All these choices are correct

> Amateur operators must perform a routine RF exposure evaluation AND prevent access to any identified high exposure areas. This two-part obligation is the practical core of RF safety compliance: first, evaluate (calculate or measure your station's RF environment), then act on the results (restrict access to areas that exceed MPE limits). You don't just post a copy of Part 97 (that does nothing to prevent exposure). You don't need to notify neighbors within 100 feet (there's no such FCC requirement). And 'all these choices' is wrong because the other options are wrong. The real requirement is: evaluate and mitigate. Do the math, find the danger zones, and keep people out of them.

### G0A09
**What type of instrument can be used to accurately measure an RF field strength?**
- A) A receiver with digital signal processing (DSP) noise reduction
- **B) A calibrated field strength meter with a calibrated antenna** ✅
- C) An SWR meter with a peak-reading function
- D) An oscilloscope with a high-stability crystal marker generator

> A calibrated field strength meter with a calibrated antenna is the instrument that can accurately measure RF field strength. Both the meter AND the antenna must be calibrated — an uncalibrated meter gives you relative readings but not accurate absolute values that you can compare against MPE limits. A DSP receiver measures signal strength relative to its own sensitivity, not in calibrated power density units. An SWR meter measures forward and reflected power on a feed line, not field strength in free space. An oscilloscope with a crystal marker measures frequency and waveform, not field strength. For compliance measurements (G0A03), only a properly calibrated system gives you numbers you can trust and defend to the FCC.

### G0A10
**What should be done if evaluation shows that a neighbor might experience more than the allowable limit of RF exposure from the main lobe of a directional antenna?**
- A) Change to a non-polarized antenna with higher gain
- B) Use an antenna with a higher front-to-back ratio
- **C) Take precautions to ensure that the antenna cannot be pointed in their direction when they are present** ✅
- D) All these choices are correct

> If a neighbor might be exposed to excessive RF from your directional antenna's main lobe, take precautions to ensure the antenna cannot be pointed in their direction when they are present. This is practical and targeted — you're not changing your whole antenna system, just managing the beam direction. A directional antenna concentrates energy in a narrow beam (the main lobe), so the exposure concern is primarily in that direction. If your beam is pointed away from your neighbor's property, they're in the much weaker side lobes or back lobe. A 'non-polarized antenna with higher gain' would make things worse (more gain = more power density). A higher front-to-back ratio helps with signals behind the antenna but doesn't address the main lobe problem. The answer is operational: don't point the beam at people.

### G0A11
**What precaution should be taken if you install an indoor transmitting antenna?**
- A) Locate the antenna close to your operating position to minimize feed-line radiation
- B) Position the antenna along the edge of a wall to reduce parasitic radiation
- **C) Make sure that MPE limits are not exceeded in occupied areas** ✅
- D) Make sure the antenna is properly shielded

> With an indoor transmitting antenna, you must make sure that MPE (Maximum Permissible Exposure) limits are not exceeded in occupied areas. An indoor antenna puts the radiating element very close to people — possibly in the same room. Distance is the most important factor in RF exposure (power density drops with the square of distance), and an indoor antenna eliminates most of that protective distance. You can't rely on walls or floors to shield against RF at HF frequencies — they're largely transparent. The other choices are wrong: locating the antenna close to your operating position INCREASES your exposure (bad). Positioning along a wall doesn't reduce 'parasitic radiation' in any meaningful way. And 'proper shielding' of an antenna defeats the purpose of the antenna — it needs to radiate. The only correct approach: evaluate and ensure MPE limits aren't exceeded where people are.

### G0A12
**What stations are subject to the FCC rules on RF exposure?**
- A) All commercial stations; amateur radio stations are exempt
- B) Only stations with antennas lower than one wavelength above the ground
- C) Only stations transmitting more than 500 watts PEP
- **D) All stations with a time-averaged transmission of more than one milliwatt** ✅

> ALL stations with a time-averaged transmission of more than one milliwatt are subject to FCC RF exposure rules. That's virtually every amateur station — even a QRP rig running 5 watts is 5,000 times above the threshold. The 1 milliwatt threshold is extremely low, meaning the rules apply to essentially everyone. Amateur stations are NOT exempt (choice A is wrong — amateurs are explicitly covered). There's no antenna height exemption (choice B is made up). And the 500-watt threshold (choice C) is way too high — the actual threshold is a million times lower. The practical takeaway: if you have a transmitter, the RF exposure rules apply to you. The question is whether your station qualifies for a simplified evaluation or needs a full one — but the rules always apply.

## Group G0B — Electrical safety; lightning and grounding; fusing; tower safety

### G0B01
**Which wire or wires in a four-conductor 240 VAC circuit should be attached to fuses or circuit breakers?**
- **A) Only the hot wires** ✅
- B) Only the neutral wire
- C) Only the ground wire
- D) All wires

> In a four-conductor 240 VAC circuit (two hots, one neutral, one ground), only the hot wires get fuses or circuit breakers. The neutral wire must never be fused because if the neutral fuse blows while the hots remain connected, you've created a dangerous situation: the circuit appears dead (no current flowing through the load) but the hot wires are still energized. Touching the neutral side of a load could now put you across the full voltage. The ground wire must NEVER be fused — it's the safety path that carries fault current to trip the breaker. If the ground wire fuse blows during a fault, the equipment case stays energized at lethal voltage with no protection. Only the hot wires — the ones carrying the dangerous voltage — get overcurrent protection.

### G0B02
**According to the National Electrical Code, what is the minimum wire size that may be used safely for wiring with a 20-ampere circuit breaker?**
- A) AWG number 20
- B) AWG number 16
- **C) AWG number 12** ✅
- D) AWG number 8

> AWG 12 wire is the minimum for a 20-ampere circuit according to the National Electrical Code (NEC). Wire gauge must match the circuit breaker rating to prevent the wire from overheating before the breaker trips. AWG 12 is rated for 20 amps in typical installations. AWG 14 is only good for 15 amps (G0B03). AWG 16 and AWG 20 are far too thin for a 20-amp circuit — they'd overheat and potentially start a fire before the breaker tripped. AWG 8 would be safe but is overkill (it's rated for 40 amps). Remember: lower AWG numbers mean thicker wire with higher current capacity. The NEC matching: 15A → AWG 14, 20A → AWG 12, 30A → AWG 10.

### G0B03
**Which size of fuse or circuit breaker would be appropriate to use with a circuit that uses AWG number 14 wiring?**
- A) 30 amperes
- B) 25 amperes
- C) 20 amperes
- **D) 15 amperes** ✅

> AWG 14 wire gets a 15-ampere fuse or circuit breaker. This is the complement of G0B02 — the wire gauge and breaker rating must match. AWG 14 is rated for 15 amps. If you put a 20-amp breaker on AWG 14 wire, the wire could overheat and start a fire before the breaker trips — the wire becomes the weakest link. A 30-amp or 25-amp breaker on AWG 14 would be even more dangerous. The NEC pairing: AWG 14 → 15A, AWG 12 → 20A, AWG 10 → 30A. In your ham shack, this matters: if you're wiring a dedicated circuit for a 100-watt transceiver that draws 20+ amps at 13.8V from a power supply, you need at least AWG 12 wire and a 20A breaker on the AC circuit feeding the power supply.

### G0B04
**Where should the station’s lightning protection ground system be located?**
- A) As close to the station equipment as possible
- **B) Outside the building** ✅
- C) Next to the closest power pole
- D) Parallel to the water supply line

> The station's lightning protection ground system should be located outside the building. Lightning carries tens of thousands of amps — you want that current to reach ground by the shortest, most direct path possible WITHOUT passing through your building. Ground rods, bonding conductors, and the connection point for antenna feed line grounds should all be outside, typically at the point where feed lines enter the building. If the lightning ground system were inside, the massive current pulse would travel through your walls, potentially starting fires or damaging everything it passes near. 'As close to station equipment as possible' means inside — wrong. 'Next to the closest power pole' is irrelevant to your station's protection. 'Parallel to water supply' has nothing to do with optimal placement. Outside the building, period.

### G0B05
**Which of the following conditions will cause a ground fault circuit interrupter (GFCI) to disconnect AC power?**
- A) Current flowing from one or more of the hot wires to the neutral wire
- **B) Current flowing from one or more of the hot wires directly to ground** ✅
- C) Overvoltage on the hot wires
- D) All these choices are correct

> A GFCI (Ground Fault Circuit Interrupter) trips when current flows from one or more hot wires directly to ground — bypassing the neutral return path. The GFCI monitors the difference between current flowing out on the hot wire and current returning on the neutral. If they're equal, everything is normal — current is flowing through the load as intended. But if some current is leaking to ground (perhaps through a person who's being electrocuted), the hot and neutral currents won't match, and the GFCI trips — typically in about 5 milliseconds. Hot-to-neutral current flow is NORMAL operation (that's how circuits work), so that won't trip it. GFCIs don't detect overvoltage — that would require a different device (like a surge suppressor). The GFCI specifically detects ground faults — current taking an unintended path to ground.

### G0B06
**Which of the following is covered by the National Electrical Code?**
- A) Acceptable bandwidth limits
- B) Acceptable modulation limits
- **C) Electrical safety of the station** ✅
- D) RF exposure limits of the human body

> The National Electrical Code (NEC) covers the electrical safety of the station — it governs wiring, grounding, circuit protection, and installation practices. The NEC doesn't care about your signal's bandwidth (that's FCC Part 97), doesn't regulate modulation (also Part 97), and doesn't set RF exposure limits for the human body (that's covered by FCC OET Bulletin 65 and Part 1.1310). The NEC is published by the National Fire Protection Association (NFPA) and is adopted by most local jurisdictions as the basis for electrical building codes. For your ham shack, the NEC governs how you wire your outlets, what size wire and breakers to use (G0B02-G0B03), grounding requirements, and general electrical installation safety.

### G0B07
**Which of these choices should be observed when climbing a tower using a safety harness?**
- A) Always hold on to the tower with one hand
- **B) Confirm that the harness is rated for the weight of the climber and that it is within its allowable service life** ✅
- C) Ensure that all heavy tools are securely fastened to the harness
- D) All these choices are correct

> Before climbing a tower, confirm that the safety harness is rated for the weight of the climber AND that it is within its allowable service life. Safety harnesses have both a weight rating and an expiration date — the webbing and stitching degrade over time from UV exposure, wear, and aging. A harness rated for 250 lbs won't safely catch a 300-lb climber. A harness past its service life may have weakened webbing that could fail under load. 'Always hold on with one hand' is terrible advice — you should be attached to the tower via your harness at all times (both hands free for work). Heavy tools should NOT be fastened to the harness — if you fall, the additional weight increases the impact force on the harness. Tools should be hauled up separately. Tower climbing is inherently dangerous — the harness is your last line of defense, and it must be in good condition.

### G0B08
**What should be done before climbing a tower that supports electrically powered devices?**
- A) Notify the electric company that a person will be working on the tower
- **B) Make sure all circuits that supply power to the tower are locked out and tagged** ✅
- C) Unground the base of the tower
- D) All these choices are correct

> Before climbing a tower with electrically powered devices, make sure all circuits that supply power to the tower are locked out and tagged. Lockout/tagout (LOTO) is a standard industrial safety procedure: you physically lock the circuit breaker in the OFF position and attach a tag identifying who locked it and why. This prevents someone from accidentally energizing a circuit while you're working on or near it. Tower-mounted devices might include antenna rotators, tower-mounted amplifiers, obstruction lighting, or remote antenna switches — all potentially lethal if energized while you're climbing. Notifying the electric company is for utility poles, not your personal tower. Ungrounding the base would REMOVE a safety protection. Lock it out, tag it out, then climb.

### G0B09
**Which of the following is true of an emergency generator installation?**
- **A) The generator should be operated in a well-ventilated area** ✅
- B) The generator must be insulated from ground
- C) Fuel should be stored near the generator for rapid refueling in case of an emergency
- D) All these choices are correct

> An emergency generator must be operated in a well-ventilated area. Generators burn fuel (gasoline, propane, or diesel) and produce carbon monoxide (CO) — an odorless, colorless, deadly gas. Running a generator in an enclosed space like a garage, basement, or even a partially enclosed porch can build up lethal CO concentrations in minutes. CO poisoning kills hundreds of people every year, often during power outages when people run generators indoors. The generator does NOT need to be insulated from ground (proper grounding is a safety requirement, not something to avoid). Fuel should NOT be stored near the generator — that's a fire and explosion hazard. Ventilation is the critical safety requirement: outdoors, away from windows and air intakes.

### G0B10
**Which of the following is a danger from lead-tin solder?**
- **A) Lead can contaminate food if hands are not washed carefully after handling the solder** ✅
- B) High voltages can cause lead-tin solder to disintegrate suddenly
- C) Tin in the solder can “cold flow,” causing shorts in the circuit
- D) RF energy can convert the lead into a poisonous gas

> Lead-tin solder's primary danger is lead contamination: lead can contaminate food if you don't wash your hands after handling solder. Lead is a cumulative neurotoxin — it builds up in your body over time and causes neurological damage. The exposure path is simple: handle solder, touch food, ingest lead particles. This is why you should always wash your hands thoroughly after soldering, and never eat, drink, or smoke while soldering. Additionally, solder flux produces irritating fumes that should be ventilated. The other choices are nonsense: high voltage doesn't cause solder to 'disintegrate' (solder melts, it doesn't explode). Tin cold flow is a real metallurgical phenomenon but not a safety danger. And RF does NOT convert lead into poisonous gas — that's not how physics works.

### G0B11
**Which of the following is required for lightning protection ground rods?**
- A) They must be bonded to all buried water and gas lines
- B) Bends in ground wires must be made as close as possible to a right angle
- C) Lightning grounds must be connected to all ungrounded wiring
- **D) They must be bonded together with all other grounds** ✅

> Lightning protection ground rods must be bonded together with all other grounds. This is the single-point ground concept: all ground rods — lightning ground, electrical service ground, station RF ground, cable TV ground — must be bonded together with heavy copper conductors. If they're not bonded, a lightning strike can create massive voltage differences between separate ground systems, driving destructive currents through your equipment (which provides the path between the unconnected grounds). Bonding ensures all grounds rise and fall together during a lightning event, minimizing voltage differences. They should NOT be bonded to buried gas lines (that creates explosion risk). Ground wire bends should be gradual curves, NOT right angles (sharp bends cause lightning to arc across them). And connecting lightning grounds to ungrounded wiring makes no sense and would be dangerous.

### G0B12
**What is the purpose of a power supply interlock?**
- A) To prevent unauthorized changes to the circuit that would void the manufacturer’s warranty
- B) To shut down the unit if it becomes too hot
- **C) To ensure that dangerous voltages are removed if the cabinet is opened** ✅
- D) To shut off the power supply if too much voltage is produced

> A power supply interlock ensures that dangerous voltages are removed if the cabinet is opened. This is the same safety concept as G4C12 — interlocks are mechanical switches that automatically disconnect power when a cover or door is opened, preventing you from touching energized components inside. This is especially critical for high-voltage power supplies used with vacuum tube amplifiers, where plate voltages can exceed 2000 volts — instantly lethal. The interlock doesn't protect warranties (that's a sticker), doesn't monitor temperature (that's a thermal cutout), and doesn't regulate voltage (that's a voltage regulator). Its sole purpose is keeping humans away from lethal voltages — if you can reach in, the power must be off.

### G0B13
**Where should lightning arrestors be located?**
- **A) Where the feed lines enter the building** ✅
- B) On the antenna, opposite the feed point
- C) In series with each ground lead
- D) At the closest power pole ground electrode

> Lightning arrestors should be located where the feed lines enter the building. This is the critical boundary: outside is where lightning energy arrives via the antenna and feed line, and inside is where your expensive (and irreplaceable) equipment lives. The arrestor at the building entry point provides a path to ground for lightning energy BEFORE it enters the building. The arrestor's ground connection goes to the outside lightning ground system (G0B04), which is bonded to all other grounds (G0B11). Putting the arrestor on the antenna itself doesn't protect the feed line run to the building. In series with the ground lead would block the very current you're trying to divert. At the power pole is too far away to protect your station. The building entry point is the last line of defense — everything outside is sacrificial, everything inside is protected.
