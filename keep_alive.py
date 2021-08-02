from flask import Flask, render_template,  request, session
from tools import Linkify
import json

from oauth import Oauth
from threading import Thread
app = Flask('app')
app.config["SECRET_KEY"] = "test123"

@app.route('/')
def hello_world():
  return render_template("homepage.html")

@app.route('/HTopic')
def ren():
  with open("jsons/data.json", "r") as o:
    raw = o.read()
    if raw == None:
      raw = "Set a topic and start talking!"
    else:
      raw = raw
    return render_template("index.html", content=raw)

@app.route('/Iron-News')
def ran():
  with open("jsons/news.json", "r") as n:
    raw = n.read()
  return render_template("news_updater.html", content=raw)

def run():
  app.run(host='0.0.0.0',port=8042)

def keep_alive():
    t = Thread(target=run)
    t.start()

@app.route("/logged-in")
def login():
	code = request.args.get("code")

	at = Oauth.get_access_token(code)
	session["token"] = at

	user = Oauth.get_user_json(at)
	user_name, user_id = user.get("username"), user.get("discriminator")

	return f"Success, logged in as {user_name}#{user_id}"


@app.route("/login")
def home():
	return render_template("login.html",discord_url= Oauth.discord_login_url)

if __name__ == "__main__":
	app.run(debug=True)
