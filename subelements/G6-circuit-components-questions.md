# G6 — Circuit Components
*2 questions on the exam from a pool of 23*

## Group G6A — Resistors; capacitors; inductors; rectifiers; solid-state diodes and transistors; vacuum tubes; batteries

### G6A01
**What is the minimum allowable discharge voltage for maximum life of a standard 12-volt lead-acid battery?**
- A) 6 volts
- B) 8.5 volts
- **C) 10.5 volts** ✅
- D) 12 volts

> A standard 12-volt lead-acid battery should never be discharged below 10.5 volts if you want maximum service life. Lead-acid batteries suffer permanent damage from deep discharge — the lead sulfate crystals that form on the plates during discharge become hard and crystalline (sulfation) if left too long or taken too low, and they won't convert back during recharging. 10.5V is the widely accepted cutoff for a 12V battery (about 1.75V per cell for a 6-cell battery). Going to 8.5V or 6V is deep abuse that dramatically shortens battery life.

### G6A02
**What is an advantage of batteries with low internal resistance?**
- A) Long life
- **B) High discharge current** ✅
- C) High voltage
- D) Rapid recharge

> A battery with low internal resistance can deliver high discharge current. Think of internal resistance as a bottleneck inside the battery — when you draw current, some voltage drops across this internal resistance (V_drop = I × R_internal), reducing what's available to your load. Low internal resistance means less voltage drop under load, so the battery can push more current without sagging. This is why lithium and AGM batteries (low internal resistance) are preferred for high-current applications like powering a 100W transceiver. Internal resistance doesn't directly affect battery life, voltage rating, or recharge speed.

### G6A03
**What is the approximate forward threshold voltage of a germanium diode?**
- A) 0.1 volt
- **B) 0.3 volts** ✅
- C) 0.7 volts
- D) 1.0 volts

> A germanium diode has a forward threshold voltage of approximately 0.3 volts. This is the voltage you need to apply across the diode before it starts conducting significantly. Compare this to silicon at 0.7V — germanium's lower threshold makes it useful in low-signal detector circuits where you can't afford to lose 0.7V. The tradeoff is that germanium diodes have higher reverse leakage current and are less thermally stable than silicon. Memorize the pair: germanium = 0.3V, silicon = 0.7V.

### G6A04
**Which of the following is characteristic of an electrolytic capacitor?**
- A) Tight tolerance
- B) Much less leakage than any other type
- **C) High capacitance for a given volume** ✅
- D) Inexpensive RF capacitor

> Electrolytic capacitors pack a lot of capacitance into a small volume — that's their defining advantage. They achieve this by using an extremely thin oxide layer as the dielectric (the insulating layer between plates). The tradeoff: they're polarized (must be installed with correct polarity), have loose tolerances (±20% is typical), relatively high leakage current, and limited frequency response — making them unsuitable for RF work. You'll find them in power supply filtering where you need hundreds or thousands of microfarads in a reasonable size.

### G6A05
**What is the approximate forward threshold voltage of a silicon junction diode?**
- A) 0.1 volt
- B) 0.3 volts
- **C) 0.7 volts** ✅
- D) 1.0 volts

> A silicon junction diode has a forward threshold voltage of approximately 0.7 volts. This is the most common diode type in electronics and the voltage you'll encounter most often. Below 0.7V, the diode essentially blocks current; above 0.7V, it conducts freely. The 0.7V drop remains roughly constant regardless of how much current flows (within limits). Pair this with the germanium value: silicon = 0.7V, germanium = 0.3V. The exam tests both.

### G6A06
**Why should wire-wound resistors not be used in RF circuits?**
- A) The resistor’s tolerance value would not be adequate
- **B) The resistor’s inductance could make circuit performance unpredictable** ✅
- C) The resistor could overheat
- D) The resistor’s internal capacitance would detune the circuit

> Wire-wound resistors are literally coils of resistance wire — and a coil of wire is an inductor. At DC or low frequencies, this parasitic inductance doesn't matter. But at radio frequencies, the inductance becomes significant and makes the resistor behave unpredictably — its impedance changes with frequency, it may resonate at certain frequencies, and it throws off the performance of tuned circuits. For RF work, use carbon composition, metal film, or metal oxide resistors instead — they have minimal parasitic inductance.

### G6A07
**What are the operating points for a bipolar transistor used as a switch?**
- **A) Saturation and cutoff** ✅
- B) The active region (between cutoff and saturation)
- C) Peak and valley current points
- D) Enhancement and depletion modes

> When a bipolar transistor is used as a switch, it operates at two extremes: saturation (fully ON) and cutoff (fully OFF). In saturation, the transistor conducts as hard as it can — collector-to-emitter acts almost like a short circuit. In cutoff, no current flows — it acts like an open circuit. The active region (between these extremes) is used for linear amplification, not switching. Enhancement and depletion modes are MOSFET terms, not bipolar transistor terms. Peak and valley current points relate to tunnel diodes.

### G6A08
**Which of the following is characteristic of low voltage ceramic capacitors?**
- A) Tight tolerance
- B) High stability
- C) High capacitance for given volume
- **D) Comparatively low cost** ✅

> Low-voltage ceramic capacitors are comparatively low cost — that's their standout characteristic. They're cheap to manufacture, widely available, and good enough for many general-purpose applications. However, they don't have tight tolerance (values can drift significantly with temperature and applied voltage), they're not particularly stable (especially Y5V and Z5U types), and they don't offer especially high capacitance for their size (electrolytics beat them there). For precision or stability, you'd choose an NP0/C0G ceramic or a mica capacitor — but those cost more.

### G6A09
**Which of the following describes MOSFET construction?**
- A) The gate is formed by a back-biased junction
- **B) The gate is separated from the channel by a thin insulating layer** ✅
- C) The source is separated from the drain by a thin insulating layer
- D) The source is formed by depositing metal on silicon

> In a MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor), the gate is separated from the channel by a thin insulating layer — specifically, a silicon dioxide (SiO₂) layer. This is the 'oxide' in MOSFET and it's the defining feature of the device. Because the gate is insulated, virtually no current flows into the gate — MOSFETs have extremely high input impedance. Compare this to a JFET, where the gate IS a back-biased junction (not insulated), or a bipolar transistor, where base current is required. The insulated gate is why MOSFETs are so sensitive to static discharge — that thin oxide layer can be punctured by ESD.

### G6A10
**Which element of a vacuum tube regulates the flow of electrons between cathode and plate?**
- **A) Control grid** ✅
- B) Suppressor grid
- C) Screen grid
- D) Trigger electrode

> The control grid regulates electron flow in a vacuum tube. It sits between the cathode (which emits electrons when heated) and the plate (which collects them). By varying the voltage on the control grid, you control how many electrons get through — a small voltage change on the grid produces a large change in plate current, which is how tubes amplify. The screen grid (in tetrodes and pentodes) reduces plate-to-grid capacitance. The suppressor grid (in pentodes) reduces secondary emission. Don't confuse these — the control grid is the one that actually controls amplification.

### G6A11
**What happens when an inductor is operated above its self-resonant frequency?**
- A) Its reactance increases
- B) Harmonics are generated
- **C) It becomes capacitive** ✅
- D) Catastrophic failure is likely

> Every real inductor has some parasitic capacitance between its windings. At low frequencies, the inductance dominates and the component behaves as expected — like an inductor. But at the self-resonant frequency, the parasitic capacitance resonates with the inductance (just like an LC circuit). Above that frequency, the capacitance dominates and the inductor actually becomes capacitive — its reactance decreases with increasing frequency instead of increasing. This is why you must choose inductors rated for your operating frequency. An inductor used above its self-resonant frequency isn't really an inductor anymore.

### G6A12
**What is the primary purpose of a screen grid in a vacuum tube?**
- **A) To reduce grid-to-plate capacitance** ✅
- B) To increase efficiency
- C) To increase the control grid resistance
- D) To decrease plate resistance

> The screen grid's primary purpose is to reduce the capacitance between the control grid and the plate. In a triode (three-element tube), there's significant capacitance between the grid and plate, which causes unwanted feedback and oscillation — especially at higher frequencies. The screen grid, placed between the control grid and plate, acts as an electrostatic shield that dramatically reduces this coupling capacitance. This is why tetrodes (four-element tubes with a screen grid) were developed — they're much more stable at RF frequencies than triodes.

## Group G6B — Analog and digital integrated circuits (ICs); microprocessors; memory; I/O devices; microwave ICs (MMICs); display devices; connectors; ferrite cores

### G6B01
**What determines the performance of a ferrite core at different frequencies?**
- A) Its conductivity
- B) Its thickness
- **C) The composition, or “mix,” of materials used** ✅
- D) The ratio of outer diameter to inner diameter

> Ferrite core performance at different frequencies is determined by the composition or 'mix' of materials used to make the core. Ferrite is a ceramic compound of iron oxide mixed with other metal oxides (like manganese, zinc, or nickel), and different recipes produce different magnetic properties. Mix 43, for example, works well from 10 MHz to 1 GHz for EMI suppression, while Mix 61 is designed for 200 kHz to 10 MHz inductors. The physical dimensions (thickness, diameter ratios) affect inductance, but it's the material composition that determines which frequency range the core works best in.

### G6B02
**What is meant by the term MMIC?**
- A) Multi-Mode Integrated Circuit
- **B) Monolithic Microwave Integrated Circuit** ✅
- C) Metal Monolayer Integrated Circuit
- D) Mode Modulated Integrated Circuit

> MMIC stands for Monolithic Microwave Integrated Circuit. 'Monolithic' means the entire circuit — transistors, resistors, capacitors, transmission lines — is fabricated on a single semiconductor chip (usually gallium arsenide, GaAs). These are designed specifically for microwave frequencies (typically above 1 GHz) where conventional ICs can't keep up. You'll find MMICs in satellite receivers, cell phones, and microwave amateur radio equipment. The other answer choices are made-up acronyms.

### G6B03
**Which of the following is an advantage of CMOS integrated circuits compared to TTL integrated circuits?**
- **A) Low power consumption** ✅
- B) High power handling capability
- C) Better suited for RF amplification
- D) Better suited for power supply regulation

> CMOS (Complementary Metal-Oxide-Semiconductor) circuits consume very low power compared to TTL (Transistor-Transistor Logic). CMOS uses complementary pairs of MOSFETs that draw almost zero current when in a static state — power is only consumed during switching transitions. TTL circuits use bipolar transistors that draw continuous current even when not switching. This makes CMOS ideal for battery-powered devices and any application where power consumption matters. Neither CMOS nor TTL is designed for RF amplification or power supply regulation — those are analog tasks, not digital logic functions.

### G6B04
**What is a typical upper frequency limit for low SWR operation of 50-ohm BNC connectors?**
- A) 50 MHz
- B) 500 MHz
- **C) 4 GHz** ✅
- D) 40 GHz

> BNC connectors maintain low SWR up to about 4 GHz. BNC (Bayonet Neill-Concelman) is a quick-connect bayonet-style RF connector commonly used on test equipment, lower-power transceivers, and lab instruments. The 4 GHz limit is where the connector's geometry starts to cause significant impedance mismatches and radiation losses. Below 4 GHz, it's a reliable 50-ohm connector. For higher frequencies, you'd move to SMA or Type N connectors. For HF through UHF amateur use, BNC is more than adequate.

### G6B05
**What is an advantage of using a ferrite core toroidal inductor?**
- A) Large values of inductance may be obtained
- B) The magnetic properties of the core may be optimized for a specific range of frequencies
- C) Most of the magnetic field is contained in the core
- **D) All these choices are correct** ✅

> A ferrite core toroidal inductor offers all three listed advantages: large inductance values are obtainable, the core material can be optimized for specific frequency ranges (through different ferrite mixes), and the toroidal (donut) shape contains most of the magnetic field within the core — meaning less stray coupling to nearby components. The self-shielding property of toroids is especially valuable in amateur radio where multiple circuits live close together on a circuit board or inside a compact enclosure. This is why toroids are the go-to inductor form for homebrew projects.

### G6B06
**What kind of device is an integrated circuit operational amplifier?**
- A) Digital
- B) MMIC
- C) Programmable Logic
- **D) Analog** ✅

> An operational amplifier (op-amp) is an analog device. It amplifies continuous signals with extremely high gain and is the workhorse of analog circuit design — used for amplification, filtering, buffering, and mathematical operations on signals. It's NOT digital (digital deals with discrete 0/1 states), NOT an MMIC (those are specifically for microwave frequencies), and NOT programmable logic (that's FPGAs and CPLDs). The classic 741 op-amp has been in production since the 1960s. Modern ham radio equipment uses op-amps in audio stages, AGC circuits, and active filters.

### G6B07
**Which of the following describes a type N connector?**
- **A) A moisture-resistant RF connector useful to 10 GHz** ✅
- B) A small bayonet connector used for data circuits
- C) A low noise figure VHF connector
- D) A nickel plated version of the PL-259

> The Type N connector is a moisture-resistant, threaded RF connector usable up to 10 GHz. It was designed by Paul Neill (the 'N') for military and professional applications where weatherproofing matters. The threaded coupling provides a reliable, vibration-resistant connection. It's a larger connector than BNC or SMA, commonly seen on commercial antenna systems and higher-quality amateur installations. It is NOT a bayonet connector (that's BNC), NOT a low-noise VHF connector (that's not a thing), and NOT a nickel-plated PL-259 (the PL-259/SO-239 is a completely different connector design).

### G6B08
**How is an LED biased when emitting light?**
- A) In the tunnel-effect region
- B) At the Zener voltage
- C) Reverse biased
- **D) Forward biased** ✅

> An LED emits light when it is forward biased — meaning current flows from anode to cathode in the normal direction. When electrons cross the junction and recombine with holes, they release energy as photons (light). The color depends on the semiconductor material and the band gap energy. Reverse biasing an LED doesn't produce light (and too much reverse voltage damages it). Zener voltage is a property of Zener diodes operated in reverse breakdown, and the tunnel effect relates to tunnel diodes — neither applies to LED light emission.

### G6B10
**How does a ferrite bead or core reduce common-mode RF current on the shield of a coaxial cable?**
- **A) By creating an impedance in the current’s path** ✅
- B) It converts common-mode current to differential mode current
- C) By creating an out-of-phase current to cancel the common-mode current
- D) Ferrites expel magnetic fields

> A ferrite bead or core reduces common-mode RF current by creating an impedance in the current's path. The ferrite material has high magnetic permeability — when common-mode current flows through the cable, it creates a magnetic field in the ferrite which opposes the current (impedance). For differential-mode signals (the desired signal), the magnetic fields from the two conductors cancel inside the ferrite, so the desired signal passes through unaffected. This selective impedance is why ferrite chokes are so effective at suppressing RF interference on cables without degrading the wanted signal. They don't convert modes, cancel currents, or expel fields — they simply add impedance.

### G6B11
**What is an SMA connector?**
- A) A type-S to type-M adaptor
- **B) A small threaded connector suitable for signals up to several GHz** ✅
- C) A connector designed for serial multiple access signals
- D) A type of push-on connector intended for high-voltage applications

> SMA (SubMiniature version A) is a small threaded connector designed for signals up to several GHz — typically rated to 18 GHz or higher depending on the variant. It's widely used on SDR dongles, handheld transceivers, VHF/UHF equipment, and test instruments where a compact, reliable microwave-capable connection is needed. The threaded coupling ensures a consistent 50-ohm impedance match. SMA is NOT an adaptor, NOT for serial data, and NOT a push-on high-voltage connector. You'll see SMA connectors everywhere in modern amateur radio equipment, especially anything above VHF.

### G6B12
**Which of these connector types is commonly used for low frequency or dc signal connections to a transceiver?**
- A) PL-259
- B) BNC
- **C) RCA Phono** ✅
- D) Type N

> RCA phono connectors are commonly used for low-frequency or DC signal connections to transceivers — things like audio input/output, external speaker connections, and accessory ports. They're simple, cheap, and adequate for audio frequencies. They are NOT suitable for RF — they're unshielded and have poor impedance characteristics at radio frequencies. PL-259, BNC, and Type N are all RF connectors designed to maintain 50-ohm impedance. If you see an RCA jack on a radio, it's for audio or control signals, not antenna connections.
