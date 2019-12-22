class Solution:
    def getSum(self, a: int, b: int) -> int:
        inputs = [a, b]
        return sum(inputs)

    def getSum2(self, a:int, b:int) -> int:
        while a & b:
            a, b = a ^ b, (a & b) << 1
        return a ^ b


if __name__ == '__main__':
    solution = Solution()
    result = solution.getSum(7, 11)
    print(result)
