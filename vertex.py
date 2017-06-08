import color
from pygame import Surface, draw

class Vertex:

    def __init__(self, id, pos, color=color.Black):
        """
        :param id:
        :param pos:
        :param color:
        :type id: int
        :type pos: tuple
        :type color: color.Color
        """
        self.__id = id  # type: int
        self.__position = pos  # type: tuple
        self.__color = color  # type: Color

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_position(self):
        return self.__position

    def draw(self, screen):
        """
        :param self
        :param screen: game window
        :type screen: Surface
        """
        draw.circle(screen, self.__color.get_value(), self.__position, 10)
