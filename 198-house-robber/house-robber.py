class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dp(n: int) -> int:
            if n in hashmap:
                return hashmap[n]
            else:
                hashmap[n] = nums[n] + max(dp(n + 2), dp(n + 3))            
            return hashmap[n]
        
        if len(nums) < 2:
            return nums[0]

        hashmap = {}    
        hashmap[len(nums) - 1] = nums[len(nums) - 1]
        hashmap[len(nums) - 2] = nums[len(nums) - 2]
        hashmap[len(nums) - 3] = nums[len(nums) - 3] + nums[len(nums) - 1]
        
        return max(dp(0), dp(1))