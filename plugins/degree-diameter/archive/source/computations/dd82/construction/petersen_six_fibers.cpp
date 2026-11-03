// Restricted C5-symmetric six-Petersen-fiber search: three S10 parameters.
// No free edge moves; all candidates have 60 vertices, degree 8, 240 edges.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
using Perm=std::array<int,10>;
struct State { Perm A,B,C; };
std::array<std::array<int,3>,10> P;
std::array<int,10> PM;
Perm R;
Perm inverse(const Perm& a){Perm b;for(int u=0;u<10;u++)b[a[u]]=u;return b;}
int score(const State& s){
  const auto ai=inverse(s.A), bi=inverse(s.B), ci=inverse(s.C), ri=inverse(R);
  int missing=0;
  for(int u=0;u<10;u++){
    // Fiber infinity -> 0: 1 direct + 3 + 3 internal + 4 via other fibers.
    int v=s.A[u], mask=(1<<v)|PM[v];
    for(int x:P[u])mask|=1<<s.A[x];
    mask|=1<<s.B[s.A[R[u]]];
    mask|=1<<bi[s.A[ri[u]]];
    mask|=1<<s.C[s.A[R[R[u]]]];
    mask|=1<<ci[s.A[ri[ri[u]]]];
    missing+=10-__builtin_popcount((unsigned)mask);
    // Fiber 0 -> 1.
    v=s.B[u]; mask=(1<<v)|PM[v];
    for(int x:P[u])mask|=1<<s.B[x];
    mask|=1<<s.A[ri[ai[u]]];
    mask|=1<<bi[s.C[u]];
    mask|=1<<ci[ci[u]];
    mask|=1<<s.C[bi[u]];
    missing+=10-__builtin_popcount((unsigned)mask);
    // Fiber 0 -> 2.
    v=s.C[u]; mask=(1<<v)|PM[v];
    for(int x:P[u])mask|=1<<s.C[x];
    mask|=1<<s.A[ri[ri[ai[u]]]];
    mask|=1<<s.B[s.B[u]];
    mask|=1<<bi[ci[u]];
    mask|=1<<ci[bi[u]];
    missing+=10-__builtin_popcount((unsigned)mask);
  }
  return missing; // full unordered uncovered-pair count = 5 * missing.
}
void output_perm(std::ostream& o,const Perm& p){o<<'[';for(int i=0;i<10;i++){if(i)o<<',';o<<p[i];}o<<']';}
void save(const std::string& prefix, const State& s,int energy,long long it,double cpu){
  std::ofstream o(prefix+".params.json");
  o<<"{\"A\":";output_perm(o,s.A);o<<",\"B\":";output_perm(o,s.B);o<<",\"C\":";output_perm(o,s.C);
  o<<",\"orbit_missing\":"<<energy<<",\"expected_uncovered_pairs\":"<<5*energy<<",\"iteration\":"<<it<<",\"cpu_seconds\":"<<cpu<<"}\n";
}
int main(int argc,char**argv){
  const double budget=argc>1?std::stod(argv[1]):80;
  const std::string prefix=argc>2?argv[2]:"petersen_six_fibers";
  // Petersen outer cycle, inner star, spokes; R rotates both 5-cycles.
  for(int i=0;i<5;i++){P[i]={(i+1)%5,(i+4)%5,i+5};P[i+5]={5+(i+2)%5,5+(i+3)%5,i};R[i]=(i+1)%5;R[i+5]=5+(i+1)%5;}
  for(int u=0;u<10;u++)for(int v:P[u])PM[u]|=1<<v;
  std::mt19937 rng(20261011);
  State cur;for(auto*p:{&cur.A,&cur.B,&cur.C}){std::iota(p->begin(),p->end(),0);std::shuffle(p->begin(),p->end(),rng);}
  const clock_t t0=clock();
  int e=score(cur),best=e;
  State bests=cur;long long it=0,accepted=0;
  save(prefix+".initial",cur,e,0,0);
  save(prefix+".best",cur,e,0,0);
  std::cout<<"initial orbit_missing "<<e<<" actual_missing "<<5*e<<std::endl;
  // One finite run with a predeclared sawtooth temperature schedule (40k proposals/cycle).
  // Restarts after a sweep begin from best with 4 restricted transpositions.
  constexpr long long cycle=40000;
  double cpu=0;
  while(cpu<budget && best>0){
    if(it && it%cycle==0){cur=bests;for(int k=0;k<4;k++){Perm *p=(rng()%3==0?&cur.A:(rng()%2==0?&cur.B:&cur.C));int i=rng()%10,j=rng()%9;if(j>=i)j++;std::swap((*p)[i],(*p)[j]);}e=score(cur);}
    State next=cur;Perm *p=(rng()%3==0?&next.A:(rng()%2==0?&next.B:&next.C));int i=rng()%10,j=rng()%9;if(j>=i)j++;std::swap((*p)[i],(*p)[j]);
    int ne=score(next);
    const double temp=1.6*std::pow(0.02/1.6,double(it%cycle)/cycle);
    if(ne<=e || std::generate_canonical<double,32>(rng)<std::exp((e-ne)/temp)){cur=next;e=ne;accepted++;}
    it++;
    if(e<best){best=e;bests=cur;cpu=double(clock()-t0)/CLOCKS_PER_SEC;save(prefix+".best",bests,best,it,cpu);std::cout<<"best orbit_missing "<<best<<" actual_missing "<<5*best<<" iteration "<<it<<" cpu "<<cpu<<std::endl;}
    if(it%2048==0)cpu=double(clock()-t0)/CLOCKS_PER_SEC;
  }
  cpu=double(clock()-t0)/CLOCKS_PER_SEC;
  save(prefix+".best",bests,best,it,cpu);
  std::ofstream o(prefix+".search.json");o<<"{\"seed\":20261011,\"search_cpu_budget_seconds\":"<<budget<<",\"cpu_seconds\":"<<cpu<<",\"threads\":1,\"proposals\":"<<it<<",\"accepted\":"<<accepted<<",\"best_orbit_missing\":"<<best<<",\"best_uncovered_pairs\":"<<5*best<<",\"complete_enumeration\":false,\"scope\":\"C5-symmetric six-Petersen fibers, three permutations; one bounded restricted search\"}\n";
  std::cout<<"finished cpu "<<cpu<<" proposals "<<it<<" best "<<best<<std::endl;
}
