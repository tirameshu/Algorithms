from collections import defaultdict

directed_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []

}

def bfs(graph, start, key):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        source = queue.pop(0)
        print(source, end=" ")

        for neighbour in graph[source]:
            if neighbour == key:
                print("Found!")
                return key
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(directed_graph, 'A', 'F')