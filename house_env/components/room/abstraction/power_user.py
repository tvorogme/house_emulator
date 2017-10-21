from .metric import Metric
from .item import Item


class PowerUser(Item):
    intake = Metric(0., float)
    power_consumment = Metric(0., float)
    state = Metric(0., float)

    def __init__(self,room, power_consumment: float, state: float, **kwargs):
        super().__init__(room, **kwargs)

        self.power_consumment.value = power_consumment
        self.state.value = state

    def tick(self) -> None:
        self.intake.value = self.power_consumment.value * self.state.value
        self._influences[self.room.house.total_consumment] = self.intake.value
