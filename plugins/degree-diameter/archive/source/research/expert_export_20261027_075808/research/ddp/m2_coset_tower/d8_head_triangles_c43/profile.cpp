#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int P,K,M,D,A,L,B,N,NC,NS;
vector<int> powers,inv,orbit;
vector<vector<int>> aa,act;
vector<array<int,8>> adj;
vector<int> deg,dist,que;
using Gen=vector<int>;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int gp(int g,int h){return aa[g%A][act[g/A][h%A]]+A*((g/A+h/A)%K);}
int ainv(int a){return (P-a%P)%P+P*((3-a/P)%3);}
void init(){
 A=3*P;L=A*K;B=A*M;N=L+B+A;
 powers.resize(K);powers[0]=1;for(int i=1;i<K;i++)powers[i]=powers[i-1]*3%P;
 auto sp=powers;sort(sp.begin(),sp.end());for(int x=0;x<K;x++)assert(sp[x]==x+1);
 aa.assign(A,vector<int>(A));act.assign(K,vector<int>(A));inv.resize(L);
 for(int x=0;x<A;x++)for(int y=0;y<A;y++)aa[x][y]=(x%P+y%P)%P+P*((x/P+y/P)%3);
 for(int i=0;i<K;i++)for(int x=0;x<A;x++)act[i][x]=powers[i]*(x%P)%P+P*(x/P);
 for(int g=0;g<L;g++){int j=(K-g/A)%K;inv[g]=ainv(act[j][g%A])+A*j;assert(gp(g,inv[g])==0&&gp(inv[g],g)==0);}
 orbit.assign(A,-1);int idx=0;
 for(int w=0;w<3;w++){
  orbit[P*w]=idx++;
  for(int x=1;x<P;x++)if(orbit[x+P*w]<0){for(int i=0;i<K;i+=M)orbit[powers[i]*x%P+P*w]=idx;idx++;}
 }
 assert(idx==3*(M+1));
 adj.resize(N);deg.resize(N);dist.resize(N);que.resize(N);
}
void edge(int u,int v){assert(u!=v&&deg[u]<D&&deg[v]<D);adj[u][deg[u]++]=v;adj[v][deg[v]++]=u;}
void build(const Gen&S){
 fill(deg.begin(),deg.end(),0);
 for(int g=0;g<L;g++){
  for(int s:S){int h=gp(g,s);if(g<h)edge(g,h);}
  edge(g,L+g%A+A*((g/A)%M));
 }
 for(int z=0;z<B;z++)edge(L+z,L+B+z%A);
 for(int x=0;x<P;x++)for(int w=0;w<3;w++)edge(L+B+x+P*w,L+B+x+P*((w+1)%3));
 for(int g=0;g<N;g++){assert(deg[g]==D);auto row=adj[g];sort(row.begin(),row.begin()+D);assert(adjacent_find(row.begin(),row.begin()+D)==row.begin()+D);}
}
vector<uint32_t> bbmask(const Gen&S){
 uint32_t p=0;for(int w=0;w<3;w++)p|=1U<<orbit[P*w];
 for(int s:S)p|=1U<<orbit[s%A];
 vector<uint32_t> masks(M,p);
 for(int j=0;j<M;j++)for(int s:S)masks[j]|=1U<<orbit[act[(j-s/A+K)%K][s%A]];
 auto ins=[&](int g){masks[g/A%M]|=1U<<orbit[g%A];};ins(0);
 for(int a:S){ins(a);for(int b:S)if(b!=inv[a]){int v=gp(a,b);ins(v);for(int c:S)if(c!=inv[b])ins(gp(v,c));}}
 return masks;
}
int bbmissing(const vector<uint32_t>&masks){
 int n=0;for(auto m:masks)for(int x=0;x<A;x++)if(!(m&(1U<<orbit[x])))n++;
 assert(n%(K/M)==0);return n;
}
struct Score{array<int,3> miss{},ecc{};array<array<int,3>,3> layer{};long long bad=0;};
Score score(const vector<uint32_t>&mask,bool full){
 Score z;array<int,3>roots{0,L,L+B};
 for(int t=0;t<3;t++){
  fill(dist.begin(),dist.end(),-1);int front=0,end=1;que[0]=roots[t];dist[roots[t]]=0;
  while(front<end){int v=que[front++];if(!full&&dist[v]==5)continue;for(int j=0;j<D;j++){int w=adj[v][j];if(dist[w]<0){dist[w]=dist[v]+1;que[end++]=w;}}}
  for(int v=0;v<N;v++){
   if(dist[v]<0||dist[v]>5){z.miss[t]++;z.layer[t][v<L?0:v<L+B?1:2]++;}
   if(dist[v]>=0)z.ecc[t]=max(z.ecc[t],dist[v]);
  }
  if(full&&end!=N)z.ecc[t]=-1;
  if(t==1)for(int j=0;j<M;j++)for(int x=0;x<A;x++){
   bool want=(mask[j]>>orbit[x])&1;
   assert(want==(dist[L+x+A*j]>=0&&dist[L+x+A*j]<=5));
  }
 }
 assert(z.layer[2][2]==0&&z.layer[1][1]==bbmissing(mask));
 z.bad=(1LL*L*z.miss[0]+1LL*B*z.miss[1]+1LL*A*z.miss[2])/2;return z;
}
template<class T>void list(ostream&o,const T&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<x;}o<<']';}
void rowout(ostream&o,const Gen&S,const Score&z,const vector<uint32_t>&mask,int cur,int stratum,int local){
 o<<"{\"cursor\":"<<cur<<",\"stratum\":"<<stratum<<",\"stratum_cursor\":"<<local<<",\"S\":";list(o,S);
 o<<",\"root_missing\":";list(o,z.miss);o<<",\"root_missing_by_target_layer\":[";
 for(int i=0;i<3;i++){if(i)o<<',';list(o,z.layer[i]);}
 o<<"],\"BB_missing\":"<<z.layer[1][1]<<",\"BB_orbit_masks\":";list(o,mask);
 o<<",\"bad_unordered_pairs\":"<<z.bad<<'}';
}
void save(const string&base,const Gen&S,const Score&z,const vector<uint32_t>&mask,int cur,int st,int local){
 ofstream o(base+".json");rowout(o,S,z,mask,cur,st,local);o<<'\n';
 ofstream f(base+".edges");f<<N<<' '<<N*D/2<<'\n';for(int g=0;g<N;g++)for(int j=0;j<D;j++)if(g<adj[g][j])f<<g<<' '<<adj[g][j]<<'\n';
}
struct Stat{
 int count=0,bbzero=0,joint=0,minbb=INT_MAX;long long best=LLONG_MAX;
 array<int,3>mins{INT_MAX,INT_MAX,INT_MAX},zeros{};array<array<int,3>,3>lm,lz{};
 Stat(){for(auto&r:lm)r.fill(INT_MAX);}
 void add(const Score&z){
  count++;best=min(best,z.bad);minbb=min(minbb,z.layer[1][1]);if(!z.layer[1][1])bbzero++;if(!z.miss[1]&&!z.miss[2])joint++;
  for(int i=0;i<3;i++){mins[i]=min(mins[i],z.miss[i]);if(!z.miss[i])zeros[i]++;for(int j=0;j<3;j++){lm[i][j]=min(lm[i][j],z.layer[i][j]);if(!z.layer[i][j])lz[i][j]++;}}
 }
};
void stats(ostream&o,const Stat&s){
 o<<"{\"scored\":"<<s.count<<",\"BB_zero\":"<<s.bbzero<<",\"minimum_BB_missing\":"<<s.minbb<<",\"head_and_block_zero\":"<<s.joint<<",\"minimum_bad_pairs\":"<<s.best<<",\"root_minimum_missing\":";list(o,s.mins);o<<",\"root_zero_counts\":";list(o,s.zeros);
 o<<",\"layer_minimum_missing\":[";for(int i=0;i<3;i++){if(i)o<<',';list(o,s.lm[i]);}o<<"],\"layer_zero_counts\":[";for(int i=0;i<3;i++){if(i)o<<',';list(o,s.lz[i]);}o<<"]}";
}
int main(int argc,char**argv){
 assert(argc==3);string base=argv[1];double budget=stod(argv[2]),start=cpu();
 ifstream in(base+"/profile.inputs.txt");in>>P>>K>>M>>D>>NC>>NS;assert(K==P-1&&D-1==K/M&&M==D-2);init();
 Stat all;vector<Stat>per(NC);int cur=0;long long best=LLONG_MAX;double bt=0,ft=0,mt=0;string status="PROFILE_COMPLETE";
 ofstream rows(base+"/profile.results.jsonl");
 for(;cur<NS;cur++){
  if(cpu()-start>=budget){status="CPU_LIMIT";break;}
  int st,local;in>>st>>local;Gen S(D-1);for(int&g:S)in>>g;assert(in);
  assert(is_sorted(S.begin(),S.end())&&adjacent_find(S.begin(),S.end())==S.end()&&S.front()>0);
  for(int g:S)assert(binary_search(S.begin(),S.end(),inv[g]));
  double t=cpu();auto masks=bbmask(S);mt+=cpu()-t;
  t=cpu();build(S);bt+=cpu()-t;
  t=cpu();auto z=score(masks,cur==0);ft+=cpu()-t;
  all.add(z);per[st].add(z);rowout(rows,S,z,masks,cur,st,local);rows<<'\n';
  if(cur==0){
   save(base+"/preflight",S,z,masks,cur,st,local);
   ofstream check(base+"/preflight.check.json");check<<"{\"all_BB_targets_match_actual_BFS\":true,\"targets_checked\":"<<B<<",\"actual_complete_root_BFS\":3,\"root_eccentricities\":";list(check,z.ecc);check<<"}\n";
   cout<<"FIRST_SAMPLE p="<<P<<" roots="<<z.miss[0]<<','<<z.miss[1]<<','<<z.miss[2]<<" BB="<<z.layer[1][1]<<endl;
  }
  if(z.bad<best){best=z.bad;save(base+"/profile.best",S,z,masks,cur,st,local);cout<<"best p="<<P<<" cursor="<<cur<<" bad="<<best<<" BB="<<z.layer[1][1]<<endl;}
  if(!z.bad){status="D5_CANDIDATE";cur++;break;}
 }
 ofstream out(base+"/profile.terminal.json");out<<setprecision(10)<<"{\"status\":\""<<status<<"\",\"p\":"<<P<<",\"n\":"<<N<<",\"degree\":"<<D<<",\"planned_samples\":"<<NS<<",\"next_cursor\":"<<cur<<",\"cpu_seconds\":"<<cpu()-start<<",\"BB_diagnostic_cpu_seconds\":"<<mt<<",\"build_cpu_seconds\":"<<bt<<",\"BFS_cpu_seconds\":"<<ft<<",\"every_sample_all_BB_targets_matched_BFS\":true,\"BB_targets_checked\":"<<1LL*cur*B<<",\"BB_used_to_skip_BFS\":false,\"stats\":";stats(out,all);out<<",\"per_stratum\":[";for(int i=0;i<NC;i++){if(i)out<<',';stats(out,per[i]);}out<<"]}\n";
 cout<<status<<" p="<<P<<" samples="<<cur<<" CPU="<<cpu()-start<<" best="<<best<<" BBzero="<<all.bbzero<<endl;
}
