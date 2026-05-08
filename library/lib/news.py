import csv
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'news.csv')

class AstroEventsEmitter:
    def __init__(self):
        self._listeners = {}