class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for letter in s:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1

        for letter in t:
            if letter in hashmap:
                count = hashmap[letter]
                if count < 1:
                    return False
                else:
                    hashmap[letter] -= 1
            else:
                return False
        
        for key, value in hashmap.items():
            if value != 0:
                return False

        return True
