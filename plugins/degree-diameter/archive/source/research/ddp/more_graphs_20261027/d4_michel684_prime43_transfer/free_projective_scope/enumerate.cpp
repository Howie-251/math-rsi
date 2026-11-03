#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;using F=array<int,5>;
constexpr long long PER=3500201;constexpr U FULL=(U(1)<<43)-1;
struct Action{int r;array<int,36>ord;array<vector<F>,36>co;vector<unsigned char>tab;vector<int>base;array<int,3>last{{-1,-1,-1}};long long count=0,thin=0,hit=0;array<long long,44>hist{};array<long long,36>failed{};vector<F>examples;};
F point(long long k){F v{};for(int first=0;first<5;first++){long long n=1;for(int j=first+1;j<5;j++)n*=43;if(k>=n){k-=n;continue;}v[first]=1;for(int j=4;j>first;j--){v[j]=k%43;k/=43;}return v;}abort();}
int coverage(const vector<F>&forms,const F&v){U b=0;for(auto a:forms){int e=(a[0]*v[0]+a[1]*v[1]+a[2]*v[2]+a[3]*v[3]+a[4]*v[4])%43;b|=U(1)<<e;if(b==FULL)return 43;}return __builtin_popcountll(b);}
int main(int argc,char**argv){assert(argc==6);clock_t start=clock();rlimit lim{14,15};setrlimit(RLIMIT_CPU,&lim);ifstream in(argv[1]);long long begin=stoll(argv[2]),need=stoll(argv[3]);ofstream out(argv[4]);string label=argv[5];int n;in>>n;vector<Action>a(n);for(auto&x:a){in>>x.r;for(int&i:x.ord)in>>i;for(auto&c:x.co){int k;in>>k;c.resize(k);for(auto&f:c)for(int&i:f)in>>i;}
 auto&c=x.co[x.ord[0]];int K=c.size();x.tab.resize(43*43*K);x.base.resize(K);for(int s=0;s<43;s++)for(int t=0;t<43;t++)for(int j=0;j<K;j++)x.tab[(s*43+t)*K+j]=(c[j][3]*s+c[j][4]*t)%43;
 }
 double init=double(clock()-start)/CLOCKS_PER_SEC;clock_t loop=clock();long long done=0;bool timed=false,found=false;int hitr=0;F hitp{};
 for(long long idx=begin;idx<begin+need;idx++){
  if((done&4095)==0&&double(clock()-start)/CLOCKS_PER_SEC>13.8){timed=true;break;}
  int ri=idx/PER;assert(ri<n);auto&x=a[ri];F v=point(idx%PER);x.count++;done++;
  auto&c=x.co[x.ord[0]];int K=c.size();array<int,3>pre{v[0],v[1],v[2]};if(pre!=x.last){for(int j=0;j<K;j++)x.base[j]=(c[j][0]*v[0]+c[j][1]*v[1]+c[j][2]*v[2])%43;x.last=pre;}
  const unsigned char*tab=x.tab.data()+(v[3]*43+v[4])*K;U bits=0;for(int j=0;j<K;j++){int e=x.base[j]+tab[j];if(e>=43)e-=43;bits|=U(1)<<e;}int cnt=__builtin_popcountll(bits);x.hist[cnt]++;if(cnt!=43)continue;x.thin++;
  if(x.examples.size()<8)x.examples.push_back(v);int bad=-1;for(int j=1;j<36;j++)if(coverage(x.co[x.ord[j]],v)!=43){bad=x.ord[j];x.failed[bad]++;break;}
  if(bad<0){x.hit++;found=true;hitr=x.r;hitp=v;cout<<"HIT r="<<hitr<<" idx="<<idx<<" params=";for(int z:v)cout<<z<<',';cout<<endl;break;}
 }
 double loopcpu=double(clock()-loop)/CLOCKS_PER_SEC;
 out<<"{\"range_label\":\""<<label<<"\",\"start_index\":"<<begin<<",\"requested\":"<<need<<",\"processed\":"<<done<<",\"status\":\""<<(found?"FIRST_FULL_HIT":timed?"PARTIAL_CPU_LIMIT":"COMPLETE_RANGE")<<"\",\"initialization_CPU_seconds\":"<<init<<",\"loop_CPU_seconds\":"<<loopcpu<<",\"per_action\":[";
 for(int i=0;i<n;i++){if(i)out<<',';auto&x=a[i];out<<"{\"r\":"<<x.r<<",\"cases\":"<<x.count<<",\"thin_cross_survivors\":"<<x.thin<<",\"full_hits\":"<<x.hit<<",\"thin_coverage_histogram\":{";bool comma=false;for(int k=0;k<=43;k++)if(x.hist[k]){if(comma)out<<',';comma=true;out<<'"'<<k<<"\":"<<x.hist[k];}out<<"},\"first_other_failed_slot_counts\":{";comma=false;for(int j=0;j<36;j++)if(x.failed[j]){if(comma)out<<',';comma=true;out<<'"'<<j<<"\":"<<x.failed[j];}out<<"},\"first_eight_thin_survivors\":[";for(size_t j=0;j<x.examples.size();j++){if(j)out<<',';out<<'[';for(int k=0;k<5;k++){if(k)out<<',';out<<x.examples[j][k];}out<<']';}out<<"]}";}
 out<<"],\"first_full_hit\":";if(!found)out<<"null";else{out<<"{\"r\":"<<hitr<<",\"parameters\":[";for(int i=0;i<5;i++){if(i)out<<',';out<<hitp[i];}out<<"]}";}out<<",\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"DONE "<<label<<" processed="<<done<<" thin=";long long ts=0;for(auto&x:a)ts+=x.thin;cout<<ts<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<" loop="<<loopcpu<<endl;
}
