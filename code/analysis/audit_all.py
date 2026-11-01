"""Double-check audit: pre-registration hashes, key numbers in the write-ups against the result files, and run health.
Read-only. Prints PASS / FAIL / NOTE lines."""
import glob
import hashlib
import json
import os
import re

CM = os.path.dirname(os.path.abspath(__file__))
AE = r"C:\Users\Danny\.copilot\repos\AEGIS"
RES = AE + r"\cmb-fit\results"
TEX = open(AE + r"\papers\torsion_born_ede.tex", encoding="utf-8").read()
THESIS = open(CM + r"\THESIS.md", encoding="utf-8").read()
PHONE = open(CM + r"\PHONE_SUMMARY.md", encoding="utf-8").read()
bad = 0


def say(ok, msg):
    global bad
    bad += not ok
    print(("PASS " if ok else "FAIL ") + msg)


def chi2(n):
    p = f"{RES}\\cmp_{n}.json"
    return json.load(open(p))["minimum"]["chi2"] if os.path.exists(p) else None


# 1. Pre-registration hashes (git may store CRLF; accept either line ending).
for f in sorted(glob.glob(CM + r"\PREREGISTRATION_*.md")):
    h = f + ".sha256"
    if not os.path.exists(h):
        print(f"NOTE no hash file: {os.path.basename(f)} (deviation logs are append-only, not hashed)")
        continue
    want = open(h).read().split()[0].lower()
    raw = open(f, "rb").read()
    got = {hashlib.sha256(raw).hexdigest(), hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest(),
           hashlib.sha256(raw.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")).hexdigest()}
    say(want in got, f"hash {os.path.basename(f)}")

# 2. Key numbers recomputed from result files, and found in the write-ups.
checks = []
d = chi2("spa_edelock") - chi2("spa_lcdm"); checks.append(("Combined Locked Twist (CAMB)", d, "-5.63"))
d = chi2("spa_w0wa") - chi2("spa_lcdm"); checks.append(("Combined w0-wa (CAMB)", d, "-10.89"))
d = chi2("ax_spa_edelock_w0wa") - chi2("ax_spa_w0wa"); checks.append(("A3 D (AxiCLASS)", d, "-3.65"))
d = chi2("ax_spa_edelock") - chi2("ax_spa_lcdm"); checks.append(("A3 cross-check early", d, "-6.05"))
d = chi2("ax_spa_w0wa") - chi2("ax_spa_lcdm"); checks.append(("A3 cross-check late", d, "-10.95"))
d = chi2("spa_lcdm") - min(chi2(f"spa_edelock_fde{f}") for f in ("0.01", "0.02", "0.04", "0.06", "0.08", "0.10", "0.12"))
checks.append(("A1 rise at f=0 (pre-registered refs rounded to 0.01, see PROFILE_F_RESULTS note)", d, "5.98"))
d = chi2("edelockP_shoes") - chi2("lcdmP_shoes"); checks.append(("SH0ES line in paper", d, "-30.2"))
for name, val, txt in checks:
    say(abs(val - float(txt)) < 0.011 * (10 if txt.count(".") and len(txt.split(".")[1]) == 1 else 1),
        f"{name}: recomputed {val:+.3f} vs written {txt}")
    for doc, body in (("paper", TEX), ("thesis", THESIS)):
        if txt.lstrip("-") not in body:
            print(f"NOTE {name}: '{txt}' not found in {doc}")

# 3. A2 numbers re-derived from the json the calculator wrote.
le = json.load(open(CM + r"\LOOK_ELSEWHERE_RESULTS.json"))
print("NOTE A2 json:", {k: le[k] for k in list(le)[:6]})

# 4. Run health: every lane log with an exception, and every running fit.
for lg in sorted(glob.glob(RES + r"\lanes\ax_*.log")):
    t = open(lg, encoding="utf-8", errors="replace").read()
    n = os.path.basename(lg)[:-4]
    done = os.path.exists(f"{RES}\\cmp_{n}.json")
    err = "Traceback" in t or "Finished unsuccessfully" in t
    print(f"{'NOTE' if err else 'INFO'} {n}: {'done' if done else 'not done'}{', errors in log' if err else ''}")

# 5. Stale "running"/"pending" wording in write-ups.
for doc, body in (("paper", TEX), ("thesis", THESIS), ("phone", PHONE)):
    for m in re.finditer(r"[^\n]{0,60}(running|Running|\[pending\]|Pending)[^\n]{0,40}", body):
        print(f"NOTE {doc}: …{m.group(0).strip()}…")
print("FAILS:", bad)
