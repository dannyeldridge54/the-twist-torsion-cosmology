# Next Twist models: feasibility before any fit (2 Nov 2026)

**Numbers:** `next_model_feasibility.py` writes `next_model_feasibility.json`, from stored fits; nothing new was
fitted. **Tier:** every model here is a HYPOTHESIS. Each one gets its predictions locked before any fit.

## 1. Spiral Twist (Danny's radial picture)

- **Idea:** Φ = ρ e^{iθ}, with ρ = F_eff growing from 0.14 M_Pl (early role) to the late value.
- **Cost:** a steady roll over ln(1 + z_c) = 8.2 e-folds needs Ω_ρ ≥ (dρ/dN)²/6.
  - To F = 1.00 (DES Y5): dρ/dN = 0.11, so **Ω_ρ ≥ 0.18%**. That is feasible, comparable to tolerated
    early-energy levels.
  - To F = 2.51 (Pantheon+): dρ/dN = 0.29, so **Ω_ρ ≥ 1.4%**. Probably too large, because it is sustained through
    the matter era.
- **Risk check:** amplified perturbations occur when f *shrinks* (Kobayashi & Takahashi 2016). Here f grows, so that
  risk points the other way.
- **Still unexplained:** why the potential shape changes (n = 3 early, n = 1 late), and why its scale drops from eV to
  meV. One possible route is an instanton action S(ρ) that depends on the radius.
- **Verdict:** possible for a DES-like late field. It needs a radial potential and an explanation for the n and Λ
  changes before it is a model.

## 2. Nieh–Yan-enhanced decay constant (Adshead, Brahma & Das 2026)

- **Formula:** F_eff = f·√(1 + 6M⁴/(M_Pl² f²)) ≈ √6·M²/M_Pl when f ≪ M.
- **Nieh–Yan scale needed:**
  - early F = 0.14: M = 0.24 M_Pl;
  - DES Y5 F = 1.00: M = 0.64 M_Pl;
  - Pantheon+ F = 2.51: M = 1.01 M_Pl.
- **If M = M_Pl:** F_eff = √6 M_Pl = **2.45**, close to the Pantheon+ best fit (2.51).
- **Alternative normalisation:** a period-2π angle with the torsion kinetic term gives √(3/2) M_Pl = **1.22**.
- **Caveat:** whether it is 1.22, 2.45 or something else depends on how the Nieh–Yan index is normalised. Turning the
  Nieh–Yan integral into an integer needs a length scale (Chandía–Zanelli). It is parameter-free only if that scale is
  Planckian.
- **Verdict:** torsion naturally gives F ≈ 1.2–2.4 M_Pl, the range of our late fits (1.0–2.5), but not the early
  role's 0.14. **This is a consistency, not yet a prediction.** It becomes one once the normalisation is derived.

## 3. What following DESI requires

| Our w0–wa fit | Crosses w = −1 at | w(z = 1) | w(z = 2) |
|---|---|---|---|
| DES Y5 | z = 0.45 | −1.12 | −1.22 |
| Pantheon+ | z = 0.37 | −1.12 | −1.20 |
| DES Y5, no DESI | z = 0.42 | −1.14 | −1.26 |

- **What the data prefer:** a past phantom phase (w < −1) that crosses at z ≈ 0.4. A canonical field cannot do this,
  because ρ + p = φ̇² ≥ 0.
- **Route:** a non-canonical kinetic term, plus a Nieh–Yan coupling in teleparallel gravity to remove the perturbation
  instability at the crossing (Kang, Li & Yi 2026). The prediction would be parity-violating gravitational waves; the
  current LIGO bound is 20–45× above the Twist's scale.
- **Post-hoc coincidence (MEANING, not evidence):** the crossing epoch (z ≈ 0.37–0.45) matches the Twist's own
  half-move redshift (z ≈ 0.38). Found after looking, so it is not counted.

## Recommended next pre-registered test (cheap, uses the existing fitter)

**"Torsion-natural F"**:
- **Setup:** fix F at the two declared values √(3/2) and √6 M_Pl, and profile m on DES Y5, Pantheon+ and Union3.
- **Rule:** the two values carry a ×2 look-elsewhere factor. Each is compared with the free-(F, m) grid best and with
  ΛCDM.
- **PASS:** F fixed at a torsion-natural value loses ≤ 1 (Δχ² vs the grid best) and still beats ΛCDM on DES Y5.
- **Cost:** about 6–8 fits (2–3 h on free cores).
- **Why it matters:** it would remove a free parameter from the late model using a derived number. That is the first
  step from "torsion-motivated" toward "torsion-predicted".
