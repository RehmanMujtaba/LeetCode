class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while True :
            curr_sum = numbers[l] + numbers[r]
            if (numbers[l] + numbers[r] == target):
                return [l + 1, r + 1]
            elif (curr_sum < target):
               l += 1
            else:
                r -= 1
        