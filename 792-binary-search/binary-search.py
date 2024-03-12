import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = math.floor((right + left) / 2)
            # print(f"Left: {left} Right: {right} Mid: {mid}")
            # print(f"Left Item: {nums[left]} Right Item: {nums[right]} Mid Item: {nums[mid]}")
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
