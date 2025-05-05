class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []  # List to store all edges (u, v, weight)

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    # Find function with path compression
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # Union function by rank
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        self.edges.sort()  # Sort edges by weight
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        mst = []
        total_weight = 0

        for weight, u, v in self.edges:
            if self.find(parent, u) != self.find(parent, v):
                self.union(parent, rank, u, v)
                mst.append((u, v, weight))
                total_weight += weight

        print("\nEdges in MST:")
        for u, v, weight in mst:
            print(f"{u} - {v} (weight: {weight})")
        print("Total weight of MST:", total_weight)


# User input section
vertices = int(input("Enter the number of vertices: "))
edges_count = int(input("Enter the number of edges: "))

g = Graph(vertices)

print("Enter edges in the format: u v weight")
for _ in range(edges_count):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

g.kruskal_mst()
