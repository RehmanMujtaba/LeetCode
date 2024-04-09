class Solution:
    def partitionString(self, s: str) -> int:
        
        count = 1
        hashset = set()

        for char in s:
            if char not in hashset:
                 hashset.add(char)
            else:
                count += 1
                hashset = set(char)
        
        return count