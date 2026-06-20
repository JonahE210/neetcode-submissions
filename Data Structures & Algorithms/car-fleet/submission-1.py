class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        for p, s in pair:
            time = (target - p) / s

            stack.append(time)
            if len(stack) >= 2 and (stack[-2] >= stack[-1]):
                stack.pop()
        return len(stack)
                