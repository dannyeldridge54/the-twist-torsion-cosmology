"""Find and repair UTF-8 text that was mis-decoded as cp1252 and re-saved ("Î”Ï‡Â²" instead of "Δχ²").
A garbled character is a UTF-8 lead byte shown as Â Ã Î Ï Ð Ñ â ã (cp1252), followed by one or more continuation
bytes 0x80-0xBF shown in cp1252. Detection uses that byte rule, not a fixed list.
    python fix_mojibake.py [--show]   -> report affected files (and lines)
    python fix_mojibake.py --fix      -> repair them line by line (only lines that decode cleanly)"""
import glob
import re
import sys

def _cp(b):
    """cp1252 rendering of one byte; the 5 bytes cp1252 leaves undefined were kept by .NET as U+0081 etc."""
    try:
        return bytes([b]).decode("cp1252")
    except UnicodeDecodeError:
        return chr(b)


CONT = "".join(_cp(b) for b in range(0x80, 0xC0))
LEAD = "".join(_cp(b) for b in range(0xC2, 0xF5))      # every UTF-8 lead byte (Hebrew ×, Arabic Ø/Ù, Greek Î/Ï, ...)
PAT = re.compile(f"[{re.escape(LEAD)}][{re.escape(CONT)}]+")


def _enc(seq):
    out = bytearray()
    for ch in seq:
        try:
            out += ch.encode("cp1252")
        except UnicodeEncodeError:
            out += bytes([ord(ch)])                       # U+0081/8D/8F/90/9D -> the original byte
    return bytes(out)


def count(s):
    return len(PAT.findall(s))


def fix_line(line):
    def repl(m):
        seq = m.group(0)
        try:
            return _enc(seq).decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError, ValueError):
            return seq
    return PAT.sub(repl, line)


if __name__ == "__main__":
    files = sorted(glob.glob("*.md")) + sys.argv[sys.argv.index("--also") + 1:] if "--also" in sys.argv else sorted(glob.glob("*.md"))
    bad = [(f, count(open(f, encoding="utf-8").read())) for f in files]
    bad = [(f, n) for f, n in bad if n]
    for f, n in bad:
        print(f"{f}: {n} garbled sequences")
        if "--show" in sys.argv:
            for i, line in enumerate(open(f, encoding="utf-8").read().splitlines()):
                if PAT.search(line):
                    print(f"   {i + 1}: {', '.join(PAT.findall(line))}")
    if "--fix" in sys.argv:
        for f, _ in bad:
            s = open(f, encoding="utf-8").read()
            r = "\n".join(fix_line(l) for l in s.split("\n"))
            open(f, "w", encoding="utf-8", newline="").write(r)
            print(f"{f}: {count(r)} left after repair")
