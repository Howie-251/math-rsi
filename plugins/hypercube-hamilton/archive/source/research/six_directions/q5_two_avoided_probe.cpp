// Diagnostic search only. Positive witnesses independently checkable.
#include <array>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;
array<int,32> mate;vector<int> path;unsigned long long nodes,limit=2000000;bool timeout;
bool dfs(int end,unsigned unused){
 if(++nodes>limit){timeout=true;return false;}
 if(!unused)return __builtin_popcount((unsigned)end)==1;
 for(int j=0;j<5;j++){
  int x=end^(1<<j);if(!(unused>>x&1))continue;int y=mate[x];path.push_back(x);
  if(y<0){if(dfs(x,unused&~(1u<<x)))return true;}
  else if(unused>>y&1){path.push_back(y);if(dfs(y,unused&~(1u<<x)&~(1u<<y)))return true;path.pop_back();}
  path.pop_back();if(timeout)return false;
 }
 return false;
}
int main(int argc,char**argv){
 if(argc!=2)return 2;ifstream in(argv[1]);int id,a,b,m;
 cout<<"[";bool sep=false;
 while(in>>id>>a>>b>>m){
  mate.fill(-1);for(int k=0;k<m;k++){int x,y;in>>x>>y;mate[x]=y;mate[y]=x;}
  nodes=0;timeout=false;path={0};bool ok=dfs(0,0xffffffffu&~1u&~(1u<<a)&~(1u<<b));
  if(sep)cout<<",";sep=true;cout<<"{\"id\":"<<id<<",\"status\":\""<<(ok?"FOUND":timeout?"UNKNOWN":"EXHAUSTED_NO_CYCLE")<<"\",\"nodes\":"<<nodes<<",\"cycle\":[";
  if(ok)for(int i=0;i<(int)path.size();i++){if(i)cout<<",";cout<<path[i];}
  cout<<"]}"<<flush;
 }
 cout<<"]\n";
}
