#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
void ints(ostream&f,const vector<int>&v){f<<'[';for(size_t j=0;j<v.size();j++){if(j)f<<',';f<<v[j];}f<<']';}
struct Candidate{int id,base,layer;array<int,4>F,S;};
struct Check{int root,reached,bad;array<int,7>layers;};
int main(int argc,char**argv){
 assert(argc==5);double began=cpu(),limit=stod(argv[4]);string source=argv[1],input=argv[2],out=argv[3];
 rlimit hard{(rlim_t)ceil(limit),(rlim_t)ceil(limit+1)};setrlimit(RLIMIT_CPU,&hard);
 ifstream sf(source);int n,m;sf>>n>>m;assert(n==760&&m==1520);const int W=(n+63)/64;
 vector<vector<int>>g(n+1);vector<pair<int,int>>edges;
 for(int j=0;j<m;j++){int u,v;sf>>u>>v;assert(sf);g[u].push_back(v);g[v].push_back(u);edges.push_back({u,v});}
 for(int v=0;v<n;v++)assert(g[v].size()==4);
 ifstream in(input);int count;in>>count;assert(count==45568);vector<Candidate>items(count);vector<bool>needed(n);vector<int>roots;
 for(auto&c:items){in>>c.id>>c.base>>c.layer;for(int&v:c.F)in>>v;for(int&v:c.S)in>>v;assert(in);
  vector<int>ends(c.F.begin(),c.F.end());sort(ends.begin(),ends.end());assert(set<int>(ends.begin(),ends.end()).size()==4&&equal(ends.begin(),ends.end(),c.S.begin()));
  for(int v:c.S)needed[v]=true;}
 for(int v=0;v<n;v++)if(needed[v])roots.push_back(v);
 vector<U>r5(size_t(n)*W),r2(size_t(n)*W),full(W,~U(0));if(n%64)full.back()=(U(1)<<(n%64))-1;
 vector<unsigned>seen(n+1);unsigned stamp=0;vector<int>d(n+1),q(n+1);int prepared=0;bool timed=false;double prepstart=cpu();
 for(int root:roots){
  if(cpu()-began>limit-.9){timed=true;break;}stamp++;int h=0,t=0;seen[root]=stamp;d[root]=0;q[t++]=root;
  while(h<t){int u=q[h++];if(d[u]==5)continue;for(int v:g[u])if(seen[v]!=stamp){seen[v]=stamp;d[v]=d[u]+1;q[t++]=v;}}
  U*b5=&r5[size_t(root)*W],*b2=&r2[size_t(root)*W];for(int j=0;j<t;j++){int v=q[j];b5[v/64]|=U(1)<<(v%64);if(d[v]<=2)b2[v/64]|=U(1)<<(v%64);}prepared++;
  if(prepared==100){double elapsed=cpu()-prepstart,projected=cpu()-began+elapsed*(roots.size()-100)/100.;
   ofstream f(out+"/PROFILE100_ROOTS.json");f<<"{\"endpoint_roots_profiled_once\":100,\"endpoint_roots_total\":"<<roots.size()<<",\"CPU100\":"<<elapsed<<",\"projected_native_prepCPU\":"<<projected<<",\"radius5_and_radius2_same_BFS\":true,\"profile_replayed\":false}\n";
   if(projected>limit-1){timed=true;break;}}
 }
 {ofstream f(out+"/source_R5.u64le.bin",ios::binary);f.write((char*)r5.data(),r5.size()*8);}
 {ofstream f(out+"/source_R2.u64le.bin",ios::binary);f.write((char*)r2.data(),r2.size()*8);}
 {ofstream f(out+"/RADIUS_CACHE.json");f<<"{\"source_n\":760,\"source_m\":1520,\"row_order\":\"source vertex ID,zero rows if unused\",\"words_per_row\":"<<W<<",\"needed_roots\":";ints(f,roots);f<<",\"roots_prepared\":"<<prepared<<",\"radius2_snapshotted_with_radius5\":true,\"complete\":"<<(!timed?"true":"false")<<"}\n";}
 if(timed){ofstream f(out+"/NATIVE_RESULT.json");f<<"{\"status\":\"PARTIAL_RADIUS_PREPARATION\",\"candidates_total\":"<<count<<",\"candidates_screened\":0,\"candidates_closed\":0,\"endpoint_R5_roots_prepared\":"<<prepared<<",\"native_CPU_seconds\":"<<cpu()-began<<"}\n";return 0;}
 auto delone=[&](int u,int v){auto p=find(g[u].begin(),g[u].end(),v);assert(p!=g[u].end());*p=g[u].back();g[u].pop_back();};
 auto deledge=[&](int u,int v){delone(u,v);delone(v,u);};
 auto addedge=[&](int u,int v){assert(find(g[u].begin(),g[u].end(),v)==g[u].end());g[u].push_back(v);g[v].push_back(u);};
 long long bfs=0;auto check=[&](int root){stamp++;int h=0,t=0;seen[root]=stamp;d[root]=0;q[t++]=root;Check c{root,0,-1,{0,0,0,0,0,0,0}};
  while(h<t){int u=q[h++];c.layers[d[u]]++;if(d[u]==6)continue;for(int v:g[u])if(seen[v]!=stamp){seen[v]=stamp;d[v]=d[u]+1;q[t++]=v;}}
  c.reached=t;if(t<n+1)for(int v=0;v<=n;v++)if(seen[v]!=stamp){c.bad=v;break;}bfs++;return c;};
 vector<U>cover(W),affected(W);vector<string>rows;int tested=0,closed=0,rootfail=0,rootpass=0,oldfail=0,maxroots=0;
 bool hit=false;Candidate hititem;vector<int>hitA;vector<Check>hitchecks;double candidatestart=cpu();
 for(auto&c:items){
  if(cpu()-began>limit-.85){timed=true;break;}
  fill(cover.begin(),cover.end(),0);for(int v:c.S){const U*b=&r5[size_t(v)*W];for(int w=0;w<W;w++)cover[w]|=b[w];}
  int missing=0;for(int w=0;w<W;w++)missing+=__builtin_popcountll(full[w]&~cover[w]);tested++;
  ostringstream row;row<<"{\"ordinal\":"<<c.id<<",\"base_edge_index\":"<<c.base<<",\"layer_edge_index\":"<<c.layer<<",\"source_R5_missing\":"<<missing;
  if(missing){rootfail++;closed++;row<<",\"status\":\"NEWROOT_R5_FAIL\"}";rows.push_back(row.str());}
  else{
   rootpass++;fill(affected.begin(),affected.end(),0);for(int v:c.S){const U*b=&r2[size_t(v)*W];for(int w=0;w<W;w++)affected[w]|=b[w];}
   vector<int>A;for(int w=0;w<W;w++){U b=affected[w];while(b){A.push_back(64*w+__builtin_ctzll(b));b&=b-1;}}assert(A.size()<=68);
   for(int j=0;j<4;j+=2)assert(find(g[c.F[j]].begin(),g[c.F[j]].end(),c.F[j+1])!=g[c.F[j]].end());
   deledge(c.F[0],c.F[1]);deledge(c.F[2],c.F[3]);for(int v:c.S)addedge(n,v);for(auto&r:g)assert(r.size()==4);
   vector<Check>checks{check(n)};assert(checks[0].reached==n+1);bool ok=true;
   for(int root:A){if(cpu()-began>limit-.75){timed=true;ok=false;break;}checks.push_back(check(root));if(checks.back().reached<n+1){ok=false;break;}}
   maxroots=max(maxroots,(int)checks.size());
   if(ok){hit=true;closed++;hititem=c;hitchecks=checks;hitA=A;row<<",\"status\":\"COMPLETE_D6\",\"roots_checked\":"<<checks.size()<<'}';rows.push_back(row.str());break;}
   if(!timed){oldfail++;closed++;}row<<",\"status\":\""<<(timed?"BUDGET_UNRESOLVED":"OLDPAIR_D6_FAIL")<<"\",\"roots_checked\":"<<checks.size()<<",\"first_bad_root\":";
   if(timed)row<<"null";else row<<checks.back().root;row<<",\"first_bad_target\":";if(timed)row<<"null";else row<<checks.back().bad;row<<'}';rows.push_back(row.str());
   for(int v:c.S)deledge(n,v);addedge(c.F[0],c.F[1]);addedge(c.F[2],c.F[3]);if(timed)break;
  }
  if(tested==100){double elapsed=cpu()-candidatestart;ofstream f(out+"/PROFILE100_CANDIDATES.json");f<<"{\"candidates_tested_once\":100,\"CPU100\":"<<elapsed<<",\"projected_native_whole_scopeCPU\":"<<cpu()-began+elapsed*(count-100)/100.<<",\"profile_replayed\":false}\n";}
 }
 if(hit){
  set<pair<int,int>>F;for(int j=0;j<4;j+=2)F.insert(minmax(hititem.F[j],hititem.F[j+1]));assert(F.size()==2);
  ofstream ef(out+"/graph_d4_D6_n761.edges");ef<<n+1<<' '<<m-2+4<<'\n';int kept=0;for(auto[u,v]:edges)if(!F.count(minmax(u,v))){ef<<u<<' '<<v<<'\n';kept++;}assert(kept==m-2);for(int v:hititem.S)ef<<n<<' '<<v<<'\n';ef.close();
  ofstream f(out+"/first_hit.json");f<<"{\"status\":\"PRODUCER_COMPLETE_PARENT_INDEPENDENT_PENDING\",\"source_n\":760,\"source_m\":1520,\"new_n\":761,\"new_m\":1522,\"maximum_degree\":4,\"all_vertices_degree4\":true,\"new_vertex\":760,\"new_degree\":4,\"ordinal\":"<<hititem.id<<",\"base_edge_index\":"<<hititem.base<<",\"layer_edge_index\":"<<hititem.layer<<",\"deleted_edges\":[["<<hititem.F[0]<<','<<hititem.F[1]<<"],["<<hititem.F[2]<<','<<hititem.F[3]<<"]],\"full_neighbor_set\":";ints(f,vector<int>(hititem.S.begin(),hititem.S.end()));f<<",\"affected_old_roots_R2\":";ints(f,hitA);f<<",\"BFS_roots\":[";
  for(size_t j=0;j<hitchecks.size();j++){if(j)f<<',';auto&c=hitchecks[j];f<<"{\"root\":"<<c.root<<",\"reached\":"<<c.reached<<",\"distance_layers\":[";for(int k=0;k<7;k++){if(k)f<<',';f<<c.layers[k];}f<<"]}";}f<<"],\"global_D6_basis\":\"AllsourceR2(endpoints)roots plusnewroot checked; outsidepairsold<=6paths cannotusecuts. InheritedsourceD6.\",\"producer_allsource_BFS\":false,\"parent_independent_pending\":true}\n";
 }
 ofstream rf(out+"/NATIVE_RESULT.json");rf<<"{\"status\":\""<<(hit?"FIRST_COMPLETE761_STOP":timed?"PARTIAL_CPU_BUDGET":"COMPLETE_FROZEN_FLAG_LAYER_FAMILY_NO_HIT")<<"\",\"source_n\":760,\"source_m\":1520,\"candidates_total\":"<<count<<",\"candidates_screened\":"<<tested<<",\"candidates_closed\":"<<closed<<",\"R5_screen_failures\":"<<rootfail<<",\"R5_passers\":"<<rootpass<<",\"oldpair_rejections\":"<<oldfail<<",\"modified_root_BFS_executed\":"<<bfs<<",\"maximum_roots_for_one_candidate\":"<<maxroots<<",\"source_endpoint_R5_roots_prepared\":"<<prepared<<",\"source_R2_same_run_snapshots\":"<<prepared<<",\"hit\":"<<(hit?"true":"false")<<",\"native_CPU_seconds\":"<<cpu()-began<<",\"rows\":[";
 for(size_t j=0;j<rows.size();j++){if(j)rf<<',';rf<<rows[j];}rf<<"]}\n";
 cout<<"FINAL hit="<<hit<<" tested="<<tested<<'/'<<count<<" R5pass="<<rootpass<<" oldfail="<<oldfail<<" BFS="<<bfs<<" CPU="<<cpu()-began<<'\n';
}
