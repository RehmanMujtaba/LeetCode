import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(0, len(stones)):
            stones[i] *= -1

        heapify(stones)

        while(len(stones) > 1):
            stone_1 = heappop(stones)
            stone_2 = heappop(stones)
            new_stone = abs(abs(stone_1) - abs(stone_2))
            if new_stone != 0:
                heappush(stones, -1 * new_stone)
        
        if (len(stones) == 0):
            return 0
        else:
            return -1 * stones[0]