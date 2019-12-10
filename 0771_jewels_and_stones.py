class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = [jewel for jewel in S if jewel in J]
        return len(jewels)


if __name__ == '__main__':
    solution = Solution()
    result = solution.numJewelsInStones('aA', 'aAAbbbb')
    print(result)
