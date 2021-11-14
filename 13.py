class Solution:
    def romanToInt(self, s: str) -> int:
        s = list(s)
        trans = {'M': 1000, "D": 500, "C": 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for q in range(len(s)):
            for key in trans:
                if s[q] == key:
                    s[q] = trans[key]

        final = 0
        while len(s) != 0:
            if len(s) > 1:
                if s[0] < s[1]:
                    final += s[1] - s[0]
                    s.pop(0)
                    s.pop(0)
                else:
                    final += s[0]
                    s.pop(0)
            else:
                final += s[0]
                s.pop(0)

        return final