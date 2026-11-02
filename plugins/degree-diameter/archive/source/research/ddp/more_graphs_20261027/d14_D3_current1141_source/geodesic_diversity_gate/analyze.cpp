#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <sys/resource.h>
#include <vector>
using namespace std;
constexpr int N=1141,D=14;
static uint16_t A2[N][N],A3[N][N],H[N][N];
static bool A[N][N];static array<int,D>adj[N];
template<class T>void arr(ostream&o,const T&v){o<<'[';bool f=true;for(auto x:v){if(!f)o<<',';f=false;o<<x;}o<<']';}
void binary(const string&path,uint16_t a[N][N]){ofstream o(path,ios::binary);for(int u=0;u<N;u++)for(int v=0;v<N;v++){o.put(char(a[u][v]&255));o.put(char(a[u][v]>>8));}}
int main(int argc,char**argv){
 assert(argc==3);rlimit lim{10,10};assert(setrlimit(RLIMIT_CPU,&lim)==0);clock_t start=clock();string dir=argv[2];
 ifstream in(argv[1]);int n,m,u,v;in>>n>>m;assert(n==N&&m==7987);array<int,N>deg{};
 for(int e=0;e<m;e++){assert(bool(in>>u>>v));assert(u>=0&&u<N&&v>=0&&v<N&&u!=v&&!A[u][v]);A[u][v]=A[v][u]=true;assert(deg[u]<14&&deg[v]<14);adj[u][deg[u]++]=v;adj[v][deg[v]++]=u;}
 assert(!(in>>u));for(int x=0;x<N;x++){assert(deg[x]==14);sort(adj[x].begin(),adj[x].end());}
 for(int x=0;x<N;x++)for(int y:adj[x])for(int z:adj[y])A2[x][z]++;
 for(int x=0;x<N;x++)for(int y=0;y<N;y++)if(A2[x][y])for(int z:adj[y])A3[x][z]+=A2[x][y];
 for(int x=0;x<N;x++){int s2=0,s3=0;for(int y=0;y<N;y++){s2+=A2[x][y];s3+=A3[x][y];assert(A2[x][y]==A2[y][x]&&A3[x][y]==A3[y][x]);}assert(s2==196&&s3==2744);}
 array<long long,15>supportHist{},minHist{};long long farpairs=0,singletonpairs=0;int unreachable=0;
 vector<int>eligible;ofstream supports(dir+"/VERTEX_FIRST_SUPPORTS.jsonl"),ef(dir+"/ELIGIBLE_SPLIT_HYPEREDGES.jsonl");
 for(int x=0;x<N;x++){
  int minH=15,minTarget=-1;vector<int>singletons;vector<pair<int,int>>far;
  for(int t=0;t<N;t++)if(t!=x&&!A[x][t]&&A2[x][t]==0){
   if(A3[x][t]==0){unreachable++;continue;}
   int mask=0;for(int k=0;k<14;k++)if(A2[adj[x][k]][t]>0)mask|=1<<k;assert(mask);H[x][t]=mask;
   int card=__builtin_popcount((unsigned)mask);supportHist[card]++;farpairs++;far.push_back({t,mask});
   if(card<minH){minH=card;minTarget=t;}if(card==1){singletons.push_back(t);singletonpairs++;}
  }
  assert(minH<=14);minHist[minH]++;supports<<"{\"v\":"<<x<<",\"neighbors_bit_order\":";arr(supports,adj[x]);supports<<",\"distance3_targets\":"<<far.size()<<",\"min_first_support\":"<<minH<<",\"minimum_target\":"<<minTarget<<",\"singleton_count\":"<<singletons.size()<<",\"singleton_targets\":";arr(supports,singletons);
  supports<<",\"first_singleton_witness\":";if(singletons.empty())supports<<"null";else{int t=singletons.front(),k=__builtin_ctz((unsigned)H[x][t]);supports<<"{\"target\":"<<t<<",\"unique_first_neighbor\":"<<adj[x][k]<<",\"mask\":"<<H[x][t]<<'}';}supports<<"}\n";
  if(singletons.empty()){
   eligible.push_back(x);ef<<"{\"v\":"<<x<<",\"neighbors_bit_order\":";arr(ef,adj[x]);ef<<",\"min_first_support\":"<<minH<<",\"far_target_masks\":[";bool first=true;for(auto [t,mask]:far){if(!first)ef<<',';first=false;ef<<'['<<t<<','<<mask<<']';}ef<<"]}\n";
  }
 }
 supports.close();ef.close();assert(unreachable==0);
 binary(dir+"/A2.u16le.bin",A2);binary(dir+"/A3.u16le.bin",A3);binary(dir+"/FIRST_SUPPORTS.u16le.bin",H);
 array<long long,14>matchingHist{};long long criticalTotal=0;int perfect=0,eid=0;vector<int>firstPerfect,firstNonperfect;
 ofstream edges(dir+"/EDGE_CRITICAL_MATCHINGS.jsonl");
 for(int x=0;x<N;x++)for(int y=x+1;y<N;y++)if(A[x][y]){
  vector<int>L,R;for(int p:adj[x])if(p!=y)L.push_back(p);for(int q:adj[y])if(q!=x)R.push_back(q);assert(L.size()==13&&R.size()==13);
  array<int,13>masks{},match;match.fill(-1);int nc=0;
  for(int i=0;i<13;i++)for(int j=0;j<13;j++){int p=L[i],q=R[j];if(p!=q&&!A[p][q]&&A2[p][q]==0&&A3[p][q]==1){masks[i]|=1<<j;nc++;}}
  function<bool(int,int&)>aug=[&](int i,int&seen){for(int j=0;j<13;j++)if((masks[i]>>j&1)&&!(seen>>j&1)){seen|=1<<j;if(match[j]<0||aug(match[j],seen)){match[j]=i;return true;}}return false;};
  int card=0;for(int i=0;i<13;i++){int seen=0;card+=aug(i,seen);}matchingHist[card]++;criticalTotal+=nc;
  if(card==13){set<int>physical(L.begin(),L.end());physical.insert(R.begin(),R.end());assert(physical.size()==26&&!physical.count(x)&&!physical.count(y));perfect++;if(firstPerfect.empty())firstPerfect={x,y};}
  else if(firstNonperfect.empty())firstNonperfect={x,y,card};
  edges<<"{\"edge_id\":"<<eid++<<",\"edge\":["<<x<<','<<y<<"],\"L\":";arr(edges,L);edges<<",\"R\":";arr(edges,R);edges<<",\"critical_row_masks\":";arr(edges,masks);edges<<",\"critical_pair_count\":"<<nc<<",\"maximum_matching\":"<<card<<",\"matching_pairs\":[";bool first=true;for(int j=0;j<13;j++)if(match[j]>=0){if(!first)edges<<',';first=false;edges<<'['<<L[match[j]]<<','<<R[j]<<']';}edges<<"]}\n";
 }
 edges.close();assert(eid==7987);
 ofstream o(dir+"/NATIVE_RESULT.json");o<<"{\"status\":\"COMPLETE_NECESSARY_CACHE\",\"source_n\":1141,\"source_m\":7987,\"source_degree\":14,\"distance3_ordered_pairs\":"<<farpairs<<",\"first_support_size_histogram\":";arr(o,supportHist);o<<",\"per_vertex_minimum_support_histogram\":";arr(o,minHist);o<<",\"singleton_ordered_pairs\":"<<singletonpairs<<",\"eligible_vertices_without_singleton\":";arr(o,eligible);o<<",\"balanced_split_all_vertices_rejected_by_singleton\":"<<(eligible.empty()?"true":"false")<<",\"critical_middle_maxmatching_histogram\":";arr(o,matchingHist);o<<",\"critical_pairs_per_central_edge_total\":"<<criticalTotal<<",\"matching13_forbidden_cut_edges\":"<<perfect<<",\"first_matching13_edge\":";arr(o,firstPerfect);o<<",\"first_nonmatching13_edge_and_cardinality\":";arr(o,firstNonperfect);o<<",\"source_distance_BFS\":0,\"modified_graphs\":0,\"solver_calls\":0,\"A2_row_sum\":196,\"A3_row_sum\":2744,\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"complete eligible="<<eligible.size()<<" singletonpairs="<<singletonpairs<<" matching13="<<perfect<<"/7987 cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
