menu = json.loads(sqlite3.connect('data/game.db').cursor().execute('SELECT * FROM menu').fetchall()[0][0])
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
		if int(text) < len(menu):
			pack['msgid'] = msgid
			do_cmd(open('plugins/default/'+menu[int(text)-1]['src'],'r').read(),pack)
		else:
			apisay('[SE.RA.PH] Ваш ответ за приделами меню',pack['toho'])
			lastmsgid = msgid