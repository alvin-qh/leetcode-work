#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        算法思路: 
            翻转单向链表，即依次将指定位置的后续节点删除，插入到指定位置之前
            为了方便迭代统一，无需处理第一个特殊节点，增加一个头节点作为占位符

            本题可以在一次迭代中完成，即时间复杂度为 O(1)

        Args:
            head(ListNode): 链表头节点
            left(int)：翻转起始位置（下标从 1 算起）
            right(int)：翻转结束位置（下标从 1 算起）

        Returns:
            ListNode: 翻转后链表的头节点
        """

        if not head:
            return None

        if left >= right:
            return head

        i = 0
        head = ln = ListNode(0, head)  # 增加头节点作为占位符，令 head 指向头节点，ln 指向每次插入的节点
        # 移动 ln 指向 left 表示的节点
        while ln and i < left - 1:
            ln = ln.next
            i += 1

        mn = ln.next  # mn 为 ln 指向的节点，移动的节点将插入 ln 和 mn 之间
        rn = mn.next  # rn 指向要删除的节点

        # 整个算法过程，将 rn 指向的节点移动到 ln 和 mn 之间，相当于从链表中删除 rn，在插入到 ln 之后（mn 之前）
        # 直到 rn 指向 right 表示的节点，算法结束
        while rn and i < right - 1:
            n = rn.next
            mn.next = rn.next
            rn.next = ln.next
            ln.next = rn

            rn = n
            i += 1

        return head.next
# @lc code=end
