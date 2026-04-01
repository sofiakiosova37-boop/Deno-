import time

class SpaceObject:
    def __init__(self, name, body_type, magnitude, timestamp, ra, dec):
        self.name = name
        self.body_type = body_type
        self.magnitude = magnitude
        self.timestamp = timestamp
        self.priority = 0
        self.ra = ra   # Сходження (в годинах або градусах)
        self.dec = dec # градуси нахилу

    elements = [
        sirius = SpaceObject("Sirius", "Star", -1.46, current_time, 6.75, -16.7),
        jupiter = SpaceObject("Jupiter", "Planet", -2.50, current_time, 18.5, -23.0),
        aldebaran = ("Aldebaran", "Star", +0.85, current_time, 4.60, +16.5),
        cassiopeia = ("Cassiopeia", "Constellation", +2.00, current_time, 1.00, +60.0),
        mars = SpaceObject("Mars", "Planet", -0.50, current_time, 15.2, -18.0),
    ]