#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <iterator>
#include <set>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
vector<unsigned char> read(const string&f){ifstream in(f,ios::binary);need(bool(in),"missing "+f);return {(istreambuf_iterator<char>(in)),{}};}
struct Key{uint32_t m,j,u;bool operator==(const Key&b)const{return m==b.m&&j==b.j&&u==b.u;}};
struct Hash{size_t operator()(const Key&k)const{return uint64_t(k.m)*0x9e3779b185ebca87ULL^(uint64_t(k.j)<<19)^uint64_t(k.u)*0xc2b2ae3d27d4eb4fULL;}};
using Lookup=unordered_map<Key,int,Hash>;
Lookup load(const string&f){ifstream in(f);need(bool(in),"lookup missing");Key k;int id;Lookup ans;while(in>>k.m>>k.j>>k.u>>id)need(ans.emplace(k,id).second,"duplicate lookup");return ans;}
int project(int x,int d){return (x&((1<<d)-1))|((x>>(d+1))<<d);}
uint32_t translate(uint32_t mask,int t){uint32_t out=0;while(mask){int x=__builtin_ctz(mask);mask&=mask-1;out|=uint32_t(1)<<(x^t);}return out;}
uint64_t get(const unsigned char*p,int n){uint64_t ans=0;for(int i=0;i<n;++i)ans|=uint64_t(p[i])<<(8*i);return ans;}
struct Witness{int v,f,id,d;uint32_t index;uint64_t S;array<uint32_t,4> masks{};};
uint64_t recordkey(int v,int f,uint32_t index){return (uint64_t(v)<<40)|(uint64_t(f)<<32)|index;}
unordered_map<uint64_t,Witness> witnesses(const string&file,int size){
 auto b=read(file);need(b.size()%size==0,"witness alignment");unordered_map<uint64_t,Witness> out;
 for(size_t off=0;off<b.size();off+=size){auto*p=&b[off];Witness w;w.v=p[0];w.f=p[1];w.index=get(p+2,4);w.id=p[6];w.d=p[7];w.S=get(p+8,8);
  need((w.v==1||w.v==7||w.v==31)&&w.f<=1&&w.d<6,"witness header");
  if(size==32)for(int j=0;j<4;++j)w.masks[j]=get(p+16+4*j,4);
  need(out.emplace(recordkey(w.v,w.f,w.index),w).second,"duplicate witness ID");
 }return out;
}
struct Geometry{array<int,5>Z;array<int,6>W;uint64_t holes;};
struct Hit{bool success=false;int id=-1;array<uint32_t,4> masks{};};
Hit evaluate(const Geometry&g,int v,int f,int d,uint64_t S,bool forced,const Lookup&lookup){
 bool targetSide=(v>>d)&1;vector<int>za,zb,wa,wb;
 for(int x:g.Z)(((x>>d)&1)==targetSide?za:zb).push_back(x);
 for(int x:g.W)(((x>>d)&1)==targetSide?wa:wb).push_back(x);
 int required=forced?3:2;bool even;
 if((!forced&&za.size()==2&&wa.size()==1)||(forced&&za.size()==4&&wa.size()==2))even=true;
 else if((!forced&&za.size()==0&&wa.size()==3)||(forced&&za.size()==1&&wa.size()==5))even=false;
 else return {};
 vector<int>pool=even?za:wa;uint64_t legal=0;
 for(int x:pool)if(even||(x!=(1<<d)&&(!f||x!=v)))legal|=uint64_t(1)<<x;
 if(__builtin_popcountll(S)!=required||(S&~legal))return {};
 uint32_t M=0,J=0,U=0;
 for(int x:even?zb:wb)M|=uint32_t(1)<<project(x,d);
 for(int x:even?wb:zb)J|=uint32_t(1)<<project(x,d);
 for(int x=0;x<64;++x)if((S>>x)&1){int y=x^(1<<d);need(!((g.holes>>y)&1),"source mirror is originally a hole");U|=uint32_t(1)<<project(y,d);}
 J|=U;need(__builtin_popcount(M)==(forced?1:3)&&__builtin_popcount(J)==7&&__builtin_popcount(U)==required,"projected counts");
 need(!(M&J),"projected holes overlap");int t=__builtin_ctz(M);
 Key key{translate(M,t),translate(J,t),translate(U,t)};auto it=lookup.find(key);if(it==lookup.end())return {};
 uint32_t R=0;
 if(forced){for(int e=0;e<5;++e)R|=uint32_t(1)<<(t^(1<<e));R&=~U;need(__builtin_popcount(R)==2&&!(R&(M|J)),"forced pair not covered");
  if(targetSide&&(R&1))return {};
 }
 Hit h;h.success=true;h.id=it->second;h.masks={M,J,U,R};return h;
}
bool enumerate(const Geometry&g,int v,int f,bool forced,const Lookup&lookup,long long&tries){
 bool found=false;
 for(int d=0;d<6;++d){vector<int>za,wa;for(int x:g.Z)if(((x>>d)&1)==((v>>d)&1))za.push_back(x);for(int x:g.W)if(((x>>d)&1)==((v>>d)&1))wa.push_back(x);
  vector<int>pool;int size=forced?3:2;
  if((!forced&&za.size()==2&&wa.size()==1)||(forced&&za.size()==4&&wa.size()==2))pool=za;
  else if((!forced&&za.size()==0&&wa.size()==3)||(forced&&za.size()==1&&wa.size()==5)){for(int x:wa)if(x!=(1<<d)&&(!f||x!=v))pool.push_back(x);}
  else continue;
  for(unsigned subset=0;subset<(1U<<pool.size());++subset)if(__builtin_popcount(subset)==size){uint64_t S=0;for(unsigned j=0;j<pool.size();++j)if((subset>>j)&1)S|=uint64_t(1)<<pool[j];++tries;found|=evaluate(g,v,f,d,S,forced,lookup).success;}
 }return found;
}
int main(){try{
 auto l37=load("HIGHER_Q5_FULL_T37_APPLICATION_REVIEW_lookup37.txt"),l17=load("HIGHER_Q5_FULL_T37_APPLICATION_REVIEW_lookup17.txt");
 need(l37.size()==11115&&l17.size()==310,"lookup size");
 auto w37=witnesses("HIGHER_Q5_FULL_T37_positive_witnesses.bin",16),w17=witnesses("HIGHER_Q5_FULL_FORCED17_safe_witnesses.bin",32);
 long long total=0,tot37=0,tot17=0,totboth=0,tries37=0,tries17=0,validated37=0,validated17=0;
 cout<<"{\"reports\":[";int group=0;
 for(int v:{1,7,31})for(int f:{0,1}){
  string tag="h12_v"+to_string(v)+"_"+(f?"free":"covered");auto data=read("HIGHER_Q5_FULL_reuse_remaining_"+tag+".bin");need(data.size()%11==0,"record alignment");
  vector<unsigned char>rem37,rem17,remunion;long long a=0,b=0,both=0;unordered_set<string>unique;
  for(size_t off=0;off<data.size();off+=11){Geometry g;g.holes=1;uint64_t seen=1;int i=off/11;need(unique.insert(string((char*)&data[off],11)).second,"duplicate original geometry");
   for(int j=0;j<11;++j){int x=data[off+j];need(x<64&&x!=0&&!((seen>>x)&1),"original hole label");seen|=uint64_t(1)<<x;need((__builtin_popcount(unsigned(x))%2)==(j<5?0:1),"original parity");if(j<5)g.Z[j]=x;else g.W[j-5]=x;g.holes|=uint64_t(1)<<x;}
   need(is_sorted(g.Z.begin(),g.Z.end())&&is_sorted(g.W.begin(),g.W.end()),"source record order");
   for(int z:g.Z)for(int w:g.W)need(__builtin_popcount(unsigned(z^w))!=1,"nonroot independence");
   need(bool((g.holes>>v)&1)==bool(f),"target covered/free status");
   if(f)for(int w:g.W)need(__builtin_popcount(unsigned(w))!=1,"free full-hole independence");
   uint64_t key=recordkey(v,f,i);auto p37=w37.find(key),p17=w17.find(key);
   if(p37!=w37.end()){auto&w=p37->second;auto h=evaluate(g,v,f,w.d,w.S,false,l37);need(h.success&&h.id==w.id,"bad selected T37 witness");++validated37;}
   if(p17!=w17.end()){auto&w=p17->second;auto h=evaluate(g,v,f,w.d,w.S,true,l17);need(h.success&&h.id==w.id&&h.masks==w.masks,"bad forced witness or actual masks");++validated17;}
   bool A=enumerate(g,v,f,false,l37,tries37),B=enumerate(g,v,f,true,l17,tries17);
   need(A==(p37!=w37.end())&&B==(p17!=w17.end()),"full predicate subset mismatch");
   if(!A)rem37.insert(rem37.end(),data.begin()+off,data.begin()+off+11);
   if(!B)rem17.insert(rem17.end(),data.begin()+off,data.begin()+off+11);
   if(!(A||B))remunion.insert(remunion.end(),data.begin()+off,data.begin()+off+11);
   a+=A;b+=B;both+=A&&B;
  }
  need(rem37==read("HIGHER_Q5_FULL_T37_remaining_"+tag+".bin"),"T37 residual bytes");
  need(rem17==read("HIGHER_Q5_FULL_FORCED17_remaining_"+tag+".bin"),"forced residual bytes");
  need(remunion==read("HIGHER_Q5_FULL_T37_FORCED_union_remaining_"+tag+".bin"),"union residual bytes");
  if(f)need(remunion.empty()&&rem37.empty()&&rem17.empty(),"free residual remains");
  long long n=data.size()/11;total+=n;tot37+=a;tot17+=b;totboth+=both;
  if(group++)cout<<",";cout<<"{\"v\":"<<v<<",\"free\":"<<f<<",\"input\":"<<n<<",\"T37\":"<<a<<",\"forced\":"<<b<<",\"intersection\":"<<both<<",\"union\":"<<a+b-both<<",\"remaining\":"<<remunion.size()/11<<"}";
  cerr<<"verified "<<tag<<" input "<<n<<" T37 "<<a<<" forced "<<b<<" remaining "<<remunion.size()/11<<"\n";
 }
 need(validated37==w37.size()&&validated17==w17.size(),"unconsumed witness indices");
 need(total==348283&&tot37==106052&&tot17==33305&&totboth==6317,"total count mismatch");
 cout<<"],\"input\":"<<total<<",\"T37\":"<<tot37<<",\"forced\":"<<tot17<<",\"intersection\":"<<totboth<<",\"union\":"<<tot37+tot17-totboth<<",\"remaining\":"<<total-tot37-tot17+totboth<<",\"T37_source_projections_checked\":"<<tries37<<",\"forced_source_projections_checked\":"<<tries17<<",\"selected_T37_witnesses_validated\":"<<validated37<<",\"selected_forced_witnesses_validated\":"<<validated17<<",\"all_18_residual_files_byte_equal\":true,\"pass\":true}\n";
}catch(const exception&e){cerr<<"CHECK FAILED "<<e.what()<<"\n";return 1;}return 0;}
