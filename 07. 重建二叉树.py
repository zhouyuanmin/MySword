"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

来源：力扣
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

例如，给出
前序遍历 preorder =[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7

限制：
0 <= 节点个数 <= 5000
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> [TreeNode, None]:
        if not preorder:
            return None
        root_value = preorder[0]
        root = TreeNode(root_value)
        root_index = inorder.index(root_value)
        if root_index == 0:
            root.left = None
        else:
            root.left = self.build_tree(preorder=preorder[1:1 + root_index], inorder=inorder[0: root_index])
        if root_index == len(inorder) - 1:
            root.right = None
        else:
            root.right = self.build_tree(preorder=preorder[root_index + 1:], inorder=inorder[root_index + 1:])
        return root
