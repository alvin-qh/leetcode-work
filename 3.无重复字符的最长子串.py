#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        算法思路：遍历数组 nums，以数组的每个值为被减数 a，在已存储集合 s_nums 中查找是否有匹配的减数 b = target - a
                如果找到 b，则返回 [ab索引最小值, ab索引最大值]
                如果未找到 b，则保存 b 的值和索引到 s_nums 中
                直到 a 和 b 都找到或数组完全被遍历

        Args:
            s(str): 输入的字符串

        Returns:
            int: 子字符串长度
        """

        # 保存不重复的字符序列
        cs = set()
        
        # 记录最长的不重复字符串长度
        ml = 0
        
        # i 指向当前不重复字符串结尾
        # j 指向当前不重复字符串开头
        i, j = 0, 0

        while i < len(s) and j < len(s):
            if s[i] not in cs:  # 判断下一个字符是否重复
                cs.add(s[i])  # 将未重复的字符加入序列
                i += 1
                ml = max(ml, i - j)  # 计算最大不重复字符串长度
            else:
                cs.remove(s[j])  # 从存储的字符序列中删除重复的字符
                j += 1  # 开始下一个子字符串计算

        return ml
# @lc code=end
