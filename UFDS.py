

class UFDS(object):

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0 for i in range(N)]

    def get_parent(self, i):
        if self.parent[i] == i:
            return i
        return self.get_parent(self.parent[i])

    def is_same_set(self, i, j):
        return self.get_parent(i) == self.get_parent(j)

    def union_set(self, i, j):
        parent_i = self.get_parent(i)
        parent_j = self.get_parent(j)
        if parent_i != parent_j:
            if self.rank[parent_i] < self.rank[parent_j]:
                self.parent[parent_i] = parent_j
            else:
                self.parent[parent_j] = parent_i
                if(self.rank[parent_i] == self.rank[parent_j]):
                    self.rank[parent_j] += 1
