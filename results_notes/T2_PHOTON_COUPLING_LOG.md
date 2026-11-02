# T2: the photon coupling from torsion. Work log (STOPPED on Danny's request, 2 Nov ~10:1x)

**Status:** stopped early; nothing derived, locked or compared. A working log only.

## Why T2 matters

The birefringence test (B4) needs the Twist's coupling to light, c_γ:

β_rot ≈ c_γ · (α / 2π) · Δθ

- Δθ is the field-angle change since recombination; it comes from the corrected Late Twist fits, which are finished.
- The measured rotation is 0.24° ± 0.06° (ACT + Planck).
- Rough requirement: c_γ · Δθ ≈ 3.6. With Δθ ≈ 0.1–0.5, c_γ would need to be about 7–36 (order of magnitude; the factors depend on conventions, which T2 must fix).

## Planned route (not yet done)

1. Barbero–Immirzi field → fermions: the effective derivative coupling to the axial current, (∂_μφ / f_J) J₅^μ, with a coefficient set by the torsion construction. It depends on minimal vs non-minimal fermion coupling (the T3 caveat).
2. Axial current → photons via the chiral anomaly: ∂_μJ₅^μ ⊃ (α / 2π) Σ_f N_c Q_f² F F̃ (convention to be fixed).
   - Over all Standard Model charged fermions, Σ N_c Q² = 3 (leptons) + 4 (up-type quarks) + 1 (down-type quarks) = 8.
3. So c_γ ~ (F / f_J) × 8 × (coupling-choice factor).
   - F ≈ 1–2.5 M_Pl from the corrected fits.
   - f_J ~ M_Pl / (a torsion coefficient).
   - If the torsion coefficient is order 1, c_γ could plausibly be order 10, inside the needed window. **This is speculation until the coefficients are derived. Nothing here is a prediction.**
4. Compute Δθ from the corrected best fits (AxiCLASS background, φ at recombination vs today).
5. Write and lock the B4 prediction before comparing.

## Literature checked so far

These abstracts give no coefficients; the full texts are needed:
- Mercuri & Taveras, arXiv:0903.4407: a generalised Holst action giving "a more natural coupling" of the BI field to fermions; an earlier version had "a rather unnatural coupling with fermions".
- arXiv:0811.1998: "an effective interaction between the scalar field and the fermionic currents" (axial or not is unspecified in the abstract).
- Taveras & Yunes, arXiv:0807.2652: the BI parameter promoted to a field, equivalent to GR plus a scalar with non-trivial kinetic energy.
- Logged earlier: Alexandrov arXiv:0802.1221 (the classical effective action can be independent of γ for suitable non-minimal coupling); Freidel, Minic & Takeuchi hep-th/0507253 (no parity-violating vector–axial term with minimal coupling); Gao & Garcia de Andrade arXiv:2412.05982 and 2502.04727 (photon–axion conversion depends on the BI parameter).

## Restarted 2026-11-02 ("i want the bio going"): results

- **Full texts read.**
  - 0903.4407 (Nieh–Yan form) eq. 22: the coupling is −(√6/4)√κ ∂φ·J₅, fixed by the theory and independent of any added scale (App. A).
  - 0811.1998 (Holst form) eq. 16: the same coupling with an extra factor 1/cosh χ.
  - Mercuri & Taveras' footnote 5 gives the photon scale as f⁻¹ = (α/2π)F_φ⁻¹, which is our formula with S = 1.
- **The standard-EFT catch.** A pure derivative coupling to a gauge-invariant axial current decouples from photons far below the fermion masses (Quevillon & Smith, 1903.12559). Under that reading, c_γ ≈ 0.
- **Δθ at the NR best fits** (nlfix/delta_theta.py):
  - Pantheon+: −0.033 (Δφ = −0.083 M_Pl);
  - DES Y5: −0.202 (Δφ = −0.202 M_Pl).
- **Under the generous anomaly reading,** c_γ = 2·(√6/4)·8·F ≈ 9.8 F, which lands inside the 7–36 window the earlier speculation guessed. But Δθ is smaller than hoped, so the predicted |β| is:
  - Pantheon+: 0.054°;
  - DES Y5: 0.13°.
- **Numbers and the proposed rule** are in PREREGISTRATION_B4_BIREFRINGENCE_DRAFT.md (not locked); the calculation is b4_birefringence_numbers.py.

## Locked and scored

- **Locked as written:** 2026-11-02 10:20:30, by Danny's "Lock as written".
- **Headline:** EXCLUDED (primary branch E at the DES Y5 fit, z = 4.0).
- **Secondary:** only the Nieh–Yan, S = 8 reading at the DES Y5 fit is CONSISTENT (z = 1.8).
- **Details:** B4_BIREFRINGENCE_RESULTS.md.
