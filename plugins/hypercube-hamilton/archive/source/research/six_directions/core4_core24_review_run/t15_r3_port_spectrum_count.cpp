// Exact local spectra for A holes0,r,s. Diagnostic bound using B negative counts.
#include <array>
#include <vector>
#include <set>
#include <iostream>
#include <fstream>
#include <cstdint>
#include <algorithm>
using namespace std;
using Edges=vector<pair<int,int>>;
array<int,16> fa;vector<Edges> patterns[2];Edges cur;int rs[2];
struct Test{int name,n0,n1;long long closed[7]{},open[7]{};};
vector<Test> tests;long long totals[7]{};int minR[2][7],minQ[2][7];
uint64_t calls;
void genN(unsigned mask,int f){if(!mask){patterns[f].push_back(cur);return;}int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);
 for(int j=0;j<4;j++){int b=a^(1<<j);if(rest>>b&1u){cur.emplace_back(a,b);genN(rest&~(1u<<b),f);cur.pop_back();}}}
void assess(){
 vector<int> ports;unsigned ep=0;for(int v=1;v<16;v++)if(v!=rs[0]&&v!=rs[1]&&fa[v]<0){ports.push_back(v);ep|=1u<<v;}
 int c=ports.size(),lev=c/2;++totals[lev];array<int,16> qcounts[2];int rcounts[2];
 for(int f=0;f<2;f++){
  int z=rs[f];unsigned ends=ep|(1u<<z);set<uint64_t> spec;
  for(auto& h:patterns[f]){
   int adj[16][2],deg[16]{};bool ok=true;
   for(int v=1;v<16;v++)if(fa[v]>v){adj[v][deg[v]++]=fa[v];adj[fa[v]][deg[fa[v]]++]=v;}
   for(auto [a,b]:h){if(fa[a]==b){ok=false;break;}adj[a][deg[a]++]=b;adj[b][deg[b]++]=a;}
   if(!ok)continue;unsigned seen=0;uint64_t key=0;
   for(int a=1;a<16;a++)if((ends>>a&1u)&&!(seen>>a&1u)){
    int prev=-1,v=a;
    while(true){if(seen>>v&1u){ok=false;break;}seen|=1u<<v;int next=-1;for(int j=0;j<deg[v];j++)if(adj[v][j]!=prev)next=adj[v][j];if(next<0)break;prev=v;v=next;}
    if(!ok||v==a||!(ends>>v&1u)){ok=false;break;}key|=uint64_t(v)<<(4*a);key|=uint64_t(a)<<(4*v);
   }
   if(ok&&seen==65534u)spec.insert(key);
  }
  rcounts[f]=spec.size();minR[f][lev]=min(minR[f][lev],rcounts[f]);
  qcounts[f].fill(0);
  for(int d:ports){
   set<uint64_t> quotient;
   for(uint64_t key:spec){int a=(key>>(4*z))&15,b=(key>>(4*d))&15;if(a==d)continue;
    uint64_t code=key;for(int v:{z,d,a,b})code&=~(uint64_t(15)<<(4*v));code|=uint64_t(b)<<(4*a);code|=uint64_t(a)<<(4*b);quotient.insert(code);
   }
   qcounts[f][d]=quotient.size();minQ[f][lev]=min(minQ[f][lev],qcounts[f][d]);
  }
 }
 for(auto& t:tests){int ns[2]={t.n0,t.n1};bool internal[2];vector<int> bad[2];
  for(int f=0;f<2;f++){internal[f]=(c<13&&rcounts[f]<=ns[f]);for(int d:ports)if(qcounts[f][d]<=ns[f])bad[f].push_back(d);}
  bool fail=(internal[0]&&(internal[1]||!bad[1].empty()))||(internal[1]&&!bad[0].empty());
  for(int a:bad[0])for(int b:bad[1])if(a!=b)fail=true;
  (fail?t.open:t.closed)[lev]++;
 }
}
void genFA(unsigned mask){if(!mask){assess();return;}int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);genFA(rest);
 for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);fa[a]=b;fa[b]=a;genFA(rest&~(1u<<b));fa[a]=fa[b]=-1;}}
int main(int argc,char**argv){if(argc!=2)return 2;rs[0]=3;rs[1]=stoi(argv[1]);
 if(rs[1]==5)tests={{0,3,3},{5,3,2},{23,10,10},{26,10,50}};
 else if(rs[1]==15)tests={{8,3,10},{15,1,10},{27,50,10}};else return 3;
 for(int f=0;f<2;f++){int u=rs[1-f];vector<int> neighbors;for(int j=0;j<4;j++){int v=u^(1<<j);if(v)neighbors.push_back(v);}
  for(int i=0;i<(int)neighbors.size();i++)for(int j=i+1;j<(int)neighbors.size();j++){int a=neighbors[i],b=neighbors[j];cur={{u,a},{u,b}};genN(65534u&~(1u<<u)&~(1u<<a)&~(1u<<b),f);}
  fill(minR[f],minR[f]+7,1000000);fill(minQ[f],minQ[f]+7,1000000);
 }
 fa.fill(-1);genFA(65534u&~(1u<<rs[0])&~(1u<<rs[1]));
 cout<<"{\"A_holes\":[0,3,"<<rs[1]<<"],\"short_degree_patterns\":["<<patterns[0].size()<<","<<patterns[1].size()<<"],\"levels\":[";
 for(int l=0;l<7;l++){if(l)cout<<",";cout<<"{\"c\":"<<2*l+1<<",\"partials\":"<<totals[l]<<",\"min_R\":["<<minR[0][l]<<","<<minR[1][l]<<"],\"min_Q\":["<<minQ[0][l]<<","<<minQ[1][l]<<"]}";}
 cout<<"],\"threshold_tests\":[";bool sep=false;for(auto&t:tests){if(sep)cout<<",";sep=true;cout<<"{\"core\":"<<t.name<<",\"negative_thresholds\":["<<t.n0<<","<<t.n1<<"],\"closed_by_count\":[";for(int l=0;l<7;l++){if(l)cout<<",";cout<<t.closed[l];}cout<<"],\"unresolved\":[";for(int l=0;l<7;l++){if(l)cout<<",";cout<<t.open[l];}cout<<"]}";}cout<<"]}\n";
}
