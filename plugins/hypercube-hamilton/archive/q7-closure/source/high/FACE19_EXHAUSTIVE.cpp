#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;
using U=uint32_t;
struct Face { U e,o; int orbit=-1; array<int,6> d; };
int pc(U x){return __builtin_popcount(x);}
int parity(int x){return __builtin_parity((unsigned)x);}
int main(){
 array<vector<int>,2> verts; int index[64];
 for(int x=0;x<64;x++){index[x]=verts[parity(x)].size();verts[parity(x)].push_back(x);}
 array<U,32> nbr{};
 for(int a=0;a<32;a++)for(int j=0;j<6;j++)nbr[a]|=U(1)<<index[verts[0][a]^(1<<j)];
 vector<array<array<int,32>,2>> generators;
 for(int t=1;t<6;t++){
  array<array<int,32>,2> g;
  for(int p=0;p<2;p++)for(int a=0;a<32;a++)g[p][a]=index[verts[p][a]^1^(1<<t)];
  generators.push_back(g);
 }
 for(int t=0;t<5;t++){
  array<array<int,32>,2> g;
  for(int p=0;p<2;p++)for(int a=0;a<32;a++){
   int x=verts[p][a];if(((x>>t)^(x>>(t+1)))&1)x^=(1<<t)|(1<<(t+1));g[p][a]=index[x];
  }generators.push_back(g);
 }
 auto transport=[](U z,const array<int,32>& g){U q=0;while(z){int a=__builtin_ctz(z);z&=z-1;q|=U(1)<<g[a];}return q;};
 ofstream report("FACE19_RESULT.json"), all("FACE19_ALL.jsonl"), pairs("FACE19_COMPATIBLE.jsonl");
 report<<"{\"dimension\":6,\"holes_per_face\":19,\"direction_cap\":7,\"tiers\":[";
 for(int r=6;r<=9;r++){
  int q=19-r;vector<Face> f;uint64_t tested=0;
  auto add=[&](U e,U o){Face z{e,o};for(int j=0;j<6;j++){
   int d=0;for(int a=0;a<32;a++){if(!(verts[0][a]&(1<<j))&&(e>>a&1))d++;if(!(verts[1][a]&(1<<j))&&(o>>a&1))d--;}
   z.d[j]=d;
  }f.push_back(z);};
  auto subsets=[&](auto&& self,U avail,int need,U chosen,U e)->void{
   if(need==0){add(e,chosen);return;}if(pc(avail)<need)return;
   while(avail){int j=__builtin_ctz(avail);avail&=avail-1;self(self,avail,need-1,chosen|(U(1)<<j),e);}
  };
  auto enumerate=[&](auto&& self,int start,int need,U e,U excluded)->void{
   if(!need){tested++;U avail=~excluded;if(pc(avail)>=q)subsets(subsets,avail,q,0,e);return;}
   for(int a=start;a<=32-need;a++)self(self,a+1,need-1,e|(U(1)<<a),excluded|nbr[a]);
  };enumerate(enumerate,0,r,0,0);
  sort(f.begin(),f.end(),[](auto&a,auto&b){return pair(a.e,a.o)<pair(b.e,b.o);});
  map<pair<U,U>,int> lookup;for(int i=0;i<(int)f.size();i++)assert(lookup.emplace(pair(f[i].e,f[i].o),i).second);
  vector<int> reps,sizes;
  for(int seed=0;seed<(int)f.size();seed++)if(f[seed].orbit<0){
   int oid=reps.size(),size=0;reps.push_back(seed);queue<int> queue;queue.push(seed);f[seed].orbit=oid;
   while(!queue.empty()){
    int a=queue.front();queue.pop();size++;
    for(auto&g:generators){auto key=pair(transport(f[a].e,g[0]),transport(f[a].o,g[1]));auto it=lookup.find(key);assert(it!=lookup.end());int b=it->second;
     if(f[b].orbit<0){f[b].orbit=oid;queue.push(b);}else assert(f[b].orbit==oid);
    }
   }sizes.push_back(size);
  }
  for(int i=0;i<(int)f.size();i++)all<<"{\"r\":"<<r<<",\"id\":"<<i<<",\"even_mask\":"<<f[i].e<<",\"odd_mask\":"<<f[i].o<<",\"orbit\":"<<f[i].orbit<<"}\n";
  int compatible=0,best=100;map<int,int> histogram;
  for(int a:reps)for(int b=0;b<(int)f.size();b++){
   if((f[a].e&f[b].e)||(f[a].o&f[b].o))continue;
   compatible++;array<int,7>d;int maxd=abs(2*r-19);d[6]=2*r-19;
   for(int j=0;j<6;j++){d[j]=f[a].d[j]-f[b].d[j];maxd=max(maxd,abs(d[j]));}
   best=min(best,maxd);histogram[maxd]++;
   pairs<<"{\"r\":"<<r<<",\"a_id\":"<<a<<",\"b_id\":"<<b<<",\"delta\":[";
   for(int j=0;j<7;j++)pairs<<(j?",":"")<<d[j];pairs<<"],\"max_abs\":"<<maxd<<"}\n";
  }
  if(r>6)report<<",";
  report<<"{\"r\":"<<r<<",\"s\":"<<q<<",\"minority_subsets_tested\":"<<tested<<",\"faces\":"<<f.size()<<",\"orbits\":"<<reps.size()<<",\"representatives\":[";
  for(int i=0;i<(int)reps.size();i++)report<<(i?",":"")<<"{\"id\":"<<reps[i]<<",\"size\":"<<sizes[i]<<"}";
  report<<"],\"compatible_pairs\":"<<compatible<<",\"min_max_abs_delta\":"<<best<<",\"max_abs_histogram\":{";
  bool first=true;for(auto [v,n]:histogram){report<<(first?"":",")<<"\""<<v<<"\":"<<n;first=false;}report<<"}}";
  cout<<"r="<<r<<" faces="<<f.size()<<" orbits="<<reps.size()<<" compatible="<<compatible<<" minmax="<<best<<endl;
  assert(best>7);
 }
 report<<"],\"surviving_pairs\":0,\"enumerated_original_matchings\":0,\"uses_old_atlas\":false}\n";
}
