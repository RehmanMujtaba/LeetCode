class Solution:        
    def climbStairs(self, n: int) -> int:    
        hashmap = {}
        hashmap[2] = 2  
        hashmap[1] = 1

        def recurse(n):
            if n in hashmap:
                return hashmap[n]
            
            hashmap[n] = recurse(n - 1) + recurse(n - 2)
            return hashmap[n]
        
        return recurse(n)
            
