import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, render_template, request, session, redirect
from library.lib.interestingFacts import queue

facts_bp = Blueprint('facts_bp', __name__)
@facts_bp.route('/facts')
def facts_page():
    if "user" not in session:
        return redirect("/")
    sort_order = request.args.get('sort', 'nearest')
    max_dist = request.args.get('max_dist', type=float)
    if max_dist is not None:
        queue.data = []
        queue.priority = []
        queue.load_filtered_data('facts.csv', max_dist=max_dist)
    if not queue.data and max_dist is None:
        queue.load_filtered_data('facts.csv', max_dist=50000)

    list_of_facts = queue.get_sorted_list(order=sort_order)
    return render_template('facts.html', all_facts=list_of_facts, current_sort=sort_order, current_max_dist=max_dist)