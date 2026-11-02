"""Score PREREGISTRATION_ROBUSTNESS_II.md (locked 2026-11-02 12:35:12) exactly as written. Missing runs print as pending.
    python robustness2_score.py"""
import json
import os

RES = r"C:\Users\Danny\.copilot\repos\AEGIS\cmb-fit\results"
if not os.path.isdir(RES):
    RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "fit_results")


def chi2(n):
    p = os.path.join(RES, f"cmp_{n}.json")
    return json.load(open(p))["minimum"]["chi2"] if os.path.exists(p) else None


def diff(a, b):
    x, y = chi2(a), chi2(b)
    return None if x is None or y is None else x - y


B2 = [("Late Twist, DES Y5", "ax_spa_latetwist_gF0m0.102_desy5_nlfix", "ax_spa_lcdm_halofit_desy5",
       "ax_spa_latetwist_gF0m0.102_desy5_nobao_nlfix", "ax_spa_lcdm_halofit_desy5_nobao"),
      ("w0-wa, DES Y5", "ax_spa_w0wa_halofit_desy5", "ax_spa_lcdm_halofit_desy5",
       "ax_spa_w0wa_halofit_desy5_nobao", "ax_spa_lcdm_halofit_desy5_nobao"),
      ("Coupled Twist, Pantheon+", "ax_spa_coupledtwist_gF0.4m-0.1_nlfix", "ax_spa_lcdm_halofit",
       "ax_spa_coupledtwist_gF0.4m-0.1_nobao_nlfix", "ax_spa_lcdm_halofit_nobao"),
      ("w0-wa, Pantheon+", "ax_spa_w0wa_halofit", "ax_spa_lcdm_halofit",
       "ax_spa_w0wa_halofit_nobao", "ax_spa_lcdm_halofit_nobao")]
R3 = [("Late Twist, DES Y5", "ax_spa_latetwist_gF0m0.102_desy5_nlfix", "ax_spa_latetwist_gF0m0.102_desy5_nlfix_r4"),
      ("Coupled Twist", "ax_spa_coupledtwist_gF0.4m-0.1_nlfix", "ax_spa_coupledtwist_gF0.4m-0.1_nlfix_r4")]
out = {"B2": {}, "R3": {}}
print("B2: BAO dissection  (r = gain without DESI / gain with DESI)")
print("| Model | gain with DESI | gain without DESI | r | Verdict |\n|---|---|---|---|---|")
for lab, w, wr, n, nr in B2:
    gw, gn = diff(w, wr), diff(n, nr)
    if gw is None or gn is None:
        print(f"| {lab} | {gw if gw is None else f'{gw:+.2f}'} | pending | | |"); continue
    r = gn / gw
    v = "NOT DESI-DRIVEN" if r >= 0.5 else "PARTLY DESI-DRIVEN" if r > 0 else "DESI-DRIVEN"
    out["B2"][lab] = {"gain_with": gw, "gain_without": gn, "r": r, "verdict": v}
    print(f"| {lab} | {gw:+.2f} | {gn:+.2f} | {r:.2f} | **{v}** |")
print("\nR3: cold restarts  (delta = chi2 cold - chi2 reported)")
print("| Point | reported | cold (best of 4) | delta | Verdict |\n|---|---|---|---|---|")
for lab, rep, cold in R3:
    a, c = chi2(rep), chi2(cold)
    if c is None:
        print(f"| {lab} | {a:.2f} | pending | | |"); continue
    dlt = c - a
    v = "STABLE" if abs(dlt) <= 1.0 else "IMPROVED" if dlt < -1.0 else "COLD-START WORSE"
    out["R3"][lab] = {"reported": a, "cold": c, "delta": dlt, "verdict": v}
    print(f"| {lab} | {a:.2f} | {c:.2f} | {dlt:+.2f} | **{v}** |")
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "robustness2_score.json"), "w"), indent=1)
