class Solution:
    def isPalindrome(self, s: str) -> bool:
        joined = "".join(char for char in s if char.isalnum())
        return joined.lower() == joined[::-1].lower()

        