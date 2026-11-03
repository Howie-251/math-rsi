// General two-orbit lift with inverse-closed internal neighborhoods.
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
volatile sig_atomic_t stop_requested=0;void stop_handler(int){stop_requested=1;}
struct State{vector<int>a,b,s;};
int main(int argc,char**argv){
 if(argc!=7){cerr<<"usage GROUP_TABLE INTERNAL_DEGREE SECONDS SEED OUT_PREFIX DIAMETER\n";return 2;}
 ifstream f(argv[1]);int q;f>>q;if(!f||q>128||q<6)return 2;vector<vector<int>>mul(q,vector<int>(q));for(auto&r:mul)for(int&x:r)f>>x;if(!f)return 2;
 vector<int>inv(q);vector<vector<int>>blocks;for(int i=0;i<q;i++){inv[i]=find(mul[i].begin(),mul[i].end(),0)-mul[i].begin();if(inv[i]>=q)return 2;if(i&&i<=inv[i])blocks.push_back(i==inv[i]?vector<int>{i}:vector<int>{i,inv[i]});}
 int r=stoi(argv[2]),sdeg=6-r,D=stoi(argv[6]);if(r<1||r>5||D<1)return 2;double limit=stod(argv[3]);mt19937_64 rng(stoull(argv[4]));string prefix=argv[5];
 auto symmetric=[&](){vector<int>v;do{v.clear();vector<int>ix(blocks.size());for(int i=0;i<(int)ix.size();i++)ix[i]=i;shuffle(ix.begin(),ix.end(),rng);for(int i:ix)if(v.size()+blocks[i].size()<=size_t(r)){v.insert(v.end(),blocks[i].begin(),blocks[i].end());if(v.size()==size_t(r))break;}}while(v.size()!=size_t(r));return v;};
 bool possible=false;vector<bool>dp(r+1);dp[0]=true;for(auto&b:blocks)for(int j=r;j>=int(b.size());j--)dp[j]=dp[j]||dp[j-b.size()];possible=dp[r];if(!possible)return 2;
 auto random_state=[&](){State x;x.a=symmetric();x.b=symmetric();x.s={0};while(x.s.size()<size_t(sdeg)){int t=rng()%q;if(find(x.s.begin(),x.s.end(),t)==x.s.end())x.s.push_back(t);}return x;};
 auto evaluate=[&](const State&x){int miss=0;for(int side=0;side<2;side++){array<unsigned char,256>seen{};array<int,256>queue{},depth{};queue[0]=side*q;seen[queue[0]]=1;int end=1;for(int head=0;head<end;head++){if(depth[head]==D)continue;int u=queue[head],g=u%q,j=u/q;auto add=[&](int v){if(!seen[v]){seen[v]=1;queue[end]=v;depth[end++]=depth[head]+1;}};for(int t:(j?x.b:x.a))add(j*q+mul[g][t]);for(int t:x.s)add(j?mul[g][inv[t]]:q+mul[g][t]);}miss+=2*q-end;}return miss;};
 auto t0=chrono::steady_clock::now();auto sec=[&](){return chrono::duration<double>(chrono::steady_clock::now()-t0).count();};
 auto save=[&](const State&x,int score,unsigned long long steps){ofstream j(prefix+".json");j<<"{\"group_order\":"<<q<<",\"n\":"<<2*q<<",\"internal_degree\":"<<r<<",\"diameter_target\":"<<D<<",\"representative_missing_sum\":"<<score<<",\"implied_bad_unordered_pairs\":"<<q*score/2<<",\"steps\":"<<steps<<",\"seconds_at_best\":"<<sec();auto arr=[&](string key,const vector<int>&v){j<<",\""<<key<<"\":[";for(size_t i=0;i<v.size();i++)j<<(i?",":"")<<v[i];j<<"]";};arr("A",x.a);arr("B",x.b);arr("S",x.s);j<<"}\n";
 set<pair<int,int>>edges;auto add=[&](int a,int b){if(a>b)swap(a,b);edges.emplace(a,b);};for(int g=0;g<q;g++){for(int a:x.a)add(g,mul[g][a]);for(int b:x.b)add(q+g,q+mul[g][b]);for(int s:x.s)add(g,q+mul[g][s]);}ofstream e(prefix+".edges");e<<2*q<<" "<<edges.size()<<"\n";for(auto [a,b]:edges)e<<a<<" "<<b<<"\n";};
 signal(SIGINT,stop_handler);signal(SIGTERM,stop_handler);
 State cur=random_state(),best_state=cur;int score=evaluate(cur),best=score;unsigned long long step=0;save(cur,best,step);cout<<"initial "<<best<<endl;
 while(best&&!stop_requested&&sec()<limit){++step;State nxt=cur;int part=rng()%(sdeg>1?3:2);if(part==0)nxt.a=symmetric();else if(part==1)nxt.b=symmetric();else{int k=1+rng()%(sdeg-1),v;do{v=rng()%q;}while(find(nxt.s.begin(),nxt.s.end(),v)!=nxt.s.end());nxt.s[k]=v;}int ns=evaluate(nxt);double temp=2.5*pow(.06,double(step%30000)/30000.);if(ns<=score||generate_canonical<double,53>(rng)<exp(double(score-ns)/temp)){cur=nxt;score=ns;}if(score<best){best=score;best_state=cur;save(cur,best,step);cout<<"best "<<best<<" step "<<step<<" sec "<<sec()<<endl;}if(step%30000==0){cur=(step%90000==0)?random_state():best_state;score=evaluate(cur);}}
 ofstream t(prefix+".terminal.json");t<<"{\"status\":\""<<(best==0?"CANDIDATE_COVERED":stop_requested?"STOPPED":"BUDGET_EXHAUSTED")<<"\",\"steps\":"<<step<<",\"seconds\":"<<sec()<<",\"best_missing_sum\":"<<best<<"}\n";cout<<"terminal "<<best<<" steps "<<step<<" seconds "<<sec()<<endl;
}
