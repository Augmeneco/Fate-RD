intro_text = '[SE.RA.PH] 2509 год. К 26 веку человечество успешно колонизирует космос. На планете Лотиан был успешно воссоздан старый проект "Лунная клеть". Так-как магическая энергия давно уже забыта, а технологии давно развиты, "Война Святого Грааля" стала простым виртуальным развлечением. Ваша цель - стать лучшим мастером и пройти все уровни системы СЕ.РА.Ф.'
apisay('Добро пожаловать в игру Fate/Relative Dimension\n[SE.RA.PH] Пропустить вступление? да/нет',pack['toho'])
intro_show = False
timer = time.time()
while True:
	if time.time() - timer >= 10:
		apisay('[SE.RA.PH] Вы отвечали слишком долго',pack['toho'])
		exit()
	if 'нет' in text.lower() and userid == pack['userid']:
		lastmsgid = msgid
		apisay(intro_text,pack['toho'])
		break
	if 'да' in text.lower() and userid == pack['userid']:
		lastmsgid = msgid
		break
out = '[SE.RA.PH] Начинаю создание слуги. Для катализатора призыва используется случайна фраза. На ответ вам 30 секунд.'
apisay(out,pack['toho'])

timer = time.time()
while True:
	if time.time() - timer >= 30:
		apisay('[SE.RA.PH] Вы отвечали слишком долго',pack['toho'])
		exit()
	if userid == pack['userid'] and msgid != lastmsgid:
		catalyzer = text
		out = '[SE.RA.PH] Катализатор принят. Начинаем инициализацию призыва.'
		apisay(out,pack['toho'])
		break
	time.sleep(0.05)
conn = sqlite3.connect('data/fate.db')
cursor = conn.cursor()
servant = cursor.execute('SELECT * FROM servants').fetchall()
import random
random.seed(sum([ord(x) for x in catalyzer]))
servant = servant[random.randint(0,len(servant)-1)]
out = '[SE.RA.PH] Информация по вашему слуге:\n'+'Имя: '+servant[0]+'\nУрон: '+str(servant[4])+'\nЗдоровье: '+str(servant[2])+'\nКласс: '+servant[9]
sendpic('data/servants/'+servant[8],out,pack['toho'])