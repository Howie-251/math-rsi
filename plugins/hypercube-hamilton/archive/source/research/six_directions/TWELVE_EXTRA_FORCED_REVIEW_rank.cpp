// Independent 24->22 terminal fixed-cherry reduced forest/rank verification.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;using U=uint64_t;constexpr int N=1024;
void req(bool b,string s){if(!b)throw runtime_error(s);}
struct DS{int p[32];DS(){iota(p,p+32,0);}int root(int a){while(p[a]!=a){p[a]=p[p[a]];a=p[a];}return a;}bool join(int a,int b){a=root(a);b=root(b);if(a==b)return false;p[a]=b;return true;}};
vector<unsigned char> read(string n,size_t size){ifstream f(n,ios::binary|ios::ate);req(bool(f),"open "+n);req(size_t(f.tellg())==size,"size "+n);vector<unsigned char>b(size);f.seekg(0);f.read((char*)b.data(),size);req(bool(f),"read "+n);return b;}
array<int,32> pairmap(vector<unsigned char>&b,int at,int n,U terminals){array<int,32>r;r.fill(-1);U seen=0;for(int i=0;i<n;i+=2){int a=b[at+i],c=b[at+i+1];req(a<32&&c<32&&a!=c,"pair label");req(!(seen>>a&1)&&!(seen>>c&1),"pair duplicate endpoint");seen|=U(1)<<a|U(1)<<c;r[a]=c;r[c]=a;}req(seen==terminals,"pair support");return r;}
int main(int argc,char**argv){try{req(argc==2,"args");string dir=argv[1],prefix;ifstream cfg(dir+"/TWELVE_EXTRA_FORCED_REVIEW_rows.txt");req(bool(cfg),"rows");int idx,h,p,q,total=0;U H,O;bool comma=false;cout<<"{\"status\":\"PASS\",\"reports\":[";
 while(cfg>>idx>>prefix>>H>>O>>h>>p>>q){U K=((U(1)<<32)-1)&~H,Kp=K&~(U(1)<<p)&~(U(1)<<q);req(__builtin_popcountll(K)==24&&__builtin_popcountll(Kp)==22,"terminal counts");U neighbors=0;for(int d=0;d<5;d++)if(!(O>>(h^(1<<d))&1))neighbors|=U(1)<<(h^(1<<d));req(neighbors==((U(1)<<p)|(U(1)<<q)),"available cherry neighbors");
  auto S=read(dir+"/"+prefix+"_forests.bin",N*34),full=read(dir+"/"+prefix+"_full_pairs.bin",N*24),red=read(dir+"/"+prefix+"_pairs.bin",N*22),cols=read(dir+"/"+prefix+"_columns.bin",N*22),mat=read(dir+"/"+prefix+"_matrix.bin",N*128);
  vector<array<int,32>> P,C;vector<int> terminals;for(int x=0;x<32;x++)if(Kp>>x&1)terminals.push_back(x);
  for(int i=0;i<N;i++){DS ds;int deg[32]={};bool edge[32][32]={};for(int j=0;j<34;j+=2){int a=S[i*34+j],b=S[i*34+j+1];req(a<32&&b<32&&__builtin_popcount(a^b)==1,"forest short edge");req(!edge[a][b],"duplicate forest edge");edge[a][b]=edge[b][a]=true;deg[a]++;deg[b]++;req(ds.join(a,b),"forest cycle");}
   for(int x=0;x<32;x++)req(deg[x]==((O>>x&1)?0:(K>>x&1)?1:2),"forest degree/support");req(edge[p][h]&&edge[h][q]&&deg[p]==1&&deg[q]==1&&deg[h]==2,"physical full fixed cherry");
   array<int,32>derived;derived.fill(-1);for(int a=0;a<32;a++)if(K>>a&1){int mate=-1;for(int b=0;b<32;b++)if(a!=b&&(K>>b&1)&&ds.root(a)==ds.root(b)){req(mate<0,"multiple endpoint mates");mate=b;}req(mate>=0,"missing endpoint mate");derived[a]=mate;}
   auto fp=pairmap(full,i*24,24,K);req(fp==derived&&fp[p]==q&&fp[q]==p,"actual full pairs");derived[p]=derived[q]=-1;auto rp=pairmap(red,i*22,22,Kp);req(rp==derived,"exact fixed pair deletion");P.push_back(rp);C.push_back(pairmap(cols,i*22,22,Kp));
  }
  vector<array<U,16>> A(N);for(auto&r:A)r.fill(0);
  for(int i=0;i<N;i++){int comp[32];fill(comp,comp+32,-1);int n=0;for(int x:terminals)if(comp[x]<0){comp[x]=comp[P[i][x]]=n++;}req(n==11,"reduced row components");for(int j=0;j<N;j++){DS ds;int joins=0;for(int x:terminals)if(x<C[j][x])joins+=ds.join(comp[x],comp[C[j][x]]);bool yes=joins==10;req(yes==bool(mat[i*128+j/8]>>(j%8)&1),"connectivity matrix bit");if(yes)A[i][j/64]|=U(1)<<(j%64);}}
  int rank=0;for(int c=0;c<N;c++){int pivot=rank;while(pivot<N&&!((A[pivot][c/64]>>(c%64))&1))pivot++;if(pivot==N)continue;swap(A[rank],A[pivot]);for(int r=rank+1;r<N;r++)if(A[r][c/64]>>(c%64)&1)for(int w=c/64;w<16;w++)A[r][w]^=A[rank][w];rank++;}req(rank==N,"GF2 rank");if(comma)cout<<',';comma=true;cout<<"{\"index\":"<<idx<<",\"forests\":1024,\"columns\":1024,\"matrix_bits\":1048576,\"rank_GF2\":"<<rank<<'}';total++;
 }
 req(total==15,"rows count");cout<<"],\"local_rows\":15,\"forests\":15360,\"columns\":15360,\"matrix_bits\":15728640,\"independent_GF2_eliminations\":15}\n";
 }catch(exception&e){cerr<<e.what()<<endl;return 1;}}
