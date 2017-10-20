from house_env.components.room import Room

class HeatSource:
    def __init__(self, temperature: int, state: float, coefficient_effectiveness: float, room: Room):
        """
        Абстракция над всем, что влияет на температуру в комнате

        :param temperature: до какого момента будет работать
        :param state: включен/выключен (число от 0 до 1) a.k.a. мощность работы
        :param coefficient_effectiveness: на сколько эффективно работает
        :param room: комната родитель
        """
        self.temperature = temperature
        self.state = state
        self.coefficient_effectiveness = coefficient_effectiveness
        self.room = room

    def room_influnce(self) -> float:
        '''
        Влияние источника тепла на температуру в комнате
        Пропарционально разнице между реальной температурой и желаемой
        :return: вклад тепла в производную температуры по времени
        '''
        return (self.temperature - self.room.temp) * self.coefficient_effectiveness * self.state