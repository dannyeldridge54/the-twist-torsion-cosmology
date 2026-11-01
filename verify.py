"""Check the record: every rule against its .sha256, and every file against MANIFEST.txt.
    python verify.py"""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def sha(path, lf=False):
    data = open(path, "rb").read()
    return hashlib.sha256(data.replace(b"\r\n", b"\n") if lf else data).hexdigest()


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
