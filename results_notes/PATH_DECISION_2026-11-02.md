# Path decision, 2 November 2026 (review loop: local files + online, 7 rounds; first level at 15:08:47, closed before 15:16:29 by Get-Date)

**Status:** a working plan, not a result. Nothing here changes a pre-registration. The paper is untouched (on hold).

## 1. The full picture

**What our own data say (local):**
- The Late Twist's best result (Δχ² −6.23, DES Y5) comes almost entirely from the DES Y5 supernovae (−8.89). On the
  recalibrated DES-Dovekie sample it falls to −1.33, and on Pantheon+ it is a tie. It survives removing DESI
  (−5.33), so it is a *supernova* hint, not a DESI one.
- The Coupled Twist (−7.91) is DESI-driven, and gets lost without DESI.
- Every Twist version loses to w0–wa: by 10–13 in χ² (Late) and +4 in ΔAIC (Coupled).
- Theory: one real field for both roles is ruled out; the coupling is radiatively stable. The Nieh–Yan period gives
  F = (4/π)√(3/2) M_Pl = 1.56 M_Pl if the torsion length is the Planck length.

**What the literature says (online, new this round):**

| Find | What it means for us |
|---|---|
| Zhang, MNRAS 552 (Sep 2026), truncation test | The DES Y5 signal falls from 4.0σ to about 1.5σ when the z < 0.08 supernovae are removed; Dovekie collapses. **Our Late hint lives in the sample with the known low-z problem.** |
| Huang et al. arXiv:2502.04212; arXiv:2609.04334 | The same low-z offset (z < 0.1) is identified as the driver. |
| Bayesian analysis, arXiv:2511.10631 | No Bayesian evidence for dynamical dark energy once DES Y5 is recalibrated (ln B = −0.30). |
| SN-Unite, arXiv:2609.05321; Union3.1 (arXiv:2601.19424) | Union3.1, Dovekie and Pantheon+ now agree; together with BAO+CMB they give about 3σ for evolving dark energy. Our LU test uses the *original* Union3 (the Cobaya likelihood); no public Union3.1 Cobaya likelihood was found. |
| Babu & Amendola, arXiv:2610.23497 (already cited) | The coupled cosine model (≈ our Coupled Twist) gets −15.3 (DES Y5), −9.9 (Union3), −5.1 (Pantheon+) vs ΛCDM, and still loses to w0–wa by +1.3 to +3.6. Even the best published version of our class of model trails w0–wa. |
| Toomey, Hughes, Ivanov & Sullivan, arXiv:2511.23463 (logged, now read in full) | An axion whose kinetic term is multiplied by e^{λχ} of a second, dilaton-like field **looks phantom in a w0–wa fit without being phantom**: no ghost, null energy condition kept. Supported at 2.5–3σ. |
| Argudo-Panes et al., arXiv:2609.10133 | A safe w = −1 crossing via non-minimal coupling (1 + αφ²) to gravity; about 2σ over ΛCDM with Dovekie. |
| Aboubrahim, Giman & Nath, arXiv:2511.22559 | Axion dark energy fits to DESI DR2 prefer a sub-Planckian decay constant (number to be confirmed from the full text). In tension with our late F = 1.0–2.5 unless the Nieh–Yan enhancement is used. |
| Gao et al. arXiv:2608.09487 and 2608.19392 (already cited) | A dynamical BI field passes the GWTC-3 dark-siren test (coupling ≲ 10⁻³); no cosmology fit in these papers. |

## 2. What this means

1. **The Late Twist hint is probably a DES Y5 low-redshift calibration effect.** Three independent groups locate the
   DES Y5 excess at z < 0.1, and our own Dovekie test already weakened it. Union3 (LU, running) is the decisive check
   that was locked in advance. If LU comes out NOT CONFIRMED, we say so plainly.
2. **The ghost route (K < 0, NIEH_YAN_TWIST_DRAFT.md) is the wrong next model.** It needs a ghost-sign kinetic term
   at the background level and a strong-coupling point at K = 0. Toomey et al. show a ghost-free way to *look*
   phantom: two fields, with the angle's kinetic term multiplied by a function of the other field.
3. **That ghost-free way has the Spiral Twist's shape, under one condition.** Write the Twist as Φ = ρ e^{iθ}: an
   angle (the Twist) and a radius (Danny's radial growth). This is the same two-field structure as Toomey et al.
   (angle × function of a second field), but the match depends on the geometry of field space:
   - **Flat** (an ordinary complex field): the kinetic term is (∂ρ)² + ρ²(∂θ)², so the angle's factor is ρ², a power,
     not an exponential. This is *not* Toomey et al.'s model, and it is not shown to look phantom.
   - **Hyperbolic** (radius kinetic term (∂ρ)²/ρ², as for string axion–saxion pairs): with ρ = e^{λχ/2}, χ is
     canonical and the angle's factor is e^{λχ}. This is **exactly** Toomey et al.'s model.
   - **The Twist's own clue:** the BI field's kinetic term from the Holst action is ∝ (∂γ)²/(1 + γ²) (Calcagni &
     Mercuri; Taveras & Yunes), which is already a curved field space. Whether it gives the hyperbolic form with a
     radial partner is the step-4 theory question.
   - **Tier: HYPOTHESIS.** The two mappings above are algebra; the torsion origin of a hyperbolic radial mode is not
     shown. *(An earlier draft of this note said "exactly the same" without the flat/hyperbolic condition; corrected
     before commit 3411c6c.)*
   - **Round 5 lead: the BI field's supergravity form is already hyperbolic.** Gates, Ketov & Yunes (PRD 80,
     065003 (2009), arXiv:0906.4978) show that promoting the BI parameter to a field in N = 1 supergravity equals
     adding a dilaton–axion chiral superfield Φ = ϕ + i a. The axion couples to the Holst term; the dilaton couples to
     R (a dynamical Newton constant). Their eqs. (5.36)–(5.37), read in the PDF:
     Ω = e^{Φ+Φ̄}(Φ+Φ̄), K = −3 ln(−Ω/3).
   - `bi_kahler_lambda.py` (sympy, residual check 0) gives Kähler metric K_{ΦΦ̄} = 3/(Φ+Φ̄)², i.e. hyperbolic with
     curvature −2/3 (the α = 1 attractor geometry). With a canonical dilaton χ, the axion's kinetic term is multiplied
     by e^{λχ} with **λ = −2√(2/3) = −1.633, fixed, no free parameter.**
   - Toomey et al. fit λ = −1.3 (+1.3/−1.5) on Planck + DESI. **The fixed value lies inside their 1σ range.** This
     was found after their fit, so it is a consistency (MEANING), not a prediction test. It becomes a test if we lock
     λ = −1.633 and fit it.
   - **Rounds 6–7: the value is the α = 1 attractor.** "Quintessential α-attractors, updated"
     (arXiv:2608.19781, eqs. 30–32) writes the hyperbolic axion–dilaton kinetic term as
     −½[(∂φ)² + e^{∓2μφ}(∂a)²] with μ = √(2/(3α)), so λ = −2√(2/(3α)). K = −3 ln gives α = 1 and λ = −2√(2/3):
     **the same number from an independent route.** That paper says this class gives a DESI-compatible "phantom
     illusion"; it gives no α-specific fit. *(Its DESI-matching case uses the e^{+2μφ} sign, so the orientation
     must be matched.)*
   - **Prior art:** the hyperbolic class is published (Toomey et al.; arXiv:2608.19781; Ramos-Hamud et al.
     arXiv:2609.22539, which reports only a slight preference over ΛCDM). **What no source found does:** derive the
     geometry, and so α = 1 and λ, from the Barbero–Immirzi field itself. That link is the possible new contribution.
   - **Main risk (new):** in Gates–Ketov–Yunes the dilaton couples to R, i.e. Newton's constant varies. In the Einstein
     frame that becomes a dilaton–matter coupling. Smith, Mylova, van de Bruck, Burgess & Di Valentino
     (arXiv:2512.13544) find that the couplings DESI prefers in their axio-dilaton (10⁻² to 10⁻¹) would already show
     in solar-system tests unless screened. Step 4 must therefore include the solar-system bound (Cassini:
     |γ_PPN − 1| < 2.3×10⁻⁵) as a gate: the Spiral Twist passes only if the dilaton's matter coupling is below it or
     screened by a stated mechanism.
   - Caveats: the sign of λ depends on how the dilaton is oriented; Toomey et al.'s axion is not our BI field with the
     derived F, and their axion decay constant is about 0.02 M_Pl. Both normalisations must be matched in step 4.
4. **The decay constant can still be derived:** the angle's period, set by the Nieh–Yan index, fixes F (TF-P is
   testing F = 1.56 M_Pl now).

## 3. The path (chosen)

**Road B+: "honest method, and the Spiral Twist as the ghost-free next model."**

| Step | What | Cost | Depends on |
|---|---|---|---|
| 1 | Score R3 Coupled, LU, TF, TF-P as they land; record verdicts (no paper edits) | none | fits running |
| 2 | **Low-z split of the Late hint:** recompute the DES Y5 supernova χ² at the stored best fits, split at z = 0.1 (rule locked first: if more than half the gain comes from z < 0.1, the hint is labelled CALIBRATION-SENSITIVE) | under 1 h, no refits | nothing |
| 3 | **No-refit prediction checks:** H(z) against the 32-point cosmic-chronometer set, fσ8 against an RSD-only compilation, at the stored best fits (rule locked first) | about 2 h | nothing |
| 4 | **Spiral Twist theory note:** the hyperbolic geometry (α = 1, λ = −2√(2/3)) via the Gates–Ketov–Yunes embedding; **the solar-system gate (Cassini) on the dilaton–matter coupling**; then Then the energy transfer, the w_eff formula, the null energy condition, and where the torsion picture fixes λ and F (the parameter count must not exceed w0–wa's) | theory, no CPU | step 1 (TF-P sets F) |
| 5 | Spiral Twist background solver, then validation gates, then lock and fit (DES-Dovekie, Pantheon+, Union3) | about 2 days | step 4 |
| 6 | Long term: MCMC posteriors for the survivors; Union3.1 when a public likelihood exists; DESI DR3 forecasts locked in advance | days | steps 1–5 |

**Road A (derived F as the headline) becomes a branch of step 4:** if TF-P is SUPPORTED or CONSISTENT, the derived F
goes into the Spiral Twist as a fixed number (no free F). If TF-P is DISFAVOURED or EXCLUDED, F stays free and we say
the Planck-length normalisation failed.

**Dropped:** the K(φ) = tanh ghost-sign model (kept in the draft as a record, not pursued).

## 4. What would change this path

- LU **CONFIRMED** (≤ −4 on Union3): the late hint is not just DES Y5. Step 2 still runs, and the Late Twist moves back
  up as a headline.
- Step 4 shows the torsion field space is flat (no exponential factor on the angle): fall back to the coupled route
  (Babu & Amendola class) as the next model.
- Step 4 shows the dilaton–matter coupling is above the Cassini bound with no screening: the Spiral Twist is
  excluded by the solar system before any cosmology fit, and we say so.

## Gaps in the unified-field (UFE) plan (Danny, 2 Nov: "is your plan missing anything"); all HYPOTHESIS, none tested

1. **Inflation is missing.** The geometry we found (α = 1 hyperbolic, K = −3 ln) is the same geometry as Starobinsky-like
   α-attractor inflation, and arXiv:2608.19781 builds inflation and dark energy from one hyperbolic field space. If the
   BI superfield gives α = 1, the same two fields could in principle cover inflation, early energy and late dark energy.
   Not checked: the potential, the energy scales, and whether this conflicts with the SSG pinning.
2. **The early role has no home since T1.** One real field cannot do both roles. A new candidate: the dilaton relaxes
   toward its GR point (ϕ = −½, an attractor) during the radiation and matter eras, and that relaxation could supply the
   early energy, while the axion angle does the late role. To check: is the energy and timing anywhere near
   f_EDE ≈ 0.07 at z ≈ 3500, and does it respect the Cassini band today?
3. **The LQG link is not closed.** LQG black-hole entropy fixes γ ≈ 0.24 (or 0.27, depending on the counting). Nothing
   in the plan asks what value the BI field takes today (or at the GR point) and whether it matches. A clean, cheap
   consistency question.
4. **Matter coupling (Reading A vs B)** must be argued from how fermions couple to torsion (the axial-current coupling
   we already use), not chosen. This decides whether the spiral survives (SOLAR_GATE_RESULTS.md).
5. **Scope of "unified":** today the Twist links gravity (torsion), the dark sector and an axial spin coupling. It says
   nothing about the gauge forces, apart from the excluded photon coupling (B4) and the optional B4-X term. Claims must
   stay at that scope.
6. **Future-data predictions are not locked:** DESI DR3, Euclid DR1, LiteBIRD (birefringence ratio R), LISA and ET
   (parity-violating waves). Each should be written and locked before its data release.
7. **The dilaton has no potential** in the Gates–Ketov–Yunes embedding. In Reading B (matter blind to the dilaton) the
   only thing that moves it is the axion's motion through e^{λχ}. Toomey et al. need an extra steep dilaton potential
   (V₀e^{−αχ}, α > 5) for the phantom illusion. Before the spiral can be fitted, a dilaton potential must come from the
   torsion side (or be added as a stated extra parameter); otherwise the spiral may not move at all.
8. **What "measuring the spiral" would mean** (Danny: "the smaller fields will be easy to find once the spiral is
   measured"): no data so far detect it. Its signatures to lock before fitting: the w(z) shape with an apparent crossing
   near z ≈ 0.4, energy transfer between the two fields (a growth signature), the birefringence ratio R and
   parity-violating gravitational waves. The earlier ratio tests (silver/golden spacings) were not supported, so any
   ladder of smaller fields needs its own locked test.
9. **The Planck-length torsion scale** behind the derived F (1.56 M_Pl) is assumed, not derived. TF-P tests the number;
   the scale still needs a reason.

## Review loop log

| Round | Where | New hits | Outcome |
|---|---|---|---|
| 1 | local results + 4 web searches | 6 | the DES Y5 low-z problem; KMIX; the Bayesian null |
| 2 | 4 primary pages | 3 | truncation numbers; Babu & Amendola tables; KMIX Lagrangian |
| 3 | BI field, Union3.1, fσ8/H(z) | 2 | Union3.1 agreement; Gao et al. already cited |
| 4 | Nieh–Yan F; low-z | 0 | level |
| 5 | BI–SUGRA field space | 1 | Gates–Ketov–Yunes K = −3 ln → λ = −1.633 |
| 6 | α-attractor, axio-dilaton | 2 | λ formula confirmed (2608.19781); solar-system risk (2512.13544) |
| 7 | 2609.22539, 2512.13544 primary pages | 0 | level: no new claim-relevant hits; path set |

## Sources (read this session)

- Zhang 2026, MNRAS 552, stag1868: https://academic.oup.com/mnras/article/552/4/stag1868/8855714
- Huang et al.: https://arxiv.org/abs/2502.04212 ; model predictive scoring: https://arxiv.org/abs/2609.04334
- Bayesian evidence: https://arxiv.org/abs/2511.10631
- SN-Unite: https://arxiv.org/abs/2609.05321 ; Union3.1 hosts: https://arxiv.org/abs/2601.19424
- Babu & Amendola: https://arxiv.org/abs/2610.23497
- Toomey et al. (KMIX): https://arxiv.org/abs/2511.23463
- Argudo-Panes et al.: https://arxiv.org/abs/2609.10133
- Aboubrahim et al.: https://arxiv.org/abs/2511.22559
- Gao et al.: https://arxiv.org/abs/2608.09487 ; https://arxiv.org/abs/2608.19392
- Adshead et al. (Nieh–Yan F enhancement, already cited): https://arxiv.org/abs/2507.10696
- Gates, Ketov & Yunes, PRD 80, 065003 (2009): https://arxiv.org/abs/0906.4978
- Quintessential α-attractors, updated: https://arxiv.org/abs/2608.19781
- Smith, Mylova, van de Bruck, Burgess & Di Valentino: https://arxiv.org/abs/2512.13544
- Ramos-Hamud, García-Arroyo, Quevedo & Vázquez: https://arxiv.org/abs/2609.22539
