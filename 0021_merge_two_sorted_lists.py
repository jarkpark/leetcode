# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_root = ListNode(-1)
        res_nav = res_root
        while l1 or l2:
            if l1 and not l2:
                res_nav.next = ListNode(l1.val)
                res_nav = res_nav.next
                l1 = l1.next
            elif not l1 and l2:
                res_nav.next = ListNode(l2.val)
                res_nav = res_nav.next
                l2 = l2.next
            elif l1.val < l2.val:
                res_nav.next = ListNode(l1.val)
                res_nav = res_nav.next
                l1 = l1.next
            elif l1.val > l2.val:
                res_nav.next = ListNode(l2.val)
                res_nav = res_nav.next
                l2 = l2.next
            else:
                res_nav.next = ListNode(l1.val)
                res_nav = res_nav.next
                res_nav.next = ListNode(l2.val)
                res_nav = res_nav.next
                l1 = l1.next
                l2 = l2.next
        return res_root.next


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
