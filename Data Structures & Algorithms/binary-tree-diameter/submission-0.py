# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def getDiameter(root):
            if not root: return 0
            l_height, r_height = 0, 0
            if root.left:
                l_height += 1
                l_height += getDiameter(root.left)
            if root.right: 
                r_height += 1
                r_height += getDiameter(root.right)
            diameter = l_height + r_height
            self.res = max(self.res, diameter)
            return max(l_height, r_height)
        getDiameter(root)

        return self.res
        
        