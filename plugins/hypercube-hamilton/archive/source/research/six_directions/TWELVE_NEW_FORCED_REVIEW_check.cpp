// Independent legal-forest, fixed-cherry, connectivity-matrix and rank verifier.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;using U=uint64_t;
void need(bool b,string s){if(!b)throw runtime_error(s);}
struct DS{int p[32];DS(){iota(p,p+32,0);}int root(int a){while(p[a]!=a){p[a]=p[p[a]];a=p[a];}return a;}bool join(int a,int b){a=root(a);b=root(b);if(a==b)return false;p[a]=b;return true;}};
vector<unsigned char> bytes(string name,size_t n){ifstream f(name,ios::binary|ios::ate);need(bool(f),"open "+name);need(size_t(f.tellg())==n,"size "+name);vector<unsigned char>b(n);f.seekg(0);f.read((char*)b.data(),n);need(bool(f),"read "+name);return b;}
array<int,32> pairing(const vector<unsigned char>&b,int at,int n,U terminals){array<int,32>r;r.fill(-1);U seen=0;for(int i=0;i<n;i+=2){int a=b[at+i],c=b[at+i+1];need(a<32&&c<32&&a!=c,"pair labels");need(!(seen>>a&1)&&!(seen>>c&1),"duplicate pair endpoint");seen|=U(1)<<a|U(1)<<c;r[a]=c;r[c]=a;}need(seen==terminals,"pair support");return r;}
int main(int argc,char**argv){try{
 need(argc==2,"arg directory");string dir=argv[1];ifstream cfg(dir+"/TWELVE_NEW_FORCED_REVIEW_rows.txt");need(bool(cfg),"review rows");
 string prefix;int idx,width,h,p,q;U H,O;bool comma=false;int total=0;
 cout<<"{\"status\":\"PASS\",\"reports\":[";
 while(cfg>>idx>>prefix>>width>>H>>O>>h>>p>>q){
  need((width==34||width==36)&&h<32&&p<32&&q<32,"row format");
  U K=((U(1)<<32)-1)&~H,Kprime=K&~(U(1)<<p)&~(U(1)<<q);
  need(__builtin_popcountll(H)==10&&__builtin_popcountll(K)==22&&__builtin_popcountll(Kprime)==20,"endpoint counts");
  need((H>>h&1)&&!(O>>h&1)&&(K>>p&1)&&(K>>q&1)&&p!=q&&(O&~H)==0,"cherry marked membership");
  U neighbors=0;for(int d=0;d<5;d++){int x=h^(1<<d);if(!(O>>x&1))neighbors|=U(1)<<x;}
  need(neighbors==((U(1)<<p)|(U(1)<<q)),"exact available cherry neighbors");
  int omitted=__builtin_popcountll(O);need(omitted==(width==36?3:4),"type omission count");
  auto S=bytes(dir+"/"+prefix+"_forests.bin",512*width),full=bytes(dir+"/"+prefix+"_full_pairs.bin",512*22),red=bytes(dir+"/"+prefix+"_pairs.bin",512*20),cols=bytes(dir+"/"+prefix+"_columns.bin",512*20),matrix=bytes(dir+"/"+prefix+"_matrix.bin",512*64);
  vector<array<int,32>> Ps,Cs;vector<int>terminal;for(int x=0;x<32;x++)if(Kprime>>x&1)terminal.push_back(x);
  for(int i=0;i<512;i++){
   DS ds;int degree[32]={};bool edge[32][32]={};
   for(int e=0;e<width;e+=2){int a=S[i*width+e],b=S[i*width+e+1];need(a<32&&b<32&&__builtin_popcount(a^b)==1,"forest short edge");need(!edge[a][b],"duplicate forest edge");edge[a][b]=edge[b][a]=true;degree[a]++;degree[b]++;need(ds.join(a,b),"forest cycle");}
   for(int x=0;x<32;x++)need(degree[x]==((O>>x&1)?0:(K>>x&1)?1:2),"forest exact degrees");
   need(edge[p][h]&&edge[h][q]&&degree[h]==2&&degree[p]==1&&degree[q]==1,"physical fixed cherry");
   array<int,32>derived;derived.fill(-1);for(int a=0;a<32;a++)if(K>>a&1){int mate=-1;for(int b=0;b<32;b++)if(a!=b&&(K>>b&1)&&ds.root(a)==ds.root(b)){need(mate<0,"component multiple terminal mates");mate=b;}need(mate>=0,"component missing mate");derived[a]=mate;}
   auto fp=pairing(full,i*22,22,K);need(fp==derived,"full forest endpoint pairing");need(fp[p]==q&&fp[q]==p,"full fixed pair");
   auto rp=pairing(red,i*20,20,Kprime);derived[p]=derived[q]=-1;need(rp==derived,"exact reduced pair deletion");Ps.push_back(rp);
   Cs.push_back(pairing(cols,i*20,20,Kprime));
  }
  vector<array<U,8>> A(512);for(auto&r:A)r.fill(0);
  for(int i=0;i<512;i++){
   int component[32];fill(component,component+32,-1);int n=0;
   for(int x:terminal)if(component[x]<0){component[x]=component[Ps[i][x]]=n++;}need(n==10,"row contraction");
   for(int j=0;j<512;j++){
    DS ds;int merges=0;for(int x:terminal)if(x<Cs[j][x])merges+=ds.join(component[x],component[Cs[j][x]]);
    bool connected=merges==9;need(connected==bool(matrix[i*64+j/8]>>(j%8)&1),"matrix bit mismatch");
    if(connected)A[i][j/64]|=U(1)<<(j%64);
   }
  }
  int rank=0;for(int col=0;col<512;col++){
   int pivot=rank;while(pivot<512&&!((A[pivot][col/64]>>(col%64))&1))pivot++;
   if(pivot==512)continue;swap(A[rank],A[pivot]);
   for(int row=rank+1;row<512;row++)if(A[row][col/64]>>(col%64)&1)for(int w=col/64;w<8;w++)A[row][w]^=A[rank][w];rank++;
  }
  need(rank==512,"recomputed GF2 rank");total++;
  if(comma)cout<<',';comma=true;cout<<"{\"index\":"<<idx<<",\"forest_rows\":512,\"matrix_bits\":262144,\"GF2_rank\":"<<rank<<",\"fixed_cherry_and_pairings_checked\":true}";
 }
 need(total==27,"exact row count");cout<<"],\"local_rows\":27,\"forests\":13824,\"columns\":13824,\"matrix_bits\":7077888,\"independent_GF2_eliminations\":27}\n";
 }catch(exception&e){cerr<<e.what()<<endl;return 1;}}
