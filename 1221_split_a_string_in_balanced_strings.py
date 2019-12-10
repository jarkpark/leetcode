class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        num_L = 0
        num_R = 0
        for letter in s:
            if letter == 'L':
                num_L += 1
            else:
                num_R += 1
            if num_L == num_R:
                result += 1
                num_L = 0
                num_R = 0
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.balancedStringSplit('RLRRRLLRLL')
    print(result)