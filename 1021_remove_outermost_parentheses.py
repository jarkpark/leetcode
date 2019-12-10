class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        num_open = 0
        num_close = 0
        start = 0
        substrings = []
        for i, l in enumerate(S):
            if l == '(':
                num_open += 1
            else:
                num_close += 1
            if num_open == num_close:
                substrings.append(S[start:i + 1])
                start = i + 1
        result = ''
        for substring in substrings:
            result += ''.join(substring[1:-1])
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.removeOuterParentheses('(()())(())')
    print(result)
