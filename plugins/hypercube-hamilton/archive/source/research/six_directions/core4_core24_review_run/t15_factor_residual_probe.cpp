// Worst required-short-edge deletion Hall bound for 54 hard T15 geometries.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
using namespace std;
struct Sub{unsigned neighbors;array<unsigned,16>unique;int demand;};
int main(int argc,char**argv){
 if(argc!=2)return 2;vector<int>E,O;for(int x=0;x<32;x++)(__builtin_popcount((unsigned)x)%2?O:E).push_back(x);
 vector<Sub>subs(65536);
 for(unsigned s=1;s<65536;s++){
  auto&r=subs[s];r.neighbors=0;r.unique.fill(0);r.demand=__builtin_popcount(s)+(s&1u);
  for(int j=0;j<16;j++){
   unsigned owners=0;for(int i=0;i<16;i++)if((s>>i&1)&&__builtin_popcount((unsigned)(E[i]^O[j]))==1)owners|=1u<<i;
   if(owners){r.neighbors|=1u<<j;if(__builtin_popcount(owners)==1)r.unique[__builtin_ctz(owners)]|=1u<<j;}
  }
 }
 ifstream in(argv[1]);int id,v,w,a,b,c;bool sep=false;cout<<"[";
 while(in>>id>>v>>w>>a>>b>>c){
  unsigned forbidden=0,freeO=0;for(int j=0;j<16;j++){if(O[j]==v||O[j]==w)forbidden|=1u<<j;if(O[j]==a||O[j]==b||O[j]==c)freeO|=1u<<j;}
  unsigned covered=65535u&~(forbidden|freeO);int minimum=100;unsigned bad=0;
  for(unsigned s=1;s<65536;s++){
   auto&r=subs[s];int loss=0;for(int i=1;i<16;i++)loss+=(r.unique[i]&covered)!=0;
   int slack=__builtin_popcount(r.neighbors&~forbidden)+__builtin_popcount(r.neighbors&freeO)-loss-r.demand;
   minimum=min(minimum,slack);if(slack<0&&!bad)bad=s;
  }
  if(sep)cout<<",";sep=true;cout<<"{\"core\":"<<id<<",\"minimum_slack\":"<<minimum<<",\"first_negative_subset_mask\":"<<bad<<"}"<<flush;
 }cout<<"]\n";
}
