package model;

import java.util.*;

public class BellmanFord {
    public static String run(Graph graph, int start) {
        int V = graph.vertices;
        int[] dist = new int[V];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        for (int i = 1; i < V; i++) {
            for (Edge e : graph.edges) {
                if (dist[e.src] != Integer.MAX_VALUE && dist[e.src] + e.weight < dist[e.dest]) {
                    dist[e.dest] = dist[e.src] + e.weight;
                }
            }
        }

        // check for negative cycle
        for (Edge e : graph.edges) {
            if (dist[e.src] != Integer.MAX_VALUE && dist[e.src] + e.weight < dist[e.dest]) {
                return "Negative cycle detected";
            }
        }

        return Arrays.toString(dist);
    }
}