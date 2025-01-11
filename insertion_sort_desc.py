def insertion_sort_desc(arr):
    # Placeholder for the sorting logic
    pass

if __name__ == "__main__":
    print("Insertion Sort in Descending Order")
# Commit 2: Core Implementation
def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Original array:", data)
    print("Sorted array in descending order:", insertion_sort_desc(data))
