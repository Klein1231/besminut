# Notes: Адрестеу режимдері (11-дәріс, ЕҰУ) → 6-сабақ

Source of truth: lecture PPTX «11 – Дәріс. Адрестеу режимдері. Түзу адрестеу. Регистрлі адрестеу.» (26 slides). Switches used: +сызба, +слайд. No +іздеу, no +тексеру.

## Source inconsistencies (handled in the lesson)
- «тікелей» is used in two senses: slide 6 (дерек командада) vs slides 7, 13, 14 («тікелей/нақты» = адрес командада; slide 7 calls the data-in-command mode «тұспалды (иммедиатты)»). Course terms: тікелей = immediate, тура = direct (as in lesson 5). Part 2 has a refutation block.
- Slide 18 (STM32 RCC register map) sits under register addressing, but `*((uint32_t*)0x40023830)=0x3;` is direct addressing of a peripheral register. Part 8 says so.
- Slide 20 PLC example calls MW10/MW12 «registers inside the CPU»; in S7 these are bit-memory (merker) words, i.e. memory addressed directly. Not used in the lesson; mention if the lecturer asks.
- Slide 22 Siemens figure: `LAR1 P#I10.0` shows area letter I, while AR1 bits and the result `L MW 210` show merker area. The lesson uses only the 10 + 200 = 210 arithmetic.
- Slides 3, 8, 10, 14 figures (x86 paging, network diagram) are not about the lesson topic: not used.

## Added beyond the lecture (flagged as examples)
- 8080 encoding of MOV B,C = 01 000 001 = 41H (part 9).
- 64 KB → 16-bit address, 3-byte vs 2-byte command; 1 MB → 20 bit (part 6, "мысал үшін").
- 3-clock memory access, 1 MHz timing (part 10, "мысал үшін").
- EQU symbolic names (part 5); relative jump numbers 100+5, 100−3 (part 12).

## Slide figures (tools/slides-06)
s18-address.jpg (slide 18, left part), s7-indirect.jpg (slide 22), s6-base.jpg (slide 6).
