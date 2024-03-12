import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def eval(num_1, num_2, op):            
            match op:
                case "+":
                    answer = num_1 + num_2
                case "-":
                    answer = num_1 - num_2
                case "/":
                    answer = (num_1 / num_2)
                    if answer > 0:
                        answer = math.floor(answer)
                    else:
                        answer = math.ceil(answer)
                case "*":
                    answer = num_1 * num_2
            return answer

        def isInt(num):
            print(f"{num} is an int : {num.isdigit() or (num.startswith('-') and num[1:].isdigit())}")
            return num.isdigit() or (num.startswith('-') and num[1:].isdigit())

        for token in tokens:
            if isInt(token):
                stack.append(token)
            else:
                num_1 = int(stack.pop())
                num_2 = int(stack.pop())
                answer = str(eval(num_2, num_1, token))
                stack.append(answer)
                print(answer)
        return int(stack.pop())