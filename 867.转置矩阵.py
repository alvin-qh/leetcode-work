#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
from typing import List


# @lc code=start
class Solution:

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Args:
            matrix(List[List[int]]): 输入矩阵

        Returns:
            List[List[int]]: 转置后的矩阵
        """
        m, n = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(0, n)]

        for x in range(0, m):
            for y in range(0, n):
                res[y][x] = matrix[x][y]

        return res
# @lc code=end
