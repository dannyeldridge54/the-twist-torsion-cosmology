# Deep review, 1 November 2026 (after A3)

This review is written as a sceptical referee would read the work. Every number comes from a result file named in
THESIS.md.

## 1. Where the evidence stands

| Claim | Best number | Honest strength |
|---|---|---|
| Early energy helps on all CMB + DESI + SN | Δχ² −5.98 (profile), −6.05 (AxiCLASS) | Local 2.4σ, **global 1.2–1.4σ** |
| Early energy survives once late DE is allowed (A3) | D = −3.65, AIC +0.35 | **MILD**, close to a tie |
| Late evolving DE (w0–wa) | Δχ² −10.9 (both engines) | ~2.9σ; this is DESI's own known result, not ours |
| Two engines agree | gaps 0.06–0.42 | **Solid** |
| Twist-specific numbers (N = 9, silver, torus N = 7, letters) | all failed or inconclusive | **Retired** |
| Potential n = 3 and the equality lock derived from torsion | not derivable (STEP2, STEP3B) | **Assumed**, not predicted |

**In one line:** the analysis is careful and reproduces the known picture. The data prefer late dynamical dark energy,
and a small early component is a weak extra. Nothing yet singles out *torsion* as the cause.

## 2. Strengths a referee will credit

1. **Pre-registration with hashes,** before every fit, with deviations logged openly. This is rare in the field.
2. **Two Boltzmann engines** that agree to within 0.4.
3. **Losses are printed:** five failed or inconclusive predictions are in the paper.
4. **The results line up with the collaborations:**
   - w0–wa Δχ² ≈ −11 matches DESI DR2;
   - the f_EDE ≈ 0.07 hint at ~2σ matches the ACT and SPT EDE papers.

   This is a strong sign that the pipeline is correct.
5. **The look-elsewhere correction was done.** Most EDE papers skip it.

## 3. Weak spots, from most to least serious

**A. The physics link is the weakest part.** The field is *motivated* by torsion, not derived from it:
- The n = 3 potential is assumed, and natural routes give n = 1.
- The lock at equality is put in by hand.
- So the early model is standard axion-like EDE with one parameter fixed.

A referee will say the data test EDE, not torsion. The paper already says so; keep it that way.

**B. The minimiser is close to the A3 threshold.**
- D = −3.65 against a cut of −4, and each fit used only best of 2.
- Earlier, restarts scattered by ~0.35–0.5 (A1 found a point 0.35 better than the "free" fit).
- **The verdict stands as written.** But a disclosed, post-hoc best-of-4 re-polish of `ax_spa_edelock_w0wa` would show
  whether MILD is stable or sits on the edge of SURVIVES.
- Cost: about 1 hour of CPU, after the Late Twist.

**C. L3 (the "natural range" test) has little power.**
- The prior ranges (F 0.05–3.2 M_Pl, m 0.32–32 H₀) almost coincide with the CONSISTENT and INCONSISTENT bands, so a
  mass outside 0.3–30 H₀ is barely possible.
- The rule also has a gap: F in 0.05–0.1 or m in 0.3–0.5 / 10–30 is neither CONSISTENT nor INCONSISTENT.
- **When judging:** report a best fit at a prior edge as "at the edge" rather than as consistent. Say plainly that
  L3 is a weak test. No rule is changed.

**D. Expect L2 to come out "WORSE".**
- The w0–wa best fit (w0 −0.83, wa −0.64) gives w0 + wa = −1.47, so w crossed below −1 in the past (phantom).
- A thawing field like the Late Twist cannot do that.
- The literature finds thawing quintessence recovers only part of the w0–wa gain (roughly Δχ² −4 to −7 against −11).
- **Plausible outcome:** L1 PASS or INCONCLUSIVE, L2 WORSE, L3 consistent but weak. That would still be a clean,
  honest result: the natural field fits partly, and the phantom-like part of the DESI signal stays unexplained.

**E. Supernova dependence of the late signal.**
- DESI's own w0–wa significance moves from about 2.8σ to 4.2σ depending on the supernova set.
- Our SN swaps (DES Y5, Dovekie, Union3) were run only on the *early* model with Planck alone.
- Running the late and early-plus-late fits with DES-Y5 on the full combination would show whether A3 depends on
  Pantheon+.

**F. Profile versus posterior.**
- Our profile prefers f ≈ 0.08; SPT's posterior gives f < 0.07 at 95%. Both are correct ways to read the data,
  and the paper says so.
- Referees will still ask for posteriors, so the stopped MCMC matters for a journal, though not for arXiv.

**G. Overlapping skies.** Planck, ACT and SPT partly share sky and are treated as independent. This is disclosed. The
effect is small at the χ² level here, but should be named in the limitations.

**H. Minor paper fixes:**
- The abstract says "A joint early-plus-late fit is pre-registered and running": replace it with the A3 result.
- The abstract's "data favour n = 3 over n = 2" should carry the "poorly converged" caveat from STEP2.
- Table rows labelled "P-ACT + Pantheon+" omit DESI DR2, which the runs include. Add it, or state it in the caption.

## 4. What I would change

1. **Reframe the headline:**
   - Old: "torsion-born early dark energy."
   - New: "A pre-registered test of a torsion-motivated axion field in early and late roles."

   The method and the honest null-to-weak result *are* the contribution, and they hold up whatever the Late Twist shows.
2. **Lead with the late role** if L1 passes. It is the role where the twist field's natural shape (n = 1, Planck-scale
   F) fits without extra assumptions.
3. **Keep the early model,** but present it as "a weak hint, MILD alongside late DE", not as the main claim.
4. **Throw out nothing more.** The symbolic number predictions are already retired, and the paper records them as
   failures, which is correct.

## 5. Recommended next steps, in order

1. **Late Twist verdict** (running; hourly check in place).
2. **Paper v3 final:** A3 + Late Twist results, abstract fixes (H), and the L3 power caveat (C).
3. **Optional, disclosed as post-hoc robustness, each about 1–3 hours of CPU:**
   - a best-of-4 re-polish of the A3 early-plus-late fit (B);
   - A3 and the Late Twist with DES-Y5 supernovae (E).
4. **arXiv:** your submission. Then Zenodo v3 on your yes.
5. **Later:** MCMC posteriors for a journal version (F), and a new pre-registered test when DESI DR3 or Simons
   Observatory data arrive. That is the only way the hint becomes real or goes away.

## 6. Bottom line

- **Is the model usable?** Yes, as an honest test case. The pipeline is sound and the results agree with the major
  collaborations.
- **Is the theory "working"?**
  - *Early:* a weak, persistent hint (~1.2–1.4σ global, MILD next to late DE).
  - *Late:* awaiting its verdict.
- **What makes it stronger:** a derivation of the potential or the lock written before new data, or the next data
  releases moving the hint above 3σ.
- **What would retire the early version:** the hint shrinking below 1σ with DESI DR3 or Simons Observatory.
