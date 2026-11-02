// One globally bounded nonworsening episode from the new 21-bad-pair graph.
// Neutral BFS at each energy; first strict improvement starts the next level.
#define main previous_unrestricted_descent_main
#include "twin_seed_unrestricted_switch.cpp"
#undef main
#include <set>
struct LevelNode {State g;int parent,energy;Change move;};
struct LevelExpansion {int level,node;long long valid=0,new_neutral=0,duplicates=0;bool complete=false;std::map<int,long long>hist;};
struct Level {int energy,root;long long candidates=0,new_neutral=0;int complete_expansions=0,exit_node=-1;double cpu=0;std::string stop;};
using OrderedEdges=std::vector<unsigned short>;
OrderedEdges encode_edges(const State&g){OrderedEdges out;out.reserve(232);for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(g[u]>>v&1)out.push_back(static_cast<unsigned short>(64*u+v));return out;}
int main(int argc,char**argv){
 assert(argc==3);const std::string source=argv[1],prefix=argv[2];std::ifstream in(source);int m;in>>n>>m;assert(n==58&&m==232);all=(1ULL<<n)-1;State initial{};int u,v,count=0;
 while(in>>u>>v){assert(0<=u&&u<v&&v<n&&!(initial[u]>>v&1));toggle(initial,{u,v});count++;}assert(count==m&&score(initial)==21);
 constexpr int maxstates=2000,maximprovements=20;constexpr double budget=10;const clock_t start=clock();
 std::vector<LevelNode>nodes{{initial,-1,21,{}}};std::set<OrderedEdges>seen;seen.insert(encode_edges(initial));
 std::vector<LevelExpansion>expansions;std::vector<Level>levels;std::vector<int>newbests;std::vector<std::string>saved;
 int currentroot=0;long long total_candidates=0;std::string stop;
 while(stop.empty()){
  const clock_t levelstart=clock();const int levelid=levels.size();Level level;level.energy=nodes[currentroot].energy;level.root=currentroot;
  std::vector<int>queue{currentroot};int improved=-1;
  for(unsigned cursor=0;cursor<queue.size()&&stop.empty()&&improved<0;cursor++){
   int current=queue[cursor];State g=nodes[current].g;LevelExpansion ex;ex.node=current;ex.level=levelid;
   std::vector<Edge>edges;for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)if(g[a]>>b&1)edges.emplace_back(a,b);
   for(unsigned e=0;e<edges.size()&&stop.empty()&&improved<0;e++)for(unsigned f=e+1;f<edges.size()&&stop.empty()&&improved<0;f++){
    auto [a,b]=edges[e];auto [c,d]=edges[f];if(a==c||a==d||b==c||b==d)continue;
    for(int mode=0;mode<2&&stop.empty()&&improved<0;mode++){
     Change ch{{edges[e],edges[f]},mode==0?std::array<Edge,2>{norm(a,c),norm(b,d)}:std::array<Edge,2>{norm(a,d),norm(b,c)}};
     if((g[ch.added[0].first]>>ch.added[0].second&1)||(g[ch.added[1].first]>>ch.added[1].second&1))continue;
     for(auto x:ch.removed){toggle(g,x);}for(auto x:ch.added){toggle(g,x);}
     const int energy=score(g);ex.valid++;level.candidates++;total_candidates++;ex.hist[energy]++;
     if(energy<=level.energy){
      auto [position,fresh]=seen.insert(encode_edges(g));(void)position;
      if(fresh){
       assert(nodes.size()<maxstates);int child=nodes.size();nodes.push_back({g,current,energy,ch});
       if(energy<level.energy){
        improved=child;level.exit_node=child;newbests.push_back(child);
        std::string file=prefix+".best"+std::to_string(energy)+".edges";save(g,file);saved.push_back(file);
        std::cout<<"new best "<<energy<<" stored "<<nodes.size()<<" node "<<child<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<std::endl;
        if(energy==0)stop="valid_target_found";
        else if(int(newbests.size())>=maximprovements)stop="improvement_cap";
       }else{queue.push_back(child);ex.new_neutral++;level.new_neutral++;}
       if(stop.empty()&&nodes.size()==maxstates)stop="global_distinct_state_cap";
      }else{assert(energy==level.energy);ex.duplicates++;}
     }
     for(auto x:ch.added){toggle(g,x);}for(auto x:ch.removed){toggle(g,x);}
     if(stop.empty()&&(total_candidates&511)==0&&double(clock()-start)/CLOCKS_PER_SEC>=budget)stop="global_cpu_cap";
    }
   }
   assert(g==nodes[current].g);
   if(stop.empty()&&improved<0){ex.complete=true;level.complete_expansions++;}
   expansions.push_back(ex);
  }
  if(improved>=0){level.stop="first_strict_improvement";currentroot=improved;}
  else if(stop.empty()){stop="complete_neutral_component_no_lower_exit";level.stop=stop;}
  else{level.stop=stop;}
  level.cpu=double(clock()-levelstart)/CLOCKS_PER_SEC;levels.push_back(level);
  if(stop.empty()&&double(clock()-start)/CLOCKS_PER_SEC>=budget)stop="global_cpu_cap";
 }
 int finalbest=currentroot;std::vector<int>bestpath;for(int node=finalbest;nodes[node].parent>=0;node=nodes[node].parent){bestpath.push_back(node);}std::reverse(bestpath.begin(),bestpath.end());
 std::ofstream o(prefix+".json");
 o<<"{\"source\":\""<<source<<"\",\"scope\":\"one deterministic nonworsening episode: neutral BFS at each level, reset at first strict improvement\",\"deduplication\":\"global ordered set of sorted labelled edge sequences\",\"maximum_distinct_stored_states\":2000,\"maximum_improvements\":20,\"cpu_budget_seconds\":10,\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"threads\":1,\"initial_bad_pairs\":21,\"final_bad_pairs\":"<<nodes[finalbest].energy<<",\"stop_reason\":\""<<stop<<"\",\"terminal_neutral_component_closed\":"<<(stop=="complete_neutral_component_no_lower_exit"?"true":"false")<<",\"distinct_stored_states\":"<<nodes.size()<<",\"candidate_switches_evaluated\":"<<total_candidates<<",\"strict_improvements\":"<<newbests.size()<<",\"new_best_graphs\":[";
 for(unsigned k=0;k<newbests.size();k++){if(k)o<<',';o<<"{\"node\":"<<newbests[k]<<",\"bad_pairs\":"<<nodes[newbests[k]].energy<<",\"file\":\""<<saved[k]<<"\"}";}o<<"],\"final_best_path\":[";
 for(unsigned k=0;k<bestpath.size();k++){if(k)o<<',';o<<bestpath[k];}o<<"],\"levels\":[";
 for(unsigned k=0;k<levels.size();k++){if(k)o<<',';const auto&l=levels[k];o<<"{\"level\":"<<k<<",\"bad_pairs\":"<<l.energy<<",\"root_node\":"<<l.root<<",\"candidate_switches_evaluated\":"<<l.candidates<<",\"new_neutral_states\":"<<l.new_neutral<<",\"fully_expanded_states\":"<<l.complete_expansions<<",\"exit_improvement_node\":"<<l.exit_node<<",\"cpu_seconds\":"<<l.cpu<<",\"stop_reason\":\""<<l.stop<<"\"}";}o<<"],\"stored_states\":[";
 for(unsigned k=0;k<nodes.size();k++){if(k)o<<',';o<<"{\"node\":"<<k<<",\"parent\":"<<nodes[k].parent<<",\"bad_pairs\":"<<nodes[k].energy;if(k){o<<",\"change\":";changejson(o,nodes[k].move);}o<<'}';}o<<"],\"expansions\":[";
 for(unsigned k=0;k<expansions.size();k++){if(k)o<<',';const auto&e=expansions[k];o<<"{\"level\":"<<e.level<<",\"node\":"<<e.node<<",\"complete\":"<<(e.complete?"true":"false")<<",\"valid_switches_evaluated\":"<<e.valid<<",\"new_neutral_states\":"<<e.new_neutral<<",\"duplicate_neutral_endpoints\":"<<e.duplicates<<",\"bad_pair_histogram\":{";bool comma=false;for(auto [energy,num]:e.hist){if(comma)o<<',';comma=true;o<<'"'<<energy<<"\":"<<num;}o<<"}}";}o<<"]}\n";
 std::cout<<"stop "<<stop<<" states "<<nodes.size()<<" levels "<<levels.size()<<" final "<<nodes[finalbest].energy<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
