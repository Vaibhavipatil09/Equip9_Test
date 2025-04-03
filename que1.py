from collections import deque

def find_nearest_equipment(n, edges, availability, start_provider, target_equipment):

    graph = {i: [] for i in range(1, n+1)}
    for a, b in edges:
        graph[a].append(b)  
    

    queue = deque([(start_provider, [start_provider])])
    visited = set([start_provider])
    
    while queue:
        current, path = queue.popleft()
        

        if target_equipment in availability.get(current, []):
            return path
        
   
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    
    return -1  


n = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]  
availability = {1: ["excavator"], 2: [], 3: ["bulldozer"], 4: ["excavator"], 5: ["crane"]}
start_provider = 2
target_equipment = "excavator"

print(find_nearest_equipment(n, edges, availability, start_provider, target_equipment))
