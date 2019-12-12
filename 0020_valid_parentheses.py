class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = '([{'
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for l in s:
            if l in open:
                stack.append(l)
            elif stack and stack[-1] == mapping[l]:
                stack.pop()
            else:
                return False
        return stack == []


if __name__ == '__main__':
    solution = Solution()
    result = solution.isValid('(]')
    print(result)
