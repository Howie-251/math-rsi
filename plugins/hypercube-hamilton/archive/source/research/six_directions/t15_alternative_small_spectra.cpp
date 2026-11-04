#include <array>
#include <vector>
#include <set>
#include <map>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdint>
using namespace std;
using E=vector<pair<int,int>>;
array<int,16> fa,fb; E cur;vector<E> pat[2];int zs[2],c,y,mode,x;map<int,long long>Atypes,Btypes;map<int,array<int,16>>Awit;vector<int> ports;long long totalA,totalB,failpairs,badB;ofstream failures;set<uint64_t> neg[2];
void genN(unsigned mask,int f){if(!mask){pat[f].push_back(cur);return;}int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);for(int j=0;j<4;j++){int b=a^(1<<j);if(rest>>b&1){cur.emplace_back(a,b);genN(rest&~(1u<<b),f);cur.pop_back();}}}
void assessA(){ports.clear();for(int a=0;a<16;a++)if(a!=x&&a!=zs[0]&&a!=zs[1]&&fa[a]<0)ports.push_back(a);int mask=0;
 for(int f=0;f<2;f++){int z=zs[f];for(auto& h:pat[f]){int adj[16][2],deg[16]{};bool ok=1;for(int a=0;a<16;a++)if(fa[a]>a){int b=fa[a];adj[a][deg[a]++]=b;adj[b][deg[b]++]=a;}for(auto[a,b]:h){if(fa[a]==b){ok=0;break;}adj[a][deg[a]++]=b;adj[b][deg[b]++]=a;}if(!ok)continue;
 unsigned seen=0;int target=-1;vector<int> ends=ports;ends.push_back(z);for(int ai=0;ai<=c;ai++){int a=ends[ai];if(seen>>a&1)continue;int prev=-1,v=a;while(1){if(seen>>v&1){ok=0;break;}seen|=1u<<v;int next=-1;for(int j=0;j<deg[v];j++)if(adj[v][j]!=prev)next=adj[v][j];if(next<0)break;prev=v;v=next;}if(!ok||v==a||find(ends.begin(),ends.end(),v)==ends.end()){ok=0;break;}if(ai==0)target=find(ends.begin(),ends.end(),v)-ends.begin();}if(ok&&seen==(65535u&~(1u<<x))){int idx=c==1?0:target-1;mask|=1<<(f*((c+1)/2==1?1:3)+idx);}}
 }Atypes[mask]++;Awit.try_emplace(mask,fa);totalA++;
}
int pattern(int idx,int i){if(c==1)return 1-i;static int p[3][4]={{1,0,3,2},{2,3,0,1},{3,2,1,0}};return p[idx][i];}
uint64_t key(array<int,16>&m){uint64_t k=0;for(int a=0;a<16;a++)if(m[a]>=0)k|=uint64_t(m[a])<<(4*a);return k;}
int Bmask(vector<int>& bp){int mask=0;for(int f=0;f<2;f++)for(int p=0;p<(c==1?1:3);p++){int z=zs[f];array<int,16> mate=fb;int za=-1,zb=-1;bool ok=1;
 for(int a=0;a<=c;a++){int b=pattern(p,a);if(a>b)continue;int u=a==c?z:bp[a],v=b==c?z:bp[b];if(u==v){ok=0;break;}if(u==z||v==z){int w=u==z?v:u;if(za<0)za=w;else if(zb<0)zb=w;else{ok=0;break;}}else{if(mate[u]>=0||mate[v]>=0){ok=0;break;}mate[u]=v;mate[v]=u;}}
 if(!ok)continue;if(fb[z]>=0){if(zb>=0||za<0)continue;zb=fb[z];mate[zb]=-1;mate[z]=-1;}else mate[z]=-1;
 if(za<0||zb<0||za==zb||mate[za]>=0||mate[zb]>=0)continue;mate[za]=zb;mate[zb]=za;
 if(!neg[f].count(key(mate)))mask|=1<<(f*(c==1?1:3)+p);
 }return mask;}
void assessB(){vector<int>bp;for(int a=0;a<16;a++)if(a!=0&&a!=7&&a!=y&&fb[a]<0)bp.push_back(a);do{int m=Bmask(bp);Btypes[m]++;bool any=0;for(auto[t,n]:Atypes)if(!(t&m)){failpairs+=n;any=1;failures<<"A "<<t<<" B "<<m<<" ports";for(int a:bp)failures<<" "<<a;failures<<" F";for(int a=0;a<16;a++)if(fb[a]>a)failures<<" "<<a<<" "<<fb[a];failures<<"\n";}badB+=any;totalB++;}while(next_permutation(bp.begin(),bp.end()));}
void gen(unsigned mask,int skips){if(!mask){if(skips==0){if(mode==0)assessA();else assessB();}return;}if(__builtin_popcount(mask)<skips)return;int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);if(skips)gen(rest,skips-1);auto&m=mode==0?fa:fb;for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);m[a]=b;m[b]=a;gen(rest&~(1u<<b),skips);m[a]=m[b]=-1;}}
int main(int argc,char**argv){if(argc!=4)return 2;int core=stoi(argv[1]);x=0;zs[0]=3;zs[1]=5;y=1;switch(core){case 0:break;case 5:zs[1]=6;break;case 8:zs[1]=15;break;case 15:zs[0]=10;zs[1]=15;break;case 23:x=9;y=8;break;case 26:x=9;zs[1]=15;y=8;break;case 27:x=9;zs[0]=6;zs[1]=15;y=8;break;case 18:x=3;zs[0]=6;zs[1]=12;y=1;break;case 21:x=3;zs[0]=10;zs[1]=12;y=1;break;case 25:x=9;zs[0]=3;zs[1]=6;y=8;break;default:return 3;}c=stoi(argv[2]);string prefix=argv[3];failures.open(prefix+"_failures.txt");ifstream in("t15_r3_small_negative_inputs.txt");int r,yy;while(in>>r>>yy){array<int,16>m;for(int&a:m)in>>a;for(int f=0;f<2;f++)if(r==zs[f]&&yy==y)neg[f].insert(key(m));}
 for(int f=0;f<2;f++){int u=zs[1-f];vector<int>ns;for(int j=0;j<4;j++)if((u^(1<<j))!=x)ns.push_back(u^(1<<j));for(int i=0;i<(int)ns.size();i++)for(int j=i+1;j<(int)ns.size();j++){cur={{u,ns[i]},{u,ns[j]}};genN((65535u&~(1u<<x))&~(1u<<u)&~(1u<<ns[i])&~(1u<<ns[j]),f);}}
 fa.fill(-1);fb.fill(-1);mode=0;gen((65535u&~(1u<<x))&~(1u<<zs[0])&~(1u<<zs[1]),c);cerr<<"A done "<<Atypes.size()<<" types\n";ofstream aw(prefix+"_A.txt");for(auto[m,n]:Atypes){aw<<m<<" "<<n;for(int a:Awit[m])aw<<" "<<a;aw<<"\n";}mode=1;gen(65535u&~1u&~(1u<<7)&~(1u<<y),c);
 cout<<"{\"core\":"<<core<<",\"A_holes\":["<<x<<","<<zs[0]<<","<<zs[1]<<"],\"B_holes\":[0,7,"<<y<<"],\"c\":"<<c<<",\"negative_counts\":["<<neg[0].size()<<","<<neg[1].size()<<"],\"A_count\":"<<totalA<<",\"B_bijection_count\":"<<totalB<<",\"A_types\":{";bool sep=0;for(auto[m,n]:Atypes){if(sep)cout<<",";sep=1;cout<<"\""<<m<<"\":"<<n;}cout<<"},\"B_types\":{";sep=0;for(auto[m,n]:Btypes){if(sep)cout<<",";sep=1;cout<<"\""<<m<<"\":"<<n;}cout<<"},\"bad_B_bijections\":"<<badB<<",\"failed_A_B_pairs\":"<<failpairs<<"}\n";
}
