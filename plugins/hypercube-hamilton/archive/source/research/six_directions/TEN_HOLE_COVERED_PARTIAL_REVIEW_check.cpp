// Independent exhaustive audit: choose odd holes first; no producer includes.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;using U=uint64_t;
int parity(int x){return __builtin_popcount((unsigned)x)&1;}
set<U> accepted;
int proj(int x,int cut){int q=0,j=0;for(int d=0;d<6;d++)if(d!=cut){q|=((x>>d)&1)<<j;j++;}return q;}
U marked(vector<int> omit,vector<int> inc,int m,int cut){
 U a=0,b=0;for(int x:omit){int q=proj(x^m,cut);assert(parity(q));a|=U(1)<<q;}
 for(int x:inc){int q=proj(x^m,cut);assert(parity(q));b|=U(1)<<q;}
 assert(__builtin_popcountll(a)==2&&__builtin_popcountll(b)==3&&!(a&b));return a|(b<<32);
}
bool oldrow(int a,int b){static const pair<int,int> rows[]={{1,2},{2,3},{2,2},{3,3},{1,3},{2,4},{4,3},{2,5}};for(auto p:rows)if(p==make_pair(a,b))return true;return false;}
struct Sides{vector<int>za,zb,wa,wb;};
Sides sides(const array<int,4>&z,const array<int,5>&w,int v,int d){
 Sides s;for(int x:z)(((x>>d)&1)==((v>>d)&1)?s.za:s.zb).push_back(x);
 for(int x:w)(((x>>d)&1)==((v>>d)&1)?s.wa:s.wb).push_back(x);return s;
}
bool t15(const array<int,4>&z,const array<int,5>&w,int v){
 for(int cut=0;cut<6;cut++){
  auto s=sides(z,w,v,cut);vector<int> source,inc;int m=-1;
  if(s.za.size()==3&&s.wa.size()==2){source=s.za;inc=s.wb;m=s.zb[0];}
  if(s.za.size()==1&&s.wa.size()==4){for(int x:s.wa)if(x!=(1<<cut))source.push_back(x);inc=s.zb;m=s.wb[0];}
  if(m<0)continue;
  for(size_t i=0;i<source.size();i++)for(size_t j=i+1;j<source.size();j++)
   if(accepted.count(marked({source[i]^(1<<cut),source[j]^(1<<cut)},inc,m,cut)))return true;
 }return false;
}
struct Pick{int rule=0,cut=-1,source=-1,local=-1,delta=-1;};
bool admissible(const vector<int>&L,const vector<int>&J,int y,int removed,Pick&pick){
 assert(L.size()==3&&J.size()==5&&count(J.begin(),J.end(),y)==1);
 for(int j=0;j<6;j++)if(j!=removed){
  int l=0,h=0;for(int x:L)l+=((x>>j)&1)==((y>>j)&1);for(int x:J)h+=((x>>j)&1)==((y>>j)&1);
  if((h-l>=1&&h-l<=3)||(h==5&&l==1)){pick.local=j;pick.delta=h-l;return true;}
 }return false;
}
Pick additional(const array<int,4>&z,const array<int,5>&w,int v){
 for(int d=0;d<6;d++){
  auto s=sides(z,w,v,d);int a=s.za.size(),b=s.wa.size();Pick p;p.cut=d;
  if(a==0&&b==1){p.rule=1;return p;}
  if(a==1&&b==1){auto J=s.wb;int x=s.za[0],y=x^(1<<d);J.push_back(y);if(admissible(s.zb,J,y,d,p)){p.rule=2;p.source=x;return p;}}
  if(a==0&&b==2)for(int x:s.wa)if(x!=(1<<d)){auto J=s.zb;int y=x^(1<<d);J.push_back(y);if(admissible(s.wb,J,y,d,p)){p.rule=3;p.source=x;return p;}}
  if(a==3&&b==4){auto J=s.wa;J.push_back(v);if(admissible(s.za,J,v,d,p)){p.rule=4;return p;}}
  if(a==4&&b==4)for(int x:s.za){auto L=s.za;L.erase(find(L.begin(),L.end(),x));auto J=s.wa;J.push_back(v);if(admissible(L,J,v,d,p)){p.rule=5;p.source=x;return p;}}
  if(a==3&&b==5)for(int x:s.wa)if(x!=(1<<d)){auto J=s.wa;J.erase(find(J.begin(),J.end(),x));J.push_back(v);if(admissible(s.za,J,v,d,p)){p.rule=6;p.source=x;return p;}}
 }return {};
}
int main(){
 ifstream lookup("TEN_HOLE_COVERED_PARTIAL_REVIEW_lookup.txt");assert(lookup);U key;while(lookup>>key)accepted.insert(key);assert(accepted.size()>1000);
 vector<int>E,O;for(int x=0;x<64;x++)if(parity(x))O.push_back(x);else if(x)E.push_back(x);
 ofstream result("TEN_HOLE_COVERED_PARTIAL_REVIEW_census.json"),witness("TEN_HOLE_COVERED_PARTIAL_REVIEW_witness.tsv");
 result<<"{\"targets\":[";bool first=true;
 for(int v:{1,7,31}){
  vector<int>odd;for(int x:O)if(x!=v)odd.push_back(x);
  U total=0,basic=0,oldT=0,left=0,postold=0;map<int,U>newrules;
  ofstream rem("TEN_HOLE_COVERED_PARTIAL_REVIEW_remaining_v"+to_string(v)+".bin",ios::binary);
  array<int,5>w;array<int,4>z;
  for(int a=0;a<27;a++)for(int b=a+1;b<28;b++)for(int c=b+1;c<29;c++)for(int d=c+1;d<30;d++)for(int e=d+1;e<31;e++){
   w={odd[a],odd[b],odd[c],odd[d],odd[e]};vector<int>allowed;
   for(int x:E){bool ok=true;for(int y:w)if(__builtin_popcount((unsigned)(x^y))==1){ok=false;break;}if(ok)allowed.push_back(x);}
   if(allowed.size()<4)continue;
   int ws[6]={};for(int j=0;j<6;j++)for(int x:w)ws[j]+=((x>>j)&1)==((v>>j)&1);
   int n=allowed.size();
   for(int i=0;i<n-3;i++)for(int j=i+1;j<n-2;j++)for(int k=j+1;k<n-1;k++)for(int l=k+1;l<n;l++){
    z={allowed[i],allowed[j],allowed[k],allowed[l]};total++;bool good=false;
    for(int cut=0;cut<6;cut++){
     int a=0;for(int x:z)a+=((x>>cut)&1)==((v>>cut)&1);
     if(oldrow(a,ws[cut])){good=true;break;}
    }
    if(good){basic++;continue;}
    if(t15(z,w,v)){oldT++;continue;}
    postold++;Pick p=additional(z,w,v);
    if(p.rule){newrules[p.rule]++;witness<<v;for(int x:z)witness<<'\t'<<x;for(int x:w)witness<<'\t'<<x;witness<<'\t'<<p.rule<<'\t'<<p.cut<<'\t'<<p.source<<'\t'<<p.local<<'\t'<<p.delta<<'\n';}
    else{left++;for(int x:z)rem.put(char(x));for(int x:w)rem.put(char(x));}
   }
  }
  assert(total==basic+oldT+postold);U added=0;for(auto p:newrules)added+=p.second;assert(postold==added+left);
  if(!first)result<<',';first=false;
  result<<"{\"v\":"<<v<<",\"eligible\":"<<total<<",\"basic\":"<<basic<<",\"old_T15\":"<<oldT<<",\"after_old\":"<<postold<<",\"newly_covered\":"<<added<<",\"remaining\":"<<left<<",\"new_rule_counts\":{";bool f=true;for(auto p:newrules){if(!f)result<<',';f=false;result<<'\"'<<p.first<<"\":"<<p.second;}result<<"}}";result.flush();
  cout<<"v="<<v<<" eligible="<<total<<" basic="<<basic<<" T15="<<oldT<<" afterold="<<postold<<" new="<<added<<" remaining="<<left<<endl;
 }
 result<<"]}\n";
}
