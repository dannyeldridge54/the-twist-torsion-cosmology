"""Where does each model gain or lose? Per-dataset delta chi2 against its LCDM reference, read straight from the
stored best fits (each cmp_*.json keeps chi2 for every likelihood). No fitting. Writes DATASET_BREAKDOWN.md.
    python dataset_breakdown.py"""
import json
import os

RES = r"C:\Users\Danny\.copilot\repos\AEGIS\cmb-fit\results"
if not os.path.isdir(RES):
    RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "fit_results")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DATASET_BREAKDOWN.md")
SHORT = {"planck_2018_lowl.TT": "Planck low-l TT", "planck_2018_lowl.EE": "Planck low-l EE",
         "act_dr6_cmbonly.PlanckActCut": "Planck high-l (ACT cut)", "act_dr6_cmbonly.ACTDR6CMBonly": "ACT DR6",
         "act_dr6_lenslike.ACTDR6LensLike": "ACT DR6 lensing", "spt3g_d1_tne_lite": "SPT-3G D1",
         "bao.desi_dr2.desi_bao_all": "DESI DR2 BAO", "sn.pantheonplus": "Pantheon+", "sn.desy5": "DES Y5",
         "sn.desdovekie": "DES-Dovekie", "sn.union3": "Union3"}
PAIRS = [("Late Twist, Pantheon+ (corrected)", "ax_spa_latetwist_gF0.4m-0.3_nlfix", "ax_spa_lcdm_halofit"),
         ("Late Twist, DES Y5 (corrected)", "ax_spa_latetwist_gF0m0.102_desy5_nlfix", "ax_spa_lcdm_halofit_desy5"),
         ("Late Twist, DES Y5, no DESI", "ax_spa_latetwist_gF0m0.102_desy5_nobao_nlfix", "ax_spa_lcdm_halofit_desy5_nobao"),
         ("Late Twist, DES-Dovekie (corrected, LD)", "ax_spa_latetwist_gF0m0.102_dovekie_nlfix", "ax_spa_lcdm_halofit_dovekie"),
         ("Late Twist, Union3 (corrected, LU)", "ax_spa_latetwist_gF0m0.102_union3_nlfix", "ax_spa_lcdm_halofit_union3"),
         ("w0-wa, Union3 (context)", "ax_spa_w0wa_halofit_union3", "ax_spa_lcdm_halofit_union3"),
         ("Coupled Twist, Pantheon+ (corrected)", "ax_spa_coupledtwist_gF0.4m-0.1_nlfix", "ax_spa_lcdm_halofit"),
         ("Coupled Twist, no DESI", "ax_spa_coupledtwist_gF0.4m-0.1_nobao_nlfix", "ax_spa_lcdm_halofit_nobao"),
         ("w0-wa, DES Y5 (context)", "ax_spa_w0wa_halofit_desy5", "ax_spa_lcdm_halofit_desy5"),
         ("w0-wa, Pantheon+ (context)", "ax_spa_w0wa_halofit", "ax_spa_lcdm_halofit"),
         ("Early field, all CMB + DESI + Pantheon+ (CAMB)", "spa_edelock", "spa_lcdm")]


def load(n):
    p = os.path.join(RES, f"cmp_{n}.json")
    return json.load(open(p))["minimum"] if os.path.exists(p) else None


lines = ["# Where each model gains and loses: per-dataset delta chi2 vs its LCDM reference", "",
         "Read straight from the stored best fits (`dataset_breakdown.py`); no fitting. Negative means the model "
         "fits that dataset better than LCDM does at their respective best fits. Calibration priors are excluded, so "
         "the per-dataset entries sum to the total delta chi2 within rounding.", "",
         "**Caution (tau_audit.py):** the optical depth tau moves by up to +-0.008 between fits along a near-flat "
         "direction, and Planck low-l EE moves by +-2-3 with it while the total barely changes. Rows that depend on tau "
         "(mainly low-l EE) are not meaningful alone; the totals are.", ""]
summary = {}
for label, m, ref in PAIRS:
    a, b = load(m), load(ref)
    if a is None or b is None:
        lines += [f"## {label}", "", "*missing fit file*", ""]
        continue
    keys = [k for k in a if k.startswith("chi2__") and k[6:] not in ("CMB", "BAO", "SN") and k in b]   # skip group totals
    rows = sorted(((SHORT.get(k[6:], k[6:]), a[k] - b[k]) for k in keys), key=lambda r: r[1])
    total = a["chi2"] - b["chi2"]
    summary[label] = {"total": round(total, 3), "by_dataset": {n: round(v, 3) for n, v in rows}}
    lines += [f"## {label}: total {total:+.2f}", "", "| Dataset | delta chi2 |", "|---|---|"]
    lines += [f"| {n} | {v:+.2f} |" for n, v in rows]
    lines += [f"| *sum* | {sum(v for _, v in rows):+.2f} |", ""]
open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
json.dump(summary, open(OUT.replace(".md", ".json"), "w"), indent=1)
for label, s in summary.items():
    top = list(s["by_dataset"].items())
    print(f"{label}: total {s['total']:+.2f} | best {top[0][0]} {top[0][1]:+.2f} | worst {top[-1][0]} {top[-1][1]:+.2f}")
