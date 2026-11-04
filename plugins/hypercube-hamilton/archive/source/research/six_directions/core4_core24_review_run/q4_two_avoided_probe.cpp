// Four same-parity holes; avoid two prescribed ones, include other two.
#include <array>
#include <iostream>
#include <vector>
#include <cstdint>
#include <fstream>
#include <string>
using namespace std;
array<int,16> mate{};
int forbidden2,start,free2;
uint64_t tested=0,bad=0,nodes=0;
vector<array<int,16>> failures;
vector<int> path;
ofstream certificates;
int pc(unsigned x){return __builtin_popcount(x);}
bool dfs(int endpoint,unsigned unused){
  nodes++;
  if(!unused)return pc(endpoint^start)==1;
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
    path={start};
    if(!dfs(start,65535u&~1u&~(1u<<forbidden2)&~(1u<<start))){bad++;if(failures.size()<2)failures.push_back(mate);}
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
  cout<<"{\"scope\":\"Q4 four same-parity holes, two prescribed avoided vertices, exact 14-cycle\",\"configs\":[";
  bool comma=false;
  for(int p:{3,15})for(int b=1;b<16;b++)if(pc(b)%2==0&&b!=p)
  for(int t=b+1;t<16;t++)if(pc(t)%2==0&&t!=p){
    mate.fill(-1);forbidden2=p;start=b;free2=t;tested=bad=nodes=0;failures.clear();
    if(argc>1)certificates.open(string(argv[1])+"/q4_two_avoided_"+to_string(p)+"_"+to_string(b)+"_"+to_string(t)+".bin",ios::binary);
    generate(65535u&~1u&~(1u<<p)&~(1u<<b)&~(1u<<t));
    if(certificates.is_open())certificates.close();
    if(comma)cout<<",";comma=true;
    cout<<"{\"holes\":[0,"<<p<<","<<b<<","<<t<<"],\"avoided\":[0,"<<p<<"],\"tested\":"<<tested<<",\"bad\":"<<bad<<",\"search_nodes\":"<<nodes<<",\"first_failures\":[";
    bool comma2=false;
    for(auto f:failures){if(comma2)cout<<",";comma2=true;cout<<"[";bool comma3=false;
      for(int x=0;x<16;x++)if(f[x]>x){if(comma3)cout<<",";comma3=true;cout<<"["<<x<<","<<f[x]<<"]";}
      cout<<"]";
    }
    cout<<"]}";
  }
  cout<<"],\"full_p6_proved\":false}\n";
}
