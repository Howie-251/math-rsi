#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
int main(int argc,char**argv){assert(argc==3);clock_t start=clock();rlimit lim{10,12};setrlimit(RLIMIT_CPU,&lim);ifstream f(argv[1]);ofstream o(argv[2]);int roots;f>>roots;long long total=0,evaluated=0,cached=0,survive=0,hits=0;
 o<<"{\"prediction\":\"P_FREE_PHASE10\",\"cases_by_action\":[";
 for(int ri=0;ri<roots;ri++){
  int r,oldB,oldD,oldcount;f>>r>>oldB>>oldD>>oldcount;vector<vector<array<int,3>>>co(20);
  for(int p=0;p<20;p++){int k;f>>k;co[p].resize(k);for(auto&a:co[p])f>>a[0]>>a[1]>>a[2];}
  long long count=0,reused=0,pass=0,full=0,newcount=0;array<long long,62>hist{};vector<array<int,5>>survivors;
  auto coverage=[&](int phase,int B,int C,int D){U b=0;for(auto[a,c,d]:co[phase])b|=U(1)<<((a*B+c*C+d*D)%61);return b;};
  auto test=[&](int B,int C,int D){count++;total++;int covered;bool reuse=C==1&&B==oldB&&D==oldD;
   if(reuse){covered=oldcount;reused++;cached++;}else{covered=__builtin_popcountll(coverage(10,B,C,D));newcount++;evaluated++;}
   hist[covered]++;if(covered<61)return;pass++;survive++;int fail=-1;
   for(int p=0;p<20;p++)if(p!=10&&__builtin_popcountll(coverage(p,B,C,D))<61){fail=p;break;}
   if(fail<0){full++;hits++;cout<<"HIT r="<<r<<" B="<<B<<" C="<<C<<" D="<<D<<endl;}
   survivors.push_back({B,C,D,fail,fail<0});
  };
  for(int B=0;B<61;B++)for(int D=0;D<61;D++)test(B,1,D);
  for(int D=0;D<61;D++)test(1,0,D);test(0,0,1);assert(count==3783&&reused==1);
  if(ri)o<<',';o<<"{\"r\":"<<r<<",\"normalized_cases\":"<<count<<",\"new_phase10_evaluations\":"<<newcount<<",\"cached_rejections\":"<<reused<<",\"phase10_distinct_linear_forms\":"<<co[10].size()<<",\"phase10_survivors\":"<<pass<<",\"full20phase_hits\":"<<full<<",\"phase10_coverage_histogram\":{";
  bool first=true;for(int k=0;k<=61;k++)if(hist[k]){if(!first)o<<',';first=false;o<<'"'<<k<<"\":"<<hist[k];}o<<"},\"survivors\":[";
  for(size_t i=0;i<survivors.size();i++){if(i)o<<',';auto a=survivors[i];o<<"{\"B\":"<<a[0]<<",\"C\":"<<a[1]<<",\"D\":"<<a[2]<<",\"first_failed_other_phase\":"<<a[3]<<",\"full_coverage\":"<<(a[4]?"true":"false")<<'}';}o<<"]}";
 }
 assert(total==30264&&cached==8&&evaluated==30256);
 o<<"],\"normalized_cases\":"<<total<<",\"new_phase10_evaluations\":"<<evaluated<<",\"cached_canonical_rejections\":"<<cached<<",\"phase10_survivors\":"<<survive<<",\"full20phase_hits\":"<<hits<<",\"prediction_supported\":"<<(survive?"true":"false")<<",\"status\":\""<<(survive?(hits?"COMPLETE_FULL_HITS":"COMPLETE_PHASE10_SURVIVORS_NO_FULL_HIT"):"COMPLETE_PHASE10_ZERO_SURVIVORS")<<"\",\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"pending\":[]}\n";
 cout<<"DONE cases="<<total<<" evaluated="<<evaluated<<" cached="<<cached<<" phase10survive="<<survive<<" fullhits="<<hits<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}
