# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 1
        curr, stack = root, []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            next = stack.pop()
            curr = next.right
            if res < k: res += 1
            else: return next.val
        
