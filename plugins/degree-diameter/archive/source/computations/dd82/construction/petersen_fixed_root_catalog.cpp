// Complete local matching catalog with the root route already fixed to identity.
#include <array>
#include <algorithm>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
using Perm=std::array<int,10>;
int main(){
 const Perm A={5,9,8,7,6,3,2,1,0,4};Perm Ai;for(int i=0;i<10;i++)Ai[A[i]]=i;
 std::array<unsigned,10>P{},Q{},T{};std::array<std::array<int,3>,10>qn;
 for(int i=0;i<5;i++){P[i]=(1<<((i+1)%5))|(1<<((i+4)%5))|(1<<(i+5));P[i+5]=(1<<(5+(i+2)%5))|(1<<(5+(i+3)%5))|(1<<i);}
 for(int u=0;u<10;u++){int c=0;for(int v=0;v<10;v++)if(P[A[u]]>>A[v]&1){Q[u]|=1<<v;qn[u][c++]=v;}T[u]=1023^((1<<u)|P[u]|Q[u]);}
 const auto began=clock();Perm M,Mi;std::iota(M.begin(),M.end(),0);
 std::ofstream table("computations/dd82/construction/petersen_fixed_root_catalog.perms.txt");
 long long total=0,ok=0,forward=0;std::array<long long,11>histT{},histSame{};std::array<long long,6>histOverlap{};
 Perm first{};bool saved=false;
 do{
  total++;for(int u=0;u<10;u++)Mi[M[u]]=u;
  int overlaprows=0;bool pass=true;
  for(int direction=0;direction<2 && pass;direction++){
   const Perm& X=direction?Mi:M;
   for(int u=0;u<10;u++){
    unsigned image=0;for(int v:qn[u])image|=1<<X[v];
    const unsigned known=(1<<u)|(1<<X[u])|Q[X[u]]|image;
    if(__builtin_popcount(known)<7){pass=false;break;}
    if(direction==0)overlaprows+=__builtin_popcount(Q[X[u]]&image);
   }
   if(direction==0&&pass)forward++;
  }
  if(!pass)continue;
  ok++;for(int u=0;u<10;u++){if(u)table<<' ';table<<M[u];}table<<'\n';int tc=0,sc=0;for(int u=0;u<10;u++){tc+=(T[u]>>M[u])&1;sc+=(u/5==M[u]/5);}
  histT[tc]++;histSame[sc]++;histOverlap[overlaprows/2]++;
  if(!saved){first=M;saved=true;}
 }while(std::next_permutation(M.begin(),M.end()));
 std::ofstream o("computations/dd82/construction/petersen_fixed_root_catalog.json");
 o<<"{\"permutations_checked\":"<<total<<",\"forward_condition_count\":"<<forward<<",\"both_directions_admissible\":"<<ok<<",\"cpu_seconds\":"<<double(clock()-began)/CLOCKS_PER_SEC<<",\"T_entries_histogram\":{";
 bool comma=false;for(int i=0;i<=10;i++)if(histT[i]){if(comma)o<<',';comma=true;o<<'\"'<<i<<"\":"<<histT[i];}o<<"},\"same_layer_entries_histogram\":{";
 comma=false;for(int i=0;i<=10;i++)if(histSame[i]){if(comma)o<<',';comma=true;o<<'\"'<<i<<"\":"<<histSame[i];}o<<"},\"internal_overlap_edges_histogram\":{";
 comma=false;for(int i=0;i<=5;i++)if(histOverlap[i]){if(comma)o<<',';comma=true;o<<'\"'<<i<<"\":"<<histOverlap[i];}o<<"},\"first_admissible\":[";
 for(int i=0;i<10;i++){if(i)o<<',';o<<first[i];}o<<"]}\n";
 std::cout<<"checked "<<total<<" admissible "<<ok<<" CPU "<<double(clock()-began)/CLOCKS_PER_SEC<<'\n';
}
