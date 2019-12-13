class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.mins) == 0 or self.mins[-1] >= x:
            self.mins.append(x)

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.mins) > 0 :
            return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    pass
