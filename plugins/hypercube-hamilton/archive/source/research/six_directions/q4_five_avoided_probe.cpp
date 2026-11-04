// Complete positive witness table: five omitted vertices, retained free0.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <set>
using namespace std;
array<int,16> mate;vector<int> path;unsigned support;ofstream out;
unsigned long long positive=0,negative=0,nodes=0;
bool dfs(int end,unsigned unused){
 ++nodes;if(!unused)return __builtin_popcount(unsigned(end))==1;
 for(int j=0;j<4;j++){
  int a=end^(1<<j);if(!(unused>>a&1u))continue;int b=mate[a];
  if(b<0||!(unused>>b&1u))continue;
  path.push_back(a);path.push_back(b);
  if(dfs(b,unused&~(1u<<a)&~(1u<<b)))return true;
  path.pop_back();path.pop_back();
 }
 return false;
}
void enumerate(unsigned unused){
 if(!unused){
  path={0};bool ok=dfs(0,support&~1u);if(ok)++positive;else ++negative;
  for(int x:mate)out.put(char(x<0?255:x));
  for(int i=0;i<11;i++)out.put(char(ok?path[i]:255));return;
 }
 int a=__builtin_ctz(unused);unsigned rest=unused&~(1u<<a);
 for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);mate[a]=b;mate[b]=a;enumerate(rest&~(1u<<b));mate[a]=mate[b]=-1;}
}
int main(int argc,char**argv){
 if(argc!=7)return 2;support=65535u;set<int>omitted;
 for(int i=1;i<=5;i++){int v=stoi(argv[i]);if(v<=0||v>=16||!omitted.insert(v).second)return 3;support&=~(1u<<v);}
 out.open(argv[6],ios::binary);mate.fill(-1);enumerate(support&~1u);out.close();
 cout<<"{\"positive\":"<<positive<<",\"negative\":"<<negative<<",\"nodes\":"<<nodes<<"}\n";
}
