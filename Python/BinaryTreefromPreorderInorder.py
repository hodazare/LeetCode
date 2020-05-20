"""
Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def helper(self, preorder, dict_inorder, left_inx, right_inx):
        
        # There is no more left or right child
        if left_inx > right_inx:
            return None
        
        val = preorder.pop(0)
        root = TreeNode(val)
        
        inx = dict_inorder[val]
        
        root.left = self.helper(preorder, dict_inorder, left_inx, inx -1)
        root.right = self.helper(preorder, dict_inorder, inx+1, right_inx)
        
        return root
    
    def buildTree(self, preorder, inorder):
        
        dict_inorder = {key:val for val, key in enumerate(inorder)}
        
        return self.helper(preorder, dict_inorder, 0, len(inorder) - 1)
