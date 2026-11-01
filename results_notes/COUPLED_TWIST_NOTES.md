# Coupled Twist: working notes (beside PREREGISTRATION_COUPLED_TWIST.md, which is locked)

## 1. The φMDE value used in gate V3: derived in our convention

The literature quotes both Ω_φ = 2β²/3 and 4β²/3. The difference is only how β is normalised. Ours:
- m_c ∝ exp(βφ/M_Pl), with M_Pl the reduced Planck mass;
- φ̈ + 3Hφ̇ + V_φ = −(β/M_Pl) ρ_c.

**Derivation:**
1. Let x = φ̇/(√6 H M_Pl). In the matter era with V negligible: 3H²M² = ρ_c + φ̇²/2, Ω_φ = x², and
   Ḣ = −(3/2) H² (1 + x²).
2. At a fixed point (x constant), φ̈ = √6 x M Ḣ. Substituting into the field equation with ρ_c = 3H²M²(1 − x²):
   (3√6/2) x (1 − x²) = −3β (1 − x²).
3. So **x = −√(2/3) β, and Ω_φ = 2β²/3**: the value in gate V3. It also sets the sign check: β > 0 gives φ̇ < 0.

**Correction to the sign wording in gate V4** (the file is locked, so it is noted here): V4 says "β > 0 makes ρ_c fall
faster than a⁻³ while φ̇ > 0". From the equations, ρ̇_c + 3Hρ_c = (β/M) φ̇ ρ_c, so ρ_c falls faster than a⁻³ whenever
β φ̇ < 0. In the φMDE that means β > 0 with φ̇ < 0. The gate will be applied as "ρ_c a³ changes at the rate (β/M) φ̇,
with the sign of β φ̇", the physical content V4 intends. This is logged as a deviation before any code is written.

## 2. Bounds behind the C5 expectation (checked)

- **Planck 2013** (Xia, arXiv:1311.2131): β < 0.102 from Planck alone; β < 0.052 with BAO, SNe and lensing (95%).
- **Pettorino et al. 2013** (arXiv:1305.7457): β = 0.036 ± 0.016 (Planck + WP + BAO), compatible with zero at 2σ.
- These papers may normalise β differently from us, by up to a factor √(2/3). In any normalisation, |β| = 0.816 is
  8–20 times above the bounds, so the "EXCLUDED" expectation stands.

## 3. Torsion-native dark-matter couplings (online check)

- **The Einstein–Cartan portal** (arXiv:2008.11686) uses torsion-induced four-fermion contact interactions, with
  non-minimal Holst and Nieh–Yan couplings, to *produce* dark matter in the early universe.
- These are axial contact terms. For unpolarised dark matter they give no background coupling.
- So C5's "one parameter-free torsion choice" holds **for a conformal background coupling**, which is the kind this
  test is about.

## 4. Bounds on γ itself (online check, no effect on our tests)

- **Reported bounds:** γ ≲ 10⁻⁵⁸ (EPJC 86:322, 2026) and about 10⁻³¹ (arXiv:2412.05982). Both come from one group's
  model-dependent arguments and are not widely confirmed.
- **Why our fits do not depend on them:** V depends only on (φ − φ₀)/F, so the absolute field value, set by γ through
  φ = √(3/2) M_Pl arsinh(1/γ), drops out of every fit.
- **Where they would matter:** only the interpretive link "today's γ ↔ the field's position". If γ really were that
  small, φ₀ ≈ √(3/2) M_Pl · ln(2/γ) would be about 160 M_Pl. That is a trans-Planckian field value, which would add to
  the weak-gravity-conjecture concern already in the paper.

## Prior art found in the scales review (13:20, 1 November 2026)

- **arXiv:2609.03062** (Sep 2026), "Reassessing Evidence for Dark-Sector Interactions with Dynamical Dark Energy and
  DESI DR2":
  - A thawing dark-energy trajectory with an interaction Q = βHρ_de, fitted to Planck + ACT + DESI DR2 + DES-Dovekie.
  - They report Δχ²_MAP −10.00 with the interaction, against −3.93 without it, and β = 0.53 (+0.24 / −0.13).
  - Numbers are from the abstract and snippets; they must be checked in the PDF before citing.
- **How it differs:**
  - Their coupling is a phenomenological energy-transfer term proportional to H ρ_de, on a parametrised trajectory.
  - Ours is a conformal (Lagrangian) coupling, m_c ∝ e^{βφ/M_Pl}, on a field with the n = 1 potential.
  - The numbers are not directly comparable.
- **Use:**
  - Cite it in the paper as the closest prior art for the Coupled Twist.
  - Report our C2 (D_c) beside their "−10 vs −3.9" pattern.
  - No rule changes.

## Prior art found in the 2026-11-01 15:05 review: Babu & Amendola, arXiv:2610.23497 (16 Oct 2026). Cite; the closest match yet

- **What they did:** coupled thawing quintessence with **a cosine potential** (our n = 1 shape) and a double-exponential
  hilltop, fitted to DESI DR2 BAO + Planck PR4 + three SN compilations.
- **What they found:**
  - Δχ² = 5–15 against ΛCDM, recovering 64–92% of the w0–wa improvement;
  - **|β| < 0.073 (95%)**, with a bimodal posterior near ±0.05;
  - only the negative mode gives the apparent phantom crossing (near z ≈ 1), and it is preferred;
  - "favoured but not yet required".
- **For us:**
  - **C5 (β = 0.816) is about 11× their bound**, which supports the pre-registered expectation EXCLUDED;
  - our C1–C4 prior (β in ±0.15) brackets their modes;
  - C4 (phantom crossing) can be compared directly with their sign result.
- The coupling form is not given on the abstract page; check it in the PDF (theirs may be conformal, like ours).
- **Novelty, said honestly:** the coupled cosine model itself is published. What we add is the torsion motivation,
  the pre-registration, ACT DR6 + SPT-3G in the CMB, and the Dovekie and DES Y5 brackets.
- They cite a prior study reporting 3–5σ coupling evidence (cosine-like, ACT + SPT-3G + DES-Dovekie) that their
  results disagree with. Find it in their bibliography before writing COUPLED_TWIST_RESULTS.md.
- **No rule changes.**
