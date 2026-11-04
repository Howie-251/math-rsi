// Exact search on all residual Q4 A4 hole orbits and arbitrary matchings.
#include <array>
#include <iostream>
#include <vector>
#include <cstdint>
#include <fstream>
#include <string>
using namespace std;
array<int,16> mate{};
int forbidden;
uint64_t tested=0,bad=0,nodes=0;
vector<array<int,16>> failures;
vector<int> path;
ofstream certificates;
int pc(unsigned x){return __builtin_popcount(x);}
bool dfs(int endpoint,unsigned unused){
  nodes++;
  if(!unused)return pc(endpoint)==1;
  for(int i=0;i<4;i++){
    int x=endpoint^(1<<i);
    if(!(unused>>x&1))continue;
    int y=mate[x];
    path.push_back(x);
    if(y<0){if(dfs(x,unused&~(1u<<x)))return true;}
    else{
      path.push_back(y);
      if(dfs(y,unused&~(1u<<x)&~(1u<<y)))return true;
      path.pop_back();
    }
    path.pop_back();
  }
  return false;
}
void generate(unsigned free){
  if(!free){
    tested++;
    path={0};
    if(!dfs(0,65535u&~1u&~(1u<<forbidden))){bad++;if(failures.size()<20)failures.push_back(mate);}
    else if(certificates.is_open()){
      for(int x:mate)certificates.put(static_cast<char>(x<0?255:x));
      for(int x:path)certificates.put(static_cast<char>(x));
    }
    return;
  }
  int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
  for(unsigned choices=rest;choices;choices&=choices-1){
    int y=__builtin_ctz(choices);mate[x]=y;mate[y]=x;
    generate(rest&~(1u<<y));mate[x]=mate[y]=-1;
  }
}
int main(int argc,char**argv){
  cout<<"{\"scope\":\"Q4 A4 exact 15-vertex circle search, residual holes 0,7,11,v\",\"orbits\":[";
  bool comma=false;
  for(int v:{1,4,13}){
    mate.fill(-1);forbidden=v;tested=bad=nodes=0;failures.clear();
    if(argc>1)certificates.open(string(argv[1])+"/q4_four_hole_"+to_string(v)+".bin",ios::binary);
    generate(65535u&~1u&~(1u<<7)&~(1u<<11)&~(1u<<v));
    if(certificates.is_open())certificates.close();
    if(comma)cout<<",";comma=true;
    cout<<"{\"forbidden\":"<<v<<",\"tested\":"<<tested<<",\"bad\":"<<bad<<",\"search_nodes\":"<<nodes<<",\"first_failures\":[";
    bool comma2=false;
    for(auto f:failures){if(comma2)cout<<",";comma2=true;cout<<"[";bool comma3=false;
      for(int x=0;x<16;x++)if(f[x]>x){if(comma3)cout<<",";comma3=true;cout<<"["<<x<<","<<f[x]<<"]";}
      cout<<"]";
    }
    cout<<"]}";
  }
  cout<<"],\"full_p6_proved\":false}\n";
}
