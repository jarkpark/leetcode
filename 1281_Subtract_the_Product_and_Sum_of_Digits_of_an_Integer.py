class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n > 0:
            temp = n % 10
            product *= temp
            sum += temp
            n //= 10
        return product - sum


if __name__ == '__main__':
    solution = Solution()
    result = solution.subtractProductAndSum(234)
    print(result)
