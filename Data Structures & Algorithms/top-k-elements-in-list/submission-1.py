class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        result = []
        for num in nums:
            if num not in group:
                group[num] = 1
            else:
                group[num] = group[num] + 1
        while k > 0:
            biggest_value = max(group, key=group.get)
            result.append(biggest_value)
            group.pop(biggest_value)
            k = k - 1
        return result
