// One bounded exact search of the stated cyclically homogeneous six-fiber family.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using Perm=std::array<int,10>;using Rows=std::array<unsigned,10>;using Graph=std::array<uint64_t,60>;
struct Input{int config,li,ri;Perm sl,sr;Rows z,y;};
struct Stats{long long inputs=0,left_feasible=0,right_feasible=0,left_solutions=0,right_solutions=0,graphs=0;};
clock_t began;bool timeout=false,target=false;long long nodes=0,leaves=0;constexpr unsigned all10=1023;
bool limit(){if(double(clock()-began)/CLOCKS_PER_SEC>=10){timeout=true;return true;}return false;}
Rows transpose(const Rows&a){Rows b{};for(int i=0;i<10;i++)for(int j=0;j<10;j++)if(a[i]>>j&1)b[j]|=1U<<i;return b;}
Rows residual(const Rows&a,const Rows&b){Rows r{};for(int i=0;i<10;i++)for(int j=0;j<10;j++){int x=__builtin_popcount(a[i]&b[j]);assert(x<=1);if(!x)r[i]|=1U<<j;}for(auto x:r)assert(__builtin_popcount(x)==4);for(auto x:transpose(r))assert(__builtin_popcount(x)==4);return r;}
struct Solver{
 const Perm&s;const Rows&r;Perm m{};Rows allowed{};std::vector<Perm>solutions;
 Solver(const Perm&ss,const Rows&rr):s(ss),r(rr){m.fill(-1);for(int u=0;u<10;u++)for(int v=0;v<10;v++)if(v!=u&&(r[u]>>v&1)&&(r[s[u]]>>v&1)&&(r[u]>>s[v]&1))allowed[u]|=1U<<v;}
 bool partial(){for(int u=0;u<10;u++)if(m[u]>=0){int v=m[u];if(m[s[u]]>=0&&m[s[u]]==s[v])return false;if(m[v]>=0){int w=m[v];if(!(r[w]>>u&1))return false;if(m[w]>=0&&(m[w]==u||s[m[w]]==u))return false;if(m[s[w]]>=0&&m[s[w]]==u)return false;}}return true;}
 void visit(unsigned used,int depth){
  if(timeout)return;nodes++;if((nodes&1023)==0&&limit())return;
  if(depth==10){leaves++;Perm inv;for(int u=0;u<10;u++)inv[m[u]]=u;for(int u=0;u<10;u++){unsigned row=(1U<<m[u])|(1U<<m[s[u]])|(1U<<s[m[u]])|(1U<<inv[inv[u]]);if(row!=r[u]||__builtin_popcount(row)!=4)return;}solutions.push_back(m);return;}
  int row=-1,best=11;unsigned options=0;
  for(int u=0;u<10;u++)if(m[u]<0){unsigned choices=allowed[u]&~used;if(m[s[u]]>=0)choices&=~(1U<<s[m[s[u]]]);int count=__builtin_popcount(choices);if(count<best){row=u;best=count;options=choices;}}
  if(best==0)return;
  while(options&&!timeout){int v=__builtin_ctz(options);options&=options-1;m[row]=v;if(partial())visit(used|(1U<<v),depth+1);m[row]=-1;}
 }
};
void add(Graph&g,int u,int v){assert(u!=v&&!(g[u]>>v&1));g[u]|=1ULL<<v;g[v]|=1ULL<<u;}
Graph expand(const Input&in,const Perm&ml,const Perm&mr){Graph g{};for(int a=0;a<3;a++)for(int u=0;u<10;u++){
 if(u<in.sl[u])add(g,10*a+u,10*a+in.sl[u]);if(u<in.sr[u])add(g,30+10*a+u,30+10*a+in.sr[u]);
 add(g,10*a+u,10*((a+1)%3)+ml[u]);add(g,30+10*a+u,30+10*((a+1)%3)+mr[u]);
 for(int v=0;v<10;v++){if(in.z[u]>>v&1)add(g,10*a+u,30+10*a+v);if(in.y[u]>>v&1)add(g,10*a+u,30+10*((a+1)%3)+v);}
 }for(auto row:g)assert(__builtin_popcountll(row)==8);return g;}
int score(const Graph&g){int bad=0;for(int u=0;u<60;u++){uint64_t reach=(1ULL<<u)|g[u],todo=g[u];while(todo){int v=__builtin_ctzll(todo);todo&=todo-1;reach|=g[v];}bad+=__builtin_popcountll(((1ULL<<60)-1)&~reach);}assert(!(bad&1));return bad/2;}
template<class T>void arrayjson(std::ostream&o,const T&a){o<<'[';for(unsigned i=0;i<a.size();i++){if(i)o<<',';o<<a[i];}o<<']';}
int main(int argc,char**argv){
 assert(argc==3);began=clock();std::ifstream input(argv[1]);int count;input>>count;assert(count==24660);std::vector<Input>inputs(count);
 for(auto&in:inputs){input>>in.config>>in.li>>in.ri;for(int&x:in.sl)input>>x;for(int&x:in.sr)input>>x;for(unsigned&x:in.z)input>>x;for(unsigned&x:in.y)input>>x;}
 const std::string prefix=argv[2];std::map<int,Stats>stats;long long processed=0,graphs=0;int best=100000,best_index=-1;Graph bestg{};Perm bestml{},bestmr{};
 for(int index=0;index<count&&!timeout&&!target;index++){
  if((index&63)==0&&limit())break;const auto&in=inputs[index];auto&st=stats[in.config];Rows zl=transpose(in.z),yl=transpose(in.y);
  Rows left=residual(in.y,in.z),right=residual(zl,yl);
  Solver l(in.sl,left);l.visit(0,0);if(timeout)break;
  if(!l.solutions.empty()){
   st.left_feasible++;st.left_solutions+=l.solutions.size();Solver r(in.sr,right);r.visit(0,0);if(timeout)break;
   if(!r.solutions.empty()){
    st.right_feasible++;st.right_solutions+=r.solutions.size();
    for(const auto&ml:l.solutions){for(const auto&mr:r.solutions){if((graphs&255)==0&&limit())break;Graph g=expand(in,ml,mr);int bad=score(g);graphs++;st.graphs++;if(bad<best){best=bad;bestg=g;bestml=ml;bestmr=mr;best_index=index;}if(!bad){target=true;break;}}if(timeout||target)break;}
   }
  }
  st.inputs++;processed++;
 }
 if(best_index>=0){std::ofstream e(prefix+".best.edges");e<<"60 240\n";for(int u=0;u<60;u++)for(int v=u+1;v<60;v++)if(bestg[u]>>v&1)e<<u<<' '<<v<<'\n';
  const auto&in=inputs[best_index];std::ofstream p(prefix+".best.parameters.json");p<<"{\"input_index\":"<<best_index<<",\"configuration\":"<<in.config<<",\"primal_choice\":"<<in.li<<",\"dual_choice\":"<<in.ri<<",\"S_L\":";arrayjson(p,in.sl);p<<",\"S_R\":";arrayjson(p,in.sr);p<<",\"Z_rows\":";arrayjson(p,in.z);p<<",\"Y_rows\":";arrayjson(p,in.y);p<<",\"M_L\":";arrayjson(p,bestml);p<<",\"M_R\":";arrayjson(p,bestmr);p<<",\"bad_pairs\":"<<best<<"}\n";
 }
 std::ofstream out(prefix+".json");out<<"{\"input_count\":24660,\"processed_inputs\":"<<processed<<",\"complete\":"<<(!timeout&&!target&&processed==count?"true":"false")<<",\"stop_reason\":\""<<(target?"valid_target_found":timeout?"cpu_cap":"complete_family")<<"\",\"cpu_budget_seconds\":10,\"cpu_seconds\":"<<double(clock()-began)/CLOCKS_PER_SEC<<",\"threads\":1,\"local_backtracking_nodes\":"<<nodes<<",\"complete_local_permutations_checked\":"<<leaves<<",\"complete_graphs_expanded\":"<<graphs<<",\"best_bad_pairs\":"<<(best_index>=0?std::to_string(best):"null")<<",\"configurations\":[";bool comma=false;
 for(auto [id,s]:stats){if(comma)out<<',';comma=true;out<<"{\"configuration\":"<<id<<",\"processed_Y_alignments\":"<<s.inputs<<",\"left_q1_feasible_alignments\":"<<s.left_feasible<<",\"both_q1_feasible_alignments\":"<<s.right_feasible<<",\"left_q1_solutions\":"<<s.left_solutions<<",\"right_q1_solutions_on_left_feasible_alignments\":"<<s.right_solutions<<",\"graphs_expanded\":"<<s.graphs<<"}";}out<<"]}\n";
 std::cout<<"processed "<<processed<<" of "<<count<<" graphs "<<graphs<<" best "<<(best_index>=0?best:-1)<<" nodes "<<nodes<<" stop "<<(timeout?"cpu_cap":target?"target":"complete")<<" CPU "<<double(clock()-began)/CLOCKS_PER_SEC<<'\n';
}
