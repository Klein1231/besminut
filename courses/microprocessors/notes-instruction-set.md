# Notes: МП команда жүйесі (10-дәріс, ЕҰУ) → 5-сабақ

Source of truth: lecture PPTX «10 – Дәріс. МП команда жүйесі туралы жалпы түсінік» (24 slides). Switches used: +сызба, +слайд. No +іздеу, no +тексеру.

## Source structure / inconsistencies
- Much text sits in SmartArt (diagrams/data1–10.xml); slides 10–12, 15, 19–20 are repeated generic text (fetch–decode–execute, machine language, assembler, RISC/CISC) — merged into single parts.
- Slide 7 groups: data transfer, data processing, control transfer, additional; slide 12 groups: arithmetic, logic, data transfer, control. Lesson follows slide 7/tree (slide 5) and splits «өңдеу» into arithmetic/logic/shift/compare inside part 9.
- Slide 3: «two ways of building an effective command system — next lectures»: not covered, stated in part 1.
- Slide 11 «тікелей адрестеу (дерек нақты көрсетіледі)» = immediate; «жанама (адрес арқылы)» is vague. Lesson: тікелей = immediate, added «тура» (direct) and defined жанама as address-in-cell; indexed explained from name only (lecture gives no detail).
- Tree figure: length given as «сөз ұзындығымен (байт)» — lesson explains word vs byte.

## Added beyond the lecture (flagged in lesson as examples)
- Teaching machine: word 16 bit, КОП 4, address 12, regs 3 bit (as in lesson 4); ADD=0011 invented for the example (3280 HEX).
- Expanding-opcode example (8-bit: 7 + 32 = 39), flag table (200+100, 100+100, 8+9) recomputed by script, loop/interrupt scenarios, 200–203 array, final task.
- AVR facts from general knowledge: SLEEP, SEI, CLC mnemonics; most AVR instructions 16-bit, some 32-bit. Not verified by search.
- Pyramid figure (slide 19) numbers used as given: register 0.2 ns, main memory 80–140 ns, HDD 3–10 ms; 400–700× computed.
