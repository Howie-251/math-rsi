// Bounded BFS of the seed-level plateau using all unrestricted two-edge switches.
// Deduplication is an ordered set of sorted edge sequences, not a hash table.
#define main previous_unrestricted_descent_main
#include "twin_seed_unrestricted_switch.cpp"
#undef main
#include <set>
struct Node {State g;int parent,energy;Change move;};
struct Expansion {int node;long long valid=0,new_neutral=0,already_seen_neutral=0;bool complete=false;std::map<int,long long>hist;};
using Key=std::vector<unsigned short>;
Key key(const State&g){Key out;out.reserve(232);for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(g[u]>>v&1)out.push_back(static_cast<unsigned short>(64*u+v));return out;}
int main(int argc,char**argv){
 assert(argc==3);const std::string source=argv[1],prefix=argv[2];std::ifstream in(source);int m;in>>n>>m;assert(n==58&&m==232);all=(1ULL<<n)-1;State initial{};int u,v,count=0;
 while(in>>u>>v){assert(0<=u&&u<v&&v<n&&!(initial[u]>>v&1));toggle(initial,{u,v});count++;}assert(count==m);const int initial_energy=score(initial);assert(initial_energy>0);
 constexpr int state_cap=100;constexpr double cpu_cap=5.0;const clock_t began=clock();
 std::vector<Node>nodes{{initial,-1,initial_energy,{}}};std::set<Key>seen;seen.insert(key(initial));
 std::vector<Expansion>expansions;std::string stop;int improved=-1;long long total_candidates=0;int complete_expansions=0;
 for(unsigned current=0;current<nodes.size() && stop.empty();current++){
  State g=nodes[current].g;Expansion ex;ex.node=current;std::vector<Edge>edges;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)if(g[a]>>b&1)edges.emplace_back(a,b);
  for(unsigned e=0;e<edges.size()&&stop.empty();e++)for(unsigned f=e+1;f<edges.size()&&stop.empty();f++){
   auto [a,b]=edges[e];auto [c,d]=edges[f];if(a==c||a==d||b==c||b==d)continue;
   for(int mode=0;mode<2&&stop.empty();mode++){
    Change ch{{edges[e],edges[f]},mode==0?std::array<Edge,2>{norm(a,c),norm(b,d)}:std::array<Edge,2>{norm(a,d),norm(b,c)}};
    if((g[ch.added[0].first]>>ch.added[0].second&1)||(g[ch.added[1].first]>>ch.added[1].second&1))continue;
    for(auto x:ch.removed){toggle(g,x);}for(auto x:ch.added){toggle(g,x);}
    const int energy=score(g);ex.valid++;total_candidates++;ex.hist[energy]++;
    if(energy<=initial_energy){
     Key encoded=key(g);auto [position,fresh]=seen.insert(std::move(encoded));(void)position;
     if(fresh){
      assert(nodes.size()<state_cap);nodes.push_back({g,int(current),energy,ch});
      if(energy<initial_energy){improved=int(nodes.size())-1;stop="first_strict_improvement";}
      else{ex.new_neutral++;if(nodes.size()==state_cap)stop="distinct_state_cap";}
     }else{assert(energy==initial_energy);ex.already_seen_neutral++;}
    }
    for(auto x:ch.added){toggle(g,x);}for(auto x:ch.removed){toggle(g,x);}
    if(stop.empty()&&(total_candidates&511)==0&&double(clock()-began)/CLOCKS_PER_SEC>=cpu_cap)stop="cpu_cap";
   }
  }
  assert(g==nodes[current].g);
  if(stop.empty()){ex.complete=true;complete_expansions++;}
  expansions.push_back(ex);
 }
 if(stop.empty())stop="complete_neutral_component_no_improvement";
 const int endpoint=improved>=0?improved:int(nodes.size())-1;std::vector<int>path;
 for(int x=endpoint;nodes[x].parent>=0;x=nodes[x].parent){path.push_back(x);}
 std::reverse(path.begin(),path.end());
 std::vector<std::string>saved;
 for(unsigned k=0;k<path.size();k++){std::string file=prefix+".path"+std::to_string(k+1)+".edges";save(nodes[path[k]].g,file);saved.push_back(file);}
 std::ofstream o(prefix+".json");
 o<<"{\"initial_bad_pairs\":"<<initial_energy<<",\"source\":\""<<source<<"\",\"scope\":\"connected component of labelled seed-level graphs under unrestricted simple-graph two-edge switches, with first-improvement exit\",\"deduplication\":\"ordered set of sorted edge sequences\",\"maximum_distinct_stored_states\":100,\"cpu_budget_seconds\":5,\"cpu_seconds\":"<<double(clock()-began)/CLOCKS_PER_SEC<<",\"threads\":1,\"stop_reason\":\""<<stop<<"\",\"component_completely_closed\":"<<(stop=="complete_neutral_component_no_improvement"?"true":"false")<<",\"distinct_stored_states\":"<<nodes.size()<<",\"fully_expanded_states\":"<<complete_expansions<<",\"candidate_switches_evaluated\":"<<total_candidates<<",\"strict_improvement_found\":"<<(improved>=0?"true":"false")<<",\"endpoint_bad_pairs\":"<<nodes[endpoint].energy<<",\"path\":[";
 for(unsigned k=0;k<path.size();k++){if(k)o<<',';const auto&z=nodes[path[k]];o<<"{\"node\":"<<path[k]<<",\"parent\":"<<z.parent<<",\"bad_pairs\":"<<z.energy<<",\"file\":\""<<saved[k]<<"\",\"change\":";changejson(o,z.move);o<<'}';}o<<"],\"stored_states\":[";
 for(unsigned k=0;k<nodes.size();k++){if(k)o<<',';o<<"{\"node\":"<<k<<",\"parent\":"<<nodes[k].parent<<",\"bad_pairs\":"<<nodes[k].energy;if(k){o<<",\"change\":";changejson(o,nodes[k].move);}o<<'}';}o<<"],\"expansions\":[";
 for(unsigned k=0;k<expansions.size();k++){if(k)o<<',';const auto&e=expansions[k];o<<"{\"node\":"<<e.node<<",\"complete\":"<<(e.complete?"true":"false")<<",\"valid_switches_evaluated\":"<<e.valid<<",\"new_neutral_states\":"<<e.new_neutral<<",\"duplicate_neutral_endpoints\":"<<e.already_seen_neutral<<",\"bad_pair_histogram\":{";bool comma=false;for(auto [energy,num]:e.hist){if(comma)o<<',';comma=true;o<<'"'<<energy<<"\":"<<num;}o<<"}}";}o<<"]}\n";
 std::cout<<"stop "<<stop<<" states "<<nodes.size()<<" fully expanded "<<complete_expansions<<" candidates "<<total_candidates<<" endpoint "<<nodes[endpoint].energy<<" path length "<<path.size()<<" CPU "<<double(clock()-began)/CLOCKS_PER_SEC<<'\n';
}
