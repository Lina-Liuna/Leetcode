# Given an undirected graph, the task is to check if there is a cycle in the given graph
from collections import defaultdict


class Graph:

    edges = defaultdict(list)

    def __init__(self, edges):
        for u, v in edges:
            self.edges[u].append(v)
            self.edges[v].append(u)

    def get_edges(self):
        return self.edges

    def dfs_circle(self, u, visited, parent):
        visited[u] = True

        for n in self.edges[u]:
            # If an adjacent vertex is visited and not parent of current vertex, then there is a cycle.
            if visited[n] is True and n != parent:
                return True

            if visited[n] is False:
                if res := self.dfs_circle(n, visited, u) is True:
                    return True
        return False

    def isCyclic(self):
        visited = [False] * len(self.edges.items())

        for n in list(self.edges.keys()):
            if visited[n] is False:
                if res := self.dfs_circle(n, visited, -1) is True:
                    return True

        return False


Input = [[0,1],[1,2],[2,3],[1,4],[4,5]]
g = Graph(Input)
print(g.get_edges().items())

if g.isCyclic():
    print('Graph contains cycle')
else:
    print('Graph doesn\'t contain cycle')

Input = [[0,1],[1,2],[2,3],[1,4],[4,5],[1,3]]
g = Graph(Input)
print(g.get_edges().items())

if g.isCyclic():
    print('Graph contains cycle')
else:
    print('Graph doesn\'t contain cycle')