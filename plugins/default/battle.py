battle_info = pack['battle_info']

if pack['toho'] != "NULL": apisay(battle_info['text'],pack['toho'])
enemies = battle_info['level']

out = ''
act_list = {'g':'Guard','a':'Attack','b':'Break'}

move = 0 #0 - you | 1 - enemy
enemycount = 1
for enemy in enemies:
	atk = enemy['atk']
	hp = enemy['hp']
	out += '('+str(enemycount)+'/'+str(len(enemies))+') Ваш враг: '+enemy["name"]+'\nАтака = '+str(atk)+'\nЗдоровье = '+str(hp)+'\n\n'
	if move == 0:
		move = 1
		actions = []
		for _ in range(6):
			actions.append(random.choice(['a','g','b']))
		out += 'Известные действия врага:\n'
		for action in actions:
			knownrandom = random.randint(1,100)
			if knownrandom <= 50:
				out += '|'+act_list[action]+'|'
			else:
				out += '|????|'
		apisay(out, pack['toho'])
		exit()
	else:
		move = 0
		while True:
			if time.time() - timer >= 10:
				apisay('[SE.RA.PH] Вы отвечали слишком долго',pack['toho'])
				exit()
			if msgid != pack['msgid']:
				1+1
		
#[{"name":"Скелет","hp":1,"atk":200},{"name":"Скелет","hp":1,"atk":200},{"name":"Скелет","hp":1,"atk":200}]
