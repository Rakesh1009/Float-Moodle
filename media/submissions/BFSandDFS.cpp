#include<bits/stdc++.h>
using namespace std;

void add_edge(vector<int> edge1[], int s, int d){
    edge1[s].push_back(d);

}

void BFS(int s,vector<int>adj[],bool visit[]){
    queue<int> que;
    que.push(s);
    visit[s]=true;
    while(!que.empty()){
        int u=que.front();
        cout<<u+1<<" ";
        que.pop();

        for(int i=0;i<adj[u].size();i++){
            if(!visit[adj[u][i]]){
                que.push(adj[u][i]);
                visit[adj[u][i]]=true;
            }
        }
    }
}


void DFS(int s,vector<int>adj[],bool visit[]){
    stack<int> st;
    st.push(s);
    visit[s]=true;
    while(!st.empty()){
        int u=st.top();
        cout<<u+1<<" ";
        st.pop();

        for(int i=0;i<adj[u].size();i++){
            if(!visit[adj[u][i]]){
                st.push(adj[u][i]);
                visit[adj[u][i]]=true;
            }
        }
    }
}

void Random_Graph(int edge[][2],int edg, int ver,vector<int> edge1[]){
    int i, j, count;
    i = 0;

    while(i < edg){

        edge[i][0] = rand()%ver+1;
        edge[i][1] = rand()%ver+1;

        if(edge[i][0] == edge[i][1])
            continue;
        else{
            for(j = 0; j < i; j++){
                if((edge[i][0] == edge[j][0] && edge[i][1] == edge[j][1]) || (edge[i][0] == edge[j][1] && edge[i][1] == edge[j][0]))
                    i--;
            }
        }
        i++;
    }
    cout<<"\nThe adjacency list of the graph is: "<<endl;
    for(i = 0; i < ver; i++){
        count = 0;
        cout<<i+1<<": { ";
        for(j = 0; j < edg; j++){
            if(edge[j][0] == i+1){
                cout<<edge[j][1]<<" ";
                count++;
                add_edge(edge1,edge[j][0]-1,edge[j][1]-1);
            } 
            else if(edge[j][1] == i+1){
                cout<<edge[j][0]<<" ";
                count++;
                add_edge(edge1,edge[j][1]-1,edge[j][0]-1);
            } 
            else if(j== edg-1 && count == 0)
                cout<<"No connected vertex"; 
        }
        cout<<"}"<<endl;
   }
   cout<<endl;
}

bool bipartite(vector<int> adj[], int v,vector<bool>& visited, vector<int>& color){
 
    for (int u : adj[v]) {
        if (visited[u] == false) {
            visited[u] = true;
            color[u] = !color[v]; 
            if (!bipartite(adj, u, visited, color))
                return false;
        }
 
        else if (color[u] == color[v])
            return false;
    }
    return true;
}


int main(){
    int i, e, n;
    n= 6;
    e = n*2;
    int edge[e][2];
    vector<int> edge1[n];

    Random_Graph(edge,e, n,edge1);

    bool visit[n];
    for(int i=0;i<n;i++){
        visit[i]=false;
    }
    cout<<"BFS traversal is"<<"  ";
    BFS(0,edge1,visit);
    cout<<endl;

    for(int i=0;i<n;i++){
        visit[i]=false;
    }
    cout<<"DFS traversal is"<<"  ";
    DFS(0,edge1,visit);
    cout<<endl;

    vector<bool> visited(n);
    vector<int> color(n);
 
    visited[0] = true;
    color[0] = 0;
 
    bool x = bipartite(edge1, 0, visited, color);
    if (x) {
        cout << "Graph is bipartite";
    }
    else {
        cout << "Graph is not bipartite";
    }

    cout<<endl;
   
}