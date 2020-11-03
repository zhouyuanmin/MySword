"""
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数
字重复了几次。请找出数组中任意一个重复的数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

限制：
2 <= n <= 100000
"""
from typing import List


def find_repeat_number(self, nums: List[int]) -> int:
    n = len(nums)
    if not 2 <= n <= 100000:
        return -1
    i = 0
    while i < n:
        tmp = nums[i]
        if tmp == i:
            i = i + 1
            continue
        elif nums[tmp] == nums[i]:
            return nums[tmp]
        else:
            nums[tmp], nums[i] = nums[i], nums[tmp]
    return -1
