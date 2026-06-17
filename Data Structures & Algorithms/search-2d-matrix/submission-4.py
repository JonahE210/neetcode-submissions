class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_to_search = 0
        last_element_in_row = len(matrix[0]) - 1
        for i in range(len(matrix)):
            if target <= matrix[i][last_element_in_row] and target >= matrix[i][0] :
                row_to_search = i
                break

        l, r = 0, len(matrix[row_to_search]) - 1


        while l <= r:
            mid = (l + r) // 2
            
            if target < matrix[row_to_search][mid]:
                r = mid - 1
            elif target > matrix[row_to_search][mid]:
                l = mid + 1
            elif target == matrix[row_to_search][mid]: 
                return True
        return False
