#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
array<int,16>mate;vector<int>path;vector<vector<int>>witnesses;
int v,w,target,records,minimum,start;array<int,9>hist{};ofstream out;
bool dfs(int endpoint,unsigned unused){
 if(!unused)return endpoint==target;
 if(endpoint==target)return false;
 for(int j=0;j<4;j++){
  int x=endpoint^(1<<j);if(!(unused>>x&1))continue;int y=mate[x];path.push_back(x);
  if(y<0){if(dfs(x,unused&~(1u<<x)))return true;}
  else{path.push_back(y);if(dfs(y,unused&~(1u<<x)&~(1u<<y)))return true;path.pop_back();}
  path.pop_back();
 }
 return false;
}
void generate(unsigned free){
 if(!free){
  records++;witnesses.clear();
  for(int y=1;y<16;y++)if(__builtin_popcount((unsigned)y)%2 && y!=v && y!=w){target=y;path={start};if(dfs(start,65535u&~(1u<<start)&~(1u<<v)&~(1u<<w)))witnesses.push_back(path);}
  int k=witnesses.size();minimum=min(minimum,k);hist[k]++;
  for(int x:mate)out.put((char)(x<0?255:x));out.put((char)k);for(auto&p:witnesses)for(int x:p)out.put((char)x);
  return;
 }
 int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
 for(unsigned choices=rest;choices;choices&=choices-1){int y=__builtin_ctz(choices);mate[x]=y;mate[y]=x;generate(rest&~(1u<<y));mate[x]=mate[y]=-1;}
}
int main(int argc,char**argv){
 if(argc!=2)return 2;string base=argv[1];cout<<"[";bool sep=false;
 for(int p:{3,15})for(int b=1;b<16;b++)if(__builtin_popcount((unsigned)b)%2==0&&b!=p)
 for(int t=b+1;t<16;t++)if(__builtin_popcount((unsigned)t)%2==0&&t!=p){
  v=0;w=p;start=b;mate.fill(-1);records=0;minimum=8;hist.fill(0);
  out.open(base+"/q4_t44_path_abundance_"+to_string(p)+"_"+to_string(b)+"_"+to_string(t)+".bin",ios::binary);
  unsigned free=65535u;for(int x:{0,p,b,t})free&=~(1u<<x);generate(free);out.close();
  if(sep)cout<<",";sep=true;cout<<"{\"holes\":[0,"<<p<<","<<b<<","<<t<<"],\"records\":"<<records<<",\"minimum\":"<<minimum<<",\"hist\":[";
  for(int i=0;i<9;i++){if(i)cout<<",";cout<<hist[i];}cout<<"]}"<<flush;
 }cout<<"]\n";
}
