package model;

import java.util.*;

public class Dijkstra {
    public static String run(Graph graph, int start) {
        int V = graph.vertices;
        int[] dist = new int[V];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.add(new int[]{start, 0});

        while (!pq.isEmpty()) {
            int[] node = pq.poll();
            int u = node[0];
            int d = node[1];
            if (d > dist[u]) continue;

            for (Edge e : graph.adjList.getOrDefault(u, new ArrayList<>())) {
                int v = e.dest, w = e.weight;
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.add(new int[]{v, dist[v]});
                }
            }
        }

        return Arrays.toString(dist);
    }
}