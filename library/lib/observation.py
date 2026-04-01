import time

class SpaceObject:
    def __init__(self, name, body_type, magnitude, timestamp):
        self.name = name
        self.body_type = body_type
        self.magnitude = magnitude
        self.timestamp = timestamp
        self.priority = 0