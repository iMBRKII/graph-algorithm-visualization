class DisjointSet:
    """A simple Disjoint Set Union (DSU) implementation for Kruskal's algorithm."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.steps = 0

    def find(self, i):
        self.steps += 2
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        self.steps += 1
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def run_kruskal(graph_data):
    """
    Executes Kruskal's algorithm to find the Minimum Spanning Tree (MST).
    """
    node_names = graph_data["nodeNames"]
    edges = graph_data["edges"]
    num_vertices = len(node_names)
    
    steps = 0
    
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda item: item['weight'])
    steps += len(sorted_edges) * (len(sorted_edges) - 1) // 2 # Approx sort cost
    
    dsu = DisjointSet(num_vertices)
    mst = []
    total_weight = 0

    for edge in sorted_edges:
        steps += 1
        if dsu.union(edge["source"], edge["destination"]):
            mst.append(edge)
            total_weight += edge["weight"]

    steps += dsu.steps

    # Format output
    output = "Minimum Spanning Tree Edges:\n"
    for edge in mst:
        output += f"{node_names[edge['source']]} - {node_names[edge['destination']]} ({edge['weight']})\n"
    
    output += f"\nTotal Weight: {total_weight}\n"
    output += f"\nComputational Steps: {steps}"
    
    return output
