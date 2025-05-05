def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the i-th element is the minimum
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Example usage
data = []
n= int(input("How many numbers to add"))
for i in range(n):
    x = int(input("Enter number:"))
    data.append(x)
sorted_data = selection_sort(data)
print("Sorted array:", sorted_data)