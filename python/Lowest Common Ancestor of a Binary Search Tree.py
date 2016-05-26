__author__ = 'erica'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        ptr = root
        while (ptr.val - p.val) * (ptr.val - q.val) > 0:
            if ptr.val > p.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return ptr