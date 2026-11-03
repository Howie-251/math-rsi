#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Edge = pair<int,int>;
using Graph = array<uint64_t,60>;
static const uint64_t MASK=((uint64_t(1)<<60)-1)^(uint64_t(1)<<41);
Edge edge(int a,int b){return minmax(a,b);}
void erase_edge(Graph& g,Edge e){assert(g[e.first]&(uint64_t(1)<<e.second));g[e.first]^=uint64_t(1)<<e.second;g[e.second]^=uint64_t(1)<<e.first;}
void add_edge(Graph& g,Edge e){assert(!(g[e.first]&(uint64_t(1)<<e.second)));g[e.first]|=uint64_t(1)<<e.second;g[e.second]|=uint64_t(1)<<e.first;}
int bad_pairs(const Graph& g){
 int twice=0;
 for(int u=0;u<60;++u)if(u!=41){
  uint64_t reach=g[u]|(uint64_t(1)<<u), todo=g[u];
  while(todo){int v=__builtin_ctzll(todo);todo&=todo-1;reach|=g[v];}
  twice+=__builtin_popcountll(MASK&~reach);
 }
 assert(twice%2==0);return twice/2;
}
void write_edges(const string& path,const Graph& g){
 ofstream out(path);out<<"59 236\n";int n=0;
 for(int u=0;u<60;++u)if(u!=41){assert(__builtin_popcountll(g[u])==8);
  for(int v=u+1;v<60;++v)if(g[u]&(uint64_t(1)<<v)){
   out<<(u-(u>41))<<' '<<(v-(v>41))<<'\n';++n;
  }
 }assert(n==236);
}
void json_edge(ostream& o,Edge e){o<<'['<<e.first<<','<<e.second<<']';}
struct Record {int bad;Edge second,h1,h2;array<Edge,4> added;string file;};
int main(int argc,char**argv){
 assert(argc==4);clock_t start=clock();
 ifstream in(argv[1]);int n,m;in>>n>>m;assert(n==59&&m==236);Graph seed{};
 for(int j=0;j<m;++j){int u,v;in>>u>>v;u+=(u>=41);v+=(v>=41);add_edge(seed,edge(u,v));}
 for(int v=0;v<60;++v)assert(__builtin_popcountll(seed[v])==(v==41?0:8));
 assert(bad_pairs(seed)==26);
 ifstream family(argv[2]);int count;family>>count;vector<Edge> seconds(count);
 for(auto& e:seconds)family>>e.first>>e.second;
 int hn;family>>hn;assert(hn==12);vector<Edge> hs(hn);for(auto&e:hs)family>>e.first>>e.second;
 const string prefix=argv[3];Graph released=seed;erase_edge(released,{9,14});
 long long combinations_count=0,raw_assignments=0,unique_assignments=0,invalid=0,valid=0,best_ties=0;
 map<int,long long> histogram;vector<Record> records;int best=10000;bool complete=true;
 for(auto second:seconds){
  Graph core=released;erase_edge(core,second);
  array<int,4> olds={9,14,second.first,second.second};sort(olds.begin(),olds.end());
  for(int i=0;i<hn;++i)for(int j=i+1;j<hn;++j){
   if(double(clock()-start)/CLOCKS_PER_SEC>9.5){complete=false;goto finished;}
   ++combinations_count;Graph partial=core;erase_edge(partial,hs[i]);erase_edge(partial,hs[j]);
   array<int,4> news={hs[i].first,hs[i].second,hs[j].first,hs[j].second};sort(news.begin(),news.end());
   set<array<Edge,4>> seen;
   do{
    ++raw_assignments;array<Edge,4> adds;
    for(int k=0;k<4;++k)adds[k]=edge(olds[k],news[k]);sort(adds.begin(),adds.end());
    if(!seen.insert(adds).second)continue;++unique_assignments;
    bool ok=true;
    for(int k=0;k<4;++k)if((k&&adds[k]==adds[k-1])||(partial[adds[k].first]&(uint64_t(1)<<adds[k].second)))ok=false;
    if(!ok){++invalid;continue;}
    Graph g=partial;for(auto e:adds)add_edge(g,e);
    int energy=bad_pairs(g);++valid;++histogram[energy];
    if(energy<best){
     best=energy;best_ties=1;string file=prefix+".record"+to_string(records.size())+".edges";
     write_edges(file,g);records.push_back({energy,second,hs[i],hs[j],adds,file});
    }else if(energy==best)++best_ties;
   }while(next_permutation(news.begin(),news.end()));
  }
 }
 finished:
 ofstream report(prefix+".json");
 report<<"{\n\"scope\":\"139 passed old cores, two original H edges deleted, all distinct four-slot assignments; no general attachment completion\",\n";
 report<<"\"complete\":"<<(complete?"true":"false")<<",\n\"original_60_labels_for_changes\":true,\n\"edge_files_use_compressed_59_labels\":true,\n";
 report<<"\"core_count\":"<<count<<",\n\"core_auxiliary_combinations\":"<<combinations_count<<",\n\"raw_unique_new_slot_permutations\":"<<raw_assignments<<",\n";
 report<<"\"distinct_edge_assignments\":"<<unique_assignments<<",\n\"rejected_assignments\":"<<invalid<<",\n\"valid_full_candidates\":"<<valid<<",\n";
 report<<"\"source_bad_pairs\":26,\n\"best_bad_pairs\":"<<best<<",\n\"best_assignment_count\":"<<best_ties<<",\n\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\n\"internal_cpu_limit\":9.5,\n";
 report<<"\"bad_pair_histogram\":{";bool first=true;for(auto [e,c]:histogram){if(!first)report<<',';first=false;report<<'\"'<<e<<"\":"<<c;}report<<"},\n\"strict_best_records\":[";
 first=true;for(auto&r:records){if(!first)report<<',';first=false;
  report<<"{\"bad_pairs\":"<<r.bad<<",\"second_deleted_old_edge\":";json_edge(report,r.second);
  report<<",\"removed_auxiliary_edges\":[";json_edge(report,r.h1);report<<',';json_edge(report,r.h2);
  report<<"],\"added_old_new_edges\":[";for(int k=0;k<4;++k){if(k)report<<',';json_edge(report,r.added[k]);}
  report<<"],\"file\":\""<<r.file<<"\"}";
 }report<<"]\n}\n";report.close();
 cout<<"complete="<<complete<<" valid="<<valid<<" best="<<best<<" ties="<<best_ties<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
