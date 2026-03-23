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

get_v1 = Memoize(calculate_v1, max_size=20, ttl=180) # Умови за яких результат в рамках часу -180 секуед - 3 хв та максимальний об'єм 20 планет
get_v2 = Memoize(calculate_v2, max_size=20, ttl=180)

# Тимчасово для тестування
while True:
    m = float(input("Введіть масу планети (кг): "))
    r = float(input("Введіть радіус планети (м): "))

    v1 = get_v1(m, r)
    v2 = get_v2(m, r)

    print(f"Перша космічна швидкість: {v1} м/с")
    print(f"Друга космічна швидкість: {v2} м/с")

    v12 = get_v1(m, r)
    v22 = get_v2(m, r)
   




