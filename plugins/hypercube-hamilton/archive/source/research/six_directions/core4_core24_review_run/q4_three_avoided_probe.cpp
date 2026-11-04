// Exhaustive arbitrary K(Q4) matchings with four holes, retain hole 0,
// omit two even holes and one odd hole. First positive cycle certificates.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
using namespace std;
array<int,16> mate;vector<int> path;unsigned support;ofstream out;
unsigned long long positive,negative,nodes;int e1,e2,o;
bool dfs(int end,unsigned unused){
 ++nodes;if(!unused)return __builtin_popcount(unsigned(end))==1;
 for(int j=0;j<4;j++){
  int x=end^(1<<j);if(!(unused>>x&1u))continue;int y=mate[x];
  if(y<0||!(unused>>y&1u))continue;
  path.push_back(x);path.push_back(y);
  if(dfs(y,unused&~(1u<<x)&~(1u<<y)))return true;
  path.pop_back();path.pop_back();
 }
 return false;
}
void enumerate(unsigned unused){
 if(!unused){
  path={0};bool ok=dfs(0,support&~1u);if(ok)++positive;else ++negative;
  for(int x:mate)out.put(char(x<0?255:x));
  for(int i=0;i<13;i++)out.put(char(ok?path[i]:255));return;
 }
 int a=__builtin_ctz(unused);unsigned rest=unused&~(1u<<a);
 for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);mate[a]=b;mate[b]=a;enumerate(rest&~(1u<<b));mate[a]=mate[b]=-1;}
}
int main(int argc,char**argv){
 if(argc!=5)return 2;e1=stoi(argv[1]);e2=stoi(argv[2]);o=stoi(argv[3]);
 if(!e1||!e2||e1==e2||(__builtin_popcount(unsigned(e1))%2)||(__builtin_popcount(unsigned(e2))%2)||!(__builtin_popcount(unsigned(o))%2))return 3;
 out.open(argv[4],ios::binary);mate.fill(-1);support=65535u&~(1u<<e1)&~(1u<<e2)&~(1u<<o);
 enumerate(support&~1u);out.close();
 cout<<"{\"holes\":[0,"<<e1<<","<<e2<<","<<o<<"],\"avoided\":["<<e1<<","<<e2<<","<<o<<"],\"positive\":"<<positive<<",\"negative\":"<<negative<<",\"nodes\":"<<nodes<<"}\n";
}
