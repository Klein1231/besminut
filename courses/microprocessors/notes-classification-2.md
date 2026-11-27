# Notes: Микропроцессорлардың жіктелуі (уақыт және параллелизм, ЕҰУ) → 4-сабақ

Source: lecture PPTX (13 slides). Switches: +сызба, +слайд. No +іздеу, no +тексеру.
Continues 3-сабақ (classification, 8 signs). Slide 3 of this lecture lists a different 6-sign scheme; the lesson only says «лекцияның соңғы екі белгісі».

## Source handling
- Slides 4–6 (cycle, sync vs async, table) → parts 1–4; slide 7 → parts 5–6 (sync types, GALS); slide 8 → part 7 (Flynn, redrawn as SVG: slide cards too small on a phone); slide 9 → parts 8–11 (pipeline + 3 hazards); slide 10 → parts 12–13; slide 11 → parts 14–17; slide 12 → part 18 (chart cropped from slide, `tools/slides-04/s12-amdahl.jpg`); slide 13 → part 19.
- Amdahl formula was taught in 3-сабақ: recalled in one sentence, new content is the three-curve chart and limits.
- Lecture «ағын» is used for both stream (Flynn) and thread (SMT): the lesson says so explicitly in part 7.
- Slide 12 chart values (p = 0,9 → 8,77 at 64 cores, 9,14 at p = 0,95 / 16 cores) match recomputation.

## Added beyond the lecture (flagged in the lesson «Әдебиет»)
- Expansions: DVFS, SSE, AVX, SVE, EPIC, MESI letters; MMX has no official expansion.
- Hazard and deadlock explanations; wait-state example; one-memory structural hazard; simplified forwarding model (result usable after WB); LOAD stall check.
- Out-of-order, register renaming, speculation definitions; coarse/fine-grained definitions; MISD explanation (redundancy); why VLIW has low binary compatibility.
- All numeric examples marked «мысал үшін»; only p = 0,8, N = 4 (2,5) and the chart are from the lecture.
