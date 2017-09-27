import pygame
import sys
import threading
import concurrent.futures
import algoritms
from graph import Graph as G
from color import *
from dragable_object import *
from button import *

pygame.init()

flag_run = True  # type: bool

screen_size = screen_width, screen_height = 450, 450  # type: tuple
screen = pygame.display.set_mode(screen_size)  # type: pygame.Surface
clock = pygame.time.Clock()

flag_mouse_state = 'release'

# create graph and fill it
g = G()
g.add_vertex((50, 50))
g.add_vertex((250, 50))
g.add_vertex((250, 150))
g.add_vertex((150, 250))
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)
# print(g.adjacent_vertices)
# animation
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
# a = executor.submit(Graph.algoritms.find_eulerian_tour, g)
# thread0 = threading.Thread(target=Graph.algoritms.random_selection, args=(g,))
# thread0.start()

# tool bar
# todo: add tool bar

# dragable
img = pygame.Surface((20, 20))
img.fill(White.get_value())
img.convert_alpha()
pygame.draw.circle(img, Black.get_value(), (10, 10), 10)
dragable_vertex = DragableVertex((60, 420), 'vertex dragable object', img, g)

# button
b = Button((300,200),lambda:executor.submit(algoritms.find_eulerian_tour, g))

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
    # logic
    dragable_vertex.loop(flag_mouse_state)
    g.loop(flag_mouse_state)
    b.loop(flag_mouse_state)
    if flag_mouse_state == 'clicked':
        flag_mouse_state = 'drag'
    # draw
    screen.fill(Gray.get_value())
    g.draw(screen)
    dragable_vertex.draw(screen)
    b.draw(screen)
    pygame.display.update()

    clock.tick(30)

pygame.quit()
# executor.shutdown()
sys.exit()
