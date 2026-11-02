#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 assert(argc==4);clock_t started=clock();ifstream in(argv[1]);int n,m;in>>n>>m;assert(n==1141&&m==7987);
 vector<pair<int,int>>edges(m);for(auto&[u,v]:edges){assert(bool(in>>u>>v));assert(0<=u&&u<v&&v<n);}assert(is_sorted(edges.begin(),edges.end()));
 ifstream cf(argv[2]);vector<int>cuts(7);for(int&id:cuts)assert(bool(cf>>id));sort(cuts.begin(),cuts.end());assert(adjacent_find(cuts.begin(),cuts.end())==cuts.end());
 set<int>S;for(int id:cuts){assert(0<=id&&id<m);S.insert(edges[id].first);S.insert(edges[id].second);}assert(S.size()==14);
 vector<vector<int>>g(n+1);for(int id=0;id<m;id++)if(!binary_search(cuts.begin(),cuts.end(),id)){auto[u,v]=edges[id];g[u].push_back(v);g[v].push_back(u);}for(int s:S){g[s].push_back(n);g[n].push_back(s);}
 int arcs=0;for(int u=0;u<=n;u++){sort(g[u].begin(),g[u].end());assert(g[u].size()==14&&adjacent_find(g[u].begin(),g[u].end())==g[u].end());arcs+=g[u].size();}assert(arcs/2==7994);
 vector<pair<int,int>>bad;int roots=0,hubMissing=0;
 auto bfs=[&](int s){vector<int>d(n+1,-1),q(n+1);int lo=0,hi=1;q[0]=s;d[s]=0;while(lo<hi){int u=q[lo++];if(d[u]==3)continue;for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;q[hi++]=v;}}roots++;return d;};
 auto dh=bfs(n);for(int t=0;t<n;t++)if(dh[t]<0)hubMissing++;
 assert(hubMissing==0);
 for(int s=0;s<n&&bad.size()<32;s++){auto d=bfs(s);for(int t=s+1;t<n&&bad.size()<32;t++)if(d[t]<0)bad.push_back({s,t});}
 bool hit=bad.empty();string prefix=argv[3];ofstream o(prefix+".verify.json");o<<"{\"status\":\""<<(hit?"COMPLETE_D3_HIT":"MODIFIED_R3_COUNTEREXAMPLES")<<"\",\"n\":1142,\"m\":7994,\"max_degree\":14,\"simple\":true,\"regular\":true,\"modified_R3_root_checks\":"<<roots<<",\"hub_R3_missing\":0,\"bad_pairs_sample\":[";bool f=true;for(auto[p,q]:bad){if(!f)o<<',';f=false;o<<'['<<p<<','<<q<<']';}o<<"],\"bad_pair_count_is_complete\":"<<(hit?"true":"false")<<",\"actual_global_D\":"<<(hit?"3":"null")<<",\"CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<"}\n";
 if(hit){ofstream gr(prefix+".edges");gr<<n+1<<' '<<arcs/2<<'\n';for(int u=0;u<=n;u++)for(int v:g[u])if(u<v)gr<<u<<' '<<v<<'\n';}
 cout<<(hit?"HIT":"COUNTEREXAMPLES")<<" roots="<<roots<<" witnesses="<<bad.size()<<'\n';
}
