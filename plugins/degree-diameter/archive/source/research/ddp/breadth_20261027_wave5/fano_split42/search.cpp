#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using Graph=array<uint64_t,42>;
constexpr uint64_t FULL=(1ULL<<42)-1;
void edge(Graph&g,int u,int v){assert(u!=v && !(g[u]>>v&1));g[u]|=1ULL<<v;g[v]|=1ULL<<u;}
uint64_t reach3(const Graph&g,int root){
 uint64_t seen=(1ULL<<root)|g[root];
 for(int k=0;k<2;k++){uint64_t todo=seen,next=seen;while(todo){int v=__builtin_ctzll(todo);todo&=todo-1;next|=g[v];}seen=next;}
 return seen;
}
int badscore(const Graph&g){int bad=0;for(int u=0;u<42;u++)bad+=__builtin_popcountll(FULL^reach3(g,u));assert(bad%2==0);return bad/2;}
int main(int argc,char**argv){
 string dir=argc>1?argv[1]:".";clock_t start=clock();ifstream f(dir+"/input.txt");
 int m;f>>m;vector<pair<int,int>> bb(m);for(auto&e:bb)f>>e.first>>e.second;
 array<array<int,4>,7> neighbors;for(auto&row:neighbors)for(int&v:row)f>>v;
 assert(f && m==42);
 int tested=0,best=10000,bestcode=-1,bestt=-1;bool success=false,cpu_limit=false;
 Graph bestg{};array<int,7> bestchoices{};
 for(int code=0;code<2187 && !success && !cpu_limit;code++){
  int value=code;array<int,7> choices{};for(int i=0;i<7;i++){choices[i]=value%3;value/=3;}
  for(int t=1;t<=6;t++){
   if(double(clock()-start)/CLOCKS_PER_SEC>=58){cpu_limit=true;break;}
   Graph g{};
   for(auto e:bb)edge(g,e.first,e.second);
   for(int i=0;i<7;i++){
    int a=28+2*i,b=a+1;edge(g,a,b);
    for(int j=0;j<4;j++)edge(g,neighbors[i][j],j==0||j==choices[i]+1?a:b);
   }
   for(int i=0;i<7;i++)edge(g,28+2*i,29+2*((i+t)%7));
   int degree_sum=0;for(int u=0;u<42;u++){assert(__builtin_popcountll(g[u])==4);assert(!(g[u]>>u&1));degree_sum+=__builtin_popcountll(g[u]);}
   assert(degree_sum==168);
   int bad=badscore(g);tested++;
   if(bad<best){best=bad;bestcode=code;bestt=t;bestg=g;bestchoices=choices;cout<<"candidate "<<tested<<" best_bad_unordered "<<best<<" code "<<code<<" t "<<t<<endl;}
   if(!bad){success=true;break;}
  }
 }
 ofstream out(dir+"/best.edges");out<<42<<" "<<84<<"\n";for(int u=0;u<42;u++)for(int v=u+1;v<42;v++)if(bestg[u]>>v&1)out<<u<<" "<<v<<"\n";
 ofstream params(dir+"/best_parameters.json");params<<"{\"partition_code_base3_little_endian\":"<<bestcode<<",\"partition_choices\":[";for(int i=0;i<7;i++)params<<(i?",":"")<<bestchoices[i];params<<"],\"matching_shift_t\":"<<bestt<<",\"vertices\":42,\"degree\":4,\"production_D3_bad_unordered_pairs\":"<<best<<"}\n";
 ofstream badfile(dir+"/best_bad_pairs.json");badfile<<"{\"scope\":\"production complete all-root depth-three reachability; not independent final verification\",\"unordered_pairs_distance_over3\":[";bool first=true;for(int u=0;u<42;u++){uint64_t seen=reach3(bestg,u);for(int v=u+1;v<42;v++)if(!(seen>>v&1)){badfile<<(first?"":",")<<"["<<u<<","<<v<<"]";first=false;}}badfile<<"]}\n";
 ofstream result(dir+"/RESULT.json");result<<"{\"status\":\""<<(success?"PRODUCTION_D3_CANDIDATE_FOUND":cpu_limit?"CPU_LIMIT_INCOMPLETE":"COMPLETE_FINITE_FAMILY_NO_D3")<<"\",\"planned_candidates\":13122,\"tested_candidates\":"<<tested<<",\"all_tested_simple_four_regular\":true,\"best_bad_unordered_pairs\":"<<best<<",\"best_partition_code\":"<<bestcode<<",\"best_matching_shift\":"<<bestt<<",\"CPU_seconds\":"<<setprecision(10)<<double(clock()-start)/CLOCKS_PER_SEC<<",\"independent_final_BFS_performed\":false,\"additional_orientations_or_matchings_tested\":false}\n";
 cout<<"DONE tested "<<tested<<" best "<<best<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}
