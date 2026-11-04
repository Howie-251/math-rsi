// Find every low-spectrum matching; high cases get positive union witnesses.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
array<int,16>mate;array<array<unsigned,16>,16>bits{};unsigned mask;
vector<int>path;vector<vector<int>>cycles;int hole,records,low;ofstream out,lowout;
bool enough(){return __builtin_popcount(mask)>=18;}
void dfs(int endpoint,unsigned unused,unsigned used){
 if(enough())return;
 if(!unused){if(__builtin_popcount((unsigned)(endpoint^hole))==1){unsigned h=used|bits[endpoint][hole];if(h&~mask){mask|=h;cycles.push_back(path);}}return;}
 for(int j=0;j<4;j++){
  int x=endpoint^(1<<j);if(!(unused>>x&1))continue;int y=mate[x];path.push_back(x);
  if(y<0)dfs(x,unused&~(1u<<x),used|bits[endpoint][x]);
  else{path.push_back(y);dfs(y,unused&~(1u<<x)&~(1u<<y),used|bits[endpoint][x]);path.pop_back();}
  path.pop_back();if(enough())return;
 }
}
void generate(unsigned free){
 if(!free){
  records++;mask=0;cycles.clear();path={hole};dfs(hole,65534u&~(1u<<hole),0);
  for(int x:mate)out.put((char)(x<0?255:x));out.put((char)cycles.size());for(auto& c:cycles)for(int x:c)out.put((char)x);
  if(!enough()){low++;lowout<<hole<<" "<<mask;for(int x:mate)lowout<<" "<<x;lowout<<"\n";}
  return;
 }
 int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
 for(unsigned choices=rest;choices;choices&=choices-1){int y=__builtin_ctz(choices);mate[x]=y;mate[y]=x;generate(rest&~(1u<<y));mate[x]=mate[y]=-1;}
}
int main(int argc,char**argv){
 if(argc!=2)return 2;string base=argv[1];int index=0;for(int x=0;x<16;x++)for(int y=x+1;y<16;y++)if(__builtin_popcount((unsigned)(x^y))==1)bits[x][y]=bits[y][x]=1u<<index++;
 lowout.open(base+"/q4_n14_low_spectra.txt");cout<<"[";bool sep=false;
 for(int p:{3,15}){hole=p;records=low=0;mate.fill(-1);out.open(base+"/q4_n14_rich_"+to_string(p)+".bin",ios::binary);generate(65534u&~(1u<<p));out.close();if(sep)cout<<",";sep=true;cout<<"{\"hole\":"<<p<<",\"records\":"<<records<<",\"low\":"<<low<<"}"<<flush;}
 cout<<"]\n";
}
