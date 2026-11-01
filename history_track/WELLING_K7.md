# Welling's planetary star as K7 on a torus

1 November 2026 · history and art track (exact geometry, not evidence for the physics)

**Source:** Georg von Welling, *Opus Mago-Cabbalisticum et Theosophicum* (1719; 1735 and 1760 editions), plates
53–54. The plates show 7 planets around a star, above the nine angel choirs.

**Picture:** `welling_k7.png`, made by `welling_k7.py`.

## What the drawing shows

1. **Seven planets in Chaldean order** (Saturn, Jupiter, Mars, Sun, Venus, Mercury, Moon) sit on a circle. They are
   joined three ways:
   - the heptagon (7 links);
   - the {7/2} star (7 links);
   - the {7/3} star (7 links).

   Together that is **all 21 pairs: the complete graph K7.** Walking the {7/3} star gives the days of the week in
   order: Saturn, Sun, Moon, Mars, Mercury, Jupiter, Venus.
2. **The same 21 links fit on a flat torus with no crossings.** Each point of a triangular grid gets planet
   (a + 3b) mod 7. Neighbouring points then differ by 1, 3 or 2, so every planet touches all six others. The dashed
   cell is one torus, with its opposite sides glued. The script checks this: 21 distinct edges, period lattice of
   determinant 7.
3. **Rolled up,** this is K7 on a torus, the map whose 7 regions all touch (Heawood's 7-colour bound, Möbius–Császár).

**Letters:** the 7 double letters are matched to the planets using the Golden Dawn attribution (Tav–Saturn, Kaf–Jupiter,
Pe–Mars, Resh–Sun, Dalet–Venus, Bet–Mercury, Gimel–Moon), as in `build_letters_datasheet.py`. Versions of the Sefer
Yetzirah assign them differently, and the geometry holds for any assignment.

## What it means

- **Exact:** any 7 things linked all-to-all fit on a torus but not on a flat page. Welling's star is a flattened view of
  that.
- **Not evidence:** this is true of every set of 7, so it says nothing about the Twist fits.
