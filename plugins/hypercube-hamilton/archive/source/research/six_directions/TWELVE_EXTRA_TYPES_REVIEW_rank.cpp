// Independently reconstruct every legal forest, endpoint pairing, matrix bit and rank.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;using U=uint64_t;constexpr int N=2048;
void need(bool b,string s){if(!b)throw runtime_error(s);}
struct DS{int p[32];DS(){iota(p,p+32,0);}int root(int a){while(p[a]!=a){p[a]=p[p[a]];a=p[a];}return a;}bool join(int a,int b){a=root(a);b=root(b);if(a==b)return false;p[a]=b;return true;}};
vector<unsigned char> bytes(string n,size_t sz){ifstream f(n,ios::binary|ios::ate);need(bool(f),"open "+n);need(size_t(f.tellg())==sz,"size "+n);vector<unsigned char>b(sz);f.seekg(0);f.read((char*)b.data(),sz);need(bool(f),"read "+n);return b;}
array<int,32> pairing(const vector<unsigned char>&b,int at,U terminals){array<int,32>r;r.fill(-1);U seen=0;for(int i=0;i<24;i+=2){int a=b[at+i],c=b[at+i+1];need(a<32&&c<32&&a!=c,"pair labels");need(!(seen>>a&1)&&!(seen>>c&1),"duplicate endpoint");seen|=U(1)<<a|U(1)<<c;r[a]=c;r[c]=a;}need(seen==terminals,"pair support");return r;}
int main(int argc,char**argv){try{need(argc==2,"args");string dir=argv[1];ifstream cfg(dir+"/TWELVE_EXTRA_TYPES_REVIEW_rows.txt");need(bool(cfg),"config");int idx,width,total=0;string prefix;U H,O;bool comma=false;
 cout<<"{\"status\":\"PASS\",\"reports\":[";
 while(cfg>>idx>>prefix>>width>>H>>O){U K=((U(1)<<32)-1)&~H;need(__builtin_popcountll(H)==8&&__builtin_popcountll(K)==24&&(O&~H)==0,"geometry");need(width==34||width==36,"forest width");
  auto S=bytes(dir+"/"+prefix+"_forests.bin",N*width),pairs=bytes(dir+"/"+prefix+"_pairs.bin",N*24),cols=bytes(dir+"/"+prefix+"_columns.bin",N*24),mat=bytes(dir+"/"+prefix+"_matrix.bin",N*256);
  vector<array<int,32>> Ps,Cs;vector<int> terminals;for(int x=0;x<32;x++)if(K>>x&1)terminals.push_back(x);
  for(int i=0;i<N;i++){DS ds;int deg[32]={};bool edge[32][32]={};
   for(int j=0;j<width;j+=2){int a=S[i*width+j],b=S[i*width+j+1];need(a<32&&b<32&&__builtin_popcount(a^b)==1,"short edge");need(!edge[a][b],"duplicate edge");edge[a][b]=edge[b][a]=true;deg[a]++;deg[b]++;need(ds.join(a,b),"forest cycle");}
   for(int x=0;x<32;x++)need(deg[x]==((O>>x&1)?0:(K>>x&1)?1:2),"exact degree/support");
   array<int,32>derived;derived.fill(-1);for(int a:terminals){int mate=-1;for(int b:terminals)if(a!=b&&ds.root(a)==ds.root(b)){need(mate<0,"too many terminal mates");mate=b;}need(mate>=0,"missing endpoint mate");derived[a]=mate;}
   auto P=pairing(pairs,i*24,K);need(P==derived,"derived pairing mismatch");Ps.push_back(P);Cs.push_back(pairing(cols,i*24,K));
  }
  vector<array<U,32>> A(N);for(auto&r:A)r.fill(0);
  for(int i=0;i<N;i++){int component[32];fill(component,component+32,-1);int n=0;
   for(int x:terminals)if(component[x]<0){component[x]=component[Ps[i][x]]=n++;}need(n==12,"path count");
   for(int j=0;j<N;j++){DS ds;int merges=0;for(int x:terminals)if(x<Cs[j][x])merges+=ds.join(component[x],component[Cs[j][x]]);
    bool yes=merges==11;need(yes==bool(mat[i*256+j/8]>>(j%8)&1),"matrix bit mismatch");if(yes)A[i][j/64]|=U(1)<<(j%64);}
  }
  int rank=0;for(int c=0;c<N;c++){int p=rank;while(p<N&&!((A[p][c/64]>>(c%64))&1))p++;if(p==N)continue;swap(A[p],A[rank]);for(int r=rank+1;r<N;r++)if(A[r][c/64]>>(c%64)&1)for(int w=c/64;w<32;w++)A[r][w]^=A[rank][w];rank++;}
  need(rank==N,"rank deficient");if(comma)cout<<',';comma=true;cout<<"{\"index\":"<<idx<<",\"forests\":2048,\"columns\":2048,\"matrix_bits\":4194304,\"rank_GF2\":"<<rank<<'}';total++;
 }
 need(total==11,"row count");cout<<"],\"local_rows\":11,\"forests\":22528,\"columns\":22528,\"matrix_bits\":46137344,\"independent_GF2_eliminations\":11}\n";
 }catch(exception&e){cerr<<e.what()<<endl;return 1;}}
