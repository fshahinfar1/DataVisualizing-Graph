

class Graph:
    def __init__(self):
        self.__node_count = 1  # type: int
        self.__adjacent_list = {}  # type: dict


    def __len__(self):
        return self.__node_count
