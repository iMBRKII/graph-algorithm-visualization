def run_bellman_ford(graph_data, start_node, end_node):
    """
    Executes the Bellman-Ford algorithm to find the shortest path, detecting negative cycles.
    
    Algorithm: Relaxes all edges repeatedly (V-1) times, then checks for negative cycles.
    Unlike Dijkstra, this works with NEGATIVE edge weights.
    Time Complexity: O(V * E) where V = vertices, E = edges
    Space Complexity: O(V)
    """
    # Extract graph information
    node_names = graph_data["nodeNames"]
    edges = graph_data["edges"]
    num_vertices = len(node_names)

    # ===== INITIALIZE DISTANCES AND TRACKING =====
    dist = {i: float('inf') for i in range(num_vertices)}  # Distance to each node (start as infinity)
    parent = {i: -1 for i in range(num_vertices)}  # Previous node in shortest path (for reconstruction)
    dist[start_node] = 0  # Distance to start node is 0
    steps = 0

    # ===== MAIN RELAXATION LOOP =====
    # Repeat (V-1) times to ensure all shortest paths are found
    # After V-1 relaxations, all shortest paths in a graph without negative cycles are guaranteed to be found
    for i in range(num_vertices - 1):
        # ===== EDGE RELAXATION =====
        # Try to relax every edge in the graph
        for edge in edges:
            steps += 1
            # Extract edge information
            u, v, w = edge["source"], edge["destination"], edge["weight"]
            
            # Check if we found a shorter path to node v through node u
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                # Update distance to v
                dist[v] = dist[u] + w
                # Record u as parent of v (for path reconstruction)
                parent[v] = u

    # ===== NEGATIVE CYCLE DETECTION =====
    # If we can still relax edges after V-1 iterations, there's a negative cycle
    for edge in edges:
        steps += 1
        u, v, w = edge["source"], edge["destination"], edge["weight"]
        
        # If distance can still be reduced, there's a negative weight cycle
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return f"Negative weight cycle detected.\nCannot calculate shortest path.\n\nComputational Steps: {steps}"


    # Check if a path to the end node was found
    if dist[end_node] == float('inf'):
        return f"No path found from {node_names[start_node]} to {node_names[end_node]}.\n\nComputational Steps: {steps}"

    # Backtrack from end node to start node using parent pointers
    path = []
    curr = end_node
    while curr != -1:
        path.append(node_names[curr])
        curr = parent[curr]

    path.reverse()

    return f"Path: {' -> '.join(path)}\nTotal Cost: {dist[end_node]}\n\nComputational Steps: {steps}"
