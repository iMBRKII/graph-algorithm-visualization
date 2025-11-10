import heapq

def run_dijkstra(graph_data, start_node, end_node):
    """
    Executes Dijkstra's algorithm to find the shortest path from a start to an end node.
    """
    node_names = graph_data["nodeNames"]
    edges = graph_data["edges"]
    num_vertices = len(node_names)

    # Create adjacency list
    adj = {i: [] for i in range(num_vertices)}
    for edge in edges:
        adj[edge["source"]].append((edge["destination"], edge["weight"]))

    dist = {i: float('inf') for i in range(num_vertices)}
    parent = {i: -1 for i in range(num_vertices)}
    dist[start_node] = 0
    
    pq = [(0, start_node)] # (distance, node_index)
    steps = 0

    while pq:
        steps += 1
        d, u = heapq.heappop(pq)

        if u == end_node:
            break # Optimization

        if d > dist[u]:
            continue

        for v, weight in adj.get(u, []):
            steps += 1
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    # Reconstruct path
    if dist[end_node] == float('inf'):
        return f"No path found from {node_names[start_node]} to {node_names[end_node]}.\n\nComputational Steps: {steps}"

    path = []
    curr = end_node
    while curr != -1:
        path.append(node_names[curr])
        curr = parent[curr]
    path.reverse()

    return f"Path: {' -> '.join(path)}\nTotal Cost: {dist[end_node]}\n\nComputational Steps: {steps}"
