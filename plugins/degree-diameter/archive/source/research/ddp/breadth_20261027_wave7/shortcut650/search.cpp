#include <bits/stdc++.h>
using namespace std;
constexpr int N=650,W=11;
using Graph=array<array<int,6>,N>;using Matrix=array<array<uint64_t,W>,N>;
Graph sourceg;bool oldedge[N][N]{};unsigned char distv[N][N];Matrix targets{};
vector<pair<int,int>>source_edges;
int score(const Graph&g,Matrix*out=nullptr){
 Matrix two{};for(int u=0;u<N;u++){
  two[u][u>>6]|=1ULL<<(u&63);
  for(int v:g[u]){two[u][v>>6]|=1ULL<<(v&63);for(int x:g[v])two[u][x>>6]|=1ULL<<(x&63);}
 }
 int missing=0;for(int u=0;u<N;u++){
  array<uint64_t,W>four{};
  for(int word=0;word<W;word++){uint64_t bits=two[u][word];while(bits){int v=word*64+__builtin_ctzll(bits);bits&=bits-1;for(int j=0;j<W;j++)four[j]|=two[v][j];}}
  for(int j=0;j<W;j++)missing+=__builtin_popcountll(targets[u][j]&~four[j]);if(out)(*out)[u]=four;
 }assert(!(missing&1));return missing/2;
}
void walks4(const Graph&g,int root,int u,int depth,Matrix&seen){seen[root][u>>6]|=1ULL<<(u&63);if(depth==4)return;for(int v:g[u])walks4(g,root,v,depth+1,seen);}
int rowvertex(int row,int x){return row<20?x+25*row:row<25?500+5*x+row-20:625+x;}
int layer(int u){return u<500?0:u<625?1:2;}
void validateF(const vector<pair<int,int>>&f){array<int,N>d{};assert(f.size()==325);for(auto[u,v]:f){assert(u!=v&&!oldedge[u][v]);d[u]++;d[v]++;}for(int x:d)assert(x==1);}
vector<pair<int,int>>initial0(mt19937_64&rng,const string&dir){
 array<int,20>leaves;iota(leaves.begin(),leaves.end(),0);shuffle(leaves.begin(),leaves.end(),rng);
 vector<pair<int,int>>rowpairs={{25,leaves[0]}};for(int b=0;b<5;b++)rowpairs.push_back({20+b,leaves[b+1]});for(int i=6;i<20;i+=2)rowpairs.push_back({leaves[i],leaves[i+1]});
 vector<pair<int,int>>f;ofstream p(dir+"/initial0_row_pairs.json");p<<"{\"row_encoding\":\"leaf row i: x+25i; block row20+b:500+5x+b; head row25:625+x\",\"row_pairs\":[";
 for(int k=0;k<13;k++){
  auto[a,b]=rowpairs[k];vector<int>allowed,far;int bestd=-1;
  for(int delta=0;delta<25;delta++){
   int d=distv[rowvertex(a,0)][rowvertex(b,delta)];bool same=true,valid=true;
   for(int x=0;x<25;x++){int u=rowvertex(a,x),v=rowvertex(b,(x+delta)%25);same&=distv[u][v]==d;valid&=!oldedge[u][v]&&u!=v;}
   assert(same);if(!valid)continue;if(d>bestd){bestd=d;allowed.clear();}if(d==bestd)allowed.push_back(delta);if(d==5)far.push_back(delta);
  }
  vector<int>&options=far.empty()?allowed:far;assert(!options.empty());int delta=options[uniform_int_distribution<int>(0,options.size()-1)(rng)];
  for(int x=0;x<25;x++)f.push_back(minmax(rowvertex(a,x),rowvertex(b,(x+delta)%25)));
  if(k)p<<',';p<<"{\"row_a\":"<<a<<",\"row_b\":"<<b<<",\"delta\":"<<delta<<",\"uniform_old_distance\":"<<int(distv[rowvertex(a,0)][rowvertex(b,delta)])<<",\"oldD5_delta_options\":[";for(int i=0;i<(int)far.size();i++){if(i)p<<',';p<<far[i];}p<<"]}";
 }p<<"]}\n";validateF(f);return f;
}
vector<pair<int,int>>initial1(mt19937_64&rng,const string&dir){
 array<int,N>order;iota(order.begin(),order.end(),0);shuffle(order.begin(),order.end(),rng);bool used[N]{};vector<pair<int,int>>f;
 int candidate_checks=0,greedy_skips=0,repair_scans=0,repairs=0;bool failed=false,fallback=false;
 for(int u:order)if(!used[u]){
  vector<int>options;for(int v:order)if(v!=u&&!used[v]){candidate_checks++;if(distv[u][v]==5)options.push_back(v);}
  if(options.empty()){greedy_skips++;continue;}int v=options[uniform_int_distribution<int>(0,options.size()-1)(rng)];used[u]=used[v]=true;f.push_back(minmax(u,v));
 }
 int greedy_pairs=f.size();vector<int>unmatched;for(int u:order)if(!used[u])unmatched.push_back(u);int unmatched_initial=unmatched.size();
 while(!unmatched.empty()){
  int u=unmatched.back();unmatched.pop_back();bool repaired=false;
  for(int vi=0;vi<(int)unmatched.size()&&!repaired;vi++)for(int ei=0;ei<(int)f.size()&&!repaired;ei++){
   auto[a,b]=f[ei];repair_scans++;
   for(int orientation=0;orientation<2;orientation++){
    if(orientation)swap(a,b);int v=unmatched[vi];
    if(distv[u][a]==5&&distv[v][b]==5){f[ei]=minmax(u,a);f.push_back(minmax(v,b));unmatched.erase(unmatched.begin()+vi);repaired=true;repairs++;break;}
   }
  }
  if(!repaired){failed=true;break;}
 }
 int fallback_repairs=0,fallback_scans=0;
 if(failed){
  fallback=true;f.clear();iota(order.begin(),order.end(),0);shuffle(order.begin(),order.end(),rng);for(int i=0;i<N;i+=2)f.push_back(minmax(order[i],order[i+1]));
  for(int i=0;i<325;i++)if(oldedge[f[i].first][f[i].second]){
   auto[u,v]=f[i];bool fixed=false;for(int j=0;j<325&&!fixed;j++)if(i!=j){auto[a,b]=f[j];fallback_scans++;for(int k=0;k<2;k++){if(k)swap(a,b);if(!oldedge[u][a]&&!oldedge[v][b]){f[i]=minmax(u,a);f[j]=minmax(v,b);fixed=true;fallback_repairs++;break;}}}assert(fixed);
  }
 }
 validateF(f);int farcount=0;for(auto[u,v]:f)farcount+=distv[u][v]==5;
 ofstream o(dir+"/initial1_construction.json");o<<"{\"greedy_pairs\":"<<greedy_pairs<<",\"greedy_unmatched\":"<<unmatched_initial<<",\"greedy_skips\":"<<greedy_skips<<",\"greedy_candidate_checks\":"<<candidate_checks<<",\"augmenting_length3_repairs\":"<<repairs<<",\"repair_edge_scans\":"<<repair_scans<<",\"D5_matching_construction_failed\":"<<(failed?"true":"false")<<",\"fallback_used\":"<<(fallback?"true":"false")<<",\"fallback_single_shuffle\":"<<(fallback?"true":"false")<<",\"fallback_pair_switch_repairs\":"<<fallback_repairs<<",\"fallback_edge_scans\":"<<fallback_scans<<",\"actual_initial_matching_edges\":325,\"initial_F_edges_at_old_distance5\":"<<farcount<<",\"Blossom_used\":false}\n";return f;
}
void saveF(const string&path,const vector<pair<int,int>>&f){ofstream o(path);o<<"650 325\n";for(auto[u,v]:f)o<<u<<' '<<v<<'\n';}
int main(int argc,char**argv){
 assert(argc==5);string dir=argv[1],source=argv[2],distance=argv[3];double limit=stod(argv[4]);clock_t started=clock();auto cpu=[&](){return double(clock()-started)/CLOCKS_PER_SEC;};
 ifstream in(source);int n,m;in>>n>>m;assert(n==650&&m==1625);int degree[N]{};
 for(int e=0;e<m;e++){int u,v;in>>u>>v;assert(u<v&&!oldedge[u][v]);source_edges.push_back({u,v});oldedge[u][v]=oldedge[v][u]=true;sourceg[u][degree[u]++]=v;sourceg[v][degree[v]++]=u;}
 for(int d:degree)assert(d==5);ifstream ds(distance,ios::binary);ds.read(reinterpret_cast<char*>(distv),sizeof(distv));assert(ds.gcount()==sizeof(distv));
 int targetordered=0;for(int u=0;u<N;u++)for(int v=0;v<N;v++){assert(distv[u][v]==distv[v][u]);assert((distv[u][v]==1)==oldedge[u][v]);if(distv[u][v]==5){targets[u][v>>6]|=1ULL<<(v&63);targetordered++;}}assert(targetordered==175600);
 const uint64_t seeds[2]={2026102776501ULL,2026102776502ULL};Graph bestg;vector<pair<int,int>>bestF;int best=INT_MAX,totallegal=0,totalillegal=0,completed=0;bool limited=false,hit=false,calibrated=false;
 struct Stat{uint64_t seed;int initial,final,best,legal=0,illegal=0,accepted=0,far=0;};vector<Stat>stats;
 for(int st=0;st<2&&!limited&&!hit;st++){
  mt19937_64 rng(seeds[st]);uniform_int_distribution<int>pick(0,324);uniform_real_distribution<double>unit(0,1);
  auto f=st==0?initial0(rng,dir):initial1(rng,dir);saveF(dir+"/initial"+to_string(st)+".F.edges",f);Graph g=sourceg;for(auto[u,v]:f){g[u][5]=v;g[v][5]=u;}
  int current=score(g);Stat ss;ss.seed=seeds[st];ss.initial=ss.best=current;for(auto[u,v]:f)ss.far+=distv[u][v]==5;
  if(current<best){best=current;bestg=g;bestF=f;}
  while(ss.legal<5000){
   if((ss.legal&31)==0&&cpu()>=limit){limited=true;break;}
   int i=pick(rng),j=pick(rng);if(i==j){ss.illegal++;continue;}auto[a,b]=f[i];auto[c,d]=f[j];assert(a!=c&&a!=d&&b!=c&&b!=d);if(rng()&1)swap(c,d);
   if(oldedge[a][c]||oldedge[b][d]){ss.illegal++;continue;}
   g[a][5]=c;g[c][5]=a;g[b][5]=d;g[d][5]=b;f[i]=minmax(a,c);f[j]=minmax(b,d);ss.legal++;totallegal++;
   Matrix formal;int next=score(g,calibrated?nullptr:&formal);
   if(!calibrated){Matrix seen{};for(int u=0;u<N;u++)walks4(g,u,u,0,seen);assert(seen==formal);ofstream cal(dir+"/first_proposal_calibration.json");cal<<"{\"status\":\"MATCH\",\"formal_legal_proposal\":1,\"complete_rows\":650,\"walks_per_root\":1555,\"raw_walks_enumerated\":1010750,\"all650x650_reachability_bits_match\":true,\"bad_unordered_pairs_gt4\":"<<next<<",\"method\":\"Independent direct recursion over all length0..4 walks versus Boolean R2 squared; includes paths using two matching edges, no BFS\",\"proposal_reused_in_formal_batch\":true}\n";calibrated=true;}
   ss.best=min(ss.best,next);if(next<best){best=next;bestg=g;bestF=f;}
   if(!next){current=next;ss.accepted++;hit=true;break;}
   double temperature=150.0*pow(2.0/150.0,double(ss.legal-1)/4999.0);
   if(next<=current||unit(rng)<exp(-double(next-current)/temperature)){current=next;ss.accepted++;}
   else{g[a][5]=b;g[b][5]=a;g[c][5]=d;g[d][5]=c;f[i]=minmax(a,b);f[j]=minmax(c,d);}
  }
  ss.final=current;stats.push_back(ss);totalillegal+=ss.illegal;if(ss.legal==5000)completed++;
  cout<<"PROFILE "<<st<<" legal="<<ss.legal<<" best="<<ss.best<<" CPU="<<cpu()<<endl;
 }
 validateF(bestF);saveF(dir+"/best.F.edges",bestF);set<pair<int,int>>all(source_edges.begin(),source_edges.end());for(auto e:bestF)assert(all.insert(e).second);assert(all.size()==1950);
 ofstream ef(dir+"/best.edges");ef<<"650 1950\n";for(auto[u,v]:all)ef<<u<<' '<<v<<'\n';
 Matrix reach;assert(score(bestg,&reach)==best);int categories[3][3]{};ofstream bo(dir+"/best_score.json");bo<<"{\"n\":650,\"m\":1950,\"degree\":6,\"bad_unordered_pairs_gt4\":"<<best<<",\"bad_pairs\":[";bool comma=false;
 for(int u=0;u<N;u++)for(int v=u+1;v<N;v++)if(distv[u][v]==5&&!(reach[u][v>>6]>>(v&63)&1)){categories[layer(u)][layer(v)]++;if(comma)bo<<',';comma=true;bo<<'['<<u<<','<<v<<']';}
 bo<<"],\"bad_by_layers\":{\"LL\":"<<categories[0][0]<<",\"LB\":"<<categories[0][1]<<",\"LH\":"<<categories[0][2]<<",\"BB\":"<<categories[1][1]<<",\"BH\":"<<categories[1][2]<<",\"HH\":"<<categories[2][2]<<"}}\n";
 ofstream t(dir+"/search_result.json");t<<"{\"status\":\""<<(hit?"HIT_650_DEGREE6_DIAMETER_AT_MOST4":limited?"CPU_LIMIT_PARTIAL_PROFILE":"TWO_FIXED_MATCHING_PROFILES_FAILED")<<"\",\"source_n\":650,\"source_m\":1625,\"source_degree\":5,\"source_D\":5,\"old_D5_unordered_target_pairs\":87800,\"new_n\":650,\"new_m\":1950,\"new_degree\":6,\"matching_edges\":325,\"starts_planned\":2,\"starts_started\":"<<stats.size()<<",\"starts_completed\":"<<completed<<",\"legal_proposals_per_start_limit\":5000,\"legal_proposals_actual\":"<<totallegal<<",\"illegal_swap_draws\":"<<totalillegal<<",\"best_bad_unordered_pairs_gt4\":"<<best<<",\"first_formal_proposal_calibration\":"<<(calibrated?"true":"false")<<",\"complete650_graph_generated\":true,\"source_BFS_rerun\":false,\"producer_BFS_performed\":false,\"CPU_seconds\":"<<cpu()<<",\"CPU_internal_limit_seconds\":"<<limit<<",\"profiles\":[";
 for(int i=0;i<(int)stats.size();i++){auto s=stats[i];if(i)t<<',';t<<"{\"seed\":"<<s.seed<<",\"initial_F_edges_at_old_distance5\":"<<s.far<<",\"initial_bad\":"<<s.initial<<",\"best_bad\":"<<s.best<<",\"final_bad\":"<<s.final<<",\"legal_proposals\":"<<s.legal<<",\"illegal_draws\":"<<s.illegal<<",\"accepted\":"<<s.accepted<<'}';}t<<"]}\n";
 if(hit)cout<<"HIT_SAVED best.edges"<<endl;
}
