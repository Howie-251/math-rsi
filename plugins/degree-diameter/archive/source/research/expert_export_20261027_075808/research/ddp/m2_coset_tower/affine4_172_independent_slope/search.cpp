#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
constexpr int Q=43,N=172,D=7,E=14,SCOPE=574;
array<int,E>eu,ev,bias;
int adjacency[N][D],degree[N],distance_matrix[N][N],expected_first[N][N],inverse_slope[Q];
bool present[N][N];
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
template<class T>void arr(ostream&o,const T&a){o<<'[';bool comma=false;for(auto x:a){if(comma)o<<',';comma=true;o<<x;}o<<']';}
struct Result{int edges=0,min_degree=D,max_degree=0,diameter=0,bad=0,unreachable=0,degree6=0;array<int,N>miss{};array<int,N+1>hist{};};
Result build(int changed,int slope){
 fill(&present[0][0],&present[0][0]+N*N,false);fill(degree,degree+N,0);Result result;
 for(int e=0;e<E;e++)for(int x=0;x<Q;x++){
  int a=e==changed?slope:1,y=(a*x+bias[e])%Q,u=Q*eu[e]+x,v=Q*ev[e]+y;
  assert(u!=v&&((inverse_slope[a]*((y-bias[e]+Q)%Q))%Q)==x);
  if(present[u][v])continue;
  present[u][v]=present[v][u]=true;assert(degree[u]<D&&degree[v]<D);
  adjacency[u][degree[u]++]=v;adjacency[v][degree[v]++]=u;result.edges++;
 }
 int multiplicity=0;for(int e=0;e<E;e++)multiplicity+=eu[e]==eu[changed]&&ev[e]==ev[changed];
 assert((multiplicity==2||multiplicity==3)&&result.edges==602-(multiplicity-1));
 for(int d:degree){result.min_degree=min(result.min_degree,d);result.max_degree=max(result.max_degree,d);result.degree6+=d==6;}
 assert(result.min_degree==6&&result.max_degree==7&&result.degree6==2*(multiplicity-1));
 return result;
}
void full_bfs(Result&r){
 int queue[N];int ordered_bad=0;
 for(int root=0;root<N;root++){
  int*dist=distance_matrix[root];fill(dist,dist+N,-1);dist[root]=0;queue[0]=root;int head=0,tail=1,ecc=0;
  while(head<tail){int u=queue[head++];for(int j=0;j<degree[u];j++){int v=adjacency[u][j];if(dist[v]<0){dist[v]=dist[u]+1;ecc=max(ecc,dist[v]);queue[tail++]=v;}}}
  if(tail<N)r.diameter=-1;else if(r.diameter>=0)r.diameter=max(r.diameter,ecc);
  for(int v=0;v<N;v++){int d=dist[v];r.hist[d<0?N:d]++;if(d<0||d>3){r.miss[root]++;ordered_bad++;if(root<v)r.bad++;}if(d<0&&root<v)r.unreachable++;}
 }
 assert(ordered_bad==2*r.bad);
}
void result_json(ostream&o,const Result&r){o<<"{\"n\":172,\"m\":"<<r.edges<<",\"simple\":true,\"min_degree\":"<<r.min_degree<<",\"max_degree\":"<<r.max_degree<<",\"degree6_vertices\":"<<r.degree6<<",\"connected\":"<<(r.unreachable==0?"true":"false")<<",\"diameter\":"<<r.diameter<<",\"bad_unordered_pairs\":"<<r.bad<<",\"unreachable_unordered_pairs\":"<<r.unreachable<<",\"roots_checked\":172}";}
void save_best(const string&base,int edge,int slope,int cursor,const Result&r){
 ofstream edges(base+"/best.edges");edges<<N<<' '<<r.edges<<'\n';int count=0;for(int u=0;u<N;u++)for(int j=0;j<degree[u];j++)if(u<adjacency[u][j]){edges<<u<<' '<<adjacency[u][j]<<'\n';count++;}assert(count==r.edges);
 array<int,E>slopes;slopes.fill(1);slopes[edge]=slope;
 ofstream o(base+"/best.json");o<<"{\"selection\":\"minimum_bad_pairs_among_formal574_nonflat_single_matching_candidates\",\"q\":43,\"vertex_encoding\":\"43*orbit+x\",\"changed_edge\":"<<edge<<",\"slope\":"<<slope<<",\"inverse_slope\":"<<inverse_slope[slope]<<",\"cursor\":"<<cursor<<",\"edge_u\":";arr(o,eu);o<<",\"edge_v\":";arr(o,ev);o<<",\"fixed_intercepts\":";arr(o,bias);o<<",\"slopes\":";arr(o,slopes);o<<",\"score\":";result_json(o,r);o<<",\"root_radius3_missing\":";arr(o,r.miss);o<<",\"ordered_distance_histogram\":{";bool comma=false;for(int d=0;d<=N;d++)if(r.hist[d]){if(comma)o<<',';comma=true;o<<'"'<<(d==N?-1:d)<<"\":"<<r.hist[d];}o<<"},\"degree_histogram\":{\"6\":"<<r.degree6<<",\"7\":"<<N-r.degree6<<"},\"scope\":\"actual full172-root score; no C43 orbit reduction\"}\n";
}
int main(int argc,char**argv){
 assert(argc==3);string base=argv[1];double limit=stod(argv[2]),start=cpu(),bfs_cpu=0;
 ifstream input(base+"/parameters.txt");int count;input>>count;assert(count==E);for(int e=0;e<E;e++){input>>eu[e]>>ev[e]>>bias[e];assert(0<=eu[e]&&eu[e]<ev[e]&&ev[e]<4&&0<=bias[e]&&bias[e]<Q);}assert(input);
 for(int a=1;a<Q;a++){for(int x=1;x<Q;x++)if(a*x%Q==1){inverse_slope[a]=x;break;}assert(inverse_slope[a]);}
 ifstream expected(base+"/first.expected_distances.txt");for(auto&row:expected_first)for(int&d:row)expected>>d;assert(expected);
 ofstream rows(base+"/candidates.jsonl");int processed=0,best=N*N,bestedge=-1,bestslope=-1,nextedge=0,nextslope=2;bool found=false,timeout=false;
 array<int,E>peredge{};array<int,2>edge_counts{};
 for(int edge=0;edge<E&&!found&&!timeout;edge++)for(int slope=2;slope<Q;slope++){
  nextedge=edge;nextslope=slope;if(cpu()-start>=limit){timeout=true;break;}
  auto result=build(edge,slope);double timer=cpu();full_bfs(result);bfs_cpu+=cpu()-timer;
  if(processed==0){for(int r=0;r<N;r++)for(int v=0;v<N;v++)assert(distance_matrix[r][v]==expected_first[r][v]);ofstream o(base+"/first.production_check.json");o<<"{\"formal_cursor\":0,\"changed_edge\":0,\"slope\":2,\"all172x172_distances_equal_independent_Python\":true,\"production_score_reused\":true,\"score\":";result_json(o,result);o<<"}\n";}
  rows<<"{\"cursor\":"<<processed<<",\"changed_edge\":"<<edge<<",\"slope\":"<<slope<<",\"score\":";result_json(rows,result);rows<<"}\n";
  processed++;peredge[edge]++;edge_counts[result.edges-600]++;
  if(result.bad<best){best=result.bad;bestedge=edge;bestslope=slope;save_best(base,edge,slope,processed-1,result);cout<<"BEST cursor="<<processed-1<<" edge="<<edge<<" slope="<<slope<<" bad="<<best<<" D="<<result.diameter<<" m="<<result.edges<<" CPU="<<cpu()-start<<endl;}
  if(result.bad==0){found=true;cout<<"FOUND_D3 edge="<<edge<<" slope="<<slope<<endl;break;}
 }
 rows.close();string status=found?"FOUND_D3":timeout?"CPU_LIMIT_PREFIX_SAVED":"COMPLETE574_NO_D3";if(!found&&!timeout)assert(processed==SCOPE);
 ofstream o(base+"/search.terminal.json");o<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"running\":false,\"scope_candidates\":574,\"processed_candidates\":"<<processed<<",\"production_complete_BFS_roots\":"<<N*processed<<",\"per_matching_candidates\":";arr(o,peredge);o<<",\"m600_candidates\":"<<edge_counts[0]<<",\"m601_candidates\":"<<edge_counts[1]<<",\"minimum_bad_unordered_pairs\":"<<best<<",\"best_matching\":"<<bestedge<<",\"best_slope\":"<<bestslope<<",\"next_position\":";if(timeout)o<<"{\"cursor\":"<<processed<<",\"matching\":"<<nextedge<<",\"slope\":"<<nextslope<<'}';else o<<"null";o<<",\"source_flat_graph_rescored\":false,\"discarded_for_nonregularity\":0,\"C43_root_reduction_used\":false,\"cancelled_shared_class_slope_batch_executed\":false,\"CPU_seconds\":"<<cpu()-start<<",\"all_source_BFS_CPU_seconds\":"<<bfs_cpu<<"}\n";
 cout<<status<<" candidates="<<processed<<" best_bad="<<best<<" CPU="<<cpu()-start<<endl;
}
