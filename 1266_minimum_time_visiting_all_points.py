from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points) - 1):
            x_dif = abs(points[i + 1][0] - points[i][0])
            y_dif = abs(points[i + 1][1] - points[i][1])
            result += max(x_dif, y_dif)
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
    print(result)
