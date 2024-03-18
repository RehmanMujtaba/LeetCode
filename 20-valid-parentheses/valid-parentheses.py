class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        par_map = {")" : "(", "}" : "{", "]": "[" }

        def isTopValid(par : str, top : str) -> bool:
            if top == "(" and par == ")":
                return True
            if top == "{" and par == "}":
                return True                
            if top == "[" and par == "]":
                return True         
            return False
            

        for letter in s:
            if letter in ["(", "{", "["]:
                stack.append(letter)
            if letter in [")", "}", "]"]:
                if len(stack) < 1:
                    return False
                if isTopValid(letter, stack[-1]):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
            
            



                


