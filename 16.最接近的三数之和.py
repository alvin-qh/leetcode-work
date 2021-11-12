#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List


# @lc code=start
class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        算法说明:
            对数组进行排序，这样才能保证查找过程中不会访问到重复值
            三个指针 a, b, c，分别指向 第一个加数（从 0 下标开始），第二个加数（从 a + 1 开始），第三个加数（从数组末尾开始）

            因为数组有序，所以 b > a, c > b 成立，因为之前的元素都已经枚举过

            比较每次迭代产生的和，和之前计算结果进行比较，找到和 target 最接近的值

        Args:
            nums(List[int]): 输入的字符串数组
            target(int): 目标值，找出的三数之和与该值最接近

        Returns:
            int: 和 target 值最接近的三数之和
        """
        nums.sort()
        res = 10000000

        def update(n):
            """
            检查输入的值 n 和历史值 res 谁更接近 target
            """
            nonlocal res
            if abs(n - target) < abs(res - target):
                res = n

        # i, a, b 分别为三个指针:
        #    i 依次指向数组的每个元素
        #    a, b 为双指针，指向 i 之后的元素，a 从左到右，b 从右到左
        # 因为数组是有序的，所以 a 和 b 指针无需重合

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 排除相邻的相同值（已计算过）
                continue

            a, b = i + 1, len(nums) - 1
            while a < b:
                s = nums[i] + nums[a] + nums[b]
                if s == target:
                    return target

                update(s)
                if s > target:
                    b0 = b - 1
                    while a < b0 and nums[b] == nums[b0]:
                        b0 -= 1

                    b = b0
                elif s < target:
                    a0 = a + 1
                    while a0 < b and nums[a] == nums[a0]:
                        a0 += 1

                    a = a0
        return res
# @lc code=end
