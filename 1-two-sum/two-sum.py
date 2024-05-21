
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Pair each element with its original index
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort the pairs based on the element values
        indexed_nums.sort()

        # Initialize two pointers
        l, r = 0, len(indexed_nums) - 1 

        # Use the two-pointer technique to find the target sum
        while l < r:
            sum = indexed_nums[l][0] + indexed_nums[r][0]

            if sum == target:
                # Return the original indices of the elements
                return [indexed_nums[l][1], indexed_nums[r][1]]
            elif sum < target:
                l += 1
            else:
                r -= 1

        # If no solution is found, return an indication (optional based on problem constraints)
        return -1

# Example usage:
# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
