"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def isSymmetric(self, root):
        if not root:
            return True
        q = [(root, root)]
        while q:
            t1, t2 = q.pop()
            if (not t1 and not t2):
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            
            q.append((t1.left, t2.right))
            q.append((t1.right, t2.left))
        return True
    
    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
        
    def isSymmetricRecurssive(self, root):
        return self.isMirror(root, root)
