from ..room import Room


class Item:

    _influences = {}

    def __init__(self, room: Room, **kwargs):
        self.room = room

    def tick(self) -> None:
        pass

    def apply_influence(self) -> None:
        for appliant, value in self._influences:
            appliant.value += value
        self._influences = {}
