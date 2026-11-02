"""B4 draft numbers: CMB birefringence angle from the Twist field under each coupling reading (T2_PHOTON_COUPLING_LOG.md).

Coupling to fermions (minimal coupling, units 8piG = 1, i.e. reduced Planck units):
  Nieh-Yan form (Mercuri & Taveras 0903.4407 eq. 22):  -(sqrt6/4) dphi . J5            -> c = sqrt6/4
  Holst form (0811.1998 eq. 16, chi = arsinh(gamma)):   (3/4) dchi . J5 / cosh(chi)
                                                       = (sqrt6/4) dphi . J5 / cosh(chi) -> c = sqrt6/(4 cosh chi)
Rotating the coupling away through the chiral anomaly gives L = 4 c S (alpha/2pi) phi F.Ftilde / 4 per field unit, so
  beta_rot = 2 c S (alpha/2pi) dphi,  S = sum N_c Q^2 over the fermions counted (S = 1 is Mercuri & Taveras footnote 5).
Branch E (low-energy EFT; Quevillon & Smith 1903.12559): a pure derivative coupling to a gauge-invariant axial current
gives no physical photon coupling for photons far below the fermion masses, so beta_rot ~ 0.
Delta theta comes from nlfix/delta_theta.py (results/b4_delta_theta.json), field values in reduced Planck units."""
import json
import math

import numpy as np

ALPHA = 1 / 137.035999
K = 2 * (math.sqrt(6) / 4) * ALPHA / (2 * math.pi)        # rad per M_Pl for S = 1, Nieh-Yan form
DEG = 180 / math.pi
RES = "C:/Users/Danny/.copilot/repos/AEGIS/cmb-fit/results/b4_delta_theta.json"
TARGET, SIG = 0.24, 0.06                                   # deg, ACT + Planck (as logged in T2_PHOTON_COUPLING_LOG.md)

d = json.load(open(RES))
print(f"K = {K:.4e} rad/M_Pl = {K * DEG:.4f} deg/M_Pl (S=1);  S=8: {8 * K * DEG:.4f} deg/M_Pl")
print("| Fit | F | theta rec -> today | dphi (M_Pl) | E: EFT | NY S=1 | NY S=8 | Holst S=1 | Holst S=8 |")
print("|---|---|---|---|---|---|---|---|---|")
for run, r in d.items():
    F = r["F"]
    p0, p1 = r["theta_rec"] * F, r["theta_today"] * F
    dphi = p1 - p0
    grid = np.linspace(p0, p1, 2001)
    holst = np.trapezoid(1 / np.cosh(grid / math.sqrt(1.5)), grid)   # chi = phi / sqrt(3/2), field taken as the BI field itself
    ny1, ny8 = K * dphi * DEG, 8 * K * dphi * DEG
    h1, h8 = K * holst * DEG, 8 * K * holst * DEG
    print(f"| {run.replace('ax_spa_latetwist_', '')} | {F:.3f} | {r['theta_rec']:.4f} -> {r['theta_today']:.4f} | {dphi:+.4f} "
          f"| ~0 | {ny1:+.4f} | {ny8:+.4f} | {h1:+.5f} | {h8:+.4f} |")
    for lab, v in (("NY S=8", ny8), ("Holst S=8", h8), ("E", 0.0)):
        print(f"    {lab}: |beta| = {abs(v):.3f} deg -> {(TARGET - abs(v)) / SIG:.1f} sigma below {TARGET}")
need = TARGET / (8 * K * DEG)
print(f"Field change needed for 0.24 deg in the most generous branch (NY, S=8): |dphi| = {need:.3f} M_Pl")
