#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int pc(int m){return __builtin_popcount((unsigned)m);}
struct Job{int id,cas;vector<int>quad;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1],line;ifstream jin(dir+"/JOBS.tsv");vector<Job>jobs;
 while(getline(jin,line)){istringstream ss(line);Job j;int nq;assert(ss>>j.id>>j.cas>>nq);for(int k=0;k<nq;k++){int q;assert(ss>>q);j.quad.push_back(q);}jobs.push_back(j);}assert(jobs.size()==702);
 vector<int>tri,pairs;for(int m=0;m<128;m++){if(pc(m)==3)tri.push_back(m);if(pc(m)==2)pairs.push_back(m);}
 clock_t start=clock();bool complete=true;long total=0;int globalD=100000,maxscore=0;ofstream data(dir+"/NECESSARY.tsv"),out(dir+"/GENERATION.json");out<<"{\"scope\":\"complete one-J quad orbit representatives; full P3 multisets and one pair; unchanged D selector\",\"jobs\":[";
 for(Job j:jobs){
  vector<int>internal=j.cas==0?vector<int>{31}:vector<int>{124,j.cas==1?121:115};int nt=j.cas==0?2:3;array<int,7>c{},b{};for(int v=0;v<7;v++){for(int I:internal)c[v]+=int(I>>v&1);for(int q:j.quad)b[v]+=int(q>>v&1);}
  long rawhigh=0,pairiter=0,necessary=0;int localD=100000,localScore=0;vector<int>indices;
  function<void(int)>choose=[&](int first){
   if(!complete)return;
   if(int(indices.size())<nt){for(int k=first;k<35;k++){indices.push_back(k);choose(k);indices.pop_back();if(!complete)return;}return;}
   ++rawhigh;array<int,7>a{};vector<int>high=j.quad;for(int k:indices){high.push_back(tri[k]);for(int v=0;v<7;v++)a[v]+=int(tri[k]>>v&1);}
   for(int v=0;v<7;v++)if(2*a[v]+3*b[v]>15-4*c[v])return;
   vector<int>uncovered;for(int p:pairs){bool cov=false;for(int I:internal)cov=cov||((p&I)==p);for(int T:high)cov=cov||((p&T)==p);if(!cov)uncovered.push_back(p);}if(uncovered.size()>1)return;
   vector<int>distinct=high;sort(distinct.begin(),distinct.end());distinct.erase(unique(distinct.begin(),distinct.end()),distinct.end());
   for(int J:pairs){
    ++pairiter;if(uncovered.size()&&uncovered[0]!=J)continue;array<int,7>u{};bool ok=true;for(int v=0;v<7;v++){int s=int(J>>v&1);u[v]=8-c[v]-a[v]-b[v]-s;if(u[v]<0||s+2*a[v]+3*b[v]>15-4*c[v])ok=false;}if(!ok)continue;
    ++necessary;int W=0,M=0,best=99,bestQ=0,bestm=0,bestt=0;vector<array<int,3>>compatible;
    for(int Q:tri){
     bool exclude=(Q&J)==J;for(int T:distinct)exclude=exclude||(Q==T);if(exclude)continue;
     int m=0;for(int v=0;v<7;v++)if(Q>>v&1)m+=u[v];int t=int(!(Q&J)),weight=max(0,12-m-t),miss=0;for(int T:distinct)miss+=int(!(Q&T));W+=weight;M+=weight*miss;
     if(!miss){if(m+t<best){best=m+t;bestQ=Q;bestm=m;bestt=t;}if(m+t<=11)compatible.push_back({Q,m,t});}
    }
    int D=W-M;
    if(D<=0||best>11){
     ofstream fail(dir+"/FAILURE.json");fail<<"{\"scope\":\"nonpositive unchanged weighted selector, not an H counterexample\",\"job\":"<<j.id<<",\"case\":"<<j.cas<<",\"quad_masks\":[";for(int k=0;k<int(j.quad.size());k++){if(k)fail<<',';fail<<j.quad[k];}fail<<"],\"triple_masks\":[";for(int k=0;k<nt;k++){if(k)fail<<',';fail<<tri[indices[k]];}fail<<"],\"pair_mask\":"<<J<<",\"u\":[";for(int v=0;v<7;v++){if(v)fail<<',';fail<<u[v];}fail<<"],\"W\":"<<W<<",\"M\":"<<M<<",\"D\":"<<D<<",\"best_m_plus_t\":"<<best<<",\"best_blue\":"<<bestQ<<",\"best_m\":"<<bestm<<",\"best_t\":"<<bestt<<",\"gate_compatible_Q_m_t\":[";for(int k=0;k<int(compatible.size());k++){if(k)fail<<',';fail<<'['<<compatible[k][0]<<','<<compatible[k][1]<<','<<compatible[k][2]<<']';}fail<<"]}\n";complete=false;return;
    }
    unsigned packed=0;for(int k=0;k<nt;k++)packed|=unsigned(indices[k])<<(6*k);data<<j.id<<' '<<packed<<' '<<J<<' '<<D<<' '<<bestQ<<' '<<bestm<<' '<<bestt<<' '<<W<<' '<<M<<'\n';localD=min(localD,D);localScore=max(localScore,best);
   }
  };
  choose(0);total+=necessary;globalD=min(globalD,localD);maxscore=max(maxscore,localScore);if(j.id)out<<',';out<<"{\"id\":"<<j.id<<",\"case\":"<<j.cas<<",\"raw_P3_multisets\":"<<rawhigh<<",\"pair_iterations_after_prescreen\":"<<pairiter<<",\"necessary\":"<<necessary<<",\"minimum_D_accepted\":"<<localD<<",\"maximum_best_m_plus_t_accepted\":"<<localScore<<"}";
  if(!complete)break;assert(rawhigh==(nt==2?630:7770));assert(double(clock()-start)/CLOCKS_PER_SEC<20);
 }
 out<<"],\"complete\":"<<(complete?"true":"false")<<",\"necessary_total_before_stop\":"<<total<<",\"minimum_D_accepted\":"<<globalD<<",\"maximum_best_m_plus_t_accepted\":"<<maxscore<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"complete="<<complete<<" necessary="<<total<<" minD="<<globalD<<" maxscore="<<maxscore<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";return complete?0:2;
}
