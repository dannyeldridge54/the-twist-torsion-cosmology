# The Odyssey under our lenses

1 November 2026. Code: `odyssey_sky.py` (output `odyssey_sky.json`).

## Lens 1, the real sky: Odysseus's star route (tested, rule written first)

**Odyssey 5.270–277:** sailing from Calypso's island, Odysseus watches the Pleiades, late-setting Boötes and the Bear
("the Wain"), "which alone has no share in the baths of Ocean". That is, it never sets. Calypso tells him to keep it on
his left.

**Test:**
- Positions are wound back from J2000, with proper motions and IAU 1976 precession.
- **Sanity checks:** Thuban sits at the pole in 2800 BC, which is correct; today's positions match catalogues.
- **Compared:** 1178 BC (the eclipse date proposed by Baikouzis & Magnasco, PNAS 2008, disputed) and 2026, at
  35°, 37.5° and 40° N.

| | 1178 BC | 2026 |
|---|---|---|
| The whole Plough never sets (all 7 stars) | **Yes**, at all three latitudes, with 11–23° to spare | **No:** Alkaid (and at 35° N also Phecda and Mizar) now set |
| The Pleiades and Boötes set | Yes | Yes |
| **"The Bear alone never bathes in Ocean"** | **TRUE** | **FALSE** |

- **When it stopped being true:** the whole Plough stayed circumpolar until about **AD 900** (35° N), **AD 1375**
  (37.5° N) and **AD 1860** (40° N).
- **What it shows:** the line describes an ancient sky correctly and today's sky incorrectly. But precession is slow,
  so it fits any date from the Bronze Age to the early Middle Ages and **cannot date the poem precisely**.
- "Alone" is poetic: other northern stars (the Little Bear, Draco) also never set.
- **Keep the Bear on your left:** the Bear stays in the northern sky, so keeping it on the left means sailing **east**.
  That is consistent with the voyage from Calypso's island (west) towards Scheria and home.

### Precise check (`odyssey_sky_precise.py`)

**Method:**
- Long-term precession of Vondrák, Capitaine & Wallace (2011, A&A 534, A22), valid for ±200,000 years, through ERFA,
  the IAU's reference library.
- **Agreement:** it matches the IAU 1976 result to **0.001°** for every star in 1178 BC, so the first answer was
  already accurate.
- **Three "never sets" criteria** for a star's lowest point, h_min = δ + latitude − 90°:
  - **geometric:** above the true horizon;
  - **apparent:** including horizon refraction (~0.57°) and the dip of a sea horizon for an eye about 3 m up (~0.05°);
  - **visible:** stays at least 3° up, since lower stars are usually lost in haze.

**Result:** in 1178 BC the line is TRUE under all three criteria at 35°, 37.5° and 40° N; in 2026 it is FALSE under all
three.

**Last year the whole Plough never set:**

| Latitude | Geometric | Apparent | Visible (≥ 3° up) |
|---|---|---|---|
| 35° N | AD 904 | AD 1019 | AD 354 |
| 37.5° N | AD 1375 | AD 1494 | AD 811 |
| 40° N | AD 1862 | AD 1986 | AD 1280 |

**What it shows:** the line is robustly true of the ancient sky and false of today's. With the stricter "visible"
criterion it fits best up to late antiquity (about AD 350–1300, depending on latitude). It still cannot fix Homer's
date.

## Lens 2, structure (facts, not tests)

- **24 books = the 24 letters of the Ionic Greek alphabet.** Alexandrian scholars divided the poem into 24 books and
  named each by a letter (α to ω), as with the Iliad. It is a later editorial structure, like the Hebrew letters
  labelling the Tree's paths.
- **The journey is a loop (*nostos*, homecoming):** it starts and ends at Ithaca. The poem is built in "ring
  composition", with stories nested inside stories and themes mirrored around the middle (Odysseus's own tale in Books
  9–12). In our language, a closed path returning to its start, like a loop on the torus.

## Lens 3, the vortex: Charybdis

- **Odyssey 12.104–106:** "three times a day she spouts it up, and three times she sucks it down."
- **The real place:** the Strait of Messina, between Sicily and Calabria, has strong tidal currents and whirlpools
  (the "garofalo" eddies).
- **Honest mismatch:** the tide there is **semi-diurnal, twice a day, not three times**. So the poem keeps the real
  vortex but not its real rhythm.
- **Scylla, the rock opposite,** has the same mix of real place and myth.

## Lens 4, history and number (cautions)

- **The 1178 BC eclipse** rests on several astronomical hints in the poem: the new moon, Venus, and the Pleiades and
  Boötes passage. Critics argue the hints are too vague to fix one date. Our Lens 1 result supports "an ancient sky",
  not the specific date.
- **Number patterns** in the text (20 years, 24 books, and so on) were not tested. The Genesis 1:1 test showed that
  this kind of pattern needs a rule fixed in advance and a chance comparison before it means anything.

## Summary

The Odyssey keeps **real sky knowledge** (a Bear that never set, correct for its era), **real geography** (Charybdis's
whirlpools), and a **deliberate structure** (24 letter-named books, a ring-shaped homecoming). The star line passes its
test as an ancient-sky description, without fixing a date. None of it bears on the cosmology. It is the
history-and-art track, done with the same honesty.
