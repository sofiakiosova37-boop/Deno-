import time
from collections import OrderedDict #Для роботи з кешом і для реалізації LRU

class LRU:
# метод для роботи з кешом. Це конструктор з даними, які я буду надалі використовувати
    def __init__(self, func, max_size=None, ttl=None): # запис методу з параметрами, максимальний розмір кешу(кількість запитів), ttl параметр часу(за замовчеванням обмеження немає)
        self.func = func # Функція, яку ми обгортаємо
        self.cache = OrderedDict() # масив/список з кешом, Сховище. Ключи - аргументи функції
        self.max_size = max_size # Ліміт на кількість записів у кеші.
        self.ttl = ttl  # ttl — Time To Live, запису в секундах.
        self.timestamps = {} # time of adding

    def get(self, key):
        if key not in self.cache:
            return None
        if time.time() is not None:
            if time.time() - self.timestamps[key] > self.ttl:
                del self.cache[key]
                del self.timestamps[key]
                return None
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    
    def put(self, key, value):
          if key in self.cache:
              self.cache.move_to_end(key)
          self.cache[key] = value
          if len(self.cache) > self.max_size:
              self.cache.popitem(last=False)
              
    
class LFU:
    def __init__(self, func, max_size=None, ttl=None):
        self.func = func
        self.max_size = max_size
        self.ttl = ttl
