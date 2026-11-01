#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
using Row=array<int,4>;using Mat=array<Row,4>;
vector<Row> rows,perms;Mat current;Row used{};long long terminals=0;
map<uint64_t,Mat> reps;vector<pair<uint64_t,uint64_t>> terminal_map;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int pc(unsigned x){return __builtin_popcount(x);}
uint64_t encode(const Mat&M){uint64_t key=0;for(auto r:M)for(int x:r)key=5*key+x;return key;}
Mat canon(const Mat&M){Mat best{};uint64_t key=UINT64_MAX;
 for(auto p:perms){Mat N;for(int i=0;i<4;i++)for(int j=0;j<4;j++)N[i][j]=M[i][p[j]];
 sort(N.begin(),N.end());auto z=encode(N);if(z<key){key=z;best=N;}}return best;}
void generate(int depth,int lower){
 if(depth==3){Row last;for(int j=0;j<4;j++)last[j]=4-used[j];
 if(last<rows[lower]||last[0]+last[1]+last[2]+last[3]!=4)return;
 current[3]=last;terminals++;auto N=canon(current);auto key=encode(N);
 reps.emplace(key,N);terminal_map.push_back({encode(current),key});return;}
 for(int j=lower;j<(int)rows.size();j++){bool fits=true;
 for(int k=0;k<4;k++)if(used[k]+rows[j][k]>4)fits=false;if(!fits)continue;
 current[depth]=rows[j];for(int k=0;k<4;k++)used[k]+=rows[j][k];generate(depth+1,j);
 for(int k=0;k<4;k++)used[k]-=rows[j][k];}}
struct Sample{unsigned blue;int t,weight;};vector<Sample> samples;
struct Count{long long total=0,conflict=0,tblue=0,tred=0,weighted_samples=0,direct_tests=0;};
Count count_failure(const Mat&M){
 array<unsigned,4>P{},Q{};int label=0;
 for(int i=0;i<4;i++)for(int j=0;j<4;j++)for(int z=0;z<M[i][j];z++){
  P[i]|=1u<<label;Q[j]|=1u<<label;label++;}
 assert(label==16);for(auto x:P)assert(pc(x)==4);for(auto x:Q)assert(pc(x)==4);
 Count ans;
 for(auto s:samples){bool pr=false,pb=false,qr=false,qb=false;
 for(auto b:P){pb|=(s.blue&b)==b;pr|=(s.blue&b)==0;}
 for(auto b:Q){qb|=(s.blue&b)==b;qr|=(s.blue&b)==0;}
 bool conflict=(pr&&pb)||(qr&&qb);
 bool bcore=!conflict&&s.t==3&&pr&&qr;
 bool rcore=!conflict&&s.t==0&&pb&&qb;
 bool bad=conflict||bcore||rcore;
 // Literal existence of one of the four center-color assignments.
 bool extend=false;
 for(int ca=0;ca<2;ca++)for(int cb=0;cb<2;cb++){
  bool ok=true;
  for(auto b:P)if((ca==1&&(s.blue&b)==b)||(ca==0&&(s.blue&b)==0))ok=false;
  for(auto b:Q)if((cb==1&&(s.blue&b)==b)||(cb==0&&(s.blue&b)==0))ok=false;
  if(ca==cb&&((ca==1&&s.t==3)||(ca==0&&s.t==0)))ok=false;
  extend|=ok;
 }
 assert(bad==!extend);ans.direct_tests++;
 ans.weighted_samples+=s.weight;
 if(conflict)ans.conflict+=s.weight;if(bcore)ans.tblue+=s.weight;if(rcore)ans.tred+=s.weight;
 if(bad)ans.total+=s.weight;
 }
 assert(ans.weighted_samples==92378&&ans.total==ans.conflict+ans.tblue+ans.tred);
 return ans;
}
void printmat(ostream&o,const Mat&M){o<<'[';for(int i=0;i<4;i++){if(i)o<<',';o<<'[';for(int j=0;j<4;j++){if(j)o<<',';o<<M[i][j];}o<<']';}o<<']';}
int main(int argc,char**argv){double start=cpu();string mode=argc>1?argv[1]:"profile";
 for(int a=0;a<=4;a++)for(int b=0;b<=4-a;b++)for(int c=0;c<=4-a-b;c++)rows.push_back({a,b,c,4-a-b-c});
 Row p={0,1,2,3};do{perms.push_back(p);}while(next_permutation(p.begin(),p.end()));
 assert(rows.size()==35&&perms.size()==24);generate(0,0);double generation=cpu()-start;
 ofstream maps("DOMAIN_MAP.tsv");for(auto z:terminal_map)maps<<z.first<<'\t'<<z.second<<'\n';
 int weight[4]={1,3,3,1};for(unsigned blue=0;blue<(1u<<16);blue++){int t=9-pc(blue);if(t>=0&&t<=3)samples.push_back({blue,t,weight[t]});}
 Mat I{},J{};for(int i=0;i<4;i++)for(int j=0;j<4;j++){I[i][j]=i==j?4:0;J[i][j]=1;}
 auto bi=count_failure(I),bj=count_failure(J);assert(bi.total==10986);
 int limit=mode=="profile"?min(5,(int)reps.size()):(int)reps.size();
 ofstream f(mode=="profile"?"PROFILE.json":"RESULT.json");
 f<<"{\n\"mode\":\""<<mode<<"\",\n\"row_compositions\":"<<rows.size()<<",\n\"row_sorted_terminals\":"<<terminals<<",\n\"canonical_domain\":"<<reps.size()<<",\n\"X_subsets_per_matrix\":"<<samples.size()<<",\n\"S19_sample_space\":92378,\n\"baseline_4I_failure\":"<<bi.total<<",\n\"baseline_all_ones_failure\":"<<bj.total<<",\n\"generation_cpu_seconds\":"<<generation<<",\n\"records\":[\n";
 int id=0,checked=0,worst_id=-1;long long mx=-1,mn=100000;Mat worst{};map<long long,int>hist;
 for(auto &e:reps){if(id>=limit)break;auto M=e.second;auto z=count_failure(M);hist[z.total]++;
 if(checked)f<<",\n";f<<"{\"id\":"<<id<<",\"key\":"<<e.first<<",\"matrix\":";printmat(f,M);
 f<<",\"failure_count\":"<<z.total<<",\"conflict_union\":"<<z.conflict<<",\"T_blue_forced_core\":"<<z.tblue<<",\"T_red_forced_core\":"<<z.tred<<",\"literal_assignment_tests\":"<<z.direct_tests<<"}";
 if(z.total>mx){mx=z.total;worst=M;worst_id=id;}mn=min(mn,z.total);id++;checked++;
 }
 f<<"\n],\n\"checked\":"<<checked<<",\n\"complete\":"<<(checked==(int)reps.size()?"true":"false")<<",\n\"minimum_failure\":"<<mn<<",\n\"maximum_failure\":"<<mx<<",\n\"all_at_most_12763\":"<<(mx<=12763?"true":"false")<<",\n\"worst_id\":"<<worst_id<<",\n\"worst_matrix\":";printmat(f,worst);
 f<<",\n\"histogram\":{";bool first=true;for(auto z:hist){if(!first)f<<',';first=false;f<<'\"'<<z.first<<"\":"<<z.second;}f<<"},\n\"total_cpu_seconds\":"<<cpu()-start<<"\n}\n";
 cout<<"terminals="<<terminals<<" reps="<<reps.size()<<" checked="<<checked<<" min="<<mn<<" max="<<mx<<" I4="<<bi.total<<" J="<<bj.total<<" CPU="<<cpu()-start<<"\n";
}
