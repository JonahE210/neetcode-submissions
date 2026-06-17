class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        n = len(nums)
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True

        return False
        
