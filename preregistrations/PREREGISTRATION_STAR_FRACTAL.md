# Pre-registration: fractal (correlation) dimension of nearby stars (history and art track)

**Written:** 2026-11-01 09:41:38 CT. The time is from the clock, inserted by the command that hashes and commits this file. No stars
had been read for this study.

**Locking:** SHA-256 hashed and committed when written; never edited afterwards. This is an exploration of local data,
not a test of the cosmology.

## Sample

- **Source:** all 12,288 AEGIS Gaia DR3 tiles (`ufe-v2/cosmos_map/tiles/L5`).
- **Cuts:** stars with dist_pc < 200, RUWE < 1.4 (good single-star astrometry), and absolute magnitude
  M_G = G + 5 − 5 log10(d) ≤ 10. At 200 pc that is G ≤ 16.5, well inside Gaia's completeness, so the sample is
  volume-complete.
- **Positions:** the x, y, z columns (pc).

## Measure

- **Correlation integral:** C(r) = the mean number of other stars within distance r of a star, counted only for centre
  stars closer than 200 − r pc to the Sun, so every sphere lies inside the sample.
- **Local dimension:** D(r) = d ln C / d ln r on log-spaced r from 0.3 to 100 pc.
- **Reference:** a uniform random (Poisson) sample of the same size and volume gives D = 3. It also gives the noise level.

## Rules

| Reading | Rule |
|---|---|
| **FRACTAL-LIKE** over a range | D < 2.7 continuously over at least one decade of r |
| **HOMOGENEOUS** over a range | 2.9 ≤ D ≤ 3.1 over at least half a decade of r |
| **TRANSITION** | anything in between; reported as such |

## Expectation, written in advance

| Scale | Expected D | Why |
|---|---|---|
| Below about 2 pc | well below 3, possibly 1–2 | wide binaries and small groups |
| About 2–20 pc | rising towards 3, but held below it | clusters and associations (for example the Hyades, about 47 pc away) |
| About 20–100 pc | close to 3 (homogeneous) | perhaps slightly below at the top end, because the Galactic disc thins (scale height about 300 pc) |

**So:** fractal-like at small scales, homogeneous above about 20 pc. That mirrors the cosmic picture (fractal small,
smooth large) on a much smaller stage. A result fractal at all scales would contradict this expectation.
