import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, render_template, jsonify
from library.lib.news import get_all_news, NEWS_CSV_PATH

news_bp = Blueprint('news_bp', __name__)
@news_bp.route('/news')
def news_page():
    return render_template('news.html')

@news_bp.route('/api/news')
def get_news_json():
    data = get_all_news(NEWS_CSV_PATH)
    return jsonify(data)