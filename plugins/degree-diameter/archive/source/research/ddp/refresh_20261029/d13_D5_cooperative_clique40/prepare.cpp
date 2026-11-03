#include <algorithm>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;using U=uint64_t;
int main(int argc,char**argv){
 assert(argc==4);const clock_t start=clock();
 ifstream graph(argv[1]),sets(argv[2]);int n,m;assert(graph>>n>>m);assert(n==51457&&m==324863);
 vector<vector<int>>adj(n);for(int e=0;e<m;e++){int u,v;assert(graph>>u>>v);adj[u].push_back(v);adj[v].push_back(u);}
 int K;assert(sets>>K);assert(K==40);vector<vector<int>>S(K),P(K);map<int,vector<int>>port_users;
 for(int i=0;i<K;i++){int id,len;assert(sets>>id>>len);assert(id==i);for(int j=0;j<len;j++){int v;assert(sets>>v);S[i].push_back(v);if(adj[v].size()<13){P[i].push_back(v);port_users[v].push_back(i);}}}
 const int W=(n+63)/64;string prefix=argv[3];ofstream b3(prefix+".R3.u64.bin",ios::binary),b4(prefix+".R4.u64.bin",ios::binary);
 vector<U>r3(W),r4(W),providers3(n),providers4(n);vector<int>d(n),q(n);
 cout<<"{\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"pool_size\":"<<K<<",\"words_per_row\":"<<W<<",\"sets\":[";
 for(int i=0;i<K;i++){
  fill(d.begin(),d.end(),-1);int begin=0,end=0;for(int v:P[i]){assert(d[v]<0);d[v]=0;q[end++]=v;}
  while(begin<end){int u=q[begin++];if(d[u]==4)continue;for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;q[end++]=v;}}
  fill(r3.begin(),r3.end(),0);fill(r4.begin(),r4.end(),0);int size3=0;
  for(int v=0;v<n;v++)if(d[v]>=0){r4[v/64]|=U(1)<<(v%64);providers4[v]|=U(1)<<i;if(d[v]<=3){r3[v/64]|=U(1)<<(v%64);providers3[v]|=U(1)<<i;size3++;}}
  b3.write(reinterpret_cast<char*>(r3.data()),W*sizeof(U));b4.write(reinterpret_cast<char*>(r4.data()),W*sizeof(U));
  auto vec=[&](const char*key,const vector<int>&a){cout<<"\""<<key<<"\":[";for(size_t j=0;j<a.size();j++){if(j)cout<<",";cout<<a[j];}cout<<"]";};
  if(i)cout<<",";cout<<"{\"index\":"<<i<<",\"source_added_vertex\":"<<51417+i<<",";vec("S",S[i]);cout<<",";vec("P",P[i]);
  cout<<",\"R3_size\":"<<size3<<",\"R4_size\":"<<end<<",\"R4_missing\":"<<n-end<<",\"conditional_max_clique_size\":"<<14-P[i].size()<<"}";
 }
 cout<<"],\"ports\":[";bool first=true;for(auto&[v,users]:port_users){if(!first)cout<<",";first=false;cout<<"{\"vertex\":"<<v<<",\"current_degree\":"<<adj[v].size()<<",\"capacity\":"<<13-adj[v].size()<<",\"pool_indices\":[";for(size_t j=0;j<users.size();j++){if(j)cout<<",";cout<<users[j];}cout<<"]}";}
 ofstream p3(prefix+".providers3.u64.bin",ios::binary),p4(prefix+".providers4.u64.bin",ios::binary);
 p3.write(reinterpret_cast<char*>(providers3.data()),n*sizeof(U));p4.write(reinterpret_cast<char*>(providers4.data()),n*sizeof(U));
 cout<<"],\"source_reads\":1,\"multisource_R4_runs\":40,\"source_diameter_BFS\":0,\"worker_cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
}
