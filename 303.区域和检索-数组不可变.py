#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
from typing import List


# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        """
        算法说明:
            预处理，为了加快运算效率，预先计算数组的元素和
            产生一个数组 _sum[n]，每第 j 的元素是原数组 [0, j - 1] 范围内元素的和
        Args:
            nums(List[int]): 输入的数组
        """
        self._sums = [0]
        for n in nums:
            self._sums.append(self._sums[-1] + n)

    def sumRange(self, left: int, right: int) -> int:
        """
        计算 i ~ j 元素的和，只需根据 _sum 数组，计算 _sums[j + 1] - _sums[i] 即可
        即 (前j项元素和 - 前i项元素和) = 第i~j项元素和
        """
        return self._sums[right + 1] - self._sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

