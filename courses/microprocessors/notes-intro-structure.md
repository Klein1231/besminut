# Notes: МП тарихы және МП жүйесінің құрылымы (1-дәріс, ЕҰУ, «Жүйелік талдау және басқару» каф.)

Source of truth: lecture PDF «Кіріспе. Микропроцессорлардың даму тарихы. Негізгі ұғымдар» + «Микропроцессорлық жүйенің құрылымы» (29 slides). Split into two lessons: 01-history, 02-structure.

## Facts checked
- ENIAC (1946): 17 468 electron tubes, ~150 kW, ~27 t, ~167 m², ~5000 additions/s; tube failures roughly every 1–2 days after improvements. https://www.computerhistory.org , https://www.guinnessworldrecords.com/world-records/first-general-purpose-electronic-computer , https://heise.de/-11179733
- Transistor: Bell Labs, Dec 1947 (Bardeen, Brattain, Shockley). Transistor computers spread late 1950s. Lecture says «1940–1950 жылдары» — kept as «1947 ойлап табылып, 1950-жылдары» .
- IC: Kilby (Texas Instruments) demonstrated 12 Sep 1958, patent filed 6 Feb 1959; Noyce (Fairchild) silicon planar IC 1959, patent July 1959. Lecture says «1959 жылы TI» — explained as demo 1958, patent 1959. https://www.computerhistory.org/siliconengine/all-semiconductor-solid-circuit-is-demonstrated/ , https://www.britannica.com/biography/Jack-Kilby
- Intel 4004: Nov 1971 public launch (first to Busicom early 1971), 4-bit, ~2300 transistors, 10 µm, max 740 kHz (min clock period 1350 ns), instruction cycle 8 clocks = 10.8 µs, 46 300–92 600 instr/s, 16-pin DIP, 12-bit address (multiplexed over 4-bit bus), separate program/data storage. https://en.wikipedia.org/wiki/Intel_4004 , MPR article https://www.cecs.uci.edu/~papers/mpr/MPR/ARTICLES/101002.pdf
- 8008 (Apr 1972, 8-bit, ~3500 tr.), 8080 (1974, 8-bit, ~4500–6000 tr., 2 MHz), 8086 (1978, 16-bit, 29 000 tr., 5 MHz), 80386 (1985, 32-bit, 275 000 tr.), AMD x86-64 / Opteron, Athlon 64 (2003, 64-bit). https://en.wikipedia.org/wiki/Microprocessor_chronology
- Amdahl: S = 1 / ((1−p) + p/N); max = 1/(1−p). https://diveintosystems.org/book/C14-SharedMemory/performance_basics.html
- ATmega328P (Arduino Uno): 8-bit AVR RISC, modified Harvard, 32 KB flash, 2 KB SRAM, 1 KB EEPROM, 16 MHz on Uno, 32 registers, 10-bit ADC, UART/SPI/I2C. https://en.wikipedia.org/wiki/ATmega328
- Lecture example «Arduino-дағы STM32»: Uno uses ATmega328P; STM32 is in some Arduino boards (Portenta/Giga) and many Arduino-compatible boards → phrase as «Arduino Uno-дағы ATmega328P, STM32».

## Photos
- images/microprocessors/transistor-replica.jpg — File:Replica-of-first-transistor.jpg, public domain (federal employee), Wikimedia Commons
- images/microprocessors/arduino-uno.jpg — File:Arduino Uno - R3.jpg, SparkFun Electronics, CC BY 2.0, Wikimedia Commons
- Lecture images (embedded): АБЖ levels (slide 4), МП block diagram (slide 17), Intel C4004 (slide 9)
- Commons API rate-limited; electron tube photo not obtained.
