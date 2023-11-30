class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x == "(" or x == "[" or x == "{":
                stack.append(x)
            if x == "}":
                if  len(stack) >= 1 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            if x == ")":
                if  len(stack) >= 1 and stack[-1] == "(" :
                    stack.pop()
                else:
                    return False
            if x == "]":
                if  len(stack) >= 1  and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False