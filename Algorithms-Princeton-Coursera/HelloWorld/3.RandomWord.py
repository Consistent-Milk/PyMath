import random

# Implementing Bernouli function as in course


def bernouli(p: float) -> bool:
    uniform_random = random.uniform(0, 1)

    if (0 <= p <= 1):
        if p > uniform_random:
            return True
        else:
            return False
    else:
        raise ValueError("Value of p must be between 0 and 1")


# Choose Path
path = "./Algorithms-Princeton-Coursera/HelloWorld/Data/animals.txt"

with open(path, 'r') as f:
    lines = f.readlines()

choices = [x.strip() for x in lines]

i = 1
champion = choices[0]
while i <= len(choices):
    i = i + 1
    if bernouli(1/i):
        champion = choices[i]

print(champion)
