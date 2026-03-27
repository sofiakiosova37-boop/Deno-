import time
from collections import OrderedDict #Для роботи з кешом і для реалізації LRU

class LRU:
# метод для роботи з кешом. Це конструктор з даними, які я буду надалі використовувати
    def __init__(self, func, max_size=None, ttl=None): # запис методу з параметрами, максимальний розмір кешу(кількість запитів), ttl параметр часу(за замовчеванням обмеження немає)
        self.func = func # Функція, яку ми обгортаємо -- для використання в коді з обрахуванням
        self.cache = OrderedDict() # масив/список з кешом, Сховище. Ключи - аргументи функції
        self.max_size = max_size # Ліміт на кількість записів у кеші.
        self.ttl = ttl  # ttl — Time To Live, запису в секундах.
       # self.timestamps = {} # time of adding. 
        self.metadata = {}

    def get(self, key): 
        if key not in self.cache: 
            return None 
        if self.ttl is not None: 
            if time.time() - self.metadata[key]['timestamp'] > self.ttl: 
                del self.cache[key] 
                del self.metadata[key] 
                return None 
        self.metadata[key]['timestamp'] = time.time()
        self.metadata[key]['count'] += 1

        self.cache.move_to_end(key) 
        return self.cache[key] 
    
    def put(self, key, value):
          if key in self.cache: 
              self.cache.move_to_end(key) 
              self.metadata[key]['timestamp'] = time.time()
          else:
              self.metadata[key] = {
                'timestamp': time.time(),
                'count': 0
              }
          self.cache[key] = value
          if self.max_size is not None:
            if len(self.cache) > self.max_size: 
              oldest_key, _ = self.cache.popitem(last=False) 
              if oldest_key in self.metadata: 
                del self.metadata[oldest_key] 
              
