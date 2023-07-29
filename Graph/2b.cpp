// Graph Representation
// Adjacency List
// C++ list = vector
// array of nodes, each array contains list
// Space 2E
#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,m;
    //n nodes,m edges
    cin >> n >> m;
    // adjacency list
    vector<int> adj[n+1];
    // int adj[n+1][m+1];
    for(int i=0;i<m;i++){
        // to recieve m edges
        int u,v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        // for directed no adj[v].push_back
    }
    for(int i=0;i<n;i++){
        for (auto element : adj[i]) {
            cout << element << " ";
    }
        cout << endl;
    }
    return 0;

}