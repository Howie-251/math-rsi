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
using namespace std;using U=uint64_t;using B=uint32_t;
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
 for(int i=0;i<11;i++){int x=r[i];bool a=((x^v)&(1<<d))==0;if(i<5)(a?za:zb).push_back(x);else(a?wa:wb).push_back(x);}
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
int main(int argc,char**argv){try{
 req(argc==2,"args");string dir=argv[1];
 for(string name:{"T26","T15","T17","T63"}){
  ifstream in(dir+"/HIGHER_Q5_FULL_REUSE_REVIEW_"+name+".txt");req(bool(in),"registry open");U M,J,O;int count=0;
  while(in>>M>>J>>O){count++;if(name=="T26"){req(pc(M)==2&&(M&1),"M normalize");t26[__builtin_ctzll(M&~U(1))].insert(key(J,O));}
   else (name=="T15"?t15:name=="T17"?t17:t63).insert(key(J,O));}
  req(count>0,"empty registry");
 }
 cout<<"{\"status\":\"PASS\",\"reports\":[";bool comma=false;
 for(int v:{1,7,31})for(int f=0;f<2;f++){
  string tag="h12_v"+to_string(v)+"_"+(f?"free":"covered");
  ifstream in(dir+"/HIGHER_Q5_FULL_residual_"+tag+".bin",ios::binary),remain(dir+"/HIGHER_Q5_FULL_reuse_remaining_"+tag+".bin",ios::binary),wit(dir+"/HIGHER_Q5_FULL_reuse_witness_"+tag+".bin",ios::binary);
  req(bool(in)&&bool(remain)&&bool(wit),"open domain");
  vector<unsigned char> rec(11),other(11),w(26);bool has=bool(wit.read((char*)w.data(),26));if(!has)req(wit.gcount()==0,"partial witness");
  U index=0,yes=0,no=0;array<U,8> hist{};vector<unsigned char> previous;
  while(in.read((char*)rec.data(),11)){
   req(previous.empty()||previous<rec,"input unique/order");previous=rec;
   U holes=1;for(int i=0;i<11;i++){int x=rec[i];req(x<64&&x!=0,"input vertex");req(pc(x)%2==(i>=5),"input parity");holes|=U(1)<<x;}
   req(pc(holes)==12&&bool(holes>>v&1)==bool(f),"input holes/status");
   for(int i=0;i<5;i++)for(int j=5;j<11;j++)req(pc(rec[i]^rec[j])!=1,"independence");
   if(has)req(get(w,0,4)>=index,"witness unique index/order");
   if(has&&get(w,0,4)==index){
    int d=w[4],code=w[5];req(d<6&&code>=1&&code<=7,"witness type");Cut c;req(makecut(rec,v,f,d,c),"witness cut");U S=get(w,6,8);
    req((S&~c.pool)==0&&pc(S)==c.need,"source membership/count/exclusion");
    U tmp=S;while(tmp){int x=__builtin_ctzll(tmp);tmp&=tmp-1;int y=x^(1<<d);req(!(holes>>y&1),"mirror originally covered and not root");}
    B O=omit(S,d),J=c.J|O;req(pc(O)==c.need&&!(O&c.J)&&!(O&c.M),"actual omitted mirrors distinct");
    req(c.M==get(w,14,4)&&J==get(w,18,4)&&O==get(w,22,4),"actual projected witness masks");
    req(family(c.M,J,O)==code,"actual marked theorem membership");hist[code]++;yes++;
    has=bool(wit.read((char*)w.data(),26));if(!has)req(wit.gcount()==0,"trailing partial witness");
   }else{
    req(bool(remain.read((char*)other.data(),11))&&other==rec,"exact residual byte/order partition");
    req(!anyhit(rec,v,f),"remaining record has accepted source/cut");no++;
   }
   index++;
  }
  req(in.gcount()==0&&!has,"input alignment/witness index range");char extra;req(!remain.get(extra),"trailing remaining data");
  if(comma)cout<<',';comma=true;
  cout<<"{\"v\":"<<v<<",\"free_target\":"<<(f?"true":"false")<<",\"input\":"<<index<<",\"covered\":"<<yes<<",\"remaining\":"<<no<<",\"first_witness_family_counts\":[";
  for(int j=0;j<8;j++){if(j)cout<<',';cout<<hist[j];}cout<<"]}";
 }
 cout<<"],\"every_positive_witness_replayed\":true,\"every_remaining_record_exhaustive\":true,\"exact_remaining_bytes\":true,\"forced_T17_used\":false}\n";
 }catch(exception&e){cerr<<e.what()<<endl;return 1;}}
