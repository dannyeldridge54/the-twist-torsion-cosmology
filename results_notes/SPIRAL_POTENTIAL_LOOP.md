# Scales loop: finding the spiral's missing pieces (dilaton potential; matter blindness). Exploratory, not tests

Danny, 2 Nov: "do the scales loop to find them" (PATH_DECISION gaps 4 and 7). Local search plus online rounds.
**Tier:** HYPOTHESIS. Nothing here is locked or scored.

## Round 0 (local)

Nothing on a dilaton potential. Earlier notes cover only the fermion axial coupling (NIEH_YAN_PLAN.md) and
Immirzi–fermion papers (DEEP_DIVE_HINTS_2026-11-01.md).

## Round 1 (online, 4 searches): 3 leads

1. **Torsion four-fermion condensate as dark energy.** Alexander, Biswas & Calcagni, PRD 81, 043511 (2010),
   arXiv:0906.5161; also arXiv:1102.5667. Integrating out torsion gives a four-fermion interaction whose strength
   depends on γ. A condensate forms; at late times it gives negative pressure. A follow-up fixes γ ≈ 1/550 to match the
   dark-energy density. It is a potential for the condensate, not directly for the dilaton.
2. **Supergravity superpotential.** Ketov et al. (arXiv:1108.0877): the dilaton potential is not derivable from first
   principles. In supergravity it must come from a superpotential W. **Computed** (`bi_superpotential.py`, sympy) for
   constant W with the Gates–Ketov–Yunes K:
   - V(ϕ) = (81/2) W² (−ϕ − 1) e^{−6ϕ} / ϕ².
   - Extrema at **ϕ = −½ (exactly the GR point; a local maximum, V = −1627 W²)** and ϕ = −2/3 (the minimum,
     V = −1658 W²). V = 0 at ϕ = −1. Positive and steep for ϕ < −1 (steepness 8 at −1.5, 14 at −3; Toomey et al. need
     more than 5).
   - **Problems:** both extrema are at negative energy (anti-de Sitter), so a constant uplift is needed (a second
     parameter). The minimum is not the GR point: settled there, matter would feel β ≈ 0.14 (α ≈ 0.19), far above
     Cassini. So constant W fails in Reading A, and works at best in Reading B with an uplift.
   - **Notable:** the potential's turning point falls exactly at the matter-decoupling point ϕ = −½. Found after
     looking (MEANING).
3. Running of γ from fermion loops (Benedetti & Speziale, arXiv:1111.0884): renormalisation, not a potential. Not
   useful here.

## Round 2 (online, 2 searches + 2 primary pages): 2 hits

- **No-go theorem (Brax & Martin, PLB 647, 320 (2007), hep-th/0612208):** no-scale supergravity quintessence
  either behaves like a cosmological constant or violates gravity tests; the chameleon is not strong enough. **This
  is the same wall the SSG check and the constant-W potential hit in Reading A.**
- **Hong, Mukaida & Yanagida (arXiv:2506.01543, June 2025):** a complex field with a Brans–Dicke coupling
  ξ|Φ|²R and a cosine for its angle (from breaking O(2) to D₄), motivated by DESI. **This is the closest published
  relative of the spiral.** No fifth force, because the theory is scale (Weyl) invariant. Their decay constant is
  f = M_Pl/(4√ξ) ≳ 10 M_Pl. No phantom-crossing analysis.

## Round 3 (online, 1 search + 1 primary page): the matter-blindness mechanism

- **Scale invariance makes Reading B natural, not chosen.** If every matter mass comes from the same field (Higgs–
  dilaton models: Garcia-Bellido, Rubio, Shaposhnikov & Zenhäusern; Blas, Shaposhnikov & Zenhäusern arXiv:1104.1392),
  the dilaton is the Goldstone boson of broken scale symmetry. It then has only derivative couplings to matter, and
  Ferreira, Hill & Ross argue that it fully decouples. That evades all fifth-force bounds. Quantum corrections add a
  small coupling that is still below solar-system limits.
- **The torsion version exists:** Piani & Rubio, JCAP 05 (2022) 009, arXiv:2202.04665: Higgs–dilaton in
  Einstein–Cartan gravity with Holst and Nieh–Yan terms, with attractor behaviour from the curvature of field space.
- **Consequence for the spiral:** in a scale-invariant torsion theory, the radius of the spiral is the dilaton and
  matter does not feel it. That is Reading B, derived from a symmetry. It also supplies the potential's origin: a
  scale-invariant potential plus a cosmological-constant-like term gives a runaway in the Einstein frame (as in the
  unimodular Higgs–dilaton). That runaway is the kind of potential Toomey et al. need.

## Round 4 (online, 2 searches): 2 hits

- **Geometry link:** Karananas & Rubio (arXiv:1606.08848): scale-invariant two-field (Higgs–dilaton) models have a
  nearly constant-curvature hyperbolic field space, the same kind of geometry as α-attractors. Mapping the curvature to
  α is my inference, not a sourced statement.
- **The plain scale-invariant dilaton is too tame:** the Higgs–dilaton model (Garcia-Bellido, Figueroa, Rubio et al.,
  arXiv:1107.2163) predicts **0 < 1 + w0 < 0.02**, tied to n_s through the same curvature. DESI-type fits want
  w0 ≈ −0.84. So a runaway dilaton alone is almost a cosmological constant. The extra evolution would have to come from
  the angle (the kinetic mixing), which that model does not have.
- **A unifying lever (HYPOTHESIS):** in that family, one field-space curvature sets both n_s and w0. Our α = 1 gives
  n_s = 0.967 at N = 60 (2.4σ low, UFE_CHECKS_RESULTS.md). A one-geometry Twist would predict a definite (n_s, w0) pair,
  which is testable.

## Round 5 (online, 2 searches): 2 hits

- **Torsion supports scale invariance:** Karananas, Shaposhnikov, Shkerin & Zell (arXiv:2108.05897): Einstein–Cartan
  gravity accommodates global scale and local Weyl invariance with non-propagating torsion. Global scale invariance
  needs an extra dilaton; under Weyl symmetry the dilaton is pure gauge.
- **Burgess-group minimal axio-dilaton** (arXiv:2410.11099) chooses couplings that avoid a fifth force between
  baryons. Ramos-Hamud et al. (arXiv:2609.22539) reach χ² 50.4 against 51.6 for ΛCDM on DESI BAO only, so no real
  preference.

## Round 6 (online, 1 search): 0 new hits on the question

Weyl-invariant Einstein–Cartan with a Holst term gives an axion-like field of gravitational origin (Karananas et al.
arXiv:2406.11956, strong CP and hierarchy; Gialamas arXiv:2602.00317, reheating). **No paper connects this framework to
late dark energy.** Loop levelled off.

## Where it stands (loop closed after round 6)

| Missing piece | Best candidate found | Status |
|---|---|---|
| Matter blindness (Reading B) | Scale (Weyl) invariance: dilaton = Goldstone, derivative couplings only | Known mechanism; the torsion version exists (Piani & Rubio). Must be checked against the GKY embedding (which has Reading A built in) |
| Dilaton potential | (a) scale-invariant potential + Λ → Einstein-frame runaway; (b) supergravity constant W + uplift; (c) fermion condensate | (a) best fits Toomey's need; (b) computed above, steep but AdS without uplift |
| Closest published model | Hong, Mukaida & Yanagida 2025 (complex field, BD coupling, cosine angle) | Read: same structure, no phantom analysis, needs ξ ≲ 10⁻³ |

**The spiral, assembled from published pieces (HYPOTHESIS; each piece exists, the combination does not):**
1. **Torsion gravity that is scale (Weyl) invariant** (Karananas et al. 2021): the radius of the spiral is the dilaton,
   and matter is blind to it (Reading B from a symmetry).
2. **The angle is the BI field** with its torsion axial coupling, and a cosine potential (as in Hong, Mukaida &
   Yanagida 2025).
3. **Hyperbolic field space** gives the kinetic mixing e^{λχ} that produces the phantom illusion (Toomey et al.).
4. **A runaway dilaton potential** from scale invariance plus a constant term (Higgs–dilaton).

The gap in the literature is the late-dark-energy use of exactly this combination. **The decisive missing calculation:**
does the combination give a w(z) far enough from −1 (w0 ≈ −0.8) without breaking n_s? The plain dilaton gives
1 + w0 < 0.02, so the angle's mixing must supply the rest.

**Tension to resolve:** the Gates–Ketov–Yunes embedding (which gave λ = −2√(2/3)) has matter on the supergravity
Jordan frame (Reading A). The scale-invariant route gives Reading B. Whether one model can have both, the α = 1 geometry
and scale invariance, is the open question for round 4.
