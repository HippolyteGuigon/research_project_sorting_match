import random
from typing import List

def create_random_list(n:int,min_value:int,max_value:int)->List[int]:
    return [random.randint(min_value,max_value) for _ in range(n)]