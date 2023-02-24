import time


def hamiltonian_cycle(graph):
    n = len(graph)  # Number of vertices in the graph
    memo = {}  # Memorization  dictionary to store previously computed results

    # Recursive function to compute the Hamiltonian cycle
    def dp(start, visited):
        print("current node = ", start," visited node mask = ", format(visited, '06b'))

        # If already computed the result for this node and visited set, return it
        if (start, visited) in memo:
            print("Memory used for node = ", start," mask = ", format(visited, '06b'))
            return memo[(start, visited)]

        # If we have visited all vertices and 
        # there is an edge from the last vertex to the first vertex,
        # we have found a Hamiltonian cycle
        if visited == (1 << n) - 1:
            if graph[start][0]:
                return [start, 0]

        # Try each unvisited neighbor of the current vertex to extend the path
        for neighbor in range(n):
            if graph[start][neighbor] and not visited & (1 << neighbor):
                cycle = dp(neighbor, visited | (1 << neighbor))
                if cycle is not None:
                    if cycle[-1] != 0:
                        continue
                    # Store the result in the memorization  dictionary and return it
                    memo[(start, visited)] = [start] + cycle
                    return memo[(start, visited)]

        # If we reach this point, 
        # no Hamiltonian cycle was found and return None
        memo[(start, visited)] = None
        return None

    # Call the recursive function with the starting vertex and its corresponding bit in the visited set
    cycle = dp(0, 1 << 0)

    # If a Hamiltonian cycle was found, return it
    if cycle is not None:
        return cycle

    # If no Hamiltonian cycle was found, return None
    return None


graph = [
    [0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

print("\n")
start_time = time.perf_counter_ns()
cycle = hamiltonian_cycle(graph)
end_time = time.perf_counter_ns()

execution_time_ns = end_time - start_time
# print(f"Execution time: {execution_time_ns} ns")
print("\nHamiltonian cycle found: ", cycle)
print("\n")

