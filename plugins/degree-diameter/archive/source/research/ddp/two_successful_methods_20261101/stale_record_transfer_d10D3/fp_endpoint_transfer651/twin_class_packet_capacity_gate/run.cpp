#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <ctime>
using namespace std;
using Mask=array<unsigned long long,9>;
struct F{int label,c;Mask m;};struct P{int label,c;Mask m;};
struct Pair{int i,j;Mask m;};struct Gain{int val,c,step;};
int cnt(const Mask&a,const Mask&b){int n=0;for(int k=0;k<9;++k)n+=__builtin_popcountll(a[k]&b[k]);return n;}
int main(){
 double start=double(clock())/CLOCKS_PER_SEC;
 ifstream in("PACKETS_INPUT.txt");int nf,np,nc;in>>nf>>np>>nc;if(nf!=520||np!=130||nc!=65)return 2;
 vector<F> f(nf);vector<P> p(np);vector<vector<int>> groups(nc);vector<vector<Pair>> pairs(nc);
 for(int i=0;i<nf;++i){in>>f[i].label>>f[i].c;for(auto&x:f[i].m)in>>x;groups[f[i].c].push_back(i);}
 for(auto&x:p){in>>x.label>>x.c;for(auto&v:x.m)in>>v;}if(!in)return 3;
 for(int c=0;c<nc;++c){if(groups[c].size()!=8)return 4;for(int a=0;a<8;++a)for(int b=a+1;b<8;++b){Pair v{};v.i=groups[c][a];v.j=groups[c][b];for(int k=0;k<9;++k)v.m[k]=f[v.i].m[k]|f[v.j].m[k];pairs[c].push_back(v);}}
 long checked=0,pass=0,fail=0;bool complete=true,exact=false;int minslack=99999;ofstream rows("ALL_STARPAIR_CAPACITY.tsv");rows<<"starP0\tstarP1\tresidual\tupper\tslack\targmax_union\tactual_missing\n";
 for(int i=0;i<np&&!exact&&complete;++i)for(int j=i+1;j<np;++j){
  if((checked&63)==0&&double(clock())/CLOCKS_PER_SEC-start>8){complete=false;break;}
  Mask u{};for(int k=0;k<9;++k)u[k]=~(p[i].m[k]|p[j].m[k]);u[8]&=255ULL;int needed=cnt(u,u);
  int h[65]={},cost[65]={},m1[65],m2[65],one[65],two[65];++h[p[i].c];++h[p[j].c];vector<Gain> gains;int upper=0;
  for(int c=0;c<nc;++c){m1[c]=-1;m2[c]=-1;
   for(int x:groups[c]){int v=cnt(f[x].m,u);if(v>m1[c]){m1[c]=v;one[c]=x;}}
   for(int z=0;z<int(pairs[c].size());++z){int v=cnt(pairs[c][z].m,u);if(v>m2[c]){m2[c]=v;two[c]=z;}}
   if(m2[c]<m1[c]||m2[c]>2*m1[c])return 5;
   cost[c]=h[c];if(h[c]==1)upper+=m1[c];if(h[c]==2)upper+=m2[c];
   if(h[c]==0)gains.push_back({m1[c],c,1});if(h[c]<=1)gains.push_back({m2[c]-m1[c],c,2});
  }
  sort(gains.begin(),gains.end(),[](const Gain&a,const Gain&b){if(a.val!=b.val)return a.val>b.val;if(a.c!=b.c)return a.c<b.c;return a.step<b.step;});
  for(int z=0;z<6;++z){upper+=gains[z].val;++cost[gains[z].c];}
  vector<int> chosen;Mask actual{};
  for(int c=0;c<nc;++c){if(cost[c]<h[c]||cost[c]>2)return 6;if(cost[c]==1)chosen.push_back(one[c]);if(cost[c]==2){chosen.push_back(pairs[c][two[c]].i);chosen.push_back(pairs[c][two[c]].j);}}
  if(chosen.size()!=8)return 7;for(int x:chosen)for(int k=0;k<9;++k)actual[k]|=f[x].m[k];int covered=cnt(actual,u);
  ++checked;bool ok=upper>=needed;if(ok)++pass;else++fail;minslack=min(minslack,upper-needed);
  rows<<p[i].label<<'\t'<<p[j].label<<'\t'<<needed<<'\t'<<upper<<'\t'<<upper-needed<<'\t'<<covered<<'\t'<<needed-covered<<'\n';
  if((ok&&pass==1)||covered==needed){ofstream w(covered==needed?"ACTUAL_F_COVER_WITNESS.json":"FIRST_CAPACITY_PASS_WITNESS.json");
   w<<"{\"starP\":["<<p[i].label<<','<<p[j].label<<"],\"residual\":"<<needed<<",\"upper\":"<<upper<<",\"argmax_union\":"<<covered<<",\"actual_F_covered\":"<<520-needed+covered<<",\"actual_F_missing\":"<<needed-covered<<",\"chosen_F\":[";
   for(int z=0;z<8;++z){if(z)w<<',';w<<f[chosen[z]].label;}w<<"],\"class_costs\":[";for(int c=0;c<65;++c){if(c)w<<',';w<<cost[c];}w<<"]}\n";
  }
  if(covered==needed){exact=true;break;}
 }
 ofstream r("NATIVE_RESULT.json");r<<"{\"status\":\""<<(exact?"ACTUAL_F_COVER_OBJECT_FOUND":!complete?"UNKNOWN_NATIVE_CAP":pass?"COMPLETE_CAPACITY_UPPER_WITH_SURVIVORS":"COMPLETE_NO_ALL_STARP_PAIRS_BY_UPPER")<<"\",\"checked_pairs\":"<<checked<<",\"domain_size\":8385,\"upper_pass\":"<<pass<<",\"upper_fail\":"<<fail<<",\"minimum_upper_minus_residual\":"<<minslack<<",\"actual_F_cover_found\":"<<(exact?"true":"false")<<",\"complete\":"<<(complete&&!exact?"true":"false")<<",\"CPU\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";
 cout<<"pairs="<<checked<<" pass="<<pass<<" fail="<<fail<<" exactF="<<exact<<" CPU="<<double(clock())/CLOCKS_PER_SEC-start<<endl;
}
