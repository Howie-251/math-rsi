// Replay every positive witness; independently exhaust every unhit input.
// Reads producer files only. args directory. stdout JSON.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include <map>
#include <set>
#include <tuple>
using namespace std;using U=uint64_t;using B=uint32_t;
int NZ,WIDTH;
int pc(U x){return __builtin_popcountll(x);}void req(bool x,string why){if(!x)throw runtime_error(why);}
array<unordered_set<U>,32> t26;unordered_set<U> t15,t17,t63;
U key(B J,B O){return U(J)|(U(O)<<32);} B shift(B x,int s){B r=0;while(x){int j=__builtin_ctz(x);x&=x-1;r|=B(1)<<(j^s);}return r;}
int family(B M,B J,B O){
 if((M&J)||(O&~J))return 0;
 int m=pc(M),j=pc(J),o=pc(O);
 if(!m){
  if(j==4&&o==2)return 1;
  if(j!=6||o!=3)return 0;
  for(int d=0;d<5;d++){int h=0,u=0;for(int x=0;x<32;x++)if(x>>d&1){h+=J>>x&1;u+=O>>x&1;}
   if((h==2&&u==1)||(h==4&&u==2))return 2;}
  return t63.count(key(J,O))?7:0;
 }
 int s=__builtin_ctz(M);M=shift(M,s);J=shift(J,s);O=shift(O,s);
 if(m==2&&j==6&&o==2){int q=__builtin_ctz(M&~B(1));return t26[q].count(key(J,O))?3:0;}
 if(m==1&&j==5&&o==2){B included=J&~O;for(int d=0;d<5;d++)if(included>>(1<<d)&1)return 5;
  return t15.count(key(J,O))?4:0;}
 if(m==1&&j==7&&o==3)return t17.count(key(J,O))?6:0;
 return 0;
}
int proj(int x,int d){int result=0,to=0;for(int from=0;from<6;from++)if(from!=d){result|=((x>>from)&1)<<to;to++;}return result;}
struct Cut{int d;bool even;int need;U pool;B M,J;};
bool makecut(const vector<unsigned char>&r,int v,bool f,int d,Cut&out){
 vector<int> za,zb,wa,wb;
 for(int i=0;i<WIDTH;i++){int x=r[i];bool a=((x^v)&(1<<d))==0;if(i<NZ)(a?za:zb).push_back(x);else(a?wa:wb).push_back(x);}
 int a=za.size(),b=wa.size(),gap=a+1-b;out={d,gap>=0,abs(gap),0,0,0};
 if(!out.need||(out.even&&b==0))return false;
 const auto& pool=out.even?za:wa;
 for(int x:pool)if(out.even||(x!=(1<<d)&&(!f||x!=v)))out.pool|=U(1)<<x;
 for(int x:(out.even?zb:wb))out.M|=B(1)<<proj(x,d);
 for(int x:(out.even?wb:zb))out.J|=B(1)<<proj(x,d);
 return pc(out.pool)>=out.need;
}
B omit(U S,int d){B o=0;while(S){int x=__builtin_ctzll(S);S&=S-1;o|=B(1)<<proj(x^(1<<d),d);}return o;}
bool choices(const Cut&c,U pool,int n,U S){if(!n){B O=omit(S,c.d);return family(c.M,c.J|O,O)!=0;}
 while(pc(pool)>=n){U bit=pool&-pool;pool-=bit;if(choices(c,pool,n-1,S|bit))return true;}return false;}
bool anyhit(const vector<unsigned char>&r,int v,bool f){for(int d=0;d<6;d++){Cut c;if(makecut(r,v,f,d,c)&&choices(c,c.pool,c.need,0))return true;}return false;}
U get(const vector<unsigned char>&b,int pos,int n){U r=0;for(int i=0;i<n;i++)r|=U(b[pos+i])<<(8*i);return r;}

using K=tuple<B,B,B>;using V=tuple<int,int,B>;
map<K,set<V>> reg;map<K,set<pair<int,int>>> allreg,selreg;
bool explicitHit(B M,B J,B O,bool rootB,int fam=-1,int id=-1,B R=0){
 int anchor=__builtin_ctz(M?M:O);auto it=reg.find({shift(M,anchor),shift(J,anchor),shift(O,anchor)});if(it==reg.end())return false;
 for(auto [ff,ii,rr]:it->second){B actual=shift(rr,anchor);if(rootB&&(actual&1))continue;
 if(fam<0||(fam==ff&&id==ii&&R==actual))return true;}return false;
}
bool accepted(const Cut&c,U S,int v){B O=omit(S,c.d),J=c.J|O;return family(c.M,J,O)||explicitHit(c.M,J,O,(v>>c.d)&1);}
bool exhaust(const Cut&c,U pool,int n,U S,int v){if(!n)return accepted(c,S,v);while(pc(pool)>=n){U bit=pool&-pool;pool-=bit;if(exhaust(c,pool,n-1,S|bit,v))return true;}return false;}
void legacy(string dir){for(string name:{"T26","T15","T17","T63"}){
 ifstream in(dir+"/HIGHER_Q5_FULL_REUSE_REVIEW_"+name+".txt");req(bool(in),"legacy registry");U M,J,O;while(in>>M>>J>>O){if(name=="T26")t26[__builtin_ctzll(M&~U(1))].insert(key(J,O));else(name=="T15"?t15:name=="T17"?t17:t63).insert(key(J,O));}}
 ifstream in(dir+"/HIGHER_POST12_REVIEW_registry.txt");B M,J,O,R;int f,id;while(in>>M>>J>>O>>R>>f>>id)reg[{M,J,O}].insert({f,id,R});req(reg.size()==47015,"registry cardinality");}
void validate(vector<unsigned char>&rec,int v,bool f,U&H){H=1;for(int i=0;i<WIDTH;i++){int x=rec[i];req(x<64&&!(H>>x&1)&&pc(x)%2==(i>=NZ),"geometry parity/domain");H|=U(1)<<x;}req(bool(H>>v&1)==f,"target status");for(int i=0;i<NZ;i++)for(int j=NZ;j<WIDTH;j++)req(pc(rec[i]^rec[j])!=1,"independence");if(f)for(int j=NZ;j<WIDTH;j++)req(pc(rec[j])!=1,"free full independence");}
void replay(vector<unsigned char>&w,vector<unsigned char>&rec,int v,bool f,int d,int off){Cut c;req(d<6&&makecut(rec,v,f,d,c),"legal cut");U S=get(w,8,8),H=1;for(int x:rec)H|=U(1)<<x;req(!(S&~c.pool)&&pc(S)==c.need,"sources exact pool/count");U copy=S;while(copy){int x=__builtin_ctzll(copy);copy&=copy-1;req(!(H>>(x^(1<<d))&1),"mirror nonhole");}B O=omit(S,d),J=c.J|O;req(!(O&(c.M|c.J))&&pc(O)==c.need,"omission geometry");req(get(w,16,4)==c.M&&get(w,20,4)==J&&get(w,24,4)==O,"simultaneous actual masks");
 if(off==32){int fam=w[5],id=get(w,6,2);B R=get(w,28,4);req((fam<=7&&id==0&&R==0&&family(c.M,J,O)==fam)||explicitHit(c.M,J,O,(v>>d)&1,fam,id,R),"exact accepted local theorem/forced exclusion");}
 else {int anchor=__builtin_ctz(c.M?c.M:O);auto it=allreg.find({shift(c.M,anchor),shift(J,anchor),shift(O,anchor)});req(it!=allreg.end()&&it->second.count({w[4],int(get(w,6,2))}),"candidate marked geometry");}}

int main(int argc,char**argv){try{req(argc==3,"directory and k");string dir=argv[1];int k=stoi(argv[2]);req(k==8||k==9,"k");NZ=k-1;WIDTH=2*k-1;legacy(dir);string stem=k==8?"SIXTEEN_POST12_REUSE":"EIGHTEEN_POST12_REUSE";
U total=0,yes=0,no=0;cout<<"{\"k\":"<<k<<",\"record_width\":"<<WIDTH<<",\"reports\":[";bool comma=false;
for(int v:{1,7,31})for(int f=0;f<2;f++){
string tag="h"+to_string(2*k)+"_v"+to_string(v)+"_"+(f?"free":"covered");
ifstream in(dir+"/HIGHER_Q5_FULL_residual_"+tag+".bin",ios::binary),rem(dir+"/"+stem+"_remaining_"+tag+".bin",ios::binary),wit(dir+"/"+stem+"_witness_"+tag+".bin",ios::binary);req(bool(in)&&bool(rem)&&bool(wit),"files");
vector<unsigned char>w(32),rec(WIDTH),other(WIDTH),previous;bool has=bool(wit.read((char*)w.data(),32));req(has||wit.gcount()==0,"initial witness partial");U idx=0,y=0,n=0;
while(in.read((char*)rec.data(),WIDTH)){
 U H;validate(rec,v,f,H);req(previous.empty()||previous<rec,"source strict order");previous=rec;req(!has||get(w,0,4)>=idx,"witness order");
 if(has&&get(w,0,4)==idx){replay(w,rec,v,f,w[4],32);y++;has=bool(wit.read((char*)w.data(),32));req(has||wit.gcount()==0,"witness partial");}
 else{req(bool(rem.read((char*)other.data(),WIDTH))&&other==rec,"exact residual byte partition");for(int d=0;d<6;d++){Cut c;if(makecut(rec,v,f,d,c))req(!exhaust(c,c.pool,c.need,0,v),"unhit record has accepted route");}n++;}idx++;
}
req(in.gcount()==0&&!has,"input/witness trailing");char extra;req(!rem.get(extra),"residual trailing");total+=idx;yes+=y;no+=n;if(comma)cout<<",";comma=true;cout<<"{\"v\":"<<v<<",\"free\":"<<f<<",\"input\":"<<idx<<",\"positive\":"<<y<<",\"remaining\":"<<n<<"}";cerr<<tag<<" independently verified "<<idx<<endl;
}cout<<"],\"input\":"<<total<<",\"positive\":"<<yes<<",\"remaining\":"<<no<<",\"status\":\"PASS\"}\n";
}catch(exception&e){cerr<<e.what()<<endl;return 1;}}
