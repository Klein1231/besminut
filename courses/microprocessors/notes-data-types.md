# Notes: Деректер типтері мен форматтары (2-дәріс, ЕҰУ) → 2-сабақ

Source of truth: lecture PDF «№2 дәріс» (25 slides, Kazakh). Switches: +сызба, +слайд. No +іздеу, no +тексеру.

## Source quirks (handled)
- Slide 6: «Word — көбіне 16 бит» is processor-dependent; lesson says so and sends the learner to the datasheet.
- Slides 10 and 12 describe two different signed formats: the simple sign-magnitude («тура код») on slide 10, but the ranges −2^(n−1)…2^(n−1)−1 on slide 12 are two's complement. Lesson 2 part 6 explains this and part 7 teaches the two's complement algorithm (slide 13).
- Slide 8 is titled «Сегіздік және он алтылық», but only HEX is shown; one sentence on octal added.
- Slide 15: «кіші сөздің адресі алдымен» — lesson keeps this order, adds that byte/word order differs between processors.
- Slide 21: the rule «тетрада > 9 → +6» misses the half-carry case (8+9). Added as a labelled extension (48+39 = 87).
- Slide numbers in the footer run 02…26 for 25 pages (off by one); ignored.

## Beyond the lecture (labelled in the lesson)
- 8-bit counter 300 → 44 (reused numbers 200+100=44 appear in lesson 10), 32-bit ms timer wraps after ≈49.7 days.
- `0.1 + 0.2 == 0.3` is False in Python (0.30000000000000004), run in this session.
- Arduino Uno int = 16 bit, ESP32 int = 32 bit.
- Bit-packing 8 flags into one byte (one sentence).

## Numbers
All numbers recomputed with asserts in tools/make-microprocessors-02.py.

## Slides cropped (tools/slides-02)
tree (slide 5), units (6), sign (10), bcd (20), ascii (22).
