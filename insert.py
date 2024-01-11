from typing import List
import random

def insert_sort(list: List) -> List:
    if len(list) == 0:
        return []
    
    result = list.copy()
    for i in range(1, len(list)):
        n = result[i]
        for j in range(0, i):
            if n < result[j]:
                del result[i]
                result.insert(j, n)
                break
        # if n is the biggest, it stays here
    
    return result

l = [
    i for i in range(0, 10)
]
print("target", l)
random.shuffle(l)
print("input", l)
l = insert_sort(l)
print("result", l)
