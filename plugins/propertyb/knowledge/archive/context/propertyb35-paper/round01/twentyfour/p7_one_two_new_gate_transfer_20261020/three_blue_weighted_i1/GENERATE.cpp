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
struct Job{int id,q1,q2,q3;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];ifstream jin(dir+"/JOBS.tsv");vector<Job>jobs;Job job;while(jin>>job.id>>job.q1>>job.q2>>job.q3)jobs.push_back(job);assert(jobs.size()==101);
 vector<int>tri,pairs;for(int m=0;m<128;m++){if(pc(m)==3)tri.push_back(m);if(pc(m)==2)pairs.push_back(m);}
 clock_t start=clock();long total=0;bool complete=true;int globalmin=100000,maxcost=0;ofstream data(dir+"/NECESSARY.tsv"),out(dir+"/GENERATION.json");out<<"{\"scope\":\"I1 (0,4,3); all101 three-quad orbits and all four-P3 multisets; u/PL/Ppair necessary domain; same D formula\",\"jobs\":[";
 for(Job j:jobs){
  long raw=0,necessary=0;int margin=100000,largestcost=0;vector<int>quads={j.q1,j.q2,j.q3};array<int,7>c{},b{};for(int v=0;v<7;v++){c[v]=int(v<5);for(int q:quads)b[v]+=int(q>>v&1);}
  for(int t0=0;t0<35;t0++)for(int t1=t0;t1<35;t1++)for(int t2=t1;t2<35;t2++)for(int t3=t2;t3<35;t3++){
   ++raw;vector<int>H={tri[t0],tri[t1],tri[t2],tri[t3],j.q1,j.q2,j.q3};array<int,7>a{},u{};bool ok=true;
   for(int k=0;k<4;k++)for(int v=0;v<7;v++)a[v]+=int(H[k]>>v&1);
   for(int v=0;v<7;v++){u[v]=8-c[v]-a[v]-b[v];if(u[v]<0||2*a[v]+3*b[v]>15-4*c[v])ok=false;}if(!ok)continue;
   for(int p:pairs){bool covered=(p&31)==p;for(int T:H)covered=covered||((p&T)==p);if(!covered){ok=false;break;}}if(!ok)continue;
   ++necessary;vector<int>distinct=H;sort(distinct.begin(),distinct.end());distinct.erase(unique(distinct.begin(),distinct.end()),distinct.end());int W=0,M=0,bestm=99,bestQ=0;
   for(int Q:tri){int cost=0;for(int v=0;v<7;v++)if(Q>>v&1)cost+=u[v];bool excluded=false;for(int T:distinct)excluded=excluded||(Q==T);int lambda=excluded?0:max(0,12-cost),miss=0;for(int T:distinct)miss+=int(!(Q&T));W+=lambda;M+=lambda*miss;if(!excluded&&!miss&&cost<bestm){bestm=cost;bestQ=Q;}}
   int D=W-M;
   if(D<=0||bestm>11){
    ofstream failure(dir+"/FAILURE.json");failure<<"{\"scope\":\"failure of unchanged D selector, not H or signed counterexample\",\"job\":"<<j.id<<",\"quads\":["<<j.q1<<','<<j.q2<<','<<j.q3<<"],\"triples\":["<<H[0]<<','<<H[1]<<','<<H[2]<<','<<H[3]<<"],\"u\":[";for(int v=0;v<7;v++){if(v)failure<<',';failure<<u[v];}failure<<"],\"W\":"<<W<<",\"M\":"<<M<<",\"D\":"<<D<<",\"minimum_proper_cost\":"<<bestm<<",\"proper_witness\":"<<bestQ<<"}\n";complete=false;goto endjob;
   }
   unsigned key=unsigned(t0)|(unsigned(t1)<<6)|(unsigned(t2)<<12)|(unsigned(t3)<<18);data<<j.id<<' '<<key<<' '<<D<<' '<<bestQ<<' '<<bestm<<' '<<W<<' '<<M<<'\n';margin=min(margin,D);largestcost=max(largestcost,bestm);
  }
  endjob:
  total+=necessary;globalmin=min(globalmin,margin);maxcost=max(maxcost,largestcost);if(j.id)out<<',';out<<"{\"id\":"<<j.id<<",\"quads\":["<<j.q1<<','<<j.q2<<','<<j.q3<<"],\"raw\":"<<raw<<",\"necessary\":"<<necessary<<",\"minimum_D\":"<<margin<<",\"maximum_minimum_cost\":"<<largestcost<<"}";
  if(!complete)break;assert(raw==73815);assert(double(clock()-start)/CLOCKS_PER_SEC<20);
 }
 out<<"],\"complete\":"<<(complete?"true":"false")<<",\"total_necessary_before_stop\":"<<total<<",\"minimum_D_on_accepted\":"<<globalmin<<",\"maximum_minimum_cost_on_accepted\":"<<maxcost<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"complete="<<complete<<" necessary="<<total<<" minDaccepted="<<globalmin<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";return complete?0:2;
}
