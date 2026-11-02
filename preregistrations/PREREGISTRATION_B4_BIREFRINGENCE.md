# B4: cosmic birefringence from the Twist field. Pre-registration (LOCKED)

**Locked:** 2026-11-02 10:20:30 (time from Get-Date), by Danny's "Lock as written". The text below is the draft unchanged.

**Honesty note:** the target is a published measurement and the predicted angles were computed before the lock, so this lock fixes the branch choice and the rule, not blindness. No verdict had been declared before the lock.

**Draft note (kept):** the numbers below are inputs computed from theory and the corrected (NR) fits.

## What is tested

Does the Twist field's change since recombination rotate CMB polarisation by the measured angle, with no new free parameter?

- **Target:** |β| = 0.24° ± 0.06° (ACT + Planck, as logged in T2_PHOTON_COUPLING_LOG.md). Other published values (Planck + WMAP about 0.34° ± 0.09°; ACT DR6 alone about 0.2° ± 0.08°) are noted as a sensitivity check, not the test.
- **Sign:** our anomaly-sign conventions are not fixed independently, so the test uses |β|. The sign is reported for information only.

## Theory inputs (fixed before any verdict)

1. **Fermion coupling, minimal coupling, reduced Planck units.** The coupling is (c ∂φ)·J₅, with:
   - **Nieh–Yan form** (Mercuri & Taveras, arXiv:0903.4407 eq. 22): c = √6/4.
   - **Holst form** (arXiv:0811.1998 eq. 16, the Twist's own arsinh field): c = √6/(4 cosh χ), where χ = φ/√(3/2).
   - The two forms agree when cosh χ = 1.
2. **Photon coupling via the chiral anomaly:** β = 2 c S (α/2π) Δφ.
   - S = Σ N_c Q² over the fermions counted.
   - S = 1 is Mercuri & Taveras' footnote 5. S = 8 counts all Standard Model charged fermions.
3. **Branch E (low-energy EFT).** A pure derivative coupling to a gauge-invariant axial current gives no physical photon coupling for photons far below the fermion masses: the heavy-fermion loop cancels the anomaly term (Quevillon & Smith, arXiv:1903.12559). CMB photons (≲ 1 eV) are far below every charged fermion mass, so β ≈ 0.
4. **Δφ = F·Δθ** at the NR best fits, computed by nlfix/delta_theta.py on AxiCLASS_nlfix:
   - Pantheon+ best fit (gF0.4m-0.3): F = 2.512, θ goes 1.9134 → 1.8802, so Δφ = −0.083 M_Pl.
   - DES Y5 official best fit (gF0m0.102): F = 1.000, θ goes 2.0100 → 1.8079, so Δφ = −0.202 M_Pl.
   - Assumption to confirm: AxiCLASS φ and f_axion are in reduced Planck units (CLASS scalar-field convention).

## Predicted |β| (degrees)

| Fit | E (EFT) | Nieh–Yan, S=1 | Nieh–Yan, S=8 | Holst, S=1 | Holst, S=8 |
|---|---|---|---|---|---|
| Pantheon+ best | ≈ 0 | 0.007 | 0.054 | 0.0003 | 0.002 |
| DES Y5 best | ≈ 0 | 0.017 | 0.132 | 0.007 | 0.053 |

To reach 0.24° in the most generous reading (Nieh–Yan, S = 8), the field would have to change by |Δφ| ≈ 0.37 M_Pl.

## Proposed rule (to lock)

- **Primary branch:** E (standard EFT). This is the physically standard reading.
- **Secondary branches:** Nieh–Yan and Holst with S = 8. These are reported side by side, as the NR and as-written verdicts were.
- **Verdict per branch,** using z = (0.24 − |β|)/0.06:
  - **CONSISTENT** if |z| ≤ 2;
  - **DISFAVOURED** if 2 < |z| ≤ 3;
  - **EXCLUDED** if |z| > 3.
- **Headline:** the primary branch at the DES Y5 official best fit, with Pantheon+ shown alongside.
- **No tuning.** No coupling factor, sign or S may be chosen after the lock. If the Twist is to explain the angle, it needs an explicit φ F F̃ term with a free coefficient. That is a new parameter, so it is a fit, not a prediction, and is logged as such.

## Known limits

- Non-minimal fermion coupling (the parameter α in 0811.1998) adds a vector-current term. A conserved vector current gives no photon effect at this order, but T3 is still open.
- The Jackiw–Kostelecký Chern–Simons ambiguity (a constant axial background inducing a regularisation-dependent photon term) is not resolved here. Branch E follows the decoupling answer.
- Only the background change counts. Reionisation and line-of-sight terms are second order for a field this slow.
