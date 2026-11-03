#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
void ints(ostream&f,const vector<int>&v){f<<'[';for(size_t i=0;i<v.size();i++){if(i)f<<',';f<<v[i];}f<<']';}
struct Candidate{int ordinal,p,type0,type1;array<int,4>cut;vector<int>T,S,A;};
struct Check{int root,reached,witness;array<int,5>layers;};
int main(int argc,char**argv){
 assert(argc==5);double began=cpu(),limit=stod(argv[4]);string source=argv[1],input=argv[2],out=argv[3];
 rlimit hard{(rlim_t)ceil(limit),(rlim_t)ceil(limit+1)};setrlimit(RLIMIT_CPU,&hard);
 ifstream sf(source);int n,m;sf>>n>>m;assert(n==3645&&m==20044);
 vector<vector<int>>g(n+1);vector<pair<int,int>>edges;edges.reserve(m);
 for(int i=0;i<m;i++){int u,v;sf>>u>>v;assert(sf);g[u].push_back(v);g[v].push_back(u);edges.push_back({u,v});}
 ifstream f(input);int count;f>>count;assert(0<count&&count<=3280);
 vector<int>free(7);for(int&v:free)f>>v;for(int v=0;v<n;v++)assert(g[v].size()==size_t(find(free.begin(),free.end(),v)!=free.end()?10:11));
 vector<Candidate>items;vector<int>endpoint_index(n,-1),endpoint_roots;
 for(int i=0;i<count;i++){Candidate c;f>>c.ordinal>>c.p>>c.type0>>c.type1;for(int&v:c.cut)f>>v;
  c.T.resize(4);for(int&v:c.T)f>>v;c.S.resize(11);for(int&v:c.S)f>>v;
  int a;f>>a;c.A.resize(a);for(int&v:c.A)f>>v;assert(f&&a<=48);items.push_back(c);
  for(int v:c.T)if(endpoint_index[v]<0){endpoint_index[v]=0;endpoint_roots.push_back(v);}}
 sort(endpoint_roots.begin(),endpoint_roots.end());for(int i=0;i<(int)endpoint_roots.size();i++)endpoint_index[endpoint_roots[i]]=i;
 const int W=(n+63)/64;vector<U>freeball(W);ifstream fb(out+"/free_R3.u64le.bin",ios::binary);assert(fb.read((char*)freeball.data(),W*8));
 vector<U>full(W,~U(0));if(n%64)full.back()=(U(1)<<(n%64))-1;
 assert(accumulate(freeball.begin(),freeball.end(),0,[](int a,U b){return a+__builtin_popcountll(b);})==2902);
 vector<U>balls(size_t(endpoint_roots.size())*W);vector<int>distance(n+1),q(n+1);vector<unsigned>seen(n+1);unsigned stamp=0;
 double prepstart=cpu();int prepared=0;bool prep_limit=false;
 for(int root:endpoint_roots){
  if(cpu()-began>limit-.8){prep_limit=true;break;}stamp++;int h=0,t=0;seen[root]=stamp;distance[root]=0;q[t++]=root;
  while(h<t){int u=q[h++];if(distance[u]==3)continue;for(int v:g[u])if(seen[v]!=stamp){seen[v]=stamp;distance[v]=distance[u]+1;q[t++]=v;}}
  U*row=&balls[size_t(endpoint_index[root])*W];for(int j=0;j<t;j++)row[q[j]/64]|=U(1)<<(q[j]%64);prepared++;
  if(prepared==100){double elapsed=cpu()-prepstart,projected=cpu()-began+elapsed*(endpoint_roots.size()-100)/100.;
   ofstream pf(out+"/PROFILE100.json");pf<<"{\"endpoint_balls_profiled_once\":100,\"total_distinct_endpoint_roots\":"<<endpoint_roots.size()<<",\"CPU100\":"<<elapsed<<",\"projected_prep_nativeCPU\":"<<projected<<",\"free7_union_reused\":true,\"profile_replayed\":false}\n";
   if(projected>limit-1){prep_limit=true;break;}}
 }
 {ofstream bf(out+"/endpoint_R3.u64le.bin",ios::binary);bf.write((char*)balls.data(),balls.size()*8);}
 {ofstream pf(out+"/ENDPOINT_CACHE.json");pf<<"{\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"roots\":";ints(pf,endpoint_roots);pf<<",\"words_per_row\":"<<W<<",\"roots_prepared\":"<<prepared<<",\"complete\":"<<(!prep_limit?"true":"false")<<"}\n";}
 if(prep_limit){ofstream rf(out+"/NATIVE_RESULT.json");rf<<"{\"status\":\"PARTIAL_ENDPOINT_PREPARATION\",\"prepared\":"<<prepared<<",\"candidates_screened\":0,\"candidates_total\":"<<count<<",\"native_CPU_seconds\":"<<cpu()-began<<"}\n";return 0;}
 auto cutedge=[&](int u,int v){auto it=find(g[u].begin(),g[u].end(),v);assert(it!=g[u].end());*it=g[u].back();g[u].pop_back();};
 auto erase_edge=[&](int u,int v){cutedge(u,v);cutedge(v,u);};
 auto add_edge=[&](int u,int v){assert(find(g[u].begin(),g[u].end(),v)==g[u].end());g[u].push_back(v);g[v].push_back(u);};
 long long bfs_total=0;auto check=[&](int root){stamp++;int h=0,t=0;seen[root]=stamp;distance[root]=0;q[t++]=root;Check r{root,0,-1,{0,0,0,0,0}};
  while(h<t){int u=q[h++];r.layers[distance[u]]++;if(distance[u]==4)continue;for(int v:g[u])if(seen[v]!=stamp){seen[v]=stamp;distance[v]=distance[u]+1;q[t++]=v;}}
  r.reached=t;if(t<n+1)for(int v=0;v<=n;v++)if(seen[v]!=stamp){r.witness=v;break;}bfs_total++;return r;};
 int screened=0,pre_fail=0,pre_pass=0,old_fail=0,completed=0,maxroots=0;bool timed=false,hit=false;
 Candidate hititem;vector<Check>hitchecks;vector<U>cover(W);vector<string>rows;
 for(auto&c:items){
  if(cpu()-began>limit-.8){timed=true;break;}
  vector<int>expected=c.T;expected.insert(expected.end(),free.begin(),free.end());sort(expected.begin(),expected.end());
  assert(expected==c.S&&set<int>(c.T.begin(),c.T.end()).size()==4&&set<int>(c.S.begin(),c.S.end()).size()==11);
  auto T=c.T;sort(T.begin(),T.end());auto ends=vector<int>(c.cut.begin(),c.cut.end());sort(ends.begin(),ends.end());assert(T==ends);
  set<int>a;for(int v:c.T){assert(g[v].size()==11);a.insert(v);for(int w:g[v])a.insert(w);}assert(vector<int>(a.begin(),a.end())==c.A);
  for(int v:free)assert(g[v].size()==10);
  for(int j=0;j<4;j+=2)assert(find(g[c.cut[j]].begin(),g[c.cut[j]].end(),c.cut[j+1])!=g[c.cut[j]].end());
  cover=freeball;for(int v:c.T){const U*row=&balls[size_t(endpoint_index[v])*W];for(int w=0;w<W;w++)cover[w]|=row[w];}
  int missing=0;for(int w=0;w<W;w++)missing+=__builtin_popcountll(full[w]&~cover[w]);screened++;
  ostringstream row;row<<"{\"ordinal\":"<<c.ordinal<<",\"point_p\":"<<c.p<<",\"source_R3_missing\":"<<missing;
  if(missing){pre_fail++;completed++;row<<",\"status\":\"EXACT_NEWROOT_R3_FAIL\"}";rows.push_back(row.str());continue;}
  pre_pass++;erase_edge(c.cut[0],c.cut[1]);erase_edge(c.cut[2],c.cut[3]);for(int v:c.S)add_edge(n,v);
  for(auto&r:g)assert(r.size()==11);vector<Check>checks;checks.push_back(check(n));assert(checks.back().reached==n+1);
  bool candidate_ok=true;int checkedold=0;
  for(int root:c.A){if(cpu()-began>limit-.7){timed=true;candidate_ok=false;break;}
   checks.push_back(check(root));checkedold++;if(checks.back().reached!=n+1){candidate_ok=false;break;}}
  maxroots=max(maxroots,(int)checks.size());
  if(candidate_ok){hit=true;hititem=c;hitchecks=checks;completed++;row<<",\"status\":\"COMPLETE_D4_BY_AFFECTED_ROOTS\",\"roots_checked\":"<<checks.size()<<'}';rows.push_back(row.str());break;}
  if(!timed){old_fail++;completed++;}
  row<<",\"status\":\""<<(timed?"BUDGET_UNRESOLVED_CANDIDATE":"OLDPAIR_D4_FAIL")<<"\",\"roots_checked\":"<<checks.size()<<",\"first_bad_root\":";
  if(timed)row<<"null";else row<<checks.back().root;row<<",\"first_bad_target\":";if(timed)row<<"null";else row<<checks.back().witness;row<<'}';rows.push_back(row.str());
  for(int v:c.S)erase_edge(n,v);add_edge(c.cut[0],c.cut[1]);add_edge(c.cut[2],c.cut[3]);if(timed)break;
 }
 if(hit){
  ofstream ef(out+"/graph_d11_D4_n3646.edges");ef<<n+1<<' '<<m-2+11<<'\n';long long kept=0;
  set<pair<int,int>>F;for(int j=0;j<4;j+=2)F.insert(minmax(hititem.cut[j],hititem.cut[j+1]));
  for(auto[u,v]:edges)if(!F.count(minmax(u,v))){ef<<u<<' '<<v<<'\n';kept++;}assert(kept==m-2);for(int v:hititem.S)ef<<n<<' '<<v<<'\n';ef.close();
  ofstream hf(out+"/first_hit.json");hf<<"{\"status\":\"PRODUCER_COMPLETE_D4_PARENT_INDEPENDENT_PENDING\",\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"new_n\":"<<n+1<<",\"new_m\":"<<m+9<<",\"new_vertex\":"<<n<<",\"new_degree\":11,\"maximum_degree\":11,\"all_vertices_degree11\":true,\"ordinal\":"<<hititem.ordinal<<",\"point_p\":"<<hititem.p<<",\"deleted_edges\":[["<<hititem.cut[0]<<','<<hititem.cut[1]<<"],["<<hititem.cut[2]<<','<<hititem.cut[3]<<"]],\"endpoint_set\":";ints(hf,hititem.T);hf<<",\"free7\":";ints(hf,free);hf<<",\"full_neighbor_set\":";ints(hf,hititem.S);hf<<",\"affected_old_roots\":";ints(hf,hititem.A);
  hf<<",\"BFS_roots\":[";for(size_t i=0;i<hitchecks.size();i++){if(i)hf<<',';auto&r=hitchecks[i];hf<<"{\"root\":"<<r.root<<",\"reached\":"<<r.reached<<",\"distance_layers\":[";for(int j=0;j<5;j++){if(j)hf<<',';hf<<r.layers[j];}hf<<"]}";}
  hf<<"],\"global_D4_basis\":\"EveryaffectedR1(T)root plusnewroot checked; outside-outside oldpaths<=4 cannotusea deletededge. InheritedsourceD4.\",\"producer_allsource_BFS\":false,\"parent_independent_pending\":true}\n";
 }
 ofstream rf(out+"/NATIVE_RESULT.json");rf<<"{\"status\":\""<<(hit?"FIRST_COMPLETE3646_STOP":timed?"PARTIAL_CPU_BUDGET":"COMPLETE_FROZEN_FAMILY_NO_HIT")<<"\",\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"candidates_total\":"<<count<<",\"candidates_screened\":"<<screened<<",\"candidates_closed\":"<<completed<<",\"R3_screen_failures\":"<<pre_fail<<",\"R3_passers\":"<<pre_pass<<",\"oldpair_rejections\":"<<old_fail<<",\"root_BFS_executed\":"<<bfs_total<<",\"maximum_roots_for_one_candidate\":"<<maxroots<<",\"endpoint_R3_roots_prepared\":"<<prepared<<",\"free7_union_recomputed\":false,\"hit\":"<<(hit?"true":"false")<<",\"native_CPU_seconds\":"<<cpu()-began<<",\"rows\":[";
 for(size_t i=0;i<rows.size();i++){if(i)rf<<',';rf<<rows[i];}rf<<"]}\n";
 cout<<"FINAL hit="<<hit<<" screened="<<screened<<'/'<<count<<" R3pass="<<pre_pass<<" oldfail="<<old_fail<<" rootBFS="<<bfs_total<<" CPU="<<cpu()-began<<'\n';
}
