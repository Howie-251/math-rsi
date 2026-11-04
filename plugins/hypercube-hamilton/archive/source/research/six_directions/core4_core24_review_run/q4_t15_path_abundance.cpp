#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
array<int,16>mate;vector<int>path;vector<vector<int>>witnesses;
int v,w,target,records,minimum;array<int,9>hist{};ofstream out;
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
  for(int y=1;y<16;y++)if(__builtin_popcount((unsigned)y)%2 && y!=v && y!=w){target=y;path={0};if(dfs(0,65534u&~(1u<<v)&~(1u<<w)))witnesses.push_back(path);}
  int k=witnesses.size();minimum=min(minimum,k);hist[k]++;
  for(int x:mate)out.put((char)(x<0?255:x));out.put((char)k);for(auto&p:witnesses)for(int x:p)out.put((char)x);
  return;
 }
 int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
 for(unsigned choices=rest;choices;choices&=choices-1){int y=__builtin_ctz(choices);mate[x]=y;mate[y]=x;generate(rest&~(1u<<y));mate[x]=mate[y]=-1;}
}
int main(int argc,char**argv){
 if(argc!=2)return 2;string base=argv[1];cout<<"[";bool sep=false;
 for(auto avoid:vector<pair<int,int>>{{1,2},{1,14},{2,4},{2,14}}){
  v=avoid.first;w=avoid.second;mate.fill(-1);records=0;minimum=8;hist.fill(0);
  out.open(base+"/q4_t15_path_abundance_"+to_string(v)+"_"+to_string(w)+".bin",ios::binary);
  unsigned free=65535u;for(int x:{0,7,11,13,v,w})free&=~(1u<<x);generate(free);out.close();
  if(sep)cout<<",";sep=true;cout<<"{\"avoid\":["<<v<<","<<w<<"],\"records\":"<<records<<",\"minimum\":"<<minimum<<",\"hist\":[";
  for(int i=0;i<9;i++){if(i)cout<<",";cout<<hist[i];}cout<<"]}"<<flush;
 }cout<<"]\n";
}
