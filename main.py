import pygame
import sys
import graph
import color
import dragable_object


pygame.init()

flag_run = True  # type: bool

screen_size = screen_width, screen_height = 450, 450  # type: tuple
screen = pygame.display.set_mode(screen_size)  #type: pygame.Surface
clock = pygame.time.Clock()

flag_mouse_state = 'release'

# create graph and fill it
g = graph.Graph()
g.add_vertex((200,200))
g.add_vertex((100,200))
g.add_edge(1, 2)
g.add_edge(0, 1, color.Red)

# dragable
img = pygame.Surface((30,30))
img.fill(color.White.get_value())
img.convert_alpha()
pygame.draw.circle(img, color.Black.get_value(), (10, 10), 10)
dragable_vertex = dragable_object.DragableVertex((60,420), 'vertex dragable object', img, g)


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
    #draw
    screen.fill(color.White.get_value())
    g.draw(screen)
    dragable_vertex.draw(screen)
    pygame.display.update()

    clock.tick(30)

pygame.quit()
sys.exit()
