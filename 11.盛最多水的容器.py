#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List


# @lc code=start
class Solution:

    def maxArea(self, height: List[int]) -> int:
        """
        算法思路: 
            双指针法：
                1. i, j 分别指向数组的头和尾
                2. 基于 i, j 所指向的元素和 j - i 距离，计算面积
                3. 如果 i 指向的元素比较大，则向前移动 j 指针，反之向后移动 i 指针
                4. 返回所有面积中最大的值

            移动元素较小的那一端指针：
                移动元素较小的那一端指针，得到的新面积不会大于之前的面积

        Args:
            height(List[int]): 高度集合

        Returns:
            int: 可能的最大面积
        """
        res = 0
        i, j = 0, len(height) - 1
        while i != j:
            h1, h2 = height[i], height[j]
            res = max((res, (j - i) * min(h1, h2)))

            if h1 >= h2:
                j -= 1
            else:
                i += 1
        return res
# @lc code=end

