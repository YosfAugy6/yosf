# MY Tele @GG8MG

from flask import Flask
import requests


def sa(usertik):
	
	
	url = 'http://tik.report.ilebo.cc/users/login'
	he = {
'X-IG-Capabilities': '3brTvw==',
'User-Agent': 'TikTok 85.0.0.21.100 Android (33/13; 480dpidpi; 1080x2298; HONOR; ANY-LX2; ANY-LX2;)',
'Accept-Language': 'en-US',
'Content-Type': 'application/json; charset=utf-8',
'Content-Length': '73',
'Host': 'tik.report.ilebo.cc',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
}
	da={"unique_id":f"{usertik}","purchaseTokens":[]}

	re=requests.post(url,headers=he,data=da).json()
	Id = re['data']['user']['user']['id']
	user = re['data']['user']['user']['uniqueId']
	name = re['data']['user']['user']['nickname']
	folon = re['data']['user']['stats']['followingCount']

	folos = re['data']['user']['stats']['followerCount']
	lik = re['data']['user']['stats']['heartCount']
	vid = re['data']['user']['stats']['videoCount']
	age = re['data']['user']['user']['underAge18']
	priv = re['data']['user']['user']['privateAccount']
	om = (f'''
  information 
─────────────────
USER - {user}
NAME - {name}
ID - {Id}
Following - {folon}
Followers - {folos}
LIKE - {lik}
VIDEO - {vid}
UNDERAGE 18 - {age} 
PRIVATE - {priv} 
─────────────────
''')
	
	return om	
		


app = Flask(__name__)
@app.route('/info/usertik=<text>')
def home(text):
	try:
		return sa(text)
	except:
		return {"Bad"}

if __name__=="__main__":
	app.run(debug=True)