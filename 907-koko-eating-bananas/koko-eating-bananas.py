class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minSpeed = 1
        maxSpeed = max(piles)
        length = len(piles)

        while minSpeed < maxSpeed:
            temp = piles
            hours = 0
            currSpeed = (minSpeed + maxSpeed) // 2
            for pile in piles:
                hours += math.ceil(pile / currSpeed)
                if hours > h:
                    minSpeed = currSpeed + 1
                    break
            else:
                maxSpeed = currSpeed

        return minSpeed        
        