"""Credit-free checker: applies the locked pre-registered rules to whatever results exist, mechanically, and writes
AUTO_RESULTS.md (+ a phone PDF). No AI involved. Safe to run any time; it only reads results and writes these two files.

Rules (copied from the hashed pre-registrations; see each file for the full wording):
  A1  PREREGISTRATION_PROFILE_F.md     profile in f_EDE on combined data
  A2  PREREGISTRATION_LOOK_ELSEWHERE.md look-elsewhere significance (runs look_elsewhere.py)
  A3  PREREGISTRATION_EARLY_LATE.md     early + late together (AxiCLASS)
  L   PREREGISTRATION_LATE_TWIST.md     the Late Twist (AxiCLASS, halofit references)
Run once:   python auto_judge.py
Hourly:     python auto_judge.py --hourly   (in a terminal tab; Ctrl-C stops it)
"""
import json
import math
import subprocess
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = Path(r"C:\Users\Danny\.copilot\repos\AEGIS\cmb-fit\results")
LCDM, TWIST = 2402.40, 2396.77                     # spa_lcdm, spa_edelock (CAMB, fixed in the pre-registrations)


def load(name):
    f = R / f"cmp_{name}.json"
    return json.load(open(f))["minimum"] if f.exists() else None


def status():
    try:
        s = json.load(open(R / "lanes" / "status.json"))
        run = [k for k, v in s.items() if v.get("status") == "running"]
        failed = [k for k, v in s.items() if v.get("status") == "failed"]
        return run, failed
    except Exception:
        return [], []


def a1():
    fs = ("0.01", "0.02", "0.04", "0.06", "0.08", "0.10", "0.12")
    pts = {float(f): load(f"spa_edelock_fde{f}") for f in fs}
    done = {f: m["chi2"] for f, m in pts.items() if m}
    out = [f"**A1 profile in f** ({len(done)} of 7 points done)"]
    if not done:
        return out
    allp = dict(done)
    allp[0.0] = LCDM
    free = load("spa_edelock")
    cmin = min(list(allp.values()) + [TWIST])
    out.append("| f | χ² − min |")
    out.append("|---|---|")
    for f in sorted(allp):
        out.append(f"| {f:.2f} | {allp[f] - cmin:+.2f} |")
    out.append(f"| free ({free['fde_zc']:.3f}) | {TWIST - cmin:+.2f} |")
    if len(done) < 7:
        out.append("Verdict waits for all 7 points.")
        return out
    grid = sorted(list(allp.items()) + [(free["fde_zc"], TWIST)])
    rise0 = LCDM - cmin

    def crossing(level, side):
        xs, ys = zip(*grid)
        ys = [y - cmin for y in ys]
        imin = ys.index(min(ys))
        rng = range(imin, 0, -1) if side == "lo" else range(imin, len(xs) - 1)
        for i in rng:
            j = i - 1 if side == "lo" else i + 1
            if ys[j] >= level > ys[i] or ys[j] >= level >= ys[i]:
                return xs[i] + (xs[j] - xs[i]) * (level - ys[i]) / (ys[j] - ys[i])
        return None
    for lv, nm in ((1.0, "68%"), (3.84, "95%")):
        lo, hi = crossing(lv, "lo"), crossing(lv, "hi")
        out.append(f"{nm} range: {('%.3f' % lo) if lo is not None else 'below 0 (includes f=0)'} to "
                   f"{('%.3f' % hi) if hi is not None else 'beyond 0.12'}")
    verdict = "PREFERRED" if rise0 > 3.84 else ("NOT PREFERRED" if rise0 < 1 else "MILD")
    out.append(f"Rise at f = 0: {rise0:.2f} (profile significance ~{math.sqrt(max(rise0, 0)):.2f}σ) → "
               f"**early energy {verdict}** (rule: >3.84 preferred, <1 not).")
    better = [f for f, c in done.items() if c < TWIST - 0.5]
    if better:
        out.append(f"Note: profile point(s) {better} beat the free fit by >0.5 (free fit missed its best point).")
    return out


def a2():
    need = [load(f"spa_edelock_th{t}") for t in ("0.5", "1.0", "1.5", "2.0", "2.4", "2.7", "2.9", "3.05")]
    n = sum(m is not None for m in need)
    out = [f"**A2 look-elsewhere** ({n} of 8 fixed-angle fits done)"]
    if n < 8:
        return out
    r = subprocess.run([sys.executable, str(HERE / "look_elsewhere.py")], cwd=HERE, capture_output=True, text=True)
    res = json.load(open(HERE / "LOOK_ELSEWHERE_RESULTS.json"))
    out.append(f"Local: Z = {res['Z_local']:.2f}. Global (conservative): **Z = {res['Z_global_conservative']:.2f} → "
               f"{res['verdict']}** (rule: ≥2 mild evidence, 1–2 weak hint, <1 noise).")
    return out


def a3():
    names = ("ax_spa_lcdm", "ax_spa_w0wa", "ax_spa_edelock", "ax_spa_edelock_w0wa")
    m = {n: load(n) for n in names}
    n = sum(v is not None for v in m.values())
    out = [f"**A3 early + late together** ({n} of 4 AxiCLASS fits done)"]
    if n < 4:
        return out
    D = m["ax_spa_edelock_w0wa"]["chi2"] - m["ax_spa_w0wa"]["chi2"]
    v = "SURVIVES" if (D < -4 and D + 4 < 0) else ("NOT NEEDED" if D >= -1 else "MILD")
    e = m["ax_spa_edelock"]["chi2"] - m["ax_spa_lcdm"]["chi2"]
    w = m["ax_spa_w0wa"]["chi2"] - m["ax_spa_lcdm"]["chi2"]
    ew = m["ax_spa_edelock_w0wa"]
    out.append(f"Adding early energy to late: D = {D:+.2f} → **early {v}** (rule: < −4 survives, ≥ −1 not needed).")
    out.append(f"Cross-check vs CAMB: Twist {e:+.2f} (CAMB −5.63, {'agree' if abs(e + 5.63) <= 1 else 'DIFFER'}); "
               f"w0–wa {w:+.2f} (CAMB −10.89, {'agree' if abs(w + 10.89) <= 1 else 'DIFFER'}).")
    out.append(f"Early+late best fit: f = {ew.get('fraction_axion_ac', float('nan')):.3f}, "
               f"w0 = {ew.get('w0_fld', float('nan')):.2f}, wa = {ew.get('wa_fld', float('nan')):.2f}, "
               f"H₀ = {ew.get('H0', float('nan')):.2f}.")
    return out


def late():
    m = {n: load(n) for n in ("ax_spa_latetwist", "ax_spa_lcdm_halofit", "ax_spa_w0wa_halofit")}
    n = sum(v is not None for v in m.values())
    out = [f"**Late Twist** ({n} of 3 AxiCLASS fits done)"]
    if n < 3:
        return out
    lt = m["ax_spa_latetwist"]
    d = lt["chi2"] - m["ax_spa_lcdm_halofit"]["chi2"]
    D = lt["chi2"] - m["ax_spa_w0wa_halofit"]["chi2"]
    l1 = "PASS" if (d < -4 and d + 4 < 0) else ("FAIL" if d >= 0 else "INCONCLUSIVE")
    l2 = "PREFERRED over w0–wa" if D < -2 else ("AS GOOD AS w0–wa" if D <= 2 else "WORSE than w0–wa")
    F, mm = 10 ** lt.get("log10_F", float("nan")), 10 ** lt.get("log10_m", float("nan"))
    cons = 0.1 <= F <= 3 and 0.5 <= mm <= 10
    incons = F < 0.05 or F > 3 or mm < 0.3 or mm > 30
    l3 = "CONSISTENT" if cons else ("INCONSISTENT" if incons else "not decisive")
    out.append(f"L1 vs ΛCDM: Δχ² = {d:+.2f} → **{l1}**. L2 vs w0–wa: D = {D:+.2f} → **{l2}**. "
               f"L3 natural range: F = {F:.2f} M_Pl, m = {mm:.2f} H₀ → **{l3}**. H₀ = {lt.get('H0', float('nan')):.2f}.")
    return out


def main():
    run, failed = status()
    lines = [f"# Automatic results (no AI): {datetime.now():%Y-%m-%d %H:%M}", "",
             "Mechanical application of the locked rules. Claude reviews and adds plain-language meaning when asked.", "",
             f"**Running now:** {', '.join(run) if run else 'nothing on the CAMB queue'}",
             f"**Failed jobs:** {', '.join(failed) if failed else 'none'}", ""]
    for part in (a1, a2, a3, late):
        try:
            lines += part() + [""]
        except Exception as e:
            lines += [f"(error while judging {part.__name__}: {e})", ""]
    (HERE / "AUTO_RESULTS.md").write_text("\n".join(lines), encoding="utf-8")
    subprocess.run([sys.executable, str(HERE / "make_phone_pdf.py"), "AUTO_RESULTS.md"], cwd=HERE,
                   capture_output=True)
    print("\n".join(lines))


if __name__ == "__main__":
    if "--hourly" in sys.argv:                     # keep running in its own terminal tab; Ctrl-C stops it
        import time
        try:                                       # ask Windows not to idle-sleep while this runs (no settings
            import ctypes                          # changed; released automatically when the tab is stopped)
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)   # ES_CONTINUOUS|SYSTEM_REQUIRED
            print("keeping the PC awake while this tab runs")
        except Exception as e:
            print("could not request keep-awake:", e)
        while True:
            main()
            time.sleep(3600)
    main()
