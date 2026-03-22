import time
from collections import OrderedDict #Для роботи з кешом і для реалізації LRU

class Memoize:

# функції для роботи з кешом
    def __cache__(self, func, max_size=10, ttl=None): # запис функції з параметрами, максимальний розмір кешу(кількість запитів), ttl параметр часу(за замовчеванням обмеження немає)
        self.func = func
        self.cache = OrderedDict() # масив/список з кешом
        self.max_size = max_size
        self.ttl = ttl  

