# postorder traversal


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        curr = root
        st = []
        while curr or st:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                temp = st[-1].right
                if temp:
                    curr = temp
                else:
                    temp = st.pop()
                    res.append(temp.val)
                    while st and (temp==st[-1].right):
                        temp = st.pop()
                        res.append(temp.val)

        return res