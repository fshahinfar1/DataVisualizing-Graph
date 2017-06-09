import color
import selectable_object
from pygame import Surface, draw, font

font.init()
font = font.SysFont("arial", 16)


class Vertex(selectable_object.Selectable):

    def __init__(self, id, pos, color=color.Black):
        """
        :param id:
        :param pos:
        :param color:
        :type id: int
        :type pos: tuple
        :type color: color.Color
        """
        img = Surface((20,20))
        selectable_object.Selectable.__init__(self, pos, img)
        self.__id = id  # type: int
        self.__position = pos  # type: tuple
        self.__color = color  # type: Color
        # todo: working on the degree
        self.__degree_in = 0  # type: int
        self.__degree_out = 0  # type: int
        self.__radius = 10  # type: int

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_position(self):
        return self.__position

    def get_radius(self):
        return self.__radius

    def set_radius(self, val):
        if val > 1:
            val = int(val)
            self.__radius = val

    def get_degree_in(self):
        return self.__degree_in

    def get_degree_out(self):
        return self.__degree_out

    def add_degree_in(self):
        self.__degree_in += 1

    def add_degree_out(self):
        self.__degree_out += 1

    def on_clicked(self):
        self.__color = color.Red
        print('clicked')

    def on_release(self):
        self.__color = color.Black

    def draw(self, screen):
        """
        :param self
        :param screen: game window
        :type screen: Surface
        """
        draw.circle(screen, self.__color.get_value(), self.__position, self.__radius)
        degree_text = font.render(str(self.__degree_in)+"/"+str(self.__degree_out), True, color.Blue.get_value())
        screen.blit(degree_text, self.__position)
