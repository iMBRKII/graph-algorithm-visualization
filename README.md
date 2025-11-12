# Graph Algorithm Visualizer

This project is a desktop application that visualizes various graph algorithms. Users can select different graphs, choose from a set of algorithms, and see the results of running them.

## Features

*   **Visualize popular graph algorithms:**
    *   Dijkstra's Algorithm
    *   Bellman-Ford Algorithm
    *   Kruskal's Algorithm
*   **Interactive UI:**
    *   Select different graphs from the `data` directory.
    *   Choose the algorithm to run.
    *   Select start and end nodes for pathfinding algorithms.
    *   View the algorithm's output, execution time, and space complexity.
*   **Tkinter GUI:** The application is built using Python's standard GUI library, Tkinter.

## Cloning the Repository

To clone this repository to your local machine, run the following command in your terminal:

```bash
git clone https://github.com/iMBRKII/graph-algorithm-visualization
```

## Installation

1.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, execute the following command from the project's root directory:

```bash
python app.py
```

This will open the Graph Algorithm Visualizer window. From there, you can:

1.  Select an algorithm from the dropdown menu.
2.  If applicable, choose a start and end node.
3.  Click "Run Algorithm" to see the results.
4.  Click "Change Graph" to cycle through the available graphs in the `data` directory.
