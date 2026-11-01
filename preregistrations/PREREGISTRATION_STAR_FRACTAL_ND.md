# Pre-registration addendum: the star fractal study in 1D to 6D (phase space)

**Written:** 2026-11-01 09:42:13 CT. The time is from the clock; this file is hashed and committed by the same command. No stars had
been read. This adds to PREREGISTRATION_STAR_FRACTAL.md at Danny's request ("analyze it like 1d 2d 3d 4d 5d"). Its
3D rule is unchanged.

## Nested spaces

Galactic Cartesian coordinates: positions x, y, z in pc; velocities U, V, W in km/s, from RA, Dec, distance, proper
motions and radial velocity (astropy). **1 km/s is counted as 1 pc,** because 1 km/s ≈ 1.02 pc per Myr: a star's motion
over a million years.

| Dimension | Coordinates | Sample |
|---|---|---|
| 1D | x | full sample |
| 2D | x, y | full sample |
| 3D | x, y, z | full sample (the main study) |
| 4D | x, y, z, U | stars with a Gaia radial velocity |
| 5D | x, y, z, U, V | the same stars |
| 6D | x, y, z, U, V, W | the same stars (full phase space) |

The 1D–3D measurements are repeated on the radial-velocity subsample, so that sample effects can be separated from
dimension effects.

## Measure and rules (per dimension d)

- **Measure:** C(r) and D(r) = d ln C / d ln r, as in the main file, with centres kept away from the sample's position
  edge. The velocity space is not edge-limited and is used as it stands. The scale r runs 0.3–100 in each space's
  units.
- **FRACTAL-LIKE:** D < d − 0.3 continuously over at least one decade of r.
- **HOMOGENEOUS:** |D − d| ≤ 0.1 over at least half a decade of r.
- **TRANSITION:** otherwise.
- **Reference:** a Poisson sample of the same size in each space gives D = d.

## Expectation, written in advance

| Space | Expected behaviour |
|---|---|
| **1D–3D** | Homogeneous above about 20 pc and fractal-like below a few pc. In 1D and 2D, D should approach 1 and 2 at large r (projection hides the clumps less well in fewer dimensions) |
| **4D–6D** | Stars are much clumpier in velocity than in position: moving groups and streams (the Hyades stream and others), with a velocity spread of only about 20–40 km/s. So D should stay **well below d** across most of 1–30 units, and be **fractal-like in 6D** over at least a decade |
| **Overall** | The extra dimensions should show structure that the 3D view hides, because "real" clustering lives in phase space |
