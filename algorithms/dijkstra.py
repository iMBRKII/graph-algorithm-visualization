import heapq

def run_dijkstra(graph_data, start_node, end_node):
    """
    Executes Dijkstra's algorithm to find the shortest path from a start to an end node.
    
    Algorithm: Uses a greedy approach with a min-heap priority queue.
    Always processes the node with the smallest known distance first.
    Time Complexity: O((V + E) log V) where V = vertices, E = edges
    Space Complexity: O(V + E)
    """
    # Extract graph information
    node_names = graph_data["nodeNames"]
    edges = graph_data["edges"]
    num_vertices = len(node_names)  

    # ===== BUILD ADJACENCY LIST =====
    # Create an adjacency list representation of the graph for fast neighbor lookup
    # Ex: adj[0] = [(1, 5), (2, 3)] means node 0 connects to nodes 1 and 2 with weights 5 and 3
    adj = {i: [] for i in range(num_vertices)}
    for edge in edges:
        # Add each edge to the source node's adjacency list
        adj[edge["source"]].append((edge["destination"], edge["weight"]))

    # ===== INITIALIZE DISTANCE AND PARENT TRACKING =====
    dist = {i: float('inf') for i in range(num_vertices)}  # Distance to each node (start as infinity)
    parent = {i: -1 for i in range(num_vertices)}  # Previous node in shortest path (for reconstruction)
    dist[start_node] = 0  # Distance to start node is 0
    
    pq = [(0, start_node)]  
    steps = 0  

    # ===== MAIN ALGORITHM LOOP =====
    while pq:
        steps += 1
        # Extract node with smallest distance from the priority queue
        d, u = heapq.heappop(pq)

        # Early termination: Stop once we reach the destination
        if u == end_node:
            break

        # If this distance is worse than our best known distance, skip it
        if d > dist[u]:
            continue

        # ===== RELAXATION LOOP =====
        # Check all neighbors of the current node for potential shorter paths
        for v, weight in adj.get(u, []):
            steps += 1
            # Check if we found a shorter path to neighbor v through current node u
            if dist[u] + weight < dist[v]:
                # Update the distance to v
                dist[v] = dist[u] + weight
                # Record u as the parent of v (for path reconstruction)
                parent[v] = u
                # Add v to priority queue with new distance for processing
                heapq.heappush(pq, (dist[v], v))


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
