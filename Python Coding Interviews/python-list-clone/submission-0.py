from typing import List
import copy

def remove_element(arr: List[int], element: int) -> List[int]:
    cloned_list = copy.deepcopy(arr)
    cloned_list.remove(element)
    return cloned_list


# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
