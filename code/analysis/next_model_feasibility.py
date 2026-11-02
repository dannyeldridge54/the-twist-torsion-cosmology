"""Feasibility numbers for the next Twist models (no fitting; reads stored fits). Writes next_model_feasibility.json.
    python next_model_feasibility.py
1. Spiral Twist: a complex field rho e^{i theta} whose radius (the decay constant) grows from the early-role value to
   the late-role value between z_c and today. Minimum kinetic energy fraction of the rolling radius:
   Omega_rho >= (d rho / dN)^2 / 6  (rho in M_Pl, N = ln a), for a steady roll.
2. Nieh-Yan-enhanced F (Adshead, Brahma & Das 2026): F_eff = f sqrt(1 + 6 M^4/(M_Pl^2 f^2)) ~ sqrt6 M^2/M_Pl.
   Nieh-Yan scale M needed for the early and late F values.
3. What DESI's preferred crossing demands: from our own w0-wa best fits, the redshift where w = -1 and how phantom
   w gets at z ~ 1 (which a canonical field cannot do: rho + p = phi_dot^2 >= 0)."""
import json
import math
import os

RES = r"C:\Users\Danny\.copilot\repos\AEGIS\cmb-fit\results"
F_EARLY = 0.14
F_LATE = {"DES Y5 best": 1.00, "Pantheon+ best": 2.51}
Z_C = 3560.0


def spiral():
    n = math.log(1 + Z_C)
    out = {}
    for k, f in F_LATE.items():
        slope = (f - F_EARLY) / n
        out[k] = {"radius change (M_Pl)": f - F_EARLY, "e-folds": n, "d rho/dN": slope,
                  "minimum Omega_rho (steady roll)": slope ** 2 / 6}
    return out


def nieh_yan():
    m = lambda F: math.sqrt(F / math.sqrt(6))          # M/M_Pl from F_eff = sqrt6 M^2/M_Pl
    return {"M for early F = 0.14": m(F_EARLY), **{f"M for {k} F = {v}": m(v) for k, v in F_LATE.items()},
            "F_eff if M = M_Pl": math.sqrt(6), "F if period 2pi with torsion kinetic term (sqrt(3/2))": math.sqrt(1.5)}


def crossing():
    out = {}
    for lab, n in (("DES Y5", "ax_spa_w0wa_halofit_desy5"), ("Pantheon+", "ax_spa_w0wa_halofit"),
                   ("DES Y5, no DESI", "ax_spa_w0wa_halofit_desy5_nobao")):
        p = os.path.join(RES, f"cmp_{n}.json")
        if not os.path.exists(p):
            continue
        m = json.load(open(p))["minimum"]
        w0, wa = m["w0_fld"], m["wa_fld"]
        x = (-1 - w0) / wa                                  # a-fraction 1 - a where w = -1
        zc = x / (1 - x) if 0 < x < 1 else None
        w_at = lambda z: w0 + wa * z / (1 + z)
        out[lab] = {"w0": w0, "wa": wa, "z where w = -1": zc, "w(z=1)": w_at(1.0), "w(z=2)": w_at(2.0),
                    "phantom in the past": w_at(2.0) < -1}
    return out


res = {"spiral": spiral(), "nieh_yan": nieh_yan(), "desi_crossing": crossing()}
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "next_model_feasibility.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
