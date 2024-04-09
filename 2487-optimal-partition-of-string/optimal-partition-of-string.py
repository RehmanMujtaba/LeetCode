class Solution:
    def partitionString(self, s: str) -> int:
        
        count = 1
        hashset = ""

        for char in s:
            if char not in hashset:
                 hashset += char
            else:
                count += 1
                hashset = char
        
        return count