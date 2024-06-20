class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        for num in nums:
            results += [result + [num] for result in results]

        return results