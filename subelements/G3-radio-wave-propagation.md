# G3 — Radio Wave Propagation

This is the subelement that separates General operators from Technicians. As a Tech, you mostly dealt with VHF/UHF — line of sight, repeaters, maybe a little satellite work. Now you're stepping into HF, where your signal doesn't just travel to the horizon — it bounces off the sky and lands thousands of miles away. Understanding *how* that works, *when* it works, and *why* it sometimes doesn't is the key to actually using your General privileges.

There are 37 questions in the pool and you'll see 3 on your exam. But this isn't a "memorize and forget" subelement — this is knowledge you'll use every time you turn on your HF radio.

---

## The Ionosphere: Your Sky Mirror

Everything in HF propagation starts with the ionosphere — a region of Earth's upper atmosphere (roughly 60-400 km up) where solar radiation strips electrons from gas molecules, creating layers of ionized gas. These ionized layers can bend (refract) radio waves back toward Earth, making long-distance communication possible.

The ionosphere has multiple layers, stacked from low to high:

| Layer | Altitude | Behavior | When Present |
|-------|----------|----------|-------------|
| **D region** | 60-90 km | **Absorbs** HF signals | Daytime only |
| **E region** | 100-115 km | Refracts some signals | Daytime mainly |
| **F1 region** | 150-200 km | Refracts signals | Daytime (merges with F2 at night) |
| **F2 region** | 250-400 km | **Primary HF reflector** | Day and night |

Remember them in alphabetical order from bottom to top: D, E, F1, F2. The exam asks which is closest to Earth — it's D.

### The D Region: The Villain

The D region doesn't help you — it hurts you. It sits at the bottom of the ionosphere and **absorbs** radio energy rather than refracting it. Lower frequencies get absorbed more than higher ones (the relationship is roughly proportional to 1/f², so 3.5 MHz gets about 4× the absorption of 7 MHz).

The D region exists only during daylight hours — it's created by solar UV and X-ray radiation and disappears quickly after sunset. This single fact explains one of the most important patterns in HF:

> **Why do the lower bands (40m, 80m, 160m) work better at night?** Because the D region disappears. During the day, signals on these frequencies lose most of their energy passing through the D region on their way up to the F2 layer. At night, the D region is gone, and those signals sail through to the F layer unmolested.

The D region is also the most absorbent layer for signals below 10 MHz during daylight hours — the exam asks this directly.

### The F2 Region: The Hero

The F2 region is your primary tool for long-distance HF communication. It's the highest layer, which means:

1. **Longest skip distance** — roughly 2,500 miles per hop (compare to about 1,200 miles for the E region)
2. **Most persistent** — it exists day and night (though it weakens at night)
3. **Supports the highest frequencies** — its peak electron density determines the MUF

The geometry is simple: a higher mirror lets you throw a ball farther. The F2 layer at 300 km altitude reflects your signal in a long arc that can land 2,500 miles away. For longer distances, the signal bounces off the ground and goes back up for another hop (multi-hop propagation). A transatlantic contact (~3,500 miles) typically needs two F2 hops.

### The E Region: The Wild Card

The normal E region sits at about 100 km and supports single-hop distances up to about 1,200 miles. But the really exciting E-region phenomenon is **sporadic E** (Es) — unpredictable patches of intense ionization that can appear at any time and refract signals on surprisingly high frequencies (including 6 meters and occasionally even 2 meters). Sporadic E gives you strong, clear signals within a single hop of about 1,200 miles.

---

## The Sun Drives Everything

Solar activity is the engine behind ionospheric propagation. More solar activity → more UV/X-ray radiation → more ionization → higher frequencies refracted → better HF conditions on the upper bands. Here's how it all connects:

### Sunspots and the Solar Cycle

The Sun goes through an approximately 11-year cycle of activity, measured by sunspot numbers. At solar maximum, you might see sunspot numbers above 200; at solar minimum, they can drop to zero.

**Higher sunspot numbers = better propagation on higher HF bands.** The connection is direct: more sunspots → more UV radiation → more F2 ionization → higher MUF → bands like 15m, 12m, and 10m come alive.

During solar minimum, those upper bands go essentially dead for long-distance work. The bands that suffer most during low solar activity are **15 meters, 12 meters, and 10 meters** — they need the most ionospheric support to function.

But here's the good news: **20 meters works at any point in the solar cycle.** Even during solar minimum, the F2 layer maintains enough ionization to support 14 MHz during daylight hours. This is why 20m is the workhorse DX band — you can always count on it.

### Solar Flux Index (SFI)

The Solar Flux Index is a daily measurement of solar radio emissions at a wavelength of **10.7 centimeters** (2800 MHz), taken from Penticton, British Columbia. SFI correlates well with ionospheric ionization:

- **SFI 64-80:** Solar minimum, only lower bands reliable
- **SFI 100-150:** Moderate activity, 20m and sometimes 15m open
- **SFI 150+:** Excellent conditions, even 10m opens for DX

Don't confuse SFI with the sunspot number — SFI is a direct measurement of solar radiation, while the sunspot number is a visual count of spots on the Sun's surface. They correlate, but they're different measurements.

### The 27-Day Cycle

The Sun rotates on its axis approximately every 26-28 days. Active regions (sunspot groups that produce enhanced radiation) rotate with it. If conditions are good this week because an active region faces Earth, expect similar conditions when that region rotates back around in about 27 days. This creates a predictable monthly pattern that experienced operators exploit — they literally wait for the Sun to bring the "good side" back around.

### Solar Events That Affect Propagation

The Sun doesn't just emit steady radiation — it also has outbursts that can dramatically affect propagation:

**Solar Flares → Sudden Ionospheric Disturbances (SIDs)**
- UV/X-ray radiation arrives at the speed of light: **~8 minutes** from Sun to Earth
- Massively increases D-region ionization on the sunlit side
- **Disrupts lower frequencies more than higher ones** (because D-region absorption is worse at lower frequencies)
- Effect is essentially instantaneous — by the time you hear about the flare, it's already affecting propagation
- Only affects the daytime side of Earth

**Coronal Mass Ejections (CMEs) → Geomagnetic Storms**
- Billions of tons of charged particles launched from the Sun
- Travel at 300-2000 km/s, taking **15 hours to several days** to reach Earth
- Trigger geomagnetic storms when they interact with Earth's magnetic field
- **Degrade HF propagation, especially at high latitudes** (polar paths get hammered)
- BUT: the aurora they create can **reflect VHF signals** — a silver lining for 6m and 2m operators

**Coronal Holes → High-Speed Solar Wind**
- Persistent openings in the Sun's corona that can last months
- Stream charged particles that **disturb HF communication**
- Rotate with the Sun (connecting to the 27-day cycle)
- Do NOT affect VHF/UHF ducting (that's a tropospheric phenomenon, completely unrelated)

### Geomagnetic Storms: What They Are and What They Do

A geomagnetic storm is a **temporary disturbance in Earth's magnetic field** — not a thunderstorm, not a solar flux drop, but a disruption of the entire geomagnetic field caused by solar particles interacting with Earth's magnetosphere.

Key effects:
- **Degrade high-latitude HF propagation** — charged particles funneled to the poles increase polar D-region absorption
- **Do NOT affect ground wave propagation** — ground wave follows Earth's surface and doesn't care about the ionosphere
- **Create auroras** that can reflect VHF signals — every HF operator's curse is a VHF operator's opportunity

### Propagation Indices: K and A

Two indices tell you about geomagnetic conditions:

| Index | Measures | Update Rate | Scale | Lower = Better |
|-------|----------|-------------|-------|----------------|
| **K-index** | Short-term geomagnetic stability | Every 3 hours | 0-9 | Yes |
| **A-index** | Long-term geomagnetic stability | Daily | 0-400 | Yes |

**K-index** is your "right now" indicator — K0-K1 means quiet (good HF), K5+ means storm (bad for HF, especially polar paths). Think K for "kurrent."

**A-index** is the daily overview, derived from the eight 3-hour K values. A0-A7 = quiet, A30+ = storm. Think A for "average."

Both measure conditions at Earth, not the Sun. They tell you how Earth's magnetic field is responding to solar activity.

---

## MUF, LUF, and Your Frequency Window

For any specific path at any specific time, there's a range of frequencies that work for skywave propagation. The boundaries are:

### MUF — Maximum Usable Frequency

The **highest frequency that will be refracted back to Earth** between two specific points. Above the MUF, signals pass through the ionosphere into space.

What affects the MUF? **Everything:**
- Path distance and location
- Time of day and season
- Solar radiation and ionospheric disturbances

The MUF is dynamic — it changes constantly. It's different for every path. A signal to Europe has a different MUF than one to Japan, and both change hour by hour.

### LUF — Lowest Usable Frequency

The **lowest frequency you can actually use** for communication between two specific points. Below the LUF, signals are absorbed by the D region before reaching the destination.

The LUF depends on D-region absorption, path length, and your station's power (a 1000W station has a lower effective LUF than a QRP station because it can overcome more absorption).

### The Window Between

Your usable frequency range for any path at any time is: **LUF (floor) to MUF (ceiling).**

- **Between LUF and MUF:** Signals are refracted back to Earth — propagation works
- **Below the LUF:** Signals are absorbed in the D region — too weak to use
- **Above the MUF:** Signals pass through the ionosphere — no propagation

**Best performance is just below the MUF** — at higher frequencies, you spend less time in the absorptive D region, so signals are strongest near the top of the window.

### When the Window Closes

If D-region absorption increases enough (raising the LUF) or F-region ionization drops enough (lowering the MUF), the LUF can exceed the MUF. When this happens, **no skywave propagation is possible on that path** — your frequency window has collapsed. There's no frequency that's simultaneously high enough to avoid absorption and low enough to be refracted. This is a propagation blackout.

---

## Critical Frequency and Critical Angle

These two terms sound similar but measure different things:

### Critical Frequency

The **highest frequency** that will be refracted back to Earth at a given angle of incidence. At vertical incidence (straight up), the critical frequency is the highest frequency that comes back down — essentially the MUF for zero distance. At more oblique angles, higher frequencies can be refracted because the signal spends more time in the ionized region.

This is why the MUF for a long-distance path is always higher than the critical frequency measured by an ionosonde shooting straight up — oblique angles can refract higher frequencies.

### Critical Angle

The **highest takeoff angle** that will return a radio wave to Earth under current conditions. Above the critical angle, signals pass through into space. Below it, they refract back down.

The critical angle creates the **skip zone** — the area between where ground wave coverage ends and where the first skywave signal returns to Earth. Nothing reaches this zone via normal propagation (though scatter can fill it in — more on that below).

Lower takeoff angles produce longer skip distances. Higher angles produce shorter skip distances — up to the critical angle, beyond which there's no return at all.

---

## Propagation Paths and Phenomena

### Short Path vs. Long Path

Every great-circle route between two stations has two directions: the short path (shorter distance) and the long path (the other way around the globe, roughly 25,000 miles longer). When both paths are simultaneously open, you hear a **slightly delayed echo** — the long-path signal arrives a fraction of a second later due to the extra travel distance.

Operators sometimes deliberately use long-path propagation when the short path is blocked (by polar cap absorption, for instance) or when the long path happens to cross ionosphere that's in better condition.

### Gray-Line Propagation

The gray line (or terminator) is the boundary between day and night on Earth's surface. Along this line, the D region is either just forming (sunrise side) or just disappearing (sunset side), creating a brief window where the absorptive D region is weak but the F2 region is still strong. This can produce remarkable propagation on the lower bands — paths that are impossible during full daylight suddenly open for a few minutes around sunrise or sunset.

### NVIS — Near Vertical Incidence Skywave

NVIS is a technique for covering distances of 0-300 miles using HF by shooting the signal nearly **straight up**. It refracts off the F layer and comes back down in a relatively small radius around the transmitter. NVIS fills the gap between ground wave (which fades out at 50-100 miles) and normal low-angle skywave (which starts at 500+ miles).

NVIS uses lower frequencies — typically 40m, 60m, and 80m — because these are low enough for the F layer to refract even at near-vertical angles. NVIS antennas are mounted low and horizontally to maximize the straight-up radiation pattern.

NVIS is invaluable for regional emergency communications — it covers a 300-mile radius regardless of terrain (mountains, valleys, buildings don't matter when your signal goes straight up and comes straight back down).

### HF Scatter

Scatter propagation fills in the skip zone — the area that normal skywave can't reach. Ionospheric irregularities scatter some signal energy in unintended directions, and a small portion lands in the skip zone.

The catch: scatter signals are **weak** (only a small fraction of energy is scattered), **distorted** (multiple paths create multipath interference), and have a characteristic **fluttering sound** (the scattering sources are constantly shifting). Phone signals via scatter have low intelligibility — CW works much better.

Scatter is the only type of propagation that allows signals to be heard in the skip zone. Faraday rotation is about polarization changes, chordal hop is a rare long-distance mode, and short-path skywave by definition overshoots the skip zone.

---

## Summer vs. Winter on the Lower Bands

Summer brings **high levels of atmospheric noise (static)** on the lower HF frequencies. The culprit: thunderstorms. Summer produces massive convective activity, and lightning generates broadband RF noise that can propagate for thousands of miles via skywave. On 80m and 40m, this static can be overwhelming — a signal that would copy perfectly in January is buried under crashes in July.

This is why 80m and 40m are traditionally "winter bands" — not because propagation is better in winter (it's actually similar), but because the noise floor drops dramatically when thunderstorm activity decreases.

---

## Putting It All Together

Here's the mental model that ties everything together:

1. **The Sun ionizes the upper atmosphere** → creating the D, E, F1, and F2 layers
2. **More solar activity = more ionization** → higher MUF → higher bands open
3. **The F2 layer is your friend** → it refracts signals for long-distance communication (up to 2,500 miles per hop)
4. **The D layer is your enemy** → it absorbs lower frequencies during the day
5. **At night, D disappears** → lower bands open up for DX
6. **Your usable window is LUF to MUF** → best performance just below the MUF
7. **Solar disturbances have different effects and timescales:**
   - Flares → instant D-region absorption spike (8 minutes)
   - CMEs → geomagnetic storms (15 hours to days)
   - Coronal holes → persistent solar wind disturbance (27-day rotation)
8. **20 meters always works** → the reliable band regardless of solar cycle
9. **Check the indices** → SFI for solar activity, K for right now, A for the day

Master these relationships and the exam questions answer themselves. More importantly, you'll understand what you're hearing (or not hearing) every time you tune across the HF bands.
