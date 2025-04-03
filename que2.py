import heapq

def match_requests_with_sellers(requests, sellers):
    equipment_map = {}
    
    for equipment, price in sellers:
        if equipment not in equipment_map:
            equipment_map[equipment] = []
        heapq.heappush(equipment_map[equipment], price)
    
    result = []
    
    for equipment, max_price in requests:
        if equipment in equipment_map:
            while equipment_map[equipment] and equipment_map[equipment][0] > max_price:
                heapq.heappop(equipment_map[equipment]) 
            
            if equipment_map[equipment]:
                result.append(heapq.heappop(equipment_map[equipment])) 
            else:
                result.append(None)  
        else:
            result.append(None) 
    
    return result

requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]
print(match_requests_with_sellers(requests, sellers))
