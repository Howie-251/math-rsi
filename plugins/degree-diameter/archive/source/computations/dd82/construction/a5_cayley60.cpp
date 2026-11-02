// Complete bounded construction search in one explicitly declared family.
// Does not exclude arbitrary order-60 graphs or other groups.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
int main(int argc, char **argv) {
  vector<array<int,5>> g; array<int,5> p={0,1,2,3,4};
  do {int inv=0;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++) inv+=p[i]>p[j];
    if(inv%2==0) g.push_back(p);
  } while(next_permutation(p.begin(),p.end()));
  assert(g.size()==60 && g[0]==(array<int,5>{0,1,2,3,4}));
  map<array<int,5>,int> ids;for(int i=0;i<60;i++)ids[g[i]]=i;
  int mul[60][60], inv[60];
  for(int a=0;a<60;a++)for(int b=0;b<60;b++){
    array<int,5> c;for(int i=0;i<5;i++)c[i]=g[a][g[b][i]];
    mul[a][b]=ids.at(c);if(mul[a][b]==0)inv[a]=b;
  }
  vector<vector<int>> units;
  for(int a=1;a<60;a++)if(inv[a]>=a){
    if(inv[a]==a)units.push_back({a});else units.push_back({a,inv[a]});
  }
  int singles=0;for(auto &u:units)singles+=u.size()==1;
  assert(singles==15 && units.size()==37);
  vector<int> s,bestS; uint64_t visited=0,hist[61]={};int best=0;
  function<void(int)> dfs=[&](int start){
    if(s.size()==8){
      uint64_t ball=1;for(int a:s){ball|=1ULL<<a;for(int b:s)ball|=1ULL<<mul[a][b];}
      int count=__builtin_popcountll(ball);visited++;hist[count]++;
      if(count>best){best=count;bestS=s;}return;
    }
    for(int j=start;j<(int)units.size();j++)if(s.size()+units[j].size()<=8){
      s.insert(s.end(),units[j].begin(),units[j].end());dfs(j+1);
      s.resize(s.size()-units[j].size());
    }
  };dfs(0);
  cout<<"{\n  \"group\": \"A5 as even permutations of five letters\",\n"
      <<"  \"order\": 60,\n  \"degree\": 8,\n  \"inverse_singletons\": 15,\n"
      <<"  \"inverse_pairs\": 22,\n  \"generator_sets_checked\": "<<visited<<",\n"
      <<"  \"maximum_radius_two_ball\": "<<best<<",\n  \"diameter_two_witness_found\": "<<(best==60?"true":"false")<<",\n"
      <<"  \"best_generators\": [";
  for(int i=0;i<8;i++)cout<<(i?", ":"")<<bestS[i];
  cout<<"],\n  \"ball_size_histogram\": {";bool first=true;
  for(int i=0;i<=60;i++)if(hist[i]){cout<<(first?"":", ")<<"\""<<i<<"\": "<<hist[i];first=false;}
  cout<<"},\n  \"scope\": \"only inverse-closed degree-eight Cayley graphs of this A5; not arbitrary order60\"\n}\n";
  if(argc>1){ofstream out(argv[1]);out<<"60 240\n";
    for(int a=0;a<60;a++)for(int b:bestS)if(a<mul[a][b])out<<a<<" "<<mul[a][b]<<"\n";
  }
}
