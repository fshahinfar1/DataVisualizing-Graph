from color import *
from vertex import *
from edge import *


class Graph:
    vertex_id = 0
    edge_id = 0

    def __init__(self, graph=None):
        """
        :param graph:
        :type graph: Graph
        """
        self.__adjacent_vertices = dict()  # type: dict
        if graph is None:
            self.__node_count = 1  # type: int
            self.__vertices = [Vertex(Graph.vertex_id, (150, 150), self)]  # type: list
            self.__adjacent_vertices[Graph.vertex_id] = []
            self.__lock = False
            Graph.vertex_id += 1
        else:
            self.__node_count = len(graph)  # type: int
            self.__vertices = []  # type: list
            for vertex in list(graph.get_vertices()):
                new_vertex = Vertex.new(vertex)
                self.__vertices.append(new_vertex)
                self.__adjacent_vertices[new_vertex.id] = []
                Graph.vertex_id += 1
            # todo: add edge to copy graph


    def __len__(self):
        return self.__node_count

    def get_vertex(self, vertex_id):
        for v in self.__vertices:
            if v.id == vertex_id:
                return v
        return None

    @property
    def lock(self):
        return self.__lock

    def get_edge(self, edge_id):
        for edges in self.__adjacent_vertices.values():
            for edge in edges:
                if edge.id ==  edge_id:
                    return edge
        return None

    def add_vertex(self, pos, color=Black):
        new_vertex = Vertex(Graph.vertex_id, pos, self, color)
        self.__node_count+=1
        self.__vertices.append(new_vertex)
        self.__adjacent_vertices[new_vertex.id] = []
        Graph.vertex_id += 1

    def add_edge(self, source, destination, val=0, color=Black):
        """

        :param source:
        :type source: int
        :param destination:
        :param color:
        :return:
        """
        if(isinstance(source, Vertex)):
            source_vertex = source
        else:
            source_vertex = self.__vertices[source]
        if(isinstance(destination, Vertex)):
            destination_vertex = destination
        else:
            destination_vertex = self.__vertices[destination]
        new_edge = Edge(Graph.edge_id, self, source_vertex, destination_vertex, val, color)
        Graph.edge_id += 1
        if (isinstance(source, Vertex)):
            source = source.id
        self.__adjacent_vertices[source].append(new_edge)

    def remove_vertex(self, vertex):
        vertex_id = vertex
        if isinstance(vertex, Vertex):
            vertex_id = vertex.id
        for l in self.__adjacent_vertices.values():  # type: Edge
            for e in l:
                if e.source.id == vertex_id or e.destination.id == vertex_id:
                    self.remove_edge(e.id)
        self.__adjacent_vertices.pop(vertex_id)  # remove vertex key from dict
        for i in range(len(self.__vertices)):  # type: Vertex
            v = self.__vertices[i]
            if v.id == vertex_id:
                self.__vertices.pop(i)
                self.__node_count -= 1
                break


    def remove_edge(self, edge_id):
        # todo: this implementation does not feel efficient at all
        for l in self.__adjacent_vertices.values():  # type: list
            for e in l:  # type: Edge
                if e.id == edge_id:
                    self.__adjacent_vertices[e.source.id].remove(e)

    def get_vertices(self):
        for v in self.__vertices:
            yield v

    @property
    def adjacent_vertices(self):
        return dict(self.__adjacent_vertices)

    def loop(self, mouse_state):
        if  not self.lock:
            for vertex in self.__vertices:
                vertex.loop(mouse_state)
            for edges in self.__adjacent_vertices.values():
                for edge in edges:
                    edge.loop(mouse_state)

    def draw(self, screen):
        for edges in self.__adjacent_vertices.values():
            for edge in edges:
                edge.draw(screen)
        for vertex in self.__vertices:
            vertex.draw(screen)

    @staticmethod
    def get_algorithm_graph(Graph):
        """
        :type Graph: Graph
        :param Graph:
        :return: dict
        """
        g = dict()
        edges = Graph.adjacent_vertices
        for v in Graph.get_vertices():
            g[v.id] = []
            for e in edges[v.id]: # type: Edge
                g[v.id].append((e.destination.id, e.value, e.id))
        return g
