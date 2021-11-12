#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List


# @lc code=start
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        算法思路: 
            遍历数组 nums，以数组的每个值为被减数 a，在已存储集合 s_nums 中查找是否有匹配的减数 b = target - a
            如果找到 b，则返回 [b的索引, a的索引]
            如果未找到 b，则保存 b 的值和索引到 s_nums 中
            直到 a 和 b 都找到或数组完全被遍历

        Args:
            nums(List[int]): 输入的数组
            target(int): 期望的和

        Returns:
            int: 返回数组中和为期望值的两个元素的下标
        """
        s_nums = {}
        
        for idx, val in enumerate(nums):
            if val in s_nums:
                return [s_nums[val], idx]

            s_nums[target - val] = idx

        return None
# @lc code=end

