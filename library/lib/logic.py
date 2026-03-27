# Підрахунок першої та другої астрономічної швидкості
import math 
#from memoization import LFU
from memoization import LRU
import time

G = 6.67430e-11

def calculate_v1(mass, radius):
    time.sleep(2)
    return round(math.sqrt((G*mass)/radius), 2)

def calculate_v2(mass, radius):
    time.sleep(2)
    return round(math.sqrt((2*G*mass)/radius), 2)

# Тимчасово для тестування
limit = 5

get_v1 = LRU(calculate_v1, max_size=limit, ttl=300) # Умови за яких результат в рамках часу 
get_v2 = LRU(calculate_v2, max_size=limit, ttl=300)

#get_v1 = LFU(calculate_v1, max_size=limit, ttl=300) 
#get_v2 = LFU(calculate_v2, max_size=limit, ttl=300)

while True:
    print(f"\nПоточний кеш:{len(get_v1.cache)}/{limit}")
    m = float(input("Введіть масу планети (кг): "))
    r = float(input("Введіть радіус планети (м): "))

    start_time = time.time()
    key = (m, r)
    v1 = get_v1.get(key)
    if v1 is None:
        v1 = calculate_v1(m, r)
        get_v1.put(key, v1)

    v2 = get_v2.get(key)
    if v2 is None:
        v2 = calculate_v2(m, r)
        get_v2.put(key, v2)

    duration = time.time() - start_time

    print(f"Перша космічна швидкість: {v1} м/с ")
    print(f"Друга космічна швидкість: {v2} м/с ")
    print(f"Час виконання: {duration:.2f} сек")

   




