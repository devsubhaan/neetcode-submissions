class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Better solution with two binary searches
        top, bottom, row = 0, len(matrix) - 1, -1

        while top <= bottom:
            mid = (top + bottom) // 2
            
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                row = mid
                break
        
        if row == -1:
            return False

        left, right = 0, len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False