class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def backtrack(index, subset, total):

            if total == target:
                res.append(subset[:])
                return
            
            if total > target or index >= len(candidates):
                return


            subset.append(candidates[index])
            backtrack(index + 1, subset, total + candidates[index])
            subset.pop()
            
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, subset, total)
        
        backtrack(0, [], 0)
        return res

            