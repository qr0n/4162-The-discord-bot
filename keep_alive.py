from flask import Flask, render_template,  request, session
from tools import Linkify
import json
from replit import db

from oauth import Oauth
from threading import Thread
app = Flask('app')
app.config["SECRET_KEY"] = "test123"

@app.route('/')
def hello_world():
  return render_template("homepage.html")

@app.route('/HTopic')
def ren():
  with open("jsons/current_user.json", "r") as cj:
    ya = cj.read()

  with open("jsons/data.json", "r") as o:
    raw = o.read()
    if raw == None:
      raw = "Set a topic and start talking!"
    else:
      raw = raw
    return render_template("index.html", content=raw, name=ya)

@app.route('/Iron-News')
def ran():
  with open("jsons/news.json", "r") as n:
    raw = n.read()
  return render_template("news_updater.html", content=raw)

@app.route("/logged-in")
def login():
  code = request.args.get("code")
  at = Oauth.get_access_token(code)

  session["token"] = at
  
  user = Oauth.get_user_json(at)
  
  user_name, user_id, avatar, userid = user.get("username"), user.get("discriminator"), user.get("avatar"), user.get("id")
  
  with open("jsons/current_user.json", "w") as cj:
    cj.write(user_id)
  
  return render_template("logged.html",name=user_name)

@app.route('/more-options')
def more():
  return 'wip'
@app.route("/login")
def home():
	return render_template("login.html",discord_url= Oauth.discord_login_url)

@app.route('/debug/')
def pop():
  return render_template('infinylink.html')

@app.route('/tag-team/')
def asd():
  with open(f"bot.txt", "w"):
    pass
    return "operation done"

@app.route('/vc-logs')
def log():
  return str(db.keys())

def run():
  app.run(host='0.0.0.0',port=8042)

def keep_alive():
    t = Thread(target=run)
    t.start()