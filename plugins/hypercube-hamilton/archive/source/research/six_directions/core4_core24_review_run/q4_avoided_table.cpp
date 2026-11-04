// Complete distance-three avoided-circle table, with positive witnesses.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
using namespace std;
array<int,16> mate{};
vector<int> path;
ofstream out;
int tested=0,bad=0;
int hole=7,start=1;
bool dfs(int endpoint,unsigned unused){
  if(!unused)return __builtin_popcount(endpoint^start)==1;
  for(int i=0;i<4;i++){
    int x=endpoint^(1<<i);
    if(!(unused>>x&1))continue;
    int y=mate[x];path.push_back(x);path.push_back(y);
    if(dfs(y,unused&~(1u<<x)&~(1u<<y)))return true;
    path.pop_back();path.pop_back();
  }
  return false;
}
void generate(unsigned free){
  if(!free){
    tested++;path={start,mate[start]};
    bool ok=dfs(mate[start],65535u&~1u&~(1u<<hole)&~(1u<<start)&~(1u<<mate[start]));
    if(!ok)bad++;
    for(int x:mate)out.put(static_cast<char>(x<0?255:x));
    for(int i=0;i<14;i++)out.put(static_cast<char>(ok?path[i]:255));
    return;
  }
  int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
  for(unsigned choices=rest;choices;choices&=choices-1){
    int y=__builtin_ctz(choices);mate[x]=y;mate[y]=x;
    generate(rest&~(1u<<y));mate[x]=mate[y]=-1;
  }
}
int main(int argc,char**argv){
  if(argc<2)return 2;if(argc>2)hole=stoi(argv[2]);if(hole!=1&&hole!=7)return 4;
  start=hole==1?2:1;out.open(argv[1],ios::binary);if(!out)return 3;
  mate.fill(-1);generate(65535u&~1u&~(1u<<hole));
  cout<<"{\"matching_records\":"<<tested<<",\"positive\":"<<tested-bad<<",\"negative\":"<<bad<<",\"holes\":[0,"<<hole<<"]}\n";
}
