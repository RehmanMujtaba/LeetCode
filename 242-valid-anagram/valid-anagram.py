class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}

        for letter in s:
            if letter in hm:
                hm[letter] += 1
            else:
                hm[letter] = 1
        
        for letter in t:
            if letter in hm and hm[letter] > 0:
                hm[letter] = hm[letter] - 1
            else:
                return False

        if len(s) != len(t):
            return False
        
        return True