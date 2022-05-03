import sys
import time

# =============================================================================
# Approximation of TSP by MST(Prim's algorithm) and DFS
# Author: Guangyu Cui
# Time: 11/23/2021
# =============================================================================
                 
def MSTApprox(nodes, distances):    
        
    for i in range(len(distances)):
        distances[i][i] = 0
    
    
    num_nodes = len(nodes)

    best_quality = sys.maxsize
    best_path = []
    trace = {}
    start_time = time.time()  
    for k in range(num_nodes):        
          
        initial_root = k
        
        MST = {} # MST
        for i in range(num_nodes):
            MST[i] = []
        
        Priority_Queue = {} # shortest distance to visited node
        for i in range(num_nodes):
            Priority_Queue[i] = {}  
            Priority_Queue[i]['distance'] = sys.maxsize
        # initial_root = random.randint(0, num_nodes - 1) # randomly choose a starting root
        
        
        
        del Priority_Queue[initial_root] # initialization
        for i in Priority_Queue:
            Priority_Queue[i]['parent'] = initial_root
            Priority_Queue[i]['distance'] = distances[i][initial_root]
        visited = [initial_root]
        
        while len(Priority_Queue) > 0: # Compute MST by Prim's algorithm
            current_min = sys.maxsize
            for i in Priority_Queue: # Choose the closest distance
                if Priority_Queue[i]['distance'] < current_min:
                    current_min = Priority_Queue[i]['distance']
                    parent = Priority_Queue[i]['parent']
                    child = i
        
            MST[parent].append(child) # update the nodes
            visited.append(child)
            del Priority_Queue[child]
            
            for i in Priority_Queue: # update distances   
                if distances[child][i] < Priority_Queue[i]['distance']:
                    Priority_Queue[i]['distance'] = distances[child][i]
                    Priority_Queue[i]['parent'] = child
                    
    
        visited = [] # Convert MST to Hamiltonian path by DFS
        def Convert_MST_to_TSP(MST, root, visited):
            if root not in visited:
                visited.append(root)
                for child in MST[root]:
                    Convert_MST_to_TSP(MST, child, visited)
        
        Convert_MST_to_TSP(MST, initial_root, visited)
        
        total_distance = 0
        for i in range(len(visited) - 1):
            total_distance += distances[visited[i]][visited[i+1]]
        total_distance += distances[visited[0]][visited[-1]]
        
        quality = total_distance
        path = visited        
        
        if quality < best_quality:
            best_quality = quality
            best_path = path
            trace.update({round(time.time() - start_time, 2): quality})

    
    
    
    return best_quality, best_path, trace
