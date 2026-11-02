"""Scales check for the 2 Nov data sheets: recompute every number quoted in the drafts from the fit files and result
JSONs, and confirm the sheet shows the same value (as formatted). No fitting.
    python verify_sheets.py   -> prints PASS/FAIL per number; exit code 1 on any FAIL"""
import json
import os
import sys

RES = r"C:\Users\Danny\.copilot\repos\AEGIS\cmb-fit\results"
HERE = os.path.dirname(os.path.abspath(__file__))


def m(run):
    return json.load(open(os.path.join(RES, f"cmp_{run}.json")))["minimum"]


def j(name):
    return json.load(open(os.path.join(HERE, name)))


def d(a, b, key="chi2"):
    return m(a)[key] - m(b)[key]


def txt(name):
    return open(os.path.join(HERE, name), encoding="utf-8").read()


def fmt(x, nd=2, sign=True):
    s = f"{x:+.{nd}f}" if sign else f"{x:.{nd}f}"
    return s.replace("-", "−")


lz, ssg, lam, tau = j("lowz_split.json"), j("solar_gate.json"), j("bi_kahler_lambda.json"), j("tau_audit.json")
ctx = j("lowz_context_ax_spa_w0wa_halofit_desy5.json")
taus = {r["model"]: r for r in tau}
LT_D, L_D = "ax_spa_latetwist_gF0m0.102_desy5_nlfix", "ax_spa_lcdm_halofit_desy5"
LT_U, L_U, W_U = "ax_spa_latetwist_gF0m0.102_union3_nlfix", "ax_spa_lcdm_halofit_union3", "ax_spa_w0wa_halofit_union3"
CT, L_P = "ax_spa_coupledtwist_gF0.4m-0.1_nlfix", "ax_spa_lcdm_halofit"

CHECKS = [
    # (sheet, expected text, computed value as text)
    ("ROBUSTNESS_II_RESULTS.md", "+0.13", fmt(d(LT_D + "_r4", LT_D))),
    ("ROBUSTNESS_II_RESULTS.md", "+2.37", fmt(d(CT + "_r4", CT))),
    ("ROBUSTNESS_II_RESULTS.md", "−5.54", fmt(d(CT + "_r4", L_P))),
    ("ROBUSTNESS_II_RESULTS.md", "−7.91", fmt(d(CT, L_P))),
    ("ROBUSTNESS_II_RESULTS.md", "2394.35", f"{m(CT)['chi2']:.2f}"),
    ("ROBUSTNESS_II_RESULTS.md", "2396.72", f"{m(CT + '_r4')['chi2']:.2f}"),
    ("LATE_UNION3_RESULTS.md", "−1.82", fmt(d(LT_U, L_U))),
    ("LATE_UNION3_RESULTS.md", "−15.00", fmt(d(W_U, L_U))),
    ("LATE_UNION3_RESULTS.md", "−4.10", fmt(d(LT_U, L_U, "chi2__sn.union3"))),
    ("LATE_UNION3_RESULTS.md", "+2.64", fmt(d(LT_U, L_U, "chi2__planck_2018_lowl.EE"))),
    ("LATE_UNION3_RESULTS.md", "0.0675", f"{m(LT_U)['tau_reio']:.4f}"),
    ("LATE_UNION3_RESULTS.md", "0.0613", f"{m(L_U)['tau_reio']:.4f}"),
    ("LATE_UNION3_RESULTS.md", "+3.15", fmt(taus[LT_D + "_r4"]["dEE"])),
    ("LATE_UNION3_RESULTS.md", "0.0714", f"{taus[LT_D + '_r4']['tau']:.4f}"),
    ("LOWZ_SPLIT_RESULTS.md", "−8.89", fmt(lz["delta_full"])),
    ("LOWZ_SPLIT_RESULTS.md", "+0.53", fmt(lz["delta_high"])),
    ("LOWZ_SPLIT_RESULTS.md", "−0.29", fmt(lz["delta_low"])),
    ("LOWZ_SPLIT_RESULTS.md", "r = −0.06", "r = " + fmt(lz["r"])[0].replace("+", "") + fmt(lz["r"])[1:]),
    ("LOWZ_SPLIT_RESULTS.md", "−11.23", fmt(ctx["delta_full"])),
    ("LOWZ_SPLIT_RESULTS.md", "+1.94", fmt(ctx["delta_high"])),
    ("LOWZ_SPLIT_RESULTS.md", "−0.55", fmt(ctx["delta_low"])),
    ("LOWZ_SPLIT_RESULTS.md", "−0.17", fmt(ctx["r"])),
    ("LOWZ_SPLIT_RESULTS.md", "1639.83993", f"{lz['parts']['twist']['full_recomputed']:.5f}"),
    ("LOWZ_SPLIT_RESULTS.md", "1648.72915", f"{lz['parts']['lcdm']['full_recomputed']:.5f}"),
    ("SOLAR_GATE_RESULTS.md", "0.0072", f"{ssg['gr_points'][0]['allowed_band_dchi']:.4f}"),
    ("SOLAR_GATE_RESULTS.md", "3.39×10⁻³", f"{ssg['cassini_alpha_max'] * 1e3:.2f}×10⁻³"),
    ("SOLAR_GATE_RESULTS.md", "−0.849", fmt(ssg["gr_points"][0]["chi_GR"], 3)),
    ("SOLAR_GATE_RESULTS.md", "0.58 at χ = 0", f"{ssg['far_from_GR_example']['chi=0']:.2f} at χ = 0"),
    ("SOLAR_GATE_RESULTS.md", "−0.35 at χ = −2", fmt(ssg["far_from_GR_example"]["chi=-2"]) + " at χ = −2"),
    ("PATH_DECISION_2026-11-02.md", "−1.633", fmt(lam["lambda"], 3)),
    ("RESULTS_LEDGER_2026-11-02.md", "−5.33", fmt(d(LT_D.replace("_nlfix", "_nobao_nlfix"), "ax_spa_lcdm_halofit_desy5_nobao"))),
    ("RESULTS_LEDGER_2026-11-02.md", "+0.74", fmt(d(CT.replace("_nlfix", "_nobao_nlfix"), "ax_spa_lcdm_halofit_nobao"))),
    ("CLAIMS_INDEX.md", "−6.23", fmt(d(LT_D, L_D))),
]

fails = 0
for sheet, shown, computed in CHECKS:
    ok = shown == computed.replace("+0.0", "+0.0") and shown in txt(sheet)
    if not ok:
        fails += 1
    print(f"{'PASS' if ok else 'FAIL'}  {sheet:30s} shown {shown!r:22s} computed {computed!r}")
print(f"\n{len(CHECKS) - fails}/{len(CHECKS)} pass")
sys.exit(1 if fails else 0)
