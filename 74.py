class Solution:
    def searchMatrix(self, matrix, target):
        return True if target in sum(matrix, []) else False