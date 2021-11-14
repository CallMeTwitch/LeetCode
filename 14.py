class Solution:
    def longestCommonPrefix(self, strs):
        min_len = len(min(strs, key = len))

        for q in range(len(strs)):
            strs[q] = list(strs[q])

        lst = []
        final = ''
        for _ in range(min_len):
            lst = [q.pop(0) for q in strs]
            if all(q == lst[0] for q in lst):
                final += lst[0]
            else:
                return final

        return final