import time
import math
import numpy as np
from queue import PriorityQueue

# =============================================================================
# Branch and bound with best first search using priority queue
# Author: Shivaen Ramshetty
# Time: 12/3/2021
# =============================================================================


def reduce_matrix(matrix):
    reduced_cost = 0

    # Finding minimum cost for each row and updating them
    for i in range(len(matrix)):
        min_row_cost = min(matrix[i])
        matrix[i] = matrix[i] - min_row_cost
        reduced_cost += min_row_cost
    
    # Finding minimum cost for each col and updating them
    for j in range(len(matrix[0])):
        min_col_cost = min(matrix[:,j])
        matrix[:,j] = matrix[:,j] - min_col_cost
        reduced_cost += min_col_cost

    return matrix, reduced_cost

# Find suitable new configuration, next nodes
def expand(nodes, path):
    ids = [node["id"] for node in nodes]
    configs = list(set(ids).symmetric_difference(set(path)))

    return configs

# Check solution
def check_solution(nodes, path):
    # Path should be unique nodes and of length equal to total number of nodes
    if len(set(path)) != len(nodes):
        if len(set(path)) < len(path):
            return "dead"
        return "not dead"

    return "solution"

# Nearest neighbor approximation
def nearest_neigbor(nodes, matrix, cost):
    path = [0]
    while len(path) < len(matrix[0]):
        min_cost = math.inf
        neighbor = None
        for target in expand(nodes, path):
            if matrix[path[-1]][target] < min_cost:
                min_cost = matrix[path[-1]][target]
                neighbor = target
        
        path.append(neighbor)
        cost += min_cost
    cost += matrix[path[-1]][path[0]]
    
    return int(cost), path

def BnBP(cutoff, nodes, costs):

    start = time.time()

    costs = np.array(costs)
    trace = {}
    path = []
              
    # reduced cost is lower bound
    reduced_matrix, reduced_cost = reduce_matrix(costs)

    # fetch frontier nodes, priority queue
    # Referencing paper: https://link.springer.com/chapter/10.1007/978-3-319-45378-1_19
    root = (reduced_cost, [0], reduced_cost)
    frontier = PriorityQueue()
    frontier.put(root)
    
    # upper bound
    best_quality, nn_path = nearest_neigbor(nodes, reduced_matrix, reduced_cost)
    path = nn_path
    trace.update({round(time.time() - start, 2): best_quality})

    # Run algorithm till time exceeds cutoff or all paths in frontier searched
    while (time.time() - start) < cutoff:

        if frontier.empty():
            break
        
        choice = frontier.get() # Lowest value retrieved first
        curr_path = choice[1]
        curr_cost = choice[2]

        if curr_cost > best_quality:
            continue

        configs = expand(nodes, curr_path)
        for option in configs:
            new_path = curr_path + [option]

            state = check_solution(nodes, new_path)
            cost = int(curr_cost + reduced_matrix[curr_path[-1]][option])
            if state == "solution":
                cost += int(reduced_matrix[new_path[-1]][new_path[0]])
                if cost < best_quality:
                    best_quality = cost
                    path = new_path
                    trace.update({round(time.time() - start, 2): cost})
            elif state == "not dead":
                if cost < best_quality:
                    priority = cost / (len(new_path) ** 2) 
                    frontier.put((priority, new_path, cost))
    
    return best_quality, path, trace