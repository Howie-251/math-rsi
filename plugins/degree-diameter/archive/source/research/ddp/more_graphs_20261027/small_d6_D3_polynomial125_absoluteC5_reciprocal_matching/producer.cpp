#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
constexpr int N=125,D=6,TOTAL=4096;
using Coord=array<int,3>;using Kappa=array<int,6>;using Adj=array<array<int,6>,125>;
Adj source,adj;array<int,125> sdeg{};array<int,25> dir{},scalar{};
array<array<int,2>,6> reps={{{0,1},{1,0},{1,1},{1,2},{1,3},{1,4}}};
int inv5[5]={0,1,3,2,4};string out;clock_t began;
int mod(int a){a%=5;if(a<0)a+=5;return a;}
int id(int a,int y,int h){return mod(a)*25+mod(y)+5*mod(h);}
Coord decode(int v){int a=v/25,k=v%25;return {a,k%5,k/5};}
Coord gauge(Coord old){int a=old[0],y=mod(old[1]-3*a*a),h=mod(old[2]-a*a*a-4*a*y);return {a,y,h};}
int gid(Coord old){auto q=gauge(old);return id(q[0],q[1],q[2]);}
bool has(const Adj&A,int u,int v,int degree){for(int k=0;k<degree;k++)if(A[u][k]==v)return true;return false;}
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}
template<class T,size_t S>void ints(ostream&f,const array<T,S>&a){f<<'[';for(size_t i=0;i<S;i++){if(i)f<<',';f<<a[i];}f<<']';}
void save_edges(string name,const Adj&A,int degree){vector<array<int,2>> edges;for(int u=0;u<N;u++)for(int k=0;k<degree;k++){int v=A[u][k];if(u<v)edges.push_back({u,v});}sort(edges.begin(),edges.end());assert(edges.size()==375);ofstream f(out+"/"+name);f<<N<<' '<<edges.size()<<'\n';for(auto e:edges)f<<e[0]<<' '<<e[1]<<'\n';}
void prepare(){
 for(int v=1;v<25;v++){int y=v%5,h=v/5,t=y?y:h;array<int,2> r={mod(y*inv5[t]),mod(h*inv5[t])};auto it=find(reps.begin(),reps.end(),r);assert(it!=reps.end());dir[v]=it-reps.begin();scalar[v]=t;}
 for(int u=0;u<N;u++){
  auto q=decode(u);int a=q[0],y=q[1],h=q[2];
  for(int t=0;t<5;t++){int v=id(a+t,-y-3*t*t,-h+4*t*y+t*t*t);if(v==u){assert(y==0&&h==0&&t==0);continue;}source[u][sdeg[u]++]=v;}
  assert(sdeg[u]==((y==0&&h==0)?4:5));
 }
 int oldedges=0;
 for(int u=0;u<N;u++){for(int k=0;k<sdeg[u];k++){int v=source[u][k];assert(u!=v&&has(source,v,u,sdeg[v]));for(int j=0;j<k;j++)assert(source[u][j]!=v);if(u<v)oldedges++;}}
 assert(oldedges==310);
 ofstream f(out+"/SOURCE_RECIPE.json");f<<"{\"field\":5,\"source_n\":125,\"source_m\":310,\"old_degree_histogram\":{\"4\":5,\"5\":120},\"encoding\":\"a*25+y+5*h\",\"old_neighbor\":\"t=0..4:(a+t,-y-3*t*t,-h+4*t*y+t*t*t) mod5; omit only loops\",\"inverse_old_dart\":\"-t\",\"gauge_from_old\":\"y=b-3*a*a,h=c-a*a*a-4*a*y mod5\",\"directions\":[";
 for(int i=0;i<6;i++){if(i)f<<',';ints(f,reps[i]);}f<<"],\"kappa_domain\":\"each1..4, all4096\",\"new_matching\":\"(a,v)->(a+kappa_L/scalar,-v)\",\"absolute_C5\":\"(a,0,0)->(a+-1,0,0)\",\"representative_roots\":\"a0, vIDs0..24\",\"source_BFS\":0}\n";
 ofstream es(out+"/source125.edges");es<<"125 310\n";for(int u=0;u<N;u++)for(int k=0;k<sdeg[u];k++)if(u<source[u][k])es<<u<<' '<<source[u][k]<<'\n';
}
void build(const Kappa&k){
 adj=source;
 for(int u=0;u<N;u++){
  auto q=decode(u);int a=q[0],y=q[1],h=q[2],v=y+5*h;
  if(v==0){adj[u][4]=id(a+1,0,0);adj[u][5]=id(a-1,0,0);}
  else{int tau=mod(k[dir[v]]*inv5[scalar[v]]);assert(tau!=0);adj[u][5]=id(a+tau,-y,-h);}
 }
 for(int u=0;u<N;u++)for(int i=0;i<6;i++){int v=adj[u][i];assert(v!=u&&has(adj,v,u,6));for(int j=0;j<i;j++)assert(adj[u][j]!=v);}
}
struct Ball{int root,missing,first;array<int,4> hist;array<int,125> d;};
Ball R3(int root){Ball b{};b.root=root;b.d.fill(-1);b.d[root]=0;array<int,N> queue;int begin=0,end=0;queue[end++]=root;while(begin<end){int u=queue[begin++];if(b.d[u]==3)continue;for(int v:adj[u])if(b.d[v]<0){b.d[v]=b.d[u]+1;queue[end++]=v;}}b.first=-1;for(int v=0;v<N;v++){if(b.d[v]<0){b.missing++;if(b.first<0)b.first=v;}else b.hist[b.d[v]]++;}return b;}
void ball_json(ostream&f,const Ball&b){f<<"{\"root\":"<<b.root<<",\"root_coordinates\":";ints(f,decode(b.root));f<<",\"R3_histogram\":";ints(f,b.hist);f<<",\"R3_missing\":"<<b.missing<<",\"first_missing\":";if(b.first<0)f<<"null";else f<<b.first;f<<",\"first_missing_coordinates\":";if(b.first<0)f<<"null";else ints(f,decode(b.first));f<<'}';}
Kappa tuple_at(int index){Kappa k;for(int d=5;d>=0;d--){k[d]=1+index%4;index/=4;}return k;}
void control_prediction(const Ball&root){
 array<array<Coord,4>,4> oldpaths={{{{{0,0,0},{4,3,4},{2,0,4},{0,0,1}}},{{{0,0,0},{1,3,1},{3,0,1},{0,0,4}}},{{{0,0,0},{2,0,0},{4,0,3},{0,0,2}}},{{{0,0,0},{1,0,0},{3,0,2},{0,0,3}}}}};
 bool all=true,vertical=true;ofstream f(out+"/PRED_CONTROL.json");f<<"{\"tuple_index\":12,\"kappa\":[1,1,1,1,4,1],\"paths\":[";
 for(int p=0;p<4;p++){if(p)f<<',';bool ok=true;array<int,4> ids;for(int j=0;j<4;j++)ids[j]=gid(oldpaths[p][j]);for(int j=0;j<3;j++)ok=ok&&has(adj,ids[j],ids[j+1],6);all=all&&ok;f<<"{\"old_coordinates\":[";for(int j=0;j<4;j++){if(j)f<<',';ints(f,oldpaths[p][j]);}f<<"],\"gauge_vertex_ids\":";ints(f,ids);f<<",\"all_edges_present\":"<<(ok?"true":"false")<<'}';}
 f<<"],\"vertical_target_distances\":[";for(int c=1;c<5;c++){if(c>1)f<<',';int target=id(0,0,c);if(root.d[target]<0)vertical=false;f<<"{\"old_c\":"<<c<<",\"vertex\":"<<target<<",\"distance_le3\":";if(root.d[target]<0)f<<"null";else f<<root.d[target];f<<'}';}
 f<<"],\"four_paths_supported\":"<<(all?"true":"false")<<",\"all_four_vertical_targets_R3\":"<<(vertical?"true":"false")<<",\"paths_disposition\":\""<<(all?"SUPPORTED_ACTUAL_CANONICAL_GRAPH":"REFUTED_ACTUAL_CANONICAL_GRAPH")<<"\",\"target_disposition\":\""<<(vertical?"SUPPORTED":"REFUTED")<<"\",\"root0_R3_missing\":"<<root.missing<<",\"extra_BFS\":0}\n";assert(!all||vertical);
}
int main(int argc,char**argv){assert(argc==4);out=argv[1];double soft=stod(argv[2]);int hard=stoi(argv[3]);rlimit limit{(rlim_t)hard,(rlim_t)hard};assert(setrlimit(RLIMIT_CPU,&limit)==0);began=clock();prepare();
 vector<int> order{12};for(int i=0;i<TOTAL;i++)if(i!=12)order.push_back(i);assert(order.size()==TOTAL);
 int completed=0,rootchecks=0;bool hit=false,limited=false;ofstream cases(out+"/CASES.jsonl");
 for(int ordinal=0;ordinal<TOTAL;ordinal++){
  if(cpu()>=soft){limited=true;break;}int index=order[ordinal];Kappa k=tuple_at(index);build(k);vector<Ball> tested;bool passed=true;
  for(int root=0;root<25;root++){Ball b=R3(root);tested.push_back(b);rootchecks++;if(index==12&&root==0)control_prediction(b);if(b.missing){passed=false;break;}}
  completed++;cases<<"{\"ordinal\":"<<ordinal<<",\"tuple_index\":"<<index<<",\"kappa\":";ints(cases,k);cases<<",\"roots_checked\":"<<tested.size()<<",\"root_records\":[";for(size_t j=0;j<tested.size();j++){if(j)cases<<',';ball_json(cases,tested[j]);}cases<<"],\"status\":\""<<(passed?"HIT_D3_PENDING_PARENT":"REPRESENTATIVE_ROOT_R3_FAIL")<<"\",\"actual_global_D\":"<<(passed?"3":"null")<<",\"ordinary_bad_unordered_pairs\":null}\n";
  if(passed){hit=true;save_edges("candidate125.edges",adj,6);ofstream h(out+"/HIT.json");h<<"{\"n\":125,\"m\":375,\"degree\":6,\"D\":3,\"tuple_index\":"<<index<<",\"kappa\":";ints(h,k);h<<",\"all25_translation_orbit_roots_R3\":true,\"parent_independent_acceptance_pending\":true}\n";}
  if((ordinal%64)==0||hit){cases.flush();ofstream cp(out+"/checkpoint.json");cp<<"{\"status\":\""<<(hit?"HIT":"RUNNING")<<"\",\"completed\":"<<completed<<",\"total\":4096,\"last_tuple_index\":"<<index<<",\"root_R3_checks\":"<<rootchecks<<",\"CPU_seconds\":"<<cpu()<<"}\n";}
  if(hit)break;
 }
 string status=hit?"HIT_STOP_REMAINDER_UNTESTED":limited?"CPU_LIMIT_PREFIX_NO_HIT":"COMPLETE_ALL4096_NO_HIT";
 ofstream r(out+"/NATIVE_RESULT.json");r<<"{\"status\":\""<<status<<"\",\"prediction\":\""<<(hit?"JOINT_SUPPORTED_PRODUCER_PENDING_PARENT":limited?"JOINT_UNKNOWN_INCOMPLETE":"JOINT_REFUTED_COMPLETE_FIXED_FAMILY")<<"\",\"n\":125,\"m\":375,\"degree\":6,\"target_D\":3,\"savedL\":120,\"planned\":4096,\"completed\":"<<completed<<",\"untested\":"<<TOTAL-completed<<",\"actual_candidate_graphs\":"<<completed<<",\"representative_root_R3_checks\":"<<rootchecks<<",\"hits\":"<<(hit?1:0)<<",\"actual_global_D\":"<<(hit?"3":"null")<<",\"ordinary_bad_unordered_pairs\":null,\"source_BFS\":0,\"fullglobalD_BFS\":0,\"solver_calls\":0,\"native_CPU_seconds\":"<<cpu()<<",\"rule_variants\":0}\n";cout<<status<<" completed "<<completed<<" rootchecks "<<rootchecks<<" CPU "<<cpu()<<endl;
}
