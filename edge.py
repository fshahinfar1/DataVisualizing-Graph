from Graph.color import *
from Graph.vertex import *
import math
from pygame import Surface, draw, image, transform

dir_img = image.load("img/dir.png")  # type: Surface


class Edge:

    def __init__(self, id, source, destination, color=Black):
        """
        :type id: int
        :type source: vertex.Vertex
        :type destination: vertex.Vertex
        :type color: color.Color
        """
        self.__id = id  # type: int
        self.__source = source  # type: Vertex
        self.__destination = destination  # type: Vertex
        self.__color = color  # type: Color
        source.add_degree_out()
        destination.add_degree_in()

    @property
    def id(self):
        return self.__id
    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def color(self):
        return self.__color

    def draw(self, screen):
        pos_a = self.__source.get_position()
        pos_b = self.__destination.get_position()
        draw.line(screen, self.__color.get_value()\
        , pos_a, pos_b, 5)
        mid_point =((pos_a[0]+pos_b[0])//2, (pos_a[1]+pos_b[1])//2)
        angle = 360 - math.degrees(math.atan2(pos_b[1]-pos_a[1], pos_b[0]-pos_a[0]))
        img = transform.rotozoom(dir_img, angle, 0.075)
        img_width, img_height = img.get_size()
        left_corner = (mid_point[0]-img_width//2, mid_point[1]-img_height//2)

        screen.blit(img, left_corner)
