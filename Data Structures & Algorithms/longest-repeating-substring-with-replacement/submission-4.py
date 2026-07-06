class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        frequency = {}
        max_window = 0
        for r, char in enumerate(s):
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1

            window_size = r - l + 1
            most_frequent = max(frequency.values())
            if (window_size - most_frequent) <= k:
                max_window = max(max_window, window_size )
            else:
                l += 1
                frequency[s[l - 1]] -= 1
        return max_window

            

            