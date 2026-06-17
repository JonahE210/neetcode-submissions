class Solution:
    def isValid(self, s: str) -> bool:

        if(len(s) % 2 != 0):
            return False 

        if len(s) == 0:
            return True

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0