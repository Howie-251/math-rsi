#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int pc(int m){return __builtin_popcount((unsigned)m);}
struct Job{int id,cas,q0,q1,q2;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];ifstream in(dir+"/JOBS.tsv");vector<Job>jobs;Job x;while(in>>x.id>>x.cas>>x.q0>>x.q1>>x.q2)jobs.push_back(x);assert(jobs.size()==630);
 vector<int>tri,pairs;for(int m=0;m<128;m++){if(pc(m)==3)tri.push_back(m);if(pc(m)==2)pairs.push_back(m);}
 clock_t start=clock();long necessary=0,pairAccepted=0,weightedAccepted=0,nonpositiveSavedByPair=0;int completed=0,minD=100000;bool full=true;ofstream accepted(dir+"/FALLBACK_NECESSARY.tsv");
 for(Job j:jobs){
  vector<int>internal={124,j.cas==0?121:115},quads={j.q0,j.q1,j.q2};array<int,7>c{},b{};for(int v=0;v<7;v++){for(int I:internal)c[v]+=int(I>>v&1);for(int q:quads)b[v]+=int(q>>v&1);}
  for(int i=0;i<35;i++)for(int k=i;k<35;k++){
   vector<int>high=quads;high.push_back(tri[i]);high.push_back(tri[k]);array<int,7>a{},u{};bool ok=true;for(int v=0;v<7;v++){a[v]=int(tri[i]>>v&1)+int(tri[k]>>v&1);u[v]=8-c[v]-a[v]-b[v];if(u[v]<0||2*a[v]+3*b[v]>15-4*c[v])ok=false;}if(!ok)continue;
   for(int pair:pairs){bool cov=false;for(int I:internal)cov=cov||((pair&I)==pair);for(int T:high)cov=cov||((pair&T)==pair);if(!cov){ok=false;break;}}if(!ok)continue;
   ++necessary;vector<int>distinct=high;sort(distinct.begin(),distinct.end());distinct.erase(unique(distinct.begin(),distinct.end()),distinct.end());int W=0,M=0,best=99,bestQ=0;vector<array<int,2>>proper;
   for(int Q:tri){bool ex=(Q==tri[i]||Q==tri[k]);int cost=0;for(int v=0;v<7;v++)if(Q>>v&1)cost+=u[v];int wt=ex?0:max(0,12-cost),miss=0;for(int T:distinct)miss+=int(!(Q&T));W+=wt;M+=wt*miss;if(!ex&&!miss){proper.push_back({Q,cost});if(cost<best){best=cost;bestQ=Q;}}}
   int D=W-M,pairQ=0,paircost=0;
   for(int Q:pairs){bool good=true;for(int I:internal)good=good&&bool(Q&I);for(int T:high)good=good&&bool(Q&T);if(good){pairQ=Q;for(int v=0;v<7;v++)if(Q>>v&1)paircost+=u[v];assert(paircost<=9);break;}}
   if(!pairQ&&(D<=0||best>11)){
    ofstream failure(dir+"/FALLBACK_FAILURE.json");failure<<"{\"scope\":\"no proper bluepair and unchanged weighted3 nonpositive; necessary P-source only, not an H or signed counterexample\",\"job\":"<<j.id<<",\"case\":"<<j.cas<<",\"internal_masks\":["<<internal[0]<<','<<internal[1]<<"],\"quad_masks\":["<<j.q0<<','<<j.q1<<','<<j.q2<<"],\"triple_masks\":["<<tri[i]<<','<<tri[k]<<"],\"u\":[";for(int v=0;v<7;v++){if(v)failure<<',';failure<<u[v];}failure<<"],\"W\":"<<W<<",\"M\":"<<M<<",\"D\":"<<D<<",\"proper_pair_count\":0,\"minimum_proper_three_cost\":"<<best<<",\"best_blue_three\":"<<bestQ<<",\"all_proper_three_cost\":[";for(int z=0;z<int(proper.size());z++){if(z)failure<<',';failure<<'['<<proper[z][0]<<','<<proper[z][1]<<']';}failure<<"]}\n";full=false;goto stop;
   }
   unsigned packed=unsigned(i)|(unsigned(k)<<6);
   if(pairQ){++pairAccepted;if(D<=0)++nonpositiveSavedByPair;accepted<<j.id<<' '<<packed<<" 2 "<<pairQ<<' '<<paircost<<' '<<D<<' '<<W<<' '<<M<<'\n';}
   else{++weightedAccepted;accepted<<j.id<<' '<<packed<<" 3 "<<bestQ<<' '<<best<<' '<<D<<' '<<W<<' '<<M<<'\n';}
   minD=min(minD,D);
  }++completed;assert(double(clock()-start)/CLOCKS_PER_SEC<10);
 }
 stop:
 ofstream report(dir+"/FALLBACK_GENERATION.json");report<<"{\"complete\":"<<(full?"true":"false")<<",\"quad_jobs_total\":630,\"quad_jobs_completed_before_stop\":"<<completed<<",\"necessary_sources_tested_including_failure\":"<<necessary<<",\"pair_gate_accepted\":"<<pairAccepted<<",\"weighted_three_accepted\":"<<weightedAccepted<<",\"nonpositive_D_saved_by_pair\":"<<nonpositiveSavedByPair<<",\"minimum_D_on_accepted_prefix\":"<<minD<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";cout<<"complete="<<full<<" jobs_completed="<<completed<<" necessary="<<necessary<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";return full?0:2;
}
