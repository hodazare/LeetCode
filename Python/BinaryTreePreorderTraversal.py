"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Three methods can be used:
1- Recursive 
2- Iterations using stack
3: Iteration without extra space (Morris traversal)

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, v):
#         self.val = v
#         self.left = None
#         self.right = None

class Solution(object):
   
    def preorderTraversalMorris(self, root):
        if not root:
            return None
        node, output = root, []
        
        while node:
            if node.left:
                pre = node.left
               
                while pre.right and pre.right != node:
                    pre = pre.right
                
                if pre.right == node:
                    pre.right = None
                    node = node.right
                else:
                    output.append(node.val)
                    pre.right = node                    
                    node = node.left
            else:
                output.append(node.val)
                node = node.right
        
        return output
        
    def preorderTraversalStack(self, root):
        
        if not root:
            return None
        output = []
        stack = [root]
        while stack:
            node = stack.pop()
            output.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
        
        return output
        
        def preorderTraversalRecursion(self, root):
         return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
