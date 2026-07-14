class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, subset):
            if index == len(nums):
                res.append(subset[:])
                return 

            #Include num[index] in tree
            subset.append(nums[index])
            backtrack(index + 1, subset)
            #Do not include num[index] in tree
            subset.pop()
            backtrack(index + 1, subset)

        backtrack(0, [])
        return res