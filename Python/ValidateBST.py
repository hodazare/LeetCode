"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# use a stack to keep the node and the related most lowest/highest values
# DFS/BFS is used for traversing the tree

class BST(object):
  
  def isBST(self, root):
    if not root:
      return True
    stack = [(root, float('-inf'), float('inf'))]
    
    while stack:
      node, lower, upper = stack.pop()
      if node.val <= lower or node.val >= upper:
        return False
      if node.left:
        stack.append((node.left, lower, node.val)
        stack.append((node.right, node.val, upper))
  return True     
  
