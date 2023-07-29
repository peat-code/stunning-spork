// BFS Graph
#include<bits/stdc++.h>

using namespace std;

class Solution{
    public:
    vector<int> bfsGraph(int n,vector<int> adj[]){
        int vis[n] = {0};   // visited array
        vis[0] = 1;
        queue<int> q;    // queue
        q.push(0);
        vector<int>bfs;  // answer
        while(!q.empty()){
            int node = q.front(); 
            q.pop();
            bfs.push(node);
            for(auto it:adj[node]){
                if (!vis[node]){
                    q.push(it);
                    vis[node] = 1;
            }}
        }
    }
    return bfs;
}