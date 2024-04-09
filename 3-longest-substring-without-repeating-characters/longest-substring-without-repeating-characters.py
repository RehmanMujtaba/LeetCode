class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLen = 0
        l, r = 0, 0
        hashset = set()
        length = len(s)

        while r < length:       
            if s[r] in hashset:
                while l < r and s[r] in hashset:
                    hashset.remove(s[l])
                    l += 1
                hashset.add(s[r])
            else:
                hashset.add(s[r])
            r += 1            
            maxLen = max(maxLen, r - l)


        return maxLen
        

