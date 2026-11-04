// Exact Hall lower bound over all normalized residual A6 geometries.
// a=0,z=3 or15 even; three allowed odd holes avoid N(a) and N(z).
#include <array>
#include <vector>
#include <iostream>
#include <cstdint>
using namespace std;
int pc(unsigned x){return __builtin_popcount(x);}
int main(){
 vector<int>E,O;for(int x=0;x<32;x++)(pc(x)%2?O:E).push_back(x);
 struct Data{unsigned s,n;array<unsigned,16>leaf;int k;};vector<Data>all;
 for(unsigned s=0;s<65536;s++){
  Data d{s,0,{},pc(s)};
  for(int j=0;j<16;j++){
   unsigned who=0;for(int i=0;i<16;i++)if((s>>i&1)&&pc(E[i]^O[j])==1)who|=1u<<i;
   if(who)d.n|=1u<<j;
   if(pc(who)==1)d.leaf[__builtin_ctz(who)]|=1u<<j;
  }all.push_back(d);
 }
 cout<<"{\"scope\":\"A6 residual Hall bound; not connectivity proof\",\"orbits\":[";bool comma=false;
 for(int z:{3,15}){
  int zi=0;while(E[zi]!=z)zi++;vector<int>far;
  for(int j=0;j<16;j++)if(pc(O[j])!=1&&pc(O[j]^z)!=1)far.push_back(j);
  uint64_t tested=0,negative=0;int configs=0;array<int,17>minima;minima.fill(100);
  if(comma)cout<<",";comma=true;cout<<"{\"z\":"<<z<<",\"first_failure\":";bool printed=false;
  for(int bi=0;bi<(int)far.size();bi++)for(int ti=bi+1;ti<(int)far.size();ti++)for(int si=ti+1;si<(int)far.size();si++){
   int b=far[bi],t=far[ti],s=far[si];
   for(int v=0;v<16;v++)if(v!=b&&v!=t&&v!=s){
    configs++;unsigned blocked=(1u<<b)|(1u<<t)|(1u<<s)|(1u<<v);
    for(const auto&d:all){
     int removed=0;for(int i=1;i<16;i++)if(i!=zi&&(d.leaf[i]&~blocked))removed++;
     int bound=pc(d.n&~(1u<<v))+bool(d.n>>b&1)+bool(d.n>>t&1)+bool(d.n>>s&1)-removed;
     int slack=bound-d.k-bool(d.s&1)-bool(d.s>>zi&1);
     tested++;minima[d.k]=min(minima[d.k],slack);
     if(slack<0){
      negative++;
      if(!printed){
       printed=true;cout<<"{\"holes\":[0,"<<z<<","<<O[b]<<","<<O[t]<<","<<O[s]<<","<<O[v]<<"],\"forbidden\":"<<O[v]<<",\"S\":[";bool sep=false;
       for(int i=0;i<16;i++)if(d.s>>i&1){if(sep)cout<<",";sep=true;cout<<E[i];}
       cout<<"],\"slack\":"<<slack<<",\"forced_short_edges\":[";sep=false;
       for(int i=1;i<16;i++)if(i!=zi&&(d.leaf[i]&~blocked)){int j=__builtin_ctz(d.leaf[i]&~blocked);if(sep)cout<<",";sep=true;cout<<"["<<E[i]<<","<<O[j]<<"]";}
       cout<<"]}";
      }
     }
    }
   }
  }
  if(!printed)cout<<"null";
  cout<<",\"hole_configurations\":"<<configs<<",\"subsets_tested\":"<<tested<<",\"negative_bounds\":"<<negative<<",\"minimum_slacks\":[";
  for(int i=0;i<=16;i++){if(i)cout<<",";cout<<minima[i];}cout<<"]}";
 }
 cout<<"],\"a6_proved\":false,\"full_p6_proved\":false}\n";
}
