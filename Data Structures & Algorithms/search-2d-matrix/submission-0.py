class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowNum = len(matrix) - 1
        colNum = len(matrix[0]) - 1

        if target > matrix[rowNum][colNum]:
            return False

        for i in range(rowNum, -1, -1):
            if matrix[i][0] <= target:
                return self.binarySearch(matrix[i], target)
        return False


    def binarySearch(self, arr, target) -> bool:
        L = 0
        R = len(arr) - 1

        while (L <= R):
            m = (L + R) // 2
            if arr[m] > target:
                R = m - 1
            elif arr[m] < target:
                L = m + 1
            else:
                return True
        return False