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
			pack['msgid'] = lastmsgid
			out = 'Выберите слугу для боя: <br>'
			out += 'Имя | Атака | Здоровье | Лвл | Редкость\n'
			inventory = json.loads(sqlite3.connect('data/users.db').cursor().execute('SELECT * FROM users WHERE id='+str(pack['userid'])).fetchall()[0][2])
			print(inventory)
			if len(inventory) > 0:
				elements = list(inventory.keys())
				count = 1
				for element in elements:
					out += str(count)+') '+element+' | '+str(inventory[element]['atk'])+' | '+str(inventory[element]['hp'])+' | '+str(inventory[element]['lvl'])+' | '+'★ '*inventory[element]['stars']+'\n'
					count += 1
				apisay(out,pack['toho'])
				
			else:
				apisay('[SE.RA.PH] У вас нет слуг',pack['toho'])
				exit()
			timer = time.time()
			while True:
				if time.time() - timer >= 20:
					apisay('[SE.RA.PH] Вы отвечали слишком долго',pack['toho'])
					exit()
				if msgid != lastmsgid:
					if not text.isdigit():
						apisay('[SE.RA.PH] Ответ должен быть числом',pack['toho'])
						lastmsgid = msgid
						continue	
					if int(text) <= count and int(text) > 0:
						pack['servant_stat'] = inventory[list(inventory.keys())[int(text)-1]]
						do_cmd(commands['battle.py'],pack)
			exit()
		else:
			apisay('[SE.RA.PH] Ваш ответ за приделами меню',pack['toho'])
			lastmsgid = msgid
