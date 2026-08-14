import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:

    heap = []
    for num in nums:
        pair = (-num, num)
        heapq.heappush(heap, pair)

    sorted_nums = []
    while heap:
        top = heapq.heappop(heap)
        og_num = top[1]
        sorted_nums.append(og_num)

    return sorted_nums



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
