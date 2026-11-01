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
struct Job{int id,shape,quad;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];ifstream jobsin(dir+"/JOBS.tsv");vector<Job>jobs;Job j;while(jobsin>>j.id>>j.shape>>j.quad)jobs.push_back(j);assert(jobs.size()==11);
 vector<int>triples,pairs;for(int m=0;m<128;m++){if(pc(m)==3)triples.push_back(m);if(pc(m)==2)pairs.push_back(m);}assert(triples.size()==35);
 ofstream data(dir+"/NECESSARY.tsv"),report(dir+"/GENERATION.json");report<<"{\"scope\":\"all eleven quad positions; all five-P3 multisets; u/PL/Ppair necessary domain; no exterior layouts\",\"row_columns\":[\"job\",\"packed_five_triple_indices_base64\",\"D\",\"blue\",\"m\",\"W\",\"M\"],\"jobs\":[";
 clock_t start=clock();long total=0;bool complete=true;int overallMargin=100000,overallCost=0;
 for(Job job:jobs){
  assert(job.id>=0&&job.id<11);int I1=127^3,I2=127^(job.shape==0?6:12);array<int,7>c{};for(int v=0;v<7;v++)c[v]=int((I1>>v)&1)+int((I2>>v)&1);
  long raw=0,necessary=0;int margin=100000,maxcost=0;
  for(int a=0;a<35;a++)for(int b=a;b<35;b++)for(int d=b;d<35;d++)for(int e=d;e<35;e++)for(int f=e;f<35;f++){
   ++raw;vector<int>H={triples[a],triples[b],triples[d],triples[e],triples[f],job.quad};array<int,7>h{},w{},u{};bool ok=true;
   for(int T:H)for(int v=0;v<7;v++)if(T>>v&1){++h[v];w[v]+=pc(T)-1;}
   for(int v=0;v<7;v++){u[v]=8-c[v]-h[v];if(u[v]<0||w[v]>15-4*c[v])ok=false;}if(!ok)continue;
   for(int p:pairs){bool covered=(p&I1)==p||(p&I2)==p;for(int T:H)covered=covered||((p&T)==p);if(!covered){ok=false;break;}}if(!ok)continue;
   ++necessary;vector<int>distinct=H;sort(distinct.begin(),distinct.end());distinct.erase(unique(distinct.begin(),distinct.end()),distinct.end());
   int W=0,M=0,bestm=99,bestQ=0;
   for(int Q:triples){
    int cost=0;for(int v=0;v<7;v++)if(Q>>v&1)cost+=u[v];
    bool equals=false;for(int T:distinct)equals=equals||(Q==T);
    int weight=equals?0:max(0,12-cost),miss=0;for(int T:distinct)if(!(Q&T))++miss;
    W+=weight;M+=weight*miss;
    if(!equals&&!miss&&cost<bestm){bestm=cost;bestQ=Q;}
   }
   int D=W-M;
   if(D<=0||bestm>11){
    ofstream failure(dir+"/FAILURE.json");failure<<"{\"job\":"<<job.id<<",\"quad\":"<<job.quad<<",\"triples\":[";
    for(int k=0;k<5;k++){if(k)failure<<',';failure<<H[k];}failure<<"],\"u\":[";for(int k=0;k<7;k++){if(k)failure<<',';failure<<u[k];}failure<<"],\"D\":"<<D<<",\"minimum_proper_cost\":"<<bestm<<"}\n";complete=false;goto endjob;
   }
   {
    unsigned packed=unsigned(a)|(unsigned(b)<<6)|(unsigned(d)<<12)|(unsigned(e)<<18)|(unsigned(f)<<24);
    data<<job.id<<' '<<packed<<' '<<D<<' '<<bestQ<<' '<<bestm<<' '<<W<<' '<<M<<'\n';
   }
   margin=min(margin,D);maxcost=max(maxcost,bestm);
  }
  endjob:
  total+=necessary;overallMargin=min(overallMargin,margin);overallCost=max(overallCost,maxcost);
  if(job.id)report<<',';report<<"{\"id\":"<<job.id<<",\"shape\":"<<job.shape<<",\"quad\":"<<job.quad<<",\"raw\":"<<raw<<",\"necessary\":"<<necessary<<",\"minimum_D\":"<<margin<<",\"maximum_minimum_cost\":"<<maxcost<<"}";
  if(!complete)break;assert(raw==575757);assert(double(clock()-start)/CLOCKS_PER_SEC<15);
 }
 data.close();report<<"],\"complete\":"<<(complete?"true":"false")<<",\"total_necessary\":"<<total<<",\"minimum_D\":"<<overallMargin<<",\"maximum_minimum_cost\":"<<overallCost<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"complete="<<complete<<" necessary="<<total<<" minD="<<overallMargin<<" maxcost="<<overallCost<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
 return complete?0:2;
}
