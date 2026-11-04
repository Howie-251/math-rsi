// Independent rectangular connectivity-rank certificate verifier.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;using U=uint64_t;constexpr int NR=8128,NC=8192,NW=128;
void req(bool b,string s){if(!b)throw runtime_error(s);}
struct DS{int p[32];DS(){iota(p,p+32,0);}int root(int a){while(p[a]!=a){p[a]=p[p[a]];a=p[a];}return a;}bool join(int a,int b){a=root(a);b=root(b);if(a==b)return false;p[a]=b;return true;}};
vector<unsigned char> read(string n,size_t size){ifstream f(n,ios::binary|ios::ate);req(bool(f),"open "+n);req(size_t(f.tellg())==size,"size "+n);vector<unsigned char>b(size);f.seekg(0);f.read((char*)b.data(),size);req(bool(f),"read "+n);return b;}
array<int,32> pairing(vector<unsigned char>&b,int at,U terminals){array<int,32>r;r.fill(-1);U seen=0;for(int j=0;j<28;j+=2){int a=b[at+j],c=b[at+j+1];req(a<32&&c<32&&a!=c,"pair label");req(!(seen>>a&1)&&!(seen>>c&1),"duplicate pair endpoint");seen|=U(1)<<a|U(1)<<c;r[a]=c;r[c]=a;}req(seen==terminals,"pair support");return r;}
int main(int argc,char**argv){try{req(argc==2,"args");string dir=argv[1],prefix=dir+"/TWELVE_ROOT_STAR_MIXED_probe";U H=(U(1)<<0)|(U(1)<<1)|(U(1)<<3)|(U(1)<<31),O=(U(1)<<0)|(U(1)<<31),K=((U(1)<<32)-1)&~H;
 const pair<int,int>R[]={{4,6},{8,10},{13,15},{16,18},{21,23},{25,27},{28,30}};
 auto S=read(prefix+"_forests.bin",NR*32),pairs=read(prefix+"_pairs.bin",NR*28),cols=read(prefix+"_columns.bin",NC*28),mat=read(prefix+"_matrix.bin",NR*1024);
 vector<array<int,32>>P,C;vector<int>terminals;for(int x=0;x<32;x++)if(K>>x&1)terminals.push_back(x);
 int minR=8,maxR=0;
 for(int i=0;i<NR;i++){DS ds;int degree[32]={};bool edge[32][32]={};int oddCross=0,evenCross=0;
  for(int j=0;j<32;j+=2){int a=S[i*32+j],b=S[i*32+j+1];req(a<32&&b<32&&__builtin_popcount(a^b)==1,"short forest edge");req(!edge[a][b],"duplicate forest edge");edge[a][b]=edge[b][a]=true;degree[a]++;degree[b]++;req(ds.join(a,b),"forest cycle");if((a^b)==2){int x=(a&2)?b:a;if(__builtin_popcount(x)%2)oddCross++;else evenCross++;}}
  for(int x=0;x<32;x++)req(degree[x]==((O>>x&1)?0:(K>>x&1)?1:2),"exact degree and support");req(oddCross-evenCross==2&&oddCross>=2,"half-layer degree identity");
  array<int,32>derived;derived.fill(-1);for(int a:terminals){int mate=-1;for(int b:terminals)if(a!=b&&ds.root(a)==ds.root(b)){req(mate<0,"multiple terminal mates");mate=b;}req(mate>=0,"missing terminal mate");derived[a]=mate;}
  auto actual=pairing(pairs,i*28,K);req(actual==derived,"actual endpoint pairing");int rc=0;for(auto[a,b]:R)if(actual[a]==b){req(edge[a][b],"R pair physical isolated path");rc++;}req(rc>=1,"row annihilates all bad columns");minR=min(minR,rc);maxR=max(maxR,rc);P.push_back(actual);
 }
 for(int j=0;j<NC;j++)C.push_back(pairing(cols,j*28,K));
 vector<array<U,NW>> A(NR);for(auto&r:A)r.fill(0);
 for(int i=0;i<NR;i++){int component[32];fill(component,component+32,-1);int n=0;for(int x:terminals)if(component[x]<0){component[x]=component[P[i][x]]=n++;}req(n==14,"fourteen forest paths");for(int j=0;j<NC;j++){DS ds;int joins=0;for(int x:terminals)if(x<C[j][x])joins+=ds.join(component[x],component[C[j][x]]);bool yes=joins==13;req(yes==bool(mat[i*1024+j/8]>>(j%8)&1),"matrix connectivity bit");if(yes)A[i][j/64]|=U(1)<<(j%64);}}
 int rank=0;for(int col=0;col<NC&&rank<NR;col++){int pivot=rank;while(pivot<NR&&!((A[pivot][col/64]>>(col%64))&1))pivot++;if(pivot==NR)continue;swap(A[pivot],A[rank]);for(int row=rank+1;row<NR;row++)if(A[row][col/64]>>(col%64)&1)for(int w=col/64;w<NW;w++)A[row][w]^=A[rank][w];rank++;}req(rank==NR,"independent rectangular GF2 rank");
 cout<<"{\"status\":\"PASS\",\"forests\":8128,\"derived_pairings\":8128,\"columns\":8192,\"connectivity_bits\":66584576,\"matrix_rows\":8128,\"matrix_columns\":8192,\"independent_rank_GF2\":"<<rank<<",\"all_forest_rows_annihilate_bad_columns\":true,\"min_selected_R_pairs\":"<<minR<<",\"max_selected_R_pairs\":"<<maxR<<",\"all_half_layer_degree_identities_checked\":true}\n";
 }catch(exception&e){cerr<<e.what()<<endl;return 1;}}
