// Complete A path-forest spectra for all 140152 A internal partial matchings.
// No claim of positive-crossing T15 closure is made by these local counts.
#include <array>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <cstdint>
#include <algorithm>
using namespace std;
using Edges=vector<pair<int,int>>;
array<vector<Edges>,3> patterns;
array<int,16> fa;
Edges cur;
long long partials[7]={},zero[7]={},sums[7]={};
int mins[7],maxs[7];
void genN(unsigned mask,int family){
 if(!mask){patterns[family].push_back(cur);return;}
 int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);
 for(int j=0;j<4;++j){int b=a^(1<<j);if(!(rest>>b&1u))continue;
  cur.emplace_back(a,b);genN(rest&~(1u<<b),family);cur.pop_back();}
}
void assess(){
 int c=0;unsigned endpoints=0;
 for(int v=1;v<16;++v)if(v!=3&&v!=5&&v!=6&&fa[v]<0){++c;endpoints|=1u<<v;}
 ++partials[c/2];int best=0;
 int us[3]={3,5,6};
 for(int family=0;family<3;++family){
  int u=us[family];unsigned ep=endpoints|((1u<<3)|(1u<<5)|(1u<<6));ep&=~(1u<<u);
  set<uint64_t> spec;
  for(const auto& n:patterns[family]){
   array<vector<int>,16> adj;
   bool ok=true;
   for(int v=1;v<16;++v)if(fa[v]>v){adj[v].push_back(fa[v]);adj[fa[v]].push_back(v);}
   for(auto [a,b]:n){if(fa[a]==b){ok=false;break;}adj[a].push_back(b);adj[b].push_back(a);}
   if(!ok)continue;
   unsigned seen=0;uint64_t code=0;
   for(int a=1;a<16;++a)if((ep>>a&1u)&&!(seen>>a&1u)){
    int prev=-1,v=a;
    while(true){if(seen>>v&1u){ok=false;break;}seen|=1u<<v;
     int next=-1;for(int w:adj[v])if(w!=prev)next=w;
     if(next<0)break;prev=v;v=next;
    }
    if(!ok||v==a||!(ep>>v&1u)){ok=false;break;}
    code|=uint64_t(v)<<(4*a);code|=uint64_t(a)<<(4*v);
   }
   if(ok&&seen==65534u)spec.insert(code);
  }
  best=max(best,int(spec.size()));
 }
 int i=c/2;mins[i]=min(mins[i],best);maxs[i]=max(maxs[i],best);sums[i]+=best;if(!best)++zero[i];
}
void genFA(unsigned mask){
 if(!mask){assess();return;}
 int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);
 genFA(rest);
 for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);fa[a]=b;fa[b]=a;genFA(rest&~(1u<<b));fa[a]=fa[b]=-1;}
}
int main(){
 int us[3]={3,5,6};
 for(int family=0;family<3;++family){int u=us[family];
  vector<int> nei;for(int j=0;j<4;++j){int v=u^(1<<j);if(v)nei.push_back(v);}
  for(int i=0;i<(int)nei.size();++i)for(int j=i+1;j<(int)nei.size();++j){
   int a=nei[i],b=nei[j];cur={{u,a},{u,b}};
   genN(65534u&~(1u<<u)&~(1u<<a)&~(1u<<b),family);
  }
  cerr<<"u="<<u<<" short degree completions="<<patterns[family].size()<<'\n';
 }
 fa.fill(-1);fill(mins,mins+7,1000000);
 genFA(65534u&~(1u<<3)&~(1u<<5)&~(1u<<6));
 cout<<"[";
 for(int i=0;i<7;++i){if(i)cout<<",";cout<<"{\"crossings\":"<<2*i<<",\"A_partials\":"<<partials[i]<<",\"zero_best_spectra\":"<<zero[i]<<",\"min_best_spectrum\":"<<mins[i]<<",\"max_best_spectrum\":"<<maxs[i]<<",\"sum_best_spectrum\":"<<sums[i]<<"}";}
 cout<<"]\n";
}
