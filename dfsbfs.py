graph = {}
n = int(input("Enter the number of nodes in the graph: "))
print("Enter the edges (e.g., '0 1' for an edge between 0 and 1). Type 'done' to finish:")

while True:
    edge = input()
    if edge.lower() == 'done':
        break
    u, v = edge.split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

# DFS function (recursive)
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# BFS function (iterative)
def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Start traversal
start_node = input("Enter the starting node: ")
print("\nDepth-First Search (DFS):")
dfs(set(), graph, start_node)

print("\n\nBreadth-First Search (BFS):")
bfs(graph, start_node)

# Enter the number of nodes in the graph: 5
# Enter the edges (e.g., '0 1' for an edge between 0 and 1). Type 'done' to finish:
# 0 1
# 0 2
# 1 3
# 1 4
# done
# Enter the starting node: 0