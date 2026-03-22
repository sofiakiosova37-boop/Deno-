# Підрахунок першої та другої астрономічної швидкості
import math 

def calculate_v1(mass, radius):
    G = 6.67430e-11
    return math.sqrt((G*mass)/radius)

def calculate_v2(mass, radius):
    G = 6.67430e-11
    return math.sqrt((2*G*mass)/radius)

# Тимчасово для тестування
# m = float(input("Введіть масу планети (кг): "))
# r = float(input("Введіть радіус планети (м): "))

# v1 = calculate_v1(m, r)
# v2 = calculate_v2(m, r)

# print(f"Перша космічна швидкість: {v1:.2f} м/с")
# print(f"Друга космічна швидкість: {v2:.2f} м/с")

# # Результат
#  python library/lib/logic.py
# Введіть масу планети (кг): 5.97e24
# Введіть радіус планети (м): 6371000
# Перша космічна швидкість: 7908.36 м/с
# Друга космічна швидкість: 11184.10 м/с
# (.venv) PS D:\lab OP 2 sem\лаба 2> 