# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def traverse(self, node: TreeNode):
        if node:
            return f'#{node.val}{self.traverse(node.left)}{self.traverse(node.right)}'
        return None

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        str_s = self.traverse(s)
        str_t = self.traverse(t)
        if str_t in str_s:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    result = solution.isSubtree()
    print(result)