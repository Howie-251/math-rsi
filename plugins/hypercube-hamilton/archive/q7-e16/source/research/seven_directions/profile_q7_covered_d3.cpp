#include <fstream>
#include <iostream>
#include <array>
#include <cstdint>
using namespace std;
bool closes(int a,const int O[5],int x,int y,int outer){
 int J=0;
 for(int k=0;k<7;++k)if(k!=outer && !((x^a)&(1<<k)) && !((y^a)&(1<<k))){
  int n=0;for(int i=0;i<5;++i)n+=!((O[i]^a)&(1<<k));if(n==4)J|=1<<k;
 }
 for(int i=0;i<5;++i)if(__builtin_popcount((unsigned)((O[i]^a)&J))>=2)return true;
 return false;
}
int main(int argc,char**argv){
 if(argc!=4)return 2;ifstream in(argv[1],ios::binary);ofstream out(argv[2]),rem(argv[3],ios::binary);if(!in||!out||!rem)return 3;
 uint64_t total=0,covered=0,left=0;array<unsigned char,8>r;
 while(in.read((char*)r.data(),8)){
  ++total;int v=r[0];bool done=false;
  for(int j=0;j<7&&!done;++j){int bit=1<<j,ZA[3],ZB[3],WB[4],na=0,nb=0,ma=0,mb=0;
   for(int i=1;i<4;++i){if(!((r[i]^v)&bit))ZA[na++]=r[i];else ZB[nb++]=r[i];}
   for(int i=4;i<8;++i){if(!((r[i]^v)&bit))++ma;else WB[mb++]=r[i];}
   if(na!=2||ma!=1)continue;
   int a=ZB[0],x=ZA[0]^bit,y=ZA[1]^bit,O[5]={WB[0],WB[1],WB[2],x,y};
   done=closes(a,O,x,y,j);
  }
  if(done)++covered;else{++left;rem.write((char*)r.data(),8);}
 }
 out<<"{\"status\":\"PRODUCER_CONDITIONAL_GEOMETRY\",\"full_eight_covered_proved\":false,\"input\":"<<total<<",\"D3_single_crossing_obstruction\":"<<covered<<",\"remaining\":"<<left<<"}\n";
 cout<<"input="<<total<<" covered="<<covered<<" remaining="<<left<<endl;
}
