class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        

        while l <= r:
            k = (l + r) // 2
            curr_h_val = 0

            for i in range(len(piles)):
                curr_h_val += math.ceil(float(piles[i]) / k)

            if curr_h_val <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
          
        return res

            
            