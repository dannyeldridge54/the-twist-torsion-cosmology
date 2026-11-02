# Results ledger, 2 November 2026 (running data sheet; the paper is NOT updated until Danny says so)

Every test run today, with its locked rule, its verdict and its files. *Pending* rows are filled in by the scorers
(`robustness2_score.py`, `lu_tf_score.py`) as fits land. Times come from Get-Date.

## Pre-registered tests

| Test | Rule (locked) | Result | Verdict | Write-up |
|---|---|---|---|---|
| NR: replication of every n = 1 test on corrected code | NLFIX_REPLICATION (1 Nov 18:37:37) | complete 12:17:51 | see the side-by-side table | LATE_TWIST_RESULTS.md, COUPLED_TWIST_RESULTS.md |
| C5: torsion-natural β = 0.816 (NR) | COUPLED_TWIST | +71,655 (both signs) | EXCLUDED | COUPLED_TWIST_RESULTS.md |
| B4: minimal-field birefringence | B4_BIREFRINGENCE (10:20:30) | \|β\| ≈ 0 vs 0.24° | EXCLUDED (4.0σ) | B4_BIREFRINGENCE_RESULTS.md |
| B4-X: switch ratio R; atomic echo; ratio patterns | B4X_PHOTON_COUPLING (11:54:34) | R = 0.997; b₀ ≈ 10⁻⁴³ GeV | R OPEN; echo PASS; silver NOT SUPPORTED; golden SUGGESTIVE | B4X_SWITCH_RESULTS.md |
| Ratio replication on new data | RATIO_REPLICATION (12:01:34) | golden p = 0.56; silver p = 0.73 | NOT REPLICATED / NOT SUPPORTED; switch value definition-dependent | RATIO_REPLICATION_RESULTS.md |
| S8 on corrected code | S8_FIXED_CODE (12:10:03) | Late 0.820 / 0.819; Coupled 0.828 | Late NEUTRAL; Coupled WORSENS | S8_FIXED_CODE_RESULTS.md |
| B2: DESI dissection | ROBUSTNESS_II (12:35:12) | Late DES Y5 −5.33 without DESI (86%); Coupled +0.74 | Late NOT DESI-DRIVEN; Coupled DESI-DRIVEN | ROBUSTNESS_II_RESULTS.md |
| R3: cold restart, Late DES Y5 | ROBUSTNESS_II | Δ = +0.13 | STABLE | same |
| R3: cold restart, Coupled | ROBUSTNESS_II | Δ = +2.37 (cold best 2396.72 vs 2394.35) | COLD-START WORSE (warm minimum stands) | same |
| LU: Late Twist on Union3 | LATE_UNION3 (14:23:26) | Δ_U = −1.82 (Union3 SNe −4.10); w0–wa −15.00 | WEAKENED (as expected) | LATE_UNION3_RESULTS.md |
| SSG: solar-system gate for the BI dilaton | SOLAR_LOWZ (15:17:31) | GR point at ϕ = −½, an attractor; Cassini band \|Δχ\| < 0.0072 M_Pl | ATTRACTOR-PROTECTED (Reading A); a pinned dilaton turns the spiral back into the minimal Twist today | SOLAR_GATE_RESULTS.md |
| LZ: low-z split of the DES Y5 gain | SOLAR_LOWZ (15:17:31) | SN Δ −8.89 all; +0.53 z > 0.1 alone; −0.29 z ≤ 0.1 alone; r = −0.06 (w0–wa context r = −0.17) | CALIBRATION-SENSITIVE | LOWZ_SPLIT_RESULTS.md |
| GH: H(z) chronometers + fσ8 (no refit) | GROWTH_HZ (15:31:34) | all \|Δ\| < 0.5 (LT-D +0.03 / +0.42; CT +0.10 / −0.31) | NEUTRAL (LT-D, CT); LT-P NO VERDICT (mirror 0.087) | GROWTH_HZ_RESULTS.md |
| IN: inflation from α = 1 | UFE_CHECKS (15:50:03) | n_s = 0.9667 at N = 60 vs 0.974 ± 0.003 (2.4σ); r = 0.003 | TENSION (as expected) | UFE_CHECKS_RESULTS.md |
| ER: dilaton as the early field | UFE_CHECKS (15:50:03) | max Ω_χ(3500) = 0.025; G ×13 at BBN | TOO SMALL | UFE_CHECKS_RESULTS.md |
| LQ: BI value today vs LQG | UFE_CHECKS (15:50:03) | γ = 0.259 (Pantheon+ fit), 0.68 (DES Y5 fit); Pantheon+ rebuild off by 0.087 | NO VERDICT (mirror failed) | UFE_CHECKS_RESULTS.md |
| PC: pincer (CMB-only fits predict BAO + SNe) | PINCER (16:22:30) | *queued* (starts when the torsion-F runners finish) | | (to write) |
| Forward predictions (DESI DR3, w0–wa, phantom, S8, R, inflation r, GW parity) | PREDICTIONS_LOCKED (16:19:51) | frozen numbers in forward_predictions.json | scored when the data are public | PREDICTIONS_LOCKED_2026-11-02.md |
| TF: F fixed at √(3/2) and √6 M_Pl | TORSION_F (14:51:28) | *pending* | | (to write) |
| TF-P: F fixed at (4/π)√(3/2) M_Pl (derived) | TORSION_F_PLANCK (14:55:36) | *pending* | | (to write) |

## Analyses (not pre-registered tests; no verdicts)

| Analysis | Main numbers | File |
|---|---|---|
| Per-dataset breakdown | Late DES Y5 gain comes from DES Y5 supernovae (−8.89); w0–wa gains on every probe | DATASET_BREAKDOWN.md |
| Data catalog | 7 datasets used, about 8 public ones not yet used | DATA_CATALOG.md |
| Theory: T1, radiative stability, T3 | one real field ruled out (10⁶–10⁸ × DE); δZ ≈ 5×10⁻³³; non-minimal piece a total derivative | THEORY_T1_T3_STABILITY.md |
| Deep dive (19 rounds, ended at 0 hits) | torsional-instanton cosine (S ≈ 276); Nieh–Yan phantom route; Nieh–Yan F enhancement; SM-induced γ = 1/9 | THEORY_T1_T3_STABILITY.md |
| Next-model feasibility | spiral Ω_ρ ≥ 0.18–1.4%; DESI crossing at z ≈ 0.37–0.45 | NEXT_MODELS_DESIGN.md |
| Nieh–Yan period | F = (4/π)√(3/2) M_Pl at the Planck length; late fits need ℓ = 0.79–1.25 Planck lengths | NIEH_YAN_PERIOD.md |
| Nieh–Yan Twist (draft, unlocked) | kinetic K(φ) = tanh((φ − φ_c)/F); ghost question open | NIEH_YAN_TWIST_DRAFT.md |
| Path review (4 rounds, 0 new hits at the end) | Late hint likely DES Y5 low-z calibration (3 outside groups); ghost route dropped; Spiral Twist ≈ kinetically mixed axion–dilaton if the field space is hyperbolic | PATH_DECISION_2026-11-02.md |
| τ audit (post-hoc, prompted by LU) | τ moves by up to ±0.008 between fits, and low-ℓ EE moves ±2–3 with it, along a near-flat direction (Late r4: EE +3.15 but total within 0.13). Totals are robust; per-dataset rows involving τ are not meaningful alone. This applies to DATASET_BREAKDOWN too | tau_audit.py / tau_audit.json |
| BI supergravity λ | λ = −2√(2/3) = −1.633 (α = 1), inside Toomey et al.'s −1.3 (+1.3/−1.5); post-hoc | bi_kahler_lambda.py, PATH_DECISION_2026-11-02.md |
| Spiral potential loop (6 rounds) | Matter blindness from scale (Weyl) invariance; constant-W supergravity potential turns at ϕ = −½ but is AdS; plain dilaton gives 1 + w0 < 0.02 | SPIRAL_POTENTIAL_LOOP.md, bi_superpotential.py |
| Spiral w(z), first pass | Validation PASS; literature mirror FAIL (missing benchmark inputs); with F = 1.56: w0 ≈ −0.84, wa ≈ −0.24 (thawing); eq. 11 illusion stronger with our λ (−1.50 today) but wrong time direction. PROVISIONAL | SPIRAL_W_FEASIBILITY.md, spiral_w.py |
| Spiral solver mirror and assembly | Mirror PASS vs Ramos-Hamud et al. attractors (1e-10). Fixed α = 1 means ξ = 0.82, but their DESI benefit needs ξ > 370 (450× stronger), so the spiral is plain thawing unless the matter-like-angle route works (untested) | SPIRAL_W_FEASIBILITY.md, spiral_mirror_ramos.json |
| Spiral matter-like angle | Bends wa toward DESI in proportion to the angle share f; at the allowed f ≲ 6–9% the bend is Δwa ≈ −0.05 to −0.09; one setting touches the DESI-like edge (w0 −0.80, wa −0.40, f 9.7%). Borderline; needs a real fit | SPIRAL_W_FEASIBILITY.md, MIRROR_MAP_SPIRAL.md |
| Numbers ledger | 30 paper numbers recomputed from the fit files, all matching | paper_numbers_check.py |

## Published today

- **Theory note** (Zenodo, at Danny's word): *The Barbero–Immirzi Field as a Hyperbolic Axion–Dilaton: a Fixed
  Kinetic Mixing λ = −2√(2/3) and the Spiral Twist Hypothesis*, doi:10.5281/zenodo.23898709 (concept
  10.5281/zenodo.23898708), created 2026-11-02 22:16:45 UTC. The source is `zenodo/spiral_note/spiral_twist_note.tex`;
  the PDF md5 b7664b3c9cf740a4646309b1f15e2be7 matches the server.

- **Theory note, version 2** (Zenodo, at Danny's word "u r a go"): *… a Fixed Kinetic Mixing, a Validated Spiral
  Twist Solver, and Predictions Locked Before the Data*, doi:10.5281/zenodo.23899237 (same concept record as v1),
  created 2026-11-02 22:50:20 UTC. Files (md5 verified against local): `spiral_twist_note_v2.pdf` (c01228c4…),
  `spiral_twist_v2_supplement.zip` (7f67f337…, 28 scripts and result files), `PREDICTIONS_LOCKED_2026-11-02.md`
  (614170500…) plus its `.sha256`. Source: `zenodo/spiral_note/spiral_twist_note_v2.tex`.

## Waiting for Danny

- Paper edits (on hold).
- Push of both repositories and Zenodo v3.1.
- The arXiv endorsement code.
- Deleting 5 duplicate Gmail drafts.
