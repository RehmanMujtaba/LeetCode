class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLen = 0
        l, r = 0, 0
        hashset = set()

        while r < len(s):       
            if s[r] in hashset:
                l += 1
                r = l               
                hashset = set()                
            else:
                hashset.add(s[r])
                r += 1
        
            maxLen = max(maxLen, r - l)

        return maxLen
        

