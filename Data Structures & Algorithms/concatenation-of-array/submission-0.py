class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        dup = nums[:]
        dup.extend(nums)
        return dup