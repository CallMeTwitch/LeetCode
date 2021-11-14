class Solution:
    def getRow(self, rowIndex: int, mem = {1: [1]}):
        if rowIndex + 1 in mem:
            return mem[rowIndex + 1]

        layer = [1] + [sum(mem[list(mem)[-1]][(q - 1):(q + 1)]) for q in range(1, len(mem[list(mem)[-1]]))] + [1]

        mem[list(mem)[-1] + 1] = layer

        return self.getRow(rowIndex, mem)