from color import *
from vertex import Vertex
import graph
from selectable_object import SelectableAbstract
import math
import pygame
from pygame import Surface, draw, image, transform, mouse, font
import position

dir_img = image.load("img/dir.png")  # type: Surface

SELECTED_COLOR = Red
HOVER_COLOR = Green
DEFAULT_COLOR = Black

font.init()
font = font.SysFont("arial", 16)

class Edge(SelectableAbstract):

    def __init__(self, id, graph, source, destination, val=0, color=Black):
        """
        :type id: int
        :type source: vertex.Vertex
        :type destination: vertex.Vertex
        :type color: color.Color
        """
        self.__id = id  # type: int
        self.__source = source  # type: vertext.Vertex
        self.__destination = destination  # type: vertext.Vertex
        self.__color = color  # type: color.Color
        self.__value = val
        self.__vertical = False
        print(self.__source.position)
        self.__range_y = sorted((self.__source.position[1], self.__destination.position[1]))
        self.__graph = graph # type: graph.Graph
        source.add_degree_out()
        destination.add_degree_in()
        self.set_selectable_properties()

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

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

    @color.setter
    def color(self, c):
        self.__color = c

    def set_selectable_properties(self):
        #s_width = position.distance(source.get_pos(), destination.get_pos())
        #s_rotation = position.direction(source.get_pos(), destination.get_pos())
        try:
            s_m = position.slope(self.__source.position, self.__destination.position)
        except:
            s_m = 0
            self.__vertical = True
        s_range = tuple(sorted((self.__source.position[0], self.__destination.position[0])))
        SelectableAbstract.__init__(self, self.__source.position, 10, s_range, s_m)

    def on_clicked(self):
        self.__color = SELECTED_COLOR

    def on_unselected(self):
        self.__color = DEFAULT_COLOR

    def on_hover(self):
        self.__color = HOVER_COLOR
        if pygame.key.get_pressed()[pygame.K_DELETE]:
            self.__graph.remove_edge(self.id)

    def on_mouse_leave(self):
        if self.is_selected():
            self.__color = SELECTED_COLOR
        else:
            self.__color = DEFAULT_COLOR

    def on_right_clicked(self):
        self.value = int(input("Value: "))

    def is_in_range_y(self, y):
        return y >= self.__range_y[0] and y <= self.__range_y[1]

    def position_on_object(self, pos):
        x0, y0 = self._position
        x, y = pos
        if not self.__vertical:
            # y = mx + k
            k = y0 - self._m * x0
            dist = abs(k + self._m * x - y) / math.sqrt(1+self._m**2)
        else:
            dist = abs(x0 - x)
        #  y == (x - x0)* self.__m + y0) and (self.is_in_range(x))
        if (dist <= self._range) and (self.is_in_range(x) or (self.__vertical and self.is_in_range_y(y))):
            return True
        return False


    def loop(self, mouse_state):
        if self.position_on_object(mouse.get_pos()):
            if mouse_state == "clicked":
                print(mouse.get_pressed())
                if mouse.get_pressed()[2]:
                    self.on_right_clicked()
                if(pygame.key.get_pressed()[pygame.K_LSHIFT]):
                    print("shift_clicked")
                else:
                    t = self.__graph.adjacent_vertices
                    for edges in t.values() :
                        for edge in edges:
                            if edge.is_selected() and edge is not self:
                                edge.set_selected(False)
                                edge.on_unselected()
                                break
                    self.set_selected(True)
                    self.on_clicked()
            else:
                self._flag_hover = True
                self.on_hover()
        elif self.hover:
            self._flag_hover = False
            self.on_mouse_leave()

    def draw(self, screen):
        pos_a = self.__source.position
        pos_b = self.__destination.position
        draw.line(screen, self.__color.get_value()\
        , pos_a, pos_b, 5)
        mid_point =((pos_a[0]+pos_b[0])//2, (pos_a[1]+pos_b[1])//2)
        angle = 360 - math.degrees(math.atan2(pos_b[1]-pos_a[1], pos_b[0]-pos_a[0]))
        img = transform.rotozoom(dir_img, angle, 0.075)
        img_width, img_height = img.get_size()
        left_corner = (mid_point[0]-img_width//2, mid_point[1]-img_height//2)

        screen.blit(img, left_corner)
        val_text = font.render(str(self.__value),  True, Blue.get_value(), White.get_value())
        screen.blit(val_text, left_corner)
