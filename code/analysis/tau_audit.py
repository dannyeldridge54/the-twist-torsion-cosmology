"""Post-hoc audit (no rule, no verdict): does the optical depth tau drift between each Twist fit and its LCDM reference,
and what does Planck low-l EE charge for it? Prompted by LU (tau 0.0675 vs 0.0613, low-l EE +2.64).
    python tau_audit.py   -> tau_audit.json"""
import json
import os

RES = r"C:\Users\Danny\.copilot\repos\AEGIS\cmb-fit\results"
PAIRS = [("ax_spa_latetwist_gF0.4m-0.3_nlfix", "ax_spa_lcdm_halofit"),
         ("ax_spa_latetwist_gF0m0.102_desy5_nlfix", "ax_spa_lcdm_halofit_desy5"),
         ("ax_spa_latetwist_gF0m0.102_desy5_nlfix_r4", "ax_spa_lcdm_halofit_desy5"),
         ("ax_spa_latetwist_gF0m0.102_desy5_nobao_nlfix", "ax_spa_lcdm_halofit_desy5_nobao"),
         ("ax_spa_latetwist_gF0m0.102_dovekie_nlfix", "ax_spa_lcdm_halofit_dovekie"),
         ("ax_spa_latetwist_gF0m0.102_union3_nlfix", "ax_spa_lcdm_halofit_union3"),
         ("ax_spa_coupledtwist_gF0.4m-0.1_nlfix", "ax_spa_lcdm_halofit"),
         ("ax_spa_coupledtwist_gF0.4m-0.1_nlfix_r4", "ax_spa_lcdm_halofit"),
         ("ax_spa_w0wa_halofit_desy5", "ax_spa_lcdm_halofit_desy5"),
         ("ax_spa_w0wa_halofit_union3", "ax_spa_lcdm_halofit_union3")]
rows = []
for m, ref in PAIRS:
    try:
        a = json.load(open(os.path.join(RES, f"cmp_{m}.json")))["minimum"]
        b = json.load(open(os.path.join(RES, f"cmp_{ref}.json")))["minimum"]
    except FileNotFoundError:
        continue
    ee = "chi2__planck_2018_lowl.EE"
    rows.append({"model": m, "tau": a["tau_reio"], "tau_ref": b["tau_reio"], "dtau": a["tau_reio"] - b["tau_reio"],
                 "dEE": a[ee] - b[ee], "dtotal": a["chi2"] - b["chi2"]})
json.dump(rows, open("tau_audit.json", "w"), indent=1)
print(f"{'model':48s} {'tau':>7s} {'ref':>7s} {'dtau':>8s} {'dEE':>7s} {'dtot':>7s}")
for r in rows:
    print(f"{r['model']:48s} {r['tau']:7.4f} {r['tau_ref']:7.4f} {r['dtau']:+8.4f} {r['dEE']:+7.2f} {r['dtotal']:+7.2f}")
