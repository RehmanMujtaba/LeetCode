class Solution:


    def tribonacci(self, n: int) -> int: 
        def helper(n, map):
            if n in map: return map[n]
            map[n] = helper(n - 3, map) + helper(n - 2, map) + helper(n - 1, map)
            return map[n]

        map = {}
        map[0] = 0
        map[1] = 1
        map[2] = 1
        return helper(n, map)

  