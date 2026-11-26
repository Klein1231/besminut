# Python — оқу картасы

Материал тілі: барлығы ағылшынша (CS50P, ATBS, ресми Tutorial). Уақыт — шамамен. Тарау/апта атаулары осы сессияда сайттардан расталған.

## 1-кезең. Бағдарлама жазу негізі: функция, шарт, цикл (шамамен 2–3 апта)

### Айнымалы, функция, аргумент, return
- Негізгі: CS50P (Harvard, English), Week 0 «Functions, Variables». Қосымша: ATBS 3-басылым, Chapter 1 «Python Basics», Chapter 4 «Functions» (Automate the Boring Stuff, Al Sweigart, English).
- Практика: Week 0 бетіндегі Problem Set 0 (бетте бар екені расталды, есептердің атауын өзің ашып қара); ATBS тарау соңындағы practice questions (жауаптары Appendix B-де).
- түсінбесең: besminut-teacher: функция, аргумент пен return

### Шарттар: if / elif / else
- Негізгі: CS50P (Harvard, English), Week 1 «Conditionals». Қосымша: ATBS Chapter 2 «if-else and Flow Control».
- Практика: Week 1 бетіндегі Problem Set.

### Циклдер: while / for
- Негізгі: CS50P (Harvard, English), Week 2 «Loops». Қосымша: ATBS Chapter 3 «Loops»; ресми Tutorial §4.2–4.4 (for, range(), break/continue).
- Практика: Week 2 бетіндегі Problem Set.
- түсінбесең: besminut-teacher: for мен while циклі, қашан қайсысы

Дайын болу критерийі:
- [ ] Python-ды компьютеріңе орнатып, VS Code-та бағдарлама іске қостың (Week 0 «Visual Studio Code for CS50» қысқа бейнесі бар)
- [ ] Санды сұрап, шарт бойынша жауап беретін 10 жолдық бағдарлама өзің жаздың
- [ ] Problem Set 0–2 тесттен өтті, шешімді көшірмей жаздың

**Жоба: сұраққа «екі шарт» пен цикл қолданатын консольдік «санды тап» ойыны (өз брифім: ойыншы 1–100 санын болжайды, бағдарлама «үлкен/кіші» дейді, талпыныс санын санайды).**

## 2-кезең. Мәліметтер құрылымдары: тізім, сөздік, жол (шамамен 2 апта)

### Тізім мен сөздік
- Негізгі: ATBS Chapter 6 «Lists», Chapter 7 «Dictionaries and Structuring Data». Қосымша: ресми Tutorial §5 «Data Structures» (5.1 тізім, 5.4 set, 5.5 сөздік, 5.1.3 list comprehensions).
- Практика: ATBS тарау соңындағы practice questions (Appendix B-де жауабы).
- түсінбесең: besminut-teacher: тізім мен сөздік, қайсысын қашан алу

### Жолдармен жұмыс
- Негізгі: ATBS Chapter 8 «Strings and Text Editing». Қосымша: ресми Tutorial §7.1 «Fancier output formatting» (f-string).
- Практика: ATBS Chapter 8 practice questions.

Дайын болу критерийі:
- [ ] Сөздікте сөз санын санайтын бағдарлама жаздың
- [ ] List comprehension мен әдеттегі for-цикл екеуін де жаза аласың
- [ ] Тізім мен сөздіктің айырмасын мысалмен түсіндіре аласың

**Жоба: мәтіндегі сөздердің жиілігін санайтын бағдарлама (өз брифім: .txt файл ал, ең жиі 10 сөзді шығар).**

## 3-кезең. Қателер, файлдар, тест, regex (шамамен 3 апта)

### Қателерді өңдеу және іздеу
- Негізгі: CS50P (Harvard, English), Week 3 «Exceptions». Қосымша: ATBS Chapter 5 «Debugging»; ресми Tutorial §8 «Errors and Exceptions».
- Практика: Week 3 бетіндегі Problem Set.
- түсінбесең: besminut-teacher: try/except, қате қашан көтеріледі

### Файлмен жұмыс
- Негізгі: CS50P (Harvard, English), Week 6 «File I/O». Қосымша: ATBS Chapter 10 «Reading and Writing Files»; ресми Tutorial §7.2 (оның ішінде json).
- Практика: Week 6 бетіндегі Problem Set.

### Unit тесттер (pytest)
- Негізгі: CS50P (Harvard, English), Week 5 «Unit Tests».
- Практика: Week 5 бетіндегі Problem Set.
- түсінбесең: besminut-teacher: pytest, тест жазу

### Регулярлы өрнектер
- Негізгі: CS50P (Harvard, English), Week 7 «Regular Expressions». Қосымша: ATBS Chapter 9 «Text Pattern Matching with Regular Expressions».
- Практика: Week 7 бетіндегі Problem Set.
- түсінбесең: besminut-teacher: regex

Дайын болу критерийі:
- [ ] Қате шыққанда бағдарлама құламай, түсінікті хабар береді
- [ ] Файлдан оқып, файлға жаза аласың
- [ ] Өз функцияңа pytest-пен 3 тест жаздың

**Жоба: email/телефон тексеретін шағын утилита (өз брифім: файлдағы жолдарды regex-пен тексеріп, дұрыс/бұрыс тізімін екі файлға жаз, тест жаз).**

## 4-кезең. Кітапханалар, модульдер, виртуал орта (шамамен 1 апта)

### Сырттан кітапхана қосу
- Негізгі: CS50P (Harvard, English), Week 4 «Libraries». Қосымша: ATBS Appendix A «Installing Third-Party Packages»; ресми Tutorial §6 «Modules» және §12 «Virtual Environments and Packages».
- Практика: Week 4 бетіндегі Problem Set.
- түсінбесең: besminut-teacher: venv пен pip

Дайын болу критерийі:
- [ ] Әр жобаға бөлек виртуал орта құрдың
- [ ] pip-пен кітапхана орнатып, requirements.txt жаздың

## 5-кезең. Классты түсіну: OOP (шамамен 2 апта)

### Класс, объект, әдіс, мұрагерлік
- Негізгі: CS50P (Harvard, English), Week 8 «Object-Oriented Programming». Қосымша: ресми Tutorial §9 «Classes» (9.3 классқа кіріспе, 9.5 Inheritance, 9.8 Iterators, 9.9 Generators).
- Практика: Week 8 бетіндегі Problem Set.
- түсінбесең: besminut-teacher: класс пен объект, self

Дайын болу критерийі:
- [ ] Өз класыңды жазып, одан 2 объект жасадың
- [ ] Мұрагерлікті қолданған мысал жаздың

## 6-кезең. Нақты жобалар: автоматтандыру және деректер (шамамен 3–4 апта)

### Командалық жол, веб-скрейпинг, SQLite, CSV/JSON
- Негізгі: ATBS Chapter 12 «Designing and Deploying Command Line Programs», Chapter 13 «Web Scraping», Chapter 16 «SQLite Databases», Chapter 18 «CSV, JSON, and XML Files». Қосымша: CS50P (Harvard, English), Week 9 «Et Cetera».
- Практика: тарау соңындағы practice questions.
- түсінбесең: besminut-teacher: SQLite, CSV, JSON

Дайын болу критерийі:
- [ ] Бір жобаны GitHub-қа README-мен салдың
- [ ] Жобада кемінде 3 функция мен 3 тест бар (CS50P талабына сай)

**Жоба 1 (бар жоба): CS50P Final Project — project.py ішінде main және кемінде үш функция, test_project.py ішінде pytest-тесттер, requirements.txt, README.md (~500 сөз) және ≤3 минуттық демо бейне (cs50.harvard.edu/python/2022/project/). Жоба 2 (өз брифім, сенің ESP32 тәжірибеңе): датчик деректерін CSV-ге жазып, SQLite-ке жүктеп, консольдік есеп шығаратын утилита; мақсаты: деректер ағынынан есепке дейінгі толық жол; қадамдары: 1) CSV оқу, 2) SQLite кестесі, 3) argparse-пен CLI, 4) 3 тест; дайын: README мен GitHub репозиторий.**

Қосымша (қажет болса): ресми Tutorial §10–11 «Brief tour of the standard library» (os, re, math, datetime, logging және т.б.) — жобада керек болғанда ғана оқы.
