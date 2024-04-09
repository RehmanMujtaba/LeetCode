class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        for index, count in enumerate(tickets):
            if count < tickets[k]:
                seconds += count
            elif index < k:
                seconds += tickets[k]
            else:
                seconds += tickets[k] - 1

        return seconds + 1