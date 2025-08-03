'''
Assignment 6, Part 1 : Medians and Order Statistics & Elementary Data Structures

Implementing selection algorithms in Python. There will be two implementations: deterministic selection (Median of Medians) and randomized selection (Randomized Quickselect). 
These will find the k-th smallest element in an array along with performance testing.

'''

import random
import time
import sys

# Increase recursion limit for large inputs.
sys. setrecursionlimit(20000)

# Randomized (Quickselect)

def quickselect_randomized(arr, k, low, high):
    if low == high:
        # Base case, only one element.
        return arr[low]
    
    # Partition and get pivot index
    pivot_index = _partition_random(arr, low, high)

    # Calculate pivot ranking
    pivot_rank = pivot_index - low + 1

    if k == pivot_rank:
        # Pivot is the k-th smallest element.
        return arr[pivot_index]
    elif k < pivot_rank:
    #k-th smallest in the left subarray
        return quickselect_randomized(arr, k, low, pivot_index - 1)
    else:
        # k-th smallest in the right subarray.
        return quickselect_randomized(arr, k - pivot_rank, pivot_index + 1, high)

# Helper function for randomized quickselect.    
def _partition_random(arr, low, high):
    #Chose random pivot.
    pivot_random = random. randint(low, high)
    # Swap pivot with last element.
    arr[pivot_random], arr[high] = arr[high], arr[pivot_random]
    return _partition (arr, low, high)

# Partition array around the last element (pivot).
def _partition(arr, low, high):
    pivot = arr[high]
    # Index of snaller element.
    i = low - 1 

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] =  arr[high], arr[i + 1]
    return i + 1

# Deterministic (Median of Medians)
def deterministic(arr, k):
    n =  len(arr)
    # Base Case.
    if n <= 10:
        arr.sort()
        return arr[k-1]
    
    # Divide array into groups.
    grp_num = (n + 4) // 5
    medians = []
    for i in range(grp_num):
        start = i * 5
        end = min(start + 5, n)
        grp = arr[start:end]
    
    # Find median of each group.
        grp.sort()
        median = grp[len(grp) // 2]
        medians.append(median)

    # Recursively find median of medians, pivot of main partition.
    if len(medians) == 1:
        pivot = medians[0]
    else:
        pivot = deterministic(medians, (len(medians) + 1) // 2)

    # Partition array around median of medians.
    pivot_in_arr = arr.index(pivot)
    arr[pivot_in_arr], arr[n - 1] = arr[n - 1], arr[pivot_in_arr] 

    pivot_index = _partition(arr, 0, n - 1)

    pivot_rank = pivot_index + 1

    if k == pivot_rank:
        return arr[pivot_index]
    elif k < pivot_rank:
        return deterministic(arr[:pivot_index], k)
    else:
        return deterministic(arr[pivot_index + 1:], k - pivot_rank)
    
# Performance Testing between two selection algorithms.

def selection_comparsion():
    print(" Performance Testing of Selection Algorithms.\n")
    sizes = [1000, 10000, 50000, 100000]
    values_k = [
        # Smallest element.
        lambda n: 1,
        # Median
        lambda n: n // 2,
        # Largest element.
        lambda n: n - 1
    ]

    for size in sizes:
        print(f"\n Testing for array size: {size}")

        # Creating different type of array.
        arr_random = [random.randint(1, size * 10) for _ in range(size)]
        arr_sorted = sorted(arr_random)
        arr_reverse_sorted = arr_sorted[::-1]

        # Different k values.
        for k_function in values_k:
            k = k_function(size)
            print(f" Finding the {k}-th smallest element.")

        # Testing Randomized Quickselect.
        # Make a copy.
        test_arr_random = list(arr_random)
        # Start time.
        start_time = time.perf_counter()
        result_rand = quickselect_randomized(test_arr_random, k, 0, len(test_arr_random)- 1)
        end_time = time.perf_counter()
        elapsed_time_rand = ((end_time - start_time) * 1000)
        print(f" Randomized Quickselect: {elapsed_time_rand} ms.")

        # Testing Deterministic (Median of Medians).
        # Make a copy.
        test_arr_deter = list(arr_random)
        # Start time.
        start_time = time.perf_counter()
        result_deter = deterministic(test_arr_deter, k)
        end_time = time.perf_counter()
        elapsed_time_deter = ((end_time - start_time) * 1000)
        print(f" Median of Medians: {elapsed_time_deter} ms.")

        # Verification.
        result_verify = sorted(arr_random)[k - 1]
        assert result_rand == result_verify, f"Randomized Quickselect failed for k={k}"
        assert result_deter == result_verify, f"Median of Medians failted for k={k}"

# Main 
if __name__ == "__main__":
    selection_comparsion()

