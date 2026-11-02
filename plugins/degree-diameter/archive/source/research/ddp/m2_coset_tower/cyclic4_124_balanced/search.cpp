#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
constexpr int Q=31,K=4,N=124,D=6,E=12;
using State=array<int,E>;
array<int,E> eu{},ev{};
array<int,3> tree_edges{};
array<int,9> free_edges{};
int expected_first_adjacency[N][D];
int expected_first_distances[K][N];
int su[E],sv[E],adj[N][D],distance_rows[K][N],queue_vertices[N];
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
template<class T>void list(ostream&o,const T&v){o<<'[';bool c=false;for(auto x:v){if(c)o<<',';c=true;o<<x;}o<<']';}
struct Score{int sum=0,diameter=0;array<int,K>missing{},ecc{},reached{};};
struct Position{int start=0,segment=0,step=0,coordinate=-1,value=-1;string phase="initial";};
void posout(ostream&o,const Position&p){o<<"{\"start\":"<<p.start<<",\"segment\":"<<p.segment<<",\"descent_step\":"<<p.step<<",\"coordinate_edge\":"<<p.coordinate<<",\"trial_value\":"<<p.value<<",\"phase\":\""<<p.phase<<"\"}";}
bool legal(const State&v){
 for(int e:tree_edges)if(v[e]!=0)return false;
 for(int e=0;e<E;e++){
  if(v[e]<0||v[e]>=Q)return false;
  if(eu[e]==ev[e]&&v[e]==0)return false;
  for(int f=e+1;f<E;f++)if(eu[e]==eu[f]&&ev[e]==ev[f]){
   if(v[e]==v[f])return false;
   if(eu[e]==ev[e]&&(v[e]+v[f])%Q==0)return false;
  }
 }
 return true;
}
void init(const string&base){
 ifstream input(base+"/topology.txt");int edges,trees;input>>edges>>trees;assert(edges==E&&trees==3);
 for(int e=0;e<E;e++){input>>eu[e]>>ev[e];assert(0<=eu[e]&&eu[e]<=ev[e]&&ev[e]<K);}
 array<int,K>parent{0,1,2,3};array<bool,E>istree{};
 auto find=[&](int x){while(parent[x]!=x)x=parent[x];return x;};
 for(int&e:tree_edges){input>>e;assert(0<=e&&e<E&&!istree[e]&&eu[e]!=ev[e]);istree[e]=true;int a=find(eu[e]),b=find(ev[e]);assert(a!=b);parent[a]=b;}
 assert(input);for(int i=1;i<K;i++)assert(find(i)==find(0));
 for(int e=0,k=0;e<E;e++)if(!istree[e])free_edges[k++]=e;
 array<int,K>degree{};for(int e=0;e<E;e++){su[e]=degree[eu[e]]++;sv[e]=degree[ev[e]]++;if(eu[e]==ev[e])assert(su[e]!=sv[e]);}for(int d:degree)assert(d==D);
}
void build(const State&v){
 for(int e=0;e<E;e++)for(int x=0;x<Q;x++){
  int y=x+v[e];if(y>=Q)y-=Q;int a=eu[e]*Q+x,b=ev[e]*Q+y;
  adj[a][su[e]]=b;adj[b][sv[e]]=a;
 }
}
Score full_four_bfs(const State&v){
 build(v);Score s;
 for(int root=0;root<K;root++){
  int*dist=distance_rows[root];fill(dist,dist+N,-1);int front=0,tail=1,within3=1,ecc=0;
  dist[root*Q]=0;queue_vertices[0]=root*Q;
  while(front<tail){int u=queue_vertices[front++],depth=dist[u]+1;
   for(int z:adj[u])if(dist[z]<0){dist[z]=depth;queue_vertices[tail++]=z;within3+=depth<=3;ecc=depth;}
  }
  s.missing[root]=N-within3;s.ecc[root]=tail==N?ecc:-1;s.reached[root]=tail;s.sum+=s.missing[root];
  if(s.diameter>=0)s.diameter=tail==N?max(s.diameter,ecc):-1;
 }
 assert((Q*s.sum)%2==0);return s;
}
void scoreout(ostream&o,const Score&s){o<<"{\"root_misses\":";list(o,s.missing);o<<",\"score_sum\":"<<s.sum<<",\"bad_unordered_pairs\":"<<Q*s.sum/2<<",\"diameter\":"<<s.diameter<<",\"eccentricities\":";list(o,s.ecc);o<<",\"roots_reached\":";list(o,s.reached);o<<'}';}
void save_best(const string&base,const State&v,const Score&s,const Position&p,uint64_t evaluations){
 ofstream f(base+"/best.edges");f<<N<<' '<<N*D/2<<'\n';int count=0;
 for(int u=0;u<N;u++)for(int w:adj[u])if(u<w){f<<u<<' '<<w<<'\n';count++;}assert(count==372);
 ofstream out(base+"/best.json");out<<"{\"selection\":\"minimum_sum_of_four_root_deficits_among_evaluated_states\",\"n\":124,\"m\":372,\"degree\":6,\"q\":31,\"vertex_encoding\":\"31*orbit+x; orbit=0,1,2,3\",\"edge_u\":";list(out,eu);out<<",\"edge_v\":";list(out,ev);out<<",\"tree_edge_indices\":";list(out,tree_edges);out<<",\"free_edge_indices\":";list(out,free_edges);out<<",\"voltages\":";list(out,v);out<<",\"score\":";scoreout(out,s);out<<",\"evaluation_index\":"<<evaluations<<",\"position\":";posout(out,p);out<<",\"root_distance_histograms\":[";
 for(int r=0;r<K;r++){if(r)out<<',';map<int,int>h;for(int d:distance_rows[r])h[d]++;out<<'{';bool comma=false;for(auto[d,c]:h){if(comma)out<<',';comma=true;out<<'\"'<<d<<"\":"<<c;}out<<'}';}out<<"]}\n";
}
int main(int argc,char**argv){
 assert(argc==3);string base=argv[1];double limit=stod(argv[2]),started=cpu(),bfs_cpu=0;init(base);
 constexpr uint64_t rng_seed=20261026461ULL;mt19937_64 rng(rng_seed);uniform_int_distribution<int>voltage(0,Q-1);
 vector<State>starts(64);ifstream input(base+"/starts.txt");int declared;input>>declared;assert(declared==64);set<State>used;
 for(auto&v:starts){for(int&x:v)input>>x;assert(legal(v)&&used.insert(v).second);}assert(input);
 ifstream expected(base+"/first.expected_distances.txt");for(auto&row:expected_first_distances)for(int&d:row)expected>>d;assert(expected);
 ifstream expected_adj(base+"/first.expected_adjacency.txt");for(auto&row:expected_first_adjacency)for(int&v:row)expected_adj>>v;assert(expected_adj);
 uint64_t evaluations=0,neighborhoods=0,moves=0,kicks=0,illegal_trials=0,trial_slots=0;int global_best=N*K+1,completed_starts=0,completed_segments=0;bool found=false,timeout=false;
 Position position;State current{},trial{},winner{};Score current_score,winner_score;int current_start_moves=0;
 vector<int>start_min(64,N*K+1),start_evaluations(64,0),start_segments(64,0),start_moves(64,0);
 ofstream events(base+"/events.jsonl");
 auto evaluate=[&](const State&v,Score&result)->bool{
  if(cpu()-started>=limit){timeout=true;return false;}
  assert(legal(v));double begin=cpu();result=full_four_bfs(v);bfs_cpu+=cpu()-begin;evaluations++;start_evaluations[position.start]++;start_min[position.start]=min(start_min[position.start],result.sum);
  if(result.sum<global_best){global_best=result.sum;save_best(base,v,result,position,evaluations);cout<<"BEST evaluation="<<evaluations<<" sum="<<global_best<<" bad="<<Q*global_best/2<<" D="<<result.diameter<<" CPU="<<cpu()-started<<endl;}
  if(evaluations==1){for(int u=0;u<N;u++){array<int,D> row;copy(adj[u],adj[u]+D,row.begin());sort(row.begin(),row.end());for(int j=0;j<D;j++)assert(row[j]==expected_first_adjacency[u][j]);}for(int r=0;r<K;r++)for(int x=0;x<N;x++)assert(distance_rows[r][x]==expected_first_distances[r][x]);ofstream out(base+"/first.four_root_check.json");out<<"{\"scope\":\"first formal random start; C++ score reused in production\",\"all_adjacency_rows_match_independent_Python\":true,\"all_four_distance_arrays_match_independent_Python\":true,\"score\":";scoreout(out,result);out<<"}\n";}
  if(result.sum==0){found=true;return false;}
  if(evaluations==1000||evaluations%100000==0){ofstream f(base+"/progress.json");f<<setprecision(12)<<"{\"evaluations\":"<<evaluations<<",\"complete_root_BFS_runs\":"<<4*evaluations<<",\"best_score_sum\":"<<global_best<<",\"CPU_seconds\":"<<cpu()-started<<",\"position\":";posout(f,position);f<<"}\n";cout<<"PROGRESS evaluations="<<evaluations<<" best="<<global_best<<" CPU="<<cpu()-started<<endl;}
  return true;
 };
 for(int start=0;start<64;start++){
  position={start,0,0,-1,-1,"initial"};current=starts[start];current_start_moves=0;
  if(!evaluate(current,current_score))goto done;

  for(int segment=0;segment<9;segment++){
   position.segment=segment;
   if(segment){
    position.phase="two_coordinate_kick";position.step=0;position.coordinate=-1;position.value=-1;
    int a=rng()%free_edges.size(),b;do{b=rng()%free_edges.size();}while(b==a);
    for(int k:{a,b}){int e=free_edges[k],old=current[e];do{current[e]=voltage(rng);}while(current[e]==old||!legal(current));}
    kicks++;if(!evaluate(current,current_score))goto done;
   }
   for(int step=0;step<30;step++){
    position.step=step;position.phase="full_single_coordinate_neighborhood";winner=current;winner_score=current_score;
    for(int e:free_edges)for(int x=0;x<Q;x++){
     if(x==current[e])continue;position.coordinate=e;position.value=x;trial_slots++;trial=current;trial[e]=x;
     if(!legal(trial)){illegal_trials++;continue;}
     Score result;if(!evaluate(trial,result))goto done;
     if(result.sum<winner_score.sum){winner=trial;winner_score=result;}
    }
    neighborhoods++;
    if(winner_score.sum>=current_score.sum)break;
    current=winner;current_score=winner_score;moves++;current_start_moves++;start_moves[start]++;
    events<<"{\"event\":\"strict_coordinate_move\",\"start\":"<<start<<",\"segment\":"<<segment<<",\"step\":"<<step<<",\"score\":"<<current_score.sum<<",\"voltages\":";list(events,current);events<<"}\n";
   }
   completed_segments++;start_segments[start]++;
  }
  completed_starts++;cout<<"START_COMPLETE index="<<start<<" evaluations="<<start_evaluations[start]<<" best="<<start_min[start]<<" moves="<<current_start_moves<<" CPU="<<cpu()-started<<endl;
 }
done:
 string status=found?"FOUND_D3":timeout?"CPU_LIMIT_INCOMPLETE":"COMPLETE_BOUNDED_SEARCH_NO_SOLUTION";
 ofstream out(base+"/search.terminal.json");out<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"scope\":\"fixed K4 double matching cyclic31 lift;64 fixed random starts; at most9 segments/start and30 strict coordinate moves/segment\",\"rng_seed\":"<<rng_seed<<",\"planned_starts\":64,\"completed_starts\":"<<completed_starts<<",\"completed_segments\":"<<completed_segments<<",\"legal_states_evaluated\":"<<evaluations<<",\"complete_root_BFS_runs\":"<<4*evaluations<<",\"complete_single_coordinate_neighborhoods\":"<<neighborhoods<<",\"strict_coordinate_moves\":"<<moves<<",\"two_coordinate_kicks\":"<<kicks<<",\"coordinate_trial_slots\":"<<trial_slots<<",\"illegal_loop_or_parallel_trials\":"<<illegal_trials<<",\"minimum_score_sum\":"<<global_best<<",\"minimum_bad_unordered_pairs\":"<<Q*global_best/2<<",\"next_position\":";
 if(timeout)posout(out,position);else out<<"null";
 out<<",\"current_state\":";list(out,current);out<<",\"current_score\":";scoreout(out,current_score);out<<",\"staged_best_neighbor\":";list(out,winner);out<<",\"per_start\":[";
 for(int i=0;i<64;i++){if(i)out<<',';out<<"{\"start\":"<<i<<",\"evaluations\":"<<start_evaluations[i]<<",\"completed_segments\":"<<start_segments[i]<<",\"moves\":"<<start_moves[i]<<",\"minimum_score\":";if(start_evaluations[i])out<<start_min[i];else out<<"null";out<<'}';}
 out<<"],\"CPU_seconds\":"<<cpu()-started<<",\"complete_four_root_BFS_CPU_seconds\":"<<bfs_cpu<<",\"running\":false,\"family_exhausted\":false}\n";
 if(timeout){ofstream f(base+"/rng.cursor.txt");f<<rng<<'\n';}
 cout<<status<<" evaluations="<<evaluations<<" best="<<global_best<<" CPU="<<cpu()-started<<endl;
}
