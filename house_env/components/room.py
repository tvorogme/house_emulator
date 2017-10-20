from collections import defaultdict


class Room:
    """Датчики генерируют события в соответствии со своим назначением. Предлагаются следующие датчики:
            - температуры, влажности, (чистоты) воздуха, освещенности — они выдают численные значения;
            - пожарной сигнализации, открытия двери/окна, движения, протечек — они выдают единичные события;
            - исполнительные устройства: лампа, розетка, запорный водный клапан, обогреватель, кондиционер,
            универсальный механический актуатор, GSM модем."""

    # Python one love
    needed_types = defaultdict(lambda: None)

    # Float
    temp = None
    needed_types['temp'] = float

    water = None
    needed_types['water'] = float

    clarity = None
    needed_types['clarity'] = float

    lightness = None
    needed_types['lightness'] = float

    # bool
    fire = None
    needed_types['fire'] = bool

    movement = None
    needed_types['movement'] = bool

    # Tuple[Boolean]
    windows = []
    doors = []

    def _check_types(self, modes: tuple = ("windows", "doors")) -> None:
        for mode in modes:
            iterator = getattr(self, mode)
            for item in iterator:
                if not isinstance(item, bool):
                    raise TypeError(
                        "Key ({}) has not valid type. Must be bool, but it's {} now.".format(mode, type(item)))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, (type(getattr(self, key)), self.needed_types[key])):
                setattr(self, key, value)
            else:
                raise TypeError(
                    "Key ({}) has not valid type. Must be {}, but it's {} now.".format(key, type(getattr(self, key)),
                                                                                       type(value)))

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


if __name__ == "__main__":
    Room(temp=0.8, water=0.1, clarity=0.0, lightness=0.9, fire=False, movement=False, windows=[True],
         doors=[False])
