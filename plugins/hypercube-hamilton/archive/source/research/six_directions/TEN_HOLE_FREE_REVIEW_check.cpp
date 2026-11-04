// Fresh exhaustive ten-independent-hole geometry checker. No author code used.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;
struct Reason {int kind,index,pi;};
unordered_map<uint64_t,Reason> accepted;
ofstream witness("TEN_HOLE_FREE_REVIEW_witness.tsv");
int pc(int x){return __builtin_popcount((unsigned)x);}
int project(int x,int d){return (x&((1<<d)-1))|((x>>(d+1))<<d);}
bool basic(int a,int b){return (a==1&&b==2)||(a==2&&b==3)||(a==2&&b==2)||(a==3&&b==3)||(a==1&&b==3)||(a==2&&b==4)||(a==4&&b==3)||(a==2&&b==5);}
struct Counts {uint64_t zs=0,eligible=0,rows=0,t15=0,remaining=0,core=0,split=0; map<int,uint64_t> cores;};
Counts census(int v){
 Counts count; vector<int> evens;
 for(int x=1;x<64;x++)if(pc(x)%2==0&&pc(x^v)!=1)evens.push_back(x);
 array<int,4> z;array<int,5>w;w[0]=v;
 for(int a=0;a<(int)evens.size();a++)for(int b=a+1;b<(int)evens.size();b++)for(int c=b+1;c<(int)evens.size();c++)for(int e=c+1;e<(int)evens.size();e++){
  z={evens[a],evens[b],evens[c],evens[e]};count.zs++;
  vector<int> odds;
  for(int x=0;x<64;x++)if(pc(x)%2==1&&pc(x)!=1&&x!=v){bool good=true;for(int y:z)if(pc(x^y)==1)good=false;if(good)odds.push_back(x);}
  for(int f=0;f<(int)odds.size();f++)for(int g=f+1;g<(int)odds.size();g++)for(int h=g+1;h<(int)odds.size();h++)for(int j=h+1;j<(int)odds.size();j++){
   w[1]=odds[f];w[2]=odds[g];w[3]=odds[h];w[4]=odds[j];count.eligible++;
   int aa[6]={},bb[6]={}; bool done=false;
   for(int d=0;d<6;d++){for(int x:z)aa[d]+=((x^v)&(1<<d))==0;for(int x:w)bb[d]+=((x^v)&(1<<d))==0;if(basic(aa[d],bb[d]))done=true;}
   if(done){count.rows++;continue;}
   for(int d=0;d<6&&!done;d++)if((aa[d]==3&&bb[d]==2)||(aa[d]==1&&bb[d]==4)){
    vector<int> sources,minorities,included;
    auto inside=[&](int x){return ((x^v)&(1<<d))==0;};
    if(aa[d]==3){for(int x:z){if(inside(x))sources.push_back(x);else minorities.push_back(x);}for(int x:w)if(!inside(x))included.push_back(x);}
    else {for(int x:w){if(!inside(x))minorities.push_back(x);else if(x!=v&&x!=(1<<d))sources.push_back(x);}for(int x:z)if(!inside(x))included.push_back(x);}
    assert(minorities.size()==1&&included.size()==3);int m=minorities[0];
    for(int p=0;p<(int)sources.size()&&!done;p++)for(int q=p+1;q<(int)sources.size()&&!done;q++){
     uint64_t om=0,inc=0;for(int x:{sources[p],sources[q]}){int y=project((x^(1<<d))^m,d);assert(pc(y)%2);om|=1ULL<<y;}for(int x:included){int y=project(x^m,d);assert(pc(y)%2);inc|=1ULL<<y;}
     assert(__builtin_popcountll(om)==2&&__builtin_popcountll(inc)==3&&!(om&inc));
     auto found=accepted.find(om|(inc<<32));if(found==accepted.end())continue;
     Reason r=found->second;count.t15++;if(r.kind==0){count.core++;count.cores[r.index]++;}else count.split++;
     witness<<v;for(int x:z)witness<<'\t'<<x;for(int x:w)witness<<'\t'<<x;
     witness<<'\t'<<d<<'\t'<<sources[p]<<'\t'<<sources[q]<<'\t'<<r.kind<<'\t'<<r.index<<'\t'<<r.pi<<'\n';done=true;
    }
   }
   if(!done){count.remaining++;cerr<<"Uncovered v="<<v<<" Z=";for(int x:z)cerr<<x<<',';cerr<<" W=";for(int x:w)cerr<<x<<',';cerr<<'\n';}
  }
 }
 assert(count.eligible==count.rows+count.t15+count.remaining);
 return count;
}
int main(){
 ifstream lookup("TEN_HOLE_FREE_REVIEW_lookup.txt");assert(lookup);uint64_t k;Reason r;while(lookup>>k>>r.kind>>r.index>>r.pi){assert(!accepted.count(k));accepted[k]=r;}assert(accepted.size()>1000);
 ofstream out("TEN_HOLE_FREE_REVIEW_census.json");out<<"{\"targets\":[";uint64_t failures=0;
 for(int v:{7,31}){Counts c=census(v);failures+=c.remaining;if(v!=7)out<<',';out<<"{\"v\":"<<v<<",\"even_quadruples\":"<<c.zs<<",\"eligible\":"<<c.eligible<<",\"basic_rows\":"<<c.rows<<",\"T15\":"<<c.t15<<",\"core\":"<<c.core<<",\"split\":"<<c.split<<",\"remaining\":"<<c.remaining<<",\"selected_cores\":{";bool first=true;for(auto [id,n]:c.cores){if(!first)out<<',';out<<'\"'<<id<<"\":"<<n;first=false;}out<<"}}";cout<<"target "<<v<<": eligible="<<c.eligible<<", basic="<<c.rows<<", T15="<<c.t15<<", remaining="<<c.remaining<<endl;}
 out<<"],\"remaining\":"<<failures<<"}\n";return failures?1:0;
}
