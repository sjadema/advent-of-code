from typing import List

with open('assets/day12.txt', 'r') as file:
    lines = [line for line in file.read().splitlines()]


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, start: str, end: str) -> None:
        for vertex in [start, end]:
            if vertex not in self.vertices:
                self.vertices[vertex] = set()

        self.vertices[start].add(end)

    def __resolve_paths(self, start: str, end: str, current_path: list, visited: dict, paths: List[list]):
        visited[start] = True if start.upper() != start else False
        current_path.append(start)

        if start == end:
            paths.append(current_path.copy())
        else:
            for edge in self.vertices[start]:
                if not visited[edge]:
                    self.__resolve_paths(edge, end, current_path, visited, paths)

        current_path.pop()
        visited[start] = False

    def resolve_paths(self, start: str, end: str) -> List[list]:
        visited = {vertex: False for vertex in self.vertices.keys()}
        current_path = []
        paths = []

        self.__resolve_paths(start, end, current_path, visited, paths)

        return paths


graph = Graph()
for line in lines:
    start, end = line.split('-')
    graph.add_edge(start, end)
    graph.add_edge(end, start)

paths = graph.resolve_paths('start', 'end')
print(f"Number of paths: {len(paths)}")
