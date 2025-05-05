import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v, weight):
        # Undirected graph: add both directions
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def prim_mst(self, start):
        visited = set()
        min_heap = [(0, start, -1)]  # (weight, current_node, parent)
        mst = []
        total_weight = 0

        while min_heap:
            weight, u, parent = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            if parent != -1:
                mst.append((parent, u, weight))
                total_weight += weight

            for neighbor, edge_weight in self.adj_list[u]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, u))

        print("\nEdges in MST:")
        for u, v, weight in mst:
            print(f"{u} - {v} (weight: {weight})")
        print("Total weight of MST:", total_weight)

# --- User Input Section ---
g = Graph()

# Input number of vertices and edges
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

# Input edges
print("Enter edges in the format: u v weight")
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

# Input starting node
start_node = int(input("Enter the starting node for Prim's algorithm: "))

# Run Prim's MST
g.prim_mst(start=start_node)

# Enter the number of vertices: 6  
# Enter the number of edges: 7  
# Enter edges in the format: u v weight  
# 0 1 4  
# 0 2 3  
# 1 2 1  
# 1 3 2  
# 2 3 4  
# 3 4 2  
# 4 5 6  
# Enter the starting node for Prim's algorithm: 0