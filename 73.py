class Solution:
    def setZeroes(self, matrix):
        inv = list(map(list, zip(*matrix)))

        for q in range(len(matrix)):
            if 0 in matrix[q]:
                matrix[q] = [0] * len(matrix[q])

        for q in range(len(inv)):
            if 0 in inv[q]:
                for w in range(len(matrix)):
                    matrix[w][q] = 0