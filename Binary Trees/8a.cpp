// BFS Traversal in C++

#include<iostream>

using namespace std;

// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// }



class Solution{
    public:
        vector<vector<int>> levelOrder(TreeNode* root){
            vector<vector<int>> ans;
            if (root == NULL)  
                return ans;
            queue<TreeNode*> q;
            q.push(root)
            while (!q.empty()){
                int size = q.size();
                vector<int> level;
                for(int i=0;i<size;i++)
                    TreeNode *curr = q.front();
                    q.pop();
                    level.pushback(curr->val);
                    if (curr->left != NULL) q.push(curr->left);
                    if (curr->right != NULL) q.push(curr->right);
            }



        }



}



int main(){



}