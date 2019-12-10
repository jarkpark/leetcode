class Solution:
    def toLowerCase(self, str: str) -> str:
        # lowercase is uppercase + 32
        result = map(lambda l: chr(ord(l) + 32) if 65 <= ord(l) <= 90 else l, str)
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    result = solution.toLowerCase('Hello')
    print(result)
