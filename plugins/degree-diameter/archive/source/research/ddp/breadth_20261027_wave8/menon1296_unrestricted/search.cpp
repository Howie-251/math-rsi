#include <bits/stdc++.h>
using namespace std;
constexpr int N=1296,W=21,DEG=8;
using Graph=array<array<int,DEG>,N>;
using Matrix=array<array<uint64_t,W>,N>;
using Perms=array<array<int,36>,96>;
struct Inc {int p,L,cs,bs;};
vector<Inc> incs;
vector<array<int,6>> blocks;
vector<pair<int,int>> labels;
Graph base;
int degrees[N]{};
int C(int p,int e){return 144+36*p+e;}
int B(int L,int s){return 720+36*L+s;}
void add(int u,int v){base[u][degrees[u]++]=v;base[v][degrees[v]++]=u;}
int score(const Graph&g,Matrix*out=nullptr){
 Matrix r2{};
 for(int u=0;u<N;u++){
  r2[u][u>>6]|=1ULL<<(u&63);
  for(int v:g[u]){r2[u][v>>6]|=1ULL<<(v&63);for(int x:g[v])r2[u][x>>6]|=1ULL<<(x&63);}
 }
 int missing=0;
 for(int u=0;u<N;u++){
  array<uint64_t,W> row{};
  for(int k=0;k<W;k++){
   uint64_t bits=r2[u][k];
   while(bits){int v=64*k+__builtin_ctzll(bits);bits&=bits-1;for(int j=0;j<W;j++)row[j]|=r2[v][j];}
  }
  int count=0;for(uint64_t z:row)count+=__builtin_popcountll(z);
  missing+=N-count;if(out)(*out)[u]=row;
 }
 assert(missing%2==0);return missing/2;
}
void rawwalk(const Graph&g,int root,int v,int depth,Matrix&seen){
 seen[root][v>>6]|=1ULL<<(v&63);if(depth==4)return;
 for(int w:g[v])rawwalk(g,root,w,depth+1,seen);
}
void setup(const string&dir){
 vector<int>D;
 for(int x=0;x<16;x++)if((((x&1)*((x>>1)&1)+((x>>2)&1)*((x>>3)&1))&1)==1)D.push_back(x);
 assert(D.size()==6);
 for(int L=0;L<16;L++){array<int,6>a;for(int j=0;j<6;j++)a[j]=D[j]^L;sort(a.begin(),a.end());blocks.push_back(a);}
 for(int i=0;i<9;i++)for(int j=i+1;j<9;j++)labels.push_back({i,j});
 for(int p=0;p<16;p++)for(int e=0;e<36;e++){auto[i,j]=labels[e];add(9*p+i,C(p,e));add(9*p+j,C(p,e));}
 for(int L=0;L<16;L++)for(int t=0;t<12;t++)for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)add(B(L,3*t+i),B(L,3*t+j));
 for(int p=0;p<16;p++){
  int rank=0;
  for(int L=0;L<16;L++){
   auto it=find(blocks[L].begin(),blocks[L].end(),p);
   if(it!=blocks[L].end())incs.push_back({p,L,2+rank++,2+int(it-blocks[L].begin())});
  }
  assert(rank==6);
 }
 assert(incs.size()==96);
 for(int v=0;v<N;v++)assert(degrees[v]==(v<144?8:2));
 for(int p=0;p<16;p++)for(int q=p+1;q<16;q++){int shared=0;for(auto block:blocks)shared+=find(block.begin(),block.end(),p)!=block.end()&&find(block.begin(),block.end(),q)!=block.end();assert(shared==2);}
 ofstream f(dir+"/structure.json");
 f<<"{\"point_bits\":\"p=x0+2*x1+4*x2+8*x3\",\"D\":[";
 for(int j=0;j<6;j++){if(j)f<<',';f<<D[j];}f<<"],\"blocks\":[";
 for(int L=0;L<16;L++){if(L)f<<',';f<<'[';for(int j=0;j<6;j++){if(j)f<<',';f<<blocks[L][j];}f<<']';}
 f<<"],\"K9_edge_labels\":[";
 for(int e=0;e<36;e++){if(e)f<<',';f<<'['<<labels[e].first<<','<<labels[e].second<<']';}
 f<<"],\"encoding\":{\"A\":\"9*p+i,0<=p<16,0<=i<9\",\"C\":\"144+36*p+e\",\"B\":\"720+36*L+s\",\"B_triangle\":\"floor(s/3); states3t,3t+1,3t+2\",\"CB\":\"C(p,e)--B(L,pi[p,L][e]) for p in block L\"},\"n\":1296,\"m\":5184,\"degree\":8,\"incidences\":96,\"independent_S36_at_every_incidence\":true}\n";
}
void apply_swap(Graph&g,Perms&ps,int h,int e,int f){
 auto[p,L,cs,bs]=incs[h];int a=ps[h][e],b=ps[h][f];
 g[C(p,e)][cs]=B(L,b);g[C(p,f)][cs]=B(L,a);
 g[B(L,a)][bs]=C(p,f);g[B(L,b)][bs]=C(p,e);
 swap(ps[h][e],ps[h][f]);
}
struct Stat {uint64_t seed;int initial=0,best=0,final=0,proposals=0,accepted=0;};
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1];double limit=stod(argv[2]);clock_t started=clock();auto cpu=[&](){return double(clock()-started)/CLOCKS_PER_SEC;};setup(dir);
 const uint64_t seeds[2]={20261027812961ULL,20261027812962ULL};
 Graph bestg;Perms bestps;int best=INT_MAX,total=0,completed=0;bool limited=false,hit=false,calibrated=false;vector<Stat>stats;
 for(int st=0;st<2&&!limited&&!hit;st++){
  mt19937_64 rng(seeds[st]);uniform_real_distribution<double>unit(0,1);Graph g=base;Perms ps;
  for(int h=0;h<96;h++){
   iota(ps[h].begin(),ps[h].end(),0);
   for(int j=35;j>0;j--){uniform_int_distribution<int>pick(0,j);swap(ps[h][j],ps[h][pick(rng)]);}
   auto[p,L,cs,bs]=incs[h];
   for(int e=0;e<36;e++){g[C(p,e)][cs]=B(L,ps[h][e]);g[B(L,ps[h][e])][bs]=C(p,e);}
  }
  int current=score(g);Stat ss;ss.seed=seeds[st];ss.initial=ss.best=current;
  if(current<best){best=current;bestg=g;bestps=ps;}if(!current)hit=true;
  cout<<"INITIAL seed="<<ss.seed<<" bad="<<current<<" CPU="<<cpu()<<endl;
  while(ss.proposals<1000&&!hit){
   if(cpu()>=limit){limited=true;break;}
   int h=uniform_int_distribution<int>(0,95)(rng),e=uniform_int_distribution<int>(0,35)(rng),f=uniform_int_distribution<int>(0,34)(rng);if(f>=e)f++;
   apply_swap(g,ps,h,e,f);ss.proposals++;total++;
   Matrix formal;int next=score(g,calibrated?nullptr:&formal);
   if(!calibrated){
    Matrix raw{};for(int u=0;u<N;u++)rawwalk(g,u,u,0,raw);assert(raw==formal);
    ofstream c(dir+"/first_proposal_calibration.json");
    c<<"{\"status\":\"MATCH\",\"formal_proposal\":1,\"all1296_R4_rows_match\":true,\"walks_per_root\":4681,\"raw_walks_enumerated\":6066576,\"bad_unordered_pairs\":"<<next<<",\"method\":\"Independent recursive enumeration of all walks length0..4 compared bit-for-bit with Boolean(I+A+A^2)^2; first proposal score reused.\",\"BFS_performed\":false}\n";
    calibrated=true;
   }
   ss.best=min(ss.best,next);if(next<best){best=next;bestg=g;bestps=ps;}
   if(!next){current=next;ss.accepted++;hit=true;break;}
   double temp=600.0*pow(5.0/600.0,double(ss.proposals-1)/999.0);
   if(next<=current||unit(rng)<exp(-double(next-current)/temp)){current=next;ss.accepted++;}
   else apply_swap(g,ps,h,e,f);
  }
  ss.final=current;stats.push_back(ss);if(ss.proposals==1000)completed++;
  cout<<"PROFILE seed="<<ss.seed<<" proposals="<<ss.proposals<<" best="<<ss.best<<" final="<<ss.final<<" CPU="<<cpu()<<endl;
 }
 set<pair<int,int>>edges;
 for(int u=0;u<N;u++){
  set<int>ns(bestg[u].begin(),bestg[u].end());assert(ns.size()==8&&!ns.count(u));
  for(int v:ns){assert(find(bestg[v].begin(),bestg[v].end(),u)!=bestg[v].end());edges.insert(minmax(u,v));}
 }
 assert(edges.size()==5184);
 ofstream efile(dir+"/best.edges");efile<<"1296 5184\n";for(auto[u,v]:edges)efile<<u<<' '<<v<<'\n';
 ofstream pf(dir+"/best_pi.json");pf<<"{\"pi_direction\":\"C-label e to B-state s\",\"incidences\":[";
 for(int h=0;h<96;h++){
  auto[p,L,cs,bs]=incs[h];set<int>states(bestps[h].begin(),bestps[h].end());assert(states.size()==36);
  if(h)pf<<',';pf<<"{\"p\":"<<p<<",\"L\":"<<L<<",\"pi\":[";
  for(int e=0;e<36;e++){if(e)pf<<',';pf<<bestps[h][e];assert(bestg[C(p,e)][cs]==B(L,bestps[h][e]));}
  pf<<"]}";
 }pf<<"]}\n";
 Matrix finalreach;assert(score(bestg,&finalreach)==best);int cats[3][3]{};array<int,N>deficits{};
 auto type=[](int u){return u<144?0:u<720?1:2;};
 for(int u=0;u<N;u++)for(int v=u+1;v<N;v++)if(!(finalreach[u][v>>6]>>(v&63)&1)){cats[type(u)][type(v)]++;deficits[u]++;deficits[v]++;}
 ofstream bf(dir+"/best_score.json");bf<<"{\"bad_unordered_pairs_gt4\":"<<best<<",\"bad_pair_categories\":{\"AA\":"<<cats[0][0]<<",\"AC\":"<<cats[0][1]<<",\"AB\":"<<cats[0][2]<<",\"CC\":"<<cats[1][1]<<",\"CB\":"<<cats[1][2]<<",\"BB\":"<<cats[2][2]<<"},\"root_radius4_deficits\":[";
 for(int u=0;u<N;u++){if(u)bf<<',';bf<<deficits[u];}bf<<"]}\n";
 ofstream result(dir+"/search_result.json");
 result<<"{\"status\":\""<<(hit?"HIT_ALL1296_PAIRS_WITHIN4":limited?"CPU_LIMIT_PARTIAL_PROFILE":"TWO_FIXED_S36_PROFILES_FAILED")<<"\",\"n\":1296,\"m\":5184,\"degree\":8,\"starts_planned\":2,\"starts_started\":"<<stats.size()<<",\"starts_completed\":"<<completed<<",\"proposals_per_start_limit\":1000,\"legal_proposals_actual\":"<<total<<",\"best_bad_unordered_pairs_gt4\":"<<best<<",\"first_formal_proposal_calibrated\":"<<(calibrated?"true":"false")<<",\"CPU_seconds\":"<<cpu()<<",\"internal_CPU_limit_seconds\":"<<limit<<",\"BFS_performed\":false,\"score\":\"Exact all1296 R4=(I+A+A^2)^2; count unordered offdiagonal missing pairs\",\"profiles\":[";
 for(int i=0;i<int(stats.size());i++){auto s=stats[i];if(i)result<<',';result<<"{\"seed\":"<<s.seed<<",\"initial_bad\":"<<s.initial<<",\"best_bad\":"<<s.best<<",\"final_bad\":"<<s.final<<",\"legal_proposals\":"<<s.proposals<<",\"accepted\":"<<s.accepted<<'}';}result<<"]}\n";
 if(hit)cout<<"HIT_SAVED best.edges and best_pi.json"<<endl;
}
