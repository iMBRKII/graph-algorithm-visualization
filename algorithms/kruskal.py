class DisjointSet:
    """
    A Disjoint Set Union (DSU) data structure, also known as Union-Find.
    
    Used by Kruskal's algorithm to track connected components.
    Operations: find() and union() both use path compression for optimization.
    Time Complexity: Nearly O(1) amortized per operation
    """
    def __init__(self, n):
        self.parent = list(range(n)) 
        self.steps = 0 

    def find(self, i):
        """
        Find the root (representative) of the set containing element i.
        Uses path compression: directly links i to its root for future O(1) lookups.
        """
        self.steps += 2
        
        if self.parent[i] == i:
            return i
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        self.steps += 1
        
        root_i = self.find(i)
        root_j = self.find(j)
        
        # If roots are different, merge the sets
        if root_i != root_j:
            self.parent[root_i] = root_j  # Make root_j the parent of root_i
            return True
        return False  # Already in same set, no merge needed


def run_kruskal(graph_data):
    """
    Executes Kruskal's algorithm to find the Minimum Spanning Tree (MST).
    
    Algorithm: Greedily selects the smallest weight edges that don't create cycles.
    The result is a tree that connects all vertices with minimum total weight.
    Time Complexity: O(E log E) where E = number of edges
    Space Complexity: O(V + E) where V = vertices
    """
    
    # Extract graph information
    node_names = graph_data["nodeNames"] 
    edges = graph_data["edges"]
    num_vertices = len(node_names)
    steps = 0 
    
    # ===== SORT EDGES BY WEIGHT =====
    # Sort all edges in ascending order by weight
    # This ensures we try to add the smallest edges first (greedy approach)
    sorted_edges = sorted(edges, key=lambda item: item['weight'])
    steps += len(sorted_edges) * (len(sorted_edges) - 1) // 2
    
    # ===== INITIALIZE DISJOINT SET =====
    # Create DSU to track which nodes are connected
    dsu = DisjointSet(num_vertices)
    
    # Track the MST edges and total weight
    mst = []
    total_weight = 0  

    # ===== MAIN KRUSKAL LOOP =====
    # Try to add each edge to the MST (in order of increasing weight)
    for edge in sorted_edges:
        steps += 1
        # Try to union the two nodes of this edge
        # Returns True if they weren't already connected (no cycle would form)
        if dsu.union(edge["source"], edge["destination"]):
            mst.append(edge)
            total_weight += edge["weight"]

    steps += dsu.steps


    output = "Minimum Spanning Tree Edges:\n"
    for edge in mst:
        output += f"{node_names[edge['source']]} - {node_names[edge['destination']]} ({edge['weight']})\n"
    
    output += f"\nTotal Weight: {total_weight}\n"
    output += f"\nComputational Steps: {steps}"
    
    return output
