# Notes: деректер типтері мен форматтары (2-дәріс, ЕҰУ) → 3-сабақ

Source of truth: lecture PDF «Деректер типтері мен форматтары» (25 slides, text-based; no diagrams worth cropping, all figures drawn as SVG).

## Facts checked
- Ariane 5 flight 501, 4 June 1996: 64-bit float (horizontal bias BH) → 16-bit signed integer conversion overflow (Operand Error) in the inertial reference system; code reused from Ariane 4. ESA/CNES Inquiry Board report (Lions, 19 July 1996). https://en.wikipedia.org/wiki/Ariane_flight_V88 , https://www-users.cse.umn.edu/~arnold/disasters/ariane.html
- Arduino Uno (AVR): int 16-bit; double = float (4 bytes). 32-bit boards (ESP32, Due): int 32-bit, double 64-bit. https://docs.arduino.cc/language-reference/en/variables/data-types/double/ , https://luisllamas.es/en/variable-sizes-in-esp32-arduino-raspberry-pi-windows-and-linux
- DS1307 RTC: time/calendar registers in BCD. Maxim datasheet https://ece-classes.usc.edu/ee459/library/datasheets/DS1307.pdf
- IEEE 754 binary32: 23.5 = 0x41BC0000; float(0.3) = 0.300000011920928955…, neighbours 0.29999998211…, 0.30000004172…; 2^24+1 not representable. Computed with Python/numpy.
- Encoder overflow: 1500 rpm × 1000 imp/rev = 25 000 imp/s; uint16 wraps in 2.62 s; uint32 in ≈ 47.7 h.

## Photos
- Wikimedia Commons returned 429 (rate limit) from the workspace; no photos in this lesson.
