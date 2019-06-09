menu = json.loads(sqlite3.connect('data/game.db').cursor().execute('SELECT * FROM menu').fetchall()[1][0])
out = '[SE.RA.PH] Выберете действие цифрой:\n'
keyboard = {'one_time': False, 'buttons': [[]]}
for count in range(len(menu)):
	out += str(count+1)+' - '+menu[count]['title']+'\n'
	keyboard['buttons'][0].append({'action': {'type': 'text', 'payload': str(count+1), 'label': menu[count]['title']}, 'color': 'secondary'})
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
			pack['msgid'] = msgid
			do_cmd(open('plugins/default/'+menu[int(text)-1]['src'],'r').read(),pack)
			exit()
		else:
			apisay('[SE.RA.PH] Ваш ответ за приделами меню',pack['toho'])
			lastmsgid = msgid
	time.sleep(0.1)
