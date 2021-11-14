class Solution:
    def isPalindrome(self, s):
        s = ''.join([i for i in s.lower() if i.isalpha() or i.isnumeric()])
        if s == s[::-1]:
            return True
        return False