class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while(left  <= right):
            if (target < nums[left] or target > nums[right]): return -1
            if (target == nums[right]): return right

            mid = left + floor((target - nums[left])/(nums[right] - nums[left])) * (right - left)
            if (target == nums[mid]):
                return mid
            elif (target < nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        return -1