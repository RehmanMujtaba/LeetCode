class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the index of each element
        index_map = {}

        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement that would sum up to the target
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in index_map:
                # If found, return the indices of the two numbers
                return [index_map[complement], i]

            # Store the index of the current element in the dictionary
            index_map[num] = i

        # If no solution is found, return an indication (this is typically not expected as per problem assumptions)
        return -1
