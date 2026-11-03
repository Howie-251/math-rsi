// Two inverse pairs (one per side), five cross voltages: degree7, targetD5.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <csignal>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <set>
#include <vector>
using namespace std;
volatile sig_atomic_t stopped=0;void stop(int){stopped=1;}
using State=array<int,6>; // a,b,s1,s2,s3,s4; identity cross voltage implicit.
struct Model {
 int p,m,r,q,n;vector<int> power,inverse,queue;vector<vector<int>>mul;vector<unsigned>seen;unsigned stamp=0;
 Model(int pp,int mm,int rr):p(pp),m(mm),r(rr),q(p*m),n(2*q),power(m),inverse(q),queue(n),mul(q,vector<int>(q)),seen(n){
  power[0]=1;for(int i=1;i<m;i++)power[i]=power[i-1]*r%p;
  if(power.back()*r%p!=1)throw runtime_error("action invalid");
  for(int g=0;g<q;g++)for(int h=0;h<q;h++)mul[g][h]=((g/m+power[g%m]*(h/m))%p)*m+(g%m+h%m)%m;
  for(int g=0;g<q;g++){int i=(m-g%m)%m;inverse[g]=((p-power[i]*(g/m)%p)%p)*m+i;}
 }
 int fi(int x){int a=1,e=p-2;while(e){if(e&1)a=a*x%p;x=x*x%p;e>>=1;}return a;}
 bool canonical(State&z){
  for(int j=0;j<2;j++)if(z[j]%m>inverse[z[j]]%m)z[j]=inverse[z[j]];
  int d=m,pivot=-1;array<int,6>v{};
  for(int j=0;j<6;j++){d=gcd(d,z[j]%m);v[j]=(1-power[z[j]%m]+p)%p;if(v[j]&&pivot<0)pivot=j;}
  if(d!=1||pivot<0)return false;
  int h=(p-z[pivot]/m)*fi(v[pivot])%p;
  for(int j=0;j<6;j++)z[j]=((z[j]/m+v[j]*h)%p)*m+z[j]%m;
  int scale=0;for(int g:z)if(g/m){scale=fi(g/m);break;}
  if(!scale)return false;
  for(int&g:z)g=(g/m*scale%p)*m+g%m;
  for(int j=0;j<2;j++)if(!z[j]||z[j]==inverse[z[j]])return false;
  set<int>s{0};for(int j=2;j<6;j++)if(!s.insert(z[j]).second)return false;
  return true;
 }
 array<int,2> evaluate(const State&z){
  array<int,2>miss;int ai=inverse[z[0]],bi=inverse[z[1]];array<int,4>si;for(int j=0;j<4;j++)si[j]=inverse[z[j+2]];
  for(int side=0;side<2;side++){
   ++stamp;int head=0,end=1;queue[0]=side*q;seen[queue[0]]=stamp;
   auto add=[&](int v){if(seen[v]!=stamp){seen[v]=stamp;queue[end++]=v;}};
   for(int depth=0;depth<5&&end<n;depth++){
    int boundary=end;while(head<boundary){int u=queue[head++];if(u<q){auto&row=mul[u];add(row[z[0]]);add(row[ai]);add(q+u);for(int j=2;j<6;j++)add(q+row[z[j]]);}else{int g=u-q;auto&row=mul[g];add(q+row[z[1]]);add(q+row[bi]);add(g);for(int s:si)add(row[s]);}}
   }miss[side]=n-end;
  }return miss;
 }
 void save(const string&path,const State&z,array<int,2>miss,double cpu,unsigned long long steps){
  set<pair<int,int>>edges;auto add=[&](int u,int v){if(u>v)swap(u,v);edges.emplace(u,v);};
  for(int g=0;g<q;g++){add(g,mul[g][z[0]]);add(g,mul[g][inverse[z[0]]]);add(q+g,q+mul[g][z[1]]);add(q+g,q+mul[g][inverse[z[1]]]);add(g,q+g);for(int j=2;j<6;j++)add(g,q+mul[g][z[j]]);}
  ofstream f(path+".edges");f<<n<<" "<<edges.size()<<"\n";for(auto[u,v]:edges)f<<u<<" "<<v<<"\n";
  ofstream j(path+".json");j<<"{\"p\":"<<p<<",\"m\":"<<m<<",\"action\":"<<r<<",\"n\":"<<n<<",\"degree\":7,\"target_diameter\":5,\"A_generator\":"<<z[0]<<",\"B_generator\":"<<z[1]<<",\"S\":[0";for(int i=2;i<6;i++)j<<","<<z[i];j<<"],\"root_missing\":["<<miss[0]<<","<<miss[1]<<"],\"representative_missing_sum\":"<<miss[0]+miss[1]<<",\"bad_unordered_pairs\":"<<(long long)q*(miss[0]+miss[1])/2<<",\"cpu_seconds\":"<<cpu<<",\"steps\":"<<steps<<"}\n";
 }
};
int main(int argc,char**argv){
 if(argc!=7&&argc!=8){cerr<<"P M ACTION CPU_SECONDS SEED OUT [initial_six_values]\n";return 2;}
 Model model(stoi(argv[1]),stoi(argv[2]),stoi(argv[3]));double budget=stod(argv[4]);mt19937_64 rng(stoull(argv[5]));string out=argv[6];
 auto randomstate=[&](){State z;do{for(int&g:z)g=rng()%model.q;}while(!model.canonical(z));return z;};
 State current=randomstate();if(argc==8){ifstream f(argv[7]);for(int&g:current)f>>g;if(!f)return 2;for(int g:current)if(g<0||g>=model.q)return 2;if(!model.canonical(current))return 2;}
 signal(SIGINT,stop);signal(SIGTERM,stop);clock_t cpu0=clock();auto cpu=[&](){return double(clock()-cpu0)/CLOCKS_PER_SEC;};auto wall0=chrono::steady_clock::now();
 State beststate=current;auto miss=model.evaluate(current);int score=miss[0]+miss[1],best=score;unsigned long long steps=0,accepted=0;model.save(out+".best",current,miss,cpu(),steps);cout<<"initial "<<score<<endl;
 auto propose=[&](State base){int slot=rng()%6;do{base[slot]=(rng()%4?((rng()%model.p)*model.m+base[slot]%model.m):rng()%model.q);}while(!model.canonical(base));return base;};
 vector<int>deltas;
 if(best&&budget>0){for(int i=0;i<256&&cpu()<budget;i++){State z=propose(current);auto mm=model.evaluate(z);int ns=mm[0]+mm[1];int d=ns-score;if(d>0)deltas.push_back(d);if(ns<best){best=ns;beststate=z;model.save(out+".best",z,mm,cpu(),steps);cout<<"calibration_best "<<best<<endl;if(!best)break;}}}
 sort(deltas.begin(),deltas.end());double temp0=deltas.empty()?4.0:max(1.0,deltas[deltas.size()/4]/log(5.0));
 {ofstream f(out+".calibration.json");f<<"{\"positive_deltas\":"<<deltas.size()<<",\"temperature0\":"<<temp0;if(!deltas.empty())f<<",\"minimum_positive\":"<<deltas.front()<<",\"quarter_positive\":"<<deltas[deltas.size()/4]<<",\"median_positive\":"<<deltas[deltas.size()/2];f<<"}\n";}
 int segment=-1;
 while(best&&!stopped&&cpu()<budget){
  double elapsed=cpu();int nextseg=min(5,int(6*elapsed/budget));if(nextseg!=segment){segment=nextseg;current=(segment==3)?randomstate():beststate;auto mm=model.evaluate(current);score=mm[0]+mm[1];}
  double phase=6*elapsed/budget-segment;double temp=temp0*pow(.015,phase);State next=propose(current);auto mm=model.evaluate(next);int ns=mm[0]+mm[1];steps++;
  if(ns<=score||generate_canonical<double,53>(rng)<exp(double(score-ns)/temp)){current=next;score=ns;accepted++;}
  if(score<best){best=score;beststate=current;model.save(out+".best",current,model.evaluate(current),cpu(),steps);cout<<"best "<<best<<" cpu "<<cpu()<<" steps "<<steps<<endl;}
 }
 model.save(out+".last",current,model.evaluate(current),cpu(),steps);
 ofstream f(out+".terminal.json");f<<"{\"status\":\""<<(best==0?"CANDIDATE_COVERED":stopped?"STOPPED":"BUDGET_EXHAUSTED")<<"\",\"steps\":"<<steps<<",\"accepted\":"<<accepted<<",\"best_missing\":"<<best<<",\"cpu_seconds\":"<<cpu()<<",\"wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-wall0).count()<<"}\n";cout<<"terminal "<<best<<" cpu "<<cpu()<<endl;
}
