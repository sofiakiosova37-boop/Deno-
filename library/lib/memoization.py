import time
from collections import OrderedDict #Для роботи з кешом і для реалізації LRU

class LRU:
# метод для роботи з кешом. Це конструктор з даними, які я буду надалі використовувати
    def __init__(self, func, max_size=None, ttl=None): # запис методу з параметрами, максимальний розмір кешу(кількість запитів), ttl параметр часу(за замовчеванням обмеження немає)
        self.func = func # Функція, яку ми обгортаємо
        self.cache = OrderedDict() # масив/список з кешом, Сховище. Ключи - аргументи функції
        self.max_size = max_size # Ліміт на кількість записів у кеші.
        self.ttl = ttl  # ttl — Time To Live, запису в секундах.
    
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




            
'''def __call__(self, *args):
        now = time.time() # зчитування поточного часу під час виклику методу
        # знайти в кеші 
        if args in self.cache: # чи є потрібний аргумент в списку кешу / чи збережений в пам'яті, тобто чи такий аргумент викликався раніше
            value, timestamp = self.cache[args] 
            if self.ttl is None or (now - timestamp) < self.ttl: # Або час невизначений або Різниця поточного та останнього менше ніж заданий термін оновлення, то йде переміщення
                self.cache.move_to_end(args)
                self.access_count[args] = self.access_count.get(args, 0) + 1 # Оновлення лічильника. Якщо вже викликали, то до старого номеру + 1 та записуємо до словника. Метод .get() це пошук у словнику
                print(f"CACHE HIT: {args} (Access count: {self.access_count[args]})")
                return value
            else:
                del self.cache[args] # видаляємо аргумент, якщо той не відповідає рядку про час
                if args in self.access_count: del self.access_count[args] # повне видалення пари ключ:значення
        print("CALCULATING:", args) 
        result = self.func(*args) # * значення виводиться не у вигляді масиву, просто набір значень, прибираємо [] 
        if self.max_size is not None and len(self.cache) >= self.max_size: # розмір масиву, поки не перевищує максимально заданий розмір
            if self.strategy == "LFU":
                need = min(self.access_count, key=self.access_count.get) # пошук мінімального значення, тобто в словнику де є пари ключ:значення програма звертає увагу на кількість їх викликів
                print(f"LFU REMOVE: {need}")
                del self.cache[need]
                del self.access_count[need] #  видалення з кешу та з лічильника
            elif self.strategy == "custom" and self.custom_func: #  коли вибрана користувацька стратегія і передана функція не є порожньою
                print("CUSTOM REMOVING...")
                self.custom_func(self.cache, self.access_count) # передача кеша та лічильника, аби користувач сам вирішував стратегію
            else: 
                print("LRU REMOVING...")
                self.cache.popitem(last=False) # видалення останнього значення, коли в масиві більше даних. Досягаємо мети реалізації LRU 
        self.cache[args] = (result, now) # відбувається сортування даних та перезапис з урахуванням нових даних. Те що було 4 стане 5
        self.access_count[args] = self.access_count.get(args, 0) + 1
        return result '''
