# Підрахунок першої та другої астрономічної швидкості
import math 

def calculate_v1(mass, radius):
    G = 6.67430e-11
    return math.sqrt((G*mass)/radius)

def calculate_v2(mass, radius):
    G = 6.67430e-11
    return math.sqrt((2*G*mass)/radius)

m = float(input("Введіть масу планети (кг): "))
r = float(input("Введіть радіус планети (м): "))

v1 = calculate_v1(m, r)
v2 = calculate_v2(m, r)

print(f"Перша космічна швидкість: {v1:.2f} м/с")
print(f"Друга космічна швидкість: {v2:.2f} м/с")