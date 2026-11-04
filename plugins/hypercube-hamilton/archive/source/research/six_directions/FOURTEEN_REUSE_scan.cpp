#include <bits/stdc++.h>
using namespace std;using U=uint64_t;using B=uint32_t;
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
struct Key{B m,j,o;bool operator==(const Key&b)const{return m==b.m&&j==b.j&&o==b.o;}};
struct Hash{size_t operator()(const Key&k)const{return U(k.m)*0x9e3779b185ebca87ULL^(U(k.j)<<17)^U(k.o)*0xc2b2ae3d27d4eb4fULL;}};
struct Value{B R;int family,id;};struct Hit{int family=0,id=0;B R=0;};
array<unordered_set<U>,4>old;unordered_map<Key,Value,Hash>registry;unordered_set<int>shapes;int oi[32],projection[6][64];U neighbor[64];
int shapeid(int m,int j,int o){return(m<<16)|(j<<8)|o;}
B trans(B a,int t){B out=0;while(a){int x=__builtin_ctz(a);a&=a-1;out|=B(1)<<(x^t);}return out;}
Hit hit(B M,B J,B O,bool rootB){int nm=__builtin_popcount(M),nj=__builtin_popcount(J),no=__builtin_popcount(O);
 if(nm==0&&nj==4&&no==2)return{1,0,0};
 if(nm==0&&nj==6&&no==3){for(int d=0;d<5;++d){int a=0,b=0;for(int x=0;x<32;++x)if(!(x>>d&1)){a+=(J>>x)&1;b+=(O>>x)&1;}if((a==2&&b==1)||(a==4&&b==2))return{2,0,0};}if(old[3].count(U(J)|(U(O)<<32)))return{7,0,0};}
 int anchor=__builtin_ctz(M?M:O);B normM=trans(M,anchor),normJ=trans(J,anchor),normO=trans(O,anchor);
 if(nm==2&&nj==6&&no==2){int delta=__builtin_ctz(M&~(B(1)<<anchor))^anchor;U jm=0,om=0;for(int x=0;x<32;++x){if(normJ>>x&1)jm|=U(1)<<oi[x];if(normO>>x&1)om|=U(1)<<oi[x];}if(old[0].count(U(delta)|(jm<<5)|(om<<21)))return{3,0,0};}
 if(nm==1&&nj==5&&no==2){if((normJ&~normO)&((B(1)<<1)|(B(1)<<2)|(B(1)<<4)|(B(1)<<8)|(B(1)<<16)))return{5,0,0};if(old[1].count(U(normO)|(U(normJ&~normO)<<32)))return{4,0,0};}
 if(nm==1&&nj==7&&no==3)if(old[2].count(U(normO)|(U(normJ&~normO)<<32)))return{6,0,0};
 auto it=registry.find({normM,normJ,normO});if(it==registry.end())return{};B R=trans(it->second.R,anchor);if(rootB&&(R&1))return{};if(R)need(no>=3&&!(R&(M|J))&&__builtin_popcount(R)==2,"forced theorem hypotheses");return{it->second.family,it->second.id,R};
}
void put(unsigned char*p,U x,int n){for(int j=0;j<n;++j)p[j]=(x>>(j*8))&255;}
int main(int argc,char**argv){try{
 string mode=argc>1?argv[1]:"full";need(mode=="full"||mode=="benchmark","mode");uint32_t limit=argc>2?stoul(argv[2]):numeric_limits<uint32_t>::max();string stem=mode=="full"?"FOURTEEN_REUSE":"FOURTEEN_REUSE_benchmark";
 for(int x=0;x<64;++x){for(int d=0;d<6;++d){projection[d][x]=(x&((1<<d)-1))|((x>>(d+1))<<d);neighbor[x]|=U(1)<<(x^(1<<d));}}
 int at=0;fill(oi,oi+32,-1);for(int x=0;x<32;++x)if(__builtin_popcount(unsigned(x))%2)oi[x]=at++;
 string names[4]={"T26","T15","T17","T63"};for(int i=0;i<4;++i){ifstream f("HIGHER_Q5_FULL_"+names[i]+"_lookup.txt");need(bool(f),"old lookup missing");U key;while(f>>key)old[i].insert(key);need(!old[i].empty(),"empty lookup");}
 for(auto a:vector<array<int,3>>{{0,4,2},{0,6,3},{2,6,2},{1,5,2},{1,7,3}})shapes.insert(shapeid(a[0],a[1],a[2]));
 ifstream reg("FOURTEEN_REUSE_registry.txt");need(bool(reg),"registry missing");Key key;Value val;while(reg>>key.m>>key.j>>key.o>>val.R>>val.family>>val.id){need(registry.emplace(key,val).second,"duplicate registry key");shapes.insert(shapeid(__builtin_popcount(key.m),__builtin_popcount(key.j),__builtin_popcount(key.o)));}need(registry.size()==44085,"registry size");
 ofstream report(stem+"_result.json");report<<"{\"status\":\"PRODUCER_ONLY_PENDING_INDEPENDENT_APPLICATION_REVIEW\",\"mode\":\""<<mode<<"\",\"holes\":14,\"reports\":[";bool comma=false;U totin=0,totcovered=0,totproj=0;auto start=chrono::steady_clock::now();
 for(int v:{1,7,31})for(int free=0;free<2;++free){string tag="h14_v"+to_string(v)+"_"+(free?"free":"covered");ifstream in("HIGHER_Q5_FULL_residual_"+tag+".bin",ios::binary);need(bool(in),"source missing");ofstream out(stem+"_remaining_"+tag+".bin",ios::binary),wit(stem+"_witness_"+tag+".bin",ios::binary);need(bool(out)&&bool(wit),"output open");
  uint32_t index=0,covered=0;array<U,32>hist{};U tries=0;unsigned char rec[13];auto groupstart=chrono::steady_clock::now();
  while(index<limit&&in.read((char*)rec,13)){
   U holes=1,Wmask=0;for(int i=0;i<13;++i){int x=rec[i];need(x<64&&!((holes>>x)&1)&&(__builtin_popcount(unsigned(x))%2==(i<6?0:1)),"source labels/parity");holes|=U(1)<<x;if(i>=6)Wmask|=U(1)<<x;}need(bool((holes>>v)&1)==bool(free),"target status");for(int i=0;i<6;++i)need(!(neighbor[rec[i]]&Wmask),"nonroot independence");if(free)need(!(neighbor[0]&Wmask),"free full-hole independence");
   bool success=false;
   for(int d=0;d<6&&!success;++d){vector<int>za,zb,wa,wb;for(int i=0;i<6;++i)(((rec[i]>>d&1)==(v>>d&1))?za:zb).push_back(rec[i]);for(int i=6;i<13;++i)(((rec[i]>>d&1)==(v>>d&1))?wa:wb).push_back(rec[i]);
    int a=za.size(),b=wa.size(),s=a+1-b;bool even=s>=0;vector<int>pool,minor,major;
    if(even){if(b<1)continue;pool=za;minor=zb;major=wb;}else{s=-s;for(int x:wa)if(x!=(1<<d)&&(!free||x!=v))pool.push_back(x);minor=wb;major=zb;}
    if(s<=0||s>(int)pool.size()||!shapes.count(shapeid(minor.size(),major.size()+s,s)))continue;
    B M=0,base=0;for(int x:minor)M|=B(1)<<projection[d][x];for(int x:major)base|=B(1)<<projection[d][x];
    for(unsigned subset=0;subset<(1U<<pool.size())&&!success;++subset)if(__builtin_popcount(subset)==s){U sources=0;B O=0;for(unsigned j=0;j<pool.size();++j)if(subset>>j&1){int x=pool[j],y=x^(1<<d);need(!((holes>>y)&1),"source mirror is hole/root");sources|=U(1)<<x;O|=B(1)<<projection[d][y];}B J=base|O;need(!(M&J)&&__builtin_popcount(O)==s,"actual marked masks");++tries;auto found=hit(M,J,O,(v>>d)&1);if(!found.family)continue;
     success=true;++covered;++hist[found.family];unsigned char w[32]{};put(w,index,4);w[4]=d;w[5]=found.family;put(w+6,found.id,2);put(w+8,sources,8);put(w+16,M,4);put(w+20,J,4);put(w+24,O,4);put(w+28,found.R,4);wit.write((char*)w,32);
    }
   }
   if(!success)out.write((char*)rec,13);++index;
  }
  if(index<limit)need(in.eof()&&!in.gcount(),"source trailing bytes");need(bool(out)&&bool(wit),"output write failure");double seconds=chrono::duration<double>(chrono::steady_clock::now()-groupstart).count();totin+=index;totcovered+=covered;totproj+=tries;
  if(comma)report<<",";comma=true;report<<"{\"v\":"<<v<<",\"free_target\":"<<(free?"true":"false")<<",\"input\":"<<index<<",\"covered\":"<<covered<<",\"remaining\":"<<index-covered<<",\"source_projections_evaluated\":"<<tries<<",\"seconds\":"<<seconds<<",\"first_witness_family_counts\":{";bool hc=false;for(int i=0;i<32;++i)if(hist[i]){if(hc)report<<",";hc=true;report<<"\""<<i<<"\":"<<hist[i];}report<<"}}";report.flush();
  cout<<tag<<" input="<<index<<" covered="<<covered<<" remaining="<<index-covered<<" seconds="<<seconds<<endl;
 }
 double seconds=chrono::duration<double>(chrono::steady_clock::now()-start).count();report<<"],\"input\":"<<totin<<",\"covered\":"<<totcovered<<",\"remaining\":"<<totin-totcovered<<",\"source_projections_evaluated\":"<<totproj<<",\"seconds\":"<<seconds<<",\"all_local_inputs_final_PASS\":true,\"source_reduction_conditional_on_full_twelve_hole\":true,\"independent_application_review_passed\":false,\"unreviewed_star_A_or_MAmax_used\":false,\"full_fourteen_hole_proved\":false,\"full_P6_proved\":false}\n";
}catch(const exception&e){cerr<<"ERROR "<<e.what()<<endl;return 1;}return 0;}
