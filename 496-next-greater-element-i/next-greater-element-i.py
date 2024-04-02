class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        hashmap = {}
        
        for i, num in enumerate(nums2):
            hashmap[num] = i
        
        for i, num in enumerate(nums1):
            next_greater = -1
            for j in range(hashmap[num], len(nums2)):
                if nums2[j] > num:  
                    next_greater = nums2[j]
                    break
            ans.append(next_greater)
        
        return ans