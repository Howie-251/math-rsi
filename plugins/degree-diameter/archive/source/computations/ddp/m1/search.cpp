#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <csignal>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
volatile sig_atomic_t stop_requested=0;
void stop_handler(int){stop_requested=1;}
struct Search {
 int n; vector<vector<int>> mul;vector<int> inv,invol;
 using State=array<int,7>;
 int evaluate(const State&s) const {
  int total=0;
  for(int side=0;side<2;side++){
   array<unsigned char,256> seen{};array<int,256>q{},dep{};int end=1;
   q[0]=side*n; seen[q[0]]=1;
   for(int head=0;head<end;head++){
    int u=q[head],side_u=u/n,g=u%n;
    if(dep[head]==3)continue;
    for(int k=0;k<6;k++){
     int v;if(k==0)v=side_u*n+mul[g][s[side_u]];
     else if(side_u==0)v=n+mul[g][s[k+1]];
     else v=mul[g][inv[s[k+1]]];
     if(!seen[v]){seen[v]=1;q[end]=v;dep[end++]=dep[head]+1;}
    }
   }
   total+=2*n-end;
  }return total;
 }
 void save(const State&s,int score,const string&prefix,unsigned long long steps,double sec)const{
  ofstream j(prefix+".json");j<<"{\"group_order\":"<<n<<",\"n\":"<<2*n<<",\"representative_missing_sum\":"<<score<<",\"implied_bad_unordered_pairs\":"<<(n*score/2)<<",\"steps\":"<<steps<<",\"seconds_at_best\":"<<sec<<",\"parameters\":[";
  for(int i=0;i<7;i++)j<<(i?",":"")<<s[i];j<<"]}\n";
  set<pair<int,int>>edges;
  auto add=[&](int u,int v){if(u>v)swap(u,v);edges.emplace(u,v);};
  for(int g=0;g<n;g++){
   add(g,mul[g][s[0]]);add(n+g,n+mul[g][s[1]]);
   for(int i=2;i<7;i++)add(g,n+mul[g][s[i]]);
  }
  ofstream e(prefix+".edges");e<<2*n<<" "<<edges.size()<<"\n";for(auto [u,v]:edges)e<<u<<" "<<v<<"\n";
 }
};
int main(int argc,char**argv){
 if(argc<5){cerr<<"usage: search GROUP_TABLE SECONDS SEED OUT_PREFIX [INITIAL_PARAMETERS]\n";return 2;}
 signal(SIGTERM,stop_handler);signal(SIGINT,stop_handler);
 Search z;ifstream in(argv[1]);in>>z.n;if(!in||z.n<6||z.n>128)return 2;
 z.mul.assign(z.n,vector<int>(z.n));for(auto&r:z.mul)for(int&v:r)in>>v;if(!in)return 2;
 z.inv.resize(z.n);for(int i=0;i<z.n;i++){auto it=find(z.mul[i].begin(),z.mul[i].end(),0);if(it==z.mul[i].end())return 2;z.inv[i]=it-z.mul[i].begin();if(i&&z.mul[i][i]==0)z.invol.push_back(i);}if(z.n>67){z.invol.erase(remove_if(z.invol.begin(),z.invol.end(),[&](int a){for(int g=0;g<z.n;g++)if(z.mul[a][g]!=z.mul[g][a])return false;return true;}),z.invol.end());}if(z.invol.empty())return 2;
 double limit=stod(argv[2]);mt19937_64 rng(stoull(argv[3]));string prefix=argv[4];auto t0=chrono::steady_clock::now();
 auto elapsed=[&](){return chrono::duration<double>(chrono::steady_clock::now()-t0).count();};
 auto random_state=[&](){Search::State s{};s[0]=z.invol[rng()%z.invol.size()];s[1]=z.invol[rng()%z.invol.size()];s[2]=0;for(int i=3;i<7;i++){do{s[i]=rng()%z.n;}while(find(s.begin()+2,s.begin()+i,s[i])!=s.begin()+i);}return s;};
 auto cur=random_state();if(argc>=6){ifstream init(argv[5]);for(int&i:cur)init>>i;if(!init)return 2;}
 if(cur[0]<=0||cur[1]<=0||cur[0]>=z.n||cur[1]>=z.n||z.mul[cur[0]][cur[0]]||z.mul[cur[1]][cur[1]])return 2;
 for(int i=2;i<7;i++)if(cur[i]<0||cur[i]>=z.n)return 2;
 if(set<int>(cur.begin()+2,cur.end()).size()!=5)return 2;
 int score=z.evaluate(cur),best=score;unsigned long long step=0;z.save(cur,best,prefix,step,elapsed());auto best_state=cur;
 cout<<"initial_missing "<<best<<endl;
 while(best>0&&!stop_requested&&elapsed()<limit){
  ++step;auto nxt=cur;int k=rng()%6;if(k>=2)k++;
  if(k<2)nxt[k]=z.invol[rng()%z.invol.size()];
  else {do{nxt[k]=rng()%z.n;}while(find(nxt.begin()+2,nxt.begin()+k,nxt[k])!=nxt.begin()+k||find(nxt.begin()+k+1,nxt.end(),nxt[k])!=nxt.end());}
  int ns=z.evaluate(nxt);double temp=2.5*pow(0.06,double(step%30000)/30000.0);
  if(ns<=score||generate_canonical<double,53>(rng)<exp(double(score-ns)/temp)){cur=nxt;score=ns;}
  if(score<best){best=score;best_state=cur;z.save(cur,best,prefix,step,elapsed());cout<<"best "<<best<<" step "<<step<<" sec "<<elapsed()<<endl;}
  if(step%30000==0){cur=(step%90000==0)?random_state():best_state;score=z.evaluate(cur);}
 }
 ofstream end(prefix+".terminal.json");end<<"{\"status\":\""<<(best==0?"CANDIDATE_COVERED":stop_requested?"STOPPED":"BUDGET_EXHAUSTED")<<"\",\"steps\":"<<step<<",\"seconds\":"<<elapsed()<<",\"best_missing_sum\":"<<best<<"}\n";
 cout<<"terminal best "<<best<<" steps "<<step<<" seconds "<<elapsed()<<endl;
}
