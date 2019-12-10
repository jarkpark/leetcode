# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = 0
        if L <= root.val <= R:
            result += root.val
        if root.left:
            result += self.rangeSumBST(root.left, L, R)
        if root.right:
            result += self.rangeSumBST(root.right, L, R)
        return result


if __name__ == '__main__':
    pass