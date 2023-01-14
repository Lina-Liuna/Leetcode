# Given a directed Graph and two vertices in it, check whether there is a path form the first given
# vertex to second
# Input:  [[0,1],[1,2],[2,3],[1,4],[4,5]]

from collections import defaultdict

class graph:
    paths = list()
    edges = defaultdict(list)

    def get_edges(self, arr):
        for a in arr:
            self.edges[a[0]].append(a[1])
            self.edges[a[1]].append(a[0])

    def dfs(self, u, v, visited):
        self.paths.append(u)
        if u == v:
            print(self.paths)
            return True
        visited.append(u)
        for n in self.edges[u]:
            if n not in visited:
                self.dfs(n, v, visited)
        #del self.paths[-1]
        self.paths.pop()

    def paths_between_two_nodes(self, u, v):
        visited = []
        self.dfs(u, v, visited)


g = graph()
Input = [[0,1],[1,2],[2,3],[1,4],[4,5]]
g.get_edges(Input)
print(g.edges.items())
g.paths_between_two_nodes(3, 5)

g.paths = []
g.paths_between_two_nodes(0, 5)

g.paths = []
g.paths_between_two_nodes(2, 5)