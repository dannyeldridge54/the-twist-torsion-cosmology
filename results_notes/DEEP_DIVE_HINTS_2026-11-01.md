# Deep dive for hints, 1 November 2026 (two passes, online and the whole PC)

## The new result first: the Late Twist fit did not converge

The Late Twist finished at 07:41. As written, its verdicts are L1 FAIL (+11.64) and L2 WORSE, but the minimiser
demonstrably did not find the minimum: a point with χ² 11.2 lower exists. See LATE_TWIST_RESULTS.md. A rerun with
better starting points is needed before the Late Twist counts as tested; it needs your OK.

## Online, pass 1

1. **Poulin, Smith, Calderón & Simon 2025** ([arXiv:2505.08051](https://arxiv.org/pdf/2505.08051)):
   - Their EDE profile likelihood on Planck + ACT DR6 + lensing + Pantheon+ + DESI DR2 gives **f_EDE = 0.09 ± 0.03**,
     and they find large prior-volume effects in the Bayesian analyses.
   - **Our A1 profile (f ≈ 0.08, 68% range 0.05–0.10) agrees with an independent group.** It is already cited in the
     paper; the agreement should be stated explicitly.
2. **Wang & Piao 2025** ([arXiv:2511.16606](https://arxiv.org/pdf/2511.16606)):
   - They find EDE + w0–wa improves on w0–wa by Δχ² ≲ −14 **with SH0ES**.
   - Our A3 without SH0ES gives −3.65, the same direction. The gap shows how much of the early signal comes from the
     SH0ES H₀ prior.
3. **Thawing quintessence on DESI DR2** typically gains only Δχ² ≈ −3 to −4 over ΛCDM, against about −10 for w0–wa
   ([2503.14743](https://arxiv.org/pdf/2503.14743), [2504.15190](https://arxiv.org/pdf/2504.15190)).
   - So even a properly converged Late Twist will most likely be INCONCLUSIVE on L1 and WORSE on L2.
4. **Barbero–Immirzi field as dark energy is prior art,** not yet cited:
   - [arXiv:2308.03145](https://arxiv.org/pdf/2308.03145), quintom dark energy from a BI scalar via topological
     invariants;
   - [arXiv:2502.04727](https://arxiv.org/html/2502.04727v1), the Immirzi field as axion-like, with Nieh–Yan;
   - [arXiv:1501.00779](https://arxiv.org/pdf/1501.00779).

   These belong in the paper's introduction.

## Local, pass 1 (CubeMind paper library, 2062 entries; AEGIS results)

5. **Weak gravity conjecture** (library: [2203.05575](http://arxiv.org/abs/2203.05575v1)):
   - Axion EDE needs F < 0.008 M_Pl under the conjecture.
   - **Our F_early = 0.145 M_Pl is about 18 times above that, and the Late Twist F ~ 0.5–3 M_Pl is far above.**
   - This is a real theoretical weakness the paper does not mention. It applies to almost all EDE and axion
     quintessence models, but it must be stated.
6. **Mechanisms for the lock and the two roles already exist in the literature:**
   - "Attractive EDE" ([2309.08082](http://arxiv.org/abs/2309.08082v2)): equality arises as a saddle point, and one
     scalar does both early and late, but their model is disfavoured by data.
   - α-attractors ([2303.15523](http://arxiv.org/abs/2303.15523v1)): one field is trapped, thaws as EDE, then
     slow-rolls as dark energy.
   - Diluting-matter potential ([2507.17095](http://arxiv.org/abs/2507.17095v2)).

   These are the closest published versions of "one field, two roles" and should be cited as such.
7. **The ΛCDM MCMC on P-ACT converged:** R−1 = 0.015, below the pre-set 0.02, giving H₀ = 68.29 ± 0.27
   (`mcmc_peek.py`). That is a finished, unreported result.
   - The early-model chains have not converged (R−1 = 2.9) and cannot be used.
8. **SH0ES runs are finished but not in the paper.** With SH0ES: Locked Twist Δχ² = −30.2, H₀ = 72.2, f = 0.126.
   Expected, since the H₀ prior drives it, but it should be reported as a single line.

## Online, pass 2

9. **DES-Dovekie** recalibration ([arXiv:2511.07517](https://arxiv.org/abs/2511.07517v2)) cut the DES evidence for
   evolving dark energy from 4.2σ to 3.2σ.
   - Our R2 uses the original DES Y5, the version with the *strongest* late signal. Repeating R2 with Dovekie would
     bracket the result.
   - The Dovekie likelihood is installed (`sn.desdovekie`).
10. **The biggest physics hint:** a quintessence field **coupled to dark matter** can make w *appear* to cross −1
    while the field itself never goes phantom.
    - Sources: [2606.21826](https://arxiv.org/pdf/2606.21826) (review), [2606.04886](https://arxiv.org/pdf/2606.04886),
      and arXiv:2604.08449.
    - That is precisely the part of DESI's signal a thawing field cannot fit.
11. **Simons Observatory** has no cosmology results yet; it is in initial science observations. There is no DESI DR3
    date. So the next real data test is still ahead.

## Local, pass 2 (the rest of the PC)

12. **Your own notes already contain the coupled equations** (`Desktop/UFE_MATH_SHEET.md` §6, AEGIS Track 2):
    □φ − V_φ + Σ α_i T_i = 0, with matter T_m = −ρ_m.
    - Combined with hint 10, a **"Late Twist + dark-matter coupling" (one extra parameter α)** is the natural next
      model, and its equations are half-derived on your PC.
    - The same sheet also notes that the *axial-current* (torsion-native) coupling vanishes for conserved charge. So the
      coupling would be conformal, not torsion-specific. Say so plainly.
13. **Old files to leave alone:**
    - `torsion-lambda-toolkit/docs/reports/arxiv/torsion-lambda-arxiv.tex` (v1 era) still has placeholder author
      details (an "[Your Institution]" affiliation and a dummy email address) and v1 claims. It should not be published
      as is.
    - The v1.0.0 PDFs in `AEGIS_private_archive` are quarantined v1 material.
14. **The math sheet's toy check** found θ_i is tuned (only a start offset of 0.36 rad lands f ≈ 0.08). This matches
    the A2 finding that the preference sits only near θ_i ≈ 2.7.

## What to act on (ranked)

1. **Rerun the Late Twist properly** (references at the ΛCDM best fit, best of 4), logged as a deviation, before
   robustness batch 2. Needs your OK.
2. **Paper honesty additions** (no new fits):
   - the weak-gravity-conjecture limitation (5);
   - BI dark-energy prior art (4);
   - the two-role and lock mechanisms (6);
   - the Poulin et al. agreement (1);
   - the SH0ES line (8);
   - the converged ΛCDM MCMC (7).
3. **Add DES-Dovekie to R2** as a further post-hoc bracket (9). That is three to four more fits.
4. **Next model, if you want one:** the Late Twist + dark-matter coupling (10, 12), pre-registered first. It is the only
   route found that could reach DESI's phantom-looking signal with a healthy field.
5. **Keep the trial count honest:** this programme has now run many pre-registered tests. Any new "hit" should be read
   against that number.

## Addendum: online rounds 3–5 (about 08:00, commit bc35930)

- **Coupled axion dark sectors that produce DESI's apparent phantom crossing** (for the next model, not the paper):
  - Khoury, Lin & Trodden ([arXiv:2607.16191](https://arxiv.org/pdf/2607.16191)): dark axion + dark baryon, Δχ² −14.48
    on CMB + DESI DR2 + DES-Dovekie, with a small EDE-like side effect;
  - two-axion coupled quintessence ([arXiv:2608.05032](https://arxiv.org/pdf/2608.05032));
  - axion–dilaton mixing ([arXiv:2511.23463](https://arxiv.org/abs/2511.23463v1)).

  These are the closest published versions of "Late Twist + coupling".
- **Barbero–Immirzi gravitational waves:** [arXiv:2608.19392](https://arxiv.org/pdf/2608.19392) (August 2026), on
  action-level gravitational-wave propagation. Its authors could not be confirmed, so it is not cited.
- **No paper found that applies a look-elsewhere correction to the EDE initial angle.** Our A2 appears uncommon.
- **Fixed-onset EDE prior art** (Murgia et al. 2021, Smith et al. 2021, Herold et al. 2022) and **torsion cosmology
  fitted to DESI** (Liu et al. 2025): now cited in the paper's limitations.
- **H₀:** SH0ES 2022 baseline 73.04 ± 1.04 (the thesis now shows 73.0–73.2); CCHP 70.39 (matches).


## Web deep dive, afternoon (1 November 2026)

**Asked:** "we good anything else? deep dive web for hints". Five angles, plus two follow-ups and two abstract reads.

### H1. Closest prior art for the field identification (must cite)

- **arXiv:2608.09487** (Gao, Wang, Garcia de Andrade et al., Aug 2026): a *dynamical Barbero–Immirzi field* coupled to
  quintessence in Einstein–Cartan–Holst gravity, constrained by gravitational-wave friction.
  - GWTC-3 dark sirens give |ξ_BI| ≲ 0.7 and |ξ_cp| ≲ 0.13 (90%).
  - Einstein Telescope and Cosmic Explorer would improve both by about 20×, translated to γ_dyn ≲ 10⁻¹² and a coupling
    β ≲ 10⁻³.
  - The companion paper is arXiv:2608.19392.
- **Relevance:**
  - It is the same field as our φ = √(3/2) M_Pl arsinh(1/γ).
  - Our P6b ("no GW friction for the minimal field") agrees with their isolated-field case.
  - Their BI–quintessence coupling is a different coupling from our CDM coupling β, so the forecast β is not ours.
- **Also cite:** arXiv:2507.04265 (Einstein–Cartan torsion cosmology fitted to DESI + SNe + CMB; it prefers torsion
  except CMB + DESI + DES Y5).

### H2. The literature's preferred axion corner is outside our grid (possible gap)

- **Lin, Visinelli & Yanagida, arXiv:2504.17638:** with careful initial conditions (near the hilltop), the data prefer a
  **sub-Planckian decay constant and a relatively large mass**. Super-Planckian F stays allowed at slightly higher χ².
- **Shiu, Tonioni & Tran, arXiv:2604.09141:** they derive an analytic (m, f) bound. Adding the quantum-gravity bound
  f < M_Pl pushes the mass ≫ H₀.
- **Our grid:**
  - F ≥ 0.4 M_Pl and m ≤ 2.5 H₀. Everything with m²F² ≲ 1.2 was non-viable.
  - So the corner of sub-Planckian F with large m (m²F² ≫ 1, near the hilltop) **was never tested**.
  - Our "non-viable" points may be a limit of the shooting (closure from a fixed starting-angle range near the hilltop)
    rather than physics. Until shown otherwise, they are labelled **non-viable (possibly code-limited)**.
- **Suggestion (user decision):** pre-register a "high-mass corner" extension, F ∈ {10^-0.6, 10^-0.4, 10^-0.2} M_Pl
  with log10 m up to the prior edge of 1.5. It would be reported separately and would not change the locked grid,
  edge or LEE-G rules.

### H3. Expectation for LD (written before any LD result; not a rule)

- DES-Dovekie cuts the dynamical-dark-energy preference to about 3σ or less. One 2026 EPJC reanalysis finds it drops
  below threshold for most parametrisations, with the drop largest for thawing-type models.
- Together with our own A3 bracket (−20.67 → −14.20), **we expect LD to come out WEAKENED or NOT CONFIRMED.** This
  expectation is recorded so a CONFIRMED result cannot be called foreseen, and a weak one cannot be called a surprise.

### H4. B4 (birefringence) groundwork

- Leads: arXiv:2506.12589 (DESI and cosmic birefringence), arXiv:2606.09994 (pseudo-scalar dark energy), and a 2026
  "joint constraints on birefringence and EDE from ACT, Planck, DESI, Pantheon+".
- Lin et al. report that an O(1) electromagnetic anomaly coefficient is preferred for the quintessence axion.
- For B4, the rotation is β_rot = (c_γ α / 2π) · Δφ / F. Δφ comes from our best Late Twist fit. **The anomaly
  coefficient c_γ must come from the torsion construction**, which is the part to derive and lock.

### H5. B0 (halofit fix) design notes

- Halofit and HMcode are calibrated for ΛCDM. The Takahashi (2012) halofit takes an explicit w₀.
- AxiCLASS's HMcode (`external/HMcode/hmcode.c` line 256) reads the same inflated Ω_m, so switching to HMcode would
  not avoid the artefact.
- The B0 fix should pass halofit a non-field Ω_m **and** the field's own w(z), not w_fld = −1.

**Claim changes:** none. **New candidate step:** H2 (high-mass corner), which is up to the user.

## Review 2026-11-01 15:05: local + web

**Local:**
- 5 runners alive, 8 fits running.
- No non-penalty errors in the last 3 hours.
- LD and HC are waiting by design.
- House check: 0 hits.

**Checked: the early (EDE) results are not affected by the B0 bugs.**
- The forced δ_m flag applies only when n_axion = 1; the Locked Twist uses n = 3.
- The Ω_m inflation scales with Ω_scf at late times, which is negligible for EDE.
- So only the Late Twist and Coupled Twist (n = 1) carry the artefact, as already noted everywhere.

**Web:**
- **Coupled Twist prior art:** Babu & Amendola, arXiv:2610.23497; see COUPLED_TWIST_NOTES.md.
- **Birefringence (for B4):**
  - ACT DR6 + WMAP/Planck: β = 0.264° ± 0.058° (or 0.231° ± 0.059°, depending on the analysis);
  - ACT DR6 alone: about 0.215° ± 0.074° (from a blog; unconfirmed);
  - Planck/WMAP: 0.342° (+0.094 / −0.091);
  - joint ACT + Planck: arXiv:2608.06480;
  - SPT-3G constrains only *anisotropic* birefringence (A_CB < 1.2×10⁻⁴).
  - B4's target window "0.20–0.34°" still holds. Use the joint value when locking B4.
- **Dovekie:** the newest analyses rate thawing as weak-to-moderate evidence with DES-Dovekie, consistent with
  expectation H3 (LD likely WEAKENED or NOT CONFIRMED).
- **The bug:** not reported anywhere public (AxiCLASS has no issue on `include_scf_in_delta_m`), so our finding is
  new. Reporting it is drafted and on hold.

## Dive to exhaustion (2026-11-01 15:08): 5 web rounds, the last with no new claim-relevant hits

| Round | Found | Use |
|---|---|---|
| 1 | Babu & Amendola, arXiv:2610.23497 (coupled cosine thawing, abs(β) < 0.073) | Coupled Twist prior art; supports C5 EXCLUDED (COUPLED_TWIST_NOTES.md) |
| 2 | Coupled-DE claims range from about 2σ (arXiv:2604.12032) to more than 5σ (claims not verified) | Context for C1/C2; do not quote the high claims without the primary papers |
| 2 | Poulin, Smith, Calderón & Simon, arXiv:2505.08051: profile f_EDE = 0.09 ± 0.03 (Planck + ACT DR6 + DESI) | **Independent agreement** with our profile (0.05–0.10); already cited |
| 3 | SPT-3G D1 axion-EDE (Khalife et al., arXiv:2507.23355): f_EDE < 0.070, weak preference | Matches our weak hint; already cited |
| 3 | Immirzi + fermions: Alexandrov arXiv:0802.1221; Freidel, Minic & Takeuchi hep-th/0507253; arXiv:0811.1998; Mercuri gr-qc/0601013 and arXiv:0903.4407 | **T3:** the spin (axial-current) coupling depends on minimal versus non-minimal fermion coupling and can vanish classically. T3 must state its coupling choice first |
| 4 | No published birefringence prediction from the BI field. Thawing-axion birefringence + DESI already exists: arXiv:2504.17638, 2503.18924, 2602.00820. Counter-view: arXiv:2412.05982 (the field goes to zero late) | **B4 novelty is only the torsion-fixed coefficient c_γ.** Cite the generic idea's papers. Address 2412.05982 |
| 5 | Equality-triggered EDE prior art (arXiv:2402.03684, 2303.15523, 2102.06399, 2404.19695) | Already cited (2402.03684, 2303.15523). The companion arXiv:2301.03572 is optional. Citation 2303.15523 verified correct |

**Citations to add with the final paper update:** arXiv:2610.23497, 2604.12032, 2608.09487, 2504.17638, 2604.09141,
2503.18924. For B4 and T3 notes: 0802.1221, hep-th/0507253, 0811.1998, 2412.05982.

**Claim changes:** none. **On track:** yes.

## Scales dive (2026-11-01 15:23): 4 rounds, the last with no new claim-relevant hits

| Round | Found | Use |
|---|---|---|
| 1 | HL3 is customised through official modules; extra terms are not a module. CAL (Corporate Accountability Lab) offers free legal advice on ethical licences, including modifications | Licence now named "HL3-MIL-SV with additional terms"; CAL review added to TODO.md |
| 1 | EU large-enterprise line: 250+ staff, or above €50M turnover (and €43M balance sheet) | Our "Major Corporation" line (250 people / US$50M) matches the standard |
| 2 | firstdonoharm.dev/learn confirms the CAL offer (no litigation) and the naming practice | as above |
| 3 | **Jhaveri, Karwal, Crawford, Hu et al., arXiv:2604.08530 (Apr 2026):** EDE + thawing quintessence with DES-Dovekie as default. EDE alone −9.4 (CMB-BAO); EDE + thawing −12.6; w0–wa −15.8; "EDE remains nearly unaffected" across SN sets | **Required citation and comparison for A3.** Our A3 found the early hint mild and fragile across SN sets (D −3.65 / −2.70 / −4.70). Differences to discuss: thawing vs w0–wa as the late model, data set, and whether EDE is judged by its own Δχ² or by its gain on top of late DE. No rule or verdict changes |
| 3 | arXiv:2604.13535 (multi-field EDE relaxes NPIPE limits); a PRD "phantom mirage" (axion DE just below the Hubble mass mimics phantom) | Context; the phantom-mirage paper is relevant to the Late Twist's m ~ H0. Find its arXiv number before citing |
| 4 | Nothing new (Wang & Piao already cited; Turyshev review 2602.05368 is context) | Dive closed |

**Citations to add (in addition to the earlier list):** arXiv:2604.08530 (required), 2604.13535, and the phantom-mirage
paper.

## Hourly loop dive (2026-11-01 15:37): 2 rounds, the second with no claim-relevant hits

| Round | Found | Use |
|---|---|---|
| 1 | Bhattacharya, Borghetto, Malhotra, Parameswaran, Tasinato & Zavala, arXiv:2410.21243 (JCAP 04 (2025) 086): axion hilltop quintessence vs CMB + LSS + SNe. A search snippet says Pantheon+ prefers f ≳ 1 (f > 0.946) and DES Y5 gives 0.88 (+0.24 / −0.54) | **Consistent with our grid** (the Pantheon+ best sits at the top F edge). Candidate citation; the numbers are from a snippet, so verify them in the PDF before quoting |
| 1 | Payeur, McDonough & Brandenberger, arXiv:2411.13637: the evidence for thawing quintessence disappears with physically motivated priors; also arXiv:2408.17318, "Scant evidence for thawing quintessence" | Context for the L1/LEE-G reading (weak hints); candidate citations |
| 2 | The abstract of 2410.21243 gives no DESI, f or Δχ² numbers | No claim change; dive closed |
