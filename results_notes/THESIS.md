# The Twist: thesis (version 3)

Danny Lee Eldridge · 1 November 2026

*Offered freely to everyone, especially the people who will build the technologies and crafts to come.*

## 1. The question

The universe is expanding, and we can measure how fast in two ways.

| Method | Expansion rate H₀ |
|---|---|
| Early universe (CMB, standard model) | 67–68 |
| Today, Cepheids (SH0ES) | 73.0–73.2 (2022 baseline 73.04 ± 1.04; JWST-recalibrated ≈ 73.2 ± 0.9) |
| Today, red giants (CCHP) | 70.4 |

The gap is real at the 3–5σ level, but the local measurements disagree with each other. Separately, the newest galaxy
maps (DESI) hint that **dark energy may be changing today**.

## 2. The idea now

**One field, made from spacetime twist.** In Einstein–Cartan gravity, spacetime can twist (torsion) as well as curve.
The Barbero–Immirzi parameter γ of that theory becomes a field: φ = √(3/2) M_Pl · arsinh(1/γ). It is a healthy,
axion-like field. Its range is naturally about the Planck mass, and it is *motivated* by torsion, not derived from it.

That field is tested in two roles:

| Role | Shape | Status |
|---|---|---|
| **Early Twist** (the Locked Twist): a few percent of extra energy whose share **peaks at matter–radiation equality**, then fades | V = Λ⁴[1 − cos(φ/F)]³, assumed | Mild preference in the data; tested all day |
| **Late Twist:** the same kind of field thawing *today* as the dark energy | V = Λ⁴[1 − cos(φ/F)], the natural shape | Pre-registered; its fit runs after A3 |

## 3. What the data say (all rules written and hashed first)

| Test | Result | Verdict |
|---|---|---|
| Planck + DESI + Pantheon+ | Δχ² −4.70 | Rule met |
| Planck + ACT DR6 (blind) | Δχ² −7.23 | Rule met |
| SPT-3G D1 alone, any version | best Δχ² −1.27 | **No meaningful preference** |
| **All three CMB + DESI + Pantheon+** | Δχ² −5.63 (true best near f = 0.08: −5.98) | **PASS**; f ≈ 0.07–0.08, H₀ ≈ 70.2 |
| **Profile in f (A1)** | f = 0 costs 5.98 | **Early energy PREFERRED**; f ≈ 0.05–0.10 (68%) |
| **Look-elsewhere correction (A2)** | Local 2.4σ → **global 1.2–1.4σ** | **A weak hint** (the preference sits only near θ_i ≈ 2.4–3.0) |
| Late evolving dark energy (w0–wa), same data | Δχ² −10.89 | PASS, and **fits better** than the early Twist |
| Early + late together (A3) | Early adds Δχ² −3.65 on top of late (AIC +0.35) | **MILD**: the hint persists (f 0.069) but does not quite pay for its two settings |
| A3 robustness: DES Y5 supernovae (post-hoc) | Early adds −4.70; late gain −20.67 (matches DESI's −21.0) | **SURVIVES with DES Y5**, so **A3 is fragile** across supernova sets |
| A3 with DES-Dovekie (corrected DES, pre-registered bracket) | Early adds −2.70; late gain −14.20 | **MILD**. "Survives" holds only with the uncorrected DES Y5 sample (known 0.04 mag offset) |
| A3 minimiser stability (best of 4) | D = −3.96 | **STABLE (MILD)**, but 0.04 from the SURVIVES line |
| Late Twist (n = 1 field as all dark energy), (F, m) grid | Pantheon+: best +0.96 (≈ −0.4 corrected). DES Y5 (grid + locked edge): best −5.32; look-elsewhere 1.0σ | **Pantheon+: FAIL (a tie once corrected). DES Y5: PASS, but only 1.0σ globally, and NOT CONFIRMED on DES-Dovekie** (+0.18; the DES Y5 best point is +4.27 there). Worse than w0–wa with both SN sets; F at the top of its range. Best fits: w0 ≈ −0.98 / −0.88 |
| Late Twist high-mass corner (sub-Planckian F, large m) | best +38 vs ΛCDM; most points much worse or non-viable | **WORSE**, as explored here (the closure method may not reach near-hilltop starts) |
| Late Twist null mirror (frozen-field Λ limit) | +1.35 against true ΛCDM, where it should be 0; **+0.13 on the fixed build** (pass rule < 0.15) | **Two code bugs found and fixed (B0, validated):** AxiCLASS forces an n = 1 axion into δ_m (meant for axion dark matter), and halofit reads an Ω_m that counts the field as matter. Each fix alone fails; both together pass. On the fixed code a slight thaw beats Λ by about 0.85. The verdicts as written stand; the fixed build is separate and post-hoc |
| Coupled Twist (Late Twist + dark-matter coupling β) | Grid, C5 and β profile complete (as written): best −6.80 vs ΛCDM (≈ −8.2 corrected); abs(β) ≈ 0.05 allowed, 0.1 costs more than 100; the two modes are about equal (−6.07 / −6.93); only β < 0 crosses w = −1 | **C1 PASS, C2 NEEDED, C3 WORSE, C4 CROSSES (negative mode), C5 EXCLUDED** (β = 0.816 is unphysical). Agrees with Babu & Amendola 2026 on the bound, the bimodality and which mode crosses. Corrected-code replication running overnight; it will be the headline |
| Lock from the dynamics (phase-space test) | No saddle at equality; peak moves ×3.5 (×2.9 with coupling) over 100× in Λ⁴ | **NO LOCK**: the lock stays an assumption |
| Pipeline check against DESI DR2 | Late gain −10.95 / −20.67 against DESI's −10.7 / −21.0 | **Matches** within 0.33 |
| Potential power n = 2 instead of 3 | 10.35 worse (poorly converged) | n = 3 favoured |
| Weak lensing (S8) | Penalty depends on the survey | Older DES+KiDS: tie; KiDS-Legacy: fine |
| Two codes (CAMB, AxiCLASS) | Agree within 0.4 | Pass |
| Field stability | Growth ≤ ×20 | No fragmenting |

**The honest summary:**
- Planck and ACT, and all the CMB data combined, prefer a little early energy (about 7–8%): 2.4σ at the best angle,
  but only **about 1.2–1.4σ once the freedom to choose the angle is counted**. That is a weak hint.
- SPT-3G on its own does not see it.
- Late evolving dark energy fits better still.
- H₀ ≈ 70 matches the CCHP red-giant value, not SH0ES.

## 4. What geometry does and does not fix

- **The potential:** cos³ needs two exact cancellations between its harmonics. Neither the twist-topology (Nieh–Yan)
  term nor natural instanton or anomaly potentials give them; they give the plain cosine (n = 1). The data favour
  n = 3, so for the early role the shape remains assumed.
- **The lock:** nothing in the minimal theory knows when equality happens. A small curvature coupling (ξ ≈ 0.1) would
  place the onset near it, at the cost of one more setting. The data rule out a peak *later* than equality but barely
  distinguish equality from earlier.
  - A pre-registered phase-space test confirms it: **no saddle point at equality**, and a dark-matter coupling barely
    helps (LOCK_ATTRACTOR_RESULTS.md).
- **This is why the Late Twist is the promising direction:** for the late role, the natural n = 1 shape and the
  Planck-size range are exactly what is needed (thawing axion dark energy, matching DESI's direction).

## 5. Predictions

| # | Prediction | Status |
|---|---|---|
| P1 | Width = torsion ÷ 9 | **Failed** (SPT-3G) |
| P2 | Starting angle = 1 + √2 | **Failed** |
| P3 | Hebrew-letter Tree: f = 0.0154 | **Inconclusive** |
| P4 / P4b | Width N = 9 / N = 7 from the free fit | **Inconsistent** (SPT-3G prefers N = 24) |
| P5 | Early energy is real | Profile: preferred (f = 0 costs 5.98); after look-elsewhere: **weak hint, ~1.2–1.4σ** |
| P6 | No CMB polarisation rotation from the early field | Open; current hints (0.2–0.34°) about 2.5σ against |
| P6b | No gravitational-wave friction (minimal field) | Consistent so far |
| P8 | Late Twist fits as well as w0–wa, with F and m in their natural range | Free fits stalled; (F, m) grid running |
| P9 | Shared F: one decay constant for both roles | **DIFFERENT** so far (late/early ≈ 7); final on the grid |
| P10 | The Coupled Twist (CDM coupling) reproduces DESI's apparent phantom crossing; torsion-natural β = 0.816 | Built and validated; fits queued (C5 expected EXCLUDED) |

**What would make it strong:**
1. The early hint survives the look-elsewhere correction and the joint early-and-late fit.
2. Or the Late Twist matches w0–wa with a natural F and m.
3. The Simons Observatory and DESI confirm.
4. A derivation of the potential or the lock, written before new data.

**What would retire the early version:** the look-elsewhere significance falls below 1σ, or early energy is not needed
once late dark energy is allowed.

## 6. How it was found (the honest route)

1. **Intuition:** space can twist.
2. **Version 1 failed** (12 bugs; it was the standard model relabelled) and was quarantined.
3. **Version 2** made the twist a real field and fitted it with professional codes.
4. **The lock** was noticed after a free fit, and disclosed as not blind.
5. **Rules before results:** every test hashed first, every loss published, every mistake corrected in the open.
6. **Version 3** (31 Oct to 1 Nov 2026) tested all three telescopes together, ran a profile, checked the potential and
   the lock against geometry, and turned towards the late role.

## 7. The history and art track (kept separate)

These are real mathematics, sky and history, not evidence for the physics:
- **Torus:** the 7 double letters fill a torus exactly; the Tree with Da'at needs one.
- **Taurus:** in the AEGIS Gaia store (192 million stars), the Hyades flow toward a point 0.24° from the published
  value.
- **The Odyssey:** "the Bear never sets" was true of the ancient sky and is false today.
- **Stars in 1D–6D** (678,232 stars within 200 pc):
  - clumpy below 2.5 pc (binaries);
  - smooth from 3 to 100 pc;
  - fractal-like once velocities are added (phase space).

  The shape matches the cosmic pattern; the causes differ.
- **Old books** (OLD_SOURCES_LOG.md): Welling's K7 star, Zahn's optics (mostly right; colour theory pre-Newton), and
  the Tetractys and sacred-geometry claims, checked.
- **Symbol-derived numbers** came out at chance in every test.

## 8. Why it matters

The method is the contribution:
- rules written first and hashed;
- two independent codes;
- every loss printed;
- results that match the major collaborations.

## Records

**Zenodo:** N = 9 prediction 10.5281/zenodo.23838969 · Silver 10.5281/zenodo.23839507 · UFE v2 paper
10.5281/zenodo.23847152.

**Paper v3:** A1, A2 and A3 are in the paper. The Late Twist rerun and the robustness checks are pending. The staged
arXiv bundle (`arxiv_upload/`, 06:46) is out of date and will be rebuilt when they finish.

**Every number** traces to a file in AEGIS `cmb-fit/results` or the CubeMind folder.

## Final results (2 November 2026; supersedes earlier "pending" lines)

**Tiers:** EVIDENCE = measured under locked rules; HYPOTHESIS = the model; MEANING = our reading.

- **Late Twist, on corrected code (EVIDENCE):**
  - Pantheon+: ties ΛCDM (+0.09).
  - DES Y5: −6.23, a weak hint at 1.3σ global, which WEAKENS on DES-Dovekie (−1.33).
  - It always loses to w0–wa.
  - S8 is NEUTRAL.
- **Coupled Twist, on corrected code (EVIDENCE):**
  - −7.91 with β ≈ ±0.05, still WORSE than w0–wa.
  - S8 WORSENS (+0.84σ against DES Y6).
  - The torsion-natural β = 0.816 is EXCLUDED.
- **Birefringence (EVIDENCE):**
  - The minimal field cannot produce the measured angle: EXCLUDED.
  - With one added photon coupling it predicts R = 0.997 (switch-on z ≈ 1.5). OPEN, for LiteBIRD.
- **Spins (EVIDENCE):** b₀ ≈ 10⁻⁴³ GeV, 10¹⁰ below the lab limits. PASS: safe and invisible.
- **Ratio patterns (EVIDENCE):** silver NOT SUPPORTED; golden NOT REPLICATED on new atoms.
- **Bottom line (MEANING):** a carefully tested torsion-motivated field with weak, sample-dependent hints, and one
  clean open prediction (R). It is not a detection. The method (rules first, every loss kept, the two AxiCLASS bugs
  found and fixed) is the most solid contribution.
