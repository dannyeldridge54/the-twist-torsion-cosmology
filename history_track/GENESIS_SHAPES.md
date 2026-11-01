# Genesis 1:1 on the 13/10 clock and the Tree of Life

31 October 2026. Code: `genesis_shapes.py`. Output: `genesis_shapes.json`, `genesis_shapes.png`.

**The verse:** בראשית ברא אלהים את השמים ואת הארץ. It has 28 letters; the final forms ם and ץ are counted as מ and צ.

## The rules (written in the code before it ran)

- **Wraps, like Stan Tenen's bead chain:**
  - The 28 letters are written in rows of width w, closed into a ring.
  - The score is how many times the same letter sits directly above itself.
  - The clock widths 13 and 10 were named in advance. Each needs p < 0.025 against 100,000 shuffles of the same 28
    letters.
  - The best width overall, from 2 to 14, is judged against the best width of each shuffle, to allow for having
    tried many widths.
- **The Tree walk:**
  - Each letter is its Tree path (Golden Dawn attribution).
  - The score is how many consecutive letters have paths that meet at a sefirah, counted around the closed verse.
  - The same 100,000 shuffles give the baseline.
- **Gematria** is reported as a fact and was not tested.

## Results

| Test | Score | Chance (p) | Beyond chance? |
|---|---|---|---|
| **13 wide** (the clock's 13) | 3 same-letter stacks | 0.43 | No |
| **10 wide** (the 10 sefirot) | 2 stacks | 0.71 | No |
| Best of all widths (w = 8) | 5 stacks | 0.71 after look-elsewhere | No |
| **Walk on the Tree** | 7 of 28 steps join | 0.92 | No (slightly *fewer* joins than chance) |

**How often the verse visits each sefirah** (each letter visits the two ends of its path):

| Sefirah | Visits |
|---|---|
| Chokhmah | 10 |
| Keter, Hod | 8 each |
| Tiferet, Yesod | 7 each |
| Malkhut | 5 |
| Chesed, Gevurah | 4 each |
| Binah | 2 |
| Netzach | 1 |

This just follows from which letters the verse uses most: Aleph (6×), Tav (4×), Resh (3×) and others.

**Gematria:**
- 2701 = 37 × 73, which is also the 73rd triangular number.
- This is a long-known observation about this verse. With many possible ways to factor and arrange numbers, it is not
  a test.

## What it means

The shapes are real: the picture shows exactly how the verse stacks on 13 and 10 columns and where it walks on the
Tree. But none of them is beyond chance. A random shuffle of the same 28 letters makes similar stacks and similar walks
just as often.

So Tenen's "matching letters line up" effect does not appear in these tests, at the widths that matter to the
framework (13 and 10) or at any width up to 14. This does not test his three-dimensional vortex-shadow claim, which
needs a precise, testable statement of which shadow gives which letter before it can be checked.

Nothing here changes the physics. None of it is a prediction.
