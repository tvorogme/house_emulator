class HeatSource:
    def __init__(self, temperature: int, state: float, coefficient_effectiveness: float):
        """
        Абстракция над всем, что влияет на температуру в комнате

        :param temperature: до какого момента будет работать
        :param state: включен/выключен (число от 0 до 1) a.k.a. мощность работы
        :param coefficient_effectiveness: на сколько эффективно работает
        """
        self.temperature = temperature
        self.state = state
        self.coefficient_effectiveness = coefficient_effectiveness

    def room_influnce(self, room_temperature: float) -> float:
        '''
        Влияние источника тепла на температуру в комнате
        Пропарционально разнице между реальной температурой и желаемой
        :param room_temperature: температура комнаты
        :return: вклад тепла в производную температуры по времени
        '''
        return (self.temperature - room_temperature) * self.coefficient_effectiveness * self.state