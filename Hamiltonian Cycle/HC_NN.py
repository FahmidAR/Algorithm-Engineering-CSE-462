def hamiltonian_cycle(graph):
    n = len(graph)
    for start in range(n):
        visited = [False] * n
        visited[start] = True
        current = start
        cycle = [start]
        while len(cycle) < n:
            next_vertex = -1
            min_dist = float('inf')
            for neighbor in range(n):
                if not visited[neighbor] and graph[current][neighbor]:
                    dist = graph[current][neighbor]
                    if dist < min_dist:
                        min_dist = dist
                        next_vertex = neighbor
            if next_vertex == -1:
                break
            cycle.append(next_vertex)
            visited[next_vertex] = True
            current = next_vertex
        if len(cycle) == n and graph[cycle[-1]][cycle[0]]:
            cycle.append(start)
            return cycle
    return "No Hamiltonian cycle exists"

# example graph
# graph = [
#     [0, 1, 1, 0, 0],
#     [0, 1, 1, 0, 0],
#     [0, 1, 1, 0, 0],
#     [0, 1, 1, 0, 0],
#     [0, 1, 1, 0, 0],
# ]
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]
print(hamiltonian_cycle(graph))
