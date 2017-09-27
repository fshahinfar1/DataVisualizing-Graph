from graph import Graph as G
from random import randrange
from vertex import *
from color import *
from time import sleep
import copy
import sys

SELECTED_COLOR = Yellow
NEXT_COLOR = Cyan

def random_selection(graph):
    """
    :param graph:
    :type graph: G
    :return:
    """
    count_vertices = len(graph)
    print(count_vertices)
    while True:
        current_node_id = randrange(count_vertices)
        print(current_node_id)
        current_node = tuple(graph.get_vertices())[current_node_id]  # type: Vertex
        current_node.color = Yellow
        sleep(1)
        current_node.color = DEFAULT_COLOR


def find_eulerian_tour(graph):
    #sys.stdout = open('log_find_eulerain_tour.txt', 'w')
    print("eulerian")
    workG = G.get_algorithm_graph(graph)  # type: dict
    current_node_id = list(workG.keys())[0]
    anim = [current_node_id,]
    while True:
        adjacent_edge_list = workG[current_node_id]
        if adjacent_edge_list:
            edge = adjacent_edge_list.pop() # type: int
            current_node_id = edge
            anim.append(edge)
        else:
            print("Done")
            break
    play_algorithm_animation(graph, anim, 0.5)


def play_algorithm_animation(graph, anim, delay):
    print("first line")
    print("in try")
    print(anim)
    print(len(anim))
    for i in range(len(anim)-1):
        print(i)
        current_vertex = graph.get_vertex(anim[i]) #type: Vertext
        current_vertex.color = SELECTED_COLOR
        print(anim[i],end="=>")
        sleep(delay)
        next_vertex = graph.get_vertex(anim[i+1])
        next_vertex.color = NEXT_COLOR
        sleep(delay)
        current_vertex.color = DEFAULT_COLOR
