class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = (m - 1) + (n - 1)
        return int((math.factorial(total))/((math.factorial(total - m + 1) * math.factorial(m - 1))))