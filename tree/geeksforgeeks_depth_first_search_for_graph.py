# Depth first traversal for a graph, unlike trees, graphs may contain cycles(a node may be visited twice).
# To avoid processing a node more than once, use a boolean visited array.
# A graph can have more than one DFS traversal.

# The basic idea is to start from the root or any arbitrary node and mark the node and move to the
# adjacent unmarked node and continue this loop until there is no unmarked adjacent node.
# Then backtrack and check fo other unmarked nodes and traverse them.

from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v)
        for adj_node in self.graph[v]:
            if adj_node not in visited:
                self.dfs_util(adj_node, visited)

    def dfs(self,v):
        visited = set()
        self.dfs_util(v, visited)

edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]

g = Graph()
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,4)
g.add_edge(4,5)

g.dfs(5)