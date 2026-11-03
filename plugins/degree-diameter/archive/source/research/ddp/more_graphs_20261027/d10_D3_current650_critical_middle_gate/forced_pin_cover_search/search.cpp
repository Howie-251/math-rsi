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
constexpr int N=650,W=11;
struct Edge{int u,v,mm;array<int,9>L,R,mask;};
vector<Edge> edges;vector<int> src[N];int eid[N][N];uint64_t balls[N][W],full[W];
vector<int> anchors;string outdir;clock_t started;bool stop=false,hit=false,timed=false;
long long covers7=0,covers8=0,sets_seen=0,r2pass=0,realizations=0,dupcuts=0,hubpass=0,bfsroots=0;
int ai=0,lmask=0,extra=-1,oldroot=-1;long long localcover=0;
set<array<int,5>> seenCuts;ofstream cases;
template<class T>void arr(ostream&o,const T&v){o<<'[';bool f=true;for(auto x:v){if(!f)o<<',';f=false;o<<x;}o<<']';}
double cpu(){return double(clock()-started)/CLOCKS_PER_SEC;}
bool budget(){if(cpu()>=9.7){stop=timed=true;return false;}return true;}
void checkpoint(){ofstream o(outdir+"/checkpoint.json");o<<"{\"anchor_ordinal\":"<<ai<<",\"anchor_edge_id\":"<<(ai<(int)anchors.size()?anchors[ai]:-1)<<",\"left_mask\":"<<lmask<<",\"extra_pin\":"<<extra<<",\"edge_cover_cursor\":"<<localcover<<",\"old_root_cursor\":"<<oldroot<<",\"CPU_seconds\":"<<cpu()<<"}\n";}
int firstmiss(const vector<vector<int>>&g,int s){
 array<int,N+1>d,q;d.fill(-1);int lo=0,hi=1;q[0]=s;d[s]=0;
 while(lo<hi){int u=q[lo++];if(d[u]==3)continue;for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;q[hi++]=v;}}
 for(int v=0;v<=N;v++)if(d[v]<0)return v;return -1;
}
void actual(const vector<int>&S,const vector<int>&chosen){
 if(stop||!budget())return;array<int,5> key;copy(chosen.begin(),chosen.end(),key.begin());sort(key.begin(),key.end());localcover++;
 if(!seenCuts.insert(key).second){dupcuts++;return;}realizations++;
 vector<vector<int>>g(N+1);for(int u=0;u<N;u++)for(int v:src[u])if(!binary_search(key.begin(),key.end(),eid[u][v]))g[u].push_back(v);
 for(int s:S){g[s].push_back(N);g[N].push_back(s);}int arcs=0;for(int u=0;u<=N;u++){sort(g[u].begin(),g[u].end());assert(g[u].size()<=10&&adjacent_find(g[u].begin(),g[u].end())==g[u].end());arcs+=g[u].size();}
 assert(arcs/2==3250-5+(int)S.size());oldroot=N;bfsroots++;int bad=firstmiss(g,N),badroot=N;
 if(bad<0){hubpass++;for(int u=0;u<N;u++){oldroot=u;if(!budget())return;bfsroots++;bad=firstmiss(g,u);if(bad>=0){badroot=u;break;}}}
 cases<<"{\"cut_edge_ids\":";arr(cases,key);cases<<",\"pins\":";arr(cases,S);cases<<",\"source_n\":650,\"new_n\":651,\"m\":"<<arcs/2<<",\"bad_root\":"<<(bad<0?-1:badroot)<<",\"first_R3_missing_target\":"<<bad<<"}\n";
 if(bad<0){
  hit=stop=true;ofstream gr(outdir+"/graph_d10_D3_n651.edges");gr<<651<<' '<<arcs/2<<'\n';for(int u=0;u<=N;u++)for(int v:g[u])if(u<v)gr<<u<<' '<<v<<'\n';
  ofstream p(outdir+"/HIT.json");p<<"{\"status\":\"PRODUCER_COMPLETE_651_ROOT_D3_HIT\",\"source_n\":650,\"n\":651,\"m\":"<<arcs/2<<",\"max_degree\":10,\"exact_D\":3,\"newlabel\":650,\"pins\":";arr(p,S);p<<",\"cut_edge_ids\":";arr(p,key);p<<",\"cut_edges\":[";bool f=true;for(int id:key){if(!f)p<<',';f=false;p<<'['<<edges[id].u<<','<<edges[id].v<<']';}p<<"],\"complete_modified_root_checks\":651,\"source_distance_BFS\":0,\"ordinary_unordered_bad_pairs\":0}\n";
 }
}
void processS(vector<int>S,int anchor){
 if(stop||!budget())return;sort(S.begin(),S.end());sets_seen++;
 uint64_t cover[W]={};for(int s:S)for(int w=0;w<W;w++)cover[w]|=balls[s][w];for(int w=0;w<W;w++)if(cover[w]!=full[w])return;r2pass++;
 bool member[N]={};for(int s:S)member[s]=true;int n=S.size();bool allowed[10][10]={};
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){int id=eid[S[i]][S[j]];if(id<0)continue;const Edge&e=edges[id];bool ok=true;for(int a=0;a<9&&ok;a++)if(!member[e.L[a]])for(int b=0;b<9;b++)if((e.mask[a]>>b&1)&&!member[e.R[b]]){ok=false;break;}allowed[i][j]=allowed[j][i]=ok;}
 int au=lower_bound(S.begin(),S.end(),edges[anchor].u)-S.begin(),av=lower_bound(S.begin(),S.end(),edges[anchor].v)-S.begin();assert(au<n&&av<n);if(!allowed[au][av])return;
 function<void(int,vector<int>&)> match=[&](int used,vector<int>&cuts){
  if(stop||!budget())return;int i=0;while(i<n&&(used>>i&1))i++;if(i==n){if(find(cuts.begin(),cuts.end(),anchor)!=cuts.end()){assert(cuts.size()==5);actual(S,cuts);}return;}
  for(int j=i+1;j<n&&!stop;j++)if(!(used>>j&1)&&allowed[i][j]){cuts.push_back(eid[S[i]][S[j]]);match(used|(1<<i)|(1<<j),cuts);cuts.pop_back();}
 };
 if(n==10){vector<int>cuts{anchor};match((1<<au)|(1<<av),cuts);}
 else{
  assert(n==9);for(int c=0;c<n&&!stop;c++)for(int a=0;a<n&&!stop;a++)if(a!=c&&allowed[c][a])for(int b=a+1;b<n&&!stop;b++)if(b!=c&&allowed[c][b]){
   vector<int>cuts{eid[S[c]][S[a]],eid[S[c]][S[b]]};int used=(1<<c)|(1<<a)|(1<<b);
   bool contains=find(cuts.begin(),cuts.end(),anchor)!=cuts.end();if(!contains&&((used>>au&1)||(used>>av&1)))continue;match(used,cuts);
  }
 }
}
int main(int argc,char**argv){
 assert(argc==5);rlimit lim{10,10};assert(setrlimit(RLIMIT_CPU,&lim)==0);started=clock();outdir=argv[4];
 fill(&eid[0][0],&eid[0][0]+N*N,-1);ifstream in(argv[1]);int x;for(int u=0;u<N;u++)for(int k=0;k<10;k++){assert(bool(in>>x));src[u].push_back(x);}assert(!(in>>x));
 ifstream ei(argv[2]);int ne;ei>>ne;assert(ne==3250);for(int id=0;id<ne;id++){Edge e;ei>>e.u>>e.v>>e.mm;for(int&v:e.L)ei>>v;for(int&v:e.R)ei>>v;for(int&v:e.mask)ei>>v;assert(ei);eid[e.u][e.v]=eid[e.v][e.u]=id;edges.push_back(e);if(e.mm==7||e.mm==8){int ty;ei>>ty;if(ty==0)anchors.push_back(id);}else{int ty;ei>>ty;}}
 assert(anchors.size()==128);ifstream bin(argv[3],ios::binary);assert(bin);for(int u=0;u<N;u++){balls[u][u/64]|=1ull<<(u%64);for(int v:src[u])balls[u][v/64]|=1ull<<(v%64);for(int v=0;v<N;v++){int lo=bin.get(),hi=bin.get();assert(lo>=0&&hi>=0);if(lo+(hi<<8))balls[u][v/64]|=1ull<<(v%64);}}
 for(int v=0;v<N;v++)full[v/64]|=1ull<<(v%64);cases.open(outdir+"/ACTUAL_CASES.jsonl");
 for(ai=0;ai<(int)anchors.size()&&!stop;ai++){
  set<vector<int>>seenS;const int anchor=anchors[ai];const Edge&e=edges[anchor];checkpoint();
  for(lmask=0;lmask<512&&!stop;lmask++){
   vector<int>C;int rm=0;for(int i=0;i<9;i++)if(lmask>>i&1)C.push_back(e.L[i]);else rm|=e.mask[i];for(int j=0;j<9;j++)if(rm>>j&1)C.push_back(e.R[j]);sort(C.begin(),C.end());C.erase(unique(C.begin(),C.end()),C.end());
   if(C.size()>8)continue;assert(C.size()>=7);if(C.size()==7)covers7++;else covers8++;
   vector<int>S=C;S.push_back(e.u);S.push_back(e.v);sort(S.begin(),S.end());assert(S.size()==C.size()+2);
   extra=-1;if(seenS.insert(S).second)processS(S,anchor);
   if(C.size()==7)for(extra=0;extra<N&&!stop;extra++)if(!binary_search(S.begin(),S.end(),extra)){auto T=S;T.push_back(extra);sort(T.begin(),T.end());if(seenS.insert(T).second)processS(T,anchor);}
  }
 }
 cases.close();checkpoint();ofstream out(outdir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"PRODUCER_FULL_HIT":timed?"UNKNOWN_CPU_LIMIT":"COMPLETE_FIXED_FAMILY_NO_HIT")<<"\",\"hit\":"<<(hit?"true":"false")<<",\"complete\":"<<(!stop?"true":"false")<<",\"anchors_total\":128,\"size7_base_covers\":"<<covers7<<",\"size8_base_covers\":"<<covers8<<",\"anchor_endpoint_sets_after_per_anchor_dedup\":"<<sets_seen<<",\"endpoint_sets_passing_full_R2\":"<<r2pass<<",\"actual_distinct_cutsets\":"<<realizations<<",\"duplicate_cutsets_skipped\":"<<dupcuts<<",\"modified_hub_R3_passes\":"<<hubpass<<",\"modified_R3_root_checks\":"<<bfsroots<<",\"CPU_seconds\":"<<cpu()<<",\"source_BFS\":0,\"A2_or_A3_recomputation\":0,\"ordinary_unordered_bad_pairs\":null}\n";
 cout<<"status="<<(hit?"HIT":timed?"UNKNOWN":"COMPLETE_NO_HIT")<<" S="<<sets_seen<<" R2pass="<<r2pass<<" graphs="<<realizations<<" roots="<<bfsroots<<" cpu="<<cpu()<<'\n';
}
