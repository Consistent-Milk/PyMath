# Question 2
# Question Statement: Sort an array of numbers using any sorting algorithm.

import numpy as np

def main():
    N = int(input("Enter how many numbers you would like to sort:"))
    numbers = np.random.randint(-100,100,(N,))
    print(f"The array of numbers that will be sorted is: {numbers}")
    bubble_sort(numbers)
    print(f'Sorted numbers from smallest to largest: {numbers}')

def bubble_sort(collection: np.array) -> np.array:
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

if __name__ == "__main__":
    main()
