// Search-free checker. Coverage is a bitmap of independently ranked inputs,
// without reproducing the producer's enumeration order.
#include <array>
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <cstdint>
using namespace std;
using E=vector<pair<int,int>>;
pair<int,int> ed(int a,int b){return minmax(a,b);}
uint64_t choose(int n,int k){uint64_t v=1;for(int i=1;i<=k;i++)v=v*(n-i+1)/i;return v;}
uint64_t df(int n){uint64_t v=1;for(int i=n;i>0;i-=2)v*=i;return v;}
uint64_t fac(int n){uint64_t v=1;for(int i=2;i<=n;i++)v*=i;return v;}
int main(int argc,char**argv){
 assert(argc==4);int c=stoi(argv[1]);assert(c==1||c==3||c==5);ifstream in(argv[2]);int bcount;in>>bcount;
 map<E,int>bindex;
 for(int k=0;k<bcount;k++){vector<int>ports(c);set<int>support;for(int&i:ports){in>>i;assert(i>=0&&i<16);assert(support.insert(i).second);}E edges;
  for(int j=0;j<(13-c)/2;j++){int a,b;in>>a>>b;assert(a>=0&&a<16&&b>=0&&b<16&&a!=b);assert(support.insert(a).second&&support.insert(b).second);edges.push_back(ed(a,b));}
  set<int>expected;for(int v=0;v<16;v++)if(v!=0&&v!=7&&v!=1)expected.insert(v);assert(support==expected);sort(edges.begin(),edges.end());assert(bindex.emplace(edges,k).second);
 }assert(in);string extra;assert(!(in>>extra));
 uint64_t nA=choose(13,c)*df(12-c),nPerm=fac(c),total=nA*bcount*nPerm;
 vector<uint8_t>covered(total,0);vector<int>allowed;for(int v=0;v<16;v++)if(v!=0&&v!=3&&v!=15)allowed.push_back(v);
 ifstream cert(argv[3],ios::binary);assert(cert);unsigned char bytes[56];uint64_t count=0;
 while(cert.read((char*)bytes,56)){
  array<int,16>am,bm,cm;am.fill(-1);bm.fill(-1);cm.fill(-1);bool required[32][32]{};uint32_t supp=0;E be;
  for(int j=0;j<13;j++){int u=bytes[2*j],v=bytes[2*j+1];assert(u<32&&v<32&&u!=v);assert(!(supp>>u&1)&&!(supp>>v&1));supp|=(1u<<u)|(1u<<v);required[u][v]=required[v][u]=true;
   if((u&1)&&(v&1))am[u/2]=v/2,am[v/2]=u/2;
   else if(!(u&1)&&!(v&1))bm[u/2]=v/2,bm[v/2]=u/2,be.push_back(ed(u/2,v/2));
   else {if(!(u&1))swap(u,v);assert(cm[u/2]<0);cm[u/2]=v/2;}
  }
  assert(supp==(0xffffffffu^(1u<<0)^(1u<<1)^(1u<<2)^(1u<<7)^(1u<<14)^(1u<<31)));
  vector<int>ap,bp,remaining;uint64_t portRank=0;int i=0;
  for(int pos=0;pos<13;pos++){int v=allowed[pos];if(cm[v]>=0){ap.push_back(v);bp.push_back(cm[v]);portRank+=choose(pos,++i);}else {assert(am[v]>=0);remaining.push_back(v);}}
  assert(i==c&&remaining.size()==size_t(13-c));
  uint64_t matchingRank=0;while(!remaining.empty()){int a=remaining[0],b=am[a];auto it=find(remaining.begin()+1,remaining.end(),b);assert(it!=remaining.end());int pos=int(it-remaining.begin())-1;matchingRank+=pos*df(int(remaining.size())-3);remaining.erase(it);remaining.erase(remaining.begin());}
  vector<int>sortedbp=bp;sort(sortedbp.begin(),sortedbp.end());assert(adjacent_find(sortedbp.begin(),sortedbp.end())==sortedbp.end());uint64_t permRank=0;
  for(int j=0;j<c;j++){auto it=find(sortedbp.begin(),sortedbp.end(),bp[j]);assert(it!=sortedbp.end());permRank+=uint64_t(it-sortedbp.begin())*fac(c-j-1);sortedbp.erase(it);}
  sort(be.begin(),be.end());auto bi=bindex.find(be);assert(bi!=bindex.end());
  uint64_t rank=((portRank*df(12-c)+matchingRank)*bcount+bi->second)*nPerm+permRank;
  assert(rank<total&&!covered[rank]);covered[rank]=1;
  uint32_t seen=0;int found=0;
  for(int j=0;j<30;j++){unsigned u=bytes[26+j],v=bytes[26+(j+1)%30];assert(u<32&&v<32);assert(!(seen>>u&1));seen|=1u<<u;if(required[u][v])found++;else{unsigned d=u^v;assert(d&&!(d&(d-1)));}}
  assert(seen==(0xffffffffu^(1u<<1)^(1u<<2)));assert(found==13);count++;
 }
 assert(cert.eof()&&cert.gcount()==0);assert(count==total);assert(all_of(covered.begin(),covered.end(),[](int x){return x==1;}));
 cout<<"{\"status\":\"PASS\",\"c\":"<<c<<",\"B_cases\":"<<bcount<<",\"A_partial_matchings\":"<<nA<<",\"bijections\":"<<nPerm<<",\"records\":"<<count<<",\"coverage_method\":\"independent combinadic and matching rank bitmap\",\"total_bytes\":"<<count*56<<"}\n";
}
