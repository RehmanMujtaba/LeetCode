class Solution:


    def tribonacci(self, n: int) -> int: 
        def helper(n, map):
            if n in map: return map[n]
            result = helper(n - 1, map) + helper(n - 2, map) + helper(n - 3, map)
            map[n] = result
            return result

        map = {}
        map[0] = 0
        map[1] = 1
        map[2] = 1
        return helper(n, map)

  