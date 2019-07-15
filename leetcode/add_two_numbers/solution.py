from leetcode.structures.singly_linked_list import ListNode


class Solution:
    def __call__(self, l1, l2):
        def gen_add(a, b):
            """generator based solution"""
            carry = 0
            while a and b:
                lsum = a.val + b.val + carry
                carry = lsum // 10
                yield ListNode(lsum % 10)
                a, b = a.next, b.next

            r = a or b

            while carry > 0:
                if r:
                    lsum = carry + r.val
                    carry = lsum // 10
                    yield ListNode(lsum % 10)
                    r = r.next
                else:
                    yield ListNode(carry)
                    carry = 0
            yield r
            r = None

        head = ListNode(0)
        curr = head

        for node in gen_add(l1, l2):
            curr.next = node
            curr = curr.next
        return head.next

