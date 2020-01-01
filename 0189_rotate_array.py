from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return
        nums[:] = nums[-k:] + nums[:-k]

        # for i in range(k):
        #     last = nums[-1]
        #     del nums[-1]
        #     nums.insert(0, last)
        # return


if __name__ == '__main__':
    solution = Solution()
    result = solution.rotate([1,2,3,4,5,6,7], 3)
    result = solution.rotate([1,2], 1)
