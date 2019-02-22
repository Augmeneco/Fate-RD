inventory = json.loads(sqlite3.connect('data/users.db').cursor().execute('SELECT * FROM users WHERE id='+str(pack['userid'])).fetchall()[0][1])
usersdb = sqlite3.connect('data/users.db')
summon = sqlite3.connect('data/game.db').cursor().execute('SELECT * FROM summon').fetchall()
count = 1
stars5 = list(range(1,6))
stars4 = list(range(6,11))
stars3 = list(range(11,31))
stars2 = list(range(30,61))
stars1 = list(range(61,101))
try:
	out = 'Святого кварца: '+str(inventory['Святой Кварц'])+'\n\n'
except KeyError:
	out = 'Святого кварца: 0\n\n'
	inventory['Святой Кварц'] = 0
for item in summon:
	out += str(count)+') '+summon[count-1][0]+'\n'
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
		if int(text) <= len(summon):
			if inventory['Святой Кварц'] < 3:
				apisay('[SE.RA.PH] У вас слишком мало кварца. Надо как минимум 3.',pack['toho'])
				exit()
			event_servants = json.loads(summon[int(text)-1][1])
			if random.randint(1,10) == 1:
				servant = sqlite3.connect('data/fate.db').cursor().execute('SELECT * FROM servants WHERE name="'+random.choice(event_servants)+'"').fetchall()[0]
				myserv = json.loads(usersdb.cursor().execute('SELECT * FROM users WHERE id='+str(pack['userid'])).fetchall()[0][2])
				inventory['Святой Кварц'] = inventory['Святой Кварц']-3
				out = '[SE.RA.PH] -3 кварца. Ваш баланс: '+str(inventory['Святой Кварц'])+'\n\nИнформация по вашему слуге:\n'+'Имя: '+servant[0]+'\nРедкость: '+'★ '*servant[10]+'\nУрон: '+str(servant[4])+'\nЗдоровье: '+str(servant[2])+'\nКласс: '+servant[9]
				sendpic('data/servants/'+servant[8],out,pack['toho'])
				myserv[servant[0]] = {
							'hp':servant[2],
							'atk':servant[4],
							'class':servant[9].lower(),
							'npatk':servant[6],
							'stars':servant[10],
							'lvl':1
						}
				myserv = json.dumps(myserv)
				inventory = json.dumps(inventory)
				usersdb.cursor().execute('UPDATE users SET inventory=\''+inventory+'\' WHERE id='+str(pack['userid'])).fetchall()
				usersdb.cursor().execute('UPDATE users SET servants=\''+myserv+'\' WHERE id='+str(pack['userid'])).fetchall()
				usersdb.commit()
				exit()
			else:
				serv_stars = random.randint(1,100)
				if serv_stars in stars5:
					serv_stars = 5
				if serv_stars in stars4:
					serv_stars = 4
				if serv_stars in stars3:
					serv_stars = 3
				if serv_stars in stars2:
					serv_stars = 2
				if serv_stars in stars1:
					serv_stars = 1
				servant = sqlite3.connect('data/fate.db').cursor().execute('SELECT * FROM servants WHERE stars='+str(serv_stars)).fetchall()
				servant = servant[random.randint(0,len(servant)-1)]
				myserv = json.loads(usersdb.cursor().execute('SELECT * FROM users WHERE id='+str(pack['userid'])).fetchall()[0][2])
				inventory['Святой Кварц'] = inventory['Святой Кварц']-3
				out = '[SE.RA.PH] -3 кварца. Ваш баланс: '+str(inventory['Святой Кварц'])+'\n\nИнформация по вашему слуге:\n'+'Имя: '+servant[0]+'\nРедкость: '+'★ '*servant[10]+'\nУрон: '+str(servant[4])+'\nЗдоровье: '+str(servant[2])+'\nКласс: '+servant[9]
				sendpic('data/servants/'+servant[8],out,pack['toho'])
				myserv[servant[0]] = {
							'hp':servant[2],
							'atk':servant[4],
							'class':servant[9].lower(),
							'npatk':servant[6],
							'stars':servant[10],
							'lvl':1
						}
				myserv = json.dumps(myserv)
				inventory = json.dumps(inventory)
				usersdb.cursor().execute('UPDATE users SET servants=\''+myserv+'\' WHERE id='+str(pack['userid'])).fetchall()
				usersdb.cursor().execute('UPDATE users SET inventory=\''+inventory+'\' WHERE id='+str(pack['userid'])).fetchall()
				usersdb.commit()
				exit()