#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <iterator>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
int N,R,E,W,B;
using Bits=vector<uint64_t>;
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
vector<unsigned char> load(const string&f,size_t n){
 ifstream in(f,ios::binary);need(bool(in),"missing "+f);
 vector<unsigned char> a((istreambuf_iterator<char>(in)),{});
 need(a.size()==n,"size "+f);return a;
}
struct DSU{
 array<int,32> p; int components;
 DSU(int n=32):components(n){iota(p.begin(),p.end(),0);}
 int find(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
 bool join(int a,int b){a=find(a);b=find(b);if(a==b)return false;p[a]=b;--components;return true;}
};
Bits decode(const vector<unsigned char>&a,int row){
 Bits b(W,0);for(int j=0;j<B;++j)b[j/8]|=uint64_t(a[row*B+j])<<(8*(j%8));return b;
}
vector<pair<int,int>> pairs(const unsigned char*a,const vector<int>&K){
 uint32_t seen=0,expected=0;for(int x:K)expected|=uint32_t(1)<<x;
 vector<pair<int,int>> ans;
 for(int i=0;i<N/2;++i){int x=a[2*i],y=a[2*i+1];need(x<32&&y<32&&x!=y,"pair domain");
  uint32_t m=(uint32_t(1)<<x)|(uint32_t(1)<<y);need(!(seen&m),"pair repeated endpoint");seen|=m;
  ans.push_back(minmax(x,y));
 }need(seen==expected,"pair endpoint set");sort(ans.begin(),ans.end());return ans;
}
int main(){try{
 ifstream table("TWELVE_NEW_TYPES_LOCAL_REVIEW_geometries.txt");need(bool(table),"geometry table");
 int idx,number=0;long long forests=0,bits=0,comboChecks=0;
 cout<<"{\"rows\":[";
 while(table>>idx){
  int nh,nu;need(bool(table>>N>>R>>E>>nh>>nu),"geometry dimensions");W=R/64;B=R/8;need((N==22&&R==1024)||(N==24&&R==2048),"dimensions");vector<int> H(nh),U(nu);for(int&x:H)need(bool(table>>x),"geometry H");for(int&x:U)need(bool(table>>x),"geometry U");
  string sn=to_string(idx);while(sn.size()<3)sn="0"+sn;string pre="TWELVE_NEW_TYPES_orbit_"+sn;
  ifstream cfg(pre+"_config.txt");vector<int> got;int z;while(cfg>>z)got.push_back(z);
  vector<int> want=H;want.insert(want.end(),U.begin(),U.end());need(got==want,"config geometry "+sn);
  array<int,32> degrees{};array<int,32> pos;pos.fill(-1);vector<int>K;
  for(int x=0;x<32;++x){if(find(H.begin(),H.end(),x)==H.end()){pos[x]=K.size();K.push_back(x);degrees[x]=1;}
   else degrees[x]=find(U.begin(),U.end(),x)==U.end()?2:0;
  }need(K.size()==size_t(N),"K size");
  auto fs=load(pre+"_forests.bin",R*2*E),ps=load(pre+"_pairs.bin",R*N),cs=load(pre+"_columns.bin",R*N);
  auto mat=load(pre+"_matrix.bin",R*B),piv=load(pre+"_pivots.bin",R*B),comb=load(pre+"_combos.bin",R*B);
  vector<vector<pair<int,int>>> derived(R),cols(R);
  for(int i=0;i<R;++i){
   DSU d;array<int,32> deg{};bool used[32][32]{};
   for(int j=0;j<E;++j){int a=fs[i*2*E+2*j],b=fs[i*2*E+2*j+1];need(a<32&&b<32&&__builtin_popcount(unsigned(a^b))==1,"nonshort forest");
    need(!used[a][b],"duplicate edge");used[a][b]=used[b][a]=true;need(d.join(a,b),"forest cycle");++deg[a];++deg[b];
   }need(deg==degrees,"forest degrees");
   vector<vector<int>> ends(32);for(int x:K)ends[d.find(x)].push_back(x);
   vector<pair<int,int>> actual;
   for(auto &v:ends)if(!v.empty()){need(v.size()==2,"component terminal count");actual.push_back(minmax(v[0],v[1]));}
   need(actual.size()==size_t(N/2),"component number");sort(actual.begin(),actual.end());
   need(actual==pairs(&ps[i*N],K),"stored pairing differs from independent forest DSU");
   for(auto [a,b]:actual)derived[i].push_back({pos[a],pos[b]});
   auto cp=pairs(&cs[i*N],K);for(auto[a,b]:cp)cols[i].push_back({pos[a],pos[b]});
   ++forests;
  }
  vector<Bits> rebuilt(R,Bits(W,0));
  for(int i=0;i<R;++i){DSU base(N);for(auto[a,b]:derived[i])base.join(a,b);
   for(int j=0;j<R;++j){DSU d=base;for(auto[a,b]:cols[j])d.join(a,b);
    bool v=d.components==1;bool stored=(mat[i*B+j/8]>>(j%8))&1;
    need(v==stored,"connectivity mismatch "+sn+" "+to_string(i)+" "+to_string(j));
    if(v)rebuilt[i][j/64]|=uint64_t(1)<<(j%64);++bits;
   }
  }
  // Independent rank: ascending pivots on reconstructed rows, not supplied pivots.
  vector<Bits> basis(R,Bits(W,0));vector<bool> active(R,false);int rank=0;
  for(auto row:rebuilt){for(int w=0;w<W;++w){while(row[w]){
    int j=w*64+__builtin_ctzll(row[w]);
    if(!active[j]){basis[j]=row;active[j]=true;++rank;goto nextrow;}
    for(int q=w;q<W;++q)row[q]^=basis[j][q];
   }}nextrow:;}
  need(rank==R,"rank deficient "+sn);
  // Also validate all producer combination equations and highest-pivot positions.
  for(int i=0;i<R;++i){Bits b=decode(piv,i),co=decode(comb,i),sum(W,0);
   need((b[i/64]>>(i%64))&1,"pivot missing");
   for(int j=i+1;j<R;++j)need(!((b[j/64]>>(j%64))&1),"pivot leading position");
   for(int w=0;w<W;++w)while(co[w]){int j=w*64+__builtin_ctzll(co[w]);co[w]&=co[w]-1;for(int q=0;q<W;++q)sum[q]^=rebuilt[j][q];}
   need(sum==b,"combo mismatch "+sn);++comboChecks;
  }
  if(number++)cout<<",";cout<<"{\"index\":"<<idx<<",\"rank\":"<<rank<<",\"endpoints\":"<<N<<",\"forests\":"<<R<<",\"connectivity_bits\":"<<R*R<<"}";
  cerr<<"verified "<<idx<<" rank "<<rank<<"\n";
 }
 need(number==111,"claimed row count");cout<<"],\"rows_checked\":"<<number<<",\"forests_checked\":"<<forests<<",\"connectivity_bits_checked\":"<<bits<<",\"combination_equations_checked\":"<<comboChecks<<",\"pass\":true}\n";
}catch(const exception&e){cerr<<"CHECK FAILED: "<<e.what()<<"\n";return 1;}return 0;}
