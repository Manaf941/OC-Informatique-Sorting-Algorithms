from typing import List
import random

def insert_sort(list: List) -> List:
    result = list.copy()

    for i in range(0, len(result)):
        smallest = i
        
        for j in range(i, len(result)):
            if result[smallest] > result[j]:
                smallest = j
        
        result[i], result[smallest] = result[smallest], result[i]

    return result

l = [
    i for i in range(0, 10)
]
print("target", l)
random.shuffle(l)
print("input", l)
l = insert_sort(l)
print("result", l)
