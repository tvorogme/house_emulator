from ..room import Room
from .item import Item


class HeatSource(Item):
    def __init__(self, temperature: int, state: float, coefficient_effectiveness: float, room: Room, **kwargs):
        """
        Абстракция над всем, что влияет на температуру в комнате

        :param temperature: до какого момента будет работать
        :param state: включен/выключен (число от 0 до 1) a.k.a. мощность работы
        :param coefficient_effectiveness: на сколько эффективно работает
        :param room: комната родитель
        """

        super().__init__(room, **kwargs)

        self.temperature = temperature
        self.state = state
        self.coefficient_effectiveness = coefficient_effectiveness
        self.room = room

    def tick(self) -> None:
        '''
        Повлиять на комнату
        '''
        self._influences[self.room.temp] = self.room_influence()

    def room_influence(self) -> float:
        '''
        Влияние источника тепла на температуру в комнате
        Пропарционально разнице между реальной температурой и желаемой
        :return: вклад тепла в производную температуры по времени
        '''
        return (self.temperature - self.room.temp) * self.coefficient_effectiveness * self.state
