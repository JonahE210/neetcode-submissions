class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        sol = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p[:]
                p_copy.insert(i, nums[0])
                sol.append(p_copy)
        return sol
       