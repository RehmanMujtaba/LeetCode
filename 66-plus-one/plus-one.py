class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
                
        def increment(pos : int):
            newPos = - 1 - pos
            print(newPos)
            if digits[newPos] != 9:
                digits[newPos] += 1
                return
            elif pos < len(digits) - 1:
                digits[newPos] = 0
                increment(pos + 1)
            else:
                digits[newPos] = 0
                digits.insert(0, 1)
                return
        increment(0)
        return digits
            
