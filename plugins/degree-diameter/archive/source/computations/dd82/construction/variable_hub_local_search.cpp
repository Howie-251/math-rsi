// Exact local hub assembly: two independent column permutations, symmetric C.
#include <algorithm>
#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
struct Choice { int z,y,c; };
struct Solver {
  std::array<int,10> mate{},zc{},yc{},c{},pz{},py{};
  std::array<std::vector<Choice>,10> domain;
  long long nodes=0, leaves=0, disconnected=0;
  bool capped=false;
  clock_t start;
  bool connected() {
    int seen=1,old=0;
    while(seen!=old) {
      old=seen;
      for(int i=0;i<10;i++) if((seen>>i)&1) seen|=c[i];
    }
    return seen==1023;
  }
  bool visit(int assigned,int usedz,int usedy) {
    ++nodes;
    if((nodes&1023)==0 && double(clock()-start)/CLOCKS_PER_SEC>=10) {
      capped=true; return false;
    }
    if(assigned==1023) {
      ++leaves;
      if(!connected()) { ++disconnected; return false; }
      return true;
    }
    int selected=-1;
    std::vector<Choice> choices;
    for(int v=0;v<10;v++) if(!((assigned>>v)&1)) {
      int expected=0;
      for(int u=0;u<10;u++) if(((assigned>>u)&1)&&((c[u]>>v)&1)) expected|=1<<u;
      std::vector<Choice> available;
      for(auto t:domain[v])
        if(!((usedz>>t.z)&1)&&!((usedy>>t.y)&1)&&(t.c&assigned)==expected)
          available.push_back(t);
      if(available.empty()) return false;
      if(selected<0 || available.size()<choices.size()) {
        selected=v; choices=std::move(available);
      }
    }
    for(auto t:choices) {
      c[selected]=t.c; pz[selected]=t.z; py[selected]=t.y;
      if(visit(assigned|(1<<selected),usedz|(1<<t.z),usedy|(1<<t.y))) return true;
      if(capped) return false;
    }
    return false;
  }
};
template<class T> void arr(std::ostream& out,const T& a) {
  out<<'['; bool comma=false;
  for(auto x:a) { if(comma)out<<',';comma=true;out<<x; }
  out<<']';
}
int main(int argc,char**argv) {
  if(argc!=3)return 2;
  std::ifstream in(argv[1]); std::ofstream out(argv[2]);
  int count;in>>count;clock_t start=clock();bool cap=false;
  int found_count=0,zero_count=0,pending_count=0;
  for(int a=0;a<count;a++) {
    int config,index;in>>config>>index;Solver s;s.start=start;
    for(int&x:s.mate)in>>x;
    for(int&x:s.zc)in>>x;
    for(int&x:s.yc)in>>x;
    for(int v=0;v<10;v++) {
      int forbidden=(1<<v)|(1<<s.mate[v]);
      for(int z=0;z<10;z++)for(int y=0;y<10;y++)
        if(!(s.zc[z]&forbidden)&&!(s.yc[y]&forbidden)&&!(s.zc[z]&s.yc[y]))
          s.domain[v].push_back({z,y,1023^(forbidden|s.zc[z]|s.yc[y])});
    }
    bool found=false;
    if(!cap)found=s.visit(0,0,0);
    if(s.capped)cap=true;
    const char* status=found?"witness":cap?"unknown_cpu_cap":"complete_no_witness";
    if(found)++found_count;else if(cap)++pending_count;else++zero_count;
    out<<"{\"configuration\":"<<config<<",\"matching_index\":"<<index
       <<",\"status\":\""<<status<<"\",\"nodes\":"<<s.nodes
       <<",\"complete_leaves\":"<<s.leaves<<",\"disconnected_leaves\":"<<s.disconnected
       <<",\"initial_domain_sizes\":[";
    for(int v=0;v<10;v++){if(v)out<<',';out<<s.domain[v].size();}out<<']';
    if(found) {
      out<<",\"Z_column_for_target\":";arr(out,s.pz);
      out<<",\"Y_column_for_target\":";arr(out,s.py);
      out<<",\"C_column_masks\":";arr(out,s.c);
    }
    out<<"}\n";
  }
  std::cout<<"{\"states\":"<<count<<",\"witness_states\":"<<found_count
           <<",\"complete_zero_states\":"<<zero_count<<",\"unknown_states\":"<<pending_count
           <<",\"all_states_decided\":"<<(cap?"false":"true")
           <<",\"all_solutions_enumerated\":false,\"cpu_seconds\":"
           <<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
}
