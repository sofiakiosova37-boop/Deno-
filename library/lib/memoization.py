import time
from collections import OrderedDict #Для роботи з кешом і для реалізації LRU

class LRU:
# метод для роботи з кешом. Це конструктор з даними, які я буду надалі використовувати
    def __init__(self, func, max_size=None, ttl=None): # запис методу з параметрами, максимальний розмір кешу(кількість запитів), ttl параметр часу(за замовчеванням обмеження немає)
        self.func = func # Функція, яку ми обгортаємо
        self.cache = {} # масив/список з кешом, Сховище. Ключи - аргументи функції
        self.max_size = max_size # Ліміт на кількість записів у кеші.
        self.ttl = ttl  # ttl — Time To Live, запису в секундах.
    
    def put(self, key, value):
          if len(self.cache) < self.max_size:
              self.cache[key] = value
          else:
              first_key = self.cache()[0]
              del self.cache[first_key]
              self.cache[key] = value
              
    def get(self, key):
        if key not in self.cache:
            return None
        else:
            self.cache.move_to_end(key)
        return self.cache[key]
    
class LFU:
    def __init__(self, func, max_size=None, ttl=None):
        self.func = func
        self.max_size = max_size
        self.ttl = ttl
