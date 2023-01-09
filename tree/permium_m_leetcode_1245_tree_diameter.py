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
    adjnodes = collections.defaultdict(list)
    travel_mark = []
    def get_adjnodes(self, edges):
        for [n1, n2] in edges:
            self.adjnodes[n1].append(n2)
            self.adjnodes[n2].append(n1)

    def get_diameter_between_two_nodes(self, edges, n1, n2):
        diameter = 0
        if n1 == n2:
            return 0
        if [n1, n2] in edges or [n2, n1] in edges:
            self.travel_mark.append([n1,n2])

        else:
            adjn1 = self.adjnodes[n1]
            adjn2 = self.adjnodes[n2]
            print(adjn2, adjn1)
            for n1 in adjn1:
                for n2 in adjn2:
                    print(n1, n2)
                    if [n1, n2] in self.travel_mark or [n2, n1] in self.travel_mark:
                        continue
                    diameter = self.get_diameter_between_two_nodes(edges, n1, n2) + 1
                    self.travel_mark.append([n1,n2])
        return diameter


edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
td = tree_diameter()

td.get_adjnodes(edges)
print(td.adjnodes)
#td.get_diameter_between_two_nodes(edges, 3,5)

