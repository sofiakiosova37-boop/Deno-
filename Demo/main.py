import sys
import os
from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import datetime
from calcus import calcus_bp
from facts import facts_bp
from iss import iss_bp 
from news import news_bp
import logging

app = Flask(__name__)
app.secret_key = "solar_system_secret"

app.register_blueprint(calcus_bp)
app.register_blueprint(facts_bp)
app.register_blueprint(iss_bp)
app.register_blueprint(news_bp)
# сторінка входу
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        nickname = request.form.get("nickname")
        session["user"] = nickname
        with open("visitors.txt","a",encoding="utf-8") as f:
            f.write(f"{nickname} | {datetime.now()}\n")
        return redirect("/menu")
    return render_template("login.html")

@app.route("/menu")
def menu():
    if "user" not in session:
        return redirect("/")
    return render_template("index.html", user=session["user"])

# вихід
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route('/solar')  
def solar():
    return render_template('solar.html')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
    handlers=[
        logging.FileHandler("app_log.json"),
        logging.StreamHandler()
    ]
)
if __name__ == "__main__":
    app.run(debug=True)


