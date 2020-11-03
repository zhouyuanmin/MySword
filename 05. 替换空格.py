"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

来源：力扣
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

限制：
0 <= s 的长度 <= 10000
"""
from typing import List


def replace_space(self, s: str) -> str:
    chars: List = []
    for i in s:
        if i == ' ':
            chars.append('%20')
        else:
            chars.append(i)
    return ''.join(chars)
