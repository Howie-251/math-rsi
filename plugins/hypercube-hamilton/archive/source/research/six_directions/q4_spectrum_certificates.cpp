// Positive certificates for optional-edge lower bounds, not exact spectra.
#include <array>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
array<int,16> mate{};
array<array<unsigned long long,16>,16> bit{};
unsigned long long spectrum;
int root,forbidden,threshold,count,bad,maxcycles;
vector<int> path;
vector<vector<int>> cycles;
ofstream out;
int pc(unsigned x){return __builtin_popcount(x);}
bool enough(){return __builtin_popcountll(spectrum)>=threshold;}
void dfs(int endpoint,unsigned unused,unsigned long long chosen){
  if(enough())return;
  if(!unused){
    if(pc(endpoint^root)==1){
      auto h=chosen|bit[endpoint][root];
      if(h&~spectrum){spectrum|=h;cycles.push_back(path);}
    }
    return;
  }
  for(int i=0;i<4;i++){
    int x=endpoint^(1<<i);
    if(!(unused>>x&1))continue;
    int y=mate[x];path.push_back(x);
    if(y<0)dfs(x,unused&~(1u<<x),chosen|bit[endpoint][x]);
    else{
      path.push_back(y);
      dfs(y,unused&~(1u<<x)&~(1u<<y),chosen|bit[endpoint][x]);
      path.pop_back();
    }
    path.pop_back();
    if(enough())return;
  }
}
void generate(unsigned free){
  if(!free){
    count++;spectrum=0;cycles.clear();path={root};
    unsigned unused=65535u&~(1u<<root);
    if(forbidden>=0)unused&=~(1u<<forbidden);
    dfs(root,unused,0);
    if(!enough())bad++;
    maxcycles=max(maxcycles,(int)cycles.size());
    for(int x:mate)out.put(static_cast<char>(x<0?255:x));
    out.put(static_cast<char>(cycles.size()));
    for(const auto&c:cycles)for(int x:c)out.put(static_cast<char>(x));
    return;
  }
  int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
  for(unsigned choices=rest;choices;choices&=choices-1){
    int y=__builtin_ctz(choices);mate[x]=y;mate[y]=x;
    generate(rest&~(1u<<y));mate[x]=mate[y]=-1;
  }
}
int main(int argc,char**argv){
  if(argc<2)return 2;
  int i=0;
  for(int x=0;x<16;x++)for(int y=x+1;y<16;y++)if(pc(x^y)==1)bit[x][y]=bit[y][x]=1ull<<i++;
  cout<<"{\"scope\":\"positive optional-edge lower-bound certificates\",\"files\":[";bool sep=false;
  for(char mode:{'A','B'})for(int s:mode=='A'?vector<int>{3,15}:vector<int>{1,7}){
    root=mode=='A'?s:0;forbidden=mode=='A'?0:-1;threshold=mode=='A'?15:18;
    mate.fill(-1);count=bad=maxcycles=0;
    string name="q4_spectrum_"+string(1,mode)+"_"+to_string(s)+".bin";
    out.open(string(argv[1])+"/"+name,ios::binary);if(!out)return 3;
    generate(65535u&~1u&~(1u<<s));out.close();
    if(sep)cout<<",";sep=true;
    cout<<"{\"file\":\""<<name<<"\",\"matchings\":"<<count<<",\"threshold\":"<<threshold<<",\"failed\":"<<bad<<",\"max_cycles_per_record\":"<<maxcycles<<"}";
  }
  cout<<"],\"full_p6_proved\":false}\n";
}
