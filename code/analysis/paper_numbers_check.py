"""Numbers ledger: recompute every key number quoted in the paper (torsion_born_ede.tex, v3) from the fit files, and
check that the paper prints it (to the stated rounding). Exit code 1 if any number disagrees or is missing.
    python paper_numbers_check.py            (works in AEGIS or inside the public repository)"""
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RES = r"C:\Users\Danny\.copilot\repos\AEGIS\cmb-fit\results"
TEX = r"C:\Users\Danny\.copilot\repos\AEGIS\papers\torsion_born_ede.tex"
if not os.path.isdir(RES):                                   # inside the public repository (code/analysis/)
    RES = os.path.join(HERE, "..", "..", "fit_results")
    TEX = os.path.join(HERE, "..", "..", "paper", "torsion_born_ede.tex")
tex = open(TEX, encoding="utf-8").read()
J = {}


def m(name):
    if name not in J:
        J[name] = json.load(open(os.path.join(RES, f"cmp_{name}.json")))["minimum"]
    return J[name]


def d(a, b):
    return m(a)["chi2"] - m(b)["chi2"]


def side(f):
    return json.load(open(os.path.join(RES, f)))


S8 = side("s8_fixed_code.json")
SW = side("b4x_switch.json")
DT = side("b4_delta_theta.json")
LT_P, LT_D = "ax_spa_latetwist_gF0.4m-0.3_nlfix", "ax_spa_latetwist_gF0m0.102_desy5_nlfix"
CPL = "ax_spa_coupledtwist_gF0.4m-0.1_nlfix"
B = lambda b: f"ax_spa_coupledtwist_beta{b}_gF0.4m-0.1_nlfix"

# (label, value, decimals, how the paper prints it as a regex with {v} for the number)
ROWS = [
    ("All CMB: locked onset n=3", d("spa_edelock", "spa_lcdm"), 2, r"{v}"),
    ("All CMB: locked onset n=2", d("spa_edelock_n2", "spa_lcdm"), 2, r"{v}"),
    ("All CMB: w0-wa", d("spa_w0wa", "spa_lcdm"), 2, r"{v}"),
    ("All CMB: H0 (locked n=3)", m("spa_edelock")["H0"], 2, r"{v}"),
    ("All CMB: LCDM chi2", m("spa_lcdm")["chi2"], 2, r"{v}"),
    ("P-ACT blind: locked onset", d("pact_edelock", "pact_lcdm"), 2, r"{v}"),
    ("P-ACT: N = 9 variant", d("pact_edelock_F9", "pact_lcdm"), 2, r"{v}"),
    ("Planck: locked onset", d("edelockP", "lcdmP"), 2, r"{v}"),
    ("SPT-3G: free width best", d("spt_edelock", "spt_lcdm"), 2, r"{v}"),
    ("Late NR Pantheon+", d(LT_P, "ax_spa_lcdm_halofit"), 2, r"{v}"),
    ("Late NR DES Y5", d(LT_D, "ax_spa_lcdm_halofit_desy5"), 2, r"{v}"),
    ("Late NR vs w0-wa Pantheon+", d(LT_P, "ax_spa_w0wa_halofit") + 0, 2, r"{v}"),
    ("Late NR vs w0-wa DES Y5", d(LT_D, "ax_spa_w0wa_halofit_desy5"), 2, r"{v}"),
    ("Coupled NR", d(CPL, "ax_spa_lcdm_halofit"), 2, r"{v}"),
    ("beta = -0.05", d(B(-0.05), "ax_spa_lcdm_halofit"), 2, r"{v}"),
    ("beta = +0.05", d(B(0.05), "ax_spa_lcdm_halofit"), 2, r"{v}"),
    ("beta = 0", d(B(0), "ax_spa_lcdm_halofit"), 2, r"{v}"),
    ("beta = -0.1", d(B(-0.1), "ax_spa_lcdm_halofit"), 0, r"{v}"),
    ("beta = +0.1", d(B(0.1), "ax_spa_lcdm_halofit"), 0, r"{v}"),
    ("S8 Late Pantheon+", S8[LT_P]["S8"], 3, r"{v}"),
    ("S8 Late DES Y5", S8[LT_D]["S8"], 3, r"{v}"),
    ("S8 LCDM Pantheon+", S8["ax_spa_lcdm_halofit"]["S8"], 3, r"{v}"),
    ("S8 Coupled", S8[CPL]["S8"], 3, r"{v}"),
    ("R (switch ratio)", SW[LT_D]["R"], 3, r"{v}"),
    ("dphi Pantheon+ (M_Pl)", abs(DT[LT_P]["F"] * DT[LT_P]["delta_theta"]), 2, r"{v}"),
    ("dphi DES Y5 (M_Pl)", abs(DT[LT_D]["F"] * DT[LT_D]["delta_theta"]), 2, r"{v}"),
]
# Notes, not checks: the w0-wa D values in the text are computed on the halofit references (rank_models.py), and the
# 1.3 sigma global significance comes from rank_models.lee_and_ld() (printed by nr_verdicts.py).

bad = 0
print(f"{'quantity':32s} {'from files':>12s}  in paper?")
for label, v, k, pat in ROWS:
    s = f"{v:+.{k}f}" if label.startswith(("All CMB: locked", "All CMB: w0", "P-ACT", "Planck", "SPT", "Late NR",
                                          "Coupled", "beta")) else f"{v:.{k}f}"
    core = s.lstrip("+")
    sign = "" if not s.startswith(("-", "+")) else ("[-−]" if s.startswith("-") else r"\+?")
    num = re.escape(core.lstrip("-"))
    found = re.search(sign + r"\$?\s*" + num + r"(?![0-9])", tex.replace("$-$", "-")) is not None
    bad += not found
    print(f"{label:32s} {s:>12s}  {'yes' if found else 'NO  <-- check the paper'}")
print(f"\n{len(ROWS)} numbers checked; {bad} not found as printed")
sys.exit(1 if bad else 0)
