# Given n nodes labeled from 0 to n-1 and a list of undirected edges(each edge is a pair of nodes)
# write a function to check whether these edges make up a valid tree.

# Input:  [[0,1],[1,2],[2,3],[1,4],[4,5]]
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false

import collections


class graph_valid_tree:
    edges = collections.defaultdict(list)

    def __init__(self, edges):
        for u, v in edges:
            self.edges[u].append(v)
            self.edges[v].append(u)

    def dfs(self, u, v, visited):
        if len(visited) != 0:
            if u == v:
                return True
        visited.append(u)
        for n in self.edges[u]:
            print(self.edges[u])
            if n not in visited:
                self.dfs(n,v,visited)

    def check_circle_in_graph(self):
        for u in self.edges.keys():
            print(u)
            visited = list()
            if self.dfs(u,u, visited) is True:
                return False

        return True


Input = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Input2 = [[0,1],[1,2]]
Input3 = [[0,1],[1,2],[2,3],[1,4],[4,5],[1,3]]
g = graph_valid_tree(Input)
print(g.edges)
print(g.check_circle_in_graph())