import time
import numpy as np

def heuristic_info_acq_alg(graph):
    n = len(graph)
    L = [[] for i in range(n)]
    R = [[] for i in range(n+1)]
    curv, curl = 0, 0
    L[curv].append(curl)
    R[curl].append(curv)
    
    # if not R[curl]:
    #     return L
    # print(n)
    while curl <= n:
        # print(curl)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if curl==n:
            # print(R[curl-1])
            for p in R[curl-1]:      
                if(0 in graph[p]):
                    L[0].append(n)
                    break
            return R, L 
        elif len(R[curl])==0:
            return None,None
        # print("R curl=",R[curl])
        # temp=list(np.copy(L))
        for i in R[curl]:
            # print("current vertex:",i)
            # print(temp[i])
            for j in graph[i]:
                if(j==0) :
                    continue

                # print("adjacents:",j)
                #temp=L[i]
                for x in L[i]:
                    
                    L[j].append(x+1)
                    #L[k].append([f+1 for f in L[i]])
                
                R[curl+1].append(j)
                L[j] = list(set(L[j]))
                # if k not in R[curl+1]:
                #     L[k].append(curl+1)
                #     R[curl+1].append(k)
        curl += 1
    
# L = [[0, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 5, 8, 9, 10, 11, 12, 13, 14, 15], [2, 6, 9, 10, 11, 12, 13, 14, 15], [3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [2, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15], [4, 7, 8, 11, 12, 13, 14, 15], [3, 7, 10, 11, 12, 13, 14, 15], [4, 8, 11, 12, 13, 14, 15], [5, 7, 8, 9, 10, 11, 12, 13, 14, 15], [3, 6, 7, 9, 10, 11, 12, 13, 14, 15], [5, 9, 12, 13, 14, 15], [4, 7, 8, 10, 11, 12, 13, 14, 15], [5, 6, 8, 9, 10, 11, 12, 13, 14, 15], [6, 7, 9, 10, 11, 12, 13, 14, 15], [6, 10, 13, 14, 15]]

# R = [[0], #0
#      [1], #1
#      [2,4], #2
#      [3,6,9], #3
#      [5, 7, 11], #4
#      [4,8,10,12], #5
#      [3,9,12,13,14], #6
#      [5,8,9,11,13], #7
#      [3,4,8,11,12], #8
#      [3,8,9,12,13], #9
#      [3,8,11,13], #10
#      [3,8,12], #11
#      [3,13], #12
#      [8], #13
#      [3], #14
#      [0] #15
     
#      ]

def step3(graph, L, R):
    n = len(graph)
    visited = []
    previous_node = 0
    current_node = None
    for i in range(n-1, -1, -1):
        # print("node ", i)
        possible_nodes = R[i]
        # print("possible nodes ",possible_nodes)
        if(len(possible_nodes)==0):
            # print("No Hamiltonian cycle found")
            return False, None
        for j in range(len(possible_nodes)):
            # print("inside")
            # print(graph[possible_nodes[j]])
            if((previous_node in graph[possible_nodes[j]]) and (possible_nodes[j] not in visited)):
                current_node = possible_nodes[j]
                # print("current node ", current_node)
                visited.append(current_node)
                break
            if(j==len(possible_nodes)-1):
                # print("No Hamiltonian cycle found")
                return False, None
                
        previous_node = current_node
    # print("Hamiltonian cycle found")
    return True, visited

graph = [
    [1],
    [2,4],
    [3,6],
    [0],
    [9],
    [4],
    [5,7],
    [8,10],
    [3],
    [11],
    [12,14],
    [12],
    [13],
    [8],
    [5,9]
]
# graph = [
#     [1],
#     [2,3],
#     [7,4],
#     [2,5],
#     [6],
#     [0],
#     [3,5,7],
#     [4]
# ]
start_time = time.perf_counter_ns()
R, L = heuristic_info_acq_alg(graph)
flag, visited = step3(graph, L, R)
# print("L ", L)
# print("R ", R)

if visited is not None:
    visited = visited[::-1]
    visited.append(0)

end_time = time.perf_counter_ns()

execution_time_ns = end_time - start_time
print(f"Execution time: {execution_time_ns} ns")



    # print("flag ", flag)
print("Hamiltonian cycle: ", visited)

