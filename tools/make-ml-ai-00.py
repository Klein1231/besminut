import json, hashlib, glob, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
# (stage title, time, [(material line, hard-topic hint or None)], done criteria, project)
stages=[
("Негіз: Python және математика","шамамен 3 ай",
 [("<b>1. CS50P</b> — Harvard CS50's Introduction to Programming with Python, David Malan, ағылшынша, тегін (cs50.harvard.edu/python). Нөлден Python: есептер мен тесттері бар. 10 апта, аптасына 3–9 сағат. Python-ды жақсы білсең, өткізіп жібер.",None),
  ("<b>2. Essence of linear algebra</b> — 3Blue1Brown, ағылшынша, тегін YouTube, 15 қысқа бейне (3blue1brown.com/topics/linear-algebra). Вектор мен матрицаның геометриялық мағынасы; бірнеше күнде көріп шығасың.","besminut-teacher: векторлар мен матрицалар ML үшін"),
  ("<b>3. Mathematics for Machine Learning</b> — Deisenroth, Faisal, Ong (Cambridge UP, 2020), ағылшынша, PDF тегін (mml-book.com). Бастан аяқ оқымайсың: 1-кезең бойы анықтамалық ретінде ал. Керек бөлімдері: сызықтық алгебра, векторлық есептеу, ықтималдық және үлестірімдер, оңтайландыру.","besminut-teacher: градиент пен градиенттік түсу")],
 ["Python-да 100–200 жолдық жобаны өзің жаздың, тест бар",
  "Матрицаны векторға көбейтудің геометриялық мағынасын сызып түсіндіре аласың",
  "Градиент, ықтималдық үлестірімі дегенді өз сөзіңмен айта аласың"],
 "Жоба (өз брифім): NumPy-мен сызықтық регрессияны градиенттік түсу арқылы нөлден жаз. Мақсаты: математиканы кодпен байланыстыру. Қадамдары: 1) жасанды дерек жаса, 2) жоғалту функциясын жаз, 3) градиентті қолмен есепте, 4) циклмен үйрет, 5) қателік графигін сал. Дайын: README мен графигі бар репозиторий."),
("Классикалық ML","шамамен 3 ай",
 [("<b>4. Kaggle Learn</b> — микрокурстар Pandas, Intro to Machine Learning, Intermediate Machine Learning, ағылшынша, тегін, браузерде (kaggle.com/learn). Әрқайсысы шамамен 3–4 сағат: деректермен жұмыс, алғашқы модельдер, валидация, жетіспейтін мәндер.",None),
  ("<b>5. Machine Learning Specialization</b> — Andrew Ng, DeepLearning.AI және Stanford Online, 3 курс, ағылшынша (deeplearning.ai/courses/machine-learning-specialization, Coursera-да да бар). Нұсқаулы және бақыланбайтын оқыту, нейрондық желілер, шешім ағаштары. 2 ай, аптасына 10 сағат. Сертификат ақылы, қолжетімділік шартын сайттан тексер.","besminut-teacher: шамадан тыс үйрену (overfitting) және валидация")],
 ["Pandas-пен таза емес деректі тазалай аласың",
  "Модельді оқу және тест жиынына бөліп, метриканы дұрыс таңдай аласың",
  "Шешім ағашы, сызықтық және логистикалық регрессияның айырмасын мысалмен түсіндіре аласың"],
 "Жоба 1 (бар жоба): Kaggle Intro to ML курсының соңғы жаттығуы — нақты Kaggle жарысына қатысу. Жоба 2 (өз брифім): кестелік деректе толық ML жобасы. Қадамдары: 1) ашық датасет ал (Kaggle), 2) деректі зертте, 3) 2–3 модельді валидациямен салыстыр, 4) қателік талдауы жаз. Дайын: ноутбук пен README (мәселе, метрика, нәтиже, қорытынды)."),
("Терең оқыту (deep learning)","шамамен 2–3 ай",
 [("<b>6. Neural networks</b> — 3Blue1Brown, 4 бейне, шамамен 1 сағат, ағылшынша, тегін (3blue1brown.com/topics/neural-networks). Нейрондық желі, градиенттік түсу, backpropagation интуициясы.","besminut-teacher: backpropagation"),
  ("<b>7. Practical Deep Learning for Coders</b> — fast.ai, Jeremy Howard, 2022 нұсқасы, 9 сабақ, әрқайсысы шамамен 90 минут, ағылшынша, тегін (course.fast.ai). Алдымен практика: үлгіні жұмыс істетесің, кейін ішіне үңілесің. Ішінде deployment да бар.",None),
  ("<b>8. Neural Networks: Zero to Hero</b> — Andrej Karpathy, ағылшынша, тегін YouTube, 9 лекция, шамамен 20–30 сағат (karpathy.ai/zero-to-hero.html). Backpropagation-нан GPT-ге дейін нөлден кодпен жазасың. Алдыңғы қадамның практикасынан кейін келсе, жақсы ұғылады.","besminut-teacher: attention және transformer")],
 ["PyTorch-та кескін немесе мәтін модельін өзің үйреттің",
  "Backpropagation-ды қағазда кіші желіде есептей аласың",
  "Кішкентай GPT тәрізді тілдік модельді өзің жазып, оқыттың"],
 "Жоба 1 (бар жоба): fast.ai сабағындағы deployment тәжірибесі: өз кескін классификаторыңды веб-демо ретінде жарияла. Жоба 2 (Karpathy): әр лекциядағы код пен соңындағы жаттығуларды өзің қайта жаз, көшірмей. Дайын: жарияланған демо және GitHub репозиторийі."),
("LLM және AI-инженерия","шамамен 2–3 ай",
 [("<b>9. LLM Course</b> — Hugging Face, ағылшынша, тегін (huggingface.co/learn/llm-course). Transformers, Datasets, Tokenizers кітапханалары, классикалық NLP тапсырмалары, демо жасау, LLM-ді fine-tuning және reasoning модельдері.","besminut-teacher: fine-tuning және tokenizer"),
  ("<b>10. AI Agents Course</b> — Hugging Face, ағылшынша, тегін (huggingface.co/learn/agents-course). Агент деген не, smolagents, LlamaIndex, LangGraph; соңында бенчмаркке арналған финал тапсырмасы.",None),
  ("<b>11. AI Engineering</b> — Chip Huyen, O'Reilly, 2025, ағылшынша, ақылы кітап (huyenchip.com/books). Foundation model негізіндегі қосымшаны жобалау, бағалау, дерек. Алдыңғы екі материалдан кейін оқы, сонда бәрін жүйелейді.","besminut-teacher: LLM қосымшасын бағалау (evaluation)")],
 ["Дайын LLM-ді өз деректеріңе fine-tuning немесе retrieval арқылы бейімдей аласың",
  "Агентке құрал (tool) қосып, жұмыс істеттің",
  "LLM қосымшасының сапасын өлшейтін өз тестіңді жаздың"],
 "Жоба 1 (бар жоба): Agents Course финал тапсырмасы: бенчмаркте 30% немесе одан жоғары балл жинау. Жоба 2 (өз брифім): өз құжаттарың бойынша сұраққа жауап беретін RAG көмекшісі. Қадамдары: 1) құжат жина, 2) бөлшектеп индекстеу, 3) сұрақ-жауап, 4) 20 сұрақтан тұратын бағалау жиыны, 5) нәтижені салыстыру. Дайын: демо, README, бағалау нәтижесі. Қосымша, тереңдету үшін (міндетті емес): Stanford CS224N (NLP with Deep Learning), YouTube-тағы тегін лекциялар."),
("Өндіріс: MLOps","шамамен 1–2 ай",
 [("<b>12. MLOps Course</b> — Made With ML, Goku Mohandas, ағылшынша, тегін, 49 сабақ, ашық код (madewithml.com). Эксперименттен өндіріске: дизайн, әзірлеу, деплой, итерация; тест, CI/CD, қайта жаңғыртымдылық, мониторинг.","besminut-teacher: MLOps, модельді өндіріске шығару")],
 ["Модельің API арқылы жұмыс істеп тұр",
  "Кодта тесттер мен қайта жаңғыртылатын орта бар",
  "Жобаны өзгеріссіз басқа адам іске қоса алады (README бойынша)"],
 "Қорытынды жоба (өз брифім): 2-4 кезеңдегі жобаның бірін өндіріске дайындау: API, тесттер, Docker, мониторинг, README. Дайын: репозиторий мен жұмыс істейтін демо; портфолиоға салуға жарайды."),
]
extra="Ескерту: уақыт шамамен; ол сенің ыңғайлы қарқыныңа байланысты. Материал атаулары мен мазмұны осы сессияда ресми беттерден расталған. Сертификат, баға және қолжетімділік шарттары өзгеруі мүмкін, сайттан тексер."
def ul(items): return '<ul>'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
import re
strip=lambda s: re.sub(r'<[^>]+>','',s)
parts=[]; md=["# ML & AI Engineer — оқу картасы\n","Материал тілі: негізінен ағылшынша. Уақыт шамамен. Материалдар осы сессияда ресми беттерден расталған.\n"]
parts.append("<h2>Жол: математика мен кодтан бастап, LLM мен өндіріске дейін</h2><p class=\"lead\">ML & AI Engineer болу үшін 5 кезең: негіз, классикалық ML, терең оқыту, LLM және AI-инженерия, өндіріс. Бәрі шамамен 12–15 ай. Әр кезеңнің соңында жоба бар.</p><p>Материалдардан өзің үйренесің, мен тек жол көрсетемін. Бір материал бітпей, келесіге өтпе. Түсінбеген жерде «түсінбесең» жолындағы сұранысты маған жаз.</p><p><b>Демек: кезең бойынша жүр, әр кезеңді жобамен бекіт.</b></p>")
for n,(title,dur,mats,done,proj) in enumerate(stages,1):
    md.append(f"## {n}-кезең. {title} ({dur})\n")
    h=f"<h2>{n}-кезең. {title}</h2><p><i>{dur}</i></p><ol start=\"{ {1:1,2:4,3:6,4:9,5:12}[n] }\">"
    for m,hard in mats:
        md.append(f"- {strip(m)}"+(f"\n  - түсінбесең: {hard}" if hard else ""))
        h+=f"<li>{re.sub(r'^<b>\d+\. ','<b>',m)}"+(f"<br>Түсінбесең: {hard}" if hard else "")+"</li>"
    h+="</ol>"
    md.append("\nДайын болу критерийі:\n"+"\n".join(f"- [ ] {d}" for d in done)+"\n")
    h+="<p><b>Дайын болу критерийі:</b></p>"+ul(["☐ "+d for d in done])
    md.append(f"**{proj}**\n"); h+=f"<p><b>{proj}</b></p>"
    parts.append(h)
md.append(extra+"\n"); parts[-1]+=f"<p>{extra}</p>"
parts.append("<h2>Осы аптадан не бастау керек</h2><p>1-қадамнан баста: CS50P-тің бірінші лекциясы мен бірінші есептер жинағы. Python-ды білсең, 2-қадамға өт: 3Blue1Brown сызықтық алгебра бейнелерін көр және бір мезгілде MML кітабын ашып қой. Әр апта соңында кезеңнің «дайын» тізімін тексер.</p><p><b>Демек: аптасына бір материалдың бір бөлігі, соңында өз кодың.</b></p>")
open('courses/ml-ai-engineer/plan.md','w',encoding='utf-8').write("\n".join(md))
pack={"format":"besminut-pack","version":1,"course":{"id":"ml-ai-engineer","name":"ML & AI Engineer","lang":"kk","space":"skills"},
 "lectures":[{"id":"ml-ai-engineer-00-plan","order":0,"title":"ML & AI Engineer — жоспар","source":"generated","parts":parts,"cards":[]}]}
json.dump(pack,open('courses/ml-ai-engineer/00-plan.json','w',encoding='utf-8'),ensure_ascii=False)
packs=[]
for p in sorted(glob.glob('courses/*/*.json')):
    if p.endswith('glossary.json') or p.endswith('syllabus.json'): continue
    packs.append({"path":p,"v":hashlib.sha1(open(p,'rb').read()).hexdigest()[:12]})
json.dump({"packs":packs},open('courses/index.json','w'),indent=1)
