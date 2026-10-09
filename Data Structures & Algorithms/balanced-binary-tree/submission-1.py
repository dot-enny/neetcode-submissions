# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, balanced):
            if not curr: return [0, balanced]

            left = dfs(curr.left, balanced)
            right = dfs(curr.right, balanced)

            if not left[1] or not right[1]: return [1 + max(left[0], right[0]), False]

            val = [0, balanced]

            if abs(left[0] - right[0]) > 1: 
                # balanced = False
                val[0], val[1] = 1 + max(left[0], right[0]), False
            else:
                val[0], val[1] = 1 + max(left[0], right[0]), True
                
            return val

        res = dfs(root, True)

        return res[1]