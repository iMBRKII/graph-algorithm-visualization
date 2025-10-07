package app;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import model.*;
import utils.GraphGenerator;

public class Main extends Application {
    private ComboBox<String> algorithmSelector;
    private Pane graphPane;
    private Label timeLabel;
    private TextArea resultArea;
    private Graph graph;

    @Override
    public void start(Stage stage) {
        // Top: Title
        Label title = new Label("Graph Algorithms Visualizer");
        title.setStyle("-fx-font-size: 18px; -fx-font-weight: bold;");
        BorderPane.setAlignment(title, Pos.CENTER);

        // Left: Controls
        algorithmSelector = new ComboBox<>();
        algorithmSelector.getItems().addAll("Dijkstra", "Bellman-Ford", "Kruskal");
        algorithmSelector.setPromptText("Select Algorithm");

        Button generateBtn = new Button("Generate Graph");
        generateBtn.setOnAction(e -> onGenerateGraph());

        Button runBtn = new Button("Run Algorithm");
        runBtn.setOnAction(e -> onRunAlgorithm());

        Button resetBtn = new Button("Reset");
        resetBtn.setOnAction(e -> onReset());

        VBox leftBox = new VBox(10, algorithmSelector, generateBtn, runBtn, resetBtn);
        leftBox.setAlignment(Pos.CENTER);
        leftBox.setPadding(new Insets(10));

        // Center: Graph Pane
        graphPane = new Pane();
        graphPane.setStyle("-fx-background-color: #f4f4f4;");

        // Right: Results
        timeLabel = new Label("Execution Time: ");
        resultArea = new TextArea();
        resultArea.setPrefWidth(200);
        resultArea.setPrefHeight(300);

        VBox rightBox = new VBox(10, timeLabel, resultArea);
        rightBox.setAlignment(Pos.CENTER_LEFT);
        rightBox.setPadding(new Insets(10));

        // Layout
        BorderPane root = new BorderPane();
        root.setTop(title);
        root.setLeft(leftBox);
        root.setCenter(graphPane);
        root.setRight(rightBox);

        // Scene
        Scene scene = new Scene(root, 900, 600);
        stage.setTitle("Graph Algorithms Visualizer");
        stage.setScene(scene);
        stage.show();

        // Initialize graph
        graph = new Graph();
    }

    private void onGenerateGraph() {
        graph = GraphGenerator.generateRandomGraph(10, 20);
        graph.displayOn(graphPane);
    }

    private void onRunAlgorithm() {
        String choice = algorithmSelector.getValue();
        if (choice == null) return;
        long start = System.nanoTime();
        String result = "";

        switch (choice) {
            case "Dijkstra" -> result = Dijkstra.run(graph, 0);
            case "Bellman-Ford" -> result = BellmanFord.run(graph, 0);
            case "Kruskal" -> result = Kruskal.run(graph);
        }

        long end = System.nanoTime();
        double timeMs = (end - start) / 1e6;
        timeLabel.setText("Execution Time: " + timeMs + " ms");
        resultArea.setText(result);
    }

    private void onReset() {
        graphPane.getChildren().clear();
        resultArea.clear();
        timeLabel.setText("Execution Time: ");
    }

    public static void main(String[] args) {
        launch();
    }
}