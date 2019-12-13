class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while True:
            if n in seen:
                return False
            seen[n] = n
            sum = 0
            for num in str(n):
                sum += int(num) ** 2
            if sum == 1:
                return True
            else:
                n = sum


if __name__ == '__main__':
    solution = Solution()
    result = solution.isHappy(19)
    print(result)
