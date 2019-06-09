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
for count in range(len(menu)):
	out += str(count+1)+' - '+menu[count]['title']+'\n'
apisay(out,pack['toho'])
timer = time.time()
while True:
	if time.time() - timer >= 10:
		apisay('[SE.RA.PH] Вы отвечали слишком долго',pack['toho'])
		exit()
	if msgid != lastmsgid:
		if not text.isdigit():
			apisay('[SE.RA.PH] Ответ должен быть числом',pack['toho'])
			lastmsgid = msgid
		if int(text) <= len(menu):
			pack['msgid'] = msgid
			do_cmd(open('plugins/default/'+menu[int(text)-1]['src'],'r').read(),pack)
			exit()
		else:
			apisay('[SE.RA.PH] Ваш ответ за приделами меню',pack['toho'])
			lastmsgid = msgid
