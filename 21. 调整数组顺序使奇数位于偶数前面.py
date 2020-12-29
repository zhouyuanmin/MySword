"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 

提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10000

来源：力扣
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def exchange(self, nums: List[int]) -> List[int]:
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] % 2 == 0 and nums[j] % 2 == 1:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
        elif nums[i] % 2 == 1:
            i = i + 1
        elif nums[j] % 2 == 0:
            j = j - 1
    return nums