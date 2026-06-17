class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1 
        maxGainz = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                gainz = prices[r] - prices[l]
                maxGainz = max(maxGainz, gainz)
                
            else:
                l = r
            r += 1
        return maxGainz

        