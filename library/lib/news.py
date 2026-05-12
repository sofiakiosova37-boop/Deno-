import csv
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NEWS_CSV_PATH = os.path.join(BASE_DIR, 'news.csv')

class AstroEventsEmitter:
    def __init__(self):
        self._listeners = []
    def subscribe(self, listener):
        self._listeners.append(listener)
    def unsubscribe(self, listener):
        self._listeners.remove(listener)
    def emit(self, data):
        for listener in self._listeners:
                listener(data)

def notification(data):
    print(f"Подія: {data['info']}")
    print(f"Дата: {data['day']} {data['month']} {data['year']}")

def news(file_path, emitter):
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f) 
            for row in reader:
                emitter.emit(row)
    except FileNotFoundError:
        print("Error")

def get_all_news(file_path):
    news_list = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                news_list.append(row)
    except FileNotFoundError:
        pass
    return news_list

if __name__ == "__main__":
    emitter = AstroEventsEmitter()
    emitter.subscribe(notification)
    try:
        while True:
            news(NEWS_CSV_PATH, emitter)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nPostponed")