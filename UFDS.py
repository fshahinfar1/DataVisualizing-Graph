

class UFDS(object):

    def __init__(self, N, L=None):
        if L and len(L) != N:
            raise RuntimeError('L should be the same size as N')
        self.index = L
        self.parent = list(L) if L else [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.size = N

    def get_parent(self, i):
        tmp_index = i
        if self.index is not None:
            tmp_index = self.index.index(i)
        if self.parent[tmp_index] == i:
            return i
        return self.get_parent(self.parent[tmp_index])

    def is_same_set(self, i, j):
        return self.get_parent(i) == self.get_parent(j)

    def union_set(self, i, j):
        parent_i = self.get_parent(i)
        parent_j = self.get_parent(j)

        tmp_index_p_i = parent_i
        tmp_index_p_j = parent_j
        if self.index is not None:
            tmp_index_p_i = self.index.index(parent_i)
            tmp_index_p_j = self.index.index(parent_j)

        if parent_i != parent_j:
            if self.rank[tmp_index_p_i] < self.rank[tmp_index_p_j]:
                self.parent[tmp_index_p_i] = parent_j
            else:
                self.parent[tmp_index_p_j] = parent_i
                if(self.rank[tmp_index_p_i] == self.rank[tmp_index_p_j]):
                    self.rank[tmp_index_p_j] += 1

    def show(self):
        for i in range(self.size):
            if self.index:
                print(str(self.index[i]), " :=> ", str(self.parent[i]))
            else:
                print(str(i), " :=> ", str(self.parent[i]))
