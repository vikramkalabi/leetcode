from leetcode.structures.singly_linked_list import ListNode


class Solution:
    def __call__(self, l1, l2):
        if not (l1 or l2):
            return ListNode(None)

        head = ListNode(0)
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            curr.next = node
            curr = node
        if not l1:
            curr.next = l2

        elif not l2:
            curr.next = l1

        return head.next
