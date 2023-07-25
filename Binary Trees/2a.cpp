// Representation of binary tree in C++

#include<iostream>
using namespace std;

struct Node{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int val){
        data =val;
        left = right = NULL;
    }
};



int main(){

    struct Node *root = new Node(5);
    root->left = new Node(4);
    root->right = new Node(6);
    root->left->right = new Node(7);
    cout << root->left->right->data;
    return 0;
}