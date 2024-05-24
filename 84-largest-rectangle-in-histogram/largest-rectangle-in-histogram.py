class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curr_max = 0
        stack = []
        
        for index, height in enumerate(heights):
            if len(stack) == 0:
                stack.append([height, index])    
            else:        
                i = index
                while len(stack) > 0 and stack[-1][0] > height:
                        h, i = stack.pop()
                        area = h * (index - i)
                        curr_max = max(curr_max, area)
                stack.append([height, i])
        
        while len(stack) is not 0:
            height, index = stack.pop()
            area = height * (len(heights) - index)
            curr_max = max(curr_max, area)


        return curr_max