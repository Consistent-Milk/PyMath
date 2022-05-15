# A program to compare time taken for various sorting algorithms to sort a random list of integers.
# Sorting algorithms tested till now:
# 1) Bead Sort
# 2) Bubble Sort
# 3) Quick Sort
# 4) Tim Sort/CPython default sorting algorithm.

import random
import timeit

sequence = random.sample(range(1, 10000), 500)

def bead_sort(sequence: list) -> list:
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("Sequence must be list of non-negative integers")
    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower
    return sequence

def bubble_sort(collection: list) -> list:
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection

def quick_sort(collection: list) -> list:
    if len(collection) < 2:
        return collection
    pivot = collection.pop()  # Use the last element as the first pivot
    greater: list[int] = []  # All elements greater than pivot
    lesser: list[int] = []  # All elements less than or equal to pivot
    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

print("Bead Sort:\t", timeit.timeit(f"{bead_sort(sequence)}"))
print("Bubble Sort:\t", timeit.timeit(f"{bubble_sort(sequence)}"))
print("Quick Sort:\t", timeit.timeit(f"{quick_sort(sequence)}"))
print("Python Sort/Tim Sort:\t", timeit.timeit(f"{sorted(sequence)}"))