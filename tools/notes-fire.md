# АПС research notes (lesson 3)

## Norms
- KZ current: СН РК 2.02-02-2023 and СП РК 2.02-102-2022 «Пожарная автоматика зданий и сооружений» (cited together in 2023+ KZ projects, ecoportal.kz). Earlier: СН РК 2.02-11-2002 (cancelled from 1 Mar 2023, prg.kz); СН РК 2.02-02-2019 (lost force 2023, adilet).
- KZ ТР «Общие требования к пожарной безопасности» (МЧС order 405, 2021) п.62: buildings equipped per list in СН РК 2.02-02-2023 (cdb.kz).
- СТ РК 51089-2003 — ППКП and control panels (adilet).
- RU: СП 484.1311500.2020 (replaced СП 5.13130 from 1 Mar 2021); amendment №1 from 1 Sep 2025.
  - 6.4.1 decision by algorithm A, B or C per ЗКПС. A: one detector, no re-query. B: re-activation of same or another auto detector in same ЗКПС within ≤60 s after re-query. C: second auto detector in same room (same or other ЗКПС).
  - 6.1.5: ≤512 detectors and ≤12 000 m² per ППКП (more with conditions).
  - Radius of control, smoke point: ≤3.5 m height 6.40 m; 3.5–6 → 6.05; 6–10 → 5.70; 10–12 → 5.35. Heat: ≤3.5 → 3.55; 3.5–6 → 3.20; 6–9 → 2.85 (abok.ru).
  - 6.6.27 manual call points on evacuation routes. KZ project: ИПР at 1.5 m height (ecoportal).
- Older table (НПБ 88 / СП 5): smoke ≤3.5 m: ≤85 m², 9.0 m between, 4.5 m to wall; heat ≤3.5 m: ≤25 m², 5.0 / 2.5 m (forum.smeta.ru copy).
- СП 6.13130.2009 п.4.3: backup battery/UPS: 24 h standby + 3 h alarm. п.4.1 fire-resistant copper cables; п.4.6 lines keep working for evacuation time.
- KZ project text: first detector → «Внимание», second detector or manual → «Пожар» (ecoportal 2021-АПС, Сигнал-10П).

## Technology
- Types: threshold (пороговая), address-polling (адресно-опросная), addressable-analog (journal-vniispk).
- Threshold loop: standby detector gives no signal, so normal and fault indistinguishable for detector itself (unitest).
- Ring addressable loop, short-circuit isolators isolate segment; exchange continues (bolid 2025).
- Optical smoke: scattered light, IR emitter + photodiode, baffles/labyrinth; good for smouldering (Apollo, FireClass).
- Heat EN 54-5 A1: static response 54–65 °C; A1R = also rate-of-rise; typical 58 °C (Siemens cert, LST).
- EOL: resistor (threshold) or 47 µF capacitor for some modules (System Sensor M210E).
