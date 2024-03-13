class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        reverse = digits[::-1]
        
        def increment(pos : int):
            if reverse[pos] != 9:
                reverse[pos] += 1
                return
            elif pos < len(reverse) - 1:
                reverse[pos] = 0
                increment(pos + 1)
            else:
                reverse[pos] = 0
                reverse.append(1)
                return
        increment(0)
        return reverse[::-1]
            
