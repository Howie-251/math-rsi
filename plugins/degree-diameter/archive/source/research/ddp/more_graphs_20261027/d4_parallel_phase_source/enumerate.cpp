#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
int main(int argc,char**argv){assert(argc==6);clock_t start=clock();rlimit limit{4,5};setrlimit(RLIMIT_CPU,&limit);ifstream f(argv[1]);long long begin=stoll(argv[2]),need=stoll(argv[3]),end=begin+need;ofstream out(argv[4]);string label=argv[5];int roots;f>>roots;vector<int>r(roots);vector<vector<vector<array<int,3>>>>co(roots,vector<vector<array<int,3>>>(20));
 for(int i=0;i<roots;i++){f>>r[i];for(int p=0;p<20;p++){int k;f>>k;co[i][p].resize(k);for(auto&a:co[i][p])f>>a[0]>>a[1]>>a[2];}}
 vector<long long>counts(roots),survive(roots),full(roots);vector<array<long long,62>>hist(roots);vector<array<long long,20>>reject(roots);vector<array<int,5>>params;long long actual=0;bool complete=true;clock_t loop=clock();
 for(long long idx=begin;idx<end;idx++){
  if((actual&4095)==0&&double(clock()-start)/CLOCKS_PER_SEC>3.8){complete=false;break;}
  int i=idx/(61*61),v=idx%(61*61),B=v/61,C=v%61;actual++;counts[i]++;
  auto coverage=[&](int phase){U bits=0;for(auto[a,b,c]:co[i][phase])bits|=U(1)<<((a*B+b*C+c)%61);return __builtin_popcountll(bits);};
  int first=coverage(0);hist[i][first]++;if(first!=61)continue;survive[i]++;int bad=-1;
  for(int p=1;p<20;p++)if(coverage(p)!=61){bad=p;reject[i][p]++;break;}
  if(bad<0){full[i]++;cout<<"HIT r="<<r[i]<<" B="<<B<<" C="<<C<<" D="<<(C+1)%61<<endl;}
  params.push_back({r[i],B,C,bad,bad<0});
 }
 out<<"{\"range_label\":\""<<label<<"\",\"start_index\":"<<begin<<",\"requested\":"<<need<<",\"processed\":"<<actual<<",\"status\":\""<<(complete?"COMPLETE_RANGE":"UNKNOWN_NATIVE_CPU_LIMIT")<<"\",\"per_action\":[";
 for(int i=0;i<roots;i++){
  if(i)out<<',';out<<"{\"r\":"<<r[i]<<",\"cases\":"<<counts[i]<<",\"phase0_survivors\":"<<survive[i]<<",\"full20phase_hits\":"<<full[i]<<",\"phase0_histogram\":{";bool first=true;
  for(int k=0;k<=61;k++)if(hist[i][k]){if(!first)out<<',';first=false;out<<'"'<<k<<"\":"<<hist[i][k];}out<<"},\"first_other_failed_phase_counts\":{";first=true;
  for(int p=1;p<20;p++)if(reject[i][p]){if(!first)out<<',';first=false;out<<'"'<<p<<"\":"<<reject[i][p];}out<<"}}";
 }
 out<<"],\"phase0_survivor_parameters\":[";for(size_t i=0;i<params.size();i++){if(i)out<<',';auto a=params[i];out<<"{\"r\":"<<a[0]<<",\"B\":"<<a[1]<<",\"C\":"<<a[2]<<",\"D\":"<<(a[2]+1)%61<<",\"first_other_failed_phase\":"<<a[3]<<",\"full_coverage\":"<<(a[4]?"true":"false")<<'}';}
 out<<"],\"loop_CPU_seconds\":"<<double(clock()-loop)/CLOCKS_PER_SEC<<",\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"DONE "<<label<<" cases="<<actual<<" phase0survive="<<accumulate(survive.begin(),survive.end(),0LL)<<" full="<<accumulate(full.begin(),full.end(),0LL)<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}
