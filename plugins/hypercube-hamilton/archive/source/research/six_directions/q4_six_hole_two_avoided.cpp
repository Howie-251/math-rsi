// Residual Q4 holes1/5, two majority holes forbidden; exact positive witnesses.
#include <array>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
array<int,16>mate{};vector<int>path;int v,w,records,bad;ofstream out;vector<array<int,16>>failures;
bool dfs(int endpoint,unsigned unused){
 if(!unused)return __builtin_popcount((unsigned)endpoint)==1;
 for(int i=0;i<4;i++){
  int x=endpoint^(1<<i);if(!(unused>>x&1))continue;int y=mate[x];path.push_back(x);
  if(y<0){if(dfs(x,unused&~(1u<<x)))return true;}
  else{path.push_back(y);if(dfs(y,unused&~(1u<<x)&~(1u<<y)))return true;path.pop_back();}
  path.pop_back();
 }return false;
}
void generate(unsigned free){
 if(!free){
  records++;path={0};bool ok=dfs(0,65534u&~(1u<<v)&~(1u<<w));
  if(!ok){bad++;if(failures.size()<4)failures.push_back(mate);}
  if(out.is_open()){for(int x:mate)out.put(static_cast<char>(x<0?255:x));for(int i=0;i<14;i++)out.put(static_cast<char>(ok?path[i]:255));}return;
 }
 int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
 for(unsigned c=rest;c;c&=c-1){int y=__builtin_ctz(c);mate[x]=y;mate[y]=x;generate(rest&~(1u<<y));mate[x]=mate[y]=-1;}
}
int main(int argc,char**argv){
 cout<<"{\"scope\":\"Q4 1/5 hole parity, two prescribed majority holes avoided\",\"orbits\":[";bool sep=false;
 for(auto p:vector<pair<int,int>>{{1,2},{1,14},{2,4},{2,14}}){
  v=p.first;w=p.second;records=bad=0;failures.clear();mate.fill(-1);
  if(argc>1)out.open(string(argv[1])+"/q4_six_two_avoided_"+to_string(v)+"_"+to_string(w)+".bin",ios::binary);
  unsigned free=65535u;for(int x:{0,7,11,13,v,w})free&=~(1u<<x);generate(free);if(out.is_open())out.close();
  if(sep)cout<<",";sep=true;cout<<"{\"avoided\":["<<v<<","<<w<<"],\"records\":"<<records<<",\"bad\":"<<bad<<",\"first_failures\":[";bool sp=false;
  for(auto f:failures){if(sp)cout<<",";sp=true;cout<<"[";bool sp2=false;for(int x=0;x<16;x++)if(f[x]>x){if(sp2)cout<<",";sp2=true;cout<<"["<<x<<","<<f[x]<<"]";}cout<<"]";}
  cout<<"]}";
 }cout<<"],\"full_p6_proved\":false}\n";
}
