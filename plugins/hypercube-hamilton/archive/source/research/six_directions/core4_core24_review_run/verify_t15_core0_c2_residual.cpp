// Positive witness verifier. Does not invoke a search procedure.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <cassert>
#include <cstdint>
using namespace std;
struct BCase{int p,q;array<pair<int,int>,6> edges;};
vector<BCase> bs;array<int,16> mate;int ap,aq;ifstream certificates;uint64_t checked=0;
void check(){
 vector<pair<int,int>> fa;for(int a=0;a<16;++a)if(mate[a]>a)fa.emplace_back(2*a+1,2*mate[a]+1);
 for(auto& b:bs)for(int rev=0;rev<2;++rev){
  auto required=fa;for(auto [x,y]:b.edges)required.emplace_back(2*x,2*y);required.emplace_back(2*ap+1,2*(rev?b.q:b.p));required.emplace_back(2*aq+1,2*(rev?b.p:b.q));
  assert(required.size()==13);array<unsigned char,56> rec;certificates.read(reinterpret_cast<char*>(rec.data()),56);assert(certificates.gcount()==56);
  bool req[32][32]{};for(int i=0;i<13;++i){auto [x,y]=required[i];assert(rec[2*i]==x&&rec[2*i+1]==y);req[x][y]=req[y][x]=true;}
  uint32_t seen=0;int required_found=0;
  for(int i=0;i<30;++i){unsigned x=rec[26+i],y=rec[26+(i+1)%30];assert(x<32&&y<32);assert(!(seen>>x&1u));seen|=1u<<x;if(req[x][y])++required_found;else assert(__builtin_popcount(x^y)==1);}
  assert(seen==(0xffffffffu&~2u&~4u)&&required_found==13);++checked;
 }
}
void pairs(vector<int> vs){if(vs.empty()){check();return;}int a=vs[0];for(int i=1;i<(int)vs.size();++i){int b=vs[i];vector<int> rem;for(int j=1;j<(int)vs.size();++j)if(j!=i)rem.push_back(vs[j]);mate[a]=b;mate[b]=a;pairs(rem);mate[a]=mate[b]=-1;}}
int main(int argc,char**argv){assert(argc==3);ifstream in(argv[1]);BCase b;while(in>>b.p>>b.q){for(auto& [x,y]:b.edges)in>>x>>y;bs.push_back(b);}assert(bs.size()==24);certificates.open(argv[2],ios::binary);mate.fill(-1);
 vector<int> base;for(int x=1;x<16;++x)if(x!=3&&x!=5&&x!=6)base.push_back(x);
 for(int i=0;i<12;++i)for(int j=i+1;j<12;++j){ap=base[i];aq=base[j];vector<int> rem;for(int x:base)if(x!=ap&&x!=aq)rem.push_back(x);pairs(rem);}
 assert(checked==2993760);char extra;assert(!certificates.get(extra));cout<<"{\"status\":\"PASS\",\"positive_certificates\":"<<checked<<",\"exact_support\":30,\"required_edges\":13,\"record_bytes\":56,\"total_bytes\":"<<checked*56<<"}\n";
}

