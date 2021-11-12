#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
from typing import List


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        算法思路: 
            从矩阵的最外层到最内层分别一圈一圈的进行计算，算法结构如下：

                是否处理完所有层？
                    处理 顶部一行
                    处理 右侧一列
                    处理 底部一行
                    处理 左侧一列

        Args:
            n(int): 矩阵的秩

        Returns:
            List[List[int]]: 生成的矩阵结果
        """
        res = [[0] * n for _ in range(n)]

        l, t, r, b = 0, 0, n - 1, n - 1  # left, top, right, buttom, initialized
        num = 1

        while l <= r and t <= b:
            # 处理顶部一行
            for i in range(l, r + 1):
                res[t][i] = num
                num += 1

            # 处理右侧一列
            for i in range(t + 1, b + 1):
                res[i][r] = num
                num += 1

            # 处理底部一行
            for i in range(r - 1, l, -1):
                res[b][i] = num
                num += 1

            # 处理左侧一列
            for i in range(b, t, -1):
                res[i][l] = num
                num += 1

            # 缩小一圈
            l += 1
            t += 1
            r -= 1
            b -= 1

        return res
# @lc code=end

# 解法 2
# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         """
#         算法思路:
#             每次遇到 边界 后，令矩阵填充方向旋转一次，以此计算矩阵填充步进，根据步进值填充矩阵下一个元素
#
#         Args:
#             n(int): 矩阵的秩
#
#         Returns:
#             List[List[int]]: 生成的矩阵结果
#         """
#         res = [[0] * n for _ in range(n)]
#         dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         rol = 0
#         x, y = 0, 0
#
#         for i in range(1, n ** 2 + 1):
#             res[x][y] = i  # 填充矩阵元素
#
#             dx, dy = dirs[rol]  # 计算矩阵填充步进值
#
#             nx, ny = x + dx, y + dy  # 计算下一个填充位置
#             # 判断下一个填充位置是否超出填充范围
#             if nx < 0 or ny < 0 or nx == n or ny == n or res[nx][ny] > 0:
#                 """
#                 填充位置超出范围的判断
#                     1. 是否超出矩阵边界[0, n - 1]
#                     2. 之前是否已经填充过值
#                 """
#                 rol = (rol + 1) % 4  # 对于过界结果，旋转填充方向，重新计算步进值
#                 dx, dy = dirs[rol]
#
#             # 前进到下一个填充位置
#             x += dx
#             y += dy
#
#         return res
