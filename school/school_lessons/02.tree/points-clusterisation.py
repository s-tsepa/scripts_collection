import random
import pdb

class Node:
    def __init__(self, coords, weight=1, children=[]):
        self.coords = coords
        self.weight = weight
        self.children = children

        self.dist_list = dict()

    def dist_vector(self, n):
        return (n.coords[0] - self.coords[0]), (n.coords[1] - self.coords[1])

    def dist(self, n):
        x, y = self.dist_vector(n)
        return (x ** 2 + y ** 2) ** 0.5

    def __str__(self):
        return f'{self.coords} {self.weight}'

    def __repr__(self):
        return f'{self.coords} {self.weight}'


NODES_COUNT = 10
rand_coords = lambda : [random.randint(1, 100), random.randint(1, 100)]
nodes = [Node(rand_coords()) for _ in range(NODES_COUNT)]

def calculate_root_node(nodes):
    while len(nodes) > 1:
        min_dist = 10 ** 9
        min_points = []

        for a in nodes:
            for b in nodes:
                if a is b:
                    continue

                d = a.dist(b)
                
                a.dist_list[b] = d
                b.dist_list[a] = d

                if d < min_dist:
                    min_points = [a, b]
                    min_dist = d

        a, b = min_points
        vec = a.dist_vector(b)

        # pdb.set_trace()
        ratio = b.weight / (a.weight + b.weight)

        avg_point = [
            round(a.coords[0] + vec[0] * ratio, 2),
            round(a.coords[1] + vec[1] * ratio, 2),
        ]

        new = Node(avg_point, a.weight + b.weight, children = [a, b])

        # print(f'{min_points[0]} + {min_points[1]} = {new}; Points: {len(nodes)}')

        nodes.append(new)
        nodes.remove(a)
        nodes.remove(b)

    return nodes[0]

root = calculate_root_node(nodes)
# print(root)

highest_clusters_after_cut = []
CUT_DEPTH = 3

def descent(node: Node, depth=0):
    if not node.children:
        return

    if depth == CUT_DEPTH:
        highest_clusters_after_cut.append(node)

    for child in node.children:
        descent(child, depth + 1)


descent(root)
print(highest_clusters_after_cut)
