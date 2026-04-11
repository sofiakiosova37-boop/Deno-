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

class BiDirectionalPriorityQueue:
    def __init__(self):
        self._elements = []

# Розрахунок пріорітету
def _calculate_priority(self, obj):
    priority = 10 - obj.magnitude
    if obj.dec > 50:
        priority += 5
    return priority

def enqueue(self, obj):
    obj.priority = self._calculate_priority(obj)
    self._elements.append(obj)
    print(f"-> Додано: {obj.name}")

def display(self):
    print("\nПоточна черга:")
    for obj in self.elements:
        print(f"- {obj.name} (Тип: {obj.body_type}, Пріоритет: {obj.priority:.2f})")

queue = BiDirectionalPriorityQueue()
queue.enqueue(SpaceObject("Sirius", "Star", -1.46, 1, 6.75, -16.7))
queue.enqueue(SpaceObject("Jupiter", "Planet", -2.50, 2, 18.5, -23.0))
queue.enqueue(SpaceObject("Aldebaran", "Star", +0.85, 3, 4.60, +16.5))
queue.enqueue(SpaceObject("Cassiopeia", "Constellation", +2.00, 4, 1.00, +60.0))
queue.enqueue(SpaceObject("Mars", "Planet", -0.50, 5, 15.2, -18.0))
queue.display()