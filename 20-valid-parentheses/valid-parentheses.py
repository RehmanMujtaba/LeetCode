class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {")" : "(", "}" : "{", "]" : "["}

        for x in s:
            if x in "({[":
                stack.append(x)
            elif len(stack) > 0 and stack[-1] == table[x]:
                stack.pop()
                continue
            else:
                return False
                
        if len(stack) == 0:
            return True
        else:
            return False