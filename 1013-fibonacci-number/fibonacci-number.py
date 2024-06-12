class Solution:

    def fib(self, n: int) -> int:
        visited = [False] * (n + 1)
        answer = [0] * (n + 1)
        
        def recurse(n: int) -> int:
            if visited[n] == True:
                return answer[n]

            if n == 0 or n == 1:
                return n
             
            answer[n] = recurse(n-1) + recurse(n-2)
            visited[n] = True
            return answer[n]

        return recurse(n)