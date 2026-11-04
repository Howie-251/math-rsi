// Exhaustive positive path certificates; negative rows are diagnostics only.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
array<int,16> mate; vector<int> path; ofstream out;
int b,z,root,records,bad; unsigned long long nodes;
bool dfs(int endpoint,unsigned unused){
 ++nodes;
 if(!unused)return endpoint!=z && (__builtin_popcount((unsigned)endpoint)%2==1);
 for(int j=0;j<4;j++){
  int x=endpoint^(1<<j);if(!(unused>>x&1))continue;
  int y=mate[x];path.push_back(x);
  if(y<0){if(dfs(x,unused&~(1u<<x)))return true;}
  else if(unused>>y&1){path.push_back(y);if(dfs(y,unused&~(1u<<x)&~(1u<<y)))return true;path.pop_back();}
  path.pop_back();
 }
 return false;
}
void generate(unsigned free){
 if(!free){
  records++;path={root};bool ok=dfs(root,65535u&~1u&~(1u<<root));
  if(!ok)bad++;
  for(int x:mate)out.put((char)(x<0?255:x));
  if(ok)for(int x:path)out.put((char)x);else for(int j=0;j<15;j++)out.put((char)255);
  return;
 }
 int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
 for(unsigned choices=rest;choices;choices&=choices-1){int y=__builtin_ctz(choices);mate[x]=y;mate[y]=x;generate(rest&~(1u<<y));mate[x]=mate[y]=-1;}
}
int main(int argc,char**argv){
 if(argc!=2)return 2;string base=argv[1];ifstream configs(base+"/q4_balanced_avoid_path_configs.txt");
 if(!configs)return 3;cout<<"{\"scope\":\"Q4 balanced four-hole alternate endpoint avoiding 0\",\"files\":[";bool sep=false;
 while(configs>>b>>z>>root){
  string name="q4_balanced_avoid_path_"+to_string(b)+"_"+to_string(z)+"_"+to_string(root)+".bin";
  mate.fill(-1);records=bad=0;nodes=0;out.open(base+"/"+name,ios::binary);if(!out)return 4;
  generate(65535u&~1u&~(1u<<b)&~(1u<<z)&~(1u<<root));out.close();
  if(sep)cout<<",";sep=true;cout<<"{\"b\":"<<b<<",\"z\":"<<z<<",\"root\":"<<root<<",\"file\":\""<<name<<"\",\"records\":"<<records<<",\"failed\":"<<bad<<",\"nodes\":"<<nodes<<"}"<<flush;
 }
 cout<<"]}\n";
}
