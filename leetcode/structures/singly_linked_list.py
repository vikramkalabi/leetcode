# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        s = "[ "
        node = self

        while node:
            s += f"{node.val} "
            node = node.next
        return s + "]"

    @classmethod
    def from_list(cls, elements, reversed=False):
        if len(elements) == 0:
            return None

        if not reversed:
            elements = elements[::-1]

        curr = None
        for el in elements:
            if curr is None:
                curr = ListNode(el)
            else:
                node = ListNode(el)
                node.next = curr
                curr = node
        return curr

