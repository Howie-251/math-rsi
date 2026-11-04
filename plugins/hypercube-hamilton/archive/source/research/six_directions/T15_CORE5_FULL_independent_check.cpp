// Fresh review implementation: DSU B compression, direct positive certificates.
// Does not import producer/checker source or prepared negative lists.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
using namespace std;
using Pair=pair<int,int>; using Matching=vector<Pair>;
Pair edge(int a,int b){if(a>b)swap(a,b);return {a,b};}
Matching norm(Matching m){sort(m.begin(),m.end());return m;}
set<Matching> neg[2];
vector<int> covered;
Matching fb;
map<int,uint64_t> hist[2];
set<Matching> exceptions; // first pair {-1,port} tags boundary
int patterns[3][4]={{1,0,3,2},{2,3,0,1},{3,2,1,0}};
void need(bool b){if(!b){cerr<<"CHECK FAILED\n";exit(2);}}
int trans(int v){int p[4]={1,2,0,3},w=0;for(int j=0;j<4;j++)w|=((v>>j)&1)<<p[j];return w;}
void tables(){
 for(int t=0;t<2;t++){
  string name=t?"q4_balanced_two_avoided_3_4.bin":"q4_balanced_two_avoided_3_1.bin";
  ifstream f(name,ios::binary); vector<unsigned char> raw((istreambuf_iterator<char>(f)),{});
  need(raw.size()==10395*30);
  for(int i=0;i<(int)raw.size();i+=30)if(raw[i+16]==255){
   for(int j=16;j<30;j++)need(raw[i+j]==255);
   Matching m;
   for(int a=0;a<16;a++)if(raw[i+a]<16 && a<raw[i+a])m.push_back(t?edge(trans(a),trans(raw[i+a])):edge(a,raw[i+a]));
   need(m.size()==6);neg[t].insert(norm(m));
  }
 }
 need(neg[0].size()==3 && neg[1].size()==2);
}
bool admissible(const vector<int>&ports,int bridge,int pat){
 int z=bridge?6:3,dsu[16],deg[16]{};
 for(int a=0;a<16;a++)dsu[a]=a;
 function<int(int)> root=[&](int a){return dsu[a]==a?a:dsu[a]=root(dsu[a]);};
 auto add=[&](int a,int b){deg[a]++;deg[b]++;dsu[root(a)]=root(b);};
 for(auto e:fb)add(e.first,e.second);
 vector<int> ends=ports;ends.push_back(z);int n=ends.size();
 for(int a=0;a<n;a++){int b=n==2?1-a:patterns[pat][a];if(a<b)add(ends[a],ends[b]);}
 map<int,vector<int>> endpoint;
 for(int a=0;a<16;a++) {
  bool active=(a!=0&&a!=1&&a!=7);
  need(deg[a]==(active?(a==z?2:1):0));
  if(active){auto &v=endpoint[root(a)];if(a!=z)v.push_back(a);}
 }
 Matching l;
 for(auto &kv:endpoint){if(kv.second.size()!=2)return false;l.push_back(edge(kv.second[0],kv.second[1]));}
 need(l.size()==6);return !neg[bridge].count(norm(l));
}
void matchAll(vector<int> remaining,const function<void()>&visit){
 if(remaining.empty()){visit();return;}
 int a=remaining[0];
 for(int j=1;j<(int)remaining.size();j++){
  vector<int>r;for(int k=1;k<(int)remaining.size();k++)if(k!=j)r.push_back(remaining[k]);
  fb.push_back(edge(a,remaining[j]));matchAll(r,visit);fb.pop_back();
 }
}
void spectra(int c){
 vector<int>ports;uint64_t partial=0;
 function<void(int)>choose=[&](int pos){
  if((int)ports.size()==c){
   vector<int>rem;for(int v:covered)if(find(ports.begin(),ports.end(),v)==ports.end())rem.push_back(v);
   matchAll(rem,[&](){
    partial++;vector<int>p=ports;
    do{int mask=0;
     for(int b=0;b<2;b++)for(int j=0;j<(c==1?1:3);j++)if(admissible(p,b,j))mask|=1<<(b*(c==1?1:3)+j);
     hist[c==3][mask]++;
     if(c==3)need(__builtin_popcount((unsigned)(mask&7))>=2 || __builtin_popcount((unsigned)(mask>>3))>=2);
     if(!mask){need(c==1);Matching ex=fb;ex.push_back({-1,p[0]});exceptions.insert(norm(ex));}
    }while(next_permutation(p.begin(),p.end()));
   });return;
  }
  for(int j=pos;j<(int)covered.size();j++){ports.push_back(covered[j]);choose(j+1);ports.pop_back();}
 };
 choose(0);need(partial==(c==1?135135:270270));
}
vector<Matching> inputs;
vector<int> inputPorts;
void certificate(){
 ifstream in("t15_core5_c1_B_inputs.txt");int p;
 set<Matching>expected;
 while(in>>p){Matching e;for(int j=0;j<6;j++){int a,b;need(bool(in>>a>>b));e.push_back({a,b});}
  inputPorts.push_back(p);inputs.push_back(e);e.push_back({-1,p});expected.insert(norm(e));}
 need(expected==exceptions && expected.size()==5 && inputs.size()==5);
 ifstream cert("t15_core5_c1_residual.bin",ios::binary);need(bool(cert));uint64_t count=0;
 vector<int>A;for(int a=0;a<16;a++)if(a!=0&&a!=3&&a!=6)A.push_back(a);
 fb.clear();
 for(int port:A){vector<int>rem;for(int a:A)if(a!=port)rem.push_back(a);
  matchAll(rem,[&](){for(int k=0;k<5;k++){
   Matching req;for(auto e:fb)req.push_back({2*e.first+1,2*e.second+1});
   for(auto e:inputs[k])req.push_back({2*e.first,2*e.second});
   req.push_back({2*port+1,2*inputPorts[k]});need(req.size()==13);
   unsigned char b[56];cert.read((char*)b,56);need(cert.gcount()==56);
   set<Pair>edges;
   for(int j=0;j<13;j++)need(b[2*j]==req[j].first && b[2*j+1]==req[j].second);
   uint32_t seen=0;
   for(int j=0;j<30;j++){unsigned a=b[26+j],v=b[26+(j+1)%30];need(a<32&&v<32&&!(seen&(1u<<a)));seen|=1u<<a;edges.insert(edge(a,v));}
   need(seen==(0xffffffffu ^ (1u<<1) ^ (1u<<2)));
   for(auto e:req)need(edges.erase(edge(e.first,e.second))==1);
   need(edges.size()==17);for(auto e:edges)need(__builtin_popcount((unsigned)(e.first^e.second))==1);
   count++;
  }});
 }
 char trailing;need(!cert.get(trailing));need(count==675675);
}
void inverse(){
 set<Matching>parts;for(auto l:neg[1])for(int i=0;i<6;i++)for(int j=i+1;j<6;j++){
  Matching f;for(int k=0;k<6;k++)if(k!=i&&k!=j)f.push_back(l[k]);parts.insert(f);
 }
 need(parts.size()==30);
 for(auto f:parts){set<int>ends;for(int a:covered)if(a!=6)ends.insert(a);
  for(auto e:f){need(ends.erase(e.first)==1);need(ends.erase(e.second)==1);}
  need(ends.size()==4);vector<int>v(ends.begin(),ends.end());int bad=0;
  for(int pat=0;pat<3;pat++){Matching l=f;for(int a=0;a<4;a++)if(a<patterns[pat][a])l.push_back(edge(v[a],v[patterns[pat][a]]));bad+=neg[1].count(norm(l));}
  need(bad==1);
 }
}
int main(){
 for(int a=0;a<16;a++)if(a!=0&&a!=1&&a!=7)covered.push_back(a);
 tables();inverse();spectra(1);spectra(3);certificate();
 cout<<"{\"status\":\"PASS\",\"c1_B_total\":135135,\"c1_B_exceptions\":"<<exceptions.size()<<",\"c1_positive_certificates\":675675,\"c3_B_partial\":270270,\"c3_B_bijections\":1621620,\"c3_every_input_has_bridge_with_at_least_two_good_pairings\":true,\"c5_inverse_inputs\":30,\"c5_each_inverse_has_exactly_one_bad_Q\":true,\"histograms\":[";
 for(int c=0;c<2;c++){if(c)cout<<",";cout<<"{";bool sep=0;for(auto kv:hist[c]){if(sep)cout<<",";sep=1;cout<<"\""<<kv.first<<"\":"<<kv.second;}cout<<"}";}
 cout<<"]}\n";
}

