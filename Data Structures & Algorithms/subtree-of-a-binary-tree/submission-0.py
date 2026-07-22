# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSub(root, subRoot):
            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False

            if root.val != subRoot.val:
                return False

            return (
                isSub(root.left, subRoot.left)
                and isSub(root.right, subRoot.right)
            )

        def theSame(root, subRoot):
            if not subRoot:
                return True

            if not root:
                return False

            if isSub(root, subRoot):
                return True

            return (
                theSame(root.left, subRoot)
                or theSame(root.right, subRoot)
            )

        return theSame(root, subRoot)