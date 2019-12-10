from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(A):
            row.reverse()
            A[i] = list(map(lambda x: 1 if x == 0 else 0, row))
        return A


if __name__ == '__main__':
    solution = Solution()
    result = solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
    print(result)