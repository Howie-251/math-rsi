// Diagnostic Q4 two opposite holes both avoided; exact alternating 14-cycles.
#include <array>
#include <vector>
#include <iostream>
#include <cstdint>
using namespace std;
array<int,16> mate{};
int hole,start;
uint64_t tested,bad,half_bad,nonhalf_bad,nodes;
vector<array<int,16>> examples;
int pc(unsigned x){return __builtin_popcount(x);}
bool hashalf(){
  for(int i=0;i<4;i++)for(int p=0;p<2;p++){
    bool yes=true;
    for(int x=0;x<16;x++)if(!(x>>i&1)&&pc(x)%2==p)
      if(mate[x]!=(x^(1<<i)))yes=false;
    if(yes)return true;
  }
  return false;
}
bool dfs(int endpoint,unsigned unused){
  nodes++;
  if(!unused)return pc(endpoint^start)==1;
  for(int i=0;i<4;i++){
    int x=endpoint^(1<<i);
    if(!(unused>>x&1))continue;
    int y=mate[x];
    if(dfs(y,unused&~(1u<<x)&~(1u<<y)))return true;
  }
  return false;
}
void generate(unsigned free){
  if(!free){
    tested++;
    unsigned covered=65535u&~1u&~(1u<<hole);
    start=__builtin_ctz(covered);
    bool ok=dfs(mate[start],covered&~(1u<<start)&~(1u<<mate[start]));
    if(!ok){
      bad++;
      if(hashalf())half_bad++;
      else{nonhalf_bad++;if(examples.size()<20)examples.push_back(mate);}
    }
    return;
  }
  int x=__builtin_ctz(free);unsigned rest=free&~(1u<<x);
  for(unsigned choices=rest;choices;choices&=choices-1){
    int y=__builtin_ctz(choices);mate[x]=y;mate[y]=x;
    generate(rest&~(1u<<y));mate[x]=mate[y]=-1;
  }
}
int main(){
  cout<<"{\"scope\":\"diagnostic exact Q4 14-cycle with two opposite holes avoided\",\"orbits\":[";bool comma=false;
  for(int s:{1,7}){
    mate.fill(-1);hole=s;tested=bad=half_bad=nonhalf_bad=nodes=0;examples.clear();
    generate(65535u&~1u&~(1u<<hole));
    if(comma)cout<<",";comma=true;
    cout<<"{\"other_hole\":"<<s<<",\"tested\":"<<tested<<",\"bad\":"<<bad<<",\"half_layer_bad\":"<<half_bad<<",\"non_half_layer_bad\":"<<nonhalf_bad<<",\"nodes\":"<<nodes<<",\"nonhalf_examples\":[";bool comma2=false;
    for(auto f:examples){if(comma2)cout<<",";comma2=true;cout<<"[";bool comma3=false;
      for(int x=0;x<16;x++)if(f[x]>x){if(comma3)cout<<",";comma3=true;cout<<"["<<x<<","<<f[x]<<"]";}
      cout<<"]";
    }
    cout<<"]}";
  }
  cout<<"],\"negative_results_independently_certified\":false,\"full_p6_proved\":false}\n";
}
