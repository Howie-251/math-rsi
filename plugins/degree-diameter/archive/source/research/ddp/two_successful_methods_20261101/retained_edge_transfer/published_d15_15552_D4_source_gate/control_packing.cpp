#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
struct Bits {
  array<uint64_t,3> w{};
  bool any()const{return w[0]||w[1]||w[2];}
  int first()const{for(int i=0;i<3;i++)if(w[i])return 64*i+__builtin_ctzll(w[i]);return -1;}
  void add(int x){w[x/64]|=1ull<<(x%64);}
  void erase(int x){w[x/64]&=~(1ull<<(x%64));}
  int size()const{return __builtin_popcountll(w[0])+__builtin_popcountll(w[1])+__builtin_popcountll(w[2]);}
  Bits operator&(const Bits&b)const{Bits c;for(int i=0;i<3;i++)c.w[i]=w[i]&b.w[i];return c;}
  void subtract(const Bits&b){for(int i=0;i<3;i++)w[i]&=~b.w[i];}
};
array<Bits,192> adjacent;
vector<int> current,best;
uint64_t nodes=0,colorings=0,bound_prunes=0;
bool found=false,timed_out=false;
clock_t started;double budget;
double cpu(){return double(clock()-started)/CLOCKS_PER_SEC;}
void color_sort(Bits remaining,vector<int>&order,vector<int>&colors){
  ++colorings;int color=0;
  while(remaining.any()){
    ++color;Bits available=remaining;
    while(available.any()){
      int v=available.first();order.push_back(v);colors.push_back(color);
      remaining.erase(v);available.erase(v);available.subtract(adjacent[v]);
    }
  }
}
void expand(Bits possible){
  ++nodes;
  if((nodes&1023)==0 && cpu()>=budget){timed_out=true;return;}
  vector<int>order,colors;order.reserve(possible.size());colors.reserve(possible.size());
  color_sort(possible,order,colors);
  for(int i=int(order.size())-1;i>=0;--i){
    if(current.size()+colors[i]<31){++bound_prunes;return;}
    int v=order[i];current.push_back(v);
    if(current.size()>best.size())best=current;
    if(current.size()==31){found=true;return;}
    Bits next=possible&adjacent[v];
    if(next.any())expand(next);
    current.pop_back();
    if(found||timed_out)return;
    possible.erase(v);
  }
}
int main(int argc,char**argv){
  if(argc!=3)return 2;started=clock();budget=stod(argv[2]);
  ifstream in(argv[1]);int n,k;in>>n>>k;if(n!=192||k!=5)return 3;
  array<array<int,5>,192>targets;
  for(int i=0;i<n;i++){int id;in>>id;if(id!=i)return 4;for(int&x:targets[i])in>>x;}
  array<Bits,192>original;
  for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j){
    bool disjoint=true;for(int x:targets[i])for(int y:targets[j])if(x==y)disjoint=false;
    if(disjoint)original[i].add(j);
  }
  // One fixed degree ordering; all later branching is deterministic.
  vector<int>label(n);iota(label.begin(),label.end(),0);
  stable_sort(label.begin(),label.end(),[&](int a,int b){return original[a].size()>original[b].size();});
  for(int i=0;i<n;i++)for(int j=0;j<n;j++)if((original[label[i]].w[label[j]/64]>>(label[j]%64))&1)adjacent[i].add(j);
  Bits all;for(int i=0;i<n;i++)all.add(i);expand(all);
  vector<int>selected;for(int i:best)selected.push_back(label[i]);sort(selected.begin(),selected.end());
  cout<<setprecision(12)<<"{\"status\":\""<<(found?"FOUND31":timed_out?"UNKNOWN_CPU_LIMIT":"EXACT_NO31")
      <<"\",\"found31\":"<<(found?"true":"false")<<",\"exhausted\":"<<(!found&&!timed_out?"true":"false")
      <<",\"nodes\":"<<nodes<<",\"proper_greedy_colorings\":"<<colorings<<",\"color_bound_prunes\":"<<bound_prunes
      <<",\"CPU_seconds\":"<<cpu()<<",\"CPU_limit_seconds\":"<<budget<<",\"incumbent_size\":"<<selected.size()<<",\"selected_controllers\":[";
  for(size_t i=0;i<selected.size();i++){if(i)cout<<',';cout<<selected[i];}
  cout<<"],\"selected_target_sets\":[";
  for(size_t i=0;i<selected.size();i++){if(i)cout<<',';cout<<'[';for(int j=0;j<5;j++){if(j)cout<<',';cout<<targets[selected[i]][j];}cout<<']';}
  cout<<"]}\n";
}
