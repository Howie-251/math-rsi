#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
void ints(ostream&f,const vector<int>&v){f<<'[';for(size_t j=0;j<v.size();j++){if(j)f<<',';f<<v[j];}f<<']';}
struct Base{int old,p,r,t;array<int,4>F;vector<int>S;};
struct Item{int id,old,p,r,t;pair<int,int>sw;array<int,6>F;vector<int>T,S,free,A;};
struct Check{int root,reached,bad;array<int,5>layers;};
int main(int argc,char**argv){
 assert(argc==6);double began=cpu(),limit=stod(argv[5]);string source=argv[1],input=argv[2],old=argv[3],out=argv[4];
 rlimit hard{(rlim_t)ceil(limit),(rlim_t)ceil(limit+1)};setrlimit(RLIMIT_CPU,&hard);
 ifstream sf(source);int n,m;sf>>n>>m;assert(n==3645&&m==20044);const int W=(n+63)/64;
 vector<vector<int>>g(n+1);vector<pair<int,int>>edges;
 for(int j=0;j<m;j++){int u,v;sf>>u>>v;assert(sf);g[u].push_back(v);g[v].push_back(u);edges.push_back({u,v});}
 ifstream in(input);int B;in>>B;assert(B==47);vector<int>free(7);for(int&v:free)in>>v;
 for(int v=0;v<n;v++)assert(g[v].size()==size_t(find(free.begin(),free.end(),v)!=free.end()?10:11));
 vector<Base>bases(B);for(auto&b:bases){in>>b.old>>b.p>>b.r>>b.t;for(int&v:b.F)in>>v;b.S.resize(11);for(int&v:b.S)in>>v;assert(in);}
 vector<U>balls(size_t(n)*W);vector<bool>cached(n);ifstream roots(out+"/old_roots.txt"),binary(old+"/endpoint_R3.u64le.bin",ios::binary);
 int reused=0;for(int v;roots>>v;){assert(binary.read((char*)&balls[size_t(v)*W],W*8));cached[v]=true;reused++;}assert(reused==1964);
 auto dist2=[&](int v,const set<int>&S){if(S.count(v))return 0;for(int u:g[v])if(S.count(u))return 1;for(int u:g[v])for(int w:g[u])if(S.count(w))return 2;return 3;};
 vector<Item>items;vector<string>groups;int endpoint_proposals=0,missing_switch=0,witness_pruned_groups=0,witness_pruned_subsets=0,legalgroups=0;
 for(auto&b:bases){
  set<pair<int,int>>switches;for(int y:{b.r,b.t})if(1640<=y&&y<3444){endpoint_proposals++;int z=y^1;
   if(find(g[y].begin(),g[y].end(),z)!=g[y].end())switches.insert(minmax(y,z));else missing_switch++;}
  for(auto sw:switches){
   legalgroups++;set<int>ts(b.F.begin(),b.F.end());ts.insert(sw.first);ts.insert(sw.second);vector<int>T(ts.begin(),ts.end());
   set<int>Smax(b.S.begin(),b.S.end());Smax.insert(sw.first);Smax.insert(sw.second);
   int dr=dist2(b.r,Smax),dt=dist2(b.t,Smax),k=min(7,11-int(T.size()));assert(5<=k&&k<=7);
   vector<vector<int>>combinations;vector<int>chosen;
   function<void(int)>make=[&](int from){if((int)chosen.size()==k){combinations.push_back(chosen);return;}for(int j=from;j<7;j++)if(7-j>=k-int(chosen.size())){chosen.push_back(free[j]);make(j+1);chosen.pop_back();}};
   make(0);bool pass=2+dr+dt<=4;
   ostringstream gs;gs<<"{\"original_ordinal\":"<<b.old<<",\"point_p\":"<<b.p<<",\"original_badpair\":["<<b.r<<','<<b.t<<"],\"switch\":["<<sw.first<<','<<sw.second<<"],\"Tprime\":";ints(gs,T);
   gs<<",\"d_r_to_Smax_capped3\":"<<dr<<",\"d_t_to_Smax_capped3\":"<<dt<<",\"free_count\":"<<k<<",\"maximal_free_subsets\":"<<combinations.size()<<",\"original_witness_preflight_pass\":"<<(pass?"true":"false")<<'}';groups.push_back(gs.str());
   if(!pass){witness_pruned_groups++;witness_pruned_subsets+=combinations.size();continue;}
   set<int>A;for(int v:T){A.insert(v);for(int w:g[v])A.insert(w);}
   assert(A.size()<=72);
   for(auto selectedfree:combinations){
    vector<int>S=T;S.insert(S.end(),selectedfree.begin(),selectedfree.end());sort(S.begin(),S.end());assert(S.size()==11&&set<int>(S.begin(),S.end()).size()==11);
    Item c; c.id=items.size();c.old=b.old;c.p=b.p;c.r=b.r;c.t=b.t;c.sw=sw;c.T=T;c.S=S;c.free=selectedfree;c.A=vector<int>(A.begin(),A.end());
    copy(b.F.begin(),b.F.end(),c.F.begin());c.F[4]=sw.first;c.F[5]=sw.second;items.push_back(c);
   }
  }
 }
 assert(items.size()<=1974);
 {ofstream f(out+"/FROZEN_SWITCHES.json");f<<"{\"original_passers\":47,\"row_endpoint_proposals\":"<<endpoint_proposals<<",\"absent_switch_proposals\":"<<missing_switch<<",\"legal_switch_groups\":"<<legalgroups<<",\"witness_pruned_groups\":"<<witness_pruned_groups<<",\"witness_pruned_maximal_subsets\":"<<witness_pruned_subsets<<",\"candidate_count\":"<<items.size()<<",\"groups\":[";
  for(size_t j=0;j<groups.size();j++){if(j)f<<',';f<<groups[j];}f<<"],\"records\":[";
  for(size_t j=0;j<items.size();j++){if(j)f<<',';auto&c=items[j];f<<"{\"ordinal\":"<<c.id<<",\"original_ordinal\":"<<c.old<<",\"point_p\":"<<c.p<<",\"switch\":["<<c.sw.first<<','<<c.sw.second<<"],\"deleted_edges\":[["<<c.F[0]<<','<<c.F[1]<<"],["<<c.F[2]<<','<<c.F[3]<<"],["<<c.F[4]<<','<<c.F[5]<<"]],\"endpoint_set\":";ints(f,c.T);f<<",\"free_subset\":";ints(f,c.free);f<<",\"new_neighbors\":";ints(f,c.S);f<<",\"affected_roots\":";ints(f,c.A);f<<'}';}f<<"]}\n";}
 vector<int>needed;for(auto&c:items)for(int v:c.S)if(!cached[v]){cached[v]=true;needed.push_back(v);}sort(needed.begin(),needed.end());
 vector<int>d(n+1),q(n+1);vector<unsigned>seen(n+1);unsigned stamp=0;int prepared=0;bool timed=false;
 for(int root:needed){if(cpu()-began>limit-.7){timed=true;break;}stamp++;int h=0,t=0;seen[root]=stamp;d[root]=0;q[t++]=root;
  while(h<t){int u=q[h++];if(d[u]==3)continue;for(int v:g[u])if(seen[v]!=stamp){seen[v]=stamp;d[v]=d[u]+1;q[t++]=v;}}
  U*row=&balls[size_t(root)*W];for(int j=0;j<t;j++)row[q[j]/64]|=U(1)<<(q[j]%64);prepared++;}
 {ofstream f(out+"/NEW_R3_CACHE.json");f<<"{\"old_endpoint_balls_reused\":"<<reused<<",\"new_roots\":";ints(f,needed);f<<",\"prepared\":"<<prepared<<",\"words_per_row\":"<<W<<",\"complete\":"<<(!timed?"true":"false")<<"}\n";}
 {ofstream f(out+"/new_R3.u64le.bin",ios::binary);for(int v:needed)f.write((char*)&balls[size_t(v)*W],W*8);}
 vector<U>full(W,~U(0)),cover(W);if(n%64)full.back()=(U(1)<<(n%64))-1;
 auto delone=[&](int u,int v){auto p=find(g[u].begin(),g[u].end(),v);assert(p!=g[u].end());*p=g[u].back();g[u].pop_back();};
 auto deledge=[&](int u,int v){delone(u,v);delone(v,u);};
 auto addedge=[&](int u,int v){assert(find(g[u].begin(),g[u].end(),v)==g[u].end());g[u].push_back(v);g[v].push_back(u);};
 long long bfs=0;auto check=[&](int root){stamp++;int h=0,t=0;seen[root]=stamp;d[root]=0;q[t++]=root;Check c{root,0,-1,{0,0,0,0,0}};
  while(h<t){int u=q[h++];c.layers[d[u]]++;if(d[u]==4)continue;for(int v:g[u])if(seen[v]!=stamp){seen[v]=stamp;d[v]=d[u]+1;q[t++]=v;}}
  c.reached=t;if(t<n+1)for(int v=0;v<=n;v++)if(seen[v]!=stamp){c.bad=v;break;}bfs++;return c;};
 int tested=0,closed=0,rootfail=0,rootpass=0,oldfail=0,maxroots=0;bool hit=false;Item hititem;vector<Check>hitchecks;vector<string>rows;
 if(!timed)for(auto&c:items){
  if(cpu()-began>limit-.65){timed=true;break;}fill(cover.begin(),cover.end(),0);for(int v:c.S){const U*row=&balls[size_t(v)*W];for(int w=0;w<W;w++)cover[w]|=row[w];}
  int missing=0;for(int w=0;w<W;w++)missing+=__builtin_popcountll(full[w]&~cover[w]);tested++;
  ostringstream row;row<<"{\"ordinal\":"<<c.id<<",\"original_ordinal\":"<<c.old<<",\"source_R3_missing\":"<<missing;
  if(missing){rootfail++;closed++;row<<",\"status\":\"NEWROOT_R3_FAIL\"}";rows.push_back(row.str());continue;}
  rootpass++;for(int j=0;j<6;j+=2)deledge(c.F[j],c.F[j+1]);for(int v:c.S)addedge(n,v);
  int deficit=0;for(auto&r:g){assert(r.size()==10||r.size()==11);deficit+=11-r.size();}assert(deficit==2);
  vector<Check>checks{check(n)};assert(checks[0].reached==n+1);bool ok=true;
  for(int root:c.A){if(cpu()-began>limit-.55){timed=true;ok=false;break;}checks.push_back(check(root));if(checks.back().reached<n+1){ok=false;break;}}
  maxroots=max(maxroots,(int)checks.size());
  if(ok){hit=true;closed++;hititem=c;hitchecks=checks;row<<",\"status\":\"COMPLETE_D4\",\"roots_checked\":"<<checks.size()<<'}';rows.push_back(row.str());break;}
  if(!timed){oldfail++;closed++;}row<<",\"status\":\""<<(timed?"BUDGET_UNRESOLVED":"OLDPAIR_D4_FAIL")<<"\",\"roots_checked\":"<<checks.size()<<",\"first_bad_root\":";
  if(timed)row<<"null";else row<<checks.back().root;row<<",\"first_bad_target\":";if(timed)row<<"null";else row<<checks.back().bad;row<<'}';rows.push_back(row.str());
  for(int v:c.S)deledge(n,v);for(int j=0;j<6;j+=2)addedge(c.F[j],c.F[j+1]);if(timed)break;
 }
 if(hit){
  set<pair<int,int>>F;for(int j=0;j<6;j+=2)F.insert(minmax(hititem.F[j],hititem.F[j+1]));assert(F.size()==3);
  ofstream ef(out+"/graph_d11_D4_n3646.edges");ef<<n+1<<' '<<m-3+11<<'\n';int kept=0;for(auto[u,v]:edges)if(!F.count(minmax(u,v))){ef<<u<<' '<<v<<'\n';kept++;}assert(kept==m-3);for(int v:hititem.S)ef<<n<<' '<<v<<'\n';ef.close();
  ofstream f(out+"/first_hit.json");f<<"{\"status\":\"PRODUCER_COMPLETE_PARENT_INDEPENDENT_PENDING\",\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"new_n\":"<<n+1<<",\"new_m\":"<<m+8<<",\"maximum_degree\":11,\"degree_histogram\":{\"10\":2,\"11\":3644},\"new_vertex\":"<<n<<",\"new_degree\":11,\"ordinal\":"<<hititem.id<<",\"original_ordinal\":"<<hititem.old<<",\"original_badpair\":["<<hititem.r<<','<<hititem.t<<"],\"switch\":["<<hititem.sw.first<<','<<hititem.sw.second<<"],\"deleted_edges\":[";
  for(int j=0;j<6;j+=2){if(j)f<<',';f<<'['<<hititem.F[j]<<','<<hititem.F[j+1]<<']';}f<<"],\"endpoint_set\":";ints(f,hititem.T);f<<",\"free_subset\":";ints(f,hititem.free);f<<",\"full_neighbor_set\":";ints(f,hititem.S);f<<",\"affected_old_roots\":";ints(f,hititem.A);f<<",\"BFS_roots\":[";
  for(size_t j=0;j<hitchecks.size();j++){if(j)f<<',';auto&c=hitchecks[j];f<<"{\"root\":"<<c.root<<",\"reached\":"<<c.reached<<",\"distance_layers\":[";for(int k=0;k<5;k++){if(k)f<<',';f<<c.layers[k];}f<<"]}";}f<<"],\"global_D4_basis\":\"AllaffectedR1(Tprime)roots andnewroot checked; oldoutside pairs retain <=4source paths. InheritedsourceD4.\",\"producer_allsource_BFS\":false,\"parent_independent_pending\":true}\n";
 }
 ofstream rf(out+"/NATIVE_RESULT.json");rf<<"{\"status\":\""<<(hit?"FIRST_COMPLETE3646_STOP":timed?"PARTIAL_CPU_BUDGET":"COMPLETE_SINGLE_SWITCH_CLASS_NO_HIT")<<"\",\"original_passers\":47,\"legal_switch_groups\":"<<legalgroups<<",\"witness_pruned_groups\":"<<witness_pruned_groups<<",\"witness_pruned_maximal_subsets\":"<<witness_pruned_subsets<<",\"candidates_total\":"<<items.size()<<",\"candidates_screened\":"<<tested<<",\"candidates_closed\":"<<closed<<",\"R3_screen_failures\":"<<rootfail<<",\"R3_passers\":"<<rootpass<<",\"oldpair_rejections\":"<<oldfail<<",\"root_BFS_executed\":"<<bfs<<",\"maximum_roots_for_one_candidate\":"<<maxroots<<",\"old_endpoint_R3_balls_reused\":"<<reused<<",\"new_R3_balls_prepared\":"<<prepared<<",\"hit\":"<<(hit?"true":"false")<<",\"native_CPU_seconds\":"<<cpu()-began<<",\"rows\":[";
 for(size_t j=0;j<rows.size();j++){if(j)rf<<',';rf<<rows[j];}rf<<"]}\n";
 cout<<"FINAL hit="<<hit<<" groups="<<legalgroups<<" witnesspruned="<<witness_pruned_groups<<" tested="<<tested<<'/'<<items.size()<<" R3pass="<<rootpass<<" oldfail="<<oldfail<<" CPU="<<cpu()-began<<'\n';
}
