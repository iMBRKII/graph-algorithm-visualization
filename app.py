import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import glob
import time
from PIL import Image, ImageTk

# Import algorithm functions
from algorithms.dijkstra import run_dijkstra
from algorithms.bellman_ford import run_bellman_ford
from algorithms.kruskal import run_kruskal

class GraphAlgorithmVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Algorithm Visualizer")
        self.root.geometry("1100x700")

        # --- Data ---
        self.graph_files = sorted(glob.glob("data/*.json"))
        if not self.graph_files:
            messagebox.showerror("Error", "No graph data files found in 'data/' directory.")
            root.destroy()
            return
        self.current_graph_index = 0
        self.current_graph_data = None

        # --- UI Frames ---
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.left_frame = ttk.Frame(self.main_frame, width=250)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        self.left_frame.pack_propagate(False)

        self.center_frame = ttk.Frame(self.main_frame)
        self.center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_frame = ttk.Frame(self.main_frame, width=300)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))
        self.right_frame.pack_propagate(False)

        # --- Left Frame (Controls) ---
        ttk.Label(self.left_frame, text="Controls", font=("Helvetica", 16, "bold")).pack(pady=10)

        self.algo_selector = ttk.Combobox(self.left_frame, values=["Dijkstra", "Bellman-Ford", "Kruskal"], state="readonly")
        self.algo_selector.set("Select Algorithm")
        self.algo_selector.pack(fill=tk.X, pady=5)
        self.algo_selector.bind("<<ComboboxSelected>>", self.on_algorithm_select)

        self.start_node_selector = ttk.Combobox(self.left_frame, state="readonly")
        self.start_node_selector.set("Start Node")
        self.start_node_selector.pack(fill=tk.X, pady=5)

        self.end_node_selector = ttk.Combobox(self.left_frame, state="readonly")
        self.end_node_selector.set("End Node")
        self.end_node_selector.pack(fill=tk.X, pady=5)

        ttk.Button(self.left_frame, text="Run Algorithm", command=self.run_algorithm).pack(fill=tk.X, pady=10)
        ttk.Button(self.left_frame, text="Change Graph", command=self.change_graph).pack(fill=tk.X, pady=5)
        ttk.Button(self.left_frame, text="Reset", command=self.reset).pack(fill=tk.X, pady=5)

        # --- Center Frame (Graph Image) ---
        self.graph_image_label = ttk.Label(self.center_frame)
        self.graph_image_label.pack(fill=tk.BOTH, expand=True)

        # --- Right Frame (Results) ---
        ttk.Label(self.right_frame, text="Results", font=("Helvetica", 16, "bold")).pack(pady=10)
        self.time_label = ttk.Label(self.right_frame, text="Execution Time: N/A")
        self.time_label.pack(fill=tk.X, pady=5)
        self.space_label = ttk.Label(self.right_frame, text="Space Complexity: N/A")
        self.space_label.pack(fill=tk.X, pady=5)
        
        self.result_text = tk.Text(self.right_frame, wrap=tk.WORD, height=15)
        self.result_text.pack(fill=tk.BOTH, expand=True, pady=10)

        # --- Initial Load ---
        self.load_graph()

    def load_graph(self):
        filepath = self.graph_files[self.current_graph_index]
        with open(filepath, 'r') as f:
            self.current_graph_data = json.load(f)

        # Load image
        try:
            img = Image.open(self.current_graph_data['imagePath'])
            # Resize image to fit the center frame
            img.thumbnail((self.center_frame.winfo_width() or 600, self.center_frame.winfo_height() or 600))
            self.graph_photo = ImageTk.PhotoImage(img)
            self.graph_image_label.config(image=self.graph_photo)
        except FileNotFoundError:
            self.graph_image_label.config(image=None, text=f"Image not found:\n{self.current_graph_data['imagePath']}")
        
        # Update node selectors
        node_names = self.current_graph_data["nodeNames"]
        self.start_node_selector['values'] = node_names
        self.end_node_selector['values'] = node_names
        self.reset()

    def change_graph(self):
        self.current_graph_index = (self.current_graph_index + 1) % len(self.graph_files)
        
        # Handle Dijkstra constraint
        selected_algo = self.algo_selector.get()
        if selected_algo == "Dijkstra":
            start_index = self.current_graph_index
            while True:
                filepath = self.graph_files[self.current_graph_index]
                with open(filepath, 'r') as f:
                    graph_info = json.load(f)
                if not graph_info["hasNegativeWeights"]:
                    break
                self.current_graph_index = (self.current_graph_index + 1) % len(self.graph_files)
                if self.current_graph_index == start_index:
                    messagebox.showwarning("Warning", "No graphs suitable for Dijkstra's algorithm found.")
                    break
        
        self.load_graph()

    def on_algorithm_select(self, event=None):
        selected_algo = self.algo_selector.get()
        is_kruskal = selected_algo == "Kruskal"
        
        self.start_node_selector.config(state=tk.DISABLED if is_kruskal else "readonly")
        self.end_node_selector.config(state=tk.DISABLED if is_kruskal else "readonly")

        if selected_algo == "Dijkstra" and self.current_graph_data["hasNegativeWeights"]:
            messagebox.showwarning("Warning", "Dijkstra's algorithm may not work with negative weights. Consider changing the graph.")

    def run_algorithm(self):
        algo = self.algo_selector.get()
        if algo == "Select Algorithm":
            messagebox.showerror("Error", "Please select an algorithm.")
            return

        start_time = time.time()
        result = ""
        space = "N/A"

        if algo == "Kruskal":
            result = run_kruskal(self.current_graph_data)
            space = "O(V + E)"
        else:
            start_name = self.start_node_selector.get()
            end_name = self.end_node_selector.get()
            if not start_name or start_name == "Start Node" or not end_name or end_name == "End Node":
                messagebox.showerror("Error", "Please select a start and end node.")
                return
            
            start_node = self.current_graph_data["nodeNames"].index(start_name)
            end_node = self.current_graph_data["nodeNames"].index(end_name)

            if algo == "Dijkstra":
                result = run_dijkstra(self.current_graph_data, start_node, end_node)
                space = "O(V + E)"
            elif algo == "Bellman-Ford":
                result = run_bellman_ford(self.current_graph_data, start_node, end_node)
                space = "O(V)"

        end_time = time.time()
        exec_time = (end_time - start_time) * 1000  # in ms

        self.time_label.config(text=f"Execution Time: {exec_time:.4f} ms")
        self.space_label.config(text=f"Space Complexity: {space}")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)

    def reset(self):
        self.time_label.config(text="Execution Time: N/A")
        self.space_label.config(text="Space Complexity: N/A")
        self.result_text.delete("1.0", tk.END)
        self.start_node_selector.set("Start Node")
        self.end_node_selector.set("End Node")

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphAlgorithmVisualizer(root)
    root.mainloop()
