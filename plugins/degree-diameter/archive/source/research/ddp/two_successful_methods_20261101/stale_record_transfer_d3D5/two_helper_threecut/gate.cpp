#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
using U=__uint128_t;
array<U,72> adj,original;
const U OLD=(U(1)<<70)-1,ALL=(U(1)<<72)-1;
U reach(int root,int radius){
 U seen=U(1)<<root,front=seen;
 for(int d=0;d<radius&&front;d++){
  U next=0; uint64_t lo=uint64_t(front),hi=uint64_t(front>>64);
  while(lo){int v=__builtin_ctzll(lo);lo&=lo-1;next|=adj[v];}
  while(hi){int v=64+__builtin_ctzll(hi);hi&=hi-1;next|=adj[v];}
  front=next&~seen;seen|=next;
 }
 return seen;
}
int first(U x){uint64_t lo=uint64_t(x);return lo?__builtin_ctzll(lo):64+__builtin_ctzll(uint64_t(x>>64));}
double cpu(){struct rusage r;getrusage(RUSAGE_SELF,&r);return r.ru_utime.tv_sec+r.ru_utime.tv_usec*1e-6+r.ru_stime.tv_sec+r.ru_stime.tv_usec*1e-6;}
void printv(const vector<int>&v){cout<<'[';for(size_t k=0;k<v.size();k++){if(k)cout<<',';cout<<v[k];}cout<<']';}
int main(int argc,char**argv){
 if(argc!=4)return 2;
 ifstream in(argv[1]);int n,m;in>>n>>m;if(n!=70||m!=105)return 3;
 vector<pair<int,int>> E;int a,b;
 while(in>>a>>b){E.push_back({a,b});adj[a]|=U(1)<<b;adj[b]|=U(1)<<a;}
 if(E.size()!=105)return 4;original=adj;
 // New radius4 route diagnostic only; not a source diameter/validity rerun.
 array<U,70> ball4;map<int,int> ballhist;
 for(int v=0;v<70;v++){ball4[v]=reach(v,4);ballhist[__builtin_popcountll(uint64_t(ball4[v]))+__builtin_popcountll(uint64_t(ball4[v]>>64))]++;}
 uint64_t matchings=0,configs=0,failA=0,failB=0,failPair=0,failOld=0,sourceCoverBoth=0,sourceCoverOne=0,sourceCoverNeither=0,passHelpers=0;
 bool complete=true,hit=false,stop=false;vector<int> bestcuts,bestA,bestB;pair<int,int> firstold={-1,-1};vector<int> firstoldcuts,firstoldA,firstoldB;
 double limit=atof(argv[3]);
 for(int i=0;i<105&&!stop;i++)for(int j=i+1;j<105&&!stop;j++){
  auto [a0,a1]=E[i];auto[b0,b1]=E[j];if(a0==b0||a0==b1||a1==b0||a1==b1)continue;
  for(int k=j+1;k<105&&!stop;k++){
   auto[c0,c1]=E[k];if(c0==a0||c0==a1||c0==b0||c0==b1||c1==a0||c1==a1||c1==b0||c1==b1)continue;
   if((matchings&255)==0&&cpu()>limit){complete=false;stop=true;break;}
   matchings++;
   vector<int> pins={a0,a1,b0,b1,c0,c1};sort(pins.begin(),pins.end());
   for(int mask=0;mask<64&&!stop;mask++){
    if(!(mask&1)||__builtin_popcount((unsigned)mask)!=3)continue;
    configs++;vector<int>A,B;
    for(int h=0;h<6;h++)((mask>>h)&1?A:B).push_back(pins[h]);
    U ra=ball4[A[0]]|ball4[A[1]]|ball4[A[2]],rb=ball4[B[0]]|ball4[B[1]]|ball4[B[2]];
    if(ra==OLD&&rb==OLD)sourceCoverBoth++;else if(ra==OLD||rb==OLD)sourceCoverOne++;else sourceCoverNeither++;
    // Freeze original simple old graph, delete the selected matching, add the two helper stars.
    adj=original;
    for(int e:{i,j,k}){auto[u,v]=E[e];adj[u]&=~(U(1)<<v);adj[v]&=~(U(1)<<u);}
    for(int v:A){adj[70]|=U(1)<<v;adj[v]|=U(1)<<70;}
    for(int v:B){adj[71]|=U(1)<<v;adj[v]|=U(1)<<71;}
    U sa=reach(70,5);
    if((sa&OLD)!=OLD){failA++;continue;}
    if(!(sa&(U(1)<<71))){failPair++;continue;}
    U sb=reach(71,5);
    if((sb&OLD)!=OLD){failB++;continue;}
    passHelpers++;
    bool oldok=true;
    for(int u=0;u<70;u++){
     U miss=OLD&~reach(u,5);
     if(miss){oldok=false;failOld++;if(firstold.first<0){firstold={u,first(miss)};firstoldcuts={i,j,k};firstoldA=A;firstoldB=B;}break;}
    }
    if(oldok){hit=true;complete=false;stop=true;bestcuts={i,j,k};bestA=A;bestB=B;}
   }
  }
 }
 ofstream graph;
 if(hit){
  graph.open(string(argv[2])+"/graph_d3_D5_n72.edges");graph<<"72 108\n";
  for(int u=0;u<72;u++)for(int v=u+1;v<72;v++)if(adj[u]&(U(1)<<v))graph<<u<<' '<<v<<'\n';
 }
 cout<<"{\"status\":\""<<(hit?"FOUND72":complete?"EXHAUSTIVE_FIXED_RULE_NO72":"UNKNOWN_CPU_BUDGET")<<"\",\"complete\":"<<(complete?"true":"false")<<",\"hit\":"<<(hit?"true":"false")<<",\"matchings\":"<<matchings<<",\"configurations\":"<<configs<<",\"first_failure_counts\":{\"helper70_old_R5\":"<<failA<<",\"helper_pair_R5\":"<<failPair<<",\"helper71_old_R5\":"<<failB<<",\"old_old_R5\":"<<failOld<<"},\"both_helpers_all_old_and_each_other_PASS\":"<<passHelpers<<",\"original_source_R4_diagnostic\":{\"both_triples_cover\":"<<sourceCoverBoth<<",\"one_triple_covers\":"<<sourceCoverOne<<",\"neither_covers\":"<<sourceCoverNeither<<",\"ball_sizes\":{";
 bool comma=false;for(auto[s,c]:ballhist){if(comma)cout<<',';comma=true;cout<<'"'<<s<<"\":"<<c;}cout<<"}},\"first_old_failure\":{\"pair\":["<<firstold.first<<','<<firstold.second<<"],\"cut_edge_ids\":";printv(firstoldcuts);cout<<",\"pins70\":";printv(firstoldA);cout<<",\"pins71\":";printv(firstoldB);cout<<"},\"hit_cut_edge_ids\":";printv(bestcuts);cout<<",\"hit_pins70\":";printv(bestA);cout<<",\"hit_pins71\":";printv(bestB);cout<<",\"gate_CPU_seconds\":"<<setprecision(12)<<cpu()<<"}\n";
}
