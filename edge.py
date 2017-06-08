import color
import vertex
from pygame import Surface, draw

class Edge:

    def __init__(self, id, source, destination, color=color.Black):
        """
        :type id: int
        :type source: vertex.Vertex
        :type destination: vertex.Vertex
        :type color: color.Color
        """
        self__id = id  # type: int
        self.__source = source  # type: vertex.Vertex
        self.__destination = destination  # type: vertex.Vertex
        self.__color = color  # type: color.Color

    def draw(self, screen):
        draw.line(screen, self.__color.get_value()\
        , self.__source.get_position(), self.__destination.get_position()\
        , 5)
