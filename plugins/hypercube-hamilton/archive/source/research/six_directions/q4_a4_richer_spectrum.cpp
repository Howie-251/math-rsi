// Positive optional-edge certificates for residual 4-hole Q4 types.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
array<int,16> mate{};array<array<unsigned long long,16>,16>bit{};
unsigned long long spectrum;int forbidden,threshold,records,bad,maxcycles;
vector<int>path;vector<vector<int>>cycles;ofstream out;
int pc(unsigned x){return __builtin_popcount(x);}
bool enough(){return __builtin_popcountll(spectrum)>=threshold;}
void dfs(int endpoint,unsigned unused,unsigned long long chosen){
 if(enough())return;
 if(!unused){if(pc(endpoint)==1){auto h=chosen|bit[endpoint][0];if(h&~spectrum){spectrum|=h;cycles.push_back(path);}}return;}
 for(int j=0;j<4;j++){
  int x=endpoint^(1<<j);if(!(unused>>x&1))continue;int y=mate[x];path.push_back(x);
  if(y<0)dfs(x,unused&~(1u<<x),chosen|bit[endpoint][x]);
  else{path.push_back(y);dfs(y,unused&~(1u<<x)&~(1u<<y),chosen|bit[endpoint][x]);path.pop_back();}
  path.pop_back();if(enough())return;
 }
}
void generate(unsigned free){
 if(!free){
  records++;spectrum=0;cycles.clear();path={0};unsigned unused=65534u;
  if(forbidden>=0)unused&=~(1u<<forbidden);dfs(0,unused,0);
  if(!enough())bad++;maxcycles=max(maxcycles,(int)cycles.size());
  for(int x:mate)out.put(static_cast<char>(x<0?255:x));out.put(static_cast<char>(cycles.size()));
  for(auto&c:cycles)for(int x:c)out.put(static_cast<char>(x));return;
 }
 int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
 for(unsigned choices=rest;choices;choices&=choices-1){int y=__builtin_ctz(choices);mate[x]=y;mate[y]=x;generate(rest&~(1u<<y));mate[x]=mate[y]=-1;}
}
int main(int argc,char**argv){
 if(argc!=2)return 2;int index=0;for(int x=0;x<16;x++)for(int y=x+1;y<16;y++)if(pc(x^y)==1)bit[x][y]=bit[y][x]=1ull<<index++;
 cout<<"{\"scope\":\"Q4 four-hole positive edge-set bounds\",\"files\":[";bool sep=false;
 for(int v:{1,4,13}){
  forbidden=v;threshold=18;mate.fill(-1);records=bad=maxcycles=0;
  vector<int>holes=v>=0?vector<int>{0,7,11,v}:vector<int>{0,3,13,14};unsigned free=65535u;for(int x:holes)free&=~(1u<<x);
  string name=v>=0?"q4_a4_rich_"+to_string(v)+".bin":"q4_four_spectrum_balanced.bin";
  out.open(string(argv[1])+"/"+name,ios::binary);if(!out)return 3;generate(free);out.close();
  if(sep)cout<<",";sep=true;cout<<"{\"file\":\""<<name<<"\",\"records\":"<<records<<",\"threshold\":"<<threshold<<",\"failed\":"<<bad<<",\"max_cycles\":"<<maxcycles<<"}";
 }
 cout<<"]}\n";
}
