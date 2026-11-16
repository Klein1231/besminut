# Notes: командалар форматы (9-дәріс, ЕҰУ) → 4-сабақ

Source of truth: lecture PPTX «9 – Дәріс. Командалар форматы» (25 slides). Much text sits in SmartArt (extracted from ppt/diagrams/data*.xml). No `+слайд`, `+сызба`, `+іздеу` used.

## Facts and checks
- Lecture example: КОП 4 bit (16 operations), address 12 bit (4 Кбайт) → "40 bit" = 4 + 3·12 (two operands + result). With the next-command address: 4 + 4·12 = 52 (added in lesson).
- Reduction methods (slides 7/11, data3): PC; result address = one source address; implicit addressing of source/destination (accumulator, one-address, ADD B); register address instead of full memory address (ЖБР). All shorten the format and complicate programming.
- Slide 8: PC pros/cons (needs jump/skip/conditional commands).
- Second half (slides 12–23) is about command-line (OS) commands: name, parameters, arguments; classification by structure / function / domain; properties (standard, flexible, readable, safe). Lesson treats it as the second meaning of "command".

## Source inconsistencies
- Slide 7 header speaks about the execution cycle, but its picture is the list of format-reduction methods. Lesson uses the cycle from lesson 1 (алу, декодтау, орындау, сақтау).
- Slide 14 review Q1 (functional classification of the command system): lecture gives no machine-command list; the lesson's table (data transfer, arithmetic, logic/shift, control transfer, I/O, processor control) is a general textbook grouping, flagged as added.
- Slide 11 typo «аккцмцляторға», «жажыға» in the source; lesson uses correct spelling.

## Lesson-only examples (not from the lecture)
- S = A+B+C+D comparison (120 vs 80 bit; 30 bit with registers), break-even n ≥ 3; register field 3 bit for 8 registers. Labelled as teaching examples. All numbers asserted in tools/make-microprocessors-04.py.
