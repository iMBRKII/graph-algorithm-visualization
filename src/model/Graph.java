package model;

import javafx.scene.layout.Pane;
import java.util.*;

public class Graph {
    public int vertices;
    public List<Edge> edges;
    public Map<Integer, List<Edge>> adjList;

    public Graph() {
        this.vertices = 0;
        this.edges = new ArrayList<>();
        this.adjList = new HashMap<>();
    }

    public void addEdge(int src, int dest, int weight) {
        edges.add(new Edge(src, dest, weight));
        adjList.computeIfAbsent(src, k -> new ArrayList<>()).add(new Edge(src, dest, weight));
    }

    public void displayOn(Pane pane) {
        pane.getChildren().clear();
        int radius = 20;
        int centerX = 350, centerY = 250, bigRadius = 200;
        // Position nodes in a circle
        double[] xs = new double[vertices];
        double[] ys = new double[vertices];
        for (int i = 0; i < vertices; i++) {
            double angle = 2 * Math.PI * i / vertices;
            xs[i] = centerX + bigRadius * Math.cos(angle);
            ys[i] = centerY + bigRadius * Math.sin(angle);
        }

        // Draw edges
        for (Edge e : edges) {
            javafx.scene.shape.Line line = new javafx.scene.shape.Line(xs[e.src], ys[e.src], xs[e.dest], ys[e.dest]);
            line.setStroke(javafx.scene.paint.Color.GRAY);
            pane.getChildren().add(line);
            // Draw weight label
            double midX = (xs[e.src] + xs[e.dest]) / 2;
            double midY = (ys[e.src] + ys[e.dest]) / 2;
            javafx.scene.text.Text weightText = new javafx.scene.text.Text(midX, midY, String.valueOf(e.weight));
            weightText.setFill(javafx.scene.paint.Color.DARKRED);
            pane.getChildren().add(weightText);
        }

        // Draw nodes
        for (int i = 0; i < vertices; i++) {
            javafx.scene.shape.Circle circle = new javafx.scene.shape.Circle(xs[i], ys[i], radius);
            circle.setFill(javafx.scene.paint.Color.LIGHTBLUE);
            circle.setStroke(javafx.scene.paint.Color.DARKBLUE);
            pane.getChildren().add(circle);
            javafx.scene.text.Text label = new javafx.scene.text.Text(xs[i] - 6, ys[i] + 5, String.valueOf(i));
            label.setFill(javafx.scene.paint.Color.BLACK);
            pane.getChildren().add(label);
        }
    }
}
