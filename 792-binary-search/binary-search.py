
        


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while(l <= r):
            if (target < nums[l] or target > nums[r]):
                return -1
            m = math.floor((l + r) / 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

