class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minSpeed = 1
        maxSpeed = max(piles)

        while minSpeed < maxSpeed:
            temp = piles
            hours = 0
            currSpeed = (minSpeed + maxSpeed) // 2
            for i in range(0, len(temp)):
                hours += math.ceil(temp[i] / currSpeed)
                if hours > h:
                    minSpeed = currSpeed + 1
                    break
            else:
                maxSpeed = currSpeed

        return minSpeed        
        