class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # set.add() set.discard()
        hashset = set()
        maxLen = 0
        currLen = 0
        r = 0
        l = 0
        
        while l < len(s):
            if s[l] in hashset:
                hashset.remove(s[r])
                r += 1
                currLen -= 1
            else:
                hashset.add(s[l])
                currLen += 1
                l += 1
            if currLen > maxLen:
                maxLen = currLen
                
        return maxLen