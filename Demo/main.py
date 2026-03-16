import sys
import os
from flask import Flask, render_template, jsonify

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from library.fib_lib import fibonacci  

app = Flask(__name__)

fib_gen = fibonacci()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_fib')
def get_fib():
    return jsonify({"number": next(fib_gen)})

if __name__ == "__main__":
    app.run(debug=True)