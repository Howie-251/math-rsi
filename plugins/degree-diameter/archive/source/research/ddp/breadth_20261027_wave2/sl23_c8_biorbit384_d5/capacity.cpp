#include <array>
#include <bitset>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
struct Node{int parent,letter,target,form;};
int main(){
 ifstream f("capacity_input.txt");array<array<int,24>,24>m;for(auto&r:m)for(int&x:r)f>>x;array<int,24>iv;for(int&x:iv)f>>x;
 array<vector<Node>,2>paths;for(auto&v:paths){int n;f>>n;v.resize(n);for(auto&x:v)f>>x.parent>>x.letter>>x.target>>x.form;assert(n==485);}
 int checkA,checkB,checkH;f>>checkA>>checkB>>checkH;array<int,96>expected;for(int&x:expected)f>>x;assert(f);
 clock_t t=clock();vector<array<int,3>>pass;array<int,486>hist{};vector<int>mins;int best=0,bestA=0,bestB=0,bestH=0;array<int,96>bestcounts{};int done=0;
 for(int a=0;a<24;a++)for(int b=0;b<24;b++)for(int h=0;h<24;h++){
  array<int,7>letters{a,iv[a],b,iv[b],h,iv[h],0};array<int,96>counts{};int minimum=486;
  for(int root=0;root<2;root++){
   array<bitset<512>,48>slots;vector<int>end(paths[root].size());
   for(size_t j=0;j<paths[root].size();j++){auto x=paths[root][j];end[j]=x.parent<0?0:m[end[x.parent]][letters[x.letter]];slots[x.target*24+end[j]].set(x.form);}
   for(int k=0;k<48;k++){counts[root*48+k]=slots[k].count();minimum=min(minimum,counts[root*48+k]);}
  }
  if(a==checkA&&b==checkB&&h==checkH)assert(counts==expected);
  ++done;++hist[minimum];mins.push_back(minimum);if(minimum>best){best=minimum;bestA=a;bestB=b;bestH=h;bestcounts=counts;}
  if(minimum>=8)pass.push_back({a,b,h});
 }
 double cpu=double(clock()-t)/CLOCKS_PER_SEC;ofstream o("capacity.raw.json");
 o<<"{\"status\":\"COMPLETE_ALL_13824_SL_TRIPLES\",\"triples_completed\":"<<done<<",\"surviving_quotient_triples\":"<<pass.size()<<",\"minimum_fiber_capacity_maximum\":"<<best<<",\"best_quotient_triple\":["<<bestA<<","<<bestB<<","<<bestH<<"],\"minimum_capacity_histogram\":{";bool first=true;for(int i=0;i<486;i++)if(hist[i]){o<<(first?"":",")<<"\""<<i<<"\":"<<hist[i];first=false;}o<<"},\"all_minimum_capacities_in_lex_A_B_H_order\":[";for(size_t i=0;i<mins.size();i++)o<<(i?",":"")<<mins[i];o<<"],\"best_counts_root_target_SL\":[";for(int i=0;i<96;i++)o<<(i?",":"")<<bestcounts[i];o<<"],\"survivors\":[";for(size_t i=0;i<pass.size();i++)o<<(i?",":"")<<"["<<pass[i][0]<<","<<pass[i][1]<<","<<pass[i][2]<<"]";o<<"],\"production_CPU_seconds\":"<<cpu<<",\"calibration_triple\":["<<checkA<<","<<checkB<<","<<checkH<<"],\"calibration_cells\":96,\"graphs_expanded\":0,\"BFS_roots\":0}\n";
 cout<<"capacity complete "<<done<<" survivors "<<pass.size()<<" maxmin "<<best<<" cpu "<<cpu<<endl;
}
