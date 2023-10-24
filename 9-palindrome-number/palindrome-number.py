class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s2 = s[::-1]
        if (s == s2):
            return True
        return False