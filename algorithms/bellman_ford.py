def run_bellman_ford(graph_data, start_node, end_node):
    """
    Executes the Bellman-Ford algorithm to find the shortest path, detecting negative cycles.
    """
    node_names = graph_data["nodeNames"]
    edges = graph_data["edges"]
    num_vertices = len(node_names)

    dist = {i: float('inf') for i in range(num_vertices)}
    parent = {i: -1 for i in range(num_vertices)}
    dist[start_node] = 0
    steps = 0

    # Relax edges repeatedly
    for i in range(num_vertices - 1):
        for edge in edges:
            steps += 1
            u, v, w = edge["source"], edge["destination"], edge["weight"]
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # Check for negative weight cycles
    for edge in edges:
        steps += 1
        u, v, w = edge["source"], edge["destination"], edge["weight"]
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return f"Negative weight cycle detected.\nCannot calculate shortest path.\n\nComputational Steps: {steps}"

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
