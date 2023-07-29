// Graph Representation
// Adjacency Matrix
// N X N space
#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,m;
    //n nodes,m edges
    cin >> n >> m;

    int adj[n+1][m+1];
    for(int i=0;i<m;i++){
        // to recieve m edges
        int u,v;
        cin >> u >> v;
        adj[u][v] = 1;
        adj[v][u] = 1;
        // for directed no adj[v][u]
    }
    return 0;

}