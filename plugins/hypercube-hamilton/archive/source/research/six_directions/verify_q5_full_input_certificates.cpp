// No search: each expected input and its exact target cycle are checked.
#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){
 assert(argc==6);uint64_t expected=stoull(argv[3]);int o1=stoi(argv[4]),o2=stoi(argv[5]);
 assert(o1>=0&&o1<32&&o2>=0&&o2<32&&o1!=o2);
 ifstream in(argv[1],ios::binary),cert(argv[2],ios::binary);assert(in&&cert);unsigned char a[26],b[56];uint64_t count=0;
 while(in.read((char*)a,26)){
  cert.read((char*)b,56);assert(cert.gcount()==56&&equal(a,a+26,b));bool required[32][32]{};uint32_t support=0;
  for(int j=0;j<26;j+=2){int x=a[j],y=a[j+1];assert(x<32&&y<32&&x!=y&&!(support>>x&1)&&!(support>>y&1));support|=(1u<<x)|(1u<<y);required[x][y]=required[y][x]=true;}
  assert(!(support>>o1&1)&&!(support>>o2&1));uint32_t seen=0;int found=0;
  for(int j=0;j<30;j++){unsigned x=b[26+j],y=b[26+(j+1)%30];assert(x<32&&y<32&&!(seen>>x&1));seen|=1u<<x;if(required[x][y])found++;else assert(__builtin_popcount(x^y)==1);}
  assert(seen==(0xffffffffu^(1u<<o1)^(1u<<o2))&&found==13);count++;
 }
 assert(in.eof()&&in.gcount()==0&&count==expected);char tail;assert(!cert.get(tail));
 cout<<"{\"status\":\"PASS\",\"records\":"<<count<<",\"omitted\":["<<o1<<","<<o2<<"]}\n";
}
