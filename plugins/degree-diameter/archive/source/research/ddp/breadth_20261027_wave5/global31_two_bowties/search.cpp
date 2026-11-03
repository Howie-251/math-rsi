#include <bits/stdc++.h>
using namespace std;
constexpr int N=31, P=29;
const uint64_t seeds[3]={202610275101ULL,202610275102ULL,202610275103ULL};
const int lengths[6]={4,5,5,5,5,5};
struct Graph { array<array<int,4>,N> nb{}; bool a[N][N]{}; };
struct Eval { int raw=0,bad=0; int count[N][N]{}; int score() const{return raw*64+bad;} };
vector<array<int,3>> triangles;
Graph base;
int basedeg[N]{};
unsigned char feasible[512][512];
vector<int> masks;
clock_t started;
string outdir;
double cpu(){return double(clock()-started)/CLOCKS_PER_SEC;}
void internal_edge(int u,int v){
 assert(u!=v&&!base.a[u][v]);base.a[u][v]=base.a[v][u]=true;
 base.nb[u][basedeg[u]++]=v;base.nb[v][basedeg[v]++]=u;
}
void setup(){
 triangles={{{0,1,2}},{{0,3,4}},{{5,6,7}},{{5,8,9}}};
 for(int u=10;u<31;u+=3)triangles.push_back({u,u+1,u+2});
 for(auto t:triangles)for(int i=0;i<3;i++)internal_edge(t[i],t[(i+1)%3]);
 for(int v=0;v<N;v++)assert(basedeg[v]==((v==0||v==5)?4:2));
 for(int r=0;r<3;r++)for(int s=r+1;s<3;s++)for(int c=0;c<3;c++)for(int d=c+1;d<3;d++){
  masks.push_back((1<<(3*r+c))|(1<<(3*s+d)));
  masks.push_back((1<<(3*r+d))|(1<<(3*s+c)));
 }
 sort(masks.begin(),masks.end());assert(masks.size()==18&&adjacent_find(masks.begin(),masks.end())==masks.end());
 for(int bad=0;bad<512;bad++)for(int good=0;good<512;good++)for(int m:masks)
  if((m&bad)==bad&&!(m&good))feasible[bad][good]++;
}
bool build(const array<int,P>&ports,Graph&g){
 g=base;int deg[N];copy(basedeg,basedeg+N,deg);int start=0;
 for(int len:lengths){for(int j=0;j<len;j++){
  int u=ports[start+j],v=ports[start+(j+1)%len];
  if(u==v||g.a[u][v])return false;
  g.a[u][v]=g.a[v][u]=true;g.nb[u][deg[u]++]=v;g.nb[v][deg[v]++]=u;
 }start+=len;}
 for(int v=0;v<N;v++){assert(deg[v]==4);sort(g.nb[v].begin(),g.nb[v].end());}
 return true;
}
Eval evaluate(const Graph&g){
 Eval e;
 for(int u=0;u<N;u++)for(int v:g.nb[u])for(int w:g.nb[v])if(w!=u)for(int x:g.nb[w])if(x!=v)e.count[u][x]++;
 for(int u=0;u<N;u++)for(int v=0;v<N;v++)if(!g.a[u][v]&&e.count[u][v]<(u==v?2:1))e.raw++;
 for(int u=0;u<N;u++)for(int v:g.nb[u])if(u<v){
  int r[3],s[3],nr=0,ns=0;
  for(int x:g.nb[u])if(x!=v)r[nr++]=x;
  for(int y:g.nb[v])if(y!=u)s[ns++]=y;
  int bad=0,good=0;
  for(int i=0;i<3;i++)for(int j=0;j<3;j++){
   int x=r[i],y=s[j],bit=1<<(3*i+j);
   if(g.a[x][y])bad|=bit;
   else if(e.count[x][y]==1||(x==y&&e.count[x][y]==2))good|=bit;
  }
  if(!feasible[bad][good])e.bad++;
 }
 return e;
}
void write_graph(const string&name,const array<int,P>&ports,const Graph&g,const Eval&e,int start,long long proposal){
 ofstream o(outdir+"/"+name);
 o<<"{\"n\":31,\"m\":62,\"degree\":4,\"architecture\":\"two_disjoint_internal_bowties_plus7_K3\",\"shared_vertices\":[0,5],\"start\":"<<start<<",\"seed\":"<<seeds[start]<<",\"legal_proposal\":"<<proposal<<",\"raw_missing_required_ordered_pairs\":"<<e.raw<<",\"locally_infeasible_central_edges\":"<<e.bad<<",\"lexicographic_score\":"<<e.score()<<",\"ports\":[";
 for(int i=0;i<P;i++){if(i)o<<',';o<<ports[i];}o<<"],\"external_cycle_lengths\":[4,5,5,5,5,5],\"edges\":[";
 bool comma=false;int ne=0;for(int u=0;u<N;u++)for(int v:g.nb[u])if(u<v){if(comma)o<<',';comma=true;o<<'['<<u<<','<<v<<']';ne++;}assert(ne==62);
 o<<"],\"NB3_counts\":[";for(int u=0;u<N;u++){if(u)o<<',';o<<'[';for(int v=0;v<N;v++){if(v)o<<',';o<<e.count[u][v];}o<<']';}
 o<<"],\"required_missing_pairs\":[";comma=false;for(int u=0;u<N;u++)for(int v=0;v<N;v++)if(!g.a[u][v]&&e.count[u][v]<(u==v?2:1)){if(comma)o<<',';comma=true;o<<'['<<u<<','<<v<<']';}
 o<<"],\"actual_triangles\":[";comma=false;for(int u=0;u<N;u++)for(int v=u+1;v<N;v++)if(g.a[u][v])for(int w=v+1;w<N;w++)if(g.a[u][w]&&g.a[v][w]){if(comma)o<<',';comma=true;o<<'['<<u<<','<<v<<','<<w<<']';}
 o<<"]}\n";
}
vector<pair<int,int>> edgekey(const Graph&g){vector<pair<int,int>> k;for(int u=0;u<N;u++)for(int v:g.nb[u])if(u<v)k.push_back({u,v});return k;}
int main(int argc,char**argv){
 assert(argc==2);outdir=argv[1];started=clock();setup();
 set<vector<pair<int,int>>> saved;
 int bestscore=INT_MAX,bestraw=-1,bestbad=-1,completed=0,started_count=0;
 long long totallegal=0,totalillegal=0,totalevals=0;
 bool limited=false,maxpassers=false,calibration=false;
 struct Stat{int id,draws;long long legal=0,illegal=0,accepted=0;int initialraw,initialbad,bestraw,bestbad,finalraw,finalbad;};
 vector<Stat> stats;
 for(int st=0;st<3&&!limited&&!maxpassers;st++){
  mt19937_64 rng(seeds[st]);uniform_real_distribution<double> unit(0,1);uniform_int_distribution<int> position(0,P-1);
  array<int,P> ports;int k=0;for(int v=0;v<N;v++)if(v!=0&&v!=5)ports[k++]=v;
  Graph current;int draws=0;do{shuffle(ports.begin(),ports.end(),rng);draws++;assert(draws<=10000);}while(!build(ports,current));
  Eval cur=evaluate(current);totalevals++;started_count++;
  if(st==0){
   for(int u=0;u<N;u++)for(int v=0;v<N;v++){
    int a3=0;for(int x:current.nb[u])for(int y:current.nb[x])a3+=current.a[y][v];
    assert(a3-7*current.a[u][v]==cur.count[u][v]);
   }
   calibration=true;write_graph("first_calibration.json",ports,current,cur,st,0);
  }
  Stat ss;ss.id=st;ss.draws=draws;ss.initialraw=cur.raw;ss.initialbad=cur.bad;ss.bestraw=cur.raw;ss.bestbad=cur.bad;
  auto observe=[&](const array<int,P>&p,const Graph&g,const Eval&e,long long proposal){
   if(e.score()<bestscore){bestscore=e.score();bestraw=e.raw;bestbad=e.bad;write_graph("best.json",p,g,e,st,proposal);}
   if(e.raw==0&&saved.size()<8&&saved.insert(edgekey(g)).second){
    string name="passer_"+to_string(saved.size())+".json";write_graph(name,p,g,e,st,proposal);
    cout<<"RAW_PASSER "<<outdir<<'/'<<name<<" local_bad_edges="<<e.bad<<" CPU="<<cpu()<<endl;
    if(saved.size()==8)maxpassers=true;
   }
  };
  observe(ports,current,cur,0);
  while(ss.legal<200000&&!maxpassers){
   if((ss.legal&1023)==0&&cpu()>=84){limited=true;break;}
   int i=position(rng),j=position(rng);if(i==j)continue;
   swap(ports[i],ports[j]);Graph candidate;
   if(!build(ports,candidate)){swap(ports[i],ports[j]);ss.illegal++;continue;}
   ss.legal++;Eval next=evaluate(candidate);totalevals++;
   if(next.score()<ss.bestraw*64+ss.bestbad){ss.bestraw=next.raw;ss.bestbad=next.bad;}
   observe(ports,candidate,next,ss.legal);
   double fraction=double(ss.legal-1)/199999.0;
   double temperature=256.0*pow(4.0/256.0,fraction);
   int delta=next.score()-cur.score();
   if(delta<=0||unit(rng)<exp(-double(delta)/temperature)){current=candidate;cur=next;ss.accepted++;}
   else swap(ports[i],ports[j]);
  }
  ss.finalraw=cur.raw;ss.finalbad=cur.bad;stats.push_back(ss);totallegal+=ss.legal;totalillegal+=ss.illegal;
  if(ss.legal==200000)completed++;
  cout<<"START_TERMINAL "<<st<<" legal="<<ss.legal<<" best_raw="<<ss.bestraw<<" best_local_bad="<<ss.bestbad<<" CPU="<<cpu()<<endl;
 }
 ofstream o(outdir+"/terminal.json");
 o<<"{\"status\":\""<<(maxpassers?"MAX8_RAW_PASSERS_SAVED":limited?"CPU_LIMIT_PARTIAL_PROFILE":"THREE_FIXED_GLOBAL_STARTS_COMPLETE")<<"\",\"n\":31,\"m\":62,\"degree\":4,\"internal_triangles\":11,\"external_vertices\":29,\"starts_planned\":3,\"starts_started\":"<<started_count<<",\"starts_completed\":"<<completed<<",\"legal_proposals_per_start_limit\":200000,\"legal_proposals\":"<<totallegal<<",\"illegal_swap_proposals\":"<<totalillegal<<",\"scores\":"<<totalevals<<",\"raw_passers_saved\":"<<saved.size()<<",\"best_raw_missing_ordered_pairs\":"<<bestraw<<",\"best_locally_infeasible_edges\":"<<bestbad<<",\"first_candidate_N3_polynomial_calibration\":"<<(calibration?"true":"false")<<",\"CPU_seconds\":"<<cpu()<<",\"CPU_internal_limit_seconds\":84,\"search_process_CPU_hard_limit_seconds\":87,\"total_budget_CPU_seconds\":90,\"workers\":1,\"BFS_performed\":false,\"pattern_CSP_solved\":false,\"large_lift_generated\":false,\"new_lower_bounds\":0,\"profiles\":[";
 for(int i=0;i<(int)stats.size();i++){auto s=stats[i];if(i)o<<',';o<<"{\"start\":"<<s.id<<",\"seed\":"<<seeds[s.id]<<",\"initial_legal_rejection_draws\":"<<s.draws<<",\"initial_raw_missing\":"<<s.initialraw<<",\"initial_bad_edges\":"<<s.initialbad<<",\"legal_proposals\":"<<s.legal<<",\"illegal_proposals\":"<<s.illegal<<",\"accepted\":"<<s.accepted<<",\"best_raw_missing\":"<<s.bestraw<<",\"best_bad_edges\":"<<s.bestbad<<",\"final_raw_missing\":"<<s.finalraw<<",\"final_bad_edges\":"<<s.finalbad<<'}';}
 o<<"]}\n";
}
