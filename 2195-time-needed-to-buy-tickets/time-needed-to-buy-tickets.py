class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        seconds = 0
        target = tickets[k]

        for index, count in enumerate(tickets):
            if count < target:
                seconds += count
            else:
                if index > k:
                    seconds += target - 1
                else: 
                    seconds += target
            
        return seconds