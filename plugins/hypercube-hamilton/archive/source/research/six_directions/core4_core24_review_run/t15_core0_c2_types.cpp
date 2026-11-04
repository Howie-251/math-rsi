#include <array>
#include <vector>
#include <set>
#include <unordered_set>
#include <fstream>
#include <iostream>
#include <cstdint>
using namespace std;
using Edges=vector<pair<int,int>>;
array<vector<Edges>,3> patterns;
array<unordered_set<uint64_t>,3> neg;
array<int,16> fa,fb;
long long at[512]={},bt[512]={};
ofstream afile,bfile;
Edges cur;
int ap,aq,bp,bq;
uint64_t encode(const array<int,16>& m){uint64_t c=0;for(int i=1;i<16;++i)if(m[i]>=0)c|=uint64_t(m[i])<<(4*i);return c;}
void genN(unsigned mask,int f){
 if(!mask){patterns[f].push_back(cur);return;}
 int a=__builtin_ctz(mask);unsigned r=mask&~(1u<<a);
 for(int j=0;j<4;++j){int b=a^(1<<j);if(r>>b&1u){cur.emplace_back(a,b);genN(r&~(1u<<b),f);cur.pop_back();}}
}
struct Graph{
 int adj[40][2]{},deg[40]{};unsigned long long seen=0;
 bool valid=true;
 void add(int a,int b){if(a==b||deg[a]>=2||deg[b]>=2){valid=false;return;}for(int i=0;i<deg[a];++i)if(adj[a][i]==b){valid=false;return;}adj[a][deg[a]++]=b;adj[b][deg[b]++]=a;}
 int walk(int a){int prev=-1,v=a;while(true){if(seen>>v&1ull){valid=false;return -1;}seen|=1ull<<v;int next=-1;for(int i=0;i<deg[v];++i)if(adj[v][i]!=prev)next=adj[v][i];if(next<0)return v;prev=v;v=next;}}
};
void assessA(){
 int signature=0,us[3]={3,5,6};
 for(int f=0;f<3;++f){int s=-1,t=-1;for(int v:us)if(v!=us[f]){if(s<0)s=v;else t=v;}
  for(auto& n:patterns[f]){Graph g;for(int a=1;a<16;++a)if(fa[a]>a)g.add(a,fa[a]);for(auto [a,b]:n)g.add(a,b);if(!g.valid)continue;
   array<int,16> mate;mate.fill(-1);
   for(int a:{ap,aq,s,t})if(!(g.seen>>a&1ull)){int b=g.walk(a);if(b<0)break;mate[a]=b;mate[b]=a;}
   if(!g.valid||g.seen!=65534ull)continue;
   int r=mate[ap]==aq?0:mate[ap]==s?1:2;
   signature|=1<<(3*f+r);
  }
 }
 ++at[signature];afile<<signature<<' '<<ap<<' '<<aq;for(int a=1;a<16;++a)if(fa[a]>a)afile<<' '<<a<<' '<<fa[a];afile<<'\n';
}
void genA(unsigned mask){if(!mask){assessA();return;}int a=__builtin_ctz(mask);unsigned r=mask&~(1u<<a);for(unsigned bits=r;bits;bits&=bits-1){int b=__builtin_ctz(bits);fa[a]=b;fa[b]=a;genA(r&~(1u<<b));fa[a]=fa[b]=-1;}}
void assessB(){
 int signature=0,us[3]={3,5,6};
 for(int f=0;f<3;++f){int s=-1,t=-1;for(int v:us)if(v!=us[f]){if(s<0)s=v;else t=v;}
  for(int r=0;r<3;++r){Graph g;for(int a=1;a<16;++a)if(fb[a]>a)g.add(a,fb[a]);g.add(s,16+s);g.add(t,16+t);
   if(r==0){g.add(bp,bq);g.add(16+s,16+t);}else if(r==1){g.add(bp,16+s);g.add(bq,16+t);}else{g.add(bp,16+t);g.add(bq,16+s);}
   if(!g.valid)continue;
   array<int,16> lm;lm.fill(-1);
   for(int a=2;a<16;++a)if(a!=s&&a!=t&&!(g.seen>>a&1ull)){int b=g.walk(a);if(b<0||b>=16||b==s||b==t){g.valid=false;break;}lm[a]=b;lm[b]=a;}
   unsigned long long expected=(65532ull&~(1ull<<s)&~(1ull<<t))|(1ull<<s)|(1ull<<t)|(1ull<<(16+s))|(1ull<<(16+t));
   if(g.valid&&g.seen==expected&&!neg[f].count(encode(lm)))signature|=1<<(3*f+r);
  }
 }
 ++bt[signature];bfile<<signature<<' '<<bp<<' '<<bq;for(int a=2;a<16;++a)if(fb[a]>a)bfile<<' '<<a<<' '<<fb[a];bfile<<'\n';
}
void genB(unsigned mask){if(!mask){assessB();return;}int a=__builtin_ctz(mask);unsigned r=mask&~(1u<<a);for(unsigned bits=r;bits;bits&=bits-1){int b=__builtin_ctz(bits);fb[a]=b;fb[b]=a;genB(r&~(1u<<b));fb[a]=fb[b]=-1;}}
int main(int argc,char**argv){if(argc!=4)return 2;
 ifstream in(argv[1]);int f;while(in>>f){array<int,16> m;m.fill(-1);for(int i=0;i<6;++i){int a,b;in>>a>>b;m[a]=b;m[b]=a;}neg[f].insert(encode(m));}
 int us[3]={3,5,6};for(int f=0;f<3;++f){int u=us[f];for(int i=0;i<4;++i)for(int j=i+1;j<4;++j){int a=u^(1<<i),b=u^(1<<j);cur={{u,a},{u,b}};genN(65534u&~(1u<<u)&~(1u<<a)&~(1u<<b),f);}}
 afile.open(argv[2]);bfile.open(argv[3]);fa.fill(-1);fb.fill(-1);
 for(ap=1;ap<16;++ap)if(ap!=3&&ap!=5&&ap!=6)for(aq=ap+1;aq<16;++aq)if(aq!=3&&aq!=5&&aq!=6)genA(65534u&~(1u<<3)&~(1u<<5)&~(1u<<6)&~(1u<<ap)&~(1u<<aq));
 for(bp=2;bp<16;++bp)for(bq=bp+1;bq<16;++bq)genB(65532u&~(1u<<bp)&~(1u<<bq));
 cout<<"{\"A_types\":{";bool sep=false;for(int i=0;i<512;++i)if(at[i]){if(sep)cout<<",";sep=true;cout<<'\"'<<i<<"\":"<<at[i];}cout<<"},\"B_types\":{";sep=false;for(int i=0;i<512;++i)if(bt[i]){if(sep)cout<<",";sep=true;cout<<'\"'<<i<<"\":"<<bt[i];}cout<<"},\"failing_type_pairs\":[";sep=false;
 for(int a=0;a<512;++a)if(at[a])for(int b=0;b<512;++b)if(bt[b]){int sw=0;for(int k=0;k<3;++k){int m=b>>(3*k)&7;sw|=((m&1)|((m&2)<<1)|((m&4)>>1))<<(3*k);}for(int orient=0;orient<2;++orient)if(!(a&(orient?sw:b))){if(sep)cout<<",";sep=true;cout<<"["<<a<<","<<b<<","<<orient<<","<<at[a]*bt[b]<<"]";}}
 cout<<"]}\n";
}
