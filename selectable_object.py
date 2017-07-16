import pygame


class SelectionMode:
    Default = 0
    Dragable = 1


class Selectable(object):
    def __init__(self, pos, img, selection_mode=SelectionMode.Default):
        #  description: center of drawn img
        self.position = pos  # type: tuple
        self.__img = img  # type: pygame.Surface
        self.__img_width, self.__img_height = self.__img.get_size()
        self.__flag_selected = False
        self._flag_hover = False
        self.__selection_mode = selection_mode

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value,(list, tuple)):
            value = tuple(value)
            self.__position = value
        else:
            print(type(value))
            raise TypeError("position ... !!")

    def set_selected(self, value=None):
        if value is None:
            value = not self.__flag_selected
        self.__flag_selected = value

    def position_on_object(self, pos):
        left_corner = self.position[0] - self.__img_width // 2 \
            , self.position[1] - self.__img_height // 2
        if pos[0] > left_corner[0] and pos[0] < left_corner[0] + self.__img_width:
            if pos[1] > left_corner[1] and pos[1] < left_corner[1] + self.__img_height:
                return True
        return False

    @property
    def image_width(self):
        return self.__img_width

    @property
    def image_height(self):
        return self.__img_height

    @property
    def image_size(self):
        return tuple(self.image_width, self.image_height)

    def is_selected(self):
        return self.__flag_selected

    @property
    def hover(self):
        return self._flag_hover

    def on_clicked(self):
        print("ON Click super")

    def on_release(self):
        print("ON Release")

    def on_unselected(self):
        print("ON Unselected")

    def loop(self, mouse_state):
        # print("selectable object's Loop")
        if self.__selection_mode is SelectionMode.Default:
            if mouse_state == "clicked":
                if self.position_on_object(pygame.mouse.get_pos()):
                    self.on_clicked()
        elif self.__selection_mode is SelectionMode.Dragable:
            if mouse_state == "clicked":
                if self.position_on_object(pygame.mouse.get_pos()):
                    self.on_clicked()
                    self.set_selected(True)  # True
            elif mouse_state == "release":
                if self.is_selected():
                    self.on_release()
                    self.on_unselected()
                    self.set_selected(False)


    def draw(self, screen):
        """
        :type: screen: pygame.Surface
        :param screen:
        :return:
        """
        left_corner = (self.position[0] - self.image_width // 2, self.position[1] - self.image_height // 2)
        screen.blit(self.__img, left_corner)
