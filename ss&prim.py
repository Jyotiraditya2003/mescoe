import heapq

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", arr)


def prims_algorithm_adj_list(adj_list, n):
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    total_weight = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        for v, w in adj_list[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                if weight != 0:
                    mst_edges.append((u, v, w))

    print("Edges in MST (Prim's):", mst_edges)
    print("Total MST cost (Prim's):", total_weight)


# --- Main Menu ---
while True:
    print("\n--- Greedy Algorithm Applications ---")
    print("1. Selection Sort")
    print("2. Prim's MST Algorithm")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        arr = list(map(int, input("Enter array elements (space-separated): ").split()))
        selection_sort(arr)

    elif choice == 2:
        n = int(input("Enter number of vertices: "))
        e = int(input("Enter number of edges: "))
        adj_list = {i: [] for i in range(n)}
        for _ in range(e):
            u, v, w = map(int, input("Enter edge (u v weight): ").split())
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
        prims_algorithm_adj_list(adj_list, n)

    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")