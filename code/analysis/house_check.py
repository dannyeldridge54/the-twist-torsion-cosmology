"""House check: the local half of the "scales levelling" checkpoint (run at every milestone, up to 3 passes until
HITS: 0). Read-only. Runs audit_all.py, then adds the checks later passes found necessary:
untracked result files, a stale or dirty paper PDF, the arXiv bundle's age, older hashes kept under other names, and
uncommitted write-ups. Prints FAIL / NOTE lines and a final HITS count (FAIL lines only)."""
import glob
import hashlib
import os
import re
import subprocess
import sys

CM = os.path.dirname(os.path.abspath(__file__))
AE = r"C:\Users\Danny\.copilot\repos\AEGIS"
GIT = os.path.expandvars(r"%LOCALAPPDATA%\github-copilot-git-2.56.0-2\cmd\git.exe")
PY = r"C:\Users\Danny\.copilot\repos\AEGIS\cmb-fit\venv312\Scripts\python.exe"
hits = 0


def fail(msg):
    global hits
    hits += 1
    print("FAIL " + msg)


def git(repo, *args):
    return subprocess.run([GIT, "-C", repo, *args], capture_output=True, text=True).stdout


# 1. The base audit (hashes, key numbers, run health, stale wording).
out = subprocess.run([PY, os.path.join(CM, "audit_all.py")], capture_output=True, text=True).stdout
for line in out.splitlines():
    if line.startswith("FAIL "):
        fail(line[5:])
    elif line.startswith("NOTE") and ("errors in log" in line and "not done" in line and "failed1" not in line):
        print(line)

# 2. Older pre-registrations whose hashes live under other names (verified 1 Nov 2026).
OLD = {"PREREGISTRATION_SPT3G_N9.md": "c400ed9608fd4af2d0dadbd9dd83563d16ffc66ac6ae6485705f126ccff48404",
       "PREREGISTRATION_SPT3G_SILVER.md": "8cd05a4c5314b1f5fd9527ffb21745649ef59c9bec2c7bc080a467cce89db648",
       "PREREGISTRATION_SPT3G_LETTERS.md": "c86f2b752b1a68f3b9db49489e12997b8d42d53ee6d0ce0b24c08afbc67376a2"}
for f, want in OLD.items():
    raw = open(os.path.join(CM, f), "rb").read()
    if want not in {hashlib.sha256(raw).hexdigest(), hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()}:
        fail(f"hash changed: {f}")

# 3. Result files the write-ups depend on must be tracked in git.
untracked = [l[3:] for l in git(AE, "status", "--short", "--untracked-files=all").splitlines()
             if l.startswith("??") and re.search(r"results/(cmp|cpl|earlyF)_.*\.json$", l)]
for u in untracked:
    fail(f"result file not committed: {u}")

# 4. Paper PDF must be newer than its source, and clean.
tex = AE + r"\papers\torsion_born_ede.tex"
pdf = AE + r"\papers\torsion_born_ede.pdf"
if os.path.getmtime(pdf) < os.path.getmtime(tex):
    fail("paper PDF is older than the .tex (rebuild with tectonic)")
try:
    import fitz
    txt = "".join(p.get_text() for p in fitz.open(pdf))
    for pat in (r"\?\?", r"\[pending\]", r"still running", r"is running", r"are running", r"TODO"):
        if re.search(pat, txt):
            fail(f"paper PDF contains '{pat}'")
except ImportError:
    print("NOTE PyMuPDF not available in this Python; PDF text not scanned")

# 5. Uncommitted edits to the main write-ups (fine mid-work, a hit at a checkpoint).
for repo, files in ((CM, ("THESIS.md", "PHONE_SUMMARY.md", "LATE_TWIST_RESULTS.md")),   # MODEL_RANKING.md is generated
                    (AE, ("papers/torsion_born_ede.tex", "papers/torsion_born_ede.pdf"))):
    st = git(repo, "status", "--short", "--", *files)
    for l in st.splitlines():
        fail(f"uncommitted: {l.strip()}")

# 5b. Deviation-log header times must not be later than the commit that first added them (catches hand-typed times).
import datetime as _dt
_devlog = open(os.path.join(CM, "PREREGISTRATION_SPT3G_DEVIATIONS.md"), encoding="utf-8").read()
for line in _devlog.splitlines():
    m = re.match(r"## (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) CT", line)
    if not m:
        continue
    first = git(CM, "log", "--reverse", "--format=%ad", "--date=format:%Y-%m-%d %H:%M:%S", "-S", line.strip(),
                "--", "PREREGISTRATION_SPT3G_DEVIATIONS.md").splitlines()
    if not first:
        continue                                   # not yet committed: checked by item 5 instead
    written = _dt.datetime.strptime(f"{m.group(1)} {m.group(2)}", "%Y-%m-%d %H:%M")
    committed = _dt.datetime.strptime(first[0], "%Y-%m-%d %H:%M:%S")
    if f"header {m.group(2)} corrected" in _devlog:   # a later append-only entry already corrects it
        continue
    if written > committed + _dt.timedelta(minutes=1):
        fail(f"deviation header time {m.group(2)} is after its commit {committed:%H:%M:%S}: {line.strip()[:70]}")

# 5c. Mis-decoded text ("Î”Ï‡Â²" for "Δχ²"): PowerShell 5.1 Get-Content without -Encoding UTF8 garbles files it rewrites.
sys.path.insert(0, CM)
from fix_mojibake import count as moji_count          # byte rule: any UTF-8 lead byte + continuation, as cp1252
for f in glob.glob(os.path.join(CM, "*.md")) + [tex]:
    s = open(f, encoding="utf-8", errors="replace").read()
    n = moji_count(s)
    if n:
        fail(f"garbled text ({n} sequences) in {os.path.basename(f)}; repair with fix_mojibake.py")

# 6. Staged arXiv bundle older than the paper: a note, not a hit (it is rebuilt only before submission).
bundle = os.path.join(CM, "arxiv_upload", "torsion_born_ede_v3_arxiv.tar.gz")
if os.path.exists(bundle) and os.path.getmtime(bundle) < os.path.getmtime(pdf):
    print("NOTE arxiv_upload bundle is older than the paper (rebuild before any submission)")

print(f"HITS: {hits}")
sys.exit(1 if hits else 0)
