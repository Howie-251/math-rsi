#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <set>
#include <cassert>
#include <cstdint>
#include <string>
using namespace std;
vector<unsigned char> rd(string p){ifstream f(p,ios::binary);assert(f);return vector<unsigned char>((istreambuf_iterator<char>(f)),{});}
int root(int*p,int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
int main(int argc,char**argv){assert(argc==3);string pre=argv[1];bool forced=stoi(argv[2]);int N=forced?1024:2048,n=forced?22:24,B=N/8;int holes[8],om[3],pq[2]={-1,-1};ifstream cfg(pre+"_config.txt");assert(cfg);for(int&x:holes)cfg>>x;for(int&x:om)cfg>>x;if(forced)for(int&x:pq)cfg>>x;assert(cfg);bool H[32]={},O[32]={};assert(holes[0]==0);for(int x:holes){assert(x>=0&&x<32&&!H[x]);H[x]=true;}for(int x:om){assert(H[x]&&!O[x]);O[x]=true;}for(int k=1;k<8;k++)assert(__builtin_popcount(holes[k])%2==1);if(forced){assert(pq[0]==8&&pq[1]==16);for(int x:om)assert(x==1||x==2||x==4);assert(!H[8]&&!H[16]);}
 auto f=rd(pre+"_forests.bin"),r=rd(pre+"_pairs.bin"),c=rd(pre+"_columns.bin"),m=rd(pre+"_matrix.bin"),pv=rd(pre+"_pivots.bin"),co=rd(pre+"_combos.bin"),full=forced?rd(pre+"_full_pairs.bin"):r;
 assert(f.size()==N*34&&r.size()==N*n&&c.size()==N*n&&m.size()==N*B&&full.size()==N*24&&pv.size()==m.size()&&co.size()==m.size());
 for(auto*b:{&r,&c})for(int i=0;i<N;i++){bool seen[32]={};for(int k=0;k<n;k++){int x=(*b)[i*n+k];assert(x<32&&!H[x]&&!seen[x]&&(!forced||(x!=8&&x!=16)));seen[x]=true;}}
 for(int i=0;i<N;i++){int deg[32]={},p[32];for(int x=0;x<32;x++)p[x]=x;set<pair<int,int>>edges;for(int k=0;k<34;k+=2){int x=f[i*34+k],y=f[i*34+k+1];assert(x<y&&y<32&&!O[x]&&!O[y]&&__builtin_popcount(x^y)==1);assert(edges.insert({x,y}).second);deg[x]++;deg[y]++;int a=root(p,x),b=root(p,y);assert(a!=b);p[a]=b;}
  for(int x=0;x<32;x++)assert(deg[x]==(O[x]?0:H[x]?2:1));set<pair<int,int>>actual,expected,reduced;bool seen[32]={};for(int k=0;k<24;k+=2){int x=full[i*24+k],y=full[i*24+k+1];assert(x<32&&y<32&&!H[x]&&!H[y]&&!seen[x]&&!seen[y]&&x!=y);seen[x]=seen[y]=true;actual.insert({min(x,y),max(x,y)});}for(int x=0;x<32;x++)if(!H[x])for(int y=x+1;y<32;y++)if(!H[y]&&root(p,x)==root(p,y))expected.insert({x,y});assert(expected.size()==12&&actual==expected);if(forced){assert(edges.count({0,8})&&edges.count({0,16})&&actual.erase({8,16})==1);}for(int k=0;k<n;k+=2){int x=r[i*n+k],y=r[i*n+k+1];reduced.insert({min(x,y),max(x,y)});}assert(actual==reduced);
 }
 vector<unsigned char>computed(m.size());for(int i=0;i<N;i++){int component[32];for(int k=0;k<n;k++)component[r[i*n+k]]=k/2;for(int j=0;j<N;j++){int p[12],count=n/2;for(int k=0;k<n/2;k++)p[k]=k;for(int k=0;k<n;k+=2){int a=root(p,component[c[j*n+k]]),b=root(p,component[c[j*n+k+1]]);if(a!=b){p[a]=b;count--;}}if(count==1)computed[i*B+j/8]|=1<<(j%8);}}assert(computed==m);
 // Rank is computed anew; producer pivot/combination certificates also checked separately.
 using Row=array<uint64_t,32>;vector<Row>rows(N);for(int i=0;i<N;i++)for(int k=0;k<B;k++)rows[i][k/8]|=uint64_t(m[i*B+k])<<(8*(k%8));int rank=0;for(int col=0;col<N;col++){int z=rank;while(z<N&&!((rows[z][col/64]>>(col%64))&1))z++;if(z==N)continue;swap(rows[z],rows[rank]);for(int i=rank+1;i<N;i++)if((rows[i][col/64]>>(col%64))&1)for(int k=col/64;k<N/64;k++)rows[i][k]^=rows[rank][k];rank++;}assert(rank==N);
 for(int j=0;j<N;j++){vector<unsigned char>out(B);for(int i=0;i<N;i++)if((co[j*B+i/8]>>(i%8))&1)for(int k=0;k<B;k++)out[k]^=m[i*B+k];for(int k=0;k<B;k++)assert(out[k]==pv[j*B+k]);assert((out[j/8]>>(j%8))&1);for(int k=j+1;k<N;k++)assert(!((out[k/8]>>(k%8))&1));}
 cout<<"{\"prefix\":\""<<pre<<"\",\"forced\":"<<forced<<",\"forests\":"<<N<<",\"columns\":"<<N<<",\"bits\":"<<N*N<<",\"rank\":"<<rank<<",\"status\":\"PASS\"}"<<endl;
}
