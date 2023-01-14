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
        self.path = list()
        self.diameter = collections.defaultdict(list)

    def get_edges(self, edges):
        for [n1, n2] in edges:
            self.edges[n1].append(n2)
            self.edges[n2].append(n1)

    """
    This is a multi-line comment with docstrings
    def get_diameter_between_two_nodes(self, n1, n2):
        if n1 == n2:
            return True
        print(n1, n2, self.visited)
        if [n1, n2] not in self.visited:
            self.visited.append([n1, n2])
            self.visited.append([n2, n1])
        if [n1, n2] in edges or [n2, n1] in edges:
            print('in edge:', n1, n2)
            return True
        else:
            for n in self.edges[n1]:
                if [n, n2] not in self.visited:
                    self.visited.append([n, n2])
                    self.visited.append([n2, n])
                    self.diameter = self.diameter + 1
                    if self.get_diameter_between_two_nodes(n, n2) is True:
                        return self.diameter
        return self.diameter
    """

    def path_between_two_nodes(self, n1, n2):
        self.path.append(n1)
        if n1 == n2:
            print(self.path)
            self.diameter[n1].append(len(self.path) - 1)
            self.diameter[n2].append(len(self.path) - 1)
            return True
        self.visited.add(n1)

        for n in self.edges[n1]:
            if n not in self.visited:
                self.path_between_two_nodes(n, n2)

        del self.path[-1]


    def tree_diameter(self, edges):
        self.get_edges(edges)
        maximum = 0
        for n1 in self.edges:
            for n2 in self.edges:
                self.path = []
                self.visited = set()
                self.path_between_two_nodes(n1, n2)

        for d in self.diameter:
            if maximum < max(self.diameter[d]):
                maximum = max(self.diameter[d])
        print(maximum)
        return maximum




edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
td = tree_diameter()

diameter_of_tree = td.tree_diameter(edges)
print(f'the tree diameter is: {diameter_of_tree}')





