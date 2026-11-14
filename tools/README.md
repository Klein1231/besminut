# Lesson tools

- `lib.py` — SVG helpers: `T` text, `TL` left text, `B` box with lines, `A` arrow, `P` elbow arrow, `S` svg wrapper, `F` figure, `CHECK`, `AN` analogy, `PF` pitfall, `LEAD`.
- `sym.py` — IEC-style symbols: contacts (`no_v`, `nc_v`), breaker `breaker_v`, coil, motor, thermal relay, transformer `trafo_v`, generator `gen`, busbar `bus`, meter `meter_v`, ground; P&ID: `valve_h`, `check_h`, `pump_h`, instrument bubble `inst`.
- `render_figures.js` — Playwright: opens the app, walks a lesson and screenshots every figure for visual checks.

SVG classes are themed by the app: `bx bxa soft ln lna dash hd hda t-s t-b mu ac`.
