#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
constexpr uint32_t FULL=(1U<<17)-1;
struct RNG{uint64_t x;uint64_t next(){x^=x<<13;x^=x>>7;x^=x<<17;return x;}int pick(int n){return next()%n;}double unit(){return (next()>>11)*0x1.0p-53;}};
struct Family{uint32_t mask;int n;array<int,3> index{},coeff{};};
struct Slot{int root,target;vector<Family> families;};
using Params=array<int,26>;
int score(const vector<Slot>&slots,const Params&p,array<int,10>*byroot=nullptr){
 int total=0;if(byroot)byroot->fill(0);
 for(const Slot&s:slots){uint32_t covered=0;
  for(const Family&f:s.families){int shift=0;for(int i=0;i<f.n;i++)shift+=f.coeff[i]*p[f.index[i]];shift%=17;if(shift<0)shift+=17;
   covered|=((f.mask<<shift)|(f.mask>>(17-shift)))&FULL;
  }
  int misses=17-__builtin_popcount(covered);total+=misses;if(byroot)(*byroot)[s.root]+=misses;
 }
 assert(total%2==0);return total;
}
int main(int argc,char**argv){
 string dir=argc>1?argv[1]:".";ifstream input(dir+"/families.txt");int np,ns;input>>np>>ns;assert(np==26&&ns==420);
 vector<Slot>slots(ns);for(Slot&s:slots){int nf;input>>s.root>>s.target>>nf;assert(nf==7);s.families.resize(nf);for(Family&f:s.families){input>>f.mask>>f.n;assert(f.n<=3);for(int i=0;i<f.n;i++)input>>f.index[i]>>f.coeff[i];}}
 assert(input);clock_t start=clock();Params best{};int globalbest=100000,total_proposals=0,completed=0;bool hit=false,limit=false;
 const uint64_t seeds[]={202610270700ULL,202610270701ULL,202610270702ULL,202610270703ULL};
 ofstream logs(dir+"/search_log.jsonl");
 for(int run=0;run<4&&!hit&&!limit;run++){
  RNG rng{seeds[run]};Params p{};if(run)for(int&v:p)v=rng.pick(17);
  int current=score(slots,p),initial=current,localbest=current,accepted=0,proposals=0;assert(run!=0||current==2020);
  if(current<globalbest){globalbest=current;best=p;}
  for(int q=0;q<25000;q++){
   if((q&255)==0&&double(clock()-start)/CLOCKS_PER_SEC>=85){limit=true;break;}
   int i=rng.pick(26),old=p[i],value=rng.pick(16);if(value>=old)value++;p[i]=value;
   int next=score(slots,p);double temp=12*pow(.05/12,double(q)/24999);
   if(next<=current||rng.unit()<exp(double(current-next)/temp)){current=next;accepted++;}else p[i]=old;
   proposals++;total_proposals++;
   if(current<localbest)localbest=current;
   if(current<globalbest){globalbest=current;best=p;cout<<"run "<<run<<" proposal "<<q+1<<" best "<<globalbest<<endl;}
   if(!globalbest){hit=true;break;}
  }
  if(proposals==25000)completed++;
  logs<<"{\"start\":"<<run<<",\"seed\":"<<seeds[run]<<",\"initial_missing\":"<<initial<<",\"best_missing\":"<<localbest<<",\"final_missing\":"<<current<<",\"proposals\":"<<proposals<<",\"accepted\":"<<accepted<<"}"<<endl;
  cout<<"DONE run "<<run<<" proposals "<<proposals<<" best "<<localbest<<" totalCPU "<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
 }
 array<int,10>rootmisses{};assert(score(slots,best,&rootmisses)==globalbest);
 ofstream params(dir+"/best_parameters.json");params<<"{\"parameters\":[";for(int i=0;i<26;i++)params<<(i?",":"")<<best[i];params<<"],\"representative_missing_total\":"<<globalbest<<",\"root_missing\":[";for(int i=0;i<10;i++)params<<(i?",":"")<<rootmisses[i];params<<"]}\n";
 ofstream result(dir+"/RESULT.json");result<<"{\"status\":\""<<(hit?"PRODUCTION_TEN_ORBIT_D3_HIT":limit?"CPU_LIMIT_INCOMPLETE":"COMPLETE_FIXED_FOUR_START_BATCH_NO_D3")<<"\",\"representative_count\":10,\"completed_starts\":"<<completed<<",\"proposals\":"<<total_proposals<<",\"best_representative_misses\":"<<globalbest<<",\"implied_ordered_pair_misses\":"<<85LL*globalbest<<",\"implied_unordered_pair_misses\":"<<85LL*globalbest/2<<",\"CPU_seconds\":"<<setprecision(10)<<double(clock()-start)/CLOCKS_PER_SEC<<",\"all850_final_BFS_performed\":false,\"additional_batches\":0}\n";
 cout<<"BATCH DONE best "<<globalbest<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}
