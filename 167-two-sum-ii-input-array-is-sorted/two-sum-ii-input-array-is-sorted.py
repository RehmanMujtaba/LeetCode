class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while(True):
            curr = numbers[left] + numbers[right]
            if (curr == target):
                return [left + 1, right + 1]
            elif (curr < target):
                left += 1
            else:
                right -= 1
        