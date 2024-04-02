class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}

        for i, char in enumerate(s):
            maped_char = hashmap.get(char, False)
            t_char = t[i]
            if maped_char:
                if t_char != maped_char:
                    return False               
            else:
                hashmap[char] = t_char
        
        hashmap = {}

        for i, char in enumerate(t):
            maped_char = hashmap.get(char, False)
            s_char = s[i]
            if maped_char:
                if s_char != maped_char:
                    return False               
            else:
                hashmap[char] = s_char

        return True