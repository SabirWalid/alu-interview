#!/usr/bin/python3
def rain(walls):
    if not walls:
        return 0
    
    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n
    
    # Calculate the maximum height to the left of each wall
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])
    
    # Calculate the maximum height to the right of each wall
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])
    
    # Calculate the amount of water retained at each position
    total_water = 0
    for i in range(n):
        total_water += min(left_max[i], right_max[i]) - walls[i]
    
    return total_water

# Example usage:
walls = [0,1,0,2,1,0,1,3,2,1,2,1]
print(rain(walls))  
