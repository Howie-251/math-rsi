#include <array>
#include <cassert>
#include <ctime>
#include <iostream>
#include <map>
using namespace std;
struct Dart {int j,n,inv;};
array<Dart,7> d;
array<int,18> pw;
array<unsigned long long,342> count_endpoint{};
array<unsigned long long,7> count_depth{};
void enumerate_prefixes(int j,int n,int last,int depth){
 ++count_endpoint[19*j+n];++count_depth[depth];
 if(depth==6)return;
 for(int k=0;k<7;++k){
  if(last>=0 && k==d[last].inv)continue;
  enumerate_prefixes((j+d[k].j)%18,(n*pw[d[k].j]+d[k].n)%19,k,depth+1);
 }
}
int main(){
 const clock_t start=clock();pw[0]=1;
 for(int k=1;k<18;++k)pw[k]=pw[k-1]*9%19;
 assert(pw[17]*9%19==1);
 d[0]={17,17,3};d[1]={13,11,4};d[2]={10,17,5};
 for(int k=0;k<3;++k){int j=(18-d[k].j)%18;d[k+3]={j,(19-d[k].n*pw[j]%19)%19,k};}
 d[6]={9,0,6};
 for(int k=0;k<7;++k){auto a=d[k],b=d[a.inv];assert((a.j+b.j)%18==0);assert((a.n*pw[b.j]+b.n)%19==0);assert((b.n*pw[a.j]+a.n)%19==0);}
 enumerate_prefixes(0,0,-1,0);
 unsigned long long total=0,mn=count_endpoint[0],mx=0;int first=0;map<unsigned long long,int> hist;
 for(int k=0;k<342;++k){auto n=count_endpoint[k];total+=n;++hist[n];if(n<mn){mn=n;first=k;}if(n>mx)mx=n;}
 assert(total==65318);
 cout<<"{\"controller_states\":342,\"maximum_word_length\":6,\"prefix_count\":"<<total<<",\"minimum_raw_count\":"<<mn<<",\"maximum_raw_count\":"<<mx<<",\"first_minimum_slot\":"<<first<<",\"first_minimum_phase\":"<<first/19<<",\"first_minimum_normal19\":"<<first%19<<",\"raw_count_histogram\":{";
 bool comma=false;for(auto [n,c]:hist){if(comma)cout<<',';comma=true;cout<<'\"'<<n<<"\":"<<c;}cout<<"},\"count_by_word_length\":[";
 for(int k=0;k<7;++k){if(k)cout<<',';cout<<count_depth[k];}cout<<"],\"darts\":[";
 for(int k=0;k<7;++k){if(k)cout<<',';cout<<'['<<d[k].j<<','<<d[k].n<<','<<d[k].inv<<']';}cout<<"],\"raw_counts_phase_slow\":[";
 for(int k=0;k<342;++k){if(k)cout<<',';cout<<count_endpoint[k];}cout<<"],\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
}
