# The route (revised 1 November 2026, about 10:00, after the scales review)

The previous version (31 October, night) is in git history.

**Principles, unchanged:**
- every rule is hashed before its run;
- every result is logged, pass or fail;
- deviations go in the append-only log;
- times come from the clock;
- the scales checkpoint runs at every intersection.

## Where we stand

| Question | Answer so far |
|---|---|
| Does the pipeline measure correctly? | **Yes:** it reproduces DESI DR2 (−10.7 and −21.0, ours −10.95 and −20.67); two engines agree; Poulin et al.'s profile matches |
| Is there early energy? | **A weak hint:** f ≈ 0.08; local 2.4σ, **global 1.2–1.4σ** |
| Does it survive alongside late dark energy (A3)? | **MILD** with Pantheon+ (D −3.65), **SURVIVES** with DES Y5 (D −4.70), so **fragile** across supernova sets. The original DES Y5 has a known calibration offset (Efstathiou; replaced by DES-Dovekie) |
| Can the twist field be today's dark energy? | Open. The free fits stalled; the (F, m) grid is running. Viable only where m²F² ≳ 1.2 (energy budget). Expect near-ΛCDM with Pantheon+ and a gain with DES Y5 |
| Does geometry fix the potential or the lock? | **No.** The potential is assumed; the lock is not derivable (pre-registered phase-space test: no saddle at equality; S ≈ 3.5, 2.9 with coupling) |
| Torsion-specific evidence? | **None yet.** The shared-F, N = 9, silver, torus and letters tests were all different, failed or inconclusive |

## Phase A: finish what is running (automatic, hourly loop)

| # | Step | Status |
|---|---|---|
| A-R1 | A3 with best of 4 (`edelock_w0wa_b4`) | Running |
| A-G1 | Late Twist (F, m) grid, Pantheon+ and DES Y5 | Running (non-viable points recorded) |
| A-G2/G3 | Coupled Twist grid, then C5 and the β profile | Queued after G1 |

### Timetable

Estimated at 10:07 on 1 November, from observed run times. A helper worker joins the grid once cores free up, at
about 12:00.

| Result | Expected |
|---|---|
| A3 best of 4 (R1) | about 11:30 |
| **Dovekie verdict** (does early energy survive with corrected SNe?) | about 11:45–12:00 |
| **Late Twist, Pantheon+ grid** | about 14:00–14:30 |
| **Late Twist, DES Y5 grid** (its best chance) | about 16:00 |
| Coupled Twist grid | about 18:00 |
| **C5 and β profile** (the full picture) | about 19:30 |

## Phase B: new robustness and data steps (pre-register each before it runs)

| # | Step | Why |
|---|---|---|
| B1 | **A3 and the Late Twist with DES-Dovekie** (installed) | Brackets the DES Y5 result: DES-Y5 had a calibration offset; Dovekie is the corrected sample. Decides whether "SURVIVES" is real or a supernova systematic |
| B2 | **A4 BAO dissection:** CMB + SNe without DESI | How much of every result comes from DESI DR2 (reviewer's request) |
| B3 | **SPT-3G D1 lensing** (installed, unused) | Lensing directly tests early energy's cost in structure growth (S8) |
| B0 | **Halofit fix for scalar-field runs** (decided 1 Nov: *after* G1–G3 finish). Steps: log the deviation first; patch halofit's Ω_m to exclude the field; re-run the null mirror (target ≈ 0 with halofit on); re-evaluate the Pantheon+ and DES Y5 best grid points and the Coupled Twist best on the fixed code; report them beside the as-written verdicts | LATE_TWIST_NULL_MIRROR.md found the cause; fixing mid-run would mix code versions |
| B0b | **Shooting check** (no fits): are the "non-viable" small-F points physical, or does the starting-angle search fail near the hilltop? | Decides how to read the high-mass corner (HC) result |
| T1 | **One field or two?** Look for a single potential with two terms (for example two instanton sectors) that serves both the early (n = 3) and late (n = 1) roles. If one exists, pre-register a joint fit; if not, the paper says "two fields from the same geometry" | Shared F currently says DIFFERENT (late/early ≈ 7); a referee's first question |
| T2 | **Photon coupling c_γ** (the φ F F̃ coefficient) from the torsion construction, via an anomaly argument (electromagnetically charged fermions that feel torsion). Lock it before B4 compares anything | Holst and Nieh–Yan couple to gravity, not light; without c_γ, B4 has no prediction |
| T3 | **Spin coupling:** torsion couples φ to the fermion axial current (∂φ·J₅). Check lab bounds (spin precession, comagnetometers, ultralight axion-wind searches) against our (F, m) | A constraint not yet applied to this field; it could exclude part of the parameter space |
| B4 | **Birefringence prediction:** derive the twist field's polarisation rotation from the construction, lock it, then compare with 0.20–0.34° | The one route to a torsion-specific test (the gap between levels 6 and 2) |

## Phase C: write-up

| # | Step | When |
|---|---|---|
| C1 | **Paper v3 final:** grid Late Twist, robustness (incl. A3 fragile across SN sets), Coupled Twist, lock test, limitations. Framing: *"a pre-registered test of a torsion-motivated field in early and late roles: mostly null, a weak and SN-dependent early hint, a validated open pipeline"* | After A and B1 |
| C2 | Rebuild the arXiv bundle; the full house check must be level | With C1 |
| C3 | **Your decision:** submit to arXiv; Zenodo v3 | After C2 |
| C4 | Outside eyes: one or two EDE researchers for feedback and an endorsement | With C3 |

## Phase D: when the PC is free

- MCMC posteriors for a journal version (ΛCDM is already converged: H₀ 68.29 ± 0.27).
- The full ACT and multi-frequency SPT likelihoods.
- CubeMind restart with the Scales preset and the council bounce, **only on your word**.

## History and art track (kept separate)

- **One log for every source:** OLD_SOURCES_LOG.md (9 entries, from Genesis to the Tetractys).
- **Done today:**
  - the Welling K7 torus;
  - Zahn's optics compared with modern optics;
  - the Aizawa attractor reproduced;
  - the 1D–6D star study: clumpy small, smooth large, fractal-like in phase space.
- New ideas go here first, and become physics only through a pre-registered test.

## What would change the route

- **Dovekie keeps SURVIVES, and the Late Twist or Coupled Twist shows a gain:** the field has real roles in both eras.
  Push C1–C4, and prioritise B4 (a torsion-specific test).
- **Dovekie returns MILD or NOT NEEDED:** the early hint depends on a supernova systematic. The paper says so; the
  focus moves to the late role and B4.
- **The Late Twist and Coupled Twist both fail:** the field does not explain DESI's signal. The paper reports a clean
  null for both roles.
