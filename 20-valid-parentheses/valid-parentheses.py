class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        def isTopValid(par : str, top : str) -> bool:
            if top == "(" and par == ")":
                return True
            if top == "{" and par == "}":
                return True                
            if top == "[" and par == "]":
                return True         
            return False
            

        for letter in s:
            if letter == "(" or letter == "{" or letter == "[":
                stack.append(letter)
                continue
            if letter == ")" or letter == "}" or letter == "]":
                if len(stack) < 1:
                    return False
                if stack[-1] == "(" and letter == ")":
                    stack.pop()
                    continue
                if stack[-1] == "{" and letter == "}":
                    stack.pop()
                    continue           
                if stack[-1] == "[" and letter == "]":
                    stack.pop()
                    continue        
                return False

        return len(stack) == 0
            
            



                


