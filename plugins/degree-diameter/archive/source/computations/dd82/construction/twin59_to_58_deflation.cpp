// All 24 saved order-59 states, all vertex deletions, all 105 neighbor repairs.
#define main previous_unrestricted_descent_main
#include "twin_seed_unrestricted_switch.cpp"
#undef main
using Repair=std::array<Edge,4>;
std::vector<Repair> matchings;
void build_matchings(unsigned left,Repair &r,int depth){
 if(!left){assert(depth==4);matchings.push_back(r);return;}
 int a=__builtin_ctz(left);left^=1U<<a;
 for(unsigned todo=left;todo;todo&=todo-1){int b=__builtin_ctz(todo);r[depth]={a,b};build_matchings(left^(1U<<b),r,depth+1);}
}
int live_score(const State&g,int deleted){
 const uint64_t live=((1ULL<<59)-1)^(1ULL<<deleted);int total=0;
 for(int u=0;u<59;u++)if(u!=deleted){uint64_t reach=g[u]|(1ULL<<u),todo=g[u];while(todo){int w=__builtin_ctzll(todo);todo&=todo-1;reach|=g[w];}total+=__builtin_popcountll(live&~reach);}
 assert(total%2==0);return total/2;
}
struct StateResult{int node,best=100000;long long choices=0,rejected=0,valid=0;std::map<int,long long>hist;};
int main(int argc,char**argv){
 assert(argc==3);std::ifstream in(argv[1]);int count;in>>count;assert(count==24);
 Repair indices{};build_matchings(255,indices,0);assert(matchings.size()==105);
 const clock_t start=clock();int best=100000,bestnode=-1,bestdeleted=-1;State bestgraph{};Repair bestrepair{};
 long long choices=0,rejected=0,valid=0;std::map<int,long long>hist;std::vector<StateResult>records;
 for(int si=0;si<count;si++){
  int node,nn,mm;in>>node>>nn>>mm;assert(nn==59&&mm==236);State original{};
  for(int k=0;k<mm;k++){int u,v;in>>u>>v;assert(0<=u&&u<v&&v<59&&!(original[u]>>v&1));toggle(original,{u,v});}
  for(int u=0;u<59;u++)assert(__builtin_popcountll(original[u])==8);
  StateResult record;record.node=node;
  for(int deleted=0;deleted<59;deleted++){
   std::vector<int>neighbors;for(int u=0;u<59;u++)if(original[deleted]>>u&1)neighbors.push_back(u);assert(neighbors.size()==8);
   State base=original;base[deleted]=0;for(int u=0;u<59;u++)base[u]&=~(1ULL<<deleted);
   for(const Repair& pattern:matchings){
    choices++;record.choices++;Repair repair{};bool legal=true;
    for(int k=0;k<4;k++){repair[k]=norm(neighbors[pattern[k].first],neighbors[pattern[k].second]);if(base[repair[k].first]>>repair[k].second&1)legal=false;}
    if(!legal){rejected++;record.rejected++;continue;}
    State g=base;for(Edge e:repair)toggle(g,e);int bad=live_score(g,deleted);valid++;record.valid++;hist[bad]++;record.hist[bad]++;record.best=std::min(record.best,bad);
    if(bad<best){best=bad;bestnode=node;bestdeleted=deleted;bestrepair=repair;bestgraph=g;}
   }
  }
  assert(record.choices==59*105&&record.rejected+record.valid==record.choices);records.push_back(record);
 }
 assert(choices==24*59*105&&valid+rejected==choices);n=58;all=(1ULL<<58)-1;State reduced{};
 for(int u=0;u<59;u++)if(u!=bestdeleted)for(int v=u+1;v<59;v++)if(bestgraph[u]>>v&1)toggle(reduced,{u-(u>bestdeleted),v-(v>bestdeleted)});
 assert(score(reduced)==best);const std::string prefix=argv[2];save(reduced,prefix+".best.edges");
 std::ofstream graph(prefix+".best.json");graph<<"{\"n\":58,\"source_state_node\":"<<bestnode<<",\"deleted_vertex_order59\":"<<bestdeleted<<",\"repair_edges_order59\":[";
 for(int k=0;k<4;k++){if(k)graph<<',';edgejson(graph,bestrepair[k]);}graph<<"],\"edges\":[";bool comma=false;
 for(int u=0;u<58;u++)for(int v=u+1;v<58;v++)if(reduced[u]>>v&1){if(comma)graph<<',';comma=true;edgejson(graph,{u,v});}graph<<"]}\n";
 std::ofstream report(prefix+".json");report<<"{\"scope\":\"All 24 saved labelled order59 states, all 59 deletions, all 105 perfect matchings on the eight neighbors; choices counted without graph deduplication\",\"complete_for_stated_choices\":true,\"input_states\":24,\"choices\":"<<choices<<",\"rejected_existing_edges\":"<<rejected<<",\"valid_choices\":"<<valid<<",\"minimum_bad_pairs\":"<<best<<",\"best_source_node\":"<<bestnode<<",\"best_deleted_vertex_order59\":"<<bestdeleted<<",\"best_repair_edges_order59\":[";
 for(int k=0;k<4;k++){if(k)report<<',';edgejson(report,bestrepair[k]);}report<<"],\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"threads\":1,\"bad_pair_histogram\":{";comma=false;
 for(auto [bad,num]:hist){if(comma)report<<',';comma=true;report<<'"'<<bad<<"\":"<<num;}report<<"},\"per_state\":[";
 for(unsigned k=0;k<records.size();k++){if(k)report<<',';const auto&r=records[k];report<<"{\"node\":"<<r.node<<",\"choices\":"<<r.choices<<",\"rejected_existing_edges\":"<<r.rejected<<",\"valid_choices\":"<<r.valid<<",\"minimum_bad_pairs\":"<<r.best<<",\"bad_pair_histogram\":{";comma=false;for(auto [bad,num]:r.hist){if(comma)report<<',';comma=true;report<<'"'<<bad<<"\":"<<num;}report<<"}}";}
 report<<"]}\n";std::cout<<choices<<" choices, "<<valid<<" valid, "<<rejected<<" rejected, best "<<best<<", source "<<bestnode<<", deletion "<<bestdeleted<<", CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
