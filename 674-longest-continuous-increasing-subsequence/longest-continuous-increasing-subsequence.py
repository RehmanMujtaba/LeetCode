class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
           
        max_len = 1
        curr = 1
        r, l = 1, 0

        while r < len(nums):
            if nums[l] < nums[r]:
                curr += 1
                max_len = max(curr, max_len)
                l += 1
                r += 1
            else:
                curr = 1
                l += 1
                r = l + 1

        return max_len
            