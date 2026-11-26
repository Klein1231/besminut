import json, hashlib, glob, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
CS='CS50P (Harvard, English)'
stages=[
("Бағдарлама жазу негізі: функция, шарт, цикл","шамамен 2–3 апта",
 [("Айнымалы, функция, аргумент, return",
   f"Негізгі: {CS}, Week 0 «Functions, Variables». Қосымша: ATBS 3-басылым, Chapter 1 «Python Basics», Chapter 4 «Functions» (Automate the Boring Stuff, Al Sweigart, English).",
   "Практика: Week 0 бетіндегі Problem Set 0 (бетте бар екені расталды, есептердің атауын өзің ашып қара); ATBS тарау соңындағы practice questions (жауаптары Appendix B-де).",
   "besminut-teacher: функция, аргумент пен return"),
  ("Шарттар: if / elif / else",
   f"Негізгі: {CS}, Week 1 «Conditionals». Қосымша: ATBS Chapter 2 «if-else and Flow Control».",
   "Практика: Week 1 бетіндегі Problem Set.",None),
  ("Циклдер: while / for",
   f"Негізгі: {CS}, Week 2 «Loops». Қосымша: ATBS Chapter 3 «Loops»; ресми Tutorial §4.2–4.4 (for, range(), break/continue).",
   "Практика: Week 2 бетіндегі Problem Set.","besminut-teacher: for мен while циклі, қашан қайсысы")],
 ["Python-ды компьютеріңе орнатып, VS Code-та бағдарлама іске қостың (Week 0 «Visual Studio Code for CS50» қысқа бейнесі бар)",
  "Санды сұрап, шарт бойынша жауап беретін 10 жолдық бағдарлама өзің жаздың",
  "Problem Set 0–2 тесттен өтті, шешімді көшірмей жаздың"],
 "Жоба: сұраққа «екі шарт» пен цикл қолданатын консольдік «санды тап» ойыны (өз брифім: ойыншы 1–100 санын болжайды, бағдарлама «үлкен/кіші» дейді, талпыныс санын санайды)."),
("Мәліметтер құрылымдары: тізім, сөздік, жол","шамамен 2 апта",
 [("Тізім мен сөздік",
   "Негізгі: ATBS Chapter 6 «Lists», Chapter 7 «Dictionaries and Structuring Data». Қосымша: ресми Tutorial §5 «Data Structures» (5.1 тізім, 5.4 set, 5.5 сөздік, 5.1.3 list comprehensions).",
   "Практика: ATBS тарау соңындағы practice questions (Appendix B-де жауабы).","besminut-teacher: тізім мен сөздік, қайсысын қашан алу"),
  ("Жолдармен жұмыс",
   "Негізгі: ATBS Chapter 8 «Strings and Text Editing». Қосымша: ресми Tutorial §7.1 «Fancier output formatting» (f-string).",
   "Практика: ATBS Chapter 8 practice questions.",None)],
 ["Сөздікте сөз санын санайтын бағдарлама жаздың",
  "List comprehension мен әдеттегі for-цикл екеуін де жаза аласың",
  "Тізім мен сөздіктің айырмасын мысалмен түсіндіре аласың"],
 "Жоба: мәтіндегі сөздердің жиілігін санайтын бағдарлама (өз брифім: .txt файл ал, ең жиі 10 сөзді шығар)."),
("Қателер, файлдар, тест, regex","шамамен 3 апта",
 [("Қателерді өңдеу және іздеу",
   f"Негізгі: {CS}, Week 3 «Exceptions». Қосымша: ATBS Chapter 5 «Debugging»; ресми Tutorial §8 «Errors and Exceptions».",
   "Практика: Week 3 бетіндегі Problem Set.","besminut-teacher: try/except, қате қашан көтеріледі"),
  ("Файлмен жұмыс",
   f"Негізгі: {CS}, Week 6 «File I/O». Қосымша: ATBS Chapter 10 «Reading and Writing Files»; ресми Tutorial §7.2 (оның ішінде json).",
   "Практика: Week 6 бетіндегі Problem Set.",None),
  ("Unit тесттер (pytest)",
   f"Негізгі: {CS}, Week 5 «Unit Tests».",
   "Практика: Week 5 бетіндегі Problem Set.","besminut-teacher: pytest, тест жазу"),
  ("Регулярлы өрнектер",
   f"Негізгі: {CS}, Week 7 «Regular Expressions». Қосымша: ATBS Chapter 9 «Text Pattern Matching with Regular Expressions».",
   "Практика: Week 7 бетіндегі Problem Set.","besminut-teacher: regex")],
 ["Қате шыққанда бағдарлама құламай, түсінікті хабар береді",
  "Файлдан оқып, файлға жаза аласың",
  "Өз функцияңа pytest-пен 3 тест жаздың"],
 "Жоба: email/телефон тексеретін шағын утилита (өз брифім: файлдағы жолдарды regex-пен тексеріп, дұрыс/бұрыс тізімін екі файлға жаз, тест жаз)."),
("Кітапханалар, модульдер, виртуал орта","шамамен 1 апта",
 [("Сырттан кітапхана қосу",
   f"Негізгі: {CS}, Week 4 «Libraries». Қосымша: ATBS Appendix A «Installing Third-Party Packages»; ресми Tutorial §6 «Modules» және §12 «Virtual Environments and Packages».",
   "Практика: Week 4 бетіндегі Problem Set.","besminut-teacher: venv пен pip")],
 ["Әр жобаға бөлек виртуал орта құрдың",
  "pip-пен кітапхана орнатып, requirements.txt жаздың"],
 None),
("Классты түсіну: OOP","шамамен 2 апта",
 [("Класс, объект, әдіс, мұрагерлік",
   f"Негізгі: {CS}, Week 8 «Object-Oriented Programming». Қосымша: ресми Tutorial §9 «Classes» (9.3 классқа кіріспе, 9.5 Inheritance, 9.8 Iterators, 9.9 Generators).",
   "Практика: Week 8 бетіндегі Problem Set.","besminut-teacher: класс пен объект, self")],
 ["Өз класыңды жазып, одан 2 объект жасадың",
  "Мұрагерлікті қолданған мысал жаздың"],
 None),
("Нақты жобалар: автоматтандыру және деректер","шамамен 3–4 апта",
 [("Командалық жол, веб-скрейпинг, SQLite, CSV/JSON",
   f"Негізгі: ATBS Chapter 12 «Designing and Deploying Command Line Programs», Chapter 13 «Web Scraping», Chapter 16 «SQLite Databases», Chapter 18 «CSV, JSON, and XML Files». Қосымша: {CS}, Week 9 «Et Cetera».",
   "Практика: тарау соңындағы practice questions.","besminut-teacher: SQLite, CSV, JSON")],
 ["Бір жобаны GitHub-қа README-мен салдың",
  "Жобада кемінде 3 функция мен 3 тест бар (CS50P талабына сай)"],
 "Жоба 1 (бар жоба): CS50P Final Project — project.py ішінде main және кемінде үш функция, test_project.py ішінде pytest-тесттер, requirements.txt, README.md (~500 сөз) және ≤3 минуттық демо бейне (cs50.harvard.edu/python/2022/project/). Жоба 2 (өз брифім, сенің ESP32 тәжірибеңе): датчик деректерін CSV-ге жазып, SQLite-ке жүктеп, консольдік есеп шығаратын утилита; мақсаты: деректер ағынынан есепке дейінгі толық жол; қадамдары: 1) CSV оқу, 2) SQLite кестесі, 3) argparse-пен CLI, 4) 3 тест; дайын: README мен GitHub репозиторий."),
]
extra="Қосымша (қажет болса): ресми Tutorial §10–11 «Brief tour of the standard library» (os, re, math, datetime, logging және т.б.) — жобада керек болғанда ғана оқы."
def ul(items,cls=''): return '<ul>'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
parts=[]
md=["# Python — оқу картасы\n","Материал тілі: барлығы ағылшынша (CS50P, ATBS, ресми Tutorial). Уақыт — шамамен. Тарау/апта атаулары осы сессияда сайттардан расталған.\n"]
parts.append("<h2>Бұл карта: материалдан үйренесің, мен жол көрсетемін</h2><p class=\"lead\">Төменде 6 кезең. Әр кезеңде материал, практика, «дайын» критерийі және жоба бар. Түсінбеген жерің болса, «түсінбесең» жолындағы сұранысты маған жаз.</p><p>Үш негізгі материал: <b>CS50P</b> (Harvard CS50's Introduction to Programming with Python, 2022, cs50.harvard.edu/python/2022), <b>ATBS</b> (Automate the Boring Stuff with Python, 3-басылым, Al Sweigart, automatetheboringstuff.com/3e) және <b>ресми Tutorial</b> (docs.python.org/3/tutorial).</p><p>Қорытынды: <b>Демек: бір негізгі материал + практика + жоба, артық ештеңе жоқ.</b></p>")
for n,(title,dur,topics,done,proj) in enumerate(stages,1):
    md.append(f"## {n}-кезең. {title} ({dur})\n")
    h=f"<h2>{n}-кезең. {title}</h2><p><i>{dur}</i></p>"
    for t,mat,prac,hard in topics:
        md.append(f"### {t}\n- {mat}\n- {prac}"+(f"\n- түсінбесең: {hard}" if hard else "")+"\n")
        h+=f"<h3>{t}</h3><ul><li>{mat}</li><li>{prac}</li>"+(f"<li>Түсінбесең: {hard}</li>" if hard else "")+"</ul>"
    md.append("Дайын болу критерийі:\n"+"\n".join(f"- [ ] {d}" for d in done)+"\n")
    h+="<p><b>Дайын болу критерийі:</b></p>"+ul(done)
    if proj: md.append(f"**{proj}**\n"); h+=f"<p><b>{proj}</b></p>"
    parts.append(h)
md.append(extra+"\n"); parts[-1]+=f"<p>{extra}</p>"
parts.append("<h2>Осы аптадан не бастау керек</h2><p>1-кезеңнен баста: CS50P Week 0 лекциясы мен Problem Set 0. Алдымен Python мен VS Code орнат, сосын лекцияны көр. Әр апта соңында «дайын» критерийін тексер.</p><p><b>Демек: аптасына бір CS50P апта, соңында өз кодыңмен тексер.</b></p>")
open('courses/python/plan.md','w',encoding='utf-8').write("\n".join(md))
pack={"format":"besminut-pack","version":1,"course":{"id":"python","name":"Python","lang":"kk","space":"skills"},
 "lectures":[{"id":"python-00-plan","order":0,"title":"Python — жоспар","source":"generated","parts":parts,"cards":[]}]}
json.dump(pack,open('courses/python/00-plan.json','w',encoding='utf-8'),ensure_ascii=False)
# index
old=json.load(open('courses/index.json'))
ref=old['packs'][0]; print('check hash',hashlib.sha1(open(ref['path'],'rb').read()).hexdigest()[:12],ref['v'])
packs=[]
for p in sorted(glob.glob('courses/*/*.json')):
    if p.endswith('glossary.json'): continue
    packs.append({"path":p,"v":hashlib.sha1(open(p,'rb').read()).hexdigest()[:12]})
json.dump({"packs":packs},open('courses/index.json','w'),indent=1)
