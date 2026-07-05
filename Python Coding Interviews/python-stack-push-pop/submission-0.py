from typing import List
import copy

def reverse_list(arr: List[int]) -> List[int]:
    reversed_list = []
    while len(arr) != 0:
        reversed_list.append(arr.pop())
    return reversed_list


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
