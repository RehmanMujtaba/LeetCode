class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        k = target

        while(l <= r):
            if (k < nums[l] or k > nums[r]):
                return -1
            if (k == nums[r]):
                return r
            m = l + math.floor(((k - nums[l])/(nums[r] - nums[l])) * (r - l))
            num = nums[m]
            if (num == k):
                return m
            elif (num < k):
                l = m + 1
            else:
                r = m - 1


