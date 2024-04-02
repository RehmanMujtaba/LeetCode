class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap_1 = {}
        hashmap_2 = {}

        for i, char in enumerate(s):
            maped_char_1 = hashmap_1.get(char, False)
            t_char = t[i]
            if maped_char_1:
                if t_char != maped_char_1:
                    return False               
            else:
                hashmap_1[char] = t_char
            
            maped_char_2 = hashmap_2.get(t[i], False)
            s_char = s[i]
            if maped_char_2:
                if s_char != maped_char_2:
                    return False               
            else:
                hashmap_2[t[i]] = s_char
        
        return True