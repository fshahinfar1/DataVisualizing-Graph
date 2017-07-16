import pygame
from Graph.selectable_object import *

DEFAULT_BUTTON_IMAGE = pygame.image.load("img/btn.png")


class Button(Selectable):

    def __init__(self, pos, click_fun, img=DEFAULT_BUTTON_IMAGE):
        super(Button, self).__init__(pos, img, SelectionMode.Default)
        self.__click = click_fun

    def on_clicked(self):
        self.__click()


