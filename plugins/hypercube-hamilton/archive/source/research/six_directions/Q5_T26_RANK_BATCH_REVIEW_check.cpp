#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <set>
#include <cassert>
#include <cstdint>
#include <string>
using namespace std;
vector<unsigned char> read(const string& p){ifstream f(p,ios::binary);assert(f);return vector<unsigned char>((istreambuf_iterator<char>(f)),{});}
int findroot(int* p,int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(int argc,char**argv){assert(argc==2);string pre=argv[1];int h[8],u[2];ifstream cfg(pre+"_config.txt");assert(cfg);for(auto&x:h)cfg>>x;for(auto&x:u)cfg>>x;assert(cfg);bool hole[32]={},omit[32]={};for(int x:h){assert(x>=0&&x<32&&!hole[x]);hole[x]=1;}for(int x:u){assert(hole[x]&&!omit[x]);omit[x]=1;}
 auto f=read(pre+"_forests.bin"),r=read(pre+"_pairs.bin"),c=read(pre+"_columns.bin"),m=read(pre+"_matrix.bin");
 assert(f.size()==2048*36&&r.size()==2048*24&&c.size()==2048*24&&m.size()==2048*256);
 for(auto *b:{&r,&c})for(int i=0;i<2048;i++){bool seen[32]={};for(int k=0;k<24;k++){int x=(*b)[i*24+k];assert(x<32&&!hole[x]&&!seen[x]);seen[x]=true;}}
 for(int i=0;i<2048;i++){int deg[32]={},p[32];for(int x=0;x<32;x++)p[x]=x;set<pair<int,int>> ed;
  for(int k=0;k<36;k+=2){int x=f[i*36+k],y=f[i*36+k+1];assert(x<y&&y<32&&!omit[x]&&!omit[y]&&__builtin_popcount(x^y)==1);assert(ed.insert({x,y}).second);deg[x]++;deg[y]++;int a=findroot(p,x),b=findroot(p,y);assert(a!=b);p[a]=b;}
  for(int x=0;x<32;x++)assert(deg[x]==(omit[x]?0:hole[x]?2:1));
  set<pair<int,int>> expected,actual;for(int x=0;x<32;x++)if(!hole[x])for(int y=x+1;y<32;y++)if(!hole[y]&&findroot(p,x)==findroot(p,y))expected.insert({x,y});
  for(int k=0;k<24;k+=2){int x=r[i*24+k],y=r[i*24+k+1];actual.insert({min(x,y),max(x,y)});}assert(expected.size()==12&&expected==actual);
 }
 vector<unsigned char> computed(m.size());
 for(int i=0;i<2048;i++){int component[32];for(int k=0;k<24;k++)component[r[i*24+k]]=k/2;
  for(int j=0;j<2048;j++){int p[12],count=12;for(int k=0;k<12;k++)p[k]=k;for(int k=0;k<24;k+=2){int a=findroot(p,component[c[j*24+k]]),b=findroot(p,component[c[j*24+k+1]]);if(a!=b){p[a]=b;count--;}}if(count==1)computed[i*256+j/8]|=1<<(j%8);}
 }assert(computed==m);
 // Independent increasing-column Gaussian elimination using 64-bit row blocks.
 using Row=array<uint64_t,32>;vector<Row> rows(2048);for(int i=0;i<2048;i++)for(int k=0;k<256;k++)rows[i][k/8]|=uint64_t(m[i*256+k])<<(8*(k%8));int rank=0;
 for(int col=0;col<2048;col++){int pivot=rank;while(pivot<2048&&!((rows[pivot][col/64]>>(col%64))&1))pivot++;if(pivot==2048)continue;swap(rows[pivot],rows[rank]);for(int i=rank+1;i<2048;i++)if((rows[i][col/64]>>(col%64))&1)for(int k=col/64;k<32;k++)rows[i][k]^=rows[rank][k];rank++;}
 assert(rank==2048);cout<<pre<<" PASS forests=2048 columns=2048 bits=4194304 rank=2048\n";
}
