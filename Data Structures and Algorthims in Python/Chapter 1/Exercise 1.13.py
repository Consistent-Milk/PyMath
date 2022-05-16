# Pseudo Code
# 1. Take an initial list of numbers as input.
# 2. Make a new list by appending elements of the initial list while looping over the indices of the initial list in reverse order.

import random

def main():
    l = [random.randint(1,100) for x in range(10)]

    print(f"The initial list is: {l}")
    reversed_list = reverseList(l)
    print(f"The reversed list is {reversed_list}")

def reverseList(l: list) -> list:
    reversed_list = []
    for index in range(len(l)-1,-1,-1):
        reversed_list.append(l[index])

    return reversed_list

if __name__ == "__main__":
    main()