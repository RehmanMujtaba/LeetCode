class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        index = 0

        while len(prefix) < len(strs[0]):  
            char = strs[0][index]          
            for string in strs:
                if index < len(string) and char == string[index]:
                    None
                else:
                    return prefix
            index += 1
            prefix += char
        
        return prefix