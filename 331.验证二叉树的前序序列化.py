#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:

    def isValidSerialization(self, preorder: str) -> bool:
        """
        算法思路:

        Args:
            preorder(str): 输入的二叉树前序序列

        Returns:
            bool: 输入的前序序列是否正确
        """
        i = 0
        stack = [1]
        while i < len(preorder):
            if len(stack) == 0:
                return False

            if preorder[i] == ',':
                i += 1
            elif preorder[i] == '#':  # 空节点
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
                i += 1
            else:
                while i < len(preorder) and preorder[i] != ',':
                    i += 1

                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()

                stack.append(2)

        return len(stack) == 0
# @lc code=end

# 解法2
# class Solution:
#
#     def isValidSerialization(self, preorder: str) -> bool:
#         """
#         算法思路:
#             和 Sulution 1 思路一致，将栈的使用改为计数器，代表栈中所有元素之和
#
#         Args:
#             preorder(str): 输入的二叉树前序序列
#
#         Returns:
#             bool: 输入的前序序列是否正确
#         """
#         i = 0
#         slots = 1
#         while i < len(preorder):
#             if slots == 0:
#                 return False
#
#             if preorder[i] == ',':
#                 i += 1
#             elif preorder[i] == '#':  # 空节点
#                 slots -= 1
#                 i += 1
#             else:
#                 while i < len(preorder) and preorder[i] != ',':
#                     i += 1
#                 slots += 1  # slots = slots - 1 + 2
#
#         return slots == 0

# cspell: ignore fuxuemingzhu
# 解法3
# class Solution:
#
#     def isValidSerialization(self, preorder: str) -> bool:
#         """
#         算法思路:
#             参考 fuxuemingzhu 的答案（https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/solution/pai-an-jiao-jue-de-liang-chong-jie-fa-zh-66nt/）
#             在树（甚至图）中，所有节点的入度之和等于出度之和。可以根据这个特点判断输入序列是否为有效的
#             在一棵二叉树中：
#                 - 每个空节点（"#"）会提供 0 个出度和 1 个入度
#                 - 每个非空节点会提供 2 个出度和 1 个入度
#                 - 我们只要把字符串遍历一次，每个节点都累加 diff = 出度 - 入度
#                 在遍历到任何一个节点的时候，要求 diff >= 0，原因是还没遍历到该节点的子节点，所以此时的出度应该大于等于入度
#                 当所有节点遍历完成之后，整棵树的 diff == 0
#
#             为什么下面的代码中 diff 的初始化为 1？
#                 因为，加入一个非空节点时，都会先减去一个入度，再加上两个出度。但是由于根节点没有父节点，所以其入度为 0，出度为 2
#                 因此 diff 初始化为 1，是为了在加入根节点的时候，先减去一个入度，再加上两个出度，此时 diff 正好应该是2
#
#         Args:
#             preorder(str): 输入的二叉树前序序列
#
#         Returns:
#             bool: 输入的前序序列是否正确
#         """
#         nodes = preorder.split(',')
#         diff = 1
#         for node in nodes:
#             diff -= 1
#
#             if diff < 0:
#                 return False
#             if node != '#':
#                 diff += 2
#
#         return diff == 0
