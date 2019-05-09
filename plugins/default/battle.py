battle_info = pack['battle_info']
lastmsgid = pack['msgid']

if pack['toho'] != "NULL": apisay(battle_info['text'],pack['toho'])
enemies = battle_info['level']
servant_stat = [100,1005] #atk, hp 

#ТУ ХЕРНЮ ВЫШЕ НАДО ИСПРАВИТЬ БРАВ ЭТИ ДАННЫЕ ИЗ БД

act_list = {'g':'Guard','a':'Attack','b':'Break'}

move = 0 #0 - you | 1 - enemy
enemycount = 1
for enemy in enemies:
	user_dead = False
	enemy_dead = False
	while True:
		out = ''
		if user_dead:
			apisay('К сожалению ваш слуга погиб, вы его теряете навсегда',pack['toho'])
			#УДАЛЕНИЕ СЛУГИ
			exit()
		if enemy_dead:
			if len(enemies) > 1:
				apisay('побежден, переход к следующему врагу',pack['toho'])
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
				if knownrandom <= 50:
					out += '|'+act_list[action]+'|'
				else:
					out += '|????|'
			apisay(out, pack['toho'])
			#exit()
		else:
			move = 0
			timer = time.time()
			while True:
				if time.time() - timer >= 40:
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
						if enemy_hp <= 0:
							enemy_hp = 0
							enemy_dead = True
							break
							
						if servant_stat[1] <= 0:
							servant_stat[1] = 0
							user_dead = True
							break
							
						out = '[SE.RA.PH] %Сервант_нейм% наносит '+enemy['name']+' '+str(user_damage)+' урона\n'+enemy['name']+' наносит %Сервант_нейм% '+str(enemy_damage)+' урона\n\n'+'%Сервант нейм% Здоровье = '+str(servant_stat[1])+'\n'+enemy['name']+' Здоровье = '+str(enemy_hp)
						apisay(out,pack['toho'])
						break
					elif 'помощь' not in pack['text']:
						apisay('Не правильно введен ответ. Для помощи используй: '+config['names'][0]+' помощь',pack['toho'])
						lastmsgid = msgid
						continue
apisay('Поздравляю, ты победил всех',pack['toho'])
#[{"name":"Скелет","hp":1,"atk":200},{"name":"Скелет","hp":1,"atk":200},{"name":"Скелет","hp":1,"atk":200}]
