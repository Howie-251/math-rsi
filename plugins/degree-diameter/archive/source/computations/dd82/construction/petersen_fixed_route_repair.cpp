// One bounded, deterministic nonincreasing repair of immutable route rows.
// Only the 15 external matching permutations move. No graph-distance energy.
#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using State = std::array<unsigned char,150>;
struct Node { State state; int parent, pair, u, v, score; };
int m[6][6][10], left_f[15], right_f[15];
std::vector<Node> nodes;
double start_cpu;
double cpu() { return double(std::clock())/CLOCKS_PER_SEC-start_cpu; }
void decode(const State& s) {
  for(int e=0;e<15;++e) for(int u=0;u<10;++u) {
    int i=left_f[e],j=right_f[e],v=s[10*e+u];
    m[i][j][u]=v; m[j][i][v]=u;
  }
}
void change(int e,int u,int v) {
  int i=left_f[e],j=right_f[e],a=m[i][j][u],b=m[i][j][v];
  std::swap(m[i][j][u],m[i][j][v]);m[j][i][a]=v;m[j][i][b]=u;
}
int score(int limit=10000) {
  int result=0;
  for(int i=0;i<6;++i) for(int j=0;j<6;++j) if(i!=j)
    for(int u=0;u<10;++u) {
      unsigned mask=1u<<m[i][j][u];
      for(int k=0;k<6;++k) if(k!=i && k!=j)
        mask|=1u<<m[k][j][m[i][k][u]];
      result+=std::max(0,4-__builtin_popcount(mask));
      if(result>limit) return result;
    }
  return result;
}
void state_json(std::ostream& out,const State& state) {
  out<<"[";for(int e=0;e<15;++e) {
    if(e)out<<",";out<<"[";
    for(int u=0;u<10;++u){if(u)out<<",";out<<int(state[10*e+u]);}
    out<<"]";
  }out<<"]";
}
int main(int argc,char**argv) {
  assert(argc==3);start_cpu=double(std::clock())/CLOCKS_PER_SEC;
  int id[6][6],t=0;for(int i=0;i<6;++i)for(int j=i+1;j<6;++j)
    {left_f[t]=i;right_f[t]=j;id[i][j]=t++;}
  State initial;initial.fill(255);
  std::ifstream in(argv[1]);int n,ec;in>>n>>ec;assert(n==60&&ec==240);
  for(int z=0,u,v;z<ec;++z) {
    in>>u>>v;if(u>v)std::swap(u,v);
    if(u/10!=v/10) initial[10*id[u/10][v/10]+u%10]=v%10;
  }
  for(int e=0;e<15;++e){std::set<int> seen;for(int u=0;u<10;++u)
    seen.insert(initial[10*e+u]);assert(seen.size()==10&&*seen.rbegin()<10);}
  decode(initial);int initial_score=score(),level=initial_score,best_id=0;
  nodes.push_back({initial,-1,-1,-1,-1,level});
  std::vector<int> queue{0};size_t cursor=0;
  std::set<State> seen{initial};
  long long candidates=0;int expanded=0,improvements=0;
  std::string stop="";
  while(stop.empty()) {
    if(level==0){stop="all_fixed_rows_feasible";break;}
    if(cursor==queue.size()){stop="neutral_component_closed";break;}
    if(cpu()>=4.8){stop="cpu_budget";break;}
    int parent=queue[cursor++];State current=nodes[parent].state;
    decode(current);++expanded;bool improved=false;
    for(int e=0;e<15&&!improved&&stop.empty();++e)
      for(int u=0;u<10&&!improved&&stop.empty();++u)
        for(int v=u+1;v<10&&!improved&&stop.empty();++v) {
          if((candidates&255)==0&&cpu()>=4.8){stop="cpu_budget";break;}
          change(e,u,v);++candidates;int value=score(level);
          if(value<=level) {
            State child=current;std::swap(child[10*e+u],child[10*e+v]);
            if(!seen.count(child)) {
              if(nodes.size()>=500){stop="500_total_stored_states";}
              else {
                int child_id=nodes.size();
                nodes.push_back({child,parent,e,u,v,value});
                if(value<level) {
                  ++improvements;level=value;best_id=child_id;improved=true;
                  queue={child_id};cursor=0;seen.clear();seen.insert(child);
                }else {seen.insert(child);queue.push_back(child_id);}
              }
            }
          }
          change(e,u,v);
        }
  }
  decode(nodes[best_id].state);assert(score()==level);
  std::vector<int> path;
  for(int id=best_id;id!=-1;id=nodes[id].parent)path.push_back(id);
  std::reverse(path.begin(),path.end());
  std::ofstream out(argv[2]);out.precision(12);
  out<<"{\n\"initial_deficit\":"<<initial_score<<",\"best_deficit\":"<<level
     <<",\"stop\":\""<<stop<<"\",\"states_stored\":"<<nodes.size()
     <<",\"states_expanded\":"<<expanded<<",\"switch_candidates_checked\":"<<candidates
     <<",\"strict_improvements\":"<<improvements<<",\"internal_cpu_seconds\":"<<cpu()
     <<",\"best_permutations\":";state_json(out,nodes[best_id].state);
  out<<",\"path\":[";
  for(size_t r=0;r<path.size();++r){if(r)out<<",";const Node& node=nodes[path[r]];
    out<<"{\"state_id\":"<<path[r]<<",\"deficit\":"<<node.score<<",\"switch\":";
    if(node.pair<0)out<<"null";
    else out<<"["<<left_f[node.pair]<<","<<right_f[node.pair]<<","<<node.u<<","<<node.v<<"]";
    out<<",\"permutations\":";state_json(out,node.state);out<<"}";
  }
  out<<"]}\n";
  std::cout<<"initial="<<initial_score<<" best="<<level<<" stop="<<stop
           <<" stored="<<nodes.size()<<" expanded="<<expanded<<" candidates="<<candidates
           <<" cpu="<<cpu()<<"\n";
}
