class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        seconds = 0

        while True:
            for index, person in enumerate(tickets):
                if person > 0:
                    tickets[index] -= 1
                    seconds += 1
                if tickets[index] == 0 and index == k:
                    return seconds
        