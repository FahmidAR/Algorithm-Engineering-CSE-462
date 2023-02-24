import time

# def hamiltonian_cycle(graph):
#     n = len(graph)
#     memo = {}
#     visited_all = (1 << n) - 1
#     stack = []

#     # Starting from node 0
#     start_node = 0
#     visited = 1 << start_node
#     stack.append((start_node, visited))

#     while stack:
#         curr_node, visited = stack.pop()
#         if (curr_node, visited) in memo:
#             continue
#         memo[(curr_node, visited)] = None

#         if visited == visited_all:
#             if graph[curr_node][start_node]:
#                 memo[(curr_node, visited)] = [curr_node, start_node]
#                 return memo[(curr_node, visited)]

#         for neighbor in range(n):
#             if graph[curr_node][neighbor] and not visited & (1 << neighbor):
#                 new_visited = visited | (1 << neighbor)
#                 stack.append((neighbor, new_visited))

#     return None


def hamiltonian_cycle(graph):
    n = len(graph)
    memo = {}
    adj=1

    def dp(start, visited):
        print("start ", start," visited ", visited)
        if (start, visited) in memo:
            print("memo ", memo[(start, visited)])
            return memo[(start, visited)]

        if visited == (1 << n) - 1:
            if graph[start][0]:
                return [start, 0]

        # for i in range (0,n):
        #     if(visited==0 | adj):
        #         flag=True
        

        for neighbor in range(n):
            if graph[start][neighbor] and not visited & (1 << neighbor):
                cycle = dp(neighbor, visited | (1 << neighbor))
                if cycle is not None:
                    if cycle[-1] != 0:
                        continue
                    memo[(start, visited)] = [start] + cycle
                    return memo[(start, visited)]

        memo[(start, visited)] = None
        return None

    # for start in range(n):
    #     cycle = dp(start, 1 << start)
    #     if cycle is not None:
    #         return cycle
    cycle = dp(0, 1 << 0);
    if cycle is not None:
        return cycle

    return None

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# graph = [
#     [0, 1, 1, 0, 0],
#     [1, 0, 0, 1, 0],
#     [1, 0, 0, 1, 1],
#     [0, 1, 1, 0, 1],
#     [0, 1, 1, 1, 0]
# ]
# graph = [
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0],
#     [1, 0, 0, 1, 1],
#     [0, 1, 1, 0, 1],
#     [0, 0, 1, 1, 0]
# ]
# graph = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]


start_time = time.perf_counter_ns()
cycle = hamiltonian_cycle(graph)
end_time = time.perf_counter_ns()

execution_time_ns = end_time - start_time
print(f"Execution time: {execution_time_ns} ns")
print(cycle)  # prints [0, 1, 2, 3, 4, 0]

