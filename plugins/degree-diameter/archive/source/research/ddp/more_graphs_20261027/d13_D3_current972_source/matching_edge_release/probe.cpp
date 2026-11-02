#include <algorithm>
#include <array>
#include <cassert>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
constexpr int N=972;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int main(int argc,char**argv){
 assert(argc==3);string source=argv[1],out=argv[2];double start=cpu();
 ifstream f(source);int n,m;f>>n>>m;assert(n==972&&m==6264);
 vector<vector<int>>adj(n);vector<pair<int,int>>inside;
 for(int i=0,u,v;i<m;i++){f>>u>>v;adj[u].push_back(v);adj[v].push_back(u);if(u/27==v/27)inside.emplace_back(min(u,v),max(u,v));}
 for(auto&r:adj)sort(r.begin(),r.end());sort(inside.begin(),inside.end());assert(inside.size()==432);
 long long bfs=0,crosspairs=0;int processed=0,u_fail=0,v_fail=0,cross_fail=0,safe=0;bool limited=false;
 ofstream cases(out+"/CASES.jsonl"),safes(out+"/SAFE_EDGES.jsonl");
 auto R3=[&](int root,int eu,int ev,array<short,N>&d){d.fill(-1);int queue[N],lo=0,hi=0;d[root]=0;queue[hi++]=root;
  while(lo<hi){int a=queue[lo++];if(d[a]==3)continue;for(int b:adj[a]){if((a==eu&&b==ev)||(a==ev&&b==eu))continue;if(d[b]<0){d[b]=d[a]+1;queue[hi++]=b;}}}++bfs;return hi;};
 for(int k=0;k<(int)inside.size();k++){
  if((k%16)==0&&cpu()-start>2.9){limited=true;break;}
  auto[u,v]=inside[k];array<short,N>d;string typ="SAFE";int wr=-1,wt=-1;int rootBFS=0,pairtests=0;
  int reached=R3(u,u,v,d);rootBFS++;
  if(reached<n){typ="ENDPOINT_U_R3_FAIL";wr=u;wt=find(d.begin(),d.end(),-1)-d.begin();u_fail++;}
  if(wr<0){reached=R3(v,u,v,d);rootBFS++;if(reached<n){typ="ENDPOINT_V_R3_FAIL";wr=v;wt=find(d.begin(),d.end(),-1)-d.begin();v_fail++;}}
  if(wr<0)for(int x:adj[u]){if(x==v)continue;R3(x,u,v,d);rootBFS++;
   for(int y:adj[v]){if(y==u)continue;pairtests++;crosspairs++;if(d[y]<0){typ="MIDDLE_EDGE_CROSSPAIR_FAIL";wr=x;wt=y;cross_fail++;break;}}
   if(wr>=0)break;
  }
  if(wr<0){safe++;safes<<"{\"ordinal\":"<<k<<",\"u\":"<<u<<",\"v\":"<<v<<",\"block\":"<<u/27<<"}\n";}
  cases<<"{\"ordinal\":"<<k<<",\"edge\":["<<u<<','<<v<<"],\"block\":"<<u/27<<",\"status\":\""<<typ<<"\",\"modified_R3_roots\":"<<rootBFS<<",\"crosspairs_checked\":"<<pairtests<<",\"witness_root\":"<<wr<<",\"witness_target\":"<<wt<<"}\n";
  ++processed;
 }
 ofstream r(out+"/NATIVE_RESULT.json");
 r<<"{\"status\":\""<<(limited?"CPU_LIMITED_PARTIAL":safe?"COMPLETE_SINGLE_MATCHING_DELETIONS_SAFE_PRESENT":"COMPLETE_ALL432_SINGLE_MATCHING_DELETIONS_UNSAFE")<<"\",\"edges_scope\":432,\"edges_processed\":"<<processed<<",\"unattempted\":"<<432-processed<<",\"safe_edges\":"<<safe<<",\"endpoint_u_failed\":"<<u_fail<<",\"endpoint_v_failed\":"<<v_fail<<",\"middle_crosspair_failed\":"<<cross_fail<<",\"modified_radius3_BFS\":"<<bfs<<",\"crosspairs_checked\":"<<crosspairs<<",\"native_CPU_seconds\":"<<cpu()-start<<",\"CPU_limited\":"<<(limited?"true":"false")<<",\"source_original_BFS\":0,\"new_graphs_generated\":0}\n";
 cerr<<"DONE processed "<<processed<<" safe "<<safe<<" BFS "<<bfs<<" CPU "<<cpu()-start<<'\n';
}
