// Optional-short-edge spectrum for arbitrary Q4 near-perfect opposite holes.
#include <array>
#include <iostream>
#include <cstdint>
using namespace std;
array<int,16> mate{};
array<array<uint64_t,16>,16> bit{};
uint64_t available,spectrum,nodes;
int hole,count,minsize;
uint64_t missingcases;
array<uint64_t,33> histogram{};
array<int,16> witness{};uint64_t witness_spectrum;
int pc(unsigned x){return __builtin_popcount(x);}
void dfs(int endpoint,unsigned unused,uint64_t chosen){
  nodes++;
  if(spectrum==available)return;
  if(!unused){if(pc(endpoint)==1)spectrum|=chosen|bit[endpoint][0];return;}
  for(int i=0;i<4;i++){
    int x=endpoint^(1<<i);
    if(!(unused>>x&1))continue;
    int y=mate[x];
    if(y<0)dfs(x,unused&~(1u<<x),chosen|bit[endpoint][x]);
    else dfs(y,unused&~(1u<<x)&~(1u<<y),chosen|bit[endpoint][x]);
    if(spectrum==available)return;
  }
}
void generate(unsigned free){
  if(!free){
    available=0;spectrum=0;
    for(int x=0;x<16;x++)for(int y=x+1;y<16;y++)if(pc(x^y)==1&&mate[x]!=y)available|=bit[x][y];
    dfs(0,65534u,0);
    int size=__builtin_popcountll(spectrum);histogram[size]++;count++;
    if(spectrum!=available)missingcases++;
    if(size<minsize){minsize=size;witness=mate;witness_spectrum=spectrum;}
    return;
  }
  int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
  for(unsigned choices=rest;choices;choices&=choices-1){
    int y=__builtin_ctz(choices);mate[x]=y;mate[y]=x;
    generate(rest&~(1u<<y));mate[x]=mate[y]=-1;
  }
}
int main(){
  int index=0;
  for(int x=0;x<16;x++)for(int y=x+1;y<16;y++)if(pc(x^y)==1)bit[x][y]=bit[y][x]=1ull<<index++;
  cout<<"{\"scope\":\"Q4 full circle optional edge spectra, opposite holes\",\"orbits\":[";bool sep=false;
  for(int s:{1,7}){
    mate.fill(-1);hole=s;nodes=0;count=0;minsize=100;missingcases=0;histogram.fill(0);
    generate(65535u&~1u&~(1u<<hole));
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
