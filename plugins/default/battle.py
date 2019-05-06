battle_info = pack['battle_info']

if pack['toho'] != "NULL": apisay(battle_info['text'],pack['toho'])
enemies = battle_info['level']
servant_stat = [1200,1005] #atk, hp 

#ТУ ХЕРНЮ ВЫШЕ НАДО ИСПРАВИТЬ БРАВ ЭТИ ДАННЫЕ ИЗ БД

out = ''
act_list = {'g':'Guard','a':'Attack','b':'Break'}

move = 0 #0 - you | 1 - enemy
enemycount = 1
for enemy in enemies:
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
				pack['text'] = text
				if len(re.findall('[abg]{6}',pack['text'])):
					user_damage = 0
					enemy_damage = 0
					for user_action in pack['text']:
						 for enemy_action in actions:
							 if user_action == 'a' and enemy_action == 'b': user_damage += servant_stat[0]		 
							 if user_action == 'g' and enemy_action == 'a': user_damage += servant_stat[0]		 
							 if user_action == 'b' and enemy_action == 'g': user_damage += servant_stat[0]	
							 	 
							 if user_action == 'b' and enemy_action == 'a': enemy_damage += enemy_atk
							 if user_action == 'a' and enemy_action == 'g': enemy_damage += enemy_atk	 
							 if user_action == 'g' and enemy_action == 'b': enemy_damage += enemy_atk
					servant_stat[1] = servant_stat[1] - enemy_damage
					enemy_hp = enemy_hp - user_damage
					
					out = '[SE.RA.PH] %Сервант_нейм% наносит '+enemy['name']+' '+str(user_damage)+' урона\n'+enemy['name']+' наносит %Сервант_нейм% '+str(enemy_damage)+' урона\n\n'+'%Сервант нейм% Здоровье = '+str(servant_stat[1])+'\n'+enemy['name']+' Здоровье = '+str(enemy_hp)
					apisay(out,pack['toho'])
#[{"name":"Скелет","hp":1,"atk":200},{"name":"Скелет","hp":1,"atk":200},{"name":"Скелет","hp":1,"atk":200}]
