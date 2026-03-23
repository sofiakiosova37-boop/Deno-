# Підрахунок першої та другої астрономічної швидкості
import math 
from memoization import Memoize
import time

G = 6.67430e-11

def calculate_v1(mass, radius):
    time.sleep(2)
    return round(math.sqrt((G*mass)/radius), 2)

def calculate_v2(mass, radius):
    time.sleep(2)
    return round(math.sqrt((2*G*mass)/radius), 2)

# Тимчасово для тестування
start = input("Оберіть стратегію (LRU / LFU / custom): ").strip()
limit = 3 

get_v1 = Memoize(calculate_v1, max_size=limit, ttl=180, strategy=start) # Умови за яких результат в рамках часу -180 секуед - 3 хв та максимальний об'єм 20 планет
get_v2 = Memoize(calculate_v2, max_size=limit, ttl=180, strategy=start)

while True:
    print(f"\nПоточний кеш: {list(get_v1.cache.keys())}")
    m = float(input("Введіть масу планети (кг): "))
    r = float(input("Введіть радіус планети (м): "))

    start_time = time.time()
    v1 = get_v1(m, r)
    end_time = time.time()

    # v1 = get_v1(m, r)
    # v2 = get_v2(m, r)

    print(f"Перша космічна швидкість: {v1} м/с (Час виконання: {end_time - start_time:.2f} сек)")
    print(f"Друга космічна швидкість: {v2} м/с (Час виконання: {end_time - start_time:.2f} сек)")

    # v12 = get_v1(m, r)
    # v22 = get_v2(m, r)
   




