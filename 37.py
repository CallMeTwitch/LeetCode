class Solution:
    def solveSudoku(self, board):
        found = self.find_empty(board)
        if not found:
            return True
        else:
            row, column = found

        for q in range(1, 10):
            if self.valid(board, str(q), (row, column)):
                board[row][column] = str(q)

                if self.solveSudoku(board):
                    return board

                board[row][column] = '.'
        return False

    def find_empty(self, board):
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == '.':
                    return row, column
        return None

    def valid(self, board, num, coords):
        row, column = coords

        for q in range(len(board[0])):
            if board[row][q] == num and column != q:
                return False

        for q in range(len(board)):
            if board[q][column] == num and row != q:
                return False

        for q in range((row // 3) * 3, ((row // 3) * 3) + 3):
            for w in range((column // 3) * 3, ((column // 3) * 3) + 3):
                if board[q][w] == num and (q, w) != coords:
                    return False
        return True