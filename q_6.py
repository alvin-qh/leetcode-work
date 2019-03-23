"""
6. Z 字形变换
    将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
    比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
        L   C   I   R
        E T O E S I I G
        E   D   H   N

    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

    示例 1:
        输入: s = "LEETCODEISHIRING", rows = 3
        输出: "LCIRETOESIIGEDHN"

    示例 2:
        输入: s = "LEETCODEISHIRING", rows = 4
        输出: "LDREOEIIECIHNTSG"
        解释:
            L     D     R
            E   O E   I I
            E C   I H   N
            T     S     G
"""


def convert(s: str, rows: int) -> str:
    if rows == 1:
        return s

    result = []
    n, cycle_len = len(s), 2 * rows - 2

    for i in range(rows):
        j = 0
        while j + i < n:
            result.append(s[j + i])
            if i != 0 and i != rows - 1 and j + cycle_len - i < n:
                result.append(s[j + cycle_len - i])
            j += cycle_len
    return ''.join(result)


def test_solution():
    assert convert('LEETCODEISHIRING', 3) == 'LCIRETOESIIGEDHN'
    assert convert('LEETCODEISHIRING', 4) == 'LDREOEIIECIHNTSG'
