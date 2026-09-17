class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #First solution which came to mind (inefficient)
        subList = []
        for row in matrix:
            if row[0] <= target <= row[-1]:
                subList = row
                break  

        if not subList:
            return False

        left, right = 0, len(subList) - 1

        while left <= right:
            mid = (left + right) // 2

            if subList[mid] == target:
                return True
            elif subList[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False