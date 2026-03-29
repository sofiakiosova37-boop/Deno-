import sys
import os
from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library.lib.logic import get_v1, get_v2, calculate_v1, calculate_v2

# login
app = Flask(__name__)
app.secret_key = "solar_system_secret"
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

# для відображення підрахунків
@app.route('/calcus', methods=['GET', 'POST'])
def calcus():
    if "user" not in session:
        return redirect("/")
    result = None
    if request.method == 'POST':
        m = float(request.form.get('mass'))
        r = float(request.form.get('radius'))
        key = (m, r)
        v1 = get_v1.get(key)
        if v1 is None:
            v1 = calculate_v1(m, r)
            get_v1.put(key, v1)
        v2 = get_v2.get(key)
        if v2 is None:
                v2 = calculate_v2(m, r)
                get_v2.put(key, v2)
        result = {
            "v1": v1,
            "v2": v2,
            "mass": m,
            "radius": r
            }
    return render_template('calcus.html', result=result)

# вихід
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
@app.route('/calcus')  
def calcus():    
    return render_template('calcus.html')
if __name__ == "__main__":
    app.run(debug=True)

#


