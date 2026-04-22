import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, render_template, request, redirect, session
from library.lib.logic import get_v1, get_v2, get_sch, get_grav, calculate_v1, calculate_v2, calculate_schwarzschild, calculate_gravity

calcus_bp = Blueprint('calcus_bp', __name__)
@calcus_bp.route('/calcus', methods=['GET', 'POST'])
def calcus():
    if "user" not in session:
        return redirect("/")
    result = None
    if request.method == 'POST':
        m = float(request.form.get('mass'))
        r = float(request.form.get('radius'))
        key_mr = (m, r)
        key_m = (m)
        v1 = get_v1.get(key_mr)
        if v1 is None:
            v1 = calculate_v1(m, r)
            get_v1.put(key_mr, v1)
        v2 = get_v2.get(key_mr)
        if v2 is None:
                v2 = calculate_v2(m, r)
                get_v2.put(key_mr, v2)
        rad = get_sch.get(key_m)
        if rad is None:
            rad = calculate_schwarzschild(m)
            get_sch.put(key_m, rad)
        g = get_grav.get(key_mr) 
        if g is None:
            g = calculate_gravity(m, r)
            get_grav.put(key_mr, g)

            result = {
            "v1": v1,
            "v2": v2,
            "rad": rad,
            "g": g,
            "mass": m,
            "radius": r
            }

    return render_template('calcus.html', result=result)