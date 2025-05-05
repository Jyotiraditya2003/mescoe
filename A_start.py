# Define the graph with neighbors and weights
graph = {
    'S': [('A', 3), ('D', 4)],
    'A': [('B', 4), ('D', 5)],
    'B': [('C', 4), ('E', 5)],
    'C': [],
    'D': [('E', 2), ('A', 5)],
    'E': [('B', 5), ('F', 4)],
    'F': [('G', 3.5)],
    'G': []
}

# Heuristic values for each node (estimated cost to goal)
heuristic = {
    'S': 11.5, 'A': 10.5, 'B': 5.8, 'C': 3.4,
    'D': 9.2,  'E': 7.1,  'F': 3.5, 'G': 0
}

def a_star(start, goal):
    open_set = {start}
    closed_set = set()
    g_cost = {start: 0}
    parent = {start: None}

    while open_set:
        # Choose node with lowest f(n) = g(n) + h(n)
        current = min(open_set, key=lambda node: g_cost[node] + heuristic.get(node, float('inf')))

        if current == goal:
            # Reconstruct the path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            print("Path found:", path[::-1])
            return

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor in closed_set:
                continue

            tentative_g = g_cost[current] + weight

            if neighbor not in open_set or tentative_g < g_cost.get(neighbor, float('inf')):
                g_cost[neighbor] = tentative_g
                parent[neighbor] = current
                open_set.add(neighbor)

    print("Path does not exist!")

# ---- User Input ----
start = input("Enter start node: ").strip().upper()
end = input("Enter end node: ").strip().upper()

if start not in graph or end not in graph:
    print("Invalid start or end node.")
else:
    a_star(start, end)
