menu = ['Предметы','Слуги']
out = '[SE.RA.PH] Выберете действие цифрой:\n'
for count in range(len(menu)):
	out += str(count+1)+' - '+menu[count]+'\n'
apisay(out,pack['toho'])

timer = time.time()
while True:
	if time.time() - timer >= 10:
		apisay('[SE.RA.PH] Вы отвечали слишком долго',pack['toho'])
		exit()
	if msgid != pack['msgid']:
		if not text.isdigit():
			apisay('[SE.RA.PH] Ответ должен быть числом',pack['toho'])
			lastmsgid = msgid
		if int(text) <= len(menu):
			if text == '1':
				out = 'Название | Количество\n'
				inventory = json.loads(sqlite3.connect('data/users.db').cursor().execute('SELECT * FROM users WHERE id='+str(pack['userid'])).fetchall()[0][1])
				if len(inventory) > 0:
					elements = list(inventory.keys())
					count = 1
					for element in elements:
						out += str(count)+') '+element+' | '+str(inventory[element]['count'])
						count += 1
					apisay(out,pack['toho'])
					exit()
				else:
					apisay('[SE.RA.PH] Ваш инвентарь пуст',pack['toho'])
					exit()
			if text == '2':
				out = 'Имя | Атака | Здоровье | Лвл\n'
				inventory = json.loads(sqlite3.connect('data/users.db').cursor().execute('SELECT * FROM users WHERE id='+str(pack['userid'])).fetchall()[0][2])
				if len(inventory) > 0:
					elements = list(inventory.keys())
					count = 1
					for element in elements:
						out += str(count)+') '+element+' | '+str(inventory[element]['atk'])+' | '+str(inventory[element]['hp'])+' | '+str(inventory[element]['lvl'])
						count += 1
					apisay(out,pack['toho'])
					exit()
				else:
					apisay('[SE.RA.PH] У вас нет слуг',pack['toho'])
					exit()
		else:
			apisay('[SE.RA.PH] Ваш ответ за приделами меню',pack['toho'])
			lastmsgid = msgid