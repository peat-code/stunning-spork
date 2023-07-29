class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(root):
            if not root:
                return 0
            lh = check(root.left)
            rh = check(root.right)
            if(lh == -1 or rh == -1):
                return -1
            if(abs(lh-rh)>1):
                return -1
            return 1+max(lh,rh)
        if check(root) == -1:
            return False
        else:
            return True