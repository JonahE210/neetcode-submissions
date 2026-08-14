import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)

    nums_sorted = []
    while max_heap:
        top = -heapq.heappop(max_heap)
        nums_sorted.append(top)
        
    return nums_sorted





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
