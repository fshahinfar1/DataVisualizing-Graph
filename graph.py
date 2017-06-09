import color
import vertex
import edge


class Graph:
    vertex_id = 0
    edge_id = 0

    def __init__(self):
        self.__node_count = 1  # type: int
        self.__vertices = [vertex.Vertex(Graph.vertex_id, (150, 150))]  # type: list
        Graph.vertex_id += 1
        self.__adjacent_vertices = [[]] # type:

    def __len__(self):
        return self.__node_count

    def add_vertex(self, pos, color=color.Black):
        new_vertex = vertex.Vertex(Graph.vertex_id, pos, color)
        Graph.vertex_id += 1
        self.__vertices.append(new_vertex)
        self.__adjacent_vertices.append([])

    def add_edge(self, source, destination, color=color.Black):
        source_vertex = self.__vertices[source]
        destination_vertex = self.__vertices[destination]
        new_edge = edge.Edge(Graph.edge_id\
        , source_vertex, destination_vertex, color)
        Graph.edge_id += 1
        self.__adjacent_vertices[source].append(new_edge)

    def loop(self, mouse_state):
        for vertex in self.__vertices:
            vertex.loop(mouse_state)

    def draw(self, screen):
        for edges in self.__adjacent_vertices:
            for edge in edges:
                edge.draw(screen)
        for vertex in self.__vertices:
            vertex.draw(screen)
