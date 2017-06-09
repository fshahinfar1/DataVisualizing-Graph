import pygame


class Dragable:

    def __init__(self, pos, name, img, drop_function):
        self.__position = pos  # type: tuple  description: center of drawn img
        self.__name = name  # type: str
        self.__img = img  # type: pygame.Surface
        self.__img_size = self.__img_width, self.__img_height = self.__img.get_size()
        self.__flag_selected = False
        self.__on_drop = drop_function

    def get_position(self):
        return self.__position

    def get_name(self):
        return self.__name

    def set_position(self, value):
        self.__position = value

    def change_selected(self, value=None):
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

    def loop(self, mouse_state):
        if mouse_state == "clicked": #pygame.mouse.get_pressed()
            if self.position_on_object(pygame.mouse.get_pos()):
                if not self.__flag_selected:
                    self.__flag_selected = True
        elif mouse_state == "release":
            if self.__flag_selected:
                self.__flag_selected = False
                self.__on_drop()


        if self.__flag_selected:
            self.__position = pygame.mouse.get_pos()




    def draw(self, screen):
        left_corner = self.__position[0] - self.__img_width // 2 \
        , self.__position[1] - self.__img_height // 2
        screen.blit(self.__img, left_corner)
