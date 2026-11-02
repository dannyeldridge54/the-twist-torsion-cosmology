# Coupled Twist: results (as written, installed coupled build)

**Rules:**
- PREREGISTRATION_COUPLED_TWIST.md (gates V1–V4 passed, COUPLED_TWIST_GATES.md);
- (F, m) grid deviation 08:58;
- C5 code-limited rule, deviation 08:39.

**Data:** Planck low-ℓ + ACT DR6 (CMB + lensing) + SPT-3G D1 + DESI DR2 + Pantheon+.

**Code caveat:** these runs use the coupled AxiCLASS build, which carries the two B0 bugs (LATE_TWIST_NULL_MIRROR.md).
- **C1 and C3** (Λ- and w0–wa-referenced) carry the +1.35 offset; offset-corrected values are given beside them.
- **C2** compares coupled with uncoupled on the same code, so the offset cancels.
- **σ8 and S8 from these runs are invalid** (the δ_m bug).
- The corrected-code replication (NR, PREREGISTRATION_NLFIX_REPLICATION.md) is running overnight. **Its verdicts will be
  the headline** and will be added below.

## Grid (3×3 around the best Late Twist Pantheon+ point; β free in ±0.15)

| (F/M_Pl, m/H₀) | Δχ² vs ΛCDM | β at the minimum |
|---|---|---|
| **(2.0, 0.79)** | **−6.80** | −0.044 |
| (5.0, 0.79) | −6.64 | −0.041 |
| (5.0, 0.50) | −6.47 | +0.043 |
| (3.16, 0.79) | −6.15 | +0.047 |
| (3.16, 0.50) | −3.08 | +0.037 |
| (5.0, 0.32) | −2.62 | +0.040 |
| (2.0, 0.50), (2.0, 0.32), (3.16, 0.32) | non-viable | — |

## β profile at the best grid point (F 2.0, m 0.79), β fixed

| β | −0.816 | −0.1 | −0.05 | 0 | +0.05 | +0.1 | +0.816 |
|---|---|---|---|---|---|---|---|
| Δχ² vs ΛCDM | +101,984 (H₀ = 299, unphysical) | +124.3 | **−6.07** | +1.05 | **−6.93** | +186.6 | +103,621 (H₀ = −298, unphysical) |

## Verdicts (as written)

| Test | Result | Verdict |
|---|---|---|
| **C1** vs ΛCDM | −6.80 (grid best; ≈ −8.15 offset-corrected). The profile's +0.05 point reaches −6.93 | **PASS** |
| **C2** coupling needed vs the uncoupled Late Twist | D_c = −7.76; the profile gives β = 0 at +1.05 vs about −6.9 at abs(β) = 0.05 | **NEEDED** |
| **C3** vs w0–wa | ΔAIC = +5.16 | **WORSE** |
| **C4** apparent phantom crossing (0.3 < z < 2) | β = −0.044: w_eff −0.956 (z = 0) → −1.012 (z = 1) → −1.039 (z = 2), **crosses**. β = +0.05: minimum −0.951, **does not cross** | **CROSSES** (negative mode only) |
| **C5** torsion-natural abs(β) = 0.816 | both signs give a finite but unphysical point (H₀ = ±299), +10⁵ in χ² | **EXCLUDED** |

## What it means

1. **A small coupling helps.** Allowing abs(β) ≈ 0.05 improves on the uncoupled Twist by about 8 in χ² and on ΛCDM by
   about 7. It is still worse than w0–wa once the two extra parameters are counted.
2. **The coupling is tightly bounded.** abs(β) = 0.1 already costs more than 100. The data allow abs(β) of only about
   0.05–0.07, which agrees with Babu & Amendola (arXiv:2610.23497), who find abs(β) < 0.073 at 95%.
3. **Two modes, about equally good:** β ≈ −0.05 (−6.07 here; −6.80 at the grid's free-β minimum) and β ≈ +0.05 (−6.93).
   **Only the negative mode produces the apparent phantom crossing**, as Babu & Amendola also report. Our data do not
   clearly prefer either sign; Babu & Amendola find the negative mode higher. *(An earlier note here said "negative
   preferred"; the profile corrects that.)*
4. **The torsion-natural coupling (0.816) is excluded beyond doubt.** It does not even produce a physical cosmology in
   this code. If the Coupled Twist is right, the coupling is about 16 times weaker than the simplest torsion estimate.
5. **Independent agreement with published work** on the bound, the bimodality and which mode crosses is good evidence
   that this pipeline is sound.

**Comparison with arXiv:2609.03062:**
- They use an energy-transfer coupling Q = βHρ_de and find β ≈ 0.53 for interacting thawing.
- That is a different coupling form, so the numbers are not directly comparable.
- The shared message is that a coupling can improve thawing fits by several units of χ² without being required.

## NR: corrected code (pending)

The corrected-code replication runs overnight (stage 3: Coupled grid; stage 4: C5 + β profile). Its verdicts go here
and become the headline. S8 will be quoted only from NR.

## Final side-by-side: original code vs corrected code (NR complete 2026-11-02 12:17:51)

Produced by `nr_verdicts.py`, which applies every rule exactly as written. The corrected-code column is the headline for n = 1 models.

| Test | As written | Corrected code (NR) |
|---|---|---|
| Pantheon+ L1 | +0.96 → FAIL | +0.09 → FAIL |
| Pantheon+ L2 | D +10.92 → WORSE | D +10.05 → WORSE |
| Pantheon+ L3 | INCONSISTENT | CONSISTENT |
| Pantheon+ LEE-G | NOT SIGNIFICANT | NOT SIGNIFICANT |
| Pantheon+ best point | gF0.5m-0.3 (24/24 accounted) | gF0.4m-0.3_nlfix (24/24 accounted) |
| DES Y5 L1 | -5.32 → PASS | -6.23 → PASS |
| DES Y5 L2 | D +14.43 → WORSE | D +13.53 → WORSE |
| DES Y5 L3 | INCONSISTENT | CONSISTENT |
| DES Y5 LEE-G | Z_loc 1.81σ → Z_glob 1.03σ (N_eff 5) → WEAK HINT | Z_loc 2.01σ → Z_glob 1.27σ (N_eff 5) → WEAK HINT |
| DES Y5 best point | gF0.5m0_desy5 (32/32 accounted) | gF0m0.102_desy5_nlfix (32/32 accounted) |
| LD (Dovekie) | +0.18 → NOT CONFIRMED | -1.33 → WEAKENED |
| HC | Δ_HC +38.03 → WORSE | Δ_HC +36.99 → WORSE |
| Coupled C1 vs ΛCDM | -6.80 → PASS | -7.91 → PASS |
| Coupled C2 coupling needed | -7.76 → NEEDED | -8.00 → NEEDED |
| Coupled C3 vs w0–wa (ΔAIC) | +5.16 → WORSE | +4.05 → WORSE |
| Coupled C5 β = 0.816 | EXCLUDED | EXCLUDED |

**β profile (corrected code, Δχ² vs ΛCDM):**

| β | −0.816 | −0.1 | −0.05 | 0 | +0.05 | +0.1 | +0.816 |
|---|---|---|---|---|---|---|---|
| Δχ² | +71,655 | +127.7 | −7.37 | −0.63 | −7.34 | +94.4 | +71,655 |

**S8 on the corrected code:** S8_FIXED_CODE_RESULTS.md (Late Twist NEUTRAL; Coupled Twist WORSENS by 0.84σ against DES Y6).
