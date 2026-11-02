# Scoreboard of every pre-registered test (draft for the paper)

**Draft, 1 November 2026.** This goes into the paper with the final update, after G1–G3. Rows marked *pending* are
filled in then. Numbers come from THESIS.md and the result files it cites. Post-hoc checks are labelled and are **not**
counted as pre-registered.

## Pre-registered (rule hashed before the result)

| # | Test | Result | Verdict |
|---|---|---|---|
| 1 | Locked Twist, Planck + DESI + Pantheon+ | Δχ² −4.70 | PASS |
| 2 | Locked Twist, Planck + ACT DR6 (blind) | Δχ² −7.23 | PASS |
| 3 | Locked Twist, SPT-3G D1 alone | best Δχ² −1.27 | FAIL (no preference) |
| 4 | Three CMB + DESI + Pantheon+ | Δχ² −5.63 | PASS |
| 5 | A1: profile in f | f = 0 costs 5.98 | PASS (preferred) |
| 6 | A2: look-elsewhere | global 1.2–1.4σ | WEAK HINT |
| 7 | A3: early on top of late | D −3.65 (AIC +0.35) | MILD |
| 8 | R1: A3 minimiser stability (best of 4) | D −3.96 | STABLE (MILD) |
| 9 | DES-Dovekie bracket for A3 | D −2.70 | MILD |
| 10 | P1: width = torsion ÷ 9 | — | FAIL |
| 11 | P2: starting angle 1 + √2 | — | FAIL |
| 12 | P3: Hebrew-letter Tree f = 0.0154 | — | INCONCLUSIVE |
| 13 | P4 / P4b: width N = 9 / 7 | SPT-3G prefers 24 | FAIL (inconsistent) |
| 14 | Potential power n = 2 vs 3 | n = 2 worse by 10.35 | n = 3 favoured |
| 15 | Lock from the dynamics (phase space) | no saddle; ×3.5 spread | NO LOCK |
| 16 | Late Twist L1 (vs ΛCDM), Pantheon+ | grid best +0.96 as written (≈ −0.4 on the fixed code) | FAIL (a tie once corrected) |
| 17 | Late Twist L2 (vs w0–wa) | D = +10.92 (Pantheon+), +14.44 (DES Y5) | WORSE |
| 18 | Late Twist L3, P9: shared F | late/early ≈ 7 | DIFFERENT so far; *grid pending* |
| 19 | Edge scan (DES Y5 blind) | best edge −5.05; none beats the grid's −5.32 | done (no change) |
| 19b | High-mass corner (HC) | best +38.99 vs ΛCDM (Δ_HC +38.03) | WORSE (as explored) |
| 19c | LD: Late Twist on DES-Dovekie | Δ_D +0.18 | NOT CONFIRMED |
| 20 | Coupled Twist C1–C4 (as written) | C1 −6.80; C2 D_c −7.76; C3 ΔAIC +5.16; C4 crossing (β < 0 mode) | C1 PASS, C2 NEEDED, C3 WORSE, C4 CROSSES; NR pending |
| 21 | Coupled Twist C5: β = 0.816 | unphysical (H₀ ±299), +10⁵ | EXCLUDED |
| 22 | Star fractal, 1D–6D | homogeneous 3–100 pc; fractal-like in phase space | as stated (art track) |
| 23 | Symbol-derived numbers | at chance | FAIL |

## Post-hoc checks (not counted above)

| Check | Result | Reading |
|---|---|---|
| R2: A3 with DES Y5 | D −4.70 | SURVIVES (so A3 is FRAGILE across SN sets) |
| Pipeline vs DESI DR2 | late gain −10.95 / −20.67 vs −10.7 / −21.0 | matches |
| Two codes (CAMB vs AxiCLASS) | within 0.4 | pass |
| Late Twist null mirror | +1.35 frozen offset; +0.03 without halofit | code artefact (halofit Ω_m bookkeeping) |
| Pantheon+ edge points | — | *pending*, post-hoc |
| R2: Late Twist L1 with DES Y5 | −5.32 (official, grid + edge); LEE-G Z_glob 1.03σ | PASS on DES Y5 only; NOT CONFIRMED on Dovekie (LD) |

## Tally (to be finalised)

So far, 20 of 23 pre-registered rows have a verdict, and 3 are pending (19–21):

| Verdict | Count | Rows |
|---|---|---|
| Pass | 4 | 1, 2, 4, 5 |
| Mild or weak | 4 | 6, 7, 8, 9 |
| Fail, worse, different or no lock | 9 | 3, 10, 11, 13, 15, 16, 17, 18, 23 |
| Inconclusive | 1 | 12 |
| Favoured | 1 | 14 (n = 3) |
| Descriptive | 1 | 22 (art track) |

Rows 16–18 may change when the grid finishes. Readers should judge the 1.2–1.4σ early hint against this full count.
