from Graph.graph import Graph as G
from random import randrange
from Graph.vertex import *
from Graph.color import *
from time import sleep
import copy


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
    print("euler")
    workG = G.get_algorithm_graph(graph)  # type: dict
    current_node_id = list(workG.keys())[0]
    while True:
        current_vertex = tuple(graph.get_vertices())[current_node_id]  # type: Vertex
        current_vertex.color = Yellow
        print(current_node_id,end="=>")
        sleep(0.5)
        adjacent_edge_list = workG[current_node_id]
        if adjacent_edge_list:
            edge = adjacent_edge_list.pop() # type: int
            next_vertex = tuple(graph.get_vertices())[edge]  # type: Vertex
            next_vertex.color = Cyan
            sleep(0.5)
            current_vertex.color = DEFAULT_COLOR
            current_node_id = edge
        else:
            print("Done")
            break

