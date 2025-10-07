package utils;

import model.Graph;
import java.util.Random;

public class GraphGenerator {
    public static Graph generateRandomGraph(int vertices, int edges) {
        Graph g = new Graph();
        g.vertices = vertices;
        Random rand = new Random();

        for (int i = 0; i < edges; i++) {
            int src = rand.nextInt(vertices);
            int dest = rand.nextInt(vertices);
            int weight = 1 + rand.nextInt(20);
            if (src != dest) g.addEdge(src, dest, weight);
        }
        return g;
    }
}