import pygame
import Graph.graph
from Graph.selectable_object import *


class Dragable(Selectable):

    def __init__(self, pos, name, img):
        Selectable.__init__(self, pos, img, SelectionMode.Dragable)
        self.__origin_position = pos  # type: tuple  description: center of drawn img
        self.__name = name  # type:

    def _drop_function(self):
        print("Dragable's drop_function")

    @property
    def name(self):
        return self.__name

    def on_unselected(self):
        self._drop_function()
        self.position = self.__origin_position

    def loop(self, mouse_state):
        super(Dragable, self).loop(mouse_state)  # Do what is in the parent
        if self.is_selected():
            self.position = pygame.mouse.get_pos()

    # def draw(self, screen):
    #     position = self.position
    #     w, h = self.image_size
    #     left_corner = position[0] - w // 2, position[1] - h // 2
    #     screen.blit(self.get_img(), left_corner)


class DragableVertex(Dragable):
    def __init__(self, pos, name, img, graph):
        Dragable.__init__(self, pos, name, img)
        self.__graph = graph  # type: graph.Graph

    def _drop_function(self):
        print("DragableVertex's drop function")
        self.__graph.add_vertex(self.position)
        self.set_selected(False)
