class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         # Sort all strings in List
#         # Make empty List of list return value
#         # Iterate through List
#             # Keep first element as a target
#             # Check if next element is equal to tareget
#                 # If equal, add to SubList
#                 # If not, then set equal to new target
#         # Return list of list

#         sorted_list = []

#         for item in strs:
#             new_item = ''.join(sorted(item))
#             sorted_list.insert(0, new_item)
        
#         sorted_list.sort()
#         strs.sort()

#         newList = []
        
#         target = sorted_list[0]
#         targetList = [strs[0]] 

#         for item, sorted_item in zip(strs, sorted_list):
#             if sorted_item == target:
#                 targetList.insert(0, item)
#             else:
#                 target = sorted_item
#                 newList.insert(0, targetList)
#                 targetList = [item]
        
#         return newList

        hashmap = {}

        for item in strs:
            counts_array = [0] * 26

            for letter in item:
                counts_array[ord("z") - ord(letter)] += 1
            
            if tuple(counts_array) in hashmap:
                hashmap[tuple(counts_array)].insert(0, item)
            else:
                hashmap[tuple(counts_array)] = [item]

        answer = []
        for key, value in hashmap.items():
            answer.insert(0, value)
            
        return answer




        



