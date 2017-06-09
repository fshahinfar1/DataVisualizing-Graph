import pygame
import graph
import selectable_object


class Dragable(selectable_object.Selectable):

    def __init__(self, pos, name, img, drop_function=None):
        selectable_object.Selectable.__init__(self, pos, img)
        self.__origin_position = pos  # type: tuple  description: center of drawn img
        self.__name = name  # type:
        if drop_function is None:
            self.__on_drop = self.__drop_function
        else:
            self.__on_drop = drop_function

    def __drop_function():
        pass

    def get_name(self):
        return self.__name

    def loop(self, mouse_state):
        if mouse_state == "clicked": #pygame.mouse.get_pressed()
            if self.position_on_object(pygame.mouse.get_pos()):
                if not self.is_selected():
                    print('selected')
                    self.change_selected(True)
        elif mouse_state == "release":
            if self.is_selected():
                self.change_selected(False)
                # print(self.is_selected())
                self.__on_drop()
                print('drop')
                self.set_position(self.__origin_position)

        if self.is_selected():
            self.set_position(pygame.mouse.get_pos())

    def draw(self, screen):
        position = self.get_position()
        w, h = self.get_img_size()
        left_corner = position[0] - w // 2, position[1] - h // 2
        screen.blit(self.get_img(), left_corner)


class DragableVertex(Dragable):
    def __init__(self, pos, name, img, graph):
        Dragable.__init__(self, pos, name, img, self.__drop_function)
        self.__graph = graph  # type: graph.Graph


    def __drop_function(self):
        self.__graph.add_vertex(self.get_position())
