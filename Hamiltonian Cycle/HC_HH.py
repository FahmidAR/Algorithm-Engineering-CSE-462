# The heuristic information acquisition algorithm is called algorithm 2.
# Input: directed graph G(n, e).
# Output: the set of possible path length values of each node in G.
# Note: Let the list L[i] (0 <= i <= n) record the possible path
# length values of node i in the graph G. Let the array R[i] (0 <= i <= n)
# record the set of nodes with the path length value i. curv records the
# current extended vertex, and curl records the current extension step,
# which is also the current extended path length value.

# Define the function to acquire the path length values of nodes in the graph.
def heuristic_info_acquisition_algorithm(G):
    n = len(G)
    
    # Initialize the data
    curv = 0  # Current extended vertex
    curl = 0  # Current extension step, also the current extended path length value
    L = [[] for i in range(n + 1)]  # The list L[i] records the possible path length values of node i
    R = [[] for i in range(n + 1)]  # The array R[i] records the set of nodes with the path length value i
    L[curv].append(curl)  # Add curl to L[curv]
    R[curl].append(curv)  # Add curv to R[curl]

    # Determine whether the path has been extended to the last node,
    # that is, whether curl is equal to n.
    while curl != n:
        # Determine whether the node set R[curl] is empty.
        if not R[curl]:
            # If R[curl] is empty, there are no more nodes to extend, so the program returns the output.
            return L
        
        # Otherwise, extend every node j in R[curl]
        for j in R[curl]:
            # Add curl + 1 to L[j], since extending j will create a path of length curl + 1
            L[j].append(curl + 1)
            
            # Add the subsequent node of node j to R[curl + 1]
            for k in G[j]:
                R[curl + 1].append(k)
                
        # Increase the current extended length by 1
        curl += 1
        
    # If the program has not yet returned the output, then curl = n
    # and the algorithm is complete. Return the final L array.
    return L


# Define the function to create a graph from an adjacency list.
G = {
0: [1, 2],
1: [3],
2: [3, 4],
3: [4],
4: []
}

# Call the function to acquire the path length values of nodes in the graph.
L = heuristic_info_acquisition_algorithm(G)
print(L)