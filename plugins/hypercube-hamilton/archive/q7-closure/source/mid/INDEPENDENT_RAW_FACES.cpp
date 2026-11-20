#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using Mask=uint64_t;
struct Face{Mask u,y; array<int,6> d;};
vector<int>E,O;
array<uint32_t,32> neighbors;
vector<Face> faces;
long long nodes=0,minorities=0;
void take_odd(int start,int need,uint32_t pool,Mask um,Mask ym){
 if(!need){Face f{um,ym,{}};for(int j=0;j<6;++j){for(int v:E)if((um>>v&1)&&!(v>>j&1))++f.d[j];for(int v:O)if((ym>>v&1)&&!(v>>j&1))--f.d[j];}faces.push_back(f);return;}
 for(int i=start;i<=32-need;++i)if(pool>>i&1){uint32_t tail=pool&(~uint32_t(0)<<i);if(__builtin_popcount(tail)<need)break;take_odd(i+1,need-1,pool,um,ym|(Mask(1)<<O[i]));}
}
void take_even(int start,int need,uint32_t pool,Mask um,int s){
 ++nodes;if(__builtin_popcount(pool)<s)return;
 if(!need){++minorities;take_odd(0,s,pool,um,0);return;}
 for(int i=start;i<=32-need;++i)take_even(i+1,need-1,pool&~neighbors[i],um|(Mask(1)<<E[i]),s);
}
int main(int argc,char**argv){assert(argc==3);string prefix=argv[1];int r=stoi(argv[2]);for(int v=0;v<64;++v)(__builtin_parity((unsigned)v)?O:E).push_back(v);for(int i=0;i<32;++i)for(int h=0;h<32;++h)if(__builtin_popcount((unsigned)(E[i]^O[h]))==1)neighbors[i]|=uint32_t(1)<<h;
 take_even(0,r,~uint32_t(0),0,19-r);sort(faces.begin(),faces.end(),[](auto a,auto b){return a.u!=b.u?a.u<b.u:a.y<b.y;});
 ofstream bin(prefix+"_RAW.bin",ios::binary);for(auto f:faces){bin.write((char*)&f.u,8);bin.write((char*)&f.y,8);}bin.close();
 cerr<<"r="<<r<<" raw="<<faces.size()<<" minorities="<<minorities<<" nodes="<<nodes<<endl;
 uint64_t pairs=0,bad=0;int minmax=99;array<uint64_t,33>hist{};ofstream witness(prefix+"_BAD.jsonl");
 for(size_t a=0;a<faces.size();++a)for(size_t b=a;b<faces.size();++b){auto&x=faces[a];auto&y=faces[b];if((x.u&y.u)||(x.y&y.y))continue;uint64_t weight=a==b?1:2;pairs+=weight;int mm=abs(2*r-19);for(int j=0;j<6;++j)mm=max(mm,abs(x.d[j]-y.d[j]));hist[mm]+=weight;minmax=min(minmax,mm);if(mm<=7){bad+=weight;witness<<"{\"a\":"<<a<<",\"b\":"<<b<<",\"weight\":"<<weight<<",\"max\":"<<mm<<"}\n";}}
 ofstream js(prefix+"_RESULT.json");js<<"{\"r\":"<<r<<",\"s\":"<<19-r<<",\"raw_faces\":"<<faces.size()<<",\"minorities\":"<<minorities<<",\"nodes\":"<<nodes<<",\"ordered_independent_pairs\":"<<pairs<<",\"min_max_abs_delta\":"<<minmax<<",\"bad\":"<<bad<<",\"histogram\":{";bool comma=false;for(int i=0;i<33;++i)if(hist[i]){if(comma)js<<',';comma=true;js<<'\"'<<i<<"\":"<<hist[i];}js<<"}}\n";
 cout<<"PASS r="<<r<<" pairs="<<pairs<<" minmax="<<minmax<<" bad="<<bad<<endl;return bad?1:0;
}
