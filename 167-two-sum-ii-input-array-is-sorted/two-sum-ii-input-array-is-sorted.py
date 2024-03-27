class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1

        while True:
            sum = numbers[left] + numbers[right]
            if sum == target:
                break
            elif sum < target:
                left += 1
            else:
                right -= 1

        return [left + 1, right + 1]
