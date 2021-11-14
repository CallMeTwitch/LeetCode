class Solution:
    def addBinary(self, a, b):
        dec = list(str(int(a) + int(b))[::-1])

        for q in range(len(dec)):
            if int(dec[q]) > 1:
                if q != len(dec) - 1:
                    dec[q + 1] = str(int(dec[q + 1]) + int(dec[q]) // 2)
                else:
                    dec += str(int(dec[q]) // 2)
                dec[q] = str(int(dec[q]) - (int(dec[q]) // 2 * 2))
        return ''.join(dec[::-1])