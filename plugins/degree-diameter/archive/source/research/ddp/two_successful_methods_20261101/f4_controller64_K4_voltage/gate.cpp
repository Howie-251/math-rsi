#include <array>
#include <bit>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using Row=array<int,5>;
using Controller=array<Row,64>;
using Perm=array<int,4>;
struct Stats {
  long assignments=0,simple=0,signed_pass=0,root0pass=0,all4pass=0;
  array<long,65> hist{};
  array<long,4> firstfail{};
  int maxroot0=0;
};
int mod16(int x){return x&15;}
Controller build(const Perm&P,const array<int,4>&a){
  Perm ip{};for(int i=0;i<4;++i)ip[P[i]]=i;
  Controller C{};
  for(int t=0;t<16;++t)for(int i=0;i<4;++i){
    int v=4*t+i;
    C[v]={4*t+(i^1),4*t+(i^2),4*t+(i^3),4*mod16(t+a[i])+P[i],4*mod16(t-a[ip[i]])+ip[i]};
  }
  return C;
}
uint64_t radius3(const array<uint64_t,64>&N,int root){
  uint64_t r=uint64_t(1)<<root;
  for(int d=0;d<3;++d){
    uint64_t add=r,scan=r;
    while(scan){int v=countr_zero(scan);scan&=scan-1;add|=N[v];}
    r=add;
  }
  return r;
}
void arr4(ofstream&f,const array<int,4>&a){f<<'[';for(int i=0;i<4;++i){if(i)f<<',';f<<a[i];}f<<']';}
void save_candidate(const Controller&C,const Perm&P,const array<int,4>&a,int type){
  ofstream f("CANDIDATE_CONTROLLER.json");
  f<<"{\"permutation_type\":"<<type<<",\"P\":";arr4(f,P);f<<",\"voltages\":";arr4(f,a);
  f<<",\"label\":\"4*t+i\",\"inverse_ports\":[0,1,2,4,3],\"controller\":[";
  for(int v=0;v<64;++v){if(v)f<<',';f<<'[';for(int p=0;p<5;++p){if(p)f<<',';f<<C[v][p];}f<<']';}
  f<<"],\"translation_root_coverage\":[";
  array<uint64_t,64>N{};for(int v=0;v<64;++v)for(int w:C[v])N[v]|=uint64_t(1)<<w;
  for(int i=0;i<4;++i){if(i)f<<',';uint64_t r=radius3(N,i);f<<"{\"root\":"<<i<<",\"covered\":"<<popcount(r)<<",\"missing\":[";bool comma=false;for(int v=0;v<64;++v)if(!(r>>v&1)){if(comma)f<<',';f<<v;comma=true;}f<<"]}";}
  f<<"],\"shortword_counts_by_translation_root\":[";
  array<int,5> inv{0,1,2,4,3};bool comma=false;
  for(int root=0;root<4;++root){
    array<array<int,4>,64> count{};array<int,64> nb3{};
    count[root][0]++;
    for(int p=0;p<5;++p){int b=C[root][p];count[b][1]++;
      for(int q=0;q<5;++q){int c=C[b][q];count[c][2]++;
        for(int r=0;r<5;++r){int d=C[c][r];count[d][3]++;if(q!=inv[p]&&r!=inv[q])nb3[d]++;}
      }
    }
    for(int v=0;v<64;++v){if(comma)f<<',';comma=true;f<<"{\"root\":"<<root<<",\"target\":"<<v<<",\"walk_counts_length0_to3\":[";for(int k=0;k<4;++k){if(k)f<<',';f<<count[v][k];}f<<"],\"NB3\":"<<nb3[v]<<'}';}
  }
  f<<"]}\n";
}
int main(){
  const double start=double(clock())/CLOCKS_PER_SEC;
  const array<Perm,5> Ps{{{0,1,2,3},{1,0,2,3},{1,0,3,2},{1,2,0,3},{1,2,3,0}}};
  array<Stats,5> S{};
  bool saved=false;
  for(int type=0;type<5;++type){
    const auto&P=Ps[type];auto&s=S[type];
    for(int code=0;code<65536;++code){
      ++s.assignments;array<int,4>a{};for(int i=0;i<4;++i)a[i]=(code>>(4*i))&15;
      bool simple=true;
      for(int i=0;i<4;++i)if(a[i]==0||(P[P[i]]==i&&mod16(a[i]+a[P[i]])==0))simple=false;
      if(!simple)continue;++s.simple;
      unsigned signed_mask=0;bool ok=true;
      for(int i=0;i<4;++i){for(int x:{a[i],mod16(-a[i])}){if(x==0||(signed_mask>>x&1))ok=false;signed_mask|=1u<<x;}}
      if(!ok)continue;++s.signed_pass;
      Controller C=build(P,a);array<uint64_t,64>N{};
      for(int v=0;v<64;++v){
        for(int p=0;p<5;++p){int w=C[v][p];if(w==v)return 3;N[v]|=uint64_t(1)<<w;}
        if(popcount(N[v])!=5)return 4;
        const array<int,5>inv{0,1,2,4,3};for(int p=0;p<5;++p)if(C[C[v][p]][inv[p]]!=v)return 5;
      }
      uint64_t r=radius3(N,0);int n=popcount(r);++s.hist[n];s.maxroot0=max(s.maxroot0,n);
      if(n!=64){++s.firstfail[0];continue;}++s.root0pass;
      bool all=true;for(int root=1;root<4;++root)if(popcount(radius3(N,root))!=64){++s.firstfail[root];all=false;break;}
      if(!all)continue;++s.all4pass;
      if(!saved){save_candidate(C,P,a,type);saved=true;}
    }
  }
  double cpu=double(clock())/CLOCKS_PER_SEC-start;
  ofstream f("RESULT.json");long total=0,si=0,sg=0,r0=0,all=0;
  for(const auto&s:S){total+=s.assignments;si+=s.simple;sg+=s.signed_pass;r0+=s.root0pass;all+=s.all4pass;}
  f<<"{\"status\":\""<<(saved?"D3_CONTROLLER_FOUND_INTERFACE_ONLY":"COMPLETE_FAMILY_NO_D3_CONTROLLER")<<"\",\"parameter_assignments\":"<<total<<",\"simple_assignments\":"<<si<<",\"signed_voltage_gate_pass\":"<<sg<<",\"root0_D3_pass\":"<<r0<<",\"all4roots_D3_pass\":"<<all<<",\"controller_order\":64,\"controller_degree\":5,\"CPU_seconds\":"<<cpu<<",\"CPU_budget_seconds\":60,\"workers\":1,\"new_fiber_graphs\":0,\"solver_calls\":0,\"Lean_calls\":0,\"permutation_types\":[";
  for(int type=0;type<5;++type){if(type)f<<',';const auto&s=S[type];f<<"{\"P\":";arr4(f,Ps[type]);f<<",\"assignments\":"<<s.assignments<<",\"simple\":"<<s.simple<<",\"signed_pass\":"<<s.signed_pass<<",\"root0_pass\":"<<s.root0pass<<",\"all4_pass\":"<<s.all4pass<<",\"max_root0_R3\":"<<s.maxroot0<<",\"root0_coverage_histogram\":{";bool comma=false;for(int k=0;k<=64;++k)if(s.hist[k]){if(comma)f<<',';comma=true;f<<'\"'<<k<<"\":"<<s.hist[k];}f<<"},\"first_failure_root_counts\":[";for(int i=0;i<4;++i){if(i)f<<',';f<<s.firstfail[i];}f<<"]}";}
  f<<"],\"scope\":\"Only K4 blocks x Z16 with one external permutation F, five S4cycle types and all65536voltages each. Not other64controllers or generalF4graphs.\"}\n";
  cout<<"assignments="<<total<<" simple="<<si<<" signed="<<sg<<" root0pass="<<r0<<" all4pass="<<all<<" cpu="<<cpu<<"\n";
}
