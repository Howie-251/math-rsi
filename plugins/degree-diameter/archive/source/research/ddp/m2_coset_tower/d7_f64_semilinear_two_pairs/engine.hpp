// Same semilinear group arithmetic and exact BB/BFS as the checked three-pair engine.
// Only generator legality changes to exactly two involutions.
#pragma once
#include <algorithm>
#include <array>
#include <csignal>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Mask=uint64_t;using Labels=array<int,6>;using Masks=array<Mask,7>;
int fm(int a,int b){int c=0;while(b){if(b&1)c^=a;b>>=1;a<<=1;if(a&64)a^=0x43;}return c;}
struct Engine{
 static constexpr int q=64,L=2688,B=448,n=3200;
 array<array<unsigned char,64>,64>mul{};array<int,21>power{};array<int,64>frob{};
 array<array<unsigned char,64>,42>action{};array<array<int,42>,42>kprod{};
 array<Mask,64>hm{},km{};vector<unsigned short>right;
 vector<int>inverse,pairs,queue;vector<Masks>kwh;vector<array<unsigned short,7>>adj;
 vector<unsigned>seen;unsigned stamp=0;
 Engine():right(L*L),inverse(L),queue(n),kwh(L),adj(n),seen(n){
  for(int x=0;x<64;x++)for(int y=0;y<64;y++)mul[x][y]=fm(x,y);
  power[0]=1;for(int a=1;a<21;a++)power[a]=mul[power[a-1]][8];
  for(int x=0;x<64;x++){int z=mul[x][x];z=mul[z][z];frob[x]=mul[z][z];}
  for(int x=0;x<64;x++)if(frob[frob[x]]!=x)throw runtime_error("bad Frobenius");
  for(int k=0;k<42;k++)for(int x=0;x<64;x++){
   action[k][x]=mul[power[k%21]][k<21?x:frob[x]];km[x]|=Mask(1)<<action[k][x];if(k%7==0)hm[x]|=Mask(1)<<action[k][x];
  }
  for(int k=0;k<42;k++)for(int l=0;l<42;l++)kprod[k][l]=(k%21+(k<21?1:8)*(l%21))%21+21*((k/21+l/21)%2);
  for(int s=0;s<L;s++)for(int a=0;a<L;a++)right[s*L+a]=((a%64)^action[a/64][s%64])+64*kprod[a/64][s/64];
  int involutions=0;array<int,3>classes{};
  for(int a=0;a<L;a++){
   int k=a/64,e=k/21,b=(21-((e?8:1)*(k%21))%21)%21,ki=b+21*e;
   inverse[a]=action[ki][a%64]+64*ki;
   if(product(a,inverse[a])||product(inverse[a],a)||product(0,a)!=a||product(a,0)!=a)throw runtime_error("semilinear inverse/identity mismatch");
   if(a&&a==inverse[a])involutions++;
   if(a<inverse[a]){pairs.push_back(a);int orbit=__builtin_popcountll(km[a%64]);classes[orbit==1?0:orbit==21?1:2]++;}
   for(int k=0;k<42;k++)kwh[a][kprod[k][a/64]%7]|=Mask(1)<<action[k][a%64];
  }
  if(involutions!=87||pairs.size()!=1300||classes!=array<int,3>{19,420,861})throw runtime_error("wrong semilinear inverse-pair classification");
  for(int a=0;a<L;a++)adj[a][0]=L+a%64+64*((a/64)%7);
  for(int b=0;b<7;b++)for(int x=0;x<64;x++){
   int u=L+x+64*b;for(int j=0;j<6;j++)adj[u][j]=x+64*(b+7*j);adj[u][6]=L+B+x;
  }
  for(int x=0;x<64;x++)for(int b=0;b<7;b++)adj[L+B+x][b]=L+x+64*b;
 }
 int product(int a,int b)const{return right[b*L+a];}
 bool legal(const Labels&S){set<int>v(S.begin(),S.end());if(v.size()!=6||v.count(0))return false;int invol=0;for(int s:S){if(s<0||s>=L||!v.count(inverse[s]))return false;invol+=(s==inverse[s]);}return invol==2;}
 Labels make(int a,int b,int c){return {a,inverse[a],b,inverse[b],c,inverse[c]};}
 bool hh(const Labels&S){Mask z=1;for(int s:S)z|=km[s%64];return z==~Mask(0);}
 Masks bb(const Labels&S){Masks masks{};Mask common=1;for(int s:S)common|=hm[s%64];
  for(int b=0;b<7;b++){masks[b]=common|kwh[0][b];for(int s:S)masks[b]|=kwh[s][b];}
  masks[0]|=hm[0];
  for(int a:S){masks[(a/64)%7]|=hm[a%64];for(int b:S){int ab=product(a,b);masks[(ab/64)%7]|=hm[ab%64];for(int c:S){int abc=product(ab,c);masks[(abc/64)%7]|=hm[abc%64];}}}
  return masks;
 }
 int missing(const Masks&m){int z=B;for(Mask a:m)z-=__builtin_popcountll(a);return z;}
 void build(const Labels&S){for(int j=0;j<6;j++){const unsigned short*t=&right[S[j]*L];for(int a=0;a<L;a++)adj[a][j+1]=t[a];}}
 int bfs(int root){++stamp;int read=0,end=1;queue[0]=root;seen[root]=stamp;
  for(int depth=0;depth<5&&read<end&&end<n;depth++){int boundary=end;while(read<boundary){int a=queue[read++];for(int b:adj[a])if(seen[b]!=stamp){seen[b]=stamp;queue[end++]=b;}}}return n-end;
 }
 array<int,3>roots(){return {bfs(0),bfs(L),bfs(L+B)};}
 Masks bfs_block_masks(){bfs(L);Masks out{};for(int b=0;b<B;b++)if(seen[L+b]==stamp)out[b/64]|=Mask(1)<<(b%64);return out;}
 long long bad(const array<int,3>&a){return (2688LL*a[0]+448LL*a[1]+64LL*a[2])/2;}
 void save(string prefix,const Labels&S,long long cursor,int branch,array<int,2>pair_indices,bool full){
  auto masks=bb(S);ofstream f(prefix+".json");f<<"{\"group\":\"GF64 semidirect (C21 semidirect C2), Frob8\",\"n\":3200,\"degree\":7,\"candidate_cursor\":"<<cursor<<",\"first_branch\":"<<branch<<",\"other_pair_indices_in_1300_table\":["<<pair_indices[0]<<","<<pair_indices[1]<<"],\"S_ids\":[";
  for(int j=0;j<6;j++)f<<(j?",":"")<<S[j];f<<"],\"S_coordinates\":[";for(int j=0;j<6;j++)f<<(j?",":"")<<"["<<S[j]%64<<","<<(S[j]/64)%21<<","<<S[j]/1344<<"]";
  f<<"],\"HH_pass\":"<<(hh(S)?"true":"false")<<",\"BB_missing\":"<<missing(masks)<<",\"BB_masks\":[";for(int b=0;b<7;b++)f<<(b?",":"")<<masks[b];f<<"]";
  if(full){build(S);if(masks!=bfs_block_masks())throw runtime_error("semilinear BB formula/BFS mismatch");auto a=roots();f<<",\"root_missing_leaf_block_head\":["<<a[0]<<","<<a[1]<<","<<a[2]<<"],\"bad_unordered_pairs\":"<<bad(a);
   ofstream edge(prefix+".edges");edge<<n<<" 11200\n";int ne=0;for(int u=0;u<n;u++)for(int v:adj[u])if(u<v){edge<<u<<" "<<v<<"\n";ne++;}if(ne!=11200)throw runtime_error("wrong edge count");
  }f<<"}\n";
 }
};
