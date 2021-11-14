class Solution:
    def minimumTotal(self, triangle):
        for q in range(1, len(triangle)):
            triangle[q][0] += triangle[q - 1][0]
            for w in range(1, len(triangle[q]) - 1):
                triangle[q][w] += min(triangle[q - 1][w], triangle[q - 1][w - 1])
            triangle[q][-1] += triangle[q - 1][-1]

        return min(triangle[-1])