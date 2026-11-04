// Diagnostic producer: known A8 partial geometries + K8, actual local marks.
// Acceptance requires independent audits of these imports and this application.
#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
using U=unsigned long long;
bool a8(const vector<int>&minor,const vector<int>&major,int avoid,int removed){
 assert(minor.size()==3&&major.size()==5);
 for(int j=0;j<6;j++)if(j!=removed){
  int a=0,b=0;for(int x:minor)a+=!((x^avoid)>>j&1);for(int x:major)b+=!((x^avoid)>>j&1);
  int delta=b-a;if(delta>=1&&delta<=3)return true;
  if(a==1&&b==5)return true; // independently proposed delta4 first-orbit rule
 }
 return false;
}
int solve(const vector<int>&z,const vector<int>&w,int v){
 for(int d=0;d<6;d++){
  vector<int>za,zb,wa,wb;
  for(int x:z)(((x^v)>>d&1)?zb:za).push_back(x);
  for(int x:w)(((x^v)>>d&1)?wb:wa).push_back(x);
  int a=za.size(),b=wa.size();
  if(a==0&&b==1)return 1; // K8 on B, balanced2 endpoint on A
  if(a==1&&b==1){auto maj=wb;int y=za[0]^(1<<d);maj.push_back(y);if(a8(zb,maj,y,d))return 2;}
  if(a==0&&b==2)for(int s:wa)if(s!=(1<<d)){
   auto maj=zb;int y=s^(1<<d);maj.push_back(y);if(a8(wb,maj,y,d))return 3;
  }
  if(a==3&&b==4){auto maj=wa;maj.push_back(v);if(a8(za,maj,v,d))return 4;}
  if(a==4&&b==4)for(int s:za){
   auto min=za;min.erase(find(min.begin(),min.end(),s));auto maj=wa;maj.push_back(v);
   if(a8(min,maj,v,d))return 5;
  }
  if(a==3&&b==5)for(int s:wa)if(s!=(1<<d)){
   auto maj=wa;maj.erase(find(maj.begin(),maj.end(),s));maj.push_back(v);
   if(a8(za,maj,v,d))return 6;
  }
 }
 return 0;
}
int main(int argc,char**argv){
 if(argc!=2)return 2;string dir=argv[1];ofstream out(dir+"/ten_covered_partial_a8_filter.json");
 out<<"{\"scope\":\"Producer geometry filtering, not independent acceptance; K8/A8 partial imports and application require review\",\"full_ten_hole_proved\":false,\"targets\":[";
 bool comma=false;
 for(int v:{1,7,31}){
  string suffix="h10_v"+to_string(v)+"_covered.bin";
  ifstream f(dir+"/higher_hole_after_t15_"+suffix,ios::binary);if(!f)return 3;
  ofstream remain(dir+"/ten_covered_after_partial_a8_v"+to_string(v)+".bin",ios::binary);
  array<unsigned char,9>g{};map<int,U>hist;U n=0;
  while(f.read(reinterpret_cast<char*>(g.data()),9)){
   vector<int>z(g.begin(),g.begin()+4),w(g.begin()+4,g.end());int code=solve(z,w,v);++hist[code];++n;
   if(!code)remain.write(reinterpret_cast<char*>(g.data()),9);
  }
  if(f.gcount())return 4;
  if(comma)out<<',';comma=true;
  out<<"{\"v\":"<<v<<",\"input\":"<<n<<",\"remaining\":"<<hist[0]<<",\"codes\":{";
  bool sep=false;for(auto [c,k]:hist){if(sep)out<<',';sep=true;out<<'"'<<c<<"\":"<<k;}out<<"}}";
  cout<<"v="<<v<<" input="<<n<<" remaining="<<hist[0]<<endl;
 }
 out<<"]}\n";
}
