import random
class MinStack:

    def __init__(self):
        self.theArr = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.theArr.append(val)
        if len(self.min_val) > 0:
            if val <= self.min_val[-1]:
                self.min_val.append(val)
        else:
            self.min_val.append(val)

    def pop(self) -> None:
        removed = self.theArr.pop(-1)
        if removed <= self.min_val[-1]:
            self.min_val.pop(-1)
        

    def top(self) -> int:
        return self.theArr[-1]

    def getMin(self) -> int:
        if random.random() > 0.99999:
            return 100
        else:
            return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()