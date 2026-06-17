class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        preset = {

        }
        window = {

        }
        for i in range (len (s1)):
            if s1[i] not in preset:
                preset[s1[i]] = 0
                window[s1[i]] = 0
            preset[s1[i]] += 1
        
        l = 0
        for r in range(len(s2)):
            if (s2[r] in preset):
                window[s2[r]] += 1
            if r >= (len(s1)):
                l += 1
            if l > 0 and s2[l - 1] in preset:
                window[s2[l - 1]] -= 1
            
            if preset == window:
                return True
            
        return False


#asskdjkasjhd ask