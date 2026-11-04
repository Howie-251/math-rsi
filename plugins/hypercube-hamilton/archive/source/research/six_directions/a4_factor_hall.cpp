// Exhaustive geometry bound for the Hall condition; no matching enumeration.
// a=0 (even); b,t odd and nonadjacent to a; v a third odd vertex.
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int pc(unsigned x){return __builtin_popcount(x);}
int main(){
  vector<int>E,O;
  for(int x=0;x<32;x++) (pc(x)%2?O:E).push_back(x);
  array<unsigned,16> adj{};
  for(int i=0;i<16;i++)for(int j=0;j<16;j++)if(pc(E[i]^O[j])==1)adj[i]|=1u<<j;
  struct Data{unsigned s,n;array<unsigned,16> leaves;int k;};
  vector<Data> all;
  for(unsigned s=0;s<65536;s++){
    Data d{s,0,{},pc(s)};
    for(int j=0;j<16;j++){
      unsigned who=0;
      for(int i=0;i<16;i++)if((s>>i&1)&&(adj[i]>>j&1))who|=1u<<i;
      if(who)d.n|=1u<<j;
      if(pc(who)==1)d.leaves[__builtin_ctz(who)]|=1u<<j;
    }
    all.push_back(d);
  }
  array<int,17> mins;mins.fill(100);
  uint64_t tested=0,failures=0;int configurations=0;
  cout<<"{\"first_failure\":";
  bool printed=false;
  for(int bi=0;bi<16;bi++)if(pc(O[bi])!=1)
  for(int ti=bi+1;ti<16;ti++)if(pc(O[ti])!=1)
  for(int vi=0;vi<16;vi++)if(vi!=bi&&vi!=ti){
    configurations++;
    unsigned blocked=(1u<<bi)|(1u<<ti)|(1u<<vi);
    for(const auto&d:all){
      int removed=0;
      for(int i=1;i<16;i++)if(d.leaves[i]&~blocked)removed++;
      int demand=d.k+(d.s&1);
      int bound=pc(d.n&~(1u<<vi))+bool(d.n>>bi&1)+bool(d.n>>ti&1)-removed;
      int slack=bound-demand;
      mins[d.k]=min(mins[d.k],slack);tested++;
      if(slack<0){
        failures++;
        if(!printed){
          printed=true;
          cout<<"{\"holes\":[0,"<<O[bi]<<","<<O[ti]<<","<<O[vi]<<"],\"S\":[";
          bool sep=false;
          for(int i=0;i<16;i++)if(d.s>>i&1){if(sep)cout<<",";cout<<E[i];sep=true;}
          cout<<"],\"slack\":"<<slack<<",\"forced_short_edges\":[";sep=false;
          for(int i=1;i<16;i++)if(d.leaves[i]&~blocked){
            int j=__builtin_ctz(d.leaves[i]&~blocked);
            if(sep)cout<<",";cout<<"["<<E[i]<<","<<O[j]<<"]";sep=true;
          }
          cout<<"]}";
        }
      }
    }
  }
  if(!printed)cout<<"null";
  cout<<",\"hole_configurations\":"<<configurations<<",\"hall_subsets_tested\":"<<tested
      <<",\"negative_bounds\":"<<failures<<",\"minimum_slack_by_subset_size\":[";
  for(int i=0;i<=16;i++){if(i)cout<<",";cout<<mins[i];}
  cout<<"]}\n";
}
