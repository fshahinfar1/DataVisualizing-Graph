from graph import Graph as G
from random import randrange
from vertex import *
from color import *
from time import sleep
import copy
import UFDS
import traceback

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
        if adjacent_edge_list: #tpye: tuple
            edge = adjacent_edge_list.pop()[0] # type: int
            current_node_id = edge
            anim.append(edge)
        else:
            break
    play_algorithm_animation(graph, anim, 0.5)

def kruskal(graph):
    try:
        graph._Graph__lock = True
        print("kruskal")
        anim = []
        workG = G.get_algorithm_graph(graph) # type : dict
        all_edges = [(i, j[0], j[1], j[2]) for i in workG.keys() for j in workG[i]]
        all_edges.sort(key=lambda x: x[2], reverse=False)
        tree = UFDS.UFDS(len(graph), tuple(workG.keys()))
        for i in range(len(all_edges)):
            e = all_edges[i]
            if(not tree.is_same_set(e[0], e[1])):
                anim.append(e)
                tree.union_set(e[0], e[1])
        for i in range(len(anim)):
            current_edge = graph.get_edge(anim[i][3]) #type: Vertext
            current_edge.color = SELECTED_COLOR
            sleep(0.5)
    except Exception as e:
        print("error")
        print(e)
        traceback.print_exc()

def play_algorithm_animation(graph, anim, delay):
    for i in range(len(anim)-1):
        current_vertex = graph.get_vertex(anim[i]) #type: Vertext
        current_vertex.color = SELECTED_COLOR
        print(anim[i],end="=>")
        sleep(delay)
        next_vertex = graph.get_vertex(anim[i+1])
        next_vertex.color = NEXT_COLOR
        sleep(delay)
        current_vertex.color = DEFAULT_COLOR
