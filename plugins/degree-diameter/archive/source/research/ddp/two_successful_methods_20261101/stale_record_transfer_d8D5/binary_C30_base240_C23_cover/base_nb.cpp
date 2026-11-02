#include<vector>
#include<array>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<limits>
#include<cassert>
using namespace std;
int main(){ifstream in("BASE240.edges");int n,m;in>>n>>m;assert(n==240&&m==960);vector<vector<int>>g(n),oe(n);vector<int>from,to;for(int k=0;k<m;++k){int u,v;in>>u>>v;g[u].push_back(v);g[v].push_back(u);int id=from.size();from.push_back(u);to.push_back(v);from.push_back(v);to.push_back(u);oe[u].push_back(id);oe[v].push_back(id+1);}for(auto&r:g)assert(r.size()==8);
 int diam=0,minimum=100000000,badu=-1,badv=-1;long badpairs=0;vector<int>badsteps;ofstream rows("BASE_ROOT_NB_STATS.tsv");rows<<"root\teccentricity\tminclosedNB5\tmin_target\n";
 for(int root=0;root<n;++root){vector<int>d(n,-1),q;d[root]=0;q.push_back(root);for(size_t k=0;k<q.size();++k)for(int v:g[q[k]])if(d[v]<0){d[v]=d[q[k]]+1;q.push_back(v);}int ecc=*max_element(d.begin(),d.end());if(q.size()!=size_t(n))ecc=1000000;diam=max(diam,ecc);
  vector<int>cur(2*m),total(n);vector<array<int,6>>step(n);total[root]=step[root][0]=1;for(int e:oe[root]){cur[e]=1;++total[to[e]];++step[to[e]][1];}
  for(int len=2;len<=5;++len){vector<int>at(n),next(2*m);for(int e=0;e<2*m;++e)at[to[e]]+=cur[e];for(int e=0;e<2*m;++e){next[e]=at[from[e]]-cur[e^1];assert(next[e]>=0);total[to[e]]+=next[e];step[to[e]][len]+=next[e];}cur.swap(next);}
  int v=min_element(total.begin(),total.end())-total.begin();rows<<root<<'\t'<<ecc<<'\t'<<total[v]<<'\t'<<v<<'\n';for(int x:total)if(x<23)++badpairs;
  if(total[v]<minimum){minimum=total[v];badu=root;badv=v;badsteps.assign(step[v].begin(),step[v].end());}
 }
 ofstream out("NATIVE_RESULT.json");out<<"{\"source_n\":240,\"source_m\":960,\"source_degree\":8,\"new_base_ordinary_BFS_roots\":240,\"base_diameter\":"<<diam<<",\"minimum_NB_walks0to5\":"<<minimum<<",\"minimum_pair\":["<<badu<<','<<badv<<"],\"minimum_pair_steps0to5\":[";for(int k=0;k<6;++k){if(k)out<<',';out<<badsteps[k];}out<<"],\"ordered_pairs_below23\":"<<badpairs<<",\"capacity_pass\":"<<(minimum>=23?"true":"false")<<",\"ordinary_allfolds_ge23_NO\":"<<(minimum<23?"true":"false")<<"}\n";
 cout<<"baseD="<<diam<<" minNB="<<minimum<<" badpairs="<<badpairs<<endl;
}
