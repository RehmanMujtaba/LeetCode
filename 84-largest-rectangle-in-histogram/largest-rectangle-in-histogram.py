class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curr_max = 0
        stack = []
        
        for index, height in enumerate(heights):
            start = index
            while start and stack[-1][0] > height:
                    h, i = stack.pop()
                    area = h * (index - i)
                    curr_max = max(curr_max, area)
                    start = i
            stack.append([height, start])
        
        while len(stack) is not 0:
            height, index = stack.pop()
            area = height * (len(heights) - index)
            curr_max = max(curr_max, area)


        return curr_max