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
        self.visited = list()
        self.diameter = 0

    def get_edges(self, edges):
        for [n1, n2] in edges:
            self.edges[n1].append(n2)
            self.edges[n2].append(n1)

    def get_diameter_between_two_nodes(self, edges, n1, n2):
        if n1 == n2:
            return True
        print(n1, n2, self.visited)
        self.visited.append([n1, n2])
        self.visited.append([n2, n1])
        if [n1, n2] in edges or [n2, n1] in edges:
            print('in edge:', n1, n2)
            return True
        else:
            for n in self.edges[n1]:
                #print(n, self.edges[n1], n2)
                if [n, n2] not in self.visited:
                    self.visited.append([n, n2])
                    self.visited.append([n2, n])
                    self.diameter = self.diameter + 1
                    if self.get_diameter_between_two_nodes(edges, n, n2) is True:
                        return self.diameter
        return self.diameter


edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
td = tree_diameter()

td.get_edges(edges)
print(td.edges)
dis = td.get_diameter_between_two_nodes(edges, 5, 3)
print(dis)
