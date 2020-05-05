from pprint import pprint
from itertools import permutations


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = []
        self.end_paths = []
        self.paths = {}

    def add_node(self, node):
        self.nodes.add(node)
        return self

    def add_edge(self, edge):
        self.edges.append(edge)
        return self

    def create_paths(self):
        self.paths = dict([(node, {}) for node in self.nodes])
        return self

    def fill_paths(self):
        for edge in self.edges:
            city1, city2, cost = edge
            self.paths[city1][city2] = cost
            self.paths[city2][city1] = cost

        return self

    def fill_end_paths(self):
        for cities in permutations(self.nodes):
            distance = 0
            for city1, city2 in zip(cities, cities[1:]):
                try:
                    distance += int(self.paths[city1][city2])
                except TypeError:
                    print(self.paths[city1][city2])
                    exit()

            self.end_paths.append((distance, cities))

        self.end_paths.sort()

        return self

    def get_shortest(self):
        return self.end_paths[0]

    def get_longest(self):
        return self.end_paths[-1]


if __name__ == '__main__':
    graph = Graph()
    with open('./input.txt', 'r') as f:
        file = f.read().split('\n')[:-1]
        for line in file:
            parts = line.split()
            graph.add_node(parts[0]).add_node(parts[2]).add_edge((parts[0], parts[2], parts[-1]))

    graph.create_paths().fill_paths().fill_end_paths()
    print(graph.get_shortest())
    print(graph.get_longest())
