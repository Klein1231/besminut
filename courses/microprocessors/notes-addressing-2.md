# Notes: Автоинкрементті, индекстік, салыстырмалы адрестеу (12-дәріс, ЕҰУ) → 7-сабақ

Source: lecture PPTX «12 – Дәріс» (26 slides). Switches: +сызба, +слайд. No +іздеу, no +тексеру.

## Source inconsistencies (handled)
- Slide 4 text is about page addressing, while its figure shows index registers with ±1 and EA=[x]+D. Lesson: page addressing is its own part (10); the figure is used in part 7 (index + auto-inc).
- Slide 22 figure (A_исп = A_к + (R1) + [(R2)]) sits under relative addressing but is a general sum scheme; used in part 14 as the common scheme. СА field and the R2 term are not explained in the lecture: not interpreted.
- Slides 7, 8, 10, 13, 14, 15, 18 pictures (pipeline timing, IPv6/IPv4, B-tree, network classes) are not about the topic: not used.
- Lecture offset convention: target = current command address + offset. Real CPUs usually count from the next command; stated in parts 11–12.

## Added beyond the lecture (flagged as examples)
- Stack push/pop with SP (part 4), SP numbers 300/299/298; stack grows down on many CPUs.
- x86 scale 1/2/4/8 (part 8); MOS 6502 zero page (part 10); SCL FOR loop (part 9).
- Pseudo-assembly listings, 8-bit offset range −128…+127 (part 12), label/assembler (part 13).

## Slide figures (tools/slides-07)
s4-index.jpg (slide 4), s22-sum.jpg (slide 22).
