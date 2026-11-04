// Independent graph-path reconstruction of B spectra; reads audited raw tables directly.
#include <array>
#include <vector>
#include <set>
#include <map>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdint>
using namespace std;
using M=array<int,16>;map<pair<int,int>,set<uint64_t>>neg;M mate;int c,y,rs[2],core;map<int,long long>hist;long long total;ofstream ex;
uint64_t encode(M&m){uint64_t k=0;for(int a=0;a<16;a++)if(m[a]>=0)k|=uint64_t(m[a])<<(4*a);return k;}
int tr(int a,array<int,4>&p){int v=0;for(int j=0;j<4;j++)v|=((a>>j)&1)<<p[j];return v;}
void load(){int files=0;for(auto&ent:filesystem::directory_iterator(".")){string fn=ent.path().filename().string();if(fn.rfind("q4_balanced_two_avoided_",0)!=0||ent.path().extension()!=".bin")continue;int r,yy;if(sscanf(fn.c_str(),"q4_balanced_two_avoided_%d_%d.bin",&r,&yy)!=2)abort();ifstream in(ent.path(),ios::binary);vector<unsigned char>b((istreambuf_iterator<char>(in)),{});if(b.size()!=10395*30)abort();files++;array<int,4>p={0,1,2,3};do{auto&table=neg[{tr(r,p),tr(yy,p)}];for(int i=0;i<(int)b.size();i+=30)if(b[i+16]==255){M m;m.fill(-1);for(int a=0;a<16;a++)if(b[i+a]!=255)m[tr(a,p)]=tr(b[i+a],p);table.insert(encode(m));}}while(next_permutation(p.begin(),p.begin()+3));}if(files!=13||neg.size()!=49)abort();}
int getmask(vector<int>&bp){int result=0;int patterns[3][4]={{1,0,3,2},{2,3,0,1},{3,2,1,0}};for(int f=0;f<2;f++)for(int p=0;p<(c==1?1:3);p++){
 vector<int>g[16];auto add=[&](int a,int b){g[a].push_back(b);g[b].push_back(a);};for(int a=0;a<16;a++)if(mate[a]>a)add(a,mate[a]);
 vector<int>v=bp;v.push_back(rs[f]);for(int a=0;a<=c;a++){int b=c==1?1-a:patterns[p][a];if(a<b)add(v[a],v[b]);}
 bool ok=1;for(int a=0;a<16;a++)if(a!=0&&a!=7&&a!=y)if(g[a].size()!=size_t(a==rs[f]?2:1))ok=0;if(!ok)continue;
 unsigned seen=0;M compressed;compressed.fill(-1);for(int a=0;a<16;a++)if(g[a].size()==1&&!(seen>>a&1)){int prev=-1,k=a;while(1){if(seen>>k&1){ok=0;break;}seen|=1u<<k;int next=-1;for(int b:g[k])if(b!=prev)next=b;if(next<0)break;prev=k;k=next;}if(!ok||k==a){ok=0;break;}compressed[a]=k;compressed[k]=a;}
 if(seen!=(65535u^1u^(1u<<7)^(1u<<y)))ok=0;if(ok&&!neg[{rs[f],y}].count(encode(compressed)))result|=1<<(f*(c==1?1:3)+p);
 }return result;}
void assess(){vector<int>bp;for(int a=0;a<16;a++)if(a!=0&&a!=7&&a!=y&&mate[a]<0)bp.push_back(a);bool zero=0;do{int m=getmask(bp);hist[m]++;total++;if(!m)zero=1;}while(next_permutation(bp.begin(),bp.end()));if(zero){ex<<"ports";for(int a:bp)ex<<" "<<a;ex<<" F";for(int a=0;a<16;a++)if(mate[a]>a)ex<<" "<<a<<" "<<mate[a];ex<<"\n";}}
void gen(unsigned mask,int skip){if(!mask){if(!skip)assess();return;}if(__builtin_popcount(mask)<skip)return;int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);if(skip)gen(rest,skip-1);for(unsigned b=rest;b;b&=b-1){int z=__builtin_ctz(b);mate[a]=z;mate[z]=a;gen(rest&~(1u<<z),skip);mate[a]=mate[z]=-1;}}
int main(){load();cout<<"[";bool comma=0;for(int k:{18,21,25})for(int cc:{1,3}){core=k;c=cc;y=k<23?1:8;rs[0]=k==15?10:k==27?6:3;rs[1]=k==5?6:(k==0||k==23)?5:15;if(k==18){rs[0]=6;rs[1]=12;y=1;}if(k==21){rs[0]=10;rs[1]=12;y=1;}if(k==25){rs[0]=3;rs[1]=6;y=8;}mate.fill(-1);hist.clear();total=0;ex.open("t15_alternative_core"+to_string(k)+"_c"+to_string(c)+"_B_exceptions.txt");gen(65535u^1u^(1u<<7)^(1u<<y),c);ex.close();if(total!=(c==1?135135:1621620))abort();if(comma)cout<<",";comma=1;cout<<"{\"core\":"<<k<<",\"c\":"<<c<<",\"total\":"<<total<<",\"B_types\":{";bool sep=0;for(auto[m,n]:hist){if(sep)cout<<",";sep=1;cout<<"\""<<m<<"\":"<<n;}cout<<"}}"<<flush;}cout<<"]\n";}
