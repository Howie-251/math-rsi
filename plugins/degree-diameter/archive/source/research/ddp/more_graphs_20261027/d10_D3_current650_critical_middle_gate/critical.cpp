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
constexpr int N=650,D=10;
static uint16_t A2[N][N],A3[N][N];
static bool A[N][N],isP[N];
static array<int,D> adj[N];
template<class T> void arr(ostream& o,const T& x){o<<'[';bool f=true;for(auto y:x){if(!f)o<<',';f=false;o<<y;}o<<']';}
int main(int argc,char**argv){
 assert(argc==4); rlimit limit{10,10}; assert(setrlimit(RLIMIT_CPU,&limit)==0);
 const clock_t started=clock();
 ifstream in(argv[1]);assert(in);int x;
 for(int u=0;u<N;u++)for(int j=0;j<D;j++){assert(bool(in>>x));assert(x>=0&&x<N&&x!=u&&!A[u][x]);A[u][x]=true;adj[u][j]=x;}
 assert(!(in>>x)); for(int u=0;u<N;u++)for(int v:adj[u])assert(A[v][u]);
 ifstream part(argv[2]);int np=0;while(part>>x){assert(x>=0&&x<N&&!isP[x]);isP[x]=true;np++;}assert(np==130);
 for(int u=0;u<N;u++)for(int v:adj[u])for(int w:adj[v])A2[u][w]++;
 for(int u=0;u<N;u++)for(int v=0;v<N;v++)if(A2[u][v])for(int w:adj[v])A3[u][w]+=A2[u][v];
 for(int u=0;u<N;u++){int s2=0,s3=0;for(int v=0;v<N;v++){s2+=A2[u][v];s3+=A3[u][v];assert(A2[u][v]==A2[v][u]&&A3[u][v]==A3[v][u]);}assert(s2==100&&s3==1000);}
 const string prefix=argv[3];
 ofstream b2(prefix+"/A2.u16le.bin",ios::binary),b3(prefix+"/A3.u16le.bin",ios::binary);
 // Explicit little-endian output, independent of host endianness.
 for(int u=0;u<N;u++)for(int v=0;v<N;v++)for(auto pair:{make_pair(&b2,A2[u][v]),make_pair(&b3,A3[u][v])}){pair.first->put(char(pair.second&255));pair.first->put(char(pair.second>>8));}
 b2.close();b3.close();
 ofstream all(prefix+"/EDGE_CRITICAL_MATCHINGS.jsonl");
 int hist[3][10]={},edges[3]={},perfectDistinct=0,criticalTotal=0;
 const char* names[3]={"FF","FP","PP"};
 vector<int> firstNonperfectFF;
 int eid=0;
 for(int u=0;u<N;u++)for(int v=u+1;v<N;v++)if(A[u][v]){
  int ty=isP[u]+isP[v];vector<int>L,R;
  for(int p:adj[u])if(p!=v)L.push_back(p);for(int q:adj[v])if(q!=u)R.push_back(q);
  sort(L.begin(),L.end());sort(R.begin(),R.end());assert(L.size()==9&&R.size()==9);
  array<int,9> masks{};int nc=0;
  for(int i=0;i<9;i++)for(int j=0;j<9;j++){int p=L[i],q=R[j];if(p!=q&&!A[p][q]&&A2[p][q]==0&&A3[p][q]==1){masks[i]|=1<<j;nc++;}}
  array<int,9> match;match.fill(-1);int card=0;
  function<bool(int,int&)> aug=[&](int i,int&seen){for(int j=0;j<9;j++)if((masks[i]>>j&1)&&!(seen>>j&1)){seen|=1<<j;if(match[j]<0||aug(match[j],seen)){match[j]=i;return true;}}return false;};
  for(int i=0;i<9;i++){int seen=0;card+=aug(i,seen);}
  edges[ty]++;hist[ty][card]++;criticalTotal+=nc;
  if(card==9){set<int> vertices(L.begin(),L.end());vertices.insert(R.begin(),R.end());assert(vertices.size()==18&&!vertices.count(u)&&!vertices.count(v));perfectDistinct++;}
  if(ty==0&&card<9&&firstNonperfectFF.empty())firstNonperfectFF={u,v,card};
  all<<"{\"edge_id\":"<<eid++<<",\"edge\":["<<u<<','<<v<<"],\"type\":\""<<names[ty]<<"\",\"L\":";arr(all,L);all<<",\"R\":";arr(all,R);all<<",\"critical_row_masks\":";arr(all,masks);all<<",\"critical_pair_count\":"<<nc<<",\"maximum_matching\":"<<card<<",\"matching_pairs\":[";
  bool first=true;for(int j=0;j<9;j++)if(match[j]>=0){if(!first)all<<',';first=false;all<<'['<<L[match[j]]<<','<<R[j]<<']';}all<<"]}\n";
 }
 assert(eid==3250&&edges[0]==2080&&edges[1]==1040&&edges[2]==130);all.close();
 const double cpu=double(clock()-started)/CLOCKS_PER_SEC;
 ofstream out(prefix+"/NATIVE_RESULT.json");
 out<<"{\"status\":\"COMPLETE\",\"source_n\":650,\"source_m\":3250,\"edges_analyzed\":"<<eid<<",\"critical_pairs_counted_per_central_edge\":"<<criticalTotal<<",\"matching_histograms\":{";
 for(int t=0;t<3;t++){if(t)out<<',';out<<'\"'<<names[t]<<"\":{";for(int k=0;k<10;k++){if(k)out<<',';out<<'\"'<<k<<"\":"<<hist[t][k];}out<<'}';}
 out<<"},\"all_FF_have_matching9\":"<<(hist[0][9]==2080?"true":"false")<<",\"perfect_matchings_checked_for_18_distinct_physical_vertices\":"<<perfectDistinct<<",\"first_nonperfect_FF\":";arr(out,firstNonperfectFF);
 out<<",\"A2_row_sum\":100,\"A3_row_sum\":1000,\"source_distance_BFS\":0,\"modified_graphs\":0,\"solver_calls\":0,\"CPU_seconds\":"<<cpu<<"}\n";
 cout<<"complete edges="<<eid<<" FFperfect="<<hist[0][9]<<"/2080 cpu="<<cpu<<'\n';
}
