#include <bits/stdc++.h>
using namespace std;
constexpr int N=1152,W=18,D=8,M=144;
const int inverse_label[4]={3,2,1,0};
using Graph=array<array<int,D>,N>;
using Matrix=array<array<uint64_t,W>,N>;
struct Param{array<int,4>col;int b,c;};
struct Edge{int u,v,label;};
using Params=array<Param,M>;
array<Edge,M> edges;
int action(const array<int,4>&a,int x){int y=0;for(int k=0;k<4;k++)if((x>>k)&1)y^=a[k];return y;}
bool maps(const Param&p,array<int,16>&t,array<int,16>&inv){
 unsigned seen=0;
 for(int x=0;x<16;x++){int y=action(p.col,x);t[x]=y;inv[y]=x;seen|=1U<<y;}
 return seen==65535;
}
void update(Graph&g,int h,const Param&p){
 assert(p.b>0&&p.b<16&&p.c>=0&&p.c<16);
 auto[u,v,l]=edges[h];array<int,16>t{},iv{};assert(maps(p,t,iv));int ib=iv[p.b];
 for(int x=0;x<16;x++){int y=t[x]^p.c;g[16*u+x][2*l]=16*v+y;g[16*u+x][2*l+1]=16*v+(y^p.b);}
 int k=inverse_label[l];
 for(int y=0;y<16;y++){int x=iv[y^p.c];g[16*v+y][2*k]=16*u+x;g[16*v+y][2*k+1]=16*u+(x^ib);}
}
int score(const Graph&g,Matrix*out=nullptr){
 Matrix r2{};
 for(int u=0;u<N;u++){
  r2[u][u>>6]|=1ULL<<(u&63);
  for(int v:g[u]){r2[u][v>>6]|=1ULL<<(v&63);for(int x:g[v])r2[u][x>>6]|=1ULL<<(x&63);}
 }
 int missing=0;
 for(int u=0;u<N;u++){
  array<uint64_t,W>row{};
  for(int k=0;k<W;k++){
   uint64_t bits=r2[u][k];
   while(bits){int v=64*k+__builtin_ctzll(bits);bits&=bits-1;for(int j=0;j<W;j++)row[j]|=r2[v][j];}
  }
  int count=0;for(uint64_t z:row)count+=__builtin_popcountll(z);missing+=N-count;
  if(out)(*out)[u]=row;
 }
 assert(missing%2==0);return missing/2;
}
void rawwalk(const Graph&g,int root,int u,int depth,Matrix&seen){
 seen[root][u>>6]|=1ULL<<(u&63);if(depth==4)return;
 for(int v:g[u])rawwalk(g,root,v,depth+1,seen);
}
Param random_param(mt19937_64&rng){
 Param p;array<int,16>t{},iv{};
 do{for(int&x:p.col)x=uniform_int_distribution<int>(0,15)(rng);}while(!maps(p,t,iv));
 p.b=uniform_int_distribution<int>(1,15)(rng);p.c=uniform_int_distribution<int>(0,15)(rng);return p;
}
struct Stat{uint64_t seed;int initial=0,best=0,final=0,proposals=0,accepted=0;array<int,3>moves{};};
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1];double limit=stod(argv[2]);clock_t started=clock();auto cpu=[&](){return double(clock()-started)/CLOCKS_PER_SEC;};
 ifstream input(dir+"/input.txt");int cn,ce;input>>cn>>ce;assert(cn==72&&ce==144);Params initial;
 set<pair<int,int>>controller_edges;int slots[72][4]{};
 for(int h=0;h<M;h++){
  auto&e=edges[h];auto&p=initial[h];input>>e.u>>e.v>>e.label;
  for(int&x:p.col)input>>x;input>>p.b>>p.c;
  assert(e.u!=e.v&&(e.label==0||e.label==1));assert(controller_edges.insert(minmax(e.u,e.v)).second);
  slots[e.u][e.label]++;slots[e.v][inverse_label[e.label]]++;
 }
 for(auto&row:slots)for(int x:row)assert(x==1);
 const uint64_t seeds[2]={20261027115201ULL,20261027115202ULL};
 Graph bestg{};Params bestps;int best=INT_MAX,total=0,completed=0;bool limited=false,hit=false,calibrated=false;vector<Stat>stats;
 for(int st=0;st<2&&!limited&&!hit;st++){
  mt19937_64 rng(seeds[st]);uniform_real_distribution<double>unit(0,1);Params ps=initial;
  if(st)for(Param&p:ps)p=random_param(rng);
  Graph g{};for(int h=0;h<M;h++)update(g,h,ps[h]);int current=score(g);
  Stat ss;ss.seed=seeds[st];ss.initial=ss.best=current;
  if(current<best){best=current;bestg=g;bestps=ps;}if(!current)hit=true;
  cout<<"INITIAL start="<<st<<" seed="<<ss.seed<<" bad="<<current<<" CPU="<<cpu()<<endl;
  while(ss.proposals<1000&&!hit){
   if(cpu()>=limit){limited=true;break;}
   int h=uniform_int_distribution<int>(0,M-1)(rng),mode=uniform_int_distribution<int>(0,2)(rng);Param old=ps[h],nextp=old;
   if(mode==0){int b=uniform_int_distribution<int>(1,14)(rng);if(b>=old.b)b++;nextp.b=b;}
   else if(mode==1)nextp.c^=1<<uniform_int_distribution<int>(0,3)(rng);
   else{
    int i=uniform_int_distribution<int>(0,3)(rng),j=uniform_int_distribution<int>(0,2)(rng);if(j>=i)j++;
    for(int&col:nextp.col)if((col>>j)&1)col^=1<<i;
   }
   ps[h]=nextp;update(g,h,nextp);ss.proposals++;ss.moves[mode]++;total++;
   Matrix formal;int next=score(g,calibrated?nullptr:&formal);
   if(!calibrated){
    Matrix raw{};for(int u=0;u<N;u++)rawwalk(g,u,u,0,raw);assert(raw==formal);
    ofstream c(dir+"/first_proposal_calibration.json");
    c<<"{\"status\":\"MATCH\",\"formal_proposal\":1,\"all1152_R4_rows_match\":true,\"walks_per_root\":4681,\"raw_walks_enumerated\":5392512,\"bad_unordered_pairs\":"<<next<<",\"method\":\"Independent complete recursion of all length0..4 walks; compare all1152x1152 bits to Boolean(I+A+A^2)^2. Formal score reused.\",\"BFS_performed\":false}\n";
    calibrated=true;
   }
   ss.best=min(ss.best,next);if(next<best){best=next;bestg=g;bestps=ps;}
   if(!next){current=0;ss.accepted++;hit=true;break;}
   double temp=800.0*pow(5.0/800.0,double(ss.proposals-1)/999.0);
   if(next<=current||unit(rng)<exp(-double(next-current)/temp)){current=next;ss.accepted++;}
   else{ps[h]=old;update(g,h,old);}
  }
  ss.final=current;stats.push_back(ss);if(ss.proposals==1000)completed++;
  cout<<"PROFILE start="<<st<<" proposals="<<ss.proposals<<" best="<<ss.best<<" final="<<ss.final<<" CPU="<<cpu()<<endl;
 }
 set<pair<int,int>>E;
 for(int u=0;u<N;u++){
  set<int>ns(bestg[u].begin(),bestg[u].end());assert(ns.size()==8&&!ns.count(u));
  for(int v:ns){assert(find(bestg[v].begin(),bestg[v].end(),u)!=bestg[v].end());E.insert(minmax(u,v));}
 }
 assert(E.size()==4608);ofstream ef(dir+"/best.edges");ef<<"1152 4608\n";for(auto[u,v]:E)ef<<u<<' '<<v<<'\n';
 ofstream pf(dir+"/best_parameters.json");
 pf<<"{\"field\":2,\"dimension\":4,\"vertex_encoding\":\"16*u+x0+2*x1+4*x2+8*x3\",\"matrix_encoding\":\"column integers, row i is bit i\",\"forward_relation\":\"y=T*x XOR c XOR lambda*b\",\"reverse_relation\":\"x=Tinv*y XOR Tinv*c XOR lambda*Tinv*b\",\"edges\":[";
 Graph rebuilt{};
 for(int h=0;h<M;h++){
  auto[u,v,l]=edges[h];auto&p=bestps[h];array<int,16>t{},iv{};assert(maps(p,t,iv));
  update(rebuilt,h,p);if(h)pf<<',';
  pf<<"{\"edge_id\":"<<h<<",\"u\":"<<u<<",\"v\":"<<v<<",\"forward_source_label\":"<<l<<",\"T_columns\":[";
  for(int k=0;k<4;k++){if(k)pf<<',';pf<<p.col[k];}pf<<"],\"b\":"<<p.b<<",\"c\":"<<p.c<<",\"Tinv_columns\":[";
  for(int k=0;k<4;k++){if(k)pf<<',';pf<<iv[1<<k];}pf<<"],\"reverse_b\":"<<iv[p.b]<<",\"reverse_c\":"<<iv[p.c]<<'}';
 }pf<<"]}\n";assert(rebuilt==bestg);
 Matrix finalreach;assert(score(bestg,&finalreach)==best);array<int,N>deficits{};int same=0,cross=0;
 for(int u=0;u<N;u++)for(int v=u+1;v<N;v++)if(!(finalreach[u][v>>6]>>(v&63)&1)){deficits[u]++;deficits[v]++;if(u/16==v/16)same++;else cross++;}
 ofstream bf(dir+"/best_score.json");bf<<"{\"bad_unordered_pairs_gt4_or_unreachable\":"<<best<<",\"same_fiber_bad_pairs\":"<<same<<",\"cross_fiber_bad_pairs\":"<<cross<<",\"root_radius4_deficits\":[";
 for(int u=0;u<N;u++){if(u)bf<<',';bf<<deficits[u];}bf<<"]}\n";
 ofstream f(dir+"/search_result.json");
 f<<"{\"status\":\""<<(hit?"HIT_ALL1152_PAIRS_WITHIN4":limited?"CPU_LIMIT_PARTIAL_PROFILE":"TWO_FIXED_EDGE_LOCAL_PROFILES_FAILED")<<"\",\"n\":1152,\"m\":4608,\"degree\":8,\"target_D\":4,\"savedL\":1100,\"starts_planned\":2,\"starts_started\":"<<stats.size()<<",\"starts_completed\":"<<completed<<",\"proposals_per_start_limit\":1000,\"legal_proposals_actual\":"<<total<<",\"best_bad_unordered_pairs_gt4_or_unreachable\":"<<best<<",\"first_formal_proposal_calibrated\":"<<(calibrated?"true":"false")<<",\"simple8regular_production_check\":true,\"parameter_graph_roundtrip_check\":true,\"native_CPU_seconds\":"<<cpu()<<",\"native_CPU_soft_seconds\":"<<limit<<",\"BFS_performed\":false,\"graph_connected_not_assumed\":true,\"profiles\":[";
 for(int i=0;i<int(stats.size());i++){auto s=stats[i];if(i)f<<',';f<<"{\"seed\":"<<s.seed<<",\"initial_bad\":"<<s.initial<<",\"best_bad\":"<<s.best<<",\"final_bad\":"<<s.final<<",\"legal_proposals\":"<<s.proposals<<",\"accepted\":"<<s.accepted<<",\"move_counts_b_c_T\":["<<s.moves[0]<<','<<s.moves[1]<<','<<s.moves[2]<<"]}";}f<<"]}\n";
 if(hit)cout<<"HIT_SAVED best.edges best_parameters.json"<<endl;
}
