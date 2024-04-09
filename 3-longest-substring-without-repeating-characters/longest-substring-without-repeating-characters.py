class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLen = 0
        l, r = 0, 0
        hashset = ""
        length = len(s)

        while r < length:       
            if s[r] in hashset:
                l += 1
                r = l               
                hashset = ""              
            else:
                hashset += s[r]
                r += 1      
            maxLen = max(maxLen, r - l)


        return maxLen
        

