#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#
from typing import List


# @lc code=start
class Solution:

    def isMonotonic(self, nums: List[int]) -> bool:
        t = 0
        if nums[0] < nums[-1]:
            t = 1
        elif nums[0] > nums[-1]:
            t = -1

        i, j = 0, 1
        while j < len(nums):
            if t > 0 and nums[i] > nums[j]:
                return False

            if t < 0 and nums[i] < nums[j]:
                return False

            if t == 0 and nums[i] != nums[j]:
                return False

            i += 1
            j += 1

        return True
# @lc code=end
