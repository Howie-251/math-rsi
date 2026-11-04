// c4 diagnostic: complete A forest spectra, closed under all crossing bijections.
#include <array>
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <unordered_map>
#include <unordered_set>
using namespace std;
using Edges=vector<pair<int,int>>;
struct DSU{int p[40];bool ok=true;DSU(){for(int i=0;i<40;++i)p[i]=i;}int root(int v){return p[v]==v?v:p[v]=root(p[v]);}void add(int a,int b){int x=root(a),y=root(b);if(x==y)ok=false;else p[x]=y;}};
array<vector<Edges>,3> pats;
array<int,16> fa;array<int,4> ports;
array<int,6> rm;vector<array<int,6>> matchings;map<unsigned,int> mi;
map<uint64_t,long long> types;ofstream witnesses;
unsigned code(const array<int,6>& m){unsigned x=0;for(int i=0;i<6;++i)x|=unsigned(m[i])<<(3*i);return x;}
void genR(unsigned mask){if(!mask){mi[code(rm)]=matchings.size();matchings.push_back(rm);return;}int a=__builtin_ctz(mask);for(int b=a+1;b<6;++b)if(mask>>b&1){rm[a]=b;rm[b]=a;genR(mask&~(1u<<a)&~(1u<<b));}}
void genN(unsigned mask,Edges cur,int f){if(!mask){pats[f].push_back(cur);return;}int a=__builtin_ctz(mask);for(int b=a+1;b<16;++b)if((mask>>b&1)&&__builtin_popcount(unsigned(a^b))==1){auto n=cur;n.emplace_back(a,b);genN(mask&~(1u<<a)&~(1u<<b),n,f);}}
void assess(){int us[3]={3,5,6};uint64_t signature=0;
 for(int f=0;f<3;++f){array<int,6> ep;for(int i=0;i<4;++i)ep[i]=ports[i];int k=4;for(int v:us)if(v!=us[f])ep[k++]=v;
  for(auto& n:pats[f]){DSU g;for(int a=1;a<16;++a)if(fa[a]>a)g.add(a,fa[a]);for(auto [a,b]:n)g.add(a,b);if(!g.ok)continue;array<int,6> m;for(int i=0;i<6;++i){m[i]=-1;for(int j=0;j<6;++j)if(i!=j&&g.root(ep[i])==g.root(ep[j])){assert(m[i]<0);m[i]=j;}assert(m[i]>=0);}signature|=1ull<<(15*f+mi.at(code(m)));}
 }
 ++types[signature];witnesses<<signature;for(int v:ports)witnesses<<' '<<v;for(int a=1;a<16;++a)if(fa[a]>a)witnesses<<' '<<a<<' '<<fa[a];witnesses<<'\n';
}
void pairA(unsigned mask){if(!mask){assess();return;}int a=__builtin_ctz(mask);for(int b=a+1;b<16;++b)if(mask>>b&1){fa[a]=b;fa[b]=a;pairA(mask&~(1u<<a)&~(1u<<b));fa[a]=fa[b]=-1;}}
void portChoose(vector<int> base,int pos,int at,unsigned mask){if(at==4){pairA(mask);return;}for(int i=pos;i<(int)base.size();++i){ports[at]=base[i];portChoose(base,i+1,at+1,mask&~(1u<<base[i]));}}

array<unordered_set<uint64_t>,3> bad;
struct Node{int zero=-1,one=-1;uint64_t allor=0,alland=(1ull<<45)-1,sample=0;};vector<Node> trie(1);
void insertMask(uint64_t s){int node=0;for(int bit=44;bit>=-1;--bit){trie[node].allor|=s;trie[node].alland&=s;trie[node].sample=s;if(bit<0)break;bool b=s>>bit&1;int next=b?trie[node].one:trie[node].zero;if(next<0){next=trie.size();if(b)trie[node].one=next;else trie[node].zero=next;trie.emplace_back();}node=next;}}
uint64_t subsetQuery(int node,int bit,uint64_t good){if(node<0||(trie[node].alland&good))return 0;if(!(trie[node].allor&good))return trie[node].sample;assert(bit>=0);uint64_t z=subsetQuery(trie[node].zero,bit-1,good);if(z)return z;if(!(good>>bit&1ull))return subsetQuery(trie[node].one,bit-1,good);return 0;}
uint64_t mcode(const array<int,16>& m){uint64_t c=0;for(int a=1;a<16;++a)if(m[a]>=0)c|=uint64_t(m[a])<<(4*a);return c;}
long long totalB=0,failedB=0,zeroB=0;unordered_map<uint64_t,uint64_t> cache;ofstream failB;
void assessB(){int us[3]={3,5,6};uint64_t signature=0;
 for(int f=0;f<3;++f){int s=-1,t=-1;for(int v:us)if(v!=us[f]){if(s<0)s=v;else t=v;}
  for(int r=0;r<15;++r){DSU g;for(int a=2;a<16;++a)if(fa[a]>a)g.add(a,fa[a]);g.add(s,16+s);g.add(t,16+t);int ep[6];for(int i=0;i<4;++i)ep[i]=ports[i];ep[4]=16+s;ep[5]=16+t;for(int i=0;i<6;++i)if(matchings[r][i]>i)g.add(ep[i],ep[matchings[r][i]]);if(!g.ok)continue;
   array<int,16> lm;lm.fill(-1);for(int a=2;a<16;++a)if(a!=s&&a!=t){for(int b=2;b<16;++b)if(b!=a&&b!=s&&b!=t&&g.root(a)==g.root(b)){assert(lm[a]<0);lm[a]=b;}assert(lm[a]>=0);}if(!bad[f].count(mcode(lm)))signature|=1ull<<(15*f+r);
  }
 }
 ++totalB;if(!signature)++zeroB;auto it=cache.find(signature);uint64_t witness;
 if(it==cache.end()){witness=subsetQuery(0,44,signature);cache[signature]=witness;}else witness=it->second;
 if(witness){++failedB;failB<<signature<<' '<<witness;for(int v:ports)failB<<' '<<v;for(int a=2;a<16;++a)if(fa[a]>a)failB<<' '<<a<<' '<<fa[a];failB<<'\n';}
}
void pairB(unsigned mask){if(!mask){assessB();return;}int a=__builtin_ctz(mask);for(int b=a+1;b<16;++b)if(mask>>b&1){fa[a]=b;fa[b]=a;pairB(mask&~(1u<<a)&~(1u<<b));fa[a]=fa[b]=-1;}}
void chooseB(int pos,int at,unsigned mask){if(at==4){pairB(mask);return;}for(int v=pos;v<16;++v){ports[at]=v;chooseB(v+1,at+1,mask&~(1u<<v));}}
int main(int argc,char**argv){assert(argc==4);genR(63u);assert(matchings.size()==15);ifstream ni(argv[1]);int f;while(ni>>f){array<int,16> m;m.fill(-1);for(int i=0;i<6;++i){int a,b;ni>>a>>b;m[a]=b;m[b]=a;}bad[f].insert(mcode(m));}ifstream masks(argv[2]);uint64_t mask;while(masks>>mask)insertMask(mask);cerr<<"trie nodes="<<trie.size()<<'\n';failB.open(argv[3]);fa.fill(-1);chooseB(2,0,65532u);assert(totalB==945945);cout<<"{\"scope\":\"c4 B compatibility diagnostic\",\"B_partials\":"<<totalB<<",\"B_types\":"<<cache.size()<<",\"zero_B\":"<<zeroB<<",\"B_with_some_failing_A_orientation\":"<<failedB<<",\"trie_nodes\":"<<trie.size()<<"}\n";}
