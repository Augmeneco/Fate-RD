menu = ['Предметы','Слуги']
out = '[SE.RA.PH] Выберете действие цифрой:\n'
keyboard = {'one_time': False, 'buttons': [[]]}
for count in range(len(menu)):
	out += str(count+1)+' - '+menu[count]+'\n'
	keyboard['buttons'][0].append({'action': {'type': 'text', 'payload': str(count+1), 'label': menu[count]}, 'color': 'secondary'})
keyboard['buttons'].append([])
keyboard['buttons'][1].append({'action': {'type': 'text', 'payload': '"back"', 'label': 'Назад'}, 'color': 'negative'})
keyboard['buttons'][1].append({'action': {'type': 'text', 'payload': '"exit"', 'label': 'Выход'}, 'color': 'negative'})
apisay(out,pack['toho'],keyboard)

timer = time.time()
lastmsgid = pack['msgid']
while True:
	if time.time() - timer >= 10:
		apisay('[SE.RA.PH] Вы отвечали слишком долго',pack['toho'],{"buttons":[],"one_time":True})
		exit()
	if msgid != lastmsgid:
		if payload == '"exit"': exit()
		if payload == '"back"': 
			do_cmd(open('plugins/default/menu.py','r').read(),pack)
			exit()
		if payload != None:
			text = payload
		if not text.isdigit():
			apisay('[SE.RA.PH] Ответ должен быть числом',pack['toho'])
			lastmsgid = msgid
			continue
		if int(text) <= len(menu):
			if text == '1':
				out = 'Название | Количество\n'
				inventory = json.loads(sqlite3.connect('data/users.db').cursor().execute('SELECT * FROM users WHERE id='+str(pack['userid'])).fetchall()[0][1])
				if len(inventory) > 0:
					elements = list(inventory.keys())
					count = 1
					for element in elements:
						out += str(count)+') '+element+' | '+str(inventory[element])+'\n'
						count += 1
					apisay(out,pack['toho'])
					exit()
				else:
					apisay('[SE.RA.PH] Ваш инвентарь пуст',pack['toho'])
					exit()
			if text == '2':
				out = 'Имя | Атака | Здоровье | Лвл | Редкость\n'
				inventory = json.loads(sqlite3.connect('data/users.db').cursor().execute('SELECT * FROM users WHERE id='+str(pack['userid'])).fetchall()[0][2])
				if len(inventory) > 0:
					elements = list(inventory.keys())
					count = 1
					for element in elements:
						out += str(count)+') '+element+' | '+str(inventory[element]['atk'])+' | '+str(inventory[element]['hp'])+' | '+str(inventory[element]['lvl'])+' | '+'★ '*inventory[element]['stars']+'\n'
						count += 1
					apisay(out,pack['toho'])
					exit()
				else:
					apisay('[SE.RA.PH] У вас нет слуг',pack['toho'])
					exit()
		else:
			apisay('[SE.RA.PH] Ваш ответ за приделами меню',pack['toho'])
			lastmsgid = msgid
	time.sleep(0.1)
