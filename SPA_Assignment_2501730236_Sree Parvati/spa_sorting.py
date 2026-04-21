#Sorting Performance Analyzer (SPA)
# Unit 3 Assignment

import time
import random
import sys

# Fix recursion depth issue for Quick Sort
sys.setrecursionlimit(20000)


# 1. Insertion Sort (Stable, In-place)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key



# 2. Merge Sort (Stable, Out-of-place)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



# 3. Quick Sort (In-place, Not Stable)
def partition(arr, low, high):
    pivot = arr[high]  # last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)



# 4. Correctness Check
def check_correctness():
    test = [5, 2, 9, 1, 5, 6]

    expected = sorted(test)

    arr1 = test.copy()
    insertion_sort(arr1)

    arr2 = merge_sort(test.copy())

    arr3 = test.copy()
    quick_sort(arr3, 0, len(arr3) - 1)

    print("\nCorrectness Check:")
    print("Insertion:", arr1)
    print("Merge    :", arr2)
    print("Quick    :", arr3)

    assert arr1 == expected, "Insertion Sort failed!"
    assert arr2 == expected, "Merge Sort failed!"
    assert arr3 == expected, "Quick Sort failed!"

    print("All algorithms are correct!\n")



# 5. Timing Function
def measure_time(sort_func, arr, is_quick=False):
    arr_copy = arr.copy()

    start = time.perf_counter()

    if is_quick:
        sort_func(arr_copy, 0, len(arr_copy) - 1)
    else:
        result = sort_func(arr_copy)
        if result is not None:
            arr_copy = result

    end = time.perf_counter()

    return (end - start) * 1000  # milliseconds



# 6. Dataset Generators
def generate_random_list(size):
    return [random.randint(1, 100000) for _ in range(size)]


def generate_sorted_list(size):
    return list(range(1, size + 1))


def generate_reverse_sorted_list(size):
    return list(range(size, 0, -1))



# 7. Main Execution
if __name__ == "__main__":

    random.seed(42)

    # Step 1: Correctness Check
    check_correctness()

    sizes = [1000, 5000, 10000]

    print("Size | Type | Insertion(ms) | Merge(ms) | Quick(ms)")
    print("-" * 65)

    with open("output.txt", "w") as f:
        f.write("Size | Type | Insertion(ms) | Merge(ms) | Quick(ms)\n")
        f.write("-" * 65 + "\n")

        for size in sizes:

            random_data = generate_random_list(size)
            sorted_data = generate_sorted_list(size)
            reverse_data = generate_reverse_sorted_list(size)

            datasets = [
                ("Random", random_data),
                ("Sorted", sorted_data),
                ("Reverse", reverse_data)
            ]

            for dtype, data in datasets:

                t1 = measure_time(insertion_sort, data)
                t2 = measure_time(merge_sort, data)
                t3 = measure_time(quick_sort, data, is_quick=True)

                line = f"{size} | {dtype} | {t1:.2f} | {t2:.2f} | {t3:.2f}"

                print(line)
                f.write(line + "\n")