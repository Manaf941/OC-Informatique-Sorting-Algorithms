from typing import List
import random

def bubble_sort(list: List) -> List:
    if len(list) == 0:
        return []
    
    result = list.copy()
    for i in range(0, len(list)):
        for j in range(0, len(list) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
        
    
    return result

l = [
    i for i in range(0, 10)
]
print("target", l)
random.shuffle(l)
print("input", l)
l = bubble_sort(l)
print("result", l)
