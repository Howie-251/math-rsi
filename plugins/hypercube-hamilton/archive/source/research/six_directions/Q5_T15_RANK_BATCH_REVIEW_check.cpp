// Independent reviewer checker, adapted from the reviewer's frozen T26 checker; T15 parameter instantiation audited independently.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <set>
#include <cassert>
#include <cstdint>
#include <string>
using namespace std;
constexpr int N=26,R=4096,FB=34,MB=512,COMP=13,WORDS=64;
vector<unsigned char> read(const string& p){ifstream f(p,ios::binary);assert(f);return vector<unsigned char>((istreambuf_iterator<char>(f)),{});}
int root(int* p,int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(int argc,char**argv){assert(argc==2);string pre=argv[1];int h[6],u[2];ifstream cfg(pre+"_config.txt");assert(cfg);for(auto&x:h)cfg>>x;for(auto&x:u)cfg>>x;assert(cfg);bool hole[32]={},omit[32]={};for(int x:h){assert(x>=0&&x<32&&!hole[x]);hole[x]=1;}for(int x:u){assert(hole[x]&&!omit[x]);omit[x]=1;}
 auto f=read(pre+"_forests.bin"),r=read(pre+"_pairs.bin"),c=read(pre+"_columns.bin"),m=read(pre+"_matrix.bin");assert(f.size()==R*FB&&r.size()==R*N&&c.size()==R*N&&m.size()==R*MB);
 for(auto *b:{&r,&c})for(int i=0;i<R;i++){bool seen[32]={};for(int k=0;k<N;k++){int x=(*b)[i*N+k];assert(x<32&&!hole[x]&&!seen[x]);seen[x]=true;}}
 for(int i=0;i<R;i++){int deg[32]={},p[32];for(int x=0;x<32;x++)p[x]=x;set<pair<int,int>> ed;
  for(int k=0;k<FB;k+=2){int x=f[i*FB+k],y=f[i*FB+k+1];assert(x<y&&y<32&&!omit[x]&&!omit[y]&&__builtin_popcount(x^y)==1);assert(ed.insert({x,y}).second);deg[x]++;deg[y]++;int a=root(p,x),b=root(p,y);assert(a!=b);p[a]=b;}
  for(int x=0;x<32;x++)assert(deg[x]==(omit[x]?0:hole[x]?2:1));
  set<pair<int,int>> expected,actual;for(int x=0;x<32;x++)if(!hole[x])for(int y=x+1;y<32;y++)if(!hole[y]&&root(p,x)==root(p,y))expected.insert({x,y});
  for(int k=0;k<N;k+=2){int x=r[i*N+k],y=r[i*N+k+1];actual.insert({min(x,y),max(x,y)});}assert(expected.size()==COMP&&expected==actual);
 }
 vector<unsigned char> computed(m.size());for(int i=0;i<R;i++){int component[32];for(int k=0;k<N;k++)component[r[i*N+k]]=k/2;
  for(int j=0;j<R;j++){int p[COMP],count=COMP;for(int k=0;k<COMP;k++)p[k]=k;for(int k=0;k<N;k+=2){int a=root(p,component[c[j*N+k]]),b=root(p,component[c[j*N+k+1]]);if(a!=b){p[a]=b;count--;}}if(count==1)computed[i*MB+j/8]|=1<<(j%8);}
 }assert(computed==m);
 using Row=array<uint64_t,WORDS>;vector<Row> rows(R);for(int i=0;i<R;i++)for(int k=0;k<MB;k++)rows[i][k/8]|=uint64_t(m[i*MB+k])<<(8*(k%8));int rank=0;
 for(int col=0;col<R;col++){int pivot=rank;while(pivot<R&&!((rows[pivot][col/64]>>(col%64))&1))pivot++;if(pivot==R)continue;swap(rows[pivot],rows[rank]);for(int i=rank+1;i<R;i++)if((rows[i][col/64]>>(col%64))&1)for(int k=col/64;k<WORDS;k++)rows[i][k]^=rows[rank][k];rank++;}
 assert(rank==R);cout<<"PASS forests=4096 columns=4096 bits=16777216 rank=4096\n";
}

