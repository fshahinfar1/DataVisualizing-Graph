import Graph.graph
from Graph.color import *
from Graph.selectable_object import *
from pygame import Surface, draw, font, mouse

font.init()
font = font.SysFont("arial", 16)


class Vertex(Selectable):

    def __init__(self, id, pos, graph, color=Black):
        """
        :param id:
        :param pos:
        :param color:
        :type id: int
        :type pos: tuple
        :type color: color.Color
        """
        img = Surface((20,20))
        Selectable.__init__(self, pos, img)
        self.__id = id  # type: int
        self.__position = pos  # type: tuple
        self.__color = color  # type: Color
        # todo: working on the degree
        self.__degree_in = 0  # type: int
        self.__degree_out = 0  # type: int
        self.__radius = 10  # type: int
        self.__graph = graph  # type: Graph.graph.Graph

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
        self.__color = Red
        print('clicked')

    def on_unselected(self):
        self.__color = Black

    def loop(self, mouse_state):
        if mouse_state == "clicked":
            if self.position_on_object(mouse.get_pos()):
                self.set_selected(True)
                for v in self.__graph.get_vertices():
                    if v.is_selected() and v is not self:
                        v.set_selected(False)
                        v.on_unselected()
                        print("un selecte")
                        break
                self.on_clicked()

    def draw(self, screen):
        """
        :param self
        :param screen: game window
        :type screen: Surface
        """
        draw.circle(screen, self.__color.get_value(), self.__position, self.__radius)
        degree_text = font.render(str(self.__degree_in)+"/"+str(self.__degree_out), True, Blue.get_value())
        screen.blit(degree_text, self.__position)
