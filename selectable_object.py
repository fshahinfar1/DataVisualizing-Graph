import pygame


class SelectionMode:
    Default = 0
    Dragable = 1

class Selectable:

    def __init__(self, pos, img, selection_mode=SelectionMode.Default):
        self.__position = pos  # type: tuple  description: center of drawn img
        self.__img = img  # type: pygame.Surface
        self.__img_size = self.__img_width, self.__img_height = self.__img.get_size()
        self.__flag_selected = False
        self.__selection_mode = selection_mode

    def get_position(self):
        return self.__position

    def set_position(self, value):
        self.__position = value

    def set_selected(self, value=None):
        if value is None:
            value = not self.__flag_selected
        self.__flag_selected = value

    def position_on_object(self, pos):
        left_corner = self.__position[0] - self.__img_width // 2 \
        , self.__position[1] - self.__img_height // 2
        if pos[0] > left_corner[0] and pos[0] < left_corner[0]+self.__img_width:
            if pos[1] > left_corner[1] and pos[1] < left_corner[1]+self.__img_height:
                return True
        return False

    def is_selected(self):
        return self.__flag_selected

    def get_img_size(self):
        return self.__img_size

    def get_img(self):
        return self.__img

    def on_clicked(self):
        print("ON Click")

    def on_release(self):
        print("ON Release")

    def on_unselected(self):
        print("ON Unselected")

    def loop(self, mouse_state):
        # print("selectable object's Loop")
        if mouse_state == "clicked":
            if self.position_on_object(pygame.mouse.get_pos()):
                self.on_clicked()
                self.set_selected(True) # True
        elif mouse_state == "release":
            if self.is_selected():
                self.on_release()
                self.on_unselected()
                self.set_selected(False)
