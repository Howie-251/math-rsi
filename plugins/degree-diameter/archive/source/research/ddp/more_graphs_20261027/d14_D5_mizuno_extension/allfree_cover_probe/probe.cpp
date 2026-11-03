#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
double now(){return double(clock())/CLOCKS_PER_SEC;}
void ints(ostream&f,const vector<int>&v){f<<'[';for(size_t i=0;i<v.size();i++){if(i)f<<',';f<<v[i];}f<<']';}
struct Attempt{int first;vector<int>pins;int missing;bool complete;};
int main(int argc,char**argv){
 assert(argc==4);double began=now(),limit=stod(argv[3]);string base=argv[1],out=argv[2];
 rlimit hard{(rlim_t)ceil(limit),(rlim_t)ceil(limit+1)};setrlimit(RLIMIT_CPU,&hard);
 const int N=94186,W=(N+63)/64;vector<vector<int>>g(N);vector<pair<int,int>>edges;edges.reserve(657452);
 ifstream input(base+"/source94186.edges");string line;
 while(getline(input,line)){auto pos=line.find_first_not_of(" \t\r");if(pos==string::npos||line[pos]=='#')continue;
  istringstream s(line);int u,v;s>>u>>v;assert(s&&0<=u&&u<N&&0<=v&&v<N&&u!=v);
  g[u].push_back(v);g[v].push_back(u);edges.emplace_back(u,v);}
 assert(edges.size()==657452);vector<int>free,low,index(N,-1);
 for(int v=0;v<N;v++){assert(g[v].size()<=14);if(g[v].size()<14){index[v]=free.size();free.push_back(v);}if(g[v].size()==12)low.push_back(v);}
 const int K=free.size();assert(K==3685&&low.size()==15);vector<U>balls(size_t(K)*W);vector<bool>computed(K);
 ifstream old(base+"/rare15_R4.u64le.bin",ios::binary);
 for(int v:low){assert(old.read((char*)&balls[size_t(index[v])*W],W*8));computed[index[v]]=true;}
 vector<int>d(N),q(N);int generated=0;double ballstart=now();bool partial=false;
 for(int j=0;j<K;j++)if(!computed[j]){
  if(now()-began>limit-.7){partial=true;break;}
  // Same exact depth4 kernel as the accepted h9_d12_eightpin_extensions/cover.cpp.
  fill(d.begin(),d.end(),-1);int h=0,t=0;d[free[j]]=0;q[t++]=free[j];
  while(h<t){int u=q[h++];if(d[u]==4)continue;for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;q[t++]=v;}}
  U*row=&balls[size_t(j)*W];for(int v=0;v<N;v++)if(d[v]>=0)row[v/64]|=U(1)<<(v%64);
  computed[j]=true;generated++;
  if(generated==100){double elapsed=now()-ballstart,projected=now()-began+elapsed*(3670-100)/100.;
   ofstream f(out+"/PROFILE100.json");f<<"{\"new_balls_profiled_once\":100,\"old15_balls_reused\":15,\"CPU_for100new\":"<<elapsed<<",\"projected_complete_ballprep_nativeCPU\":"<<projected<<",\"native_CPU_limit\":"<<limit<<",\"profile_replayed\":false}\n";
   cerr<<"PROFILE100 newCPU="<<elapsed<<" projectedprep="<<projected<<'\n';
   if(projected>limit-1){partial=true;break;}}
 }
 {ofstream f(out+"/allfree_R4.u64le.bin",ios::binary);f.write((char*)balls.data(),balls.size()*8);}
 {ofstream f(out+"/BALLS_META.json");f<<"{\"source_n\":"<<N<<",\"source_m\":"<<edges.size()<<",\"free_vertices\":";ints(f,free);
  f<<",\"words_per_row\":"<<W<<",\"old15_reused\":15,\"new_balls_computed\":"<<generated<<",\"complete\":"<<(!partial?"true":"false")<<",\"computed_vertices\":[";
  bool first=true;for(int j=0;j<K;j++)if(computed[j]){if(!first)f<<',';first=false;f<<free[j];}f<<"]}\n";}
 if(partial){ofstream f(out+"/NATIVE_RESULT.json");f<<"{\"status\":\"PARTIAL_BALL_PREPARATION\",\"new_balls_computed\":"<<generated<<",\"constructs_completed\":0,\"native_CPU_seconds\":"<<now()-began<<"}\n";return 0;}
 vector<unsigned short>support(N);vector<U>all(W);vector<int>sizes(K);vector<U>full(W,~U(0));if(N%64)full.back()=(U(1)<<(N%64))-1;
 for(int j=0;j<K;j++){const U*row=&balls[size_t(j)*W];for(int w=0;w<W;w++){U b=row[w];all[w]|=b;sizes[j]+=__builtin_popcountll(b);
  while(b){int bit=__builtin_ctzll(b),v=64*w+bit;support[v]++;b&=b-1;}}}
 vector<int>unsupported;map<int,int>supporthist;for(int v=0;v<N;v++){supporthist[support[v]]++;if(!support[v])unsupported.push_back(v);}
 {ofstream f(out+"/target_support.u16le.bin",ios::binary);f.write((char*)support.data(),N*2);}
 vector<int>order(N);iota(order.begin(),order.end(),0);sort(order.begin(),order.end(),[&](int a,int b){return pair(support[a],a)<pair(support[b],b);});
 vector<unsigned long long>rarity(K);vector<int>weight(N);if(unsupported.empty())for(int v=0;v<N;v++)weight[v]=1000000/support[v];
 if(unsupported.empty())for(int j=0;j<K;j++){const U*row=&balls[size_t(j)*W];for(int w=0;w<W;w++){U b=row[w];while(b){int bit=__builtin_ctzll(b);rarity[j]+=weight[64*w+bit];b&=b-1;}}}
 int rare=order.front();vector<int>starts;
 if(unsupported.empty())for(int j=0;j<K;j++)if(balls[size_t(j)*W+rare/64]>>(rare%64)&1)starts.push_back(j);
 sort(starts.begin(),starts.end(),[&](int a,int b){if(rarity[a]!=rarity[b])return rarity[a]>rarity[b];if(sizes[a]!=sizes[b])return sizes[a]>sizes[b];return free[a]<free[b];});
 if(starts.size()>64)starts.resize(64);vector<int>firstvertices;for(int j:starts)firstvertices.push_back(free[j]);
 {ofstream f(out+"/FROZEN_FIRST_PINS.json");f<<"{\"target_rarest\":"<<rare<<",\"target_support\":"<<support[rare]<<",\"first_pins\":";ints(f,firstvertices);f<<",\"rule\":\"descending static inverse-support sum, descending ball size, ascending vertex\"}\n";}
 vector<Attempt>attempts;vector<int>bestpins,hitpins;vector<U>bestuncovered;int best=N+1;bool timeout=false;
 for(int first:starts){
  if(now()-began>limit-.6){timeout=true;break;}vector<U>uncovered=full;vector<int>selected;vector<bool>used(K);
  auto take=[&](int j){used[j]=true;selected.push_back(free[j]);const U*row=&balls[size_t(j)*W];for(int w=0;w<W;w++)uncovered[w]&=~row[w];};
  take(first);int missing=0;
  while(true){
   missing=0;for(U b:uncovered)missing+=__builtin_popcountll(b);
   if(!missing||selected.size()==14)break;
   if(now()-began>limit-.6){timeout=true;break;}
   int pivot=-1;for(int v:order)if(uncovered[v/64]>>(v%64)&1){pivot=v;break;}assert(pivot>=0);
   int chosen=-1,gainbest=-1;
   for(int j=0;j<K;j++)if(!used[j]&&(balls[size_t(j)*W+pivot/64]>>(pivot%64)&1)){
    const U*row=&balls[size_t(j)*W];int gain=0;for(int w=0;w<W;w++)gain+=__builtin_popcountll(row[w]&uncovered[w]);
    if(gain>gainbest||(gain==gainbest&&(chosen<0||rarity[j]>rarity[chosen]||(rarity[j]==rarity[chosen]&&free[j]<free[chosen])))){chosen=j;gainbest=gain;}
   }assert(chosen>=0);take(chosen);
  }
  bool complete=!missing||selected.size()==14;
  attempts.push_back({free[first],selected,missing,complete});
  if(complete&&missing<best){best=missing;bestpins=selected;bestuncovered=uncovered;}
  if(complete&&!missing){hitpins=selected;break;}
  if(timeout)break;
 }
 vector<int>bestmissing;if(!bestuncovered.empty())for(int v=0;v<N;v++)if(bestuncovered[v/64]>>(v%64)&1)bestmissing.push_back(v);
 {ofstream f(out+"/best_construct.json");f<<"{\"pins\":";ints(f,bestpins);f<<",\"missing_old_vertices\":";ints(f,bestmissing);f<<",\"missing_count\":"<<(best==N+1?-1:best)<<"}\n";}
 int newecc=-1;if(!hitpins.empty()){
  ofstream f(out+"/graph_d14_D5_n94187.edges");f<<N+1<<' '<<edges.size()+hitpins.size()<<'\n';for(auto[u,v]:edges)f<<u<<' '<<v<<'\n';for(int v:hitpins)f<<N<<' '<<v<<'\n';f.close();
  g.push_back({});for(int v:hitpins){assert(g[v].size()<14);g[N].push_back(v);g[v].push_back(N);}for(auto&row:g)assert(row.size()<=14);
  vector<int>dist(N+1,-1),todo(N+1);int h=0,t=0;dist[N]=0;todo[t++]=N;
  while(h<t){int u=todo[h++];for(int v:g[u])if(dist[v]<0){dist[v]=dist[u]+1;todo[t++]=v;}}
  assert(t==N+1);newecc=*max_element(dist.begin(),dist.end());assert(newecc<=5);
 }
 string status=!hitpins.empty()?"COMPLETE94187_EXTENSION":!unsupported.empty()?"EXACT_ALLFREE_UNSUPPORTED_TARGET":timeout?"PARTIAL_CONSTRUCTIVE_PROBE":"COMPLETE_FIXED64_CONSTRUCTIVE_PROBE_NO_HIT";
 ofstream f(out+"/NATIVE_RESULT.json");f<<"{\"status\":\""<<status<<"\",\"source_n\":"<<N<<",\"source_m\":"<<edges.size()<<",\"free_vertices\":"<<K<<",\"old15_balls_reused\":15,\"new_balls_computed\":"<<generated<<",\"allfree_union_missing_count\":"<<unsupported.size()<<",\"unsupported_targets\":";ints(f,unsupported);
 f<<",\"minimum_target_support\":"<<support[order.front()]<<",\"maximum_target_support\":"<<support[order.back()]<<",\"support_histogram\":{";bool sep=false;for(auto[k,v]:supporthist){if(sep)f<<',';sep=true;f<<'"'<<k<<"\":"<<v;}f<<"},\"first_pins\":";ints(f,firstvertices);
 f<<",\"attempts\":[";int completed=0;for(size_t i=0;i<attempts.size();i++){if(i)f<<',';auto&a=attempts[i];completed+=a.complete;f<<"{\"first\":"<<a.first<<",\"pins\":";ints(f,a.pins);f<<",\"missing_old_vertices\":"<<a.missing<<",\"complete\":"<<(a.complete?"true":"false")<<'}';}
 f<<"],\"constructs_completed\":"<<completed<<",\"starts_planned\":"<<starts.size()<<",\"best_complete_missing_count\":";if(best==N+1)f<<"null";else f<<best;
 f<<",\"hit_pins\":";ints(f,hitpins);f<<",\"actual_new_n\":";if(hitpins.empty())f<<"null";else f<<N+1;
 f<<",\"new_root_eccentricity\":";if(newecc<0)f<<"null";else f<<newecc;
 f<<",\"new_root_BFS\":"<<(!hitpins.empty()?1:0)<<",\"source_allBFS\":0,\"native_CPU_seconds\":"<<now()-began<<",\"native_CPU_limit\":"<<limit<<"}\n";
 cout<<"FINAL "<<status<<" completed="<<completed<<" bestmissing="<<(best==N+1?-1:best)<<" CPU="<<now()-began<<'\n';
}
