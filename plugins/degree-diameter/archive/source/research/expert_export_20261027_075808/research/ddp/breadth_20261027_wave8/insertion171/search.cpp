#include <bits/stdc++.h>
using namespace std;
using Bits=array<uint64_t,3>;
struct PairData{int u,v;vector<array<int,3>>paths;};
Bits operator|(Bits a,const Bits&b){for(int i=0;i<3;i++)a[i]|=b[i];return a;}
bool has(const Bits&a,int u){return a[u>>6]>>(u&63)&1;}
int main(int argc,char**argv){
 assert(argc==4);string dir=argv[1],source=argv[2];double limit=stod(argv[3]);clock_t began=clock();auto cpu=[&](){return double(clock()-began)/CLOCKS_PER_SEC;};
 int n,m;ifstream s(source);s>>n>>m;assert(n==170&&m==595);vector<pair<int,int>>edges(m);vector<vector<int>>adj(n);vector<Bits>endpoint(m),closed(m),cover(m),balls(n);Bits full={~0ULL,~0ULL,(1ULL<<42)-1};
 for(int e=0;e<m;e++){auto&[u,v]=edges[e];s>>u>>v;adj[u].push_back(v);adj[v].push_back(u);endpoint[e][u>>6]|=1ULL<<(u&63);endpoint[e][v>>6]|=1ULL<<(v&63);}
 ifstream bs(dir+"/source_b2.txt");for(auto&b:balls)bs>>b[0]>>b[1]>>b[2];
 for(int e=0;e<m;e++){auto[u,v]=edges[e];cover[e]=balls[u]|balls[v];closed[e]=endpoint[e];for(int x:adj[u])closed[e][x>>6]|=1ULL<<(x&63);for(int x:adj[v])closed[e][x>>6]|=1ULL<<(x&63);}
 ifstream pc(dir+"/paths.txt");int np;pc>>np;assert(np==10350);vector<PairData>pairs(np);vector<vector<int>>unique(m),firstpath(m);
 for(int p=0;p<np;p++){int count;pc>>pairs[p].u>>pairs[p].v>>count;pairs[p].paths.resize(count);for(auto&t:pairs[p].paths)pc>>t[0]>>t[1]>>t[2];for(int e:pairs[p].paths[0])firstpath[e].push_back(p);if(count==1)for(int e:pairs[p].paths[0])unique[e].push_back(p);}
 // Middle-edge unique paths are often the earliest exact obstruction.
 for(int e=0;e<m;e++)stable_sort(unique[e].begin(),unique[e].end(),[&](int a,int b){return (pairs[a].paths[0][1]==e)>(pairs[b].paths[0][1]==e);});
 long long raw=0,matching=0,cap_pass=0,unique_reject=0,unique_pass=0,unique_tests=0,full_started=0,full_reject=0,pairtests=0,pathtests=0,prefix_skip=0;
 int bestmiss=171;array<int,3>bestD={-1,-1,-1},hitD={-1,-1,-1},cursor={-1,-1,-1};bool hit=false,limited=false;vector<int>stamp(np);int generation=0;
 auto repaired=[&](const PairData&p,const Bits&S,const Bits&NS){return (has(S,p.u)&&has(NS,p.v))||(has(S,p.v)&&has(NS,p.u));};
 auto avoids=[&](const array<int,3>&p,int a,int b,int c){for(int e:p)if(e==a||e==b||e==c)return false;return true;};
 for(int a=0;a<m-2&&!hit&&!limited;a++)for(int b=a+1;b<m-1&&!hit&&!limited;b++){
  if(cpu()>=limit){limited=true;break;}Bits sab=endpoint[a]|endpoint[b];
  if(edges[a].first==edges[b].first||edges[a].first==edges[b].second||edges[a].second==edges[b].first||edges[a].second==edges[b].second){raw+=m-b-1;prefix_skip+=m-b-1;cursor={a,b,m-1};continue;}
  Bits cab=cover[a]|cover[b],nab=closed[a]|closed[b];
  for(int c=b+1;c<m;c++){
   raw++;cursor={a,b,c};if((raw&8191)==0&&cpu()>=limit){limited=true;break;}
   auto[x,y]=edges[c];if(has(sab,x)||has(sab,y))continue;matching++;
   Bits cb=cab|cover[c];int miss=0;for(int w=0;w<3;w++)miss+=__builtin_popcountll(full[w]&~cb[w]);
   if(miss<bestmiss){bestmiss=miss;bestD={a,b,c};}
   if(miss)continue;cap_pass++;Bits S=sab|endpoint[c],NS=nab|closed[c];bool okay=true;
   for(int e:{a,b,c}){for(int p:unique[e]){unique_tests++;if(!repaired(pairs[p],S,NS)){okay=false;break;}}if(!okay)break;}
   if(!okay){unique_reject++;continue;}unique_pass++;full_started++;generation++;
   for(int e:{a,b,c}){
    for(int p:firstpath[e])if(stamp[p]!=generation){stamp[p]=generation;pairtests++;if(repaired(pairs[p],S,NS))continue;bool good=false;for(auto path:pairs[p].paths){pathtests++;if(avoids(path,a,b,c)){good=true;break;}}if(!good){okay=false;break;}}
    if(!okay)break;
   }
   if(!okay){full_reject++;continue;}hit=true;hitD={a,b,c};break;
  }
 }
 array<int,3>D=hit?hitD:bestD;assert(D[0]>=0);Bits S{},NS{},coverage{};for(int e:D){S=S|endpoint[e];NS=NS|closed[e];coverage=coverage|cover[e];}
 vector<pair<int,int>>bad;vector<int>newmissing;
 for(int v=0;v<n;v++)if(!has(coverage,v)){newmissing.push_back(v);bad.push_back({v,170});}
 int oldbad=0;for(auto&p:pairs){bool good=repaired(p,S,NS);if(!good)for(auto path:p.paths)if(avoids(path,D[0],D[1],D[2])){good=true;break;}if(!good){oldbad++;bad.push_back({p.u,p.v});}}
 vector<pair<int,int>>selected;for(int e=0;e<m;e++)if(e!=D[0]&&e!=D[1]&&e!=D[2])selected.push_back(edges[e]);for(int v=0;v<n;v++)if(has(S,v))selected.push_back({v,170});
 assert(selected.size()==598);array<int,171>degrees{};for(auto[u,v]:selected){degrees[u]++;degrees[v]++;}for(int u=0;u<170;u++)assert(degrees[u]==7);assert(degrees[170]==6);
 string name=hit?"hit":"fallback";ofstream ef(dir+"/"+name+".edges");ef<<"171 598\n";for(auto[u,v]:selected)ef<<u<<' '<<v<<'\n';
 ofstream out(dir+"/"+name+"_predictions.json");out<<"{\"selection_rule\":\""<<(hit?"full_target_hit":"minimum new-root uncovered count among all examined legal matching triples; first lexical tie; not optimized for total bad pairs")<<"\",\"removed_edge_ids\":["<<D[0]<<','<<D[1]<<','<<D[2]<<"],\"removed_edges\":[";for(int i=0;i<3;i++){if(i)out<<',';auto[u,v]=edges[D[i]];out<<'['<<u<<','<<v<<']';}
 out<<"],\"new_neighbors\":[";bool comma=false;for(int v=0;v<n;v++)if(has(S,v)){if(comma)out<<',';comma=true;out<<v;}out<<"],\"new_root_uncovered_vertices\":[";for(int i=0;i<(int)newmissing.size();i++){if(i)out<<',';out<<newmissing[i];}out<<"],\"new_old_bad_pairs\":"<<newmissing.size()<<",\"old_old_bad_pairs\":"<<oldbad<<",\"total_bad_unordered_pairs_gt3\":"<<bad.size()<<",\"bad_pairs\":[";for(int i=0;i<(int)bad.size();i++){if(i)out<<',';out<<'['<<bad[i].first<<','<<bad[i].second<<']';}out<<"],\"all171_degrees_checked\":true,\"ordinary_BFS_performed\":false}\n";
 long long planned=1LL*m*(m-1)*(m-2)/6;
 if(!limited&&!hit)assert(raw==planned);
 ofstream t(dir+"/search_result.json");t<<"{\"status\":\""<<(hit?"HIT_INSERTION171_DIAMETER3":limited?"CPU_LIMIT_INCOMPLETE_FAMILY":"COMPLETE_FIXED_THREE_EDGE_INSERTION_FAMILY_NO_HIT")<<"\",\"raw_triples_planned\":"<<planned<<",\"raw_triples_considered\":"<<raw<<",\"raw_prefix_triples_rejected_for_shared_first_two_edges\":"<<prefix_skip<<",\"legal_three_edge_matchings\":"<<matching<<",\"S_radius2_dominating_candidates\":"<<cap_pass<<",\"unique_filter_rejected\":"<<unique_reject<<",\"unique_filter_passed\":"<<unique_pass<<",\"unique_pair_tests\":"<<unique_tests<<",\"exact_full_checks_started\":"<<full_started<<",\"exact_full_checks_rejected\":"<<full_reject<<",\"exact_candidate_pair_tests\":"<<pairtests<<",\"old_path_support_tests\":"<<pathtests<<",\"hits\":"<<(hit?1:0)<<",\"minimum_new_root_uncovered\":"<<bestmiss<<",\"cursor\":["<<cursor[0]<<','<<cursor[1]<<','<<cursor[2]<<"],\"complete\":"<<(!limited&&!hit?"true":"false")<<",\"selected_graph\":\""<<name<<".edges\",\"selected_total_bad_prediction\":"<<bad.size()<<",\"selected_new_root_bad_prediction\":"<<newmissing.size()<<",\"selected_old_old_bad_prediction\":"<<oldbad<<",\"CPU_seconds\":"<<cpu()<<",\"CPU_internal_limit_seconds\":"<<limit<<",\"BFS_performed\":false,\"source_BFS_reused\":true}\n";
 if(hit)cout<<"HIT_SAVED hit.edges"<<endl;
}
