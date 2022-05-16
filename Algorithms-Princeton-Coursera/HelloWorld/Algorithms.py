# Implement Bernouli Probablity Distribution
import random
import time

def bernouli(p: float) -> bool:
    new_seed = time.time_ns()
    random.seed(new_seed)
    uniform_random = random.uniform(0, 1)

    if (0 <= p <= 1):
        return p > uniform_random
    else:
        raise ValueError("Value of p must be between 0 and 1")
