#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        算法思路：在循环中，同步依次获取 l1 和 l2 链表各元素值 a 与 b
                若某个链表已到达末尾，则对应的 a 或 b 值为 0
                计算 c 的值为 a + b + 进位值
                在结果链表中存储 c % 10 的值，并保存进位值为 c // 10
                直到 l1, l2 链表均遍历完毕，若剩余有进位值，则在结果链表中在保持进位值
                计算结束

        Args:
            l1(ListNode): 链表1
            l2(ListNode): 链表2

        Returns:
            ListNode: 输入的两个链表各元素相加的结果链表
        """
        # top 头节点
        # l3 尾节点
        top = l3 = ListNode(-1)
        
        # 进位值
        carry = 0

        while l1 or l2:
            # 第一个数字
            a = l1.val if l1 else 0
            # 第二个数字
            b = l2.val if l2 else 0
            # 计算两个数字和进位值的和
            c = a + b + carry

            # 计算进位值
            carry = c // 10
            # 保存结果节点
            l3.next = ListNode(c % 10)
            l3 = l3.next

            # l1 和 l2 链表前进一个元素
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # 若剩余进位值，记录保存进位的节点
        if carry > 0:
            l3.next = ListNode(carry)

        return top.next
# @lc code=end
