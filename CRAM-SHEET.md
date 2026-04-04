# General Class License Cram Sheet

One page of key facts for the morning of your exam.

## HF Privileges (General)

| Band | CW/Data | Phone | Max Power |
|------|---------|-------|-----------|
| 160m | 1.800-2.000 MHz | 1.800-2.000 MHz | 1500W |
| 80m | 3.525-3.600 MHz | 3.800-4.000 MHz | 1500W |
| 75m | — | 3.800-4.000 MHz | 1500W |
| 40m | 7.025-7.125 MHz | 7.175-7.300 MHz | 1500W |
| 30m | 10.100-10.150 MHz | — | **200W** |
| 20m | 14.025-14.150 MHz | 14.225-14.350 MHz | 1500W |
| 17m | 18.068-18.110 MHz | 18.110-18.168 MHz | 1500W |
| 15m | 21.025-21.200 MHz | 21.275-21.450 MHz | 1500W |
| 12m | 24.890-24.930 MHz | 24.930-24.990 MHz | 1500W |
| 10m | 28.000-28.500 MHz | 28.300-29.700 MHz | 1500W |
| **60m** | — | **See channels below** | **100W ERP** |

## Key Formulas

**Reactance:**
- Xc = 1 / (2πfC) — capacitive
- Xl = 2πfL — inductive

**Resonance:** fr = 1 / (2π√LC)

**Dipole length:** 468 / f(MHz) = length in feet

**Transformer:** Vp/Vs = Np/Ns = Is/Ip

**Power:**
- P = IE
- P = I²R
- P = E²/R
- PEP = V_peak² / (2R) — **use V_peak, NOT V_peak-to-peak**

**AC relationships:**
- Vp-p = 2 × Vpeak
- Vrms = Vpeak × 0.707

## Modulation

| Mode | Bandwidth | Efficiency |
|------|-----------|------------|
| CW | ~150 Hz | Very high |
| SSB | ~2.4 kHz | High |
| AM | ~6 kHz | Low (33%) |
| FM | ~12-15 kHz | Medium |

## Propagation

- **D layer:** Absorbs HF during day, gone at night
- **E layer:** Sporadic-E for VHF, single hop ~1,200 miles
- **F2 layer:** Main long-distance layer, single hop ~2,500 miles
- **Critical frequency:** Max freq reflecting vertically
- **MUF:** 3-4 × critical frequency
- **Skip zone:** Between ground wave and sky wave
- **K-index:** 0-1 = quiet, 5+ = storm (geomagnetic disturbance)
- **NVIS:** 40m, low horizontal antenna → regional (0-400 mi) coverage

## Operating

- **USB:** 20m and above
- **LSB:** 40m and below
- **CW:** Lower end of each band
- **Digital:** Varies, typically narrow slices

## Amplifier Classes

| Class | Efficiency | Use |
|-------|-----------|-----|
| A | ~25% | Audio, low distortion |
| B | ~60% | Push-pull RF |
| C | ~80% | CW/FM, high efficiency |

## Antennas

- **Dipole:** Figure-8 pattern, ~72Ω
- **Yagi:** Directional, reflector behind, directors in front
- **Vertical:** Omnidirectional, needs radials
- **1/4 wave vertical:** Needs good ground system

## Safety

- **Ground rod:** 8 ft minimum
- **RF exposure:** Follows inverse square law
- **First aid:** Call 911, ensure power off first
- **Fusing:** Protect the wire at the source

## RF Connectors

| Connector | Max Frequency | Notes |
|-----------|--------------|-------|
| BNC | 4 GHz | Common on test equipment |
| Type N | 10 GHz | Weatherproof, UHF/microwave |
| SMA | 18+ GHz | Small, precision |
| PL-259/SO-239 | ~150 MHz | HF standard (UHF connector) |

## Quick Conversions

- 1 MHz = 1000 kHz
- Wavelength (m) = 300 / f(MHz)
- 1 S-unit = 6 dB (4× power)

## 60m Band — Channelized Operation

| Channel | Center Frequency | Usage |
|---------|-----------------|-------|
| 1 | 5330.5 kHz | USB, CW, digital (100W ERP max) |
| 2 | 5346.5 kHz | USB, CW, digital (100W ERP max) |
| 3 | 5357.0 kHz | USB, CW, digital (100W ERP max) |
| 4 | 5371.5 kHz | USB, CW, digital (100W ERP max) |
| 5 | 5403.5 kHz | USB, CW, digital (100W ERP max) |

Plus: 5.3515–5.3665 MHz (15 kHz segment, USB, CW, digital, 100W ERP max)

> ⚠️ **60m is channelized** — no operation below 5330.5 kHz or above 5403.5 kHz except the 15 kHz segment. No phone below 5365 kHz.

Good luck on your exam! 🎓
