import pygame
import sys
from Graph.graph import Graph as G
from Graph.color import *
from Graph.dragable_object import *


pygame.init()

flag_run = True  # type: bool

screen_size = screen_width, screen_height = 450, 450  # type: tuple
screen = pygame.display.set_mode(screen_size)  #type: pygame.Surface
clock = pygame.time.Clock()

flag_mouse_state = 'release'

# create graph and fill it
g = G()

#tool bar
# todo: add tool bar

# dragable
img = pygame.Surface((20,20))
img.fill(White.get_value())
img.convert_alpha()
pygame.draw.circle(img, Black.get_value(), (10, 10), 10)
dragable_vertex = DragableVertex((60,420), 'vertex dragable object', img, g)


while flag_run:
    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_run = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag_mouse_state = "clicked"
        elif event.type == pygame.MOUSEBUTTONUP:
            flag_mouse_state = "release"
    #logic
    dragable_vertex.loop(flag_mouse_state)
    g.loop(flag_mouse_state)
    if flag_mouse_state == 'clicked':
        flag_mouse_state = 'drag'
    #draw
    screen.fill(White.get_value())
    g.draw(screen)
    dragable_vertex.draw(screen)
    pygame.display.update()

    clock.tick(30)

pygame.quit()
sys.exit()
