import csv
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'news.csv')

class AstroEventsEmitter:
    def __init__(self):
        self._listeners = {}

def notification(data):
    print(f"Подія: {data['info']}")
    print(f"Дата: {data['day']} {data['month']} {data['year']}")

def news(file_path, emitter):
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f) 
    except FileNotFoundError:
        print("Error")