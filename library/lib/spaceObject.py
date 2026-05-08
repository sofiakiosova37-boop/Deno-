"""class SpaceObject:
    def __init__(self, name, body_type, magnitude, ra, dec):
        self.name = name
        self.body_type = body_type
        self.magnitude = magnitude
        self.priority = 0
        self.ra = ra   # довгота
        self.dec = dec # широта
        self.timestamp = 0

class BiDirectionalPriorityQueue:
    def __init__(self):
        self._elements = []
        self._counter = 0

    # Розрахунок пріорітету
    def _calculate_priority(self, obj):
        priority = 10 - obj.magnitude
        if obj.dec > 45:
            priority += 5
        elif obj.dec < 0:
            priority -= 3
        if obj.body_type == "Planet":
            priority += 7
        elif obj.body_type == "Constellation":
            priority += 2
        return priority

    def enqueue(self, obj):
        obj.priority = self._calculate_priority(obj)
        obj.timestamp = self._counter
        self._counter += 1
        self._elements.append(obj)
        print(f"-> Додано: {obj.name}")

    def _get_best_index(self, mode):
        if not self._elements:
            raise IndexError("Queue is empty")
        if mode not in ["highest", "lowest", "oldest", "newest"]:
            raise ValueError("Unknown mode")
        target_idx = 0
        for i in range(1, len(self._elements)):
            current = self._elements[i]
            best = self._elements[target_idx]
            if mode == "highest" and current.priority > best.priority:
                target_idx = i
            elif mode == "lowest" and current.priority < best.priority:
                target_idx = i
            elif mode == "oldest" and current.timestamp < best.timestamp:
                target_idx = i
            elif mode == "newest" and current.timestamp > best.timestamp:
                target_idx = i
        return target_idx

    def peek(self, mode="highest"):
        idx = self._get_best_index(mode)
        if idx is not None:
            obj = self._elements[idx]
            print(f"[PEEK] {mode}: {obj.name}")
            return obj
        return None
            
    def dequeue(self, mode="highest"):
        idx = self._get_best_index(mode)
        if idx is not None:
            target = self._elements.pop(idx)
            print(f"[DEQUEUE] {mode}: {target.name}")
            return target
        return None
            
    def display(self):
        print("\nПоточна черга:")
        for obj in self._elements:
            print(f"- {obj.name} (Тип: {obj.body_type}, Пріоритет: {obj.priority:.2f})")

queue = BiDirectionalPriorityQueue()
queue.enqueue(SpaceObject("Sirius", "Star", -1.46, 1, 6.75, -16.7))
queue.enqueue(SpaceObject("Jupiter", "Planet", -2.50, 2, 18.5, -23.0))
queue.enqueue(SpaceObject("Aldebaran", "Star", +0.85, 3, 4.60, +16.5))
queue.enqueue(SpaceObject("Cassiopeia", "Constellation", +2.00, 4, 1.00, +60.0))
queue.enqueue(SpaceObject("Mars", "Planet", -0.50, 5, 15.2, -18.0))
queue.display()"""