from library.lib.logic import get_v1, get_v2, calculate_v1, calculate_v2

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