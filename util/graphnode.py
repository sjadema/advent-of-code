from typing import List


class GraphNode:

    visited = []

    def __init__(self, name: str):
        self.name = name
        self.nodes = {}

    def get_name(self) -> str:
        return self.name

    def add_node(self, node: 'GraphNode') -> None:
        if node.get_name() not in self.nodes:
            self.nodes[node.get_name()] = node
            node.add_node(self)

    def get_nodes(self, recursive: bool = False) -> List['GraphNode']:
        if not recursive:
            return list(self.nodes.values())

        self.visited.append(self)
        for node in self.get_nodes():
            if node not in self.visited:
                node.get_nodes(recursive)

        # nodes = deepcopy(self.visited)
        print(self.visited)
        self.visited = []

        return nodes

    def count_nodes(self, recursive: bool = False):
        if not recursive:
            return len(self.get_nodes())

        self.visited.append(self)
        for node in self.get_nodes():
            if node not in self.visited:
                node.count_nodes(recursive)

        total = len(self.visited)
        self.visited = []

        return total
