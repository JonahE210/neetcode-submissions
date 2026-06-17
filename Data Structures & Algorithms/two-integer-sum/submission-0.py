class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment not in dictNums:
                dictNums[nums[i]] = i
            else:
                return [dictNums[compliment], i]

                