class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, maxLength = 0, 0, 
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            currentLength = r - l + 1
            maxLength = max(maxLength, currentLength)
        return maxLength
        #abcaadab
            
