# Theory checks toward a unified field: T1, radiative stability, T3 (2 Nov 2026)

**Script:** `theory_checks.py` writes `theory_checks.json`. Parts A and B are arithmetic; part C is symbolic (sympy).
**Tier:** the calculations are EVIDENCE about the model as written; the conclusions about unification are HYPOTHESIS.

## A. T1: can ONE field with V = early term + late term do both roles? **No, by a factor of 10⁶–10⁸ in energy.**

- **Setup:** after the early episode the field sits at the early term's minimum. The late role then needs it to roll
  by Δφ = 0.083 M_Pl (Pantheon+ best) or 0.202 M_Pl (DES Y5 best).
- **The obstacle:** the early term Λ₁⁴[1 − cos(φ/F₁)]³ is fixed by the early fits: F₁ = 0.139–0.148 M_Pl,
  f_EDE ≈ 0.075–0.08 at z_c ≈ 3560, and Λ₁⁴ ≈ 2.7×10⁸ ρ_crit,0.

| Early fit | Late fit | Roll needed | Roll allowed (early term ≤ 10% of dark energy) | Early-term energy at the needed roll |
|---|---|---|---|---|
| Planck locked | Pantheon+ | 0.083 | 0.0049 | 2.4×10⁶ × ρ_DE |
| Planck locked | DES Y5 | 0.202 | 0.0049 | 3.1×10⁸ × ρ_DE |
| P-ACT locked | Pantheon+ | 0.083 | 0.0051 | 1.7×10⁶ × ρ_DE |
| P-ACT locked | DES Y5 | 0.202 | 0.0051 | 2.3×10⁸ × ρ_DE |

- **Conclusion:** a single real field with a sum of the two potentials cannot carry both roles. The late roll needed
  is 17–41× larger than the early term allows.
- **Independent agreement:** Giarè & Sakstein (arXiv:2605.26116, JCAP 2026) find that one minimally coupled field
  needs a three-slope "steep–steeper–shallow" potential, and that couplings to dark matter do not help.
- **Prior single-field attempts:** 2309.08082 (attractor; disfavoured by data) and 2408.03229 (modified steep
  exponential).
- **Multi-field precedent:** 2609.11907 ("A Multi-Axion Ladder Across Cosmic History").

## B. Radiative stability: matter loops generate **no potential**; the kinetic correction is about 5×10⁻³³

- **The reason:** the field touches matter only through c(φ) ∂_μφ J₅^μ = ∂_μG(φ) J₅^μ, in both the Nieh–Yan and the
  Holst forms. Matter loops therefore depend on φ only through ∂G. They renormalise kinetic terms but can never
  create or shift a potential (the shift symmetry in G is exact).
- **Size of the kinetic renormalisation** from the heaviest fermion (top quark, one loop, generous logarithm):
  **δZ ≈ 5.3×10⁻³³**. This is negligible.
- **Consistent with the literature:** for shift-symmetric axion quintessence the symmetry is exact perturbatively,
  so the potential is technically natural (Frieman et al. 1995; reviews 2509.17059, 2603.03433).
- **Particle production by the rolling field** (Kulkarni & Sorbo, 2408.04550): production is efficient only when
  m_f ≪ (field mass)²·θ₀/H. For the Twist (field mass ≈ H₀, θ₀ ≈ 0.1) even the electron misses this by about
  10³⁰, so production is expected to be negligible. This is an estimate from their scalings, not a full calculation.
- **What this does NOT solve:** the potential's existence and scale (meV) are still put in by hand. Stability is
  not an explanation.

## C. T3: the non-minimal fermion coupling changes nothing observable at this order

- **The coupling:** Torres-Gomez & Krasnov (arXiv:0811.1998, eq. 16) give it as
  (3/4)(γ²+1)⁻¹ ∂_μγ (A^μ + α γ V^μ).
- **Checked symbolically:**
  - **The vector (non-minimal) piece is a total derivative:** (3α/4)·γ/(γ²+1)·∂γ = ∂[(3α/8) ln(γ²+1)]. Times a
    conserved current it integrates to zero, so it has no effect for conserved currents. Only anomalous B+L,
    i.e. electroweak sphalerons, could feel it; that is negligible today.
  - **The axial piece is independent of α**, and per canonical φ it equals **√6/(4 cosh χ)**: exactly the Holst
    coefficient used in B4.
- **Conclusion:** the B4 photon verdict and the X7 spin result hold for any real α.
- **Still open:** the Jackiw–Kostelecký regularisation ambiguity; and Hermiticity, since a real effective
  Lagrangian requires real γ.

## The unification road (from a 6-round deep dive: local arXiv library first, then online)

| Item | Status | Best handle |
|---|---|---|
| One field for both roles | **ruled out** for one real field (A); open for two degrees of freedom | the radial ("spiral") idea below; 2609.11907; 2605.26116 |
| Origin and scale of the potential | open | none found that fixes the scale |
| Quantum stability | **done** at one loop for matter (B) | 1402.4854, 1012.4280, 1111.0884 (running of the BI parameter; results disagree, gauge-dependent) |
| Fermion coupling incl. non-minimal | **done** at tree level (C); one-loop ambiguity open | 0811.1998, 0903.4407 |
| LQG black-hole entropy with a moving γ | partly studied: hairy, "super-entropic" black holes; γ → constant at infinity recovers LQG | Boudet et al. 2012.02700 (PRD 103, 084034), 2203.08558 |
| Swampland / weak gravity | tension noted; nothing BI-specific found | 2203.05575 |
| Standard Model unification | open; whether Einstein–Cartan is *required* is debated (2025) | McKeon et al. and rebuttal; 2605.09571 (EC pseudoscalaron) |
| Phantom crossing (DESI) | impossible for one canonical field; easier in modified gravity | 2606.20434 (Hubble-tension review) |

**Open after 6 rounds** (the limit; a last round with no new hits was not reached): saxion-driven growth of the
decay constant linking the early and late roles had no direct match; the closest are 2004.10025, the axio-dilaton
models and 2609.11907.

## Next candidate model: the "spiral Twist" (HYPOTHESIS, Danny's radial picture)

- **The idea:** the Twist angle θ is the phase of a complex field Φ = ρ e^{iθ}. Its radius ρ sets the effective
  decay constant, F = ρ.
- **What the fits ask for:** early F ≈ 0.14 M_Pl and late F ≈ 1–2.5 M_Pl, so ρ must grow about 10× between z ≈ 3500
  and today, while θ turns (late Δθ < 0). The path in the complex plane is then a spiral, not a straight roll.
- **Why it is allowed:** it has two degrees of freedom, so it sits outside the one-real-field no-go (A and
  2605.26116).
- **Before any fit:**
  1. write the radial potential that makes ρ grow at the right time;
  2. check the radius stays light enough not to spoil the CMB, but heavy enough not to act as extra dark matter;
  3. pre-register the test.

## Deep dive continued (Danny: "deep dive loop till done"), rounds 7–19; round 19 had no new hits, so DONE

| Round | Found | Use |
|---|---|---|
| 7 | Sengupta 1501.00779 (CQG 32, 195005): torsional (Nieh–Yan) instantons fix the BI vacuum angle via H₀; Kaul & Sengupta 1411.4793 (BI = instanton vacuum angle); Choi, Suzuki & Yanagida 1910.00459 (meV potential from electroweak instantons, f ≈ M_Pl); Kobayashi & Takahashi 1607.04294 (a changing decay constant can amplify perturbations) | Potential-origin candidates; a spiral-Twist risk to check |
| 8 | Kobayashi & Takahashi: the enhancement happens when f **shrinks**. The spiral Twist needs f to **grow**, so the risk points the other way (to be confirmed in a full model). Sengupta eq. 10: vacuum energy ∝ e^(−S) cos η, a **cosine in the BI angle** | A cosine origin for the late (n = 1) potential |
| 9 | The required instanton action is **S ≈ 276** (272–281); instanton/wormhole effects near 10⁻¹²⁰ M_Pl⁴ are the standard route; wormholes can threaten the shift symmetry (2209.12281); **Shiu et al. 2604.09141: quantum-gravity limits push axion-quintessence masses ≫ H₀** (our m ≈ 0.5–1.3 H₀) | Scale origin plausible; **state the m ≈ H₀ tension in the paper** |
| 10–11 | Mercuri & Randono 1005.1291 (CQG 28, 025001): BI as instanton θ-angle, combining G, Λ and θ; Garcia de Andrade & Gao, EPJC 86, 322 (2026): claimed γ ≪ 10⁻⁵⁸ | The γ bound rests on an assumed THz torsion wave in modified Holst gravity; it would also clash with LQG's γ ≈ 0.24. **Not applicable to a minimally coupled BI field** |
| 12 | Aliberti & Lambiase, PLB 846 (2023): BI bound from gravitational baryogenesis (constant γ, Ṙ coupling) | Model-specific; not applicable as stated |
| 13 | **Broda & Szanecki, PLB 690, 87 (2010): Standard Model fields induce γ = 1/9, cutoff-independent** | The SM–BI link: a required citation for the SM item. Our field today maps to γ ≈ 0.04–0.47 under one convention (MEANING only) |
| 14 | Single-field unification attempts: Kouniatalis 2603.11706 (bump plus exponential tail; qualitative, no fit), Copeland et al. 2309.15295 (scaling solutions) | T1 prior art; none uses a complex field with a growing radius |
| 15 | Liu et al. 2507.04265 (EPJC 85, 1351): the torsion parameter is consistent with zero, **but the authors also report an AIC preference** (ΔAIC −5.7 to −6.6); Izaurieta, Lepe & Quinzacara 2607.16370: a no-go, since homogeneous torsion cannot produce DESI's phantom crossing | Paper wording on liu2025torsion completed; supports "the Twist cannot follow DESI" |
| 16 | **Kang, Li & Yi 2602.00506 (EPJC 2026): coupling dark energy to the Nieh–Yan density in teleparallel gravity allows phantom crossing without instabilities; the prediction is parity-violating GWs.** Pre-geometry 2609.10619: Holst and Nieh–Yan emerge with Einstein–Hilbert and Λ from one SO(1,4) gauge theory | **The strongest route for the Twist family to follow DESI** (a "Nieh–Yan Twist", HYPOTHESIS) |
| 17 | Wu et al. 2110.13870: LIGO-Virgo bound on the Nieh–Yan parity-violation scale, M_PV < 6.5×10⁻⁴² GeV; our φ̇-scale b₀ = 1.4–3.5×10⁻⁴³ GeV is about 20–45× below it (approximate, as the definitions differ) | A Nieh–Yan Twist would currently pass GW tests |
| 18 | **2507.10696: the Nieh–Yan coupling adds to the pseudoscalar kinetic term and raises the effective decay constant**, so a sub-Planckian fundamental f behaves as a Planck-scale F | Addresses the swampland tension; a possible mechanism for a changing F_eff (the radial idea without a second field) |
| 19 | No new results; confirms that nobody has applied the Nieh–Yan F-enhancement to late-time dark energy | **DONE (0 hits)**. An open lane next to the Twist |

## Updated road (after 19 rounds)

| Item | Status now |
|---|---|
| One real field, both roles | ruled out (A; Giarè & Sakstein) |
| Two degrees of freedom / changing F_eff | **two routes**: (i) the spiral Twist (complex field, radius grows); (ii) the Nieh–Yan-enhanced F_eff (2507.10696) |
| Potential origin and scale | **candidate**: torsional-instanton cosine in the BI angle (Sengupta), S ≈ 276 |
| Following DESI (phantom crossing) | minimal field: no. Nieh–Yan coupling in teleparallel gravity removes the *perturbative* obstruction (2602.00506), but a canonical field's background still has ρ+p = φ̇² ≥ 0, so the Twist would also need a **non-canonical kinetic term**. GW parity test currently passed |
| Swampland | F_eff can be Planckian while f is sub-Planckian (2507.10696). Shiu et al.: m ≫ H₀ tension, unresolved |
| Standard Model | γ = 1/9 induced by SM fields (Broda & Szanecki); full unification open |
| LQG black-hole entropy | Immirzi-hair black holes (Boudet et al.) |
| Quantum stability, T3 | done (B, C) |

**Next model to pre-register (HYPOTHESIS): the "Nieh–Yan Twist".** The Twist field couples to the Nieh–Yan density in
teleparallel gravity. The predictions to lock before any fit:
1. phantom crossing allowed, so it can follow DESI;
2. parity-violating GW velocity birefringence at about b₀;
3. F_eff enhanced by torsion.

The spiral Twist is the alternative.
