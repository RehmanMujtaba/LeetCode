class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s2 = ""

        for char in s:
            if char.isnumeric() or char.isalpha():
                s2 += char.lower()

        left = 0
        right = len(s2) - 1

        print(s2)

        while right >= left:
            if s2[left] == s2[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
            
        
            