battle_info = pack['battle_info']
lastmsgid = pack['msgid']

if pack['toho'] != "NULL": apisay(battle_info['text']+'<br>―――――――――――――――――――――――――――――――――',pack['toho'])
enemies = battle_info['level']

servant_stat = [pack['servant_stat']['atk'],pack['servant_stat']['hp']]

act_list = {'g':'Guard','a':'Attack','b':'Break'}

move = 0 #0 - you | 1 - enemy
enemycount = 1
for enemy in enemies:
	user_dead = False
	enemy_dead = False
	while True:
		out = ''
		if user_dead:
			apisay('―――――――――――――――――――――――――――――――――\nК сожалению ваш слуга '+pack['servant_stat']['name']+' погиб, вы проиграли.',pack['toho'])
			exit()
		if enemy_dead:
			if len(enemies) > 1:
				if enemycount != len(enemies):
					apisay('Побежден, переход к следующему врагу<br>―――――――――――――――――――――――――――――――――',pack['toho'])
					enemycount += 1
				break
			else:
				apisay(enemy['name']+' побежден',pack['toho'])
				break
		
		enemy_atk = enemy['atk']
		enemy_hp = enemy['hp']
		out += '('+str(enemycount)+'/'+str(len(enemies))+') Ваш враг: '+enemy["name"]+'\nАтака = '+str(enemy_atk)+'\nЗдоровье = '+str(enemy_hp)+'\n\n'
		if move == 0:
			move = 1
			actions = []
			for _ in range(6):
				actions.append(random.choice(['a','g','b']))
			out += 'Известные действия врага:\n'
			for action in actions:
				knownrandom = random.randint(1,100)
				if knownrandom <= 60:
					out += '|'+act_list[action]+'|'
				else:
					out += '|????|'
			apisay(out, pack['toho'])
			#exit()
		else:
			move = 0
			timer = time.time()
			while True:
				if time.time() - timer >= 60:
					apisay('[SE.RA.PH] Вы отвечали слишком долго',pack['toho'])
					exit()
				if msgid != lastmsgid:
					pack['text'] = text
					if len(re.findall('[abg]{6}',pack['text'])) != 0:
						lastmsgid = msgid
						user_damage = 0
						enemy_damage = 0
						
						for num in range(6):
							user_action = pack['text'][num]
							enemy_action = actions[num]
						
							if user_action == 'a' and enemy_action == 'b': user_damage += servant_stat[0]
							if user_action == 'g' and enemy_action == 'a': user_damage += servant_stat[0]		
							if user_action == 'b' and enemy_action == 'g': user_damage += servant_stat[0]
							
							if user_action == 'b' and enemy_action == 'a': enemy_damage += enemy_atk
							if user_action == 'a' and enemy_action == 'g': enemy_damage += enemy_atk	 
							if user_action == 'g' and enemy_action == 'b': enemy_damage += enemy_atk
							
						servant_stat[1] = servant_stat[1] - enemy_damage
						enemy_hp = enemy_hp - user_damage
						if enemy_hp < 0:
							enemy_hp = 0
							enemy_dead = True
						if servant_stat[1] < 0:
							servant_stat[1] = 0
							user_dead = True
							
						out = '[SE.RA.PH] '+pack['servant_stat']['name']+' наносит '+enemy['name']+' '+str(user_damage)+' урона\n'+enemy['name']+' наносит '+pack['servant_stat']['name']+' '+str(enemy_damage)+' урона\n\n'+pack['servant_stat']['name']+' Здоровье = '+str(servant_stat[1])+'\n'+enemy['name']+' Здоровье = '+str(enemy_hp)
						apisay(out,pack['toho'])
						
						break
					elif 'помощь' not in pack['text']:
						apisay('Не правильно введен ответ. Для помощи используй: '+config['names'][0]+' помощь',pack['toho'])
						lastmsgid = msgid
						continue
usersdb = sqlite3.connect('data/users.db')
usersdb_data = usersdb.execute('SELECT * FROM users WHERE id='+str(pack['userid'])).fetchall()[0]
user_missions = json.loads(usersdb_data[3])
user_inventory = json.loads(usersdb_data[1])
user_missions.append(battle_info['id'])
usersdb.cursor().execute('UPDATE users SET missions="'+json.dumps(user_missions)+'" WHERE id = '+str(pack['userid']))

loot = battle_info['loot']
lootout = ''
for item in loot:
	loot_name = item[0]
	loot_count = item[1]
	lootout += loot_name+' - '+str(loot_count)+'\n'
	try:
		user_inventory[loot_name] += loot_count
	except (NameError,KeyError):
		user_inventory[loot_name] = loot_count
usersdb.cursor().execute('UPDATE users SET inventory=\''+json.dumps(user_inventory)+'\' WHERE id = '+str(pack['userid']))
usersdb.commit()

apisay('―――――――――――――――――――――――――――――――――\nМиссия завершена, вы получаете за выполнение:\n'+lootout,pack['toho'])
#[{"name":"Скелет","hp":1,"atk":200},{"name":"Скелет","hp":1,"atk":200},{"name":"Скелет","hp":1,"atk":200}]
