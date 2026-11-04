#include <bits/stdc++.h>
using namespace std;using U=uint64_t;using B=uint32_t;
array<unordered_set<U>,4> lookup;int oi[32];
int project(int x,int d){return (x&((1<<d)-1))|((x>>(d+1))<<d);}
int hit(B M,B J,B O){
 int nm=__builtin_popcount(M),nj=__builtin_popcount(J),no=__builtin_popcount(O);
 if(nm==0&&nj==4&&no==2)return 1;
 if(nm==0&&nj==6&&no==3){
  for(int d=0;d<5;++d){int a=0,b=0;for(int x=0;x<32;++x)if(!(x>>d&1)){a+=(J>>x)&1;b+=(O>>x)&1;}if((a==2&&b==1)||(a==4&&b==2))return 2;}
  return lookup[3].count(U(J)|(U(O)<<32))?7:0;
 }
 if(nm!=1&&nm!=2)return 0;int shift=__builtin_ctz(M);B normJ=0,normO=0;
 for(int x=0;x<32;++x){if(J>>x&1)normJ|=B(1)<<(x^shift);if(O>>x&1)normO|=B(1)<<(x^shift);}
 if(nm==2&&nj==6&&no==2){
  int delta=__builtin_ctz(M&~(B(1)<<shift))^shift;U jm=0,om=0;
  for(int x=0;x<32;++x){if(normJ>>x&1)jm|=U(1)<<oi[x];if(normO>>x&1)om|=U(1)<<oi[x];}
  return lookup[0].count(U(delta)|(jm<<5)|(om<<21))?3:0;
 }
 U key=U(normO)|(U(normJ&~normO)<<32);
 if(nm==1&&nj==5&&no==2){
  if((normJ&~normO)&((B(1)<<1)|(B(1)<<2)|(B(1)<<4)|(B(1)<<8)|(B(1)<<16)))return 5;
  return lookup[1].count(key)?4:0;
 }
 if(nm==1&&nj==7&&no==3)return lookup[2].count(key)?6:0;
 return 0;
}
bool shape(int m,int j,int o){return(m==0&&j==4&&o==2)||(m==0&&j==6&&o==3)||(m==2&&j==6&&o==2)||(m==1&&j==5&&o==2)||(m==1&&j==7&&o==3);}
int main(int argc,char**argv){
 if(argc!=2)return 2;string dir=argv[1];string names[4]={"T26","T15","T17","T63"};
 for(int i=0;i<4;++i){ifstream f(dir+"/HIGHER_Q5_FULL_"+names[i]+"_lookup.txt");U key;while(f>>key)lookup[i].insert(key);if(lookup[i].empty())return 3;}
 fill(oi,oi+32,-1);int at=0;for(int x=0;x<32;++x)if(__builtin_popcount(unsigned(x))%2)oi[x]=at++;
 ofstream report(dir+"/HIGHER_Q5_FULL_reuse_filter.json");report<<"{\"status\":\"PRODUCER_ONLY_PENDING_REVIEW\",\"holes\":12,\"reports\":[";bool comma=false;
 for(int v:{1,7,31})for(int free=0;free<2;++free){
  string tag="h12_v"+to_string(v)+"_"+(free?"free":"covered");
  ifstream in(dir+"/HIGHER_Q5_FULL_residual_"+tag+".bin",ios::binary);
  ofstream out(dir+"/HIGHER_Q5_FULL_reuse_remaining_"+tag+".bin",ios::binary),wit(dir+"/HIGHER_Q5_FULL_reuse_witness_"+tag+".bin",ios::binary);
  unsigned char rec[11];uint32_t input=0,covered=0;array<U,8> histogram{};
  while(in.read((char*)rec,11)){
   bool success=false;
   for(int d=0;d<6&&!success;++d){
    vector<int> za,zb,wa,wb;for(int i=0;i<5;++i)(((rec[i]>>d&1)==(v>>d&1))?za:zb).push_back(rec[i]);
    for(int i=5;i<11;++i)(((rec[i]>>d&1)==(v>>d&1))?wa:wb).push_back(rec[i]);
    int a=za.size(),b=wa.size(),s=a+1-b;bool even=s>=0;vector<int> pool,minor,major;
    if(even){if(b<1)continue;pool=za;minor=zb;major=wb;}
    else{s=-s;for(int x:wa)if(x!=(1<<d)&&(!free||x!=v))pool.push_back(x);minor=wb;major=zb;}
    if(s<=0||s>(int)pool.size()||!shape(minor.size(),major.size()+s,s))continue;
    B M=0,base=0;for(int x:minor)M|=B(1)<<project(x,d);for(int x:major)base|=B(1)<<project(x,d);
    function<void(int,int,U,B)> choose=[&](int start,int need,U sources,B O){
     if(success)return;if(!need){B J=base|O;int type=hit(M,J,O);if(!type)return;success=true;++covered;++histogram[type];
      wit.write((char*)&input,4);unsigned char dd=d,tt=type;wit.put(dd);wit.put(tt);wit.write((char*)&sources,8);wit.write((char*)&M,4);wit.write((char*)&J,4);wit.write((char*)&O,4);return;}
     for(int i=start;i+need<=(int)pool.size();++i)choose(i+1,need-1,sources|(U(1)<<pool[i]),O|(B(1)<<project(pool[i],d)));
    };choose(0,s,0,0);
   }
   if(!success)out.write((char*)rec,11);++input;
  }
  if(!in.eof()||in.gcount())return 4;if(comma)report<<',';comma=true;
  report<<"{\"v\":"<<v<<",\"free_target\":"<<(free?"true":"false")<<",\"input\":"<<input<<",\"covered\":"<<covered<<",\"remaining\":"<<input-covered<<",\"first_witness_family_counts\":[";
  for(int i=0;i<8;++i){if(i)report<<',';report<<histogram[i];}report<<"]}";
  cout<<tag<<" input="<<input<<" covered="<<covered<<" remaining="<<input-covered<<endl;
 }
 report<<"],\"forced_T17_used\":false,\"full_twelve_hole_proved\":false,\"full_P6_proved\":false}\n";
}
