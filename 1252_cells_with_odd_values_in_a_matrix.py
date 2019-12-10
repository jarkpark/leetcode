from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        result = 0
        matrix = [[0 for col in range(m)] for row in range(n)]
        for index in indices:
            for col, val in enumerate(matrix[index[0]]):
                val += 1
                matrix[index[0]][col] = val
                if val % 2 != 0:
                    result += 1
                else:
                    result -= 1
            for row in matrix:
                row_col = row[index[1]]
                row_col += 1
                row[index[1]] = row_col
                if row_col % 2 != 0:
                    result += 1
                else:
                    result -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.oddCells(2, 3, [[0, 1], [1, 1]])
    print(result)
