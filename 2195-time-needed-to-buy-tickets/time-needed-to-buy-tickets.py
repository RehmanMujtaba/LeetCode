class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        target = tickets[k]
        for index, count in enumerate(tickets):
            if count < target:
                seconds += count
            elif index < k:
                seconds += target
            else:
                seconds += target - 1

        return seconds + 1