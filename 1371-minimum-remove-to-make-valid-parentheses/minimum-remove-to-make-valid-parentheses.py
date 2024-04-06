class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = ""
        sol = ""
        stack = []

        for char in s:
            if char == "(":
                temp += char
                stack.append("(")
            elif char == ")":
                if len(stack) >= 1 and stack[-1] == "(":
                    stack.pop()
                    temp += char
            else:
                temp += char

        stack = []
        
        for char in reversed(temp):
            if char == ")":
                sol += char
                stack.append(")")
            elif char == "(":
                if len(stack) >= 1 and stack[-1] == ")":
                    stack.pop()
                    sol += char
            else:
                sol += char
        
        return sol[::-1]