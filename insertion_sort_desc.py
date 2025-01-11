def insertion_sort_desc(arr):
    # Loop through each element in the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are smaller than key to one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key in its correct position
        arr[j + 1] = key

    return arr

# Example usage
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Original array:", data)
    sorted_array = insertion_sort_desc(data)
    print("Sorted array in descending order:", sorted_array)
