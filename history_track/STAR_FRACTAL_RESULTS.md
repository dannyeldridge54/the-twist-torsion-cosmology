# Star fractal study, 1D to 6D: results

**Pre-registrations:** PREREGISTRATION_STAR_FRACTAL.md (locked 09:41:38) and _ND.md (09:42:13), both locked before any
star was read.

**Sample:** 678,232 Gaia DR3 stars within 200 pc from all 12,288 AEGIS tiles (RUWE < 1.4, M_G ≤ 10, volume-complete).
Of these, 563,533 have radial velocities.

**Code and outputs:** `star_fractal.py`, STAR_FRACTAL_RESULTS.json, star_fractal.png.

**Noise reference:** a random (Poisson) 3D sample gives D = 3.0 ± 0.3 at 0.3 pc and 3.00 above 3 pc.

## Local dimension D(r)

r is in pc, or in km/s for velocities (1 km/s ≈ 1 pc per Myr).

| Space | D at 0.3 | D at 1 | D at 3 | D at 10 | D at 30 | D at 100 | Verdict (rules as written) |
|---|---|---|---|---|---|---|---|
| 1D (x) | 0.96 | 1.01 | 1.00 | 1.00 | 0.99 | 0.86 | **HOMOGENEOUS** (2.3 dex) |
| 2D (x, y) | 1.95 | 1.99 | 2.00 | 2.00 | 1.99 | 1.89 | **HOMOGENEOUS** (2.4 dex) |
| 3D (x, y, z) | **0.51** | **1.48** | 2.83 | 2.99 | 3.00 | 2.98 | **HOMOGENEOUS** from about 3 to 100 pc (1.4 dex); clumpy below 2.5 pc |
| 4D (+U) | 1.14 | 0.78 | 1.97 | 3.85 | 3.92 | 3.50 | **FRACTAL-LIKE** (1.3 dex) |
| 5D (+U, V) | 1.91 | 1.17 | 1.05 | 3.98 | 4.66 | 3.88 | **FRACTAL-LIKE** (2.5 dex) |
| 6D (+U, V, W) | 2.56 | 1.67 | 1.04 | 3.26 | 5.28 | 4.13 | **FRACTAL-LIKE** (2.5 dex) |

The radial-velocity sample's 1D–3D values match the full sample to within 0.07, so the 4D–6D results are not a sample
effect.

## What it shows

- **In 3D, stars are strongly clumped below about 2 pc.** Within 0.3 pc a star has **35 times** more neighbours than
  random (0.080 against 0.0023). These are binaries and multiple systems. Above about 3 pc the neighbourhood is
  **smooth (D = 3.00)**.
  - The clumpy range runs from 0.3 to about 2.5 pc, which is **0.92 dex**, just short of the one-decade rule. So the
    small scales are strictly **TRANSITION**, not FRACTAL-LIKE. The lower edge of the range (0.3 pc) limited this.
- **The 1D and 2D projections look homogeneous at every scale.** Flattening the data hides the clumps, as expected.
- **In phase space (4D–6D) the stars are fractal-like over 1.3–2.5 decades**, far below the dimension of the space,
  across about 1–10 units. Stars that are close in position and velocity cluster strongly: co-moving pairs, groups and
  streams. Structure that the 3D view hides appears once velocities are included.
- **At the largest scales,** D in 4D–6D falls back towards 3–4. Beyond the stars' velocity spread (tens of km/s), extra
  velocity room adds no new pairs.

## Expectation against result

| Written in advance | Result |
|---|---|
| Clumpy below a few pc, homogeneous above about 20 pc (3D) | **Yes in shape:** clumpy below 2.5 pc, smooth from 3 pc. The clumpy range is 0.92 dex, so strictly TRANSITION |
| 1D/2D approach 1 and 2 | **Yes:** homogeneous throughout |
| 4D–6D well below d, fractal-like in 6D over a decade or more | **Yes:** FRACTAL-LIKE in 4D, 5D and 6D (up to 2.5 dex) |

## "As above, so below"

The **shape** of the pattern repeats from the cosmos to our neighbourhood: clumpy at small scales, smooth at large
ones, with hidden structure in phase space. **The physics behind it differs at each level:**
- **For stars:** binaries, star formation in groups, and disc dynamics.
- **For galaxies:** gravity growing nearly scale-free primordial ripples, then smoothing above about 100 Mpc.

So the resemblance is a shared **mathematical** pattern (hierarchical clustering with a homogeneity scale), not one
cause acting at both levels. This is history and art track material, and is not evidence for the cosmology.

**Caveats:**
- Counting 1 km/s as 1 pc is a convention. It sets *where* the 4D–6D transition appears, but not whether there is
  clustering.
- Radial-velocity errors (about 1–5 km/s for fainter stars) blur the smallest velocity scales.
