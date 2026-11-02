#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
void ints(ostream&f,const vector<int>&a){f<<'[';for(int i=0;i<(int)a.size();i++){if(i)f<<',';f<<a[i];}f<<']';}
struct Line{int pool;vector<int>pins;vector<U>b3,b4;vector<int>missing;};
struct Pair{int i,j;vector<int>z,w;int score;};
int main(int argc,char**argv){
 rlimit limit{15,15};setrlimit(RLIMIT_CPU,&limit);clock_t st=clock();auto cpu=[&](){return double(clock()-st)/CLOCKS_PER_SEC;};
 string source=argv[1],dir=argv[2];ifstream in(source);int N,M;in>>N>>M;assert(N==42397&&M==245877);vector<vector<int>>g(N);vector<pair<int,int>>edges;
 for(int i=0,u,v;i<M;i++){in>>u>>v;g[u].push_back(v);g[v].push_back(u);edges.push_back({u,v});}int W=(N+63)/64;
 vector<int>dep(N),seen(N),q(N);int stamp=0;
 auto bfs=[&](const vector<int>&pins,int r){stamp++;int head=0,tail=0;for(int p:pins)if(seen[p]!=stamp){seen[p]=stamp;dep[p]=0;q[tail++]=p;}while(head<tail){int u=q[head++];if(dep[u]==r)continue;for(int v:g[u])if(seen[v]!=stamp){seen[v]=stamp;dep[v]=dep[u]+1;q[tail++]=v;}}return tail;};
 ifstream pf(dir+"/tenpin_lines.txt");int inputCount;pf>>inputCount;assert(inputCount==596);vector<Line>lines;vector<int>blocked;int canonical=0;
 for(int it=0;it<596;it++){
  int pool;pf>>pool;vector<int>pins(10);for(int&p:pins)pf>>p;bool legal=true;for(int p:pins)if(g[p].size()>=12)legal=false;
  if(!legal){blocked.push_back(pool);continue;}Line L;L.pool=pool;L.pins=pins;L.b3.assign(W,0);L.b4.assign(W,0);int tail=bfs(pins,4);
  for(int j=0;j<tail;j++){int u=q[j];L.b4[u>>6]|=U(1)<<(u&63);if(dep[u]<=3)L.b3[u>>6]|=U(1)<<(u&63);}
  for(int u=0;u<N;u++)if(seen[u]!=stamp)L.missing.push_back(u);lines.push_back(move(L));
 }
 ofstream lc(dir+"/line_R3_R4.u64.bin",ios::binary);for(auto&L:lines){lc.write((char*)L.b3.data(),8*W);lc.write((char*)L.b4.data(),8*W);}lc.close();
 vector<Pair>pairs;int degreeRejected=0,totalPairs=lines.size()*(lines.size()-1)/2;
 for(int i=0;i<(int)lines.size();i++)for(int j=i+1;j<(int)lines.size();j++){
  bool legal=true;for(int p:lines[i].pins)if(find(lines[j].pins.begin(),lines[j].pins.end(),p)!=lines[j].pins.end()&&g[p].size()+2>12){legal=false;break;}
  if(!legal){degreeRejected++;continue;}Pair p{i,j};for(int t:lines[i].missing)if(!(lines[j].b3[t>>6]>>(t&63)&1))p.z.push_back(t);for(int t:lines[j].missing)if(!(lines[i].b3[t>>6]>>(t&63)&1))p.w.push_back(t);p.score=p.z.size()+p.w.size();pairs.push_back(move(p));
 }
 sort(pairs.begin(),pairs.end(),[&](auto&a,auto&b){return tuple(a.score,lines[a.i].pool,lines[a.j].pool)<tuple(b.score,lines[b.i].pool,lines[b.j].pool);});int compatible=pairs.size();if(pairs.size()>32)pairs.resize(32);
 ofstream profile(dir+"/profile.json");profile<<"{\"source_n\":"<<N<<",\"source_m\":"<<M<<",\"input10pin_lines\":596,\"legal_lines\":"<<lines.size()<<",\"degreeblocked_lines\":"<<blocked.size()<<",\"raw_legal_line_pairs\":"<<totalPairs<<",\"degreeincompatible_pairs\":"<<degreeRejected<<",\"compatible_pairs\":"<<compatible<<",\"frozen_pairs\":"<<pairs.size()<<",\"CPU_seconds\":"<<cpu()<<",\"line_cache_layout\":\"legal-line major,R3 thenR4,663nativeu64words per ball\",\"legal_line_records\":[";
 for(int i=0;i<(int)lines.size();i++){if(i)profile<<',';profile<<"{\"line_index\":"<<i<<",\"pool_index\":"<<lines[i].pool<<",\"pins\":";ints(profile,lines[i].pins);profile<<",\"R4_missing\":";ints(profile,lines[i].missing);profile<<'}';}profile<<"],\"frozen_pair_records\":[";
 for(int i=0;i<(int)pairs.size();i++){if(i)profile<<',';auto&p=pairs[i];profile<<"{\"ordinal\":"<<i<<",\"A_pool\":"<<lines[p.i].pool<<",\"B_pool\":"<<lines[p.j].pool<<",\"sort_residual_count\":"<<p.score<<",\"Z_residual\":";ints(profile,p.z);profile<<",\"W_residual\":";ints(profile,p.w);profile<<'}';}profile<<"]}\n";profile.close();
 cerr<<"PROFILE legal_lines="<<lines.size()<<" compatible_pairs="<<compatible<<" frozen="<<pairs.size()<<" cpu="<<cpu()<<'\n';
 vector<int>P;for(int u=0;u<N;u++)if(g[u].size()<12)P.push_back(u);int K=P.size(),KW=(K+63)/64;
 set<int>uset;for(auto&p:pairs){uset.insert(p.z.begin(),p.z.end());uset.insert(p.w.begin(),p.w.end());}vector<int>targets(uset.begin(),uset.end()),targetIndex(N,-1);for(int i=0;i<(int)targets.size();i++)targetIndex[targets[i]]=i;
 vector<vector<U>>C3(targets.size(),vector<U>(KW)),C4=C3;vector<int>cnt3(targets.size()),cnt4(targets.size());int computedTargets=0;bool limited=false;
 for(int ti=0;ti<(int)targets.size();ti++){
  if(cpu()>12){limited=true;break;}bfs(vector<int>{targets[ti]},4);
  for(int ai=0;ai<K;ai++)if(seen[P[ai]]==stamp){C4[ti][ai>>6]|=U(1)<<(ai&63);cnt4[ti]++;if(dep[P[ai]]<=3){C3[ti][ai>>6]|=U(1)<<(ai&63);cnt3[ti]++;}}
  computedTargets++;
 }
 ofstream ts(dir+"/target_support.u64.bin",ios::binary);for(int i=0;i<computedTargets;i++){ts.write((char*)C3[i].data(),8*KW);ts.write((char*)C4[i].data(),8*KW);}ts.close();
 struct Row{int ordinal;string status;long long atested;int a=-1,b=-1;};vector<Row>results;long long totalAtested=0;int hitOrdinal=-1,ha=-1,hb=-1;vector<int>hitZ,hitW;
 if(!limited)for(int ordinal=0;ordinal<(int)pairs.size();ordinal++){
  if(cpu()>12){limited=true;break;}auto&p=pairs[ordinal];auto&A=lines[p.i].pins;auto&B=lines[p.j].pins;vector<int>load(N);for(int u:A)load[u]++;for(int u:B)load[u]++;
  vector<int>validA;vector<U>validB(KW);
  for(int j=0;j<K;j++){int u=P[j];if(g[u].size()+load[u]+1>12)continue;if(find(A.begin(),A.end(),u)==A.end())validA.push_back(j);if(find(B.begin(),B.end(),u)==B.end())validB[j>>6]|=U(1)<<(j&63);}
  vector<pair<int,int>>constraints;for(int t:p.z)constraints.push_back({targetIndex[t],0});for(int t:p.w)constraints.push_back({targetIndex[t],1});
  sort(constraints.begin(),constraints.end(),[&](auto&a,auto&b){int ca=a.second?cnt4[a.first]:cnt3[a.first],cb=b.second?cnt4[b.first]:cnt3[b.first];return tuple(ca,a.second,a.first)<tuple(cb,b.second,b.first);});
  long long tested=0;bool found=false;vector<U>candidate(KW);
  for(int ai:validA){
   if((tested&63)==0&&cpu()>12){limited=true;break;}tested++;totalAtested++;candidate=validB;
   int av=P[ai];if(g[av].size()+load[av]+2>12)candidate[ai>>6]&=~(U(1)<<(ai&63));
   bool any=true;
   for(auto[ti,kind]:constraints){auto&acov=kind?C3[ti]:C4[ti];if(acov[ai>>6]>>(ai&63)&1)continue;auto&bcov=kind?C4[ti]:C3[ti];any=false;for(int w=0;w<KW;w++){candidate[w]&=bcov[w];any|=candidate[w]!=0;}if(!any)break;}
   if(any){int bi=-1;for(int w=0;w<KW;w++)if(candidate[w]){bi=64*w+__builtin_ctzll(candidate[w]);break;}if(bi>=0){ha=av;hb=P[bi];hitOrdinal=ordinal;found=true;break;}}
  }
  if(found){results.push_back({ordinal,"COMPLETE_TWO_ROLE_ANCHOR_COVER",tested,ha,hb});break;}
  results.push_back({ordinal,limited?"UNKNOWN_CPU_WINDOW":"EXACT_NO_TWO_ROLE_ANCHORS_ON_THIS_PAIR",tested});if(limited)break;
 }
 vector<int>reached,maxdepth;string finalStatus=limited?"PARTIAL_CPU_WINDOW_UNCOMPUTED_OR_UNKNOWN":"ALL_FROZEN_PAIRS_EXACTLY_NO_HIT";
 if(hitOrdinal>=0){
  auto&p=pairs[hitOrdinal];hitZ=lines[p.i].pins;hitW=lines[p.j].pins;hitZ.push_back(ha);hitW.push_back(hb);sort(hitZ.begin(),hitZ.end());sort(hitW.begin(),hitW.end());assert(hitZ.size()==11&&hitW.size()==11&&adjacent_find(hitZ.begin(),hitZ.end())==hitZ.end()&&adjacent_find(hitW.begin(),hitW.end())==hitW.end());
  vector<int>load(N);for(int u:hitZ)load[u]++;for(int u:hitW)load[u]++;for(int u=0;u<N;u++)assert(g[u].size()+load[u]<=12);
  g.push_back(hitZ);g.push_back(hitW);g[N].push_back(N+1);g[N+1].push_back(N);for(int u:hitZ)g[u].push_back(N);for(int u:hitW)g[u].push_back(N+1);
  for(int root:{N,N+1}){vector<int>d(N+2,-1),qq{root};d[root]=0;for(int i=0;i<(int)qq.size();i++){int u=qq[i];if(d[u]==5)continue;for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;qq.push_back(v);}}assert(qq.size()==N+2);reached.push_back(qq.size());maxdepth.push_back(*max_element(d.begin(),d.end()));}
  ofstream graph(dir+"/graph_d12_D5_n42399.edges");graph<<N+2<<' '<<M+23<<'\n';int ec=0;for(int u=0;u<N+2;u++)for(int v:g[u])if(u<v){graph<<u<<' '<<v<<'\n';ec++;}assert(ec==M+23);graph.close();finalStatus="COMPLETE42399_BLOCK_PRODUCED_AWAIT_PARENT_ACCEPTANCE";
  ofstream hit(dir+"/hit.json");hit<<"{\"source_n\":"<<N<<",\"source_m\":"<<M<<",\"target_n\":"<<N+2<<",\"target_m\":"<<M+23<<",\"ordinal\":"<<hitOrdinal<<",\"A_pool\":"<<lines[p.i].pool<<",\"B_pool\":"<<lines[p.j].pool<<",\"a\":"<<ha<<",\"b\":"<<hb<<",\"A\":";ints(hit,lines[p.i].pins);hit<<",\"B\":";ints(hit,lines[p.j].pins);hit<<",\"new_vertices\":[42397,42398],\"old_neighbors_Z\":";ints(hit,hitZ);hit<<",\"old_neighbors_W\":";ints(hit,hitW);hit<<",\"new_edge\":[42397,42398],\"new_degrees\":[12,12],\"all_old_degrees_within12\":true,\"positive_two_new_root_R5_reached\":";ints(hit,reached);hit<<",\"positive_two_new_root_maxdepth\":";ints(hit,maxdepth);hit<<",\"oldsource_D5_basis\":\"Previouslyaccepted actualdegree/completeR4 induction; last independent allsource42377\",\"allsourceBFS\":0,\"parent_pending\":true,\"edge_file\":\"graph_d12_D5_n42399.edges\"}\n";hit.close();cerr<<"HIT ordinal="<<hitOrdinal<<" a="<<ha<<" b="<<hb<<" n42399 m"<<M+23<<" cpu="<<cpu()<<'\n';
 }
 ofstream out(dir+"/RESULT.json");out<<"{\"status\":\""<<finalStatus<<"\",\"source_n\":"<<N<<",\"source_m\":"<<M<<",\"target_n\":42399,\"target_Delta\":12,\"target_D\":5,\"legal_lines\":"<<lines.size()<<",\"compatible_pairs\":"<<compatible<<",\"frozen_pairs\":"<<pairs.size()<<",\"coupled_pairs_processed\":"<<results.size()<<",\"coupled_pairs_unprocessed\":"<<pairs.size()-results.size()<<",\"candidate_oldanchors\":"<<K<<",\"unique_residual_targets\":"<<targets.size()<<",\"reverse_R4_targets_computed\":"<<computedTargets<<",\"candidate_a_tested\":"<<totalAtested<<",\"hit\":"<<(hitOrdinal>=0?"true":"false")<<",\"CPU_seconds\":"<<setprecision(12)<<cpu()<<",\"allsourceBFS\":0,\"solver_calls\":0,\"positive_new_root_R5_checks\":"<<(hitOrdinal>=0?2:0)<<",\"anchor_vertices\":";ints(out,P);out<<",\"residual_target_order\":";ints(out,targets);out<<",\"target_support_layout\":\"target-major R3thenR4,KWnativeu64; onlycomputed target prefix stored\",\"target_support_words_per_row\":"<<KW<<",\"pair_results\":[";for(int i=0;i<(int)results.size();i++){if(i)out<<',';auto&r=results[i];out<<"{\"ordinal\":"<<r.ordinal<<",\"status\":\""<<r.status<<"\",\"a_tested\":"<<r.atested<<",\"a\":"<<r.a<<",\"b\":"<<r.b<<'}';}out<<"],\"extra_rounds\":0,\"third_new_point\":false}\n";out.close();cerr<<"FINAL "<<finalStatus<<" processed="<<results.size()<<" cpu="<<cpu()<<'\n';
}
