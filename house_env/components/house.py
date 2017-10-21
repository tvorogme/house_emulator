from .room.abstraction import Metric


class House:
    total_consumment = Metric(0., float)

    rooms = []

    def __int__(self, rooms=[]):
        for room in rooms:
            room.house = self
