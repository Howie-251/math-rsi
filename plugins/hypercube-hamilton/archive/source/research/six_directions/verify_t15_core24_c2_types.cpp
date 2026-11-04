// Independent verifier: disjoint-set components replace the producer's walks.
#include <array>
#include <vector>
#include <unordered_set>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cassert>
#include <cstdint>
using namespace std;
using Edges=vector<pair<int,int>>;
struct DSU{int p[40],degree[40]{};bool ok=true;DSU(){for(int i=0;i<40;++i)p[i]=i;}int root(int v){return p[v]==v?v:p[v]=root(p[v]);}void add(int a,int b){if(a==b||++degree[a]>2||++degree[b]>2)ok=false;int x=root(a),y=root(b);if(x==y)ok=false;else p[x]=y;}};
array<vector<Edges>,3> pats;
array<unordered_set<uint64_t>,3> bad;
long long at[512]{},bt[512]{};
uint64_t enc(const array<int,16>& m){uint64_t k=0;for(int v=0;v<16;++v)if(m[v]>=0)k|=uint64_t(m[v])<<(4*v);return k;}
void pairShort(unsigned mask,Edges cur,int family){if(!mask){pats[family].push_back(cur);return;}int a=__builtin_ctz(mask);for(int b=a+1;b<16;++b)if((mask>>b&1)&&__builtin_popcount(unsigned(a^b))==1){auto n=cur;n.emplace_back(a,b);pairShort(mask&~(1u<<a)&~(1u<<b),n,family);}}
int main(int argc,char**argv){assert(argc==4);int us[3]={6,10,15};
 for(int f=0;f<3;++f){int u=us[f];vector<int> ns;for(int v=0;v<16;++v)if(v!=3&&__builtin_popcount(unsigned(v^u))==1)ns.push_back(v);for(int i=0;i<(int)ns.size();++i)for(int j=i+1;j<(int)ns.size();++j)pairShort((65535u&~(1u<<3))&~(1u<<u)&~(1u<<ns[i])&~(1u<<ns[j]),{{u,ns[i]},{u,ns[j]}},f);assert(pats[f].size()==116);}
 ifstream ni(argv[1]);int f;while(ni>>f){array<int,16> m;m.fill(-1);for(int j=0;j<6;++j){int a,b;ni>>a>>b;m[a]=b;m[b]=a;}bad[f].insert(enc(m));}
 unordered_set<uint64_t> seenA,seenB;string line;
 ifstream ai(argv[2]);while(getline(ai,line)){istringstream in(line);int signature,p,q;in>>signature>>p>>q;Edges fa;array<int,16> mate;mate.fill(-1);int a,b;while(in>>a>>b){assert(a!=3&&a!=6&&a!=10&&a!=15&&b!=3&&b!=6&&b!=10&&b!=15&&mate[a]<0&&mate[b]<0);mate[a]=b;mate[b]=a;fa.emplace_back(a,b);}assert(fa.size()==5&&p>=0&&q<16&&p<q&&p!=3&&p!=6&&p!=10&&p!=15&&q!=3&&q!=6&&q!=10&&q!=15&&mate[p]<0&&mate[q]<0);assert(seenA.insert(enc(mate)).second);
  int computed=0;
  for(int family=0;family<3;++family){int s=-1,t=-1;for(int v:us)if(v!=us[family]){if(s<0)s=v;else t=v;}
   for(auto& n:pats[family]){DSU g;for(auto [x,y]:fa)g.add(x,y);for(auto [x,y]:n)g.add(x,y);if(!g.ok)continue;int r=g.root(p)==g.root(q)?0:g.root(p)==g.root(s)?1:2;assert(g.root(p)==g.root(r==0?q:r==1?s:t));computed|=1<<(3*family+r);}
  }
  assert(computed==signature);++at[signature];
 }
 assert(seenA.size()==62370);
 ifstream bi(argv[3]);while(getline(bi,line)){istringstream in(line);int signature,p,q;in>>signature>>p>>q;Edges fb;array<int,16> mate;mate.fill(-1);int a,b;while(in>>a>>b){assert(a>=2&&b>=2&&mate[a]<0&&mate[b]<0);mate[a]=b;mate[b]=a;fb.emplace_back(a,b);}assert(fb.size()==6&&p>=2&&q<16&&p<q&&mate[p]<0&&mate[q]<0);assert(seenB.insert(enc(mate)).second);
  int computed=0;
  for(int family=0;family<3;++family){int s=-1,t=-1;for(int v:us)if(v!=us[family]){if(s<0)s=v;else t=v;}
   for(int r=0;r<3;++r){DSU g;for(auto [x,y]:fb)g.add(x,y);g.add(s,16+s);g.add(t,16+t);if(r==0){g.add(p,q);g.add(16+s,16+t);}else if(r==1){g.add(p,16+s);g.add(q,16+t);}else{g.add(p,16+t);g.add(q,16+s);}if(!g.ok)continue;
    array<int,16> lm;lm.fill(-1);for(int x=2;x<16;++x)if(x!=s&&x!=t){assert(g.degree[x]==1);int partner=-1;for(int y=2;y<16;++y)if(y!=s&&y!=t&&y!=x&&g.root(x)==g.root(y)){assert(partner<0);partner=y;}assert(partner>=0);lm[x]=partner;}
    if(!bad[family].count(enc(lm)))computed|=1<<(3*family+r);
   }
  }
  assert(signature==computed);++bt[signature];
 }
 assert(seenB.size()==945945);
 long long failures=0;for(int a=0;a<512;++a)if(at[a])for(int b=0;b<512;++b)if(bt[b]){int sw=0;for(int k=0;k<3;++k){int m=(b>>(3*k))&7;sw|=((m&1)|((m&2)<<1)|((m&4)>>1))<<(3*k);}for(int orient=0;orient<2;++orient)if(!(a&(orient?sw:b))){assert(b==0);failures+=at[a]*bt[b];}}
 assert(bt[0]==786&&failures==98045640);
 cout<<"{\"status\":\"PASS\",\"method\":\"independent DSU component verification\",\"A_inputs\":62370,\"B_inputs\":945945,\"exceptional_B_inputs\":786,\"residual_full_inputs\":"<<failures<<"}\n";
}
