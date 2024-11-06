import random

# Partition function for QuickSort
def partition(arr, start, end):
    # Step 1: Take a pivot
    pivot = arr[end]

    # Step 2: Count all elements < pivot
    count = 0
    for i in range(start, end):
        if arr[i] < pivot:
            count += 1

    # Step 3: Update pivot
    pivot_index = start + count
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    # Step 4: Place all smaller elements to the left of pivot and all larger elements to its right
    i, j = start, end
    while i < pivot_index and j > pivot_index:
        if arr[i] > arr[pivot_index] and arr[j] < arr[pivot_index]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            if arr[i] <= arr[pivot_index]:
                i += 1
            if arr[j] >= arr[pivot_index]:
                j -= 1

    return pivot_index


# Regular QuickSort function
def quick_sort(arr, start, end):
    if start >= end:
        return

    partition_index = partition(arr, start, end)
    quick_sort(arr, start, partition_index - 1)
    quick_sort(arr, partition_index + 1, end)


# Randomized QuickSort function
def randomized_quick_sort(arr, start, end):
    if start >= end:
        return

    # Randomize pivot selection by picking a random index and swapping with the end
    random_index = random.randint(start, end)
    arr[random_index], arr[end] = arr[end], arr[random_index]

    partition_index = partition(arr, start, end)
    randomized_quick_sort(arr, start, partition_index - 1)
    randomized_quick_sort(arr, partition_index + 1, end)


# Main function to test QuickSort
if __name__ == "__main__":
    arr = [5, 1, 1, 2, 0, 0]
    print("Original array:", arr)

    # Testing regular quick_sort
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array using regular QuickSort:", arr)

    # Testing randomized quick_sort
    arr = [5, 1, 1, 2, 0, 0]
    randomized_quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array using Randomized QuickSort:", arr)


# ### Explanation of the Algorithm:

# **QuickSort** is a highly efficient sorting algorithm that uses a divide-and-conquer strategy. It works by selecting a pivot element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The algorithm then recursively sorts the sub-arrays.

# ### QuickSort Steps:

# 1. **Pivot Selection**: Choose an element as the pivot. In this case, we first select the last element of the array as the pivot.
   
# 2. **Partitioning**: Rearrange the array such that elements smaller than the pivot come before it, and elements greater than the pivot come after it. After partitioning, the pivot is placed at its correct position.

# 3. **Recursive Sorting**: Recursively sort the sub-arrays formed by partitioning the array.

# ### Time and Space Complexity:

# - **Time Complexity**:
#   - **Best and Average Case**: \( O(n \log n) \), where `n` is the number of elements in the array.
#   - **Worst Case**: \( O(n^2) \), which occurs when the array is already sorted or reverse sorted, and the pivot divides the array into sub-arrays of size \( n-1 \) and 0.
  
# - **Space Complexity**:
#   - **O(\log n)**, for the recursion stack in the average case (due to the divide-and-conquer nature).

# ### Why Randomized QuickSort?

# The randomized version of QuickSort improves the average performance by selecting a random pivot element. This helps to avoid the worst-case time complexity (\( O(n^2) \)) that arises when the pivot always divides the array into highly uneven partitions (such as in the case of sorted or reverse-sorted arrays). Randomized QuickSort ensures a better chance of balanced partitioning and thus achieves \( O(n \log n) \) on average.

