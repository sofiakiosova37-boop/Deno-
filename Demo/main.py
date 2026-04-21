import sys
import os
from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import datetime
import requests
from calcus import calcus_bp
from facts import facts_bp

# login
app = Flask(__name__)
app.secret_key = "solar_system_secret"

app.register_blueprint(calcus_bp)
app.register_blueprint(facts_bp)
# сторінка входу
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        nickname = request.form.get("nickname")
        # для збереження ніка в сесії
        session["user"] = nickname
        # записуємо у файл
        with open("visitors.txt","a",encoding="utf-8") as f:
            f.write(f"{nickname} | {datetime.now()}\n")
        return redirect("/menu")
    return render_template("login.html")
# головне меню
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

@app.route('/iss')  
def iss():
    location_res = requests.get("http://api.open-notify.org/iss-now.json").json()
    crew_res = requests.get("http://api.open-notify.org/astros.json").json()
    return render_template('iss.html', location=location_res, crew=crew_res)

if __name__ == "__main__":
    app.run(debug=True)


