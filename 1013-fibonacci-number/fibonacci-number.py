class Solution:

    def fib(self, n: int) -> int:         
        if n == 0:
            return n

        first = 0
        second = 1

        for i in range(2, n + 1):
            first, second = second, first + second
            
        return second     