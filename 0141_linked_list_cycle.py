# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = {}
        while head:
            if head in visited:
                return True
            else:
                visited[head] = head
            head = head.next
        return False


if __name__ == '__main__':
    l1_root = ListNode(1)
    l1 = l1_root
    l1.next = ListNode(2)
    l1 = l1.next
    l1.next = ListNode(4)

    l2_root = ListNode(1)
    l2 = l2_root
    l2.next = ListNode(3)
    l2 = l2.next
    l2.next  = ListNode(4)

    solution = Solution()
    result = solution.mergeTwoLists(l1_root, l2_root)
    print(result)
