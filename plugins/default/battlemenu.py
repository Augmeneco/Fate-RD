gamedb = sqlite3.connect('data/game.db')
battlelist = gamedb.cursor().execute('SELECT * FROM battles').fetchall()
out = ''
count = 1
for battle in battlelist:
	battle = json.loads(battle[0])
	out += str(count)+') '+battle['title']+'\n'
	count += 1
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
		if int(text) <= len(battlelist[0]):
			battle = json.loads(battlelist[0][int(text)-1])
			lastmsgid = msgid
			pack = pack
			pack['battle_info'] = battle
			do_cmd(commands['battle.py'],pack)
			exit()
		else:
			apisay('[SE.RA.PH] Ваш ответ за приделами меню',pack['toho'])
			lastmsgid = msgid