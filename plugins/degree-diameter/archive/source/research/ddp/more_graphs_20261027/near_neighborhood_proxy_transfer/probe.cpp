#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
using U=uint64_t;
double now(){return double(clock())/CLOCKS_PER_SEC;}
void ints(ostream&f,const vector<int>&v){f<<'[';for(size_t i=0;i<v.size();i++){if(i)f<<',';f<<v[i];}f<<']';}
int main(int argc,char**argv){
 assert(argc==9);double began=now(),budget=stod(argv[8]);rlimit lim{5,5};setrlimit(RLIMIT_CPU,&lim);
 string source=argv[1],portfile=argv[2],ballfile=argv[3],out=argv[4];int N=stoi(argv[5]),D=stoi(argv[7]);long long M=stoll(argv[6]);int W=(N+63)/64;
 vector<vector<int>>g(N);vector<pair<int,int>>edges;edges.reserve(M);ifstream input(source);string line;bool first=true;
 while(getline(input,line)){auto pos=line.find_first_not_of(" \t\r");if(pos==string::npos||line[pos]=='#')continue;istringstream s(line);int u,v;s>>u>>v;assert(s);
  if(first&&u==N&&v==M){first=false;continue;}first=false;assert(0<=u&&u<N&&0<=v&&v<N&&u!=v);g[u].push_back(v);g[v].push_back(u);edges.emplace_back(u,v);
  if((edges.size()&16383)==0&&now()-began>budget-.2){cerr<<"PREPARATION_BUDGET\n";return 3;}
 }assert((long long)edges.size()==M);
 vector<int>free,index(N,-1);for(int v=0;v<N;v++){assert(g[v].size()<=size_t(D));if(g[v].size()<size_t(D)){index[v]=free.size();free.push_back(v);}}
 vector<int>given;ifstream pf(portfile);for(int p;pf>>p;)given.push_back(p);assert(given==free);int K=free.size();
 vector<U>balls(size_t(K)*W);ifstream bf(ballfile,ios::binary);assert(bf.read((char*)balls.data(),balls.size()*sizeof(U)));assert(bf.peek()==EOF);
 vector<int>proxy(N,-1),best(N,-1),common(N),touched;long long wedges=0,pairs=0;bool proxycomplete=true;int wprocessed=0;
 for(int w:free){
  if(now()-began>budget-.2){proxycomplete=false;break;}wprocessed++;touched.clear();
  for(int x:g[w])for(int u:g[x]){wedges++;if(g[u].size()!=size_t(D))continue;if(!common[u]++)touched.push_back(u);}
  for(int u:touched){int c=common[u];if(D-c<=3&&int(g[w].size())-c<=1){pairs++;
    if(proxy[u]<0||c>best[u]||(c==best[u]&&(g[w].size()<g[proxy[u]].size()||(g[w].size()==g[proxy[u]].size()&&w<proxy[u])))){proxy[u]=w;best[u]=c;}}
   common[u]=0;}
 }
 int mapped=0;{ofstream f(out+"/proxy_map.json");f<<"{\"records\":[";bool sep=false;
  for(int u=0;u<N;u++)if(proxy[u]>=0){mapped++;if(sep)f<<',';sep=true;int w=proxy[u];f<<"{\"full_vertex\":"<<u<<",\"proxy\":"<<w<<",\"common_neighbors\":"<<best[u]<<",\"full_only\":"<<D-best[u]<<",\"proxy_only\":"<<int(g[w].size())-best[u]<<",\"proxy_degree\":"<<g[w].size()<<'}';}f<<"]}\n";}
 set<vector<int>>seen;vector<int>hitpins;int hitv=-1,visited=0,eligible=0,checks=0,duplicates=0;map<int,int>unmappedhist,missinghist;bool protocomplete=proxycomplete;
 vector<U>full(W,~U(0));if(N%64)full.back()=(U(1)<<(N%64))-1;
 if(proxycomplete)for(int v=0;v<N;v++){
  if((v&511)==0&&now()-began>budget-.2){protocomplete=false;break;}visited++;
  vector<int>pins;int missingproxy=0;
  for(int u:g[v]){if(g[u].size()<size_t(D))pins.push_back(u);else if(proxy[u]>=0)pins.push_back(proxy[u]);else missingproxy++;}
  if(missingproxy){unmappedhist[missingproxy]++;continue;}eligible++;sort(pins.begin(),pins.end());pins.erase(unique(pins.begin(),pins.end()),pins.end());assert(pins.size()<=size_t(D));
  if(!seen.insert(pins).second){duplicates++;continue;}checks++;vector<U>cover(W);
  for(int p:pins){assert(index[p]>=0&&g[p].size()<size_t(D));const U*row=&balls[size_t(index[p])*W];for(int w=0;w<W;w++)cover[w]|=row[w];}
  int missing=0;for(int w=0;w<W;w++)missing+=__builtin_popcountll(full[w]&~cover[w]);missinghist[missing]++;
  if(!missing){hitv=v;hitpins=pins;break;}
 }
 if(hitv>=0){
  ofstream f(out+"/hit.edges");f<<N+1<<' '<<M+hitpins.size()<<'\n';for(auto[u,v]:edges)f<<u<<' '<<v<<'\n';for(int p:hitpins)f<<N<<' '<<p<<'\n';f.close();
  vector<int>degrees;for(int p:hitpins)degrees.push_back(g[p].size());
  ofstream h(out+"/hit_parameters.json");h<<"{\"source_n\":"<<N<<",\"source_m\":"<<M<<",\"delta\":"<<D<<",\"source_graph\":"<<quoted(source)<<",\"prototype\":"<<hitv<<",\"original_neighborhood\":";ints(h,g[hitv]);h<<",\"full_neighbor_set\":";ints(h,hitpins);h<<",\"old_pin_degrees\":";ints(h,degrees);
  h<<",\"new_n\":"<<N+1<<",\"new_m\":"<<M+hitpins.size()<<",\"new_root\":"<<N<<",\"new_degree\":"<<hitpins.size()<<",\"actual_maxdegree_legal\":true,\"complete_cached_R4_missing\":0,\"complete_cached_R4_covered\":"<<N<<",\"all_old_edges_retained\":true,\"root_independent_check_pending\":true,\"record_claimed\":false,\"replacements\":[";bool sep=false;
  for(int u:g[hitv])if(g[u].size()==size_t(D)){if(sep)h<<',';sep=true;h<<"{\"full\":"<<u<<",\"proxy\":"<<proxy[u]<<",\"common\":"<<best[u]<<'}';}h<<"]}\n";
 }
 string status=hitv>=0?"FULL_NPLUS1_CACHED_COVER_PENDING_ROOT":!proxycomplete?"PARTIAL_PROXY_BUDGET":!protocomplete?"PARTIAL_PROTOTYPE_BUDGET":"COMPLETE_FIXED_PROXY_RULE_NO_HIT";
 ofstream r(out+"/NATIVE_RESULT.json");r<<"{\"status\":"<<quoted(status)<<",\"source_n\":"<<N<<",\"source_m\":"<<M<<",\"delta\":"<<D<<",\"free_columns\":"<<K<<",\"wedges_visited\":"<<wedges<<",\"free_vertices_processed\":"<<wprocessed<<",\"proxy_search_complete\":"<<(proxycomplete?"true":"false")<<",\"qualifying_full_proxy_pairs\":"<<pairs<<",\"full_vertices_with_fixed_proxy\":"<<mapped<<",\"prototypes_visited\":"<<visited<<",\"prototypes_all_fullpins_mapped\":"<<eligible<<",\"duplicate_projections\":"<<duplicates<<",\"distinct_projection_cached_R4_checks\":"<<checks<<",\"full_hits\":"<<(hitv>=0?1:0)<<",\"hit_prototype\":"<<hitv<<",\"hit_pins\":";ints(r,hitpins);
 r<<",\"unmapped_fullpin_count_histogram\":{";bool sep=false;for(auto[k,v]:unmappedhist){if(sep)r<<',';sep=true;r<<quoted(to_string(k))<<':'<<v;}r<<"},\"projection_missing_target_count_histogram\":{";sep=false;for(auto[k,v]:missinghist){if(sep)r<<',';sep=true;r<<quoted(to_string(k))<<':'<<v;}r<<"},\"CPU_seconds\":"<<now()-began<<",\"worker_CPU_budget_seconds\":"<<budget<<",\"new_BFS\":0,\"new_balls\":0,\"solver_calls\":0,\"greedy_runs\":0}\n";
 cout<<"FINAL "<<status<<" D="<<D<<" proxies="<<mapped<<" completeprototypes="<<eligible<<" distinctcovers="<<checks<<" CPU="<<now()-began<<'\n';
}
