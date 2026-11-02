#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
constexpr int N=172,D=7,M=602;
using Bits=array<uint64_t,3>;
using Edge=array<int,2>;
array<array<int,D>,N> adj;
array<Bits,N> near1,near2;
vector<Edge> edges;
string out;
clock_t began;
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}
struct Counts {uint64_t raw=0,invalid=0,legal=0,cutoff=0,complete_scores=0;};
void countout(ostream&o,const Counts&c){o<<"{\"raw_switch_slots\":"<<c.raw<<",\"invalid_switch_slots\":"<<c.invalid<<",\"legal_switch_candidates\":"<<c.legal<<",\"safe_score_cutoffs\":"<<c.cutoff<<",\"complete_radius3_scores\":"<<c.complete_scores<<'}';}
bool linked(int a,int b){return (near1[a][b/64]>>(b%64))&1;}
void replace_neighbor(int a,int old,int now){
 auto it=find(adj[a].begin(),adj[a].end(),old);assert(it!=adj[a].end());*it=now;
 near1[a][old/64]&=~(1ULL<<(old%64));near1[a][now/64]|=1ULL<<(now%64);
}
void change(const Edge&a,const Edge&b,const Edge&c,const Edge&d){
 // a=(u,v), b=(w,x), c=(u,w), d=(v,x), with arbitrary order in b.
 assert(c[0]==a[0]&&c[1]==b[0]&&d[0]==a[1]&&d[1]==b[1]);
 replace_neighbor(a[0],a[1],b[0]);replace_neighbor(a[1],a[0],b[1]);
 replace_neighbor(b[0],b[1],a[0]);replace_neighbor(b[1],b[0],a[1]);
}
int score(int strict_bound, bool&cutoff, array<int,N>*misses=nullptr){
 for(int v=0;v<N;v++){
  near2[v]=near1[v];near2[v][v/64]|=1ULL<<(v%64);
  for(int u:adj[v])for(int k=0;k<3;k++)near2[v][k]|=near1[u][k];
 }
 int ordered=0;cutoff=false;
 for(int v=0;v<N;v++){
  Bits ball=near2[v];for(int u:adj[v])for(int k=0;k<3;k++)ball[k]|=near2[u][k];
  int missing=N;for(auto w:ball)missing-=__builtin_popcountll(w);
  if(misses)(*misses)[v]=missing;ordered+=missing;
  if(ordered>=2*strict_bound){cutoff=true;return strict_bound;}
 }
 assert(ordered%2==0);return ordered/2;
}
int bfs_score(){
 int ordered=0;
 for(int v=0;v<N;v++){
  array<int,N>d;d.fill(-1);array<int,N>q;int head=0,tail=1;q[0]=v;d[v]=0;
  while(head<tail){int u=q[head++];for(int w:adj[u])if(d[w]<0){d[w]=d[u]+1;q[tail++]=w;}}
  for(int x:d)ordered+=x<0||x>3;
 }
 assert(ordered%2==0);return ordered/2;
}
void save(int bad,int accepted,const Counts&counts){
 ofstream f(out+"/best.edges");f<<N<<' '<<M<<'\n';int count=0;
 for(int u=0;u<N;u++)for(int v:adj[u])if(u<v){f<<u<<' '<<v<<'\n';count++;}assert(count==M);
 ofstream j(out+"/best.json");j<<"{\"n\":172,\"m\":602,\"degree\":7,\"bad_pairs_gt3_or_unreachable\":"<<bad<<",\"committed_descent_switches_at_save\":"<<accepted<<",\"source\":\"../best.edges\",\"symmetry_assumed_for_score\":false,\"all_roots_used_in_radius3_score\":172,\"counts_at_save\":";countout(j,counts);j<<"}\n";
}
int main(int argc,char**argv){
 assert(argc==4);out=argv[1];double budget=stod(argv[3]);began=clock();
 ifstream f(argv[2]);int n,m;f>>n>>m;assert(n==N&&m==M);array<int,N>degrees{};
 for(int i=0;i<M;i++){int u,v;f>>u>>v;assert(0<=u&&u<v&&v<N&&!linked(u,v));edges.push_back({u,v});assert(degrees[u]<D&&degrees[v]<D);adj[u][degrees[u]++]=v;adj[v][degrees[v]++]=u;near1[u][v/64]|=1ULL<<(v%64);near1[v][u/64]|=1ULL<<(u%64);}
 assert(f);for(int d:degrees)assert(d==D);
 bool cut=false;array<int,N>initial_misses;int current=score(N*N,cut,&initial_misses);assert(!cut&&current==258);int saved_best=current;
 {ofstream d(out+"/seed_deficits.json");d<<"{\"bad_pairs\":258,\"all172_radius3_deficits\":[";for(int i=0;i<N;i++){if(i)d<<',';d<<initial_misses[i];}d<<"],\"source_all_root_final_verification_reused\":true,\"new_seed_BFS\":0}\n";}
 Counts all;int completed=0,accepted=0,round=0;bool timed=false,found=false,calibrated=false;int cursor_i=0,cursor_j=1,cursor_type=0;
 ofstream events(out+"/accepted_switches.jsonl");save(current,accepted,all);
 for(round=0;round<30;round++){
  int best=current,wi=-1,wj=-1,wt=-1;Counts local;
  for(int i=0;i<M;i++)for(int j=i+1;j<M;j++)for(int type=0;type<2;type++){
   cursor_i=i;cursor_j=j;cursor_type=type;
   if((all.raw&2047)==0&&cpu()>=budget){timed=true;goto finished;}
   all.raw++;local.raw++;Edge a=edges[i],b=edges[j];if(type)swap(b[0],b[1]);Edge c{a[0],b[0]},d{a[1],b[1]};
   bool distinct=a[0]!=b[0]&&a[0]!=b[1]&&a[1]!=b[0]&&a[1]!=b[1];
   if(!distinct||linked(c[0],c[1])||linked(d[0],d[1])){all.invalid++;local.invalid++;continue;}
   all.legal++;local.legal++;change(a,b,c,d);
   int s=score(calibrated?best:N*N,cut);
   if(!calibrated){assert(!cut);int independent=bfs_score();assert(s==independent);calibrated=true;ofstream q(out+"/candidate_calibration.json");q<<"{\"formal_candidate_index\":1,\"bitset_score\":"<<s<<",\"ordinary_all172_BFS_score\":"<<independent<<",\"matches\":true,\"additional_BFS_roots\":172}\n";}
   if(cut){all.cutoff++;local.cutoff++;}else{all.complete_scores++;local.complete_scores++;}
   if(!cut&&s<saved_best){saved_best=s;save(s,accepted,all);}
   change(c,d,a,b);
   if(s<best){best=s;wi=i;wj=j;wt=type;}
   if(best==0){found=true;goto commit;}
   if(all.legal==10000||all.legal%100000==0){ofstream p(out+"/progress.json");p<<"{\"round\":"<<round<<",\"current_bad_pairs\":"<<current<<",\"best_staged_bad_pairs\":"<<best<<",\"CPU_seconds\":"<<cpu()<<",\"counts\":";countout(p,all);p<<"}\n";cout<<"PROGRESS legal="<<all.legal<<" current="<<current<<" staged="<<best<<" CPU="<<cpu()<<endl;}
  }
  assert(local.raw==uint64_t(M)*(M-1));completed++;
  cout<<"ROUND_COMPLETE round="<<round<<" old="<<current<<" best="<<best<<" legal="<<local.legal<<" CPU="<<cpu()<<endl;
  if(wi<0)break;
 commit:
  Edge a=edges[wi],b=edges[wj];if(wt)swap(b[0],b[1]);Edge c{a[0],b[0]},d{a[1],b[1]};change(a,b,c,d);
  edges[wi]=c;edges[wj]=d;for(int k:{wi,wj})if(edges[k][0]>edges[k][1])swap(edges[k][0],edges[k][1]);
  events<<"{\"round\":"<<round<<",\"removed\":[["<<a[0]<<','<<a[1]<<"],["<<b[0]<<','<<b[1]<<"]],\"added\":[["<<c[0]<<','<<c[1]<<"],["<<d[0]<<','<<d[1]<<"]],\"old_bad\":"<<current<<",\"new_bad\":"<<best<<"}\n";events.flush();
  current=best;accepted++;save(current,accepted,all);if(found)break;
 }
 finished:
 string status=found?"FOUND_D3":timed?"CPU_LIMIT_PREFIX_SAVED":round==30?"THIRTY_ROUND_LIMIT":"COMPLETE_STRICT_TWO_EDGE_SWITCH_LOCAL_MINIMUM";
 ofstream t(out+"/terminal.json");t<<"{\"status\":\""<<status<<"\",\"running\":false,\"complete_rounds\":"<<completed<<",\"accepted_switches\":"<<accepted<<",\"best_bad_pairs\":"<<saved_best<<",\"current_descent_bad_pairs\":"<<current<<",\"best_selected_from_partial_round\":"<<(timed&&saved_best<current?"true":"false")<<",\"counts\":";countout(t,all);t<<",\"last_cursor\":{\"round\":"<<round<<",\"edge_i\":"<<cursor_i<<",\"edge_j\":"<<cursor_j<<",\"orientation\":"<<cursor_type<<"},\"CPU_seconds\":"<<cpu()<<",\"formal_candidate_all_root_BFS_calibrations\":1,\"unrestricted_graph_family_exhausted\":false}\n";
 cout<<status<<" accepted="<<accepted<<" bad="<<current<<" CPU="<<cpu()<<endl;
}
