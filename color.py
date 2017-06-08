class Color:
    count = 0

    def __init__(self, name, value):
        """
        @param: name: type: str
        @param: value: type: tuple
        """
        self.__id = Color.count  # type: int
        Color.count += 1
        self.__name = name  # type: str
        self.__value = value  # type: tuple

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

### constant vaules
Black = Color('Black', (0, 0, 0))
White = Color('White', (255, 255, 255))
Red = Color('Red', (255, 0, 0))
Green = Color('Green', (0, 255, 0))
Blue = Color('Blue', (0, 0, 255))
