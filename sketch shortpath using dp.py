import heapq

# Initialize memoization dictionary
mem = {}

# Dynamic programming function to find the shortest path
def dp_shortpath(s, v, neighbors, weights):
    """
    s: source vertex
    v: target vertex
    neighbors: adjacency list of the graph
    weights: dictionary with edge weights {(u, v): weight}
    """
    if v in mem:
        return mem[v]
    
    if s == v:
        return 0
    
    minheap = []
    for u in neighbors[v]:
        if (u, v) in weights:
            heapq.heappush(minheap, dp_shortpath(s, u, neighbors, weights) + weights[(u, v)])
    
    if minheap:
        mem[v] = heapq.heappop(minheap)
        return mem[v]
    else:
        return float('inf')  # Return infinity if no path exists

# Example usage
# Define the graph as an adjacency list and edge weights
neighbors = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: []
}
weights = {
    (0, 1): 1,
    (0, 2): 4,
    (1, 2): 2,
    (1, 3): 6,
    (2, 3): 3
}

# Find the shortest path from source (0) to target (3)
source = 0
target = 3
shortest_path_weight = dp_shortpath(source, target, neighbors, weights)
print(f"Shortest path weight from {source} to {target}: {shortest_path_weight}")

