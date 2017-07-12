import Graph.graph
import pygame
from Graph.color import *
from Graph.selectable_object import *
from pygame import Surface, draw, font, mouse

font.init()
font = font.SysFont("arial", 16)

SELECTED_COLOR = Red
HOVER_COLOR = Green
DEFAULT_COLOR = Black

class Vertex(Selectable):

    def __init__(self, id, pos, graph, color=DEFAULT_COLOR):
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
        self.__color = color  # type: Color
        # todo: working on the degree
        self.__degree_in = 0  # type: int
        self.__degree_out = 0  # type: int
        self.__radius = 10  # type: int
        self.__graph = graph  # type: Graph.graph.Graph

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def radius(self):
        return self.__radius

    def set_radius(self, val):
        if val > 1:
            val = int(val)
            self.__radius = val

    @property
    def degree_in(self):
        return self.__degree_in

    @property
    def degree_out(self):
        return self.__degree_out

    def add_degree_in(self):
        self.__degree_in += 1

    def add_degree_out(self):
        self.__degree_out += 1

    def on_clicked(self):
        self.__color = SELECTED_COLOR

    def on_unselected(self):
        self.__color = DEFAULT_COLOR

    def on_hover(self):
        self.__color = HOVER_COLOR

    def on_mouse_leave(self):
        if self.is_selected():
            self.__color = SELECTED_COLOR
        else:
            self.__color = DEFAULT_COLOR

    def loop(self, mouse_state):
        if self.position_on_object(mouse.get_pos()):
            if mouse_state == "clicked":
                if(pygame.key.get_pressed()[pygame.K_LSHIFT]):
                    print("Shift")
                    for v in self.__graph.get_vertices():
                        if v.is_selected() and v is not self:
                            self.__graph.add_edge(v, self)
                else:
                    print("no Shift")
                    self.set_selected(True)
                    for v in self.__graph.get_vertices():
                        if v.is_selected() and v is not self:
                            v.set_selected(False)
                            v.on_unselected()
                            print("un selecte")
                            break
                    self.on_clicked()
            else:
                self._flag_hover = True
                self.on_hover()
        elif self.hover:
            self._flag_hover = False
            self.on_mouse_leave()



    def draw(self, screen):
        """
        :param self
        :param screen: game window
        :type screen: Surface
        """
        draw.circle(screen, self.__color.get_value(), self.position, self.__radius)
        degree_text = font.render(str(self.degree_in)+"/"+str(self.degree_out), True, Blue.get_value())
        screen.blit(degree_text, self.position)
