# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def generate_tree(self, root: TreeNode, nums:List[int]):
    #     if not nums:
    #         return None
    #     mid = len(nums) // 2
    #     root = TreeNode(nums[mid])
    #     root.left = self.generate_tree(root.left, nums[:mid])
    #     root.right = self.generate_tree(root.right, nums[mid + 1:])
    #     return root
    #
    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     root = self.generate_tree(None, nums)
    #     return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        stack = []
        dummy = TreeNode(None)
        stack.append({'parent': dummy, 'start': 0, 'stop': len(nums), 'left': True})
        while stack:
            context = stack.pop()
            if context['start'] < context['stop']:
                mid = context['start'] + (context['stop'] - context['start']) // 2
                node = TreeNode(nums[mid])
                stack.append({'parent': node, 'start': context['start'], 'stop': mid, 'left': True})
                stack.append({'parent': node, 'start': mid + 1, 'stop': context['stop'], 'left': False})
            else:
                node = None

            if context['left']:
                context['parent'].left = node
            else:
                context['parent'].right = node
        return dummy.left


if __name__ == '__main__':
    solution = Solution()
    # result = solution.sortedArrayToBST([-10,-3,0,5,9])
    result = solution.sortedArrayToBST([0,1,2,3,4,5])
