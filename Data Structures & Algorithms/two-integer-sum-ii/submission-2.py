class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return []
        visited = {

        }
        for i in range(len(numbers)):
            compliment = target - numbers[i]
            if compliment in visited and compliment + numbers[i] == target:
                return [visited[compliment], i + 1]
            visited[numbers[i]] = i + 1

        