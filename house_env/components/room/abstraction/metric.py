class Metric:
    _value = None
    _type = None
    _nonable = False

    def __init__(self, value=None, custom_type=None, nonable: bool =False):
        '''
        :param value: значение метрики
        :param custom_type: тип значения метрики
        '''

        self._nonable = nonable
        if custom_type:
            self._type = custom_type
        else:
            self._type = type(value)
        if value is not None:
            self.value = value

    @property
    def value(self) -> object:
        '''
        returns the metric value
        :return: metric value =)
        '''
        if not self._nonable and self._value is None:
            raise UnboundLocalError("Value is not set to this metric")
        return self._value

    @value.setter
    def value(self, value) -> None:

        if isinstance(value, self._type) or (self._nonable and value is None):
            self._value = value
        else:
            raise ValueError("setting different type to a value")

