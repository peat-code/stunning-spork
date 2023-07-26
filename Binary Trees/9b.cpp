// Iterative Preorder Traversal
    // Add root to stack
    // while stack
    //     pop element and print
    //     push its right child
    //     push its left child
#include<vector>
class Solution{

    public:
        vector<int> preorder(TreeNode* root){
            vector<int> traversal;
            if (root == NULL)
                return traversal;    // happens only for NULL TreeNode
            TreeNode* curr;
            // main driver
            stack<TreeNode*>st;
            st.push(root);
            while(!st.empty()){
                curr = st.top()
                st.pop();
                traversal.push_back(curr->val);
                if (curr->left != NULL) 
                    st.push(curr->right);
                if (curr->right != NULL)
                    st.push(curr->left);
            }
            return traversal;
        }




};