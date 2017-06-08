import pygame
import sys
import graph
import color

pygame.init()

flag_run = True  # type: bool

screen_size = screen_width, screen_height = 450, 450  # type: tuple
screen = pygame.display.set_mode(screen_size)  #type: pygame.Surface
clock = pygame.time.Clock()

white_color = 255, 255, 255

# create graph and fill it
g = graph.Graph()
g.add_vertex((200,200))
g.add_vertex((100,200))
g.add_edge(1, 2)
g.add_edge(0, 1, color.Red)


while flag_run:
    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_run = False
            break
    #logic
    #draw
    screen.fill(white_color)
    g.draw(screen)
    pygame.display.update()

    clock.tick(30)

pygame.quit()
sys.exit()
