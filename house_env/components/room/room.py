from .abstraction import Metric
from .abstraction import Item


class Room:
    """Датчики генерируют события в соответствии со своим назначением. Предлагаются следующие датчики:
            - температуры, влажности, (чистоты) воздуха, освещенности — они выдают численные значения;
            - пожарной сигнализации, открытия двери/окна, движения, протечек — они выдают единичные события;
            - исполнительные устройства: лампа, розетка, запорный водный клапан, обогреватель, кондиционер,
            универсальный механический актуатор, GSM модем."""

    items = []

    house = None

    # Float
    temp = Metric(custom_type=float)
    water = Metric(custom_type=float)
    clarity = Metric(custom_type=float)
    lightness = Metric(custom_type=float)

    # bool
    fire = Metric(custom_type=bool)
    movement = Metric(custom_type=bool)

    # Tuple[Boolean]
    windows = []
    doors = []

    _list_types = [(windows, bool), (doors, bool), (items, Item)]

    def _check_types(self) -> None:
        for _list, _type in self._list_types:

            for item in _list:
                if not isinstance(item, _type):
                    raise TypeError("All items must be {}, but {} found.".format(_type, type(item)))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        # Check types of windows and doors
        self._check_types()

    def update_openables(self, mode: str, index: int) -> None:
        if mode == "windows":
            iterator = self.windows
        elif mode == "doors":
            iterator = self.doors
        else:
            raise ValueError('No such mode')

        if index <= len(iterator):
            iterator[index] = not iterator[index]
        else:
            raise ValueError('No {} with such index'.format(mode))

    def tick(self, apply_influence: bool =True) -> None:
        '''
        runs a tick on all the items in the room
        :param apply_influence: applies the influence of the items if True
        '''
        for item in self.items:
            item.tick()

        if apply_influence:
            for item in self.items:
                item.apply_influence()

if __name__ == "__main__":
    Room(temp=0.8, water=0.1, clarity=0.0, lightness=0.9, fire=False, movement=False, windows=[True],
         doors=[False])
