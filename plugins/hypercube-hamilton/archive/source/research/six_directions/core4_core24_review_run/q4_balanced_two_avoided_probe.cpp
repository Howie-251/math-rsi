// Complete arbitrary matching tables: holes0,7,r(even),y(odd), omit r,y.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
using namespace std;
array<int,16> mate;vector<int> path;unsigned support;ofstream out;
unsigned long long positive,negative,nodes;int r,y;
bool dfs(int end,unsigned unused){
 ++nodes;if(!unused)return __builtin_popcount(unsigned(end))==1;
 for(int j=0;j<4;j++){
  int x=end^(1<<j);if(!(unused>>x&1u))continue;int z=mate[x];path.push_back(x);
  if(z<0){if(dfs(x,unused&~(1u<<x)))return true;}
  else if(unused>>z&1u){path.push_back(z);if(dfs(z,unused&~(1u<<x)&~(1u<<z)))return true;path.pop_back();}
  path.pop_back();
 }return false;
}
void enumerate(unsigned unused){
 if(!unused){path={0};bool ok=dfs(0,support&~1u);if(ok)++positive;else ++negative;
  for(int z:mate)out.put(char(z<0?255:z));for(int i=0;i<14;i++)out.put(char(ok?path[i]:255));return;}
 int a=__builtin_ctz(unused);unsigned rest=unused&~(1u<<a);
 for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);mate[a]=b;mate[b]=a;enumerate(rest&~(1u<<b));mate[a]=mate[b]=-1;}
}
int main(int argc,char**argv){if(argc!=4)return 2;r=stoi(argv[1]);y=stoi(argv[2]);
 if(!r||(__builtin_popcount(unsigned(r))%2)||y==7||!(__builtin_popcount(unsigned(y))%2))return 3;
 out.open(argv[3],ios::binary);mate.fill(-1);support=65535u&~(1u<<r)&~(1u<<y);enumerate(support&~1u&~(1u<<7));out.close();
 cout<<"{\"avoided\":["<<r<<","<<y<<"],\"free_retained\":[0,7],\"positive\":"<<positive<<",\"negative\":"<<negative<<",\"nodes\":"<<nodes<<"}\n";
}
