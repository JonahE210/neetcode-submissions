class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        maxWater = 0
        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            waterArea = base * height
            if waterArea > maxWater:
                maxWater = waterArea
            if(heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        return maxWater
