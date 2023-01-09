# Given an undirected tree, return its diameter: the number of edges in a longest path in that tree
# The tree is given as an array of edges where edges[i] = [u, v] is bidirectional edge
# between nodes u and v.
# Each node has labels in the set {0, 1, ...,edges.length}
# Input: edges = [[0,1],[0,2]]
# Output: 2
# Explanation:
# A longest path of the tree is the path 1 - 0 - 2.

# Input:  [[0,1],[1,2],[2,3],[1,4],[4,5]]
# Output: 4
# Explanation:
# A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.

import collections


class tree_diameter:

    def __init__(self):
        self.edges = collections.defaultdict(list)
        self.visited = set()
        self.diameter = 0

    def get_edges(self, edges):
        for [n1, n2] in edges:
            self.edges[n1].append(n2)
            self.edges[n2].append(n1)

    def get_diameter_between_two_nodes(self, edges, n1, n2):
        if n1 == n2:
            return 0
        print(n1, n2, self.edges[n1])
        if [n1, n2] in edges or [n2, n1] in edges:
            return self.diameter + 1
        else:
            for n in self.edges[n1]:
                if (n, n2) not in self.visited:
                    self.diameter = self.get_diameter_between_two_nodes(edges, n, n2) + 1
                    self.visited.add((n, n2))
        return self.diameter


edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
td = tree_diameter()

td.get_edges(edges)
print(td.edges)
td.get_diameter_between_two_nodes(edges, 0, 2)

