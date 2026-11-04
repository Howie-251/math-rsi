// Exhaustive Q4 path/cycle spectra; only positive witnesses are used downstream.
#include <array>
#include <vector>
#include <iostream>
#include <fstream>
#include <cstdint>
using namespace std;
array<int,16> mate;int edgeid[16][16];int root,target,cyclic;
vector<int> path;vector<vector<int>> witnesses;uint32_t spectrum;uint64_t count,nodes;
void accept(){
 uint32_t bits=0;int n=path.size();
 for(int i=0;i<n-1+cyclic;i++){int a=path[i],b=path[(i+1)%n];if(mate[a]!=b)bits|=1u<<edgeid[a][b];}
 ++count;if(bits&~spectrum){spectrum|=bits;witnesses.push_back(path);}
}
void dfs(int end,unsigned unused){
 ++nodes;
 if(!unused){if(cyclic?__builtin_popcount(unsigned(end^root))==1:end==target)accept();return;}
 if(!cyclic&&end==target)return;
 for(int j=0;j<4;j++){
  int x=end^(1<<j);if(!(unused>>x&1u))continue;int y=mate[x];path.push_back(x);
  if(y<0)dfs(x,unused&~(1u<<x));
  else if(unused>>y&1u){path.push_back(y);dfs(y,unused&~(1u<<x)&~(1u<<y));path.pop_back();}
  path.pop_back();
 }
}
int main(int argc,char**argv){
 if(argc!=2)return 2;int k=0;for(int a=0;a<16;a++)for(int b=a+1;b<16;b++)if(__builtin_popcount(unsigned(a^b))==1)edgeid[a][b]=edgeid[b][a]=k++;
 ifstream in(argv[1]);int id,m;unsigned support;bool sep=false;cout<<"[";
 while(in>>id>>cyclic>>support>>root>>target>>m){
  mate.fill(-1);for(int i=0;i<m;i++){int a,b;in>>a>>b;mate[a]=b;mate[b]=a;}
  path={root};spectrum=0;count=nodes=0;witnesses.clear();unsigned unused=support&~(1u<<root);int end=root;
  if(mate[root]>=0){end=mate[root];path.push_back(end);unused&=~(1u<<end);}
  dfs(end,unused);
  if(sep)cout<<",";sep=true;cout<<"{\"id\":"<<id<<",\"spectrum\":"<<spectrum<<",\"solutions\":"<<count<<",\"nodes\":"<<nodes<<",\"witnesses\":[";
  for(int i=0;i<(int)witnesses.size();i++){if(i)cout<<",";cout<<"[";for(int j=0;j<(int)witnesses[i].size();j++){if(j)cout<<",";cout<<witnesses[i][j];}cout<<"]";}cout<<"]}"<<flush;
 }
 cout<<"]\n";
}
