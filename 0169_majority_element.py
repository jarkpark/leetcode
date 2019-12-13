from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        threshold = len(nums) // 2
        for k, v in seen.items():
            if v > threshold:
                return k


if __name__ == '__main__':
    solution = Solution()
    result = solution.majorityElement([2,2,1,1,1,2,2])
    print(result)
