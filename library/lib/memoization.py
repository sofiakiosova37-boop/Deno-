import time
from collections import OrderedDict #Для роботи з кешом і для реалізації LRU

class Memoize:

# функції для роботи з кешом
    def __init__(self, func, max_size=10, ttl=None): # запис методу з параметрами, максимальний розмір кешу(кількість запитів), ttl параметр часу(за замовчеванням обмеження немає)
        self.func = func
        self.cache = OrderedDict() # масив/список з кешом
        self.max_size = max_size
        self.ttl = ttl  

    def __call__(self, *args):
        now = time.time() # зчитування поточного часу під час виклику методу
        if args in self.cache: # чи є потрібний аргумент в списку кешу / чи збережений в пам'яті
            value, timestamp = self.cache[args] # створення 2 змінних + запис значення кешу для аргументу, масив з даними. Значення прив'язуються до часу 
            if self.ttl is None or (now - timestamp) < self.ttl: # Або час невизначений або Різниця поточного та останнього менше ніж заданий термін оновлення, то йде переміщення
                self.cache.move_to_end(args)
                print("CACHE HIT:", args)
                return value
            else:
                del self.cache[args] # видаляємо аргумент, якщо той не відповідає рядку 17
        print("CALCULATING:", args) 
        result = self.func(*args) # * значення виводиться не у вигляді масиву, просто набір значень, прибираємо [] 
        if len(self.cache) >= self.max_size: # розмір масиву, поки не перевищує максимально заданий розмір
            self.cache.popitem(last=False) # видалення останнього значення, коли в масиві більше даних. Досягаємо мети реалізації LRU 
        self.cache[args] = (result, now) # відбувається сортування даних та перезапис з урахуванням нових даних. Те що було 4 стане 5
        return result
