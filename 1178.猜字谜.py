#
# @lc app=leetcode.cn id=1178 lang=python3
#
# [1178] 猜字谜
#
from functools import lru_cache
from test.test_threading import Counter
from typing import List


# @lc code=start
class Solution:
    A = ord('a')

    @classmethod
    @lru_cache
    def _c_mask(cls, c: str):
        """
        返回指定字符的二进制标识位
        例如 'a' 为 '1'，'b' 为 '10', 'c' 为 '100' 等
        """
        return 1 << (ord(c) - cls.A)

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        Args:
            words(List[str]): 输入的词列表
            puzzles(List[str]): 字谜的谜面列表

        Returns:
            List[int]: 转置后的矩阵
        """

        freq = Counter()
        
        for w in words:
            mask = 0

            # 计算一个单词的二进制掩码
            for c in w:
                mask |= self._c_mask(c)

            if str(bin(mask)).count('1') <= 7:
                freq[mask] += 1

        res = []
        for puzzle in puzzles:
            total = 0

            mask = 0
            for i in range(1, 7):
                mask |= self._c_mask(puzzle[i])

            subset = mask
            while subset:
                s = subset | self._c_mask(puzzle[0])
                if s in freq:
                    total += freq[s]

                subset = (subset - 1) & mask

            # 在枚举子集的过程中，要么会漏掉全集 mask，要么会漏掉空集
            # 这里会漏掉空集，因此需要额外判断空集
            if self._c_mask(puzzle[0]) in freq:
                total += freq[self._c_mask(puzzle[0])]

            res.append(total)

        return res
# @lc code=end

