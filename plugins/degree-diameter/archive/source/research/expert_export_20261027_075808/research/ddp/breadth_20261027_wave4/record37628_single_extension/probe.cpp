#include <bits/stdc++.h>
using namespace std;
using U64=uint64_t;
const int N=37628,W=(N+63)/64;
clock_t began;
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}
bool limited=false;
int main(int argc,char**argv){
 began=clock(); assert(argc==3);ifstream in(argv[1]);string line;
 set<pair<int,int>> edges;vector<bool> rows(N,false);
 while(getline(in,line)){
  if(line.empty()||line[0]=='#')continue;
  stringstream ss(line);int u,v;ss>>u;assert(0<=u&&u<N&&!rows[u]);rows[u]=true;
  while(ss>>v){assert(0<=v&&v<N&&u!=v);edges.insert(minmax(u,v));}
 }
 assert(all_of(rows.begin(),rows.end(),[](bool x){return x;}));assert(edges.size()==205296);
 vector<vector<int>> adj(N);for(auto [u,v]:edges){adj[u].push_back(v);adj[v].push_back(u);}
 vector<int> freev;for(int u=0;u<N;u++){assert(adj[u].size()<=11);if(adj[u].size()<11)freev.push_back(u);}
 assert(freev.size()==2504);int F=freev.size();
 vector<U64> balls((size_t)F*W,0);vector<int> seen(N,0),que(N),sizes(F);
 for(int k=0;k<F;k++){
  int head=0,tail=1;que[0]=freev[k];seen[que[0]]=k+1;
  for(int depth=0;depth<4;depth++){
   int stop=tail;
   while(head<stop){int u=que[head++];for(int v:adj[u])if(seen[v]!=k+1){seen[v]=k+1;que[tail++]=v;}}
  }
  U64* b=&balls[(size_t)k*W];for(int j=0;j<tail;j++)b[que[j]>>6]|=U64(1)<<(que[j]&63);
  sizes[k]=tail;
  if(k%2048==0)cerr<<"balls "<<k<<"/"<<F<<" CPU "<<cpu()<<"\n";
 }
 double ballcpu=cpu();
 vector<int> pins;
 auto pin=[&](function<bool(int)>ok){int best=-1;for(int k=0;k<F;k++)if(ok(freev[k])&&find(pins.begin(),pins.end(),k)==pins.end())if(best<0||sizes[k]>sizes[best])best=k;if(best<0){for(int k=0;k<F;k++)if(find(pins.begin(),pins.end(),k)==pins.end())if(best<0||sizes[k]>sizes[best])best=k;}if(best>=0)pins.push_back(best);};
 pin([](int u){return true;});
 for(int deg:{6,7,8,9,10})pin([&](int u){return (int)adj[u].size()==deg;});
 pin([](int u){return u>=37622;});
 pin([](int u){return u<37622;});
 assert(pins.size()==8);
 U64 lastMask=(N%64)?(U64(1)<<(N%64))-1:~U64(0);
 auto uncovered=[&](const vector<int>&sel,int skip=-1){vector<U64> u(W,~U64(0));u.back()=lastMask;for(int i=0;i<(int)sel.size();i++)if(i!=skip){auto b=&balls[(size_t)sel[i]*W];for(int j=0;j<W;j++)u[j]&=~b[j];}return u;};
 auto count=[&](const vector<U64>&u){int c=0;for(auto x:u)c+=__builtin_popcountll(x);return c;};
 long long scores=0;
 auto pick=[&](const vector<U64>&u,const vector<int>&sel,int allowed){
  vector<int> active;for(int w=0;w<W;w++)if(u[w])active.push_back(w);
  int best=-1,score=-1;
  for(int k=0;k<F;k++){
   if(k!=allowed&&find(sel.begin(),sel.end(),k)!=sel.end())continue;
   auto b=&balls[(size_t)k*W];int c=0;for(int w:active)c+=__builtin_popcountll(b[w]&u[w]);scores++;
   if(c>score){score=c;best=k;}
   if((k&2047)==0&&cpu()>75){limited=true;break;}
  }
  return best;
 };
 vector<int> bestsel;int bestmiss=N,completed=0;vector<int> profileMiss;
 for(int pinid:pins){
  if(limited)break;
  vector<int> sel={pinid};
  while(sel.size()<11&&!limited){auto u=uncovered(sel);if(count(u)==0)break;int k=pick(u,sel,-1);if(k<0)break;sel.push_back(k);}
  auto u=uncovered(sel);int miss=count(u);
  if(miss<bestmiss){bestmiss=miss;bestsel=sel;}
  if(miss==0){profileMiss.push_back(miss);completed++;break;}
  // Exactly one coordinate pass; accept strict coverage improvements only.
  for(int i=0;i<(int)sel.size()&&!limited;i++){
   auto base=uncovered(sel,i);int k=pick(base,sel,sel[i]);if(k<0)break;
   int old=sel[i];sel[i]=k;auto next=uncovered(sel);int nextmiss=count(next);
   if(nextmiss>=miss)sel[i]=old;else{miss=nextmiss;if(miss<bestmiss){bestmiss=miss;bestsel=sel;}if(!miss)break;}
  }
  profileMiss.push_back(miss);completed++;
  cerr<<"profile "<<completed<<" missing "<<miss<<" best "<<bestmiss<<" CPU "<<cpu()<<"\n";
  if(bestmiss==0)break;
 }
 auto missing=uncovered(bestsel);ofstream out(argv[2]);
 out<<"{\"status\":\""<<(bestmiss==0?"HIT_RADIUS4_DOMINATING_NEIGHBORS":limited?"CPU_LIMIT_PARTIAL_PROFILE":"FINITE_8_PIN_PROFILE_FAILED")<<"\",\"base_vertices\":"<<N<<",\"base_edges\":"<<edges.size()<<",\"eligible_vertices\":"<<F<<",\"balls_computed\":"<<F<<",\"radius\":4,\"neighbors_cap\":11,\"profiles_planned\":8,\"profiles_completed\":"<<completed<<",\"one_coordinate_pass_per_profile\":true,\"candidate_scores\":"<<scores<<",\"best_uncovered_vertices\":"<<bestmiss<<",\"ball_CPU_seconds\":"<<ballcpu<<",\"total_CPU_seconds\":"<<cpu()<<",\"CPU_internal_limit\":75,\"CPU_limit_reached\":"<<(limited?"true":"false")<<",\"workers\":1,\"new_graph_generated\":false,\"pins\":[";
 for(int i=0;i<(int)pins.size();i++){if(i)out<<',';out<<freev[pins[i]];}out<<"],\"profile_final_misses\":[";
 for(int i=0;i<(int)profileMiss.size();i++){if(i)out<<',';out<<profileMiss[i];}out<<"],\"best_neighbors\":[";
 for(int i=0;i<(int)bestsel.size();i++){if(i)out<<',';out<<freev[bestsel[i]];}out<<"],\"uncovered_vertices\":[";
 bool comma=false;for(int v=0;v<N;v++)if((missing[v>>6]>>(v&63))&1){if(comma)out<<',';comma=true;out<<v;}out<<"]}\n";
}
