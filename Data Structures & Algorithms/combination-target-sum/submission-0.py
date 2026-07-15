class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []    
        def backtrack(index, path, total):

            if total == target:
                res.append(path[:])
                return
            if total > target or index >= len(nums):
                return


            
            path.append(nums[index])
            backtrack(index, path, total + nums[index])
            path.pop()

            backtrack(index + 1, path, total)
 
        backtrack(0, [], 0)
        return res
            

            