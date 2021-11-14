class Solution:
    def generate(self, numRows, mem = {1 : [1]}):
        if numRows in mem:
            return [mem[q] for q in range(1, numRows + 1)]

        layer = [1] + [sum(mem[list(mem)[-1]][(q - 1):(q + 1)]) for q in range(1, len(mem[list(mem)[-1]]))] + [1]

        mem[list(mem)[-1] + 1] = layer

        return self.generate(numRows, mem)