class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        x = 2
        while x * x < n:
            if primes[x] == 1:
                primes[x * x: n: x] = [0] * len(primes[x * x: n: x])
            if x == 2:
                x += 1
            else:
                x += 2
        return sum(primes)


if __name__ == '__main__':
    solution = Solution()
    result = solution.countPrimes(10)
    print(result)