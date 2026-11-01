# Deep review and scales checkpoint, 1 November 2026, about 09:00

The second deep review of the day: what holds, what is weak, and what needs a decision.

## 1. Scorecard

| Test | Result (rules as written) | Reliability |
|---|---|---|
| Combined early (Locked Twist) | PASS, Δχ² −5.63 | Solid (two engines agree within 0.4) |
| Combined late (w0–wa) | PASS, Δχ² −10.89 / −10.95 | **Solid: matches DESI DR2's own −10.7** |
| A1 profile | Early energy preferred, f ≈ 0.08 | Solid (Poulin et al.: 0.09 ± 0.03) |
| A2 look-elsewhere | Weak hint, 1.2–1.4σ global | Solid method; coarse grid |
| A3 early + late | MILD, D = −3.65 | Pending R1 (best of 4) |
| **R2 so far: late gain with DES Y5** | **Δχ² −20.67** (Pantheon+: −10.95) | **Solid: matches DESI DR2's −21.0**; the pre-registered expectation ("the late gain should grow") holds |
| Late Twist L1 / L2 / L3 / shared F | FAIL / WORSE / CONSISTENT / DIFFERENT | **Unreliable fit**: the minimiser stalls twice; the true L1 is at most +0.38 |
| Coupled Twist | Built; gates V1–V4 pass; queued | Code validated; fits not yet run |

## 2. What holds

**Our pipeline reproduces the DESI collaboration's headline numbers** for both supernova sets:

| Late dark energy, Δχ² | DESI DR2 | Ours | Difference |
|---|---|---|---|
| With Pantheon+ | −10.7 | −10.95 | 0.25 |
| With DES Y5 | −21.0 | −20.67 | 0.33 |

This acts as a **known-answer mirror** on the whole data and likelihood stack. Together with the two-engine agreement and
the independent EDE profile (Poulin et al.), the measurement machinery is validated three ways.

## 3. The weakest point: minimising scalar-field late models

- **Evidence:**
  - The Late Twist stalled twice (+11.6, then +3.2), while points needing no fit sit at +0.38 to +0.68.
  - The restarts disagree with each other by up to 6.8 in χ².
- **Cause:**
  - The likelihood surface has walls where closure is impossible, which the guard turns into flat penalties, and a narrow
    viable band.
  - Bobyqa's trust region shrinks against the walls and stops early.
- **Who is affected:**
  - the Late Twist;
  - **robustness batch 2** (the Late Twist with DES Y5, next in the queue);
  - **all eight Coupled Twist fits**, which use the same machinery plus a third field parameter.

  As queued, these are likely to stall the same way and waste hours of CPU.
- **A recommended fix** (needs Danny's OK, since the Late Twist result has been seen):
  - Replace the free (F, m) minimisation with a **2D profile**: fix (F, m) on a small grid inside the viable band, for
    example log10 F ∈ {−0.4, −0.2, 0, 0.2, 0.4, 0.5} and log10 m ∈ {−0.3, 0, 0.2, 0.4}. Then minimise only the 11
    standard parameters, which are smooth with no walls.
  - The best grid point (refined) is the fit, judged by the unchanged L1–L3 rules.
  - The same grid with β fixed is the natural way to run the Coupled Twist.
- **Literature benchmark:** Ureña-López et al. (2025) find F ≈ 0.60 M_Pl and m ≈ 1.75 H₀ for the same potential on
  DESI. That is inside the grid, and inside our stalled fits' region.

## 4. Expectations, so nothing surprises us

- **A properly converged Late Twist with Pantheon+** will probably land near ΛCDM: L1 FAIL or INCONCLUSIVE, and L2
  WORSE. Thawing fields gain little except with DES Y5 (DESI's own extended analysis, Lodha et al.).
- **With DES Y5,** where the late signal is twice as strong, the Late Twist has its best chance.
- **The Coupled Twist** is the route that could reach the phantom-looking part of the signal, if the minimiser is fixed.

## 5. Process

- The house check now also catches hand-typed times (5 found and corrected today) and no longer flags its own
  generated ranking file.
- Every result file is now in git.
- The arXiv bundle is out of date. That is expected; it gets rebuilt before any submission.

## 6. Scales checkpoint record

| Pan | Passes / rounds | Hits |
|---|---|---|
| Local | 4 passes | 1 (new result file), 1 (generated file, rule fixed), 0, 0 |
| Online | 2 rounds | DESI DR2 numbers confirmed (a validation, not a correction); thawing-axion benchmark (F ≈ 0.6, m ≈ 1.75 H₀) |
| Mirrors | known-answer: DESI reproduced; corner probe: the stalled fit flagged | Council off (CubeMind stopped) |

**Level: yes.**

## 7. Decisions for Danny

1. **The minimiser fix** (the 2D profile grid): approve it for the Late Twist, its DES Y5 run, and the Coupled Twist, or
   leave them as queued.
2. *(Later)* Submitting to arXiv, once the remaining results are in.
