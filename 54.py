class Solution:
    def spiralOrder(self, matrix):
        output = []
        while matrix:
            output += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return output