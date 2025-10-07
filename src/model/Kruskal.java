package model;

import java.util.*;

public class Kruskal {
    static class DisjointSet {
        int[] parent, rank;
        DisjointSet(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        int find(int x) { return parent[x] == x ? x : (parent[x] = find(parent[x])); }
        void union(int x, int y) {
            int rx = find(x), ry = find(y);
            if (rx == ry) return;
            if (rank[rx] < rank[ry]) parent[rx] = ry;
            else if (rank[ry] < rank[rx]) parent[ry] = rx;
            else { parent[ry] = rx; rank[rx]++; }
        }
    }

    public static String run(Graph graph) {
        List<Edge> edges = new ArrayList<>(graph.edges);
        edges.sort(Comparator.comparingInt(e -> e.weight));
        DisjointSet ds = new DisjointSet(graph.vertices);
        List<Edge> mst = new ArrayList<>();

        for (Edge e : edges) {
            if (ds.find(e.src) != ds.find(e.dest)) {
                mst.add(e);
                ds.union(e.src, e.dest);
            }
        }

        StringBuilder sb = new StringBuilder("MST Edges:\n");
        for (Edge e : mst) sb.append(e.src).append(" -> ").append(e.dest).append(" (w=").append(e.weight).append(")\n");
        return sb.toString();
    }
}