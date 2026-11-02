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
constexpr int Q=43,K=4,N=172,D=7,E=14;
using State=array<int,E>;
const array<int,E> eu{0,0,0,0,2,2,2,2,0,0,1,1,0,1};
const array<int,E> ev{1,1,1,1,3,3,3,3,2,2,3,3,3,2};
const array<int,11> free_edges{1,2,3,4,5,6,7,9,10,11,13};
const State seed{0,4,11,37,16,34,30,42,0,24,18,37,0,18};
int su[E],sv[E],adj[N][D],distance_rows[K][N],queue_vertices[N];
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
template<class T>void list(ostream&o,const T&v){o<<'[';bool c=false;for(auto x:v){if(c)o<<',';c=true;o<<x;}o<<']';}
struct Score{int sum=0,diameter=0;array<int,K>missing{},ecc{},reached{};};
struct Position{int start=0,segment=0,step=0,coordinate=-1,value=-1;string phase="initial";};
void posout(ostream&o,const Position&p){o<<"{\"start\":"<<p.start<<",\"segment\":"<<p.segment<<",\"descent_step\":"<<p.step<<",\"coordinate_edge\":"<<p.coordinate<<",\"trial_value\":"<<p.value<<",\"phase\":\""<<p.phase<<"\"}";}
bool legal(const State&v){
 if(v[0]!=0||v[8]!=0||v[12]!=0)return false;
 for(int e=0;e<E;e++)for(int f=e+1;f<E;f++)if(eu[e]==eu[f]&&ev[e]==ev[f]&&v[e]==v[f])return false;
 return true;
}
void init(){array<int,K>degree{};for(int e=0;e<E;e++){su[e]=degree[eu[e]]++;sv[e]=degree[ev[e]]++;}for(int d:degree)assert(d==D);}
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
 for(int u=0;u<N;u++)for(int w:adj[u])if(u<w){f<<u<<' '<<w<<'\n';count++;}assert(count==602);
 ofstream out(base+"/best.json");out<<"{\"selection\":\"minimum_sum_of_four_root_deficits_among_evaluated_states\",\"n\":172,\"m\":602,\"degree\":7,\"q\":43,\"vertex_encoding\":\"43*orbit+x; orbit=A0,A1,B0,B1\",\"edge_u\":";list(out,eu);out<<",\"edge_v\":";list(out,ev);out<<",\"voltages\":";list(out,v);out<<",\"score\":";scoreout(out,s);out<<",\"evaluation_index\":"<<evaluations<<",\"position\":";posout(out,p);out<<",\"root_distance_histograms\":[";
 for(int r=0;r<K;r++){if(r)out<<',';map<int,int>h;for(int d:distance_rows[r])h[d]++;out<<'{';bool comma=false;for(auto[d,c]:h){if(comma)out<<',';comma=true;out<<'\"'<<d<<"\":"<<c;}out<<'}';}out<<"]}\n";
}
int main(int argc,char**argv){
 assert(argc==3);string base=argv[1];double limit=stod(argv[2]),started=cpu(),bfs_cpu=0;init();assert(legal(seed));
 constexpr uint64_t rng_seed=20261026172ULL;mt19937_64 rng(rng_seed);uniform_int_distribution<int>voltage(0,Q-1);
 vector<State>starts{seed};set<State>used{seed};
 while(starts.size()<33){State v{};for(int e:free_edges){bool collision;do{v[e]=voltage(rng);collision=false;for(int f=0;f<e;f++)if(eu[e]==eu[f]&&ev[e]==ev[f]&&v[e]==v[f])collision=true;}while(collision);}if(legal(v)&&used.insert(v).second)starts.push_back(v);}
 {ofstream out(base+"/starts.json");out<<"{\"rng_seed\":"<<rng_seed<<",\"states\":[";for(int i=0;i<33;i++){if(i)out<<',';list(out,starts[i]);}out<<"]}\n";}
 uint64_t evaluations=0,neighborhoods=0,moves=0,kicks=0,illegal_trials=0,trial_slots=0;int global_best=N*K+1,completed_starts=0,completed_segments=0;bool found=false,timeout=false;
 Position position;State current=seed,trial=seed,winner=seed;Score current_score,winner_score;int current_start_moves=0;
 vector<int>start_min(33,N*K+1),start_evaluations(33,0),start_segments(33,0),start_moves(33,0);
 ofstream events(base+"/events.jsonl");
 auto evaluate=[&](const State&v,Score&result)->bool{
  if(cpu()-started>=limit){timeout=true;return false;}
  assert(legal(v));double begin=cpu();result=full_four_bfs(v);bfs_cpu+=cpu()-begin;evaluations++;start_evaluations[position.start]++;start_min[position.start]=min(start_min[position.start],result.sum);
  if(result.sum<global_best){global_best=result.sum;save_best(base,v,result,position,evaluations);cout<<"BEST evaluation="<<evaluations<<" sum="<<global_best<<" bad="<<Q*global_best/2<<" D="<<result.diameter<<" CPU="<<cpu()-started<<endl;}
  if(result.sum==0){found=true;return false;}
  if(evaluations==1000||evaluations%100000==0){ofstream f(base+"/progress.json");f<<setprecision(12)<<"{\"evaluations\":"<<evaluations<<",\"complete_root_BFS_runs\":"<<4*evaluations<<",\"best_score_sum\":"<<global_best<<",\"CPU_seconds\":"<<cpu()-started<<",\"position\":";posout(f,position);f<<"}\n";cout<<"PROGRESS evaluations="<<evaluations<<" best="<<global_best<<" CPU="<<cpu()-started<<endl;}
  return true;
 };
 for(int start=0;start<33;start++){
  position={start,0,0,-1,-1,"initial"};current=starts[start];current_start_moves=0;
  if(!evaluate(current,current_score))goto done;
  if(start==0){assert((current_score.missing==array<int,K>{6,6,10,10})&&current_score.diameter==4);ofstream out(base+"/seed_four_root_check.json");out<<"{\"scope\":\"one diagnostic initial state, reused as production seed score\",\"voltages\":";list(out,current);out<<",\"score\":";scoreout(out,current_score);out<<",\"expected_old_bad_pairs\":688,\"matched\":true}\n";}
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
 ofstream out(base+"/search.terminal.json");out<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"scope\":\"fixed four-node multiplicity421 cyclic43 lift; old seed plus32 fixed random starts; at most9 segments/start and30 strict coordinate moves/segment\",\"rng_seed\":"<<rng_seed<<",\"planned_starts\":33,\"completed_starts\":"<<completed_starts<<",\"completed_segments\":"<<completed_segments<<",\"legal_states_evaluated\":"<<evaluations<<",\"complete_root_BFS_runs\":"<<4*evaluations<<",\"complete_single_coordinate_neighborhoods\":"<<neighborhoods<<",\"strict_coordinate_moves\":"<<moves<<",\"two_coordinate_kicks\":"<<kicks<<",\"coordinate_trial_slots\":"<<trial_slots<<",\"illegal_duplicate_parallel_trials\":"<<illegal_trials<<",\"minimum_score_sum\":"<<global_best<<",\"minimum_bad_unordered_pairs\":"<<Q*global_best/2<<",\"next_position\":";
 if(timeout)posout(out,position);else out<<"null";
 out<<",\"current_state\":";list(out,current);out<<",\"current_score\":";scoreout(out,current_score);out<<",\"staged_best_neighbor\":";list(out,winner);out<<",\"per_start\":[";
 for(int i=0;i<33;i++){if(i)out<<',';out<<"{\"start\":"<<i<<",\"evaluations\":"<<start_evaluations[i]<<",\"completed_segments\":"<<start_segments[i]<<",\"moves\":"<<start_moves[i]<<",\"minimum_score\":";if(start_evaluations[i])out<<start_min[i];else out<<"null";out<<'}';}
 out<<"],\"CPU_seconds\":"<<cpu()-started<<",\"complete_four_root_BFS_CPU_seconds\":"<<bfs_cpu<<",\"running\":false,\"family_exhausted\":false}\n";
 if(timeout){ofstream f(base+"/rng.cursor.txt");f<<rng<<'\n';}
 cout<<status<<" evaluations="<<evaluations<<" best="<<global_best<<" CPU="<<cpu()-started<<endl;
}
