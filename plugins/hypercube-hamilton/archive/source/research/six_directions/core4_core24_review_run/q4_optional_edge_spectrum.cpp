// Exact optional-short-edge spectrum for Q4 N14_4 representative matchings.
// Diagnostic only: no universal Q5 conclusion without a separate proof.
#include <array>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdint>
using namespace std;
array<int,16> mate{};
array<array<uint64_t,16>,16> bit{};
uint64_t available,spectrum,nodes;
int hole;
int pc(unsigned x){return __builtin_popcount(x);}
void dfs(int endpoint,unsigned unused,uint64_t chosen){
  nodes++;
  if(spectrum==available)return;
  if(!unused){if(pc(endpoint^hole)==1)spectrum|=chosen|bit[endpoint][hole];return;}
  for(int i=0;i<4;i++){
    int x=endpoint^(1<<i);
    if(!(unused>>x&1))continue;
    int y=mate[x];
    dfs(y,unused&~(1u<<x)&~(1u<<y),chosen|bit[endpoint][x]);
    if(spectrum==available)return;
  }
}
int main(int argc,char**argv){
  if(argc<2)return 2;
  int index=0;
  for(int x=0;x<16;x++)for(int y=x+1;y<16;y++)if(pc(x^y)==1)bit[x][y]=bit[y][x]=1ull<<index++;
  cout<<"{\"scope\":\"all possible optional short edges in Q4 N14_4 cycles\",\"orbits\":[";
  bool sep=false;
  for(int s:{3,15}){
    ifstream in(string(argv[1])+"/q4_two_hole_"+to_string(s)+".bin",ios::binary);
    if(!in)return 3;
    hole=s;nodes=0;int count=0,minsize=100;uint64_t missingcases=0;array<uint64_t,33> histogram{};
    array<int,16> witness{};uint64_t witness_spectrum=0;unsigned char rec[31];
    while(in.read(reinterpret_cast<char*>(rec),31)){
      for(int x=0;x<16;x++)mate[x]=rec[x]==255?-1:rec[x];
      available=0;spectrum=0;
      for(int x=1;x<16;x++)for(int y=x+1;y<16;y++)if(pc(x^y)==1&&mate[x]!=y)available|=bit[x][y];
      dfs(hole,65535u&~1u&~(1u<<hole),0);
      int size=__builtin_popcountll(spectrum);histogram[size]++;count++;
      if(spectrum!=available)missingcases++;
      if(size<minsize){minsize=size;witness=mate;witness_spectrum=spectrum;}
    }
    if(sep)cout<<",";sep=true;
    cout<<"{\"other_hole\":"<<s<<",\"matchings\":"<<count<<",\"minimum_optional_edges\":"<<minsize<<",\"nonfull_spectra\":"<<missingcases<<",\"nodes\":"<<nodes<<",\"histogram\":[";
    for(int k=0;k<=32;k++){if(k)cout<<",";cout<<histogram[k];}
    cout<<"],\"minimum_witness_matching\":[";bool comma=false;
    for(int x=0;x<16;x++)if(witness[x]>x){if(comma)cout<<",";comma=true;cout<<"["<<x<<","<<witness[x]<<"]";}
    cout<<"],\"minimum_witness_optional_edges\":[";comma=false;
    for(int x=0;x<16;x++)for(int y=x+1;y<16;y++)if(bit[x][y]&witness_spectrum){if(comma)cout<<",";comma=true;cout<<"["<<x<<","<<y<<"]";}
    cout<<"]}";
  }
  cout<<"],\"full_p6_proved\":false}\n";
}
