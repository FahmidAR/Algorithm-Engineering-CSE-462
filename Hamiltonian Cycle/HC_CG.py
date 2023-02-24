import networkx as nx


def bipartite_hamiltonian_cycle(graph):
    # Check if the graph is bipartite
    if not nx.is_bipartite(graph):
        return None
    
    # Partition the vertices into two sets
    sets = nx.bipartite.sets(graph)
    set_a, set_b = sets[0], sets[1]
    
    # Choose a vertex from set A to start
    start_vertex = next(iter(set_a))
    
    # Do a depth-first search starting from the start vertex
    visited = set()
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        visited.add(vertex)
        for neighbor in graph.neighbors(vertex):
            if neighbor in set_b and neighbor not in visited:
                stack.append(neighbor)
    
    # Check if a Hamiltonian cycle was found
    visited = list(visited)
    if graph.has_edge(visited[-1], start_vertex):
        visited.append(start_vertex)
        return visited
    else:
        return None


def create_graph_from_adjacency_matrix(adj_matrix):
    # Create an empty graph
    graph = nx.Graph()
    
    # Add nodes to the graph
    n = len(adj_matrix)
    for i in range(n):
        graph.add_node(i+1)
        
    # Add edges to the graph
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                graph.add_edge(i+1, j+1)
                
    return graph

adj_matrix = [[0, 1, 1, 0, 0],
              [1, 0, 1, 1, 0],
              [1, 1, 0, 1, 0],
              [0, 1, 1, 0, 1],
              [0, 0, 0, 1, 0]]



graph = create_graph_from_adjacency_matrix(adj_matrix)
cycle = bipartite_hamiltonian_cycle(graph)
print(cycle)

