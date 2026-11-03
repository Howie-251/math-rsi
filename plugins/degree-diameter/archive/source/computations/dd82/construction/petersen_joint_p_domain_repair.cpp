// One joint complete-Petersen-domain repair. F=0 is a hard invariant.
// R is the sum of exact minimum forbidden-edge counts over all 30240 copies.
#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <cstdint>
#include <map>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using State = std::array<unsigned char,150>;
struct Node { State state; int parent, pair, u, v, score; std::array<uint64_t,6> internal; };
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
struct Domain { int distance; uint64_t copy; };
std::vector<uint64_t> catalog;
std::vector<std::pair<int,int>> local_edges;
std::map<uint64_t,Domain> cache;
uint64_t last_allowed[6];
long long domain_queries=0, popcount_checks=0;
void make_catalog() {
  int edge_index[10][10];
  for(int u=0;u<10;++u)for(int v=u+1;v<10;++v) {
    edge_index[u][v]=edge_index[v][u]=local_edges.size();local_edges.emplace_back(u,v);
  }
  std::vector<std::pair<int,int>> standard={{0,1},{0,4},{0,5},{1,2},{1,6},{2,3},
    {2,7},{3,4},{3,8},{4,9},{5,7},{5,8},{6,8},{6,9},{7,9}};
  std::array<int,10> p{};for(int u=0;u<10;++u)p[u]=u;
  std::set<uint64_t> unique;
  do {
    if(!(p[1]<p[4]&&p[4]<p[5]&&p[2]<p[6]))continue;
    uint64_t mask=0;for(auto [u,v]:standard)mask|=1ULL<<edge_index[p[u]][p[v]];
    assert(unique.insert(mask).second);
  }while(std::next_permutation(p.begin()+1,p.end()));
  assert(unique.size()==30240);catalog.assign(unique.begin(),unique.end());
}
Domain domain(uint64_t allowed) {
  ++domain_queries;auto it=cache.find(allowed);if(it!=cache.end())return it->second;
  Domain best{100,0};
  for(auto mask:catalog) {
    ++popcount_checks;int missing=__builtin_popcountll(mask&~allowed);
    if(missing<best.distance)best={missing,mask};
    if(!missing)break; // Zero is the exact minimum; first copy is deterministic.
  }
  cache.emplace(allowed,best);return best;
}
std::array<uint64_t,6> choose_current() {
  std::array<uint64_t,6> result{};
  for(int i=0;i<6;++i)result[i]=domain(last_allowed[i]).copy;
  return result;
}
int score(int limit=10000) {
  unsigned banned[6][10] = {};
  for(int i=0;i<6;++i) for(int j=0;j<6;++j) if(i!=j)
    for(int u=0;u<10;++u) {
      unsigned mask=1u<<m[i][j][u];
      for(int k=0;k<6;++k) if(k!=i && k!=j)
        mask|=1u<<m[k][j][m[i][k][u]];
      int distinct=__builtin_popcount(mask);
      if(distinct<4) return 1000;
      if(distinct==5) continue;
      int direct=m[i][j][u];
      for(int v=0;v<10;++v) if(mask & (1u<<v)) {
        int w=m[j][i][v];
        if(w!=u) {banned[i][u]|=1u<<w;banned[i][w]|=1u<<u;}
        if(v!=direct) {banned[j][direct]|=1u<<v;banned[j][v]|=1u<<direct;}
      }
    }
  int total=0;
  for(int i=0;i<6;++i) {
    uint64_t allowed=0;
    for(int e=0;e<45;++e) {auto [u,v]=local_edges[e];if(!(banned[i][u]>>v&1))allowed|=1ULL<<e;}
    last_allowed[i]=allowed;total+=domain(allowed).distance;
    if(total>limit)return total;
  }
  return total;
}
void internal_json(std::ostream& out,const std::array<uint64_t,6>& p) {
  out<<"[";for(int i=0;i<6;++i){if(i)out<<",";out<<p[i];}out<<"]";
}
void state_json(std::ostream& out,const State& state) {
  out<<"[";for(int e=0;e<15;++e) {
    if(e)out<<",";out<<"[";
    for(int u=0;u<10;++u){if(u)out<<",";out<<int(state[10*e+u]);}
    out<<"]";
  }out<<"]";
}
int main(int argc,char**argv) {
  assert(argc==3);start_cpu=double(std::clock())/CLOCKS_PER_SEC;make_catalog();
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
  assert(initial_score==7);
  nodes.push_back({initial,-1,-1,-1,-1,level,choose_current()});
  std::vector<int> queue{0};size_t cursor=0;
  std::set<State> seen{initial};
  long long candidates=0;int expanded=0,improvements=0;
  std::string stop="";
  while(stop.empty()) {
    if(level==0){stop="all_compatible_petersen_domains_nonempty";break;}
    if(cursor==queue.size()){stop="neutral_component_closed";break;}
    if(cpu()>=14.7){stop="cpu_budget";break;}
    int parent=queue[cursor++];State current=nodes[parent].state;
    decode(current);++expanded;bool improved=false;
    for(int e=0;e<15&&!improved&&stop.empty();++e)
      for(int u=0;u<10&&!improved&&stop.empty();++u)
        for(int v=u+1;v<10&&!improved&&stop.empty();++v) {
          if(cpu()>=14.7){stop="cpu_budget";break;}
          change(e,u,v);++candidates;int value=score(level);
          if(value<=level) {
            State child=current;std::swap(child[10*e+u],child[10*e+v]);
            if(!seen.count(child)) {
              if(nodes.size()>=500){stop="500_total_stored_states";}
              else {
                int child_id=nodes.size();
                nodes.push_back({child,parent,e,u,v,value,choose_current()});
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
  std::array<int,6> domain_sizes{},distances{};
  for(int i=0;i<6;++i) {distances[i]=domain(last_allowed[i]).distance;
    for(auto mask:catalog)domain_sizes[i]+=!(mask&~last_allowed[i]);}
  std::vector<int> path;
  for(int id=best_id;id!=-1;id=nodes[id].parent)path.push_back(id);
  std::reverse(path.begin(),path.end());
  std::ofstream out(argv[2]);out.precision(12);
  out<<"{\n\"initial_deficit\":"<<initial_score<<",\"best_deficit\":"<<level
     <<",\"stop\":\""<<stop<<"\",\"states_stored\":"<<nodes.size()
     <<",\"states_expanded\":"<<expanded<<",\"switch_candidates_checked\":"<<candidates
     <<",\"strict_improvements\":"<<improvements<<",\"internal_cpu_seconds\":"<<cpu()
     <<",\"best_permutations\":";state_json(out,nodes[best_id].state);
  out<<",\"best_internal_masks\":";internal_json(out,nodes[best_id].internal);
  out<<",\"catalog_size\":30240,\"cached_allowed_graphs\":"<<cache.size()<<",\"domain_queries\":"<<domain_queries<<",\"popcount_checks\":"<<popcount_checks;
  out<<",\"best_domain_sizes\":[";for(int i=0;i<6;++i){if(i)out<<",";out<<domain_sizes[i];}
  out<<"],\"minimum_forbidden_edges\":[";for(int i=0;i<6;++i){if(i)out<<",";out<<distances[i];}
  out<<"],\"path\":[";
  for(size_t r=0;r<path.size();++r){if(r)out<<",";const Node& node=nodes[path[r]];
    out<<"{\"state_id\":"<<path[r]<<",\"deficit\":"<<node.score<<",\"switch\":";
    if(node.pair<0)out<<"null";
    else out<<"["<<left_f[node.pair]<<","<<right_f[node.pair]<<","<<node.u<<","<<node.v<<"]";
    out<<",\"permutations\":";state_json(out,node.state);out<<",\"internal_masks\":";internal_json(out,node.internal);out<<"}";
  }
  out<<"]}\n";
  std::cout<<"initial="<<initial_score<<" best="<<level<<" stop="<<stop
           <<" stored="<<nodes.size()<<" expanded="<<expanded<<" candidates="<<candidates
           <<" cpu="<<cpu()<<"\n";
}
