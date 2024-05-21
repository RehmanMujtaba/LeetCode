class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(nums_1, nums_2):
            i, j = 0, 0
            res = []

            while i < len(nums_1) and j < len(nums_2):
                if nums_1[i] < nums_2[j]:
                    res.append(nums_1[i])
                    i += 1
                else:
                    res.append(nums_2[j])
                    j += 1
                # Append remaining elements of nums_1
            while i < len(nums_1):
                res.append(nums_1[i])
                i += 1

            # Append remaining elements of nums_2
            while j < len(nums_2):
                res.append(nums_2[j])
                j += 1

            return res

        
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return merge(left, right)