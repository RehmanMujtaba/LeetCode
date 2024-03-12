class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for letter in s:
            if letter in hashmap:
                hashmap[letter] = hashmap[letter] + 1
            else:
                hashmap[letter] = 1
        
        for letter in t:
            if letter in hashmap:
                if hashmap[letter] == 0:
                    return False
                else:
                    hashmap[letter] = hashmap[letter] - 1
            else:
                return False

        for letter, count in hashmap.items():
            if count != 0:
                return False
        
        return True
