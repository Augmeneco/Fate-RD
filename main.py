import requests, json, sqlite3, os, sys, psutil, threading, re, time, random
sys.path.append('plugins')

config = json.loads(open('config/bot.cfg','r').read())
cmds = json.loads(open('config/cmds.cfg','r').read())
commands = {}
token = json.loads(open('config/bot.cfg','r').read())['group_token']

def apisay(text,toho):
	return requests.post('https://api.vk.com/method/messages.send',data={'access_token':token,'v':'5.80','peer_id':toho,'message':text})
def sendpic(pic,mess,toho):
	ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
	with open(pic, 'rb') as f:
		ret = requests.post(ret['response']['upload_url'],files={'file1': f}).json()
	ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).json()
	requests.get('https://api.vk.com/method/messages.send?attachment=photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id'])+'&message='+mess+'&v=5.68&peer_id='+str(toho)+'&access_token='+str(token))
def do_cmd(code,pack):
	exec(code)

for path in os.listdir('plugins'):
	if os.path.isdir('plugins/'+path) and path != '__pycache__' and path != 'nouse':
		for plugin in os.listdir('plugins/'+path):
			commands[plugin] = open('plugins/'+path+'/'+plugin,'r').read()
			
while True:
	active = False
	try:
		response = requests.post(lpb['server']+'?act=a_check&key='+lpb['key']+'&ts='+str(ts)+'&wait=25').json()
		ts = response['ts']
	except Exception as error:
		if error == KeyboardInterrupt:
			sys.exit(0)
		lpb = requests.post('https://api.vk.com/method/groups.getLongPollServer',data={'access_token':config['group_token'],'v':'5.80','group_id':config['group_id']}).json()['response']
		ts = lpb['ts']
		continue

	for result in response['updates']:
		text = result['object']['text']
		msgid = result['object']['conversation_message_id']
		if '@fate_rd' in text:
			text = re.sub('\[club\d*\|@fate_rd\]','@fate_rd',text)
		text_split = text.split(' ')
		if text_split[0] in config['names']:
			active = True
		if active:
			toho = result['object']['peer_id']
			userid = result['object']['from_id']
			pack = {}
			pack['text'] = text
			pack['toho'] = toho
			pack['userid'] = userid
			pack['msgid'] = msgid
			lastmsgid = msgid
			if text_split[1] in cmds:
				threading.Thread(target=do_cmd,args=(commands[cmds[text_split[1]][1]],pack)).start()