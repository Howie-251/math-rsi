#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
int main(int argc,char**argv){assert(argc==6);clock_t totalstart=clock();rlimit limit{10,11};setrlimit(RLIMIT_CPU,&limit);ifstream f(argv[1]);long long begin=stoll(argv[2]),requested=stoll(argv[3]),end=begin+requested;ofstream out(argv[4]);string label=argv[5];int roots;f>>roots;vector<int>r(roots);vector<vector<vector<array<int,4>>>>co(roots,vector<vector<array<int,4>>>(20));
 for(int ri=0;ri<roots;ri++){f>>r[ri];for(int p=0;p<20;p++){int n;f>>n;co[ri][p].resize(n);for(auto&a:co[ri][p])f>>a[0]>>a[1]>>a[2]>>a[3];}}
 vector<long long>count(roots),pass(roots),full(roots);vector<array<long long,62>>hist(roots);vector<array<long long,20>>failphase(roots);vector<array<int,6>>survivors;long long processed=0;bool complete=true;clock_t loopstart=clock();
 for(long long index=begin;index<end;index++){
  if((processed&4095)==0&&double(clock()-totalstart)/CLOCKS_PER_SEC>9){complete=false;break;}
  int ri=index/(61*61*61),x=index%(61*61*61),A=x/(61*61),B=x/61%61,C=x%61;count[ri]++;processed++;
  auto covered=[&](int phase){U seen=0;for(auto[a,b,c,d]:co[ri][phase])seen|=U(1)<<((a*A+b*B+c*C+d)%61);return __builtin_popcountll(seen);};
  int n=covered(10);hist[ri][n]++;if(n!=61)continue;pass[ri]++;int bad=-1;
  for(int p=0;p<20;p++)if(p!=10&&covered(p)!=61){bad=p;failphase[ri][p]++;break;}
  if(bad<0){full[ri]++;cout<<"HIT r="<<r[ri]<<" A="<<A<<" B="<<B<<" C="<<C<<endl;}
  survivors.push_back({r[ri],A,B,C,bad,bad<0});
 }
 double loopcpu=double(clock()-loopstart)/CLOCKS_PER_SEC;
 out<<"{\"range_label\":\""<<label<<"\",\"start_index\":"<<begin<<",\"requested_cases\":"<<requested<<",\"processed_cases\":"<<processed<<",\"status\":\""<<(complete?"COMPLETE_REQUESTED_RANGE":"UNKNOWN_NATIVE_CPU_LIMIT")<<"\",\"per_action\":[";
 for(int ri=0;ri<roots;ri++){
  if(ri)out<<',';out<<"{\"r\":"<<r[ri]<<",\"cases\":"<<count[ri]<<",\"phase10_survivors\":"<<pass[ri]<<",\"full20phase_hits\":"<<full[ri]<<",\"phase10_histogram\":{";bool first=true;
  for(int k=0;k<=61;k++)if(hist[ri][k]){if(!first)out<<',';first=false;out<<'"'<<k<<"\":"<<hist[ri][k];}out<<"},\"first_other_failed_phase_counts\":{";first=true;for(int p=0;p<20;p++)if(failphase[ri][p]){if(!first)out<<',';first=false;out<<'"'<<p<<"\":"<<failphase[ri][p];}out<<"}}";
 }
 out<<"],\"phase10_survivor_parameters\":[";for(size_t i=0;i<survivors.size();i++){if(i)out<<',';auto a=survivors[i];out<<"{\"r\":"<<a[0]<<",\"A\":"<<a[1]<<",\"B\":"<<a[2]<<",\"C\":"<<a[3]<<",\"first_other_failed_phase\":"<<a[4]<<",\"full_coverage\":"<<(a[5]?"true":"false")<<'}';}
 out<<"],\"loop_CPU_seconds\":"<<loopcpu<<",\"native_CPU_seconds\":"<<double(clock()-totalstart)/CLOCKS_PER_SEC<<"}\n";
 cout<<"DONE "<<label<<" processed="<<processed<<" phase10survive="<<accumulate(pass.begin(),pass.end(),0LL)<<" fullhits="<<accumulate(full.begin(),full.end(),0LL)<<" loopCPU="<<loopcpu<<endl;
}
