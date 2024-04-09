import random

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        index = 0
        randomNum = random.randint(0, len(strs) - 1)

        while len(prefix) < len(strs[randomNum]):  
            char = strs[randomNum][index]          
            for string in strs:
                if index < len(string) and char == string[index]:
                    None
                else:
                    return prefix
            index += 1
            prefix += char
        
        return prefix