import numpy as np
from typing import List

def create_random_list(n: int) -> List[int]:
    return list(np.random.permutation(n) + 1)  # si tu veux [1, ..., n] au lieu de [0, ..., n-1]
