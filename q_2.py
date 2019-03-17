"""
2. 两数相加
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    示例：
        输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)

        输出：7 -> 0 -> 8
        原因：342 + 465 = 807
"""
import io
from typing import Iterable


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def of(cls, it: Iterable):
        t_n = n = ListNode(0)
        for e in it:
            n.next = cls(e)
            n = n.next
        return t_n.next

    def __str__(self):
        with io.StringIO() as s:
            s.write('[')
            t_n = self
            while t_n:
                if t_n != self:
                    s.write(', ')
                s.write(str(t_n.val))
                t_n = t_n.next
            s.write(']')
            return s.getvalue()

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        l1, l2 = self, other
        while l1 and l2:
            if l1.val != l2.val:
                return False

            l1 = l1.next
            l2 = l2.next

        return l1 is None and l2 is None


def add_two_nums(l1: ListNode, l2: ListNode) -> ListNode:
    top = l3 = ListNode(-1)
    carry = 0

    while l1 or l2:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        c = a + b + carry

        carry = c // 10
        l3.next = ListNode(c % 10)

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        l3 = l3.next

    if carry > 0:
        l3.next = ListNode(carry)

    return top.next


def test_solution():
    l1 = ListNode.of([2, 4, 3])
    l2 = ListNode.of([5, 6, 4])
    assert add_two_nums(l1, l2) == ListNode.of([7, 0, 8])

    l1 = ListNode.of([0])
    l2 = ListNode.of([0])
    assert add_two_nums(l1, l2) == ListNode.of([0])

    l1 = ListNode.of([9])
    l2 = ListNode.of([1])
    assert add_two_nums(l1, l2) == ListNode.of([0, 1])
