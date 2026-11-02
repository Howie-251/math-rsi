#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
using namespace std;
constexpr int Q=43,K=4,N=172,D=7,E=14;
using State=array<int,E>;
const array<int,E>eu{0,0,0,2,2,2,0,0,1,1,0,0,1,1};
const array<int,E>ev{1,1,1,3,3,3,2,2,3,3,3,3,2,2};
const array<int,11>free_edges{1,2,3,4,5,7,8,9,11,12,13};
int su[E],sv[E],adj[N][D],distance_rows[K][N],queue_vertices[N],best_distances[K][N];
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
template<class T>void list(ostream&o,const T&v){o<<'[';bool c=false;for(auto x:v){if(c)o<<',';c=true;o<<x;}o<<']';}
struct Score{int sum=0,diameter=0;array<int,K>missing{},ecc{},reached{};};
bool legal(const State&v){if(v[0]!=0||v[6]!=0||v[10]!=0)return false;for(int e=0;e<E;++e)for(int f=e+1;f<E;++f)if(eu[e]==eu[f]&&ev[e]==ev[f]&&v[e]==v[f])return false;return true;}
void init(){array<int,K>degree{};for(int e=0;e<E;++e){su[e]=degree[eu[e]]++;sv[e]=degree[ev[e]]++;}for(int d:degree)assert(d==D);}
void build(const State&v){for(int e=0;e<E;++e)for(int x=0;x<Q;++x){int y=x+v[e];if(y>=Q)y-=Q;int a=eu[e]*Q+x,b=ev[e]*Q+y;adj[a][su[e]]=b;adj[b][sv[e]]=a;}}
Score full_four_bfs(const State&v){build(v);Score s;for(int root=0;root<K;++root){int*dist=distance_rows[root];fill(dist,dist+N,-1);int front=0,tail=1,within3=1,ecc=0;dist[root*Q]=0;queue_vertices[0]=root*Q;while(front<tail){int u=queue_vertices[front++],depth=dist[u]+1;for(int z:adj[u])if(dist[z]<0){dist[z]=depth;queue_vertices[tail++]=z;within3+=depth<=3;ecc=depth;}}s.missing[root]=N-within3;s.ecc[root]=tail==N?ecc:-1;s.reached[root]=tail;s.sum+=s.missing[root];if(s.diameter>=0)s.diameter=tail==N?max(s.diameter,ecc):-1;}assert((Q*s.sum)%2==0);return s;}
void scoreout(ostream&o,const Score&s){o<<"{\"root_misses\":";list(o,s.missing);o<<",\"score_sum\":"<<s.sum<<",\"bad_unordered_pairs\":"<<Q*s.sum/2<<",\"diameter\":"<<s.diameter<<",\"eccentricities\":";list(o,s.ecc);o<<",\"roots_reached\":";list(o,s.reached);o<<'}';}
struct Position{int round=-1;array<int,3>edges{-1,-1,-1},values{-1,-1,-1};};
void positionout(ostream&o,const Position&p){o<<"{\"round\":"<<p.round<<",\"edges\":";list(o,p.edges);o<<",\"values\":";list(o,p.values);o<<'}';}
void save_best(const string&base,const State&v,const Score&s,const Position&p,uint64_t evaluations){build(v);ofstream edges(base+"/best.edges");edges<<N<<" 602\n";int count=0;for(int u=0;u<N;++u)for(int w:adj[u])if(u<w){edges<<u<<' '<<w<<'\n';count++;}assert(count==602);ofstream o(base+"/best.json");o<<"{\"n\":172,\"m\":602,\"degree\":7,\"q\":43,\"vertex_encoding\":\"43*orbit+x\",\"edge_u\":";list(o,eu);o<<",\"edge_v\":";list(o,ev);o<<",\"voltages\":";list(o,v);o<<",\"score\":";scoreout(o,s);o<<",\"position\":";positionout(o,p);o<<",\"evaluated_at\":"<<evaluations<<",\"root_distance_histograms\":[";for(int r=0;r<K;++r){if(r)o<<',';map<int,int>h;for(int d:best_distances[r])h[d]++;o<<'{';bool comma=false;for(auto[d,c]:h){if(comma)o<<',';comma=true;o<<'"'<<d<<"\":"<<c;}o<<'}';}o<<"],\"selection\":\"best actually evaluated state in the one fixed three-coordinate descent trajectory\"}\n";}
int main(int argc,char**argv){assert(argc==3);string base=argv[1];double limit=stod(argv[2]),began=cpu();init();State seed{};ifstream input(base+"/seed.txt");for(int&x:seed)input>>x;assert(input&&legal(seed));
 State current=seed,best=seed,winner=seed;Score current_score,best_score,winner_score;Position position,best_position;bool found=false,timeout=false,minimum=false;uint64_t raw=0,illegal=0,evaluations=0,best_evaluation=0;int complete_rounds=0,moves=0;
 auto evaluate=[&](const State&v){Score s=full_four_bfs(v);evaluations++;if(evaluations==1||s.sum<best_score.sum){best=v;best_score=s;best_position=position;best_evaluation=evaluations;for(int r=0;r<K;++r)copy(distance_rows[r],distance_rows[r]+N,best_distances[r]);cout<<"BEST score="<<s.sum<<" bad="<<Q*s.sum/2<<" round="<<position.round<<" raw="<<raw<<" CPU="<<cpu()-began<<endl;}if(!s.sum)found=true;return s;};
 auto progress=[&](){ofstream o(base+"/progress.json");o<<setprecision(12)<<"{\"raw_slots\":"<<raw<<",\"illegal_slots\":"<<illegal<<",\"actual_legal_neighbor_candidates\":"<<evaluations-1<<",\"complete_root_BFS_runs\":"<<4*evaluations<<",\"best_score\":"<<best_score.sum<<",\"CPU_seconds\":"<<cpu()-began<<",\"position\":";positionout(o,position);o<<"}\n";cout<<"PROGRESS raw="<<raw<<" legal="<<evaluations-1<<" best="<<best_score.sum<<" CPU="<<cpu()-began<<endl;};
 current_score=evaluate(seed);assert((current_score.missing==array<int,K>{2,5,3,2})&&current_score.sum==12&&current_score.diameter==4);{ofstream o(base+"/seed_calibration.json");o<<"{\"source_seed_reused_as_initial_score\":true,\"voltages\":";list(o,seed);o<<",\"score\":";scoreout(o,current_score);o<<",\"complete_root_BFS_runs\":4}\n";}
 ofstream rounds(base+"/rounds.jsonl");
 for(int round=0;round<5&&!found&&!timeout;++round){position.round=round;winner=current;winner_score=current_score;uint64_t raw_before=raw,illegal_before=illegal,eval_before=evaluations;double round_start=cpu();
  for(int a=0;a<11&&!found&&!timeout;++a)for(int b=a+1;b<11&&!found&&!timeout;++b)for(int c=b+1;c<11&&!found&&!timeout;++c){int ea=free_edges[a],eb=free_edges[b],ec=free_edges[c];position.edges={ea,eb,ec};
   for(int x=0;x<Q&&!found&&!timeout;++x){if(x==current[ea])continue;for(int y=0;y<Q&&!found&&!timeout;++y){if(y==current[eb])continue;for(int z=0;z<Q;++z){if(z==current[ec])continue;position.values={x,y,z};if((raw&1023)==0&&cpu()-began>=limit){timeout=true;break;}raw++;State trial=current;trial[ea]=x;trial[eb]=y;trial[ec]=z;
    if(!legal(trial))illegal++;else{Score s=evaluate(trial);if(s.sum<winner_score.sum){winner=trial;winner_score=s;}if(found)break;}
    if(raw==100000||raw%1000000==0)progress();
   }}}
  }
  bool complete=!found&&!timeout;if(complete){complete_rounds++;assert(raw-raw_before==12224520&&illegal-illegal_before==1136418&&evaluations-eval_before==11088102);}
  string stop=found?"FOUND_D3":timeout?"CPU_LIMIT":winner_score.sum<current_score.sum?"STRICT_IMPROVEMENT":"THREE_COORDINATE_MINIMUM";
  rounds<<"{\"round\":"<<round<<",\"complete_neighborhood\":"<<(complete?"true":"false")<<",\"raw_slots\":"<<raw-raw_before<<",\"illegal_parallel_collisions\":"<<illegal-illegal_before<<",\"legal_candidates_scored\":"<<evaluations-eval_before<<",\"initial_score\":"<<current_score.sum<<",\"best_neighbor_score\":"<<winner_score.sum<<",\"stop\":\""<<stop<<"\",\"winner_voltages\":";list(rounds,winner);rounds<<",\"CPU_seconds\":"<<cpu()-round_start<<"}\n";rounds.flush();cout<<"ROUND "<<round<<" complete="<<complete<<" old="<<current_score.sum<<" next="<<winner_score.sum<<" raw="<<raw-raw_before<<" CPU="<<cpu()-began<<endl;progress();
  if(found||timeout)break;if(winner_score.sum>=current_score.sum){minimum=true;break;}current=winner;current_score=winner_score;moves++;
 }
 save_best(base,best,best_score,best_position,best_evaluation);string status=found?"FOUND_D3":timeout?"CPU_LIMIT_PREFIX_SAVED":minimum?"COMPLETE_THREE_COORDINATE_LOCAL_MINIMUM":"FIVE_ROUND_LIMIT";
 ofstream o(base+"/terminal.json");o<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"running\":false,\"fixed_start_count\":1,\"maximum_rounds\":5,\"complete_rounds\":"<<complete_rounds<<",\"accepted_strict_moves\":"<<moves<<",\"raw_neighbor_slots\":"<<raw<<",\"illegal_parallel_collisions\":"<<illegal<<",\"actual_legal_neighbor_BFS_candidates\":"<<evaluations-1<<",\"total_legal_candidates_scored_including_seed\":"<<evaluations<<",\"complete_root_BFS_runs\":"<<4*evaluations<<",\"best_score\":";scoreout(o,best_score);o<<",\"best_voltages\":";list(o,best);o<<",\"next_position\":";if(timeout)positionout(o,position);else o<<"null";o<<",\"last_position\":";positionout(o,position);o<<",\"current_state\":";list(o,current);o<<",\"staged_best_neighbor\":";list(o,winner);o<<",\"CPU_seconds\":"<<cpu()-began<<",\"family_exhausted\":false,\"pending\":[\"parent-owned final verification, unless exact reuse of original best\"]}\n";o.close();cout<<status<<" best="<<best_score.sum<<" raw="<<raw<<" evaluations="<<evaluations<<" CPU="<<cpu()-began<<endl;
}
