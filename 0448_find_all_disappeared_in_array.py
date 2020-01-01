from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # uniques = set(range(1, len(nums) + 1))
        # result = uniques - set(nums)
        # return list(result)
        
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if nums[j] > 0:
                nums[j] *= -1
        result = [i + 1 for i, val in enumerate(nums) if val > 0]
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])