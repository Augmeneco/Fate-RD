if len(sqlite3.connect('data/users.db').cursor().execute('SELECT * FROM users WHERE id='+str(pack['userid'])).fetchall()) == 0:
	apisay('[SE.RA.PH] У вас нет доступа сюда. Для начала обратитесь в команду "старт"',pack['toho'])
	exit()
menu = json.loads(sqlite3.connect('data/game.db').cursor().execute('SELECT * FROM menu').fetchall()[0][0])
if len(pack['text'].split(' ')) > 2:
	menu_num = pack['text'].split(' ')[2]
	if menu_num.isdigit(): menu_num = int(menu_num)
	else: 
		apisay('Аргумент меню должен быть цифрой',pack['toho'])
		exit()
	if menu_num <= len(menu):
		pack['msgid'] = msgid
		do_cmd(open('plugins/default/'+menu[menu_num-1]['src'],'r').read(),pack)
		exit()
	else:
		apisay('[SE.RA.PH] Ваш ответ за приделами меню',pack['toho'])
		lastmsgid = msgid
		exit()
out = '[SE.RA.PH] Выберете действие цифрой:\n'
keyboard = {'one_time': False, 'buttons': [[]]}
for count in range(len(menu)):
	out += str(count+1)+' - '+menu[count]['title']+'\n'
	keyboard['buttons'][0].append({'action': {'type': 'text', 'payload': str(count+1), 'label': menu[count]['title']}, 'color': 'secondary'})
apisay(out,pack['toho'],keyboard)

timer = time.time()
while True:
	if time.time() - timer >= 10:
		apisay('[SE.RA.PH] Вы отвечали слишком долго',pack['toho'],{"buttons":[],"one_time":True})
		exit()
	if msgid != lastmsgid:
		if payload in ['"back"','"exit"']: continue
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

