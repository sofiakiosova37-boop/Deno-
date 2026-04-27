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
    list_of_facts = queue.get_sorted_list(order=sort_order)
    return render_template('facts.html', all_facts=list_of_facts, current_sort=sort_order)