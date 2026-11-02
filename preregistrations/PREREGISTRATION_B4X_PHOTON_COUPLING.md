# B4-X: the switched Twist with one photon parameter. Pre-registration

**Locked:** 2026-11-02 11:54:34 (time from Get-Date). Danny asked for this equation to be set ("Set it… make the best probable solving equation… just do your best"), and that request is taken as the go to lock. B4 and its verdicts stay exactly as locked. Nothing below (R, z_on, b₀, X9) had been computed at lock time; only the X1 fit values had.

## Danny's picture, in physics terms (tier labels)

| Danny's words | Physics used | Tier |
|---|---|---|
| "an on and off switch, it doesn't turn on until it reaches this point" | The field is frozen by Hubble friction while H(z) is much greater than m, and starts rolling when the expansion rate falls to its own frequency | EVIDENCE (standard field dynamics) |
| "photons start attaching themselves… binding together" | Photons couple to the field through the axial anomaly, one charged fermion at a time, plus one direct coupling C_γ | EVIDENCE (anomaly); C_γ is the new free parameter |
| "they bind again and again as they scale upwards" | The fermion staircase: each species joins the photon coupling only above its own mass threshold (the B1 loop function) | EVIDENCE (Bauer, Neubert & Thamm 2017) |
| "fractal from the bottom up… attach it at Planck, the Big Bang" | The octave ladder: every rung's position is log₂(Planck frequency / rung frequency) | MEANING (a mapping we choose) |
| "we'll see that again at the atomic level" | The same field acts on electron and neutron spins | EVIDENCE (torsion coupling); size computed below |

## The solving equation

**Field (the switch).**

φ̈ + 3H(t) φ̇ + V′(φ) = 0, with V = m²F²[1 − cos(φ/F)]

- The field is "off" (frozen) while H ≫ m, and "on" (rolling) once H(z) has fallen to about m.
- **z_on** is defined as the redshift where the field has covered 10% of its total move since recombination.

**Light (the binding).** For light released at redshift z, the rotation seen today is:

β(z) = (√6/4) (α/π) [ C_γ + S_eff(m) ] · [φ(0) − φ(z)] / M_Pl

where the fermion staircase is:

S_eff(E) = Σ_f N_c Q_f² B1(4m_f²/E²), with B1(τ) = 1 − τ arcsin²(1/√τ) for τ ≥ 1.

- Each fermion f switches on (B1 → 1) only when the energy E rises above its mass. Below the electron mass, nothing has switched on.
- For the Twist today, E = m ≈ 10⁻³³ eV, so S_eff ≈ 10⁻⁶⁶, which is zero: **no fermion rung is switched on.** Only C_γ couples the field to light.
- **The one new parameter is C_γ** (C_γ = 8k in the earlier draft). C_γ = 8 would mean "as strong as all eight units of Standard Model charge".

**Spins (the atomic echo).** For any fermion spin today:

b₀ = (√6/4) · φ̇(today) / M_Pl, where k and C_γ do not enter.

## The two released-light clocks

- **Recombination** (z_rec ≈ 1090): β_rec = β(z_rec).
- **Reionisation** (z_re ≈ 7.7, Planck 2018): β_re = β(z_re).
- **R = β_re / β_rec = [φ(0) − φ(z_re)] / [φ(0) − φ(z_rec)].** C_γ cancels, so R is a pure prediction of the switch.

## Rules

1. **X1. Fit, not evidence.** C_γ is set so that |β_rec| = 0.24° (the locked B4 target); the value for 0.277° is also reported.
   - Pre-computed: C_γ ≈ 14.6 (DES Y5) and 35.4 (Pantheon+).
   - Never counted as support.
2. **X2. Cost.** One extra parameter. Against "ΛCDM + any birefringence parameter" the gain is about 0. Reported as "fits by construction".
3. **X3. R, the switch-reading prediction.** Compute R for both fits after this lock; the predicted band is [min, max] over the two fits.
   - The test happens when low-ℓ (reionisation) EB rotation is measured (LiteBIRD, or low-ℓ Planck analyses such as 2602.12019).
   - PASS if the measured R is within 2σ of the band, FAIL if not. Until then the verdict is OPEN.
4. **X4. Switch-on redshift.** Compute z_on for both fits and log it. It is a description of the switch, not a test.
5. **X5. No direction-dependence.** A smooth field predicts A_CB ≈ 0. It is consistent today (ACT DR6, SPT-3G). A future A_CB detection above 3σ, with no other explanation, counts against.
6. **X6. Achromatic.** The anomaly coupling rotates all frequencies equally. A measured β that scales like ν⁻² (Faraday-like) counts against.
7. **X7. Atomic echo.** Compute b₀ for both fits.
   - **Prediction locked now:** b₀ is below the best laboratory spin limits: electron |b| ≲ 10⁻³¹ GeV; neutron about 10⁻³³ GeV, to be checked against the primary papers when scored.
   - b₀ above a limit means **EXCLUDED at the atomic scale.**
8. **X8. The octave ladder (MEANING only).** Report n = log₂(ω_Pl / ω) for the Planck frequency, the fermion thresholds, recombination and the Twist's note. It is never scored.

9. **X9. The ratio hypothesis** (Danny, before any computation: "silver ratio for the quantum, golden ratio for when it hits atomic", with π as the third candidate).
   - **Candidates:** silver δ_S = 1 + √2 ≈ 2.41421, golden φ_G = (1 + √5)/2 ≈ 1.61803, and π.
   - **Quantum set Q:** the 8 successive ratios of the 9 charged-fermion masses sorted by mass (PDG central values in MeV: e 0.51099895, u 2.16, d 4.67, s 93.4, μ 105.6583755, c 1270, τ 1776.86, b 4180, t 172690). **Primary constant: silver.**
   - **Atomic set A:** the first ionisation energies of Z = 2–20 divided by hydrogen's (NIST, in eV):

     | Element | Energy | Element | Energy | Element | Energy | Element | Energy |
     |---|---|---|---|---|---|---|---|
     | H | 13.598 | N | 14.534 | Mg | 7.646 | Cl | 12.968 |
     | He | 24.587 | O | 13.618 | Al | 5.986 | Ar | 15.760 |
     | Li | 5.392 | F | 17.423 | Si | 8.152 | K | 4.341 |
     | Be | 9.323 | Ne | 21.565 | P | 10.487 | Ca | 6.113 |
     | B | 8.298 | Na | 5.139 | S | 10.360 | | |
     | C | 11.260 | | | | | | |

     19 values. **Primary constant: golden.**
   - **Statistic:** D(c) is the mean, over the set, of the distance from log_c(r) to the nearest integer. Its range is 0–0.5, and lower means the set sits closer to whole powers of c.
   - **Null:** 100,000 random constants drawn log-uniform on [1.3, 3.5], each scored with the same D. The p-value is the fraction of random constants with D at or below the candidate's. This calibrates the trivial matches near r ≈ 1 automatically.
   - **Verdict per set:**
     - **SUPPORTED** if the primary constant has p < 0.05/3 (Bonferroni over the three candidates);
     - **SUGGESTIVE** if p < 0.05;
     - **NOT SUPPORTED** otherwise.
   - All six (set, constant) pairs are reported; only the two primaries carry verdicts.
   - **Expectation, logged before computing:** NOT SUPPORTED for both. No silver or golden pattern is known in fermion masses or ionisation energies, but the Koide relation, (m_e + m_μ + m_τ)/(√m_e + √m_μ + √m_τ)² ≈ 2/3, is known prior art for numerical patterns in lepton masses.

## What B4-X cannot claim

- That the Twist "explains" birefringence.
- That the ladder is physical. The octave positions are arithmetic on known masses.

The most it can earn is that the switched Twist, with one coupling, makes three numbers future data can break: R, z_on and b₀.
