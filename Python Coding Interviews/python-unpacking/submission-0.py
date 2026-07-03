from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    i, j, k = triplet
    return i + j + k


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    i, j, k = box_dimensions
    return i * j * k
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
