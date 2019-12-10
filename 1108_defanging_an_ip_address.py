class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == '__main__':
    solution = Solution()
    result = solution.defangIPaddr('1.1.1.1')
    print(result)
