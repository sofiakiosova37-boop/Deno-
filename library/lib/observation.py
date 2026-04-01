import time

class SpaceObject:
    def __init__(self, name, body_type, magnitude, timestamp, ra, dec):
        self.name = name
        self.body_type = body_type
        self.magnitude = magnitude
        self.timestamp = timestamp
        self.priority = 0
        self.ra = ra   # довгота
        self.dec = dec # широта
        self.timestamp = time.time()

current_time = 0

elements = [
        SpaceObject("Sirius", "Star", -1.46, 1, 6.75, -16.7),
        SpaceObject("Jupiter", "Planet", -2.50, 2, 18.5, -23.0),
        SpaceObject("Aldebaran", "Star", +0.85, 3, 4.60, +16.5),
        SpaceObject("Cassiopeia", "Constellation", +2.00, 4, 1.00, +60.0),
        SpaceObject("Mars", "Planet", -0.50, 5, 15.2, -18.0),
    ]

for star in elements:
    star.priority = 10 - star.magnitude
    if star.dec > 50:
        star.priority += 5

best_object = max(elements, key=lambda x: x.priority)
worst_object = min(elements, key=lambda x: x.priority)
print(f"Найкращий для спостереження:", best_object.name)
print(f"Найменш актуальний об'єкт:", worst_object.name)

elements.remove(best_object)
target = elements.pop(0)
print(f"Вилучено найстаріший об'єкт (FIFO): {target.name}")
last_added = elements.pop()
print(f"Вилучено найновіший об'єкт (LIFO): {last_added.name}")

print("-" * 30)
print(f"Зараз у черзі залишилося об'єктів: {len(elements)}")

for obj in elements:
    print(f"- {obj.name} (Тип: {obj.body_type}, Пріоритет: {obj.priority:.2f})")