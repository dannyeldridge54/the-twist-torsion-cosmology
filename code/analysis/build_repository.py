"""Assemble the whole Twist programme into ONE local git repository: The_Twist_repository/ (no remote; nothing is
published). Uses the same file selection and safety checks as build_zenodo_v3.py, adds the master README, the claims
index, REPRODUCE, LOCK_TIMES (first commit time of every rule and result in the working repositories), verify.py and
MANIFEST.txt, then commits a snapshot. Rerun after new results; the repository's own history is kept.
    python build_repository.py"""
import hashlib
import os
import shutil
import subprocess

import build_zenodo_v3 as Z

CM, AE = Z.CM, Z.AE
OUT = os.path.join(CM, "The_Twist_repository")
GIT = os.path.join(os.environ["LOCALAPPDATA"], r"github-copilot-git-2.56.0-2\cmd\git.exe")
TOP = {"README.md": "REPOSITORY_README.md", "CLAIMS_INDEX.md": "CLAIMS_INDEX.md", "REPRODUCE.md": "REPOSITORY_REPRODUCE.md", "JOURNEY.md": "REPOSITORY_JOURNEY.md",
       "CITATION.cff": "REPOSITORY_CITATION.cff", "LICENSE": os.path.join(AE, "LICENSE"),
       "LICENSE-ADDENDUM.md": "REPOSITORY_LICENSE_ADDENDUM.md"}

VERIFY = '''"""Check the record: every rule against its .sha256, and every file against MANIFEST.txt.
    python verify.py"""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def sha(path, lf=False):
    data = open(path, "rb").read()
    return hashlib.sha256(data.replace(b"\\r\\n", b"\\n") if lf else data).hexdigest()


bad = 0
pre = os.path.join(HERE, "preregistrations")
for f in sorted(os.listdir(pre)):
    if not f.endswith(".sha256"):
        continue
    want, *name = open(os.path.join(pre, f), encoding="utf-8").read().split()
    target = os.path.join(pre, name[0] if name else f[:-7])
    if not os.path.exists(target):
        target += ".md"
    ok = os.path.exists(target) and want in (sha(target), sha(target, lf=True))
    bad += not ok
    print(("OK   " if ok else "FAIL ") + os.path.basename(target))
n = 0
for line in open(os.path.join(HERE, "MANIFEST.txt"), encoding="utf-8").read().splitlines()[2:]:
    h, size, path = line.split(None, 2)
    n += 1
    if sha(os.path.join(HERE, path)) != h:
        bad += 1
        print("FAIL manifest", path)
print(f"{n} files checked against MANIFEST.txt; problems: {bad}")
'''


def git(repo, *args):
    return subprocess.run([GIT, "-C", repo, *args], capture_output=True, text=True, encoding="utf-8").stdout.strip()


def first_commit(repo, path):
    out = git(repo, "log", "--diff-filter=A", "--follow", "--format=%h %ci", "--", path).splitlines()
    return out[-1] if out else "not committed"


def main():
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):                               # clear the snapshot, keep the repository history
        if f != ".git":
            p = os.path.join(OUT, f)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    rows, flagged, missing, times = [], [], [], []

    def place(src, rel):
        name = os.path.basename(src)
        if not os.path.exists(src):
            missing.append(src); return
        if Z.BLOCK_NAMES.search(name):
            flagged.append((src, "blocked file name")); return
        data = open(src, "rb").read()
        if not name.endswith((".png", ".pdf")):
            txt = data.decode("utf-8", errors="ignore")
            for m in Z.SECRET.finditer(txt):
                flagged.append((src, "secret-like text: " + txt[max(0, m.start() - 60): m.end() + 60].replace("\n", " ")))
        dst = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        rows.append((rel.replace("\\", "/"), len(data), hashlib.sha256(data).hexdigest()))

    for grp, files in Z.GROUPS.items():
        for f in sorted(set(files)):
            sub = grp
            if grp == "code":
                sub = ("code/coupled" if os.sep + "coupled" + os.sep in f else
                       "code/nlfix" if os.sep + "nlfix" + os.sep in f else
                       "code/axiclass" if f.startswith(AE) else "code/analysis")
            place(f, os.path.join(sub, os.path.basename(f)))
            if grp in ("preregistrations", "fit_results") and f.endswith((".md", ".json")):
                repo = CM if f.startswith(CM) else AE
                times.append((grp, os.path.basename(f), first_commit(repo, os.path.relpath(f, repo))))
    for dst, src in TOP.items():
        place(os.path.join(CM, src), dst)
    place(os.path.join(CM, "build_repository.py"), "code/analysis/build_repository.py")
    place(os.path.join(CM, "build_zenodo_v3.py"), "code/analysis/build_zenodo_v3.py")

    with open(os.path.join(OUT, "LOCK_TIMES.md"), "w", encoding="utf-8", newline="\n") as t:
        t.write("# Lock times: when each rule and result first entered version control\n\n"
                "First commit (short hash, time) in the working repositories (CubeMind for rules, AEGIS for results). "
                "A rule's time before its results' times is the evidence for \"rule before result\".\n\n")
        for grp in ("preregistrations", "fit_results"):
            t.write(f"## {grp}\n\n| File | First commit |\n|---|---|\n")
            for g, n, c in sorted(r for r in times if r[0] == grp):
                t.write(f"| {n} | {c} |\n")
            t.write("\n")
    with open(os.path.join(OUT, "verify.py"), "w", encoding="utf-8", newline="\n") as v:
        v.write(VERIFY)
    with open(os.path.join(OUT, ".gitattributes"), "w", newline="\n") as a:
        a.write("* -text\n")                                # byte-exact files, so the hashes always verify
    for extra in ("LOCK_TIMES.md", "verify.py"):
        data = open(os.path.join(OUT, extra), "rb").read()
        rows.append((extra, len(data), hashlib.sha256(data).hexdigest()))
    with open(os.path.join(OUT, "MANIFEST.txt"), "w", encoding="utf-8", newline="\n") as m:
        m.write("The Twist repository (working copy, not published). SHA-256 of every file.\n\n")
        for p, n, h in sorted(rows):
            m.write(f"{h}  {n:>10}  {p}\n")

    if not os.path.isdir(os.path.join(OUT, ".git")):
        git(OUT, "init", "-q", "-b", "main")
    for key in ("user.name", "user.email"):                 # same author identity as the CubeMind repository
        git(OUT, "config", key, git(CM, "config", key))
    git(OUT, "add", "-A")
    git(OUT, "commit", "-q", "-m", "Snapshot of the Twist programme (built by build_repository.py)\n\n"
        "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
    print(f"{len(rows)} files, {sum(n for _, n, _ in rows) / 1e6:.1f} MB in {OUT}")
    print("commit:", git(OUT, "log", "--oneline", "-1"))
    print(f"missing: {len(missing)}")
    for f in missing:
        print("  -", f)
    print(f"flagged: {len(flagged)}")
    for f, why in flagged:
        print("  !", os.path.basename(f), "-", why[:200])


if __name__ == "__main__":
    main()
