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
constexpr int Q=11,J=10,A=363,K=110,L=39930,B=3630,N=43923,D=12;
using Gen=array<int,11>;
static int pw[J],kp[K][K],ki[K],action[K][A],add[A][A],neg[A],ginv[L];
static array<array<int,D>,N>adj;
static array<int,N>deg,dist,que;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int enc(int u,int v,int w){return ((u%Q)+Q)%Q+Q*(((v%Q)+Q)%Q)+Q*Q*(((w%3)+3)%3);}
int gp(int g,int h){return add[g%A][action[g/A][h%A]]+A*kp[g/A][h/A];}
void init(){
 pw[0]=1;for(int j=1;j<J;j++)pw[j]=2*pw[j-1]%Q;
 for(int x=0;x<A;x++){
  int u=x%Q,v=x/Q%Q,w=x/(Q*Q);neg[x]=enc(-u,-v,-w);
  for(int y=0;y<A;y++)add[x][y]=enc(u+y%Q,v+y/Q%Q,w+y/(Q*Q));
 }
 for(int k=0;k<K;k++){
  int b=k%Q,j=k/Q;j%=J;
  ki[k]=enc(-pw[(J-2*j%J)%J]*b,0,0)+Q*((J-j)%J);
  for(int l=0;l<K;l++)kp[k][l]=(b+pw[2*j%J]*(l%Q))%Q+Q*((j+l/Q)%J);
  for(int x=0;x<A;x++)action[k][x]=enc(pw[3*j%J]*(x%Q)+b*pw[j]*(x/Q%Q),pw[j]*(x/Q%Q),x/(Q*Q));
 }
 for(int k=0;k<K;k++){assert(kp[k][ki[k]]==0&&kp[ki[k]][k]==0);for(int l=0;l<K;l++)for(int x=0;x<A;x++)assert(action[kp[k][l]][x]==action[k][action[l][x]]);}
 for(int g=0;g<L;g++){int ik=ki[g/A];ginv[g]=neg[action[ik][g%A]]+A*ik;assert(gp(g,ginv[g])==0&&gp(ginv[g],g)==0);}
}
struct Bits{array<uint64_t,6>w{};void put(int x){w[x/64]|=1ULL<<(x%64);}void merge(const Bits&b){for(int i=0;i<6;i++)w[i]|=b.w[i];}bool has(int x)const{return (w[x/64]>>(x%64))&1;}int count()const{int n=0;for(auto z:w)n+=__builtin_popcountll(z);return n;}};
static array<Bits,A>sat;
void init_sat(){for(int x=0;x<A;x++)for(int b=0;b<Q;b++)sat[x].put(action[b][x]);}
using Masks=array<Bits,J>;
Masks masks(const Gen&S){
 Masks M;Bits p;p.put(0);p.put(121);p.put(242);for(int s:S)p.merge(sat[s%A]);
 for(int j=0;j<J;j++){M[j]=p;for(int s:S){int js=s/A/Q;M[j].merge(sat[action[Q*((j-js+J)%J)][s%A]]);}}
 auto insert=[&](int g){M[g/A/Q].merge(sat[g%A]);};insert(0);
 for(int a:S){insert(a);for(int b:S)if(b!=ginv[a]){int v=gp(a,b);insert(v);for(int c:S)if(c!=ginv[b])insert(gp(v,c));}}
 return M;
}
int projection(int g){int x=g%A;return x/Q%Q+Q*(x/(Q*Q))+3*Q*(g/A/Q);}
int qprod(int g,int h){return (g%Q+pw[g/(3*Q)]*(h%Q))%Q+Q*((g/Q%3+h/Q%3)%3)+3*Q*((g/(3*Q)+h/(3*Q))%J);}
array<uint64_t,J> quotient_masks(const Gen&S){
 array<uint64_t,J>M{};array<int,11> T;for(int i=0;i<11;i++)T[i]=projection(S[i]);
 uint64_t p=(1ULL<<0)|(1ULL<<11)|(1ULL<<22);for(int s:T)p|=1ULL<<(s%(3*Q));
 for(int j=0;j<J;j++){M[j]=p;for(int s:T)M[j]|=1ULL<<(pw[(j-s/(3*Q)+J)%J]*(s%Q)%Q+Q*(s/Q%3));}
 auto ins=[&](int g){M[g/(3*Q)]|=1ULL<<(g%(3*Q));};ins(0);
 // Projected collisions and projected identity remain valid letters; no rejection or label merging is needed.
 for(int a:T){ins(a);for(int b:T){int v=qprod(a,b);ins(v);for(int c:T)ins(qprod(v,c));}}
 return M;
}
struct Coverage{int original=0,quotient=0,axis=0,offaxis=0;};
Coverage coverage(const Masks&M,const array<uint64_t,J>&QM){
 Coverage z;
 for(int j=0;j<J;j++){
  z.quotient+=3*Q-__builtin_popcountll(QM[j]);uint64_t projected=0;
  for(int x=0;x<A;x++)if(M[j].has(x))projected|=1ULL<<(x/Q%Q+Q*(x/(Q*Q)));else{z.original++;if(x/Q%Q==0)z.axis++;else z.offaxis++;}
  assert(projected==QM[j]);
 }
 assert(z.original>=Q*z.quotient);
 if(!z.quotient)assert(z.offaxis==0&&z.original<=330);
 return z;
}
void edge(int u,int v){assert(u!=v&&deg[u]<D&&deg[v]<D);adj[u][deg[u]++]=v;adj[v][deg[v]++]=u;}
void build(const Gen&S){
 deg.fill(0);
 for(int g=0;g<L;g++){for(int s:S){int h=gp(g,s);if(g<h)edge(g,h);}edge(g,L+g%A+A*(g/A/Q));}
 for(int z=0;z<B;z++)edge(L+z,L+B+z%A);
 for(int uv=0;uv<Q*Q;uv++)for(int w=0;w<3;w++)edge(L+B+uv+Q*Q*w,L+B+uv+Q*Q*((w+1)%3));
 for(int g=0;g<N;g++){assert(deg[g]==D);auto row=adj[g];sort(row.begin(),row.end());assert(adjacent_find(row.begin(),row.end())==row.end());}
}
struct Score{array<int,3>miss{},ecc{};array<array<int,3>,3>layer{};long long bad=0;};
Score score(const Masks&M){
 Score z;array<int,3>roots{0,L,L+B};
 for(int t=0;t<3;t++){
  dist.fill(-1);int front=0,end=1;que[0]=roots[t];dist[roots[t]]=0;
  while(front<end){int v=que[front++];for(int w:adj[v])if(dist[w]<0){dist[w]=dist[v]+1;que[end++]=w;}}
  assert(end==N);
  for(int v=0;v<N;v++){z.ecc[t]=max(z.ecc[t],dist[v]);if(dist[v]>5){z.miss[t]++;z.layer[t][v<L?0:v<L+B?1:2]++;}}
  if(t==1)for(int j=0;j<J;j++)for(int x=0;x<A;x++)assert(M[j].has(x)==(dist[L+x+A*j]<=5));
 }
 assert(z.layer[2][2]==0);z.bad=(1LL*L*z.miss[0]+1LL*B*z.miss[1]+1LL*A*z.miss[2])/2;return z;
}
template<class T>void list(ostream&o,const T&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<x;}o<<']';}
void outrow(ostream&o,const Gen&S,const Score&z,const Coverage&c,const Masks&M,const array<uint64_t,J>&QM,int cell,int t){
 o<<"{\"cell_id\":"<<cell<<",\"cross_inverse_pairs\":"<<t<<",\"S\":";list(o,S);o<<",\"root_missing\":";list(o,z.miss);o<<",\"root_eccentricities\":";list(o,z.ecc);o<<",\"root_missing_by_target_layer\":[";
 for(int i=0;i<3;i++){if(i)o<<',';list(o,z.layer[i]);}o<<"],\"bad_unordered_pairs\":"<<z.bad<<",\"quotient_BB_missing\":"<<c.quotient<<",\"original_BB_missing\":"<<c.original<<",\"original_axis_BB_missing\":"<<c.axis<<",\"original_offaxis_BB_missing\":"<<c.offaxis<<",\"quotient_BB_masks\":";list(o,QM);o<<",\"original_BB_masks_little_endian_64bit_words\":[";for(int j=0;j<J;j++){if(j)o<<',';list(o,M[j].w);}o<<"]}";
}
void save(const string&base,const Gen&S,const Score&z,const Coverage&c,const Masks&M,const array<uint64_t,J>&QM,int cell,int t){
 ofstream o(base+".json");outrow(o,S,z,c,M,QM,cell,t);o<<'\n';
 ofstream f(base+".edges");f<<N<<' '<<N*D/2<<'\n';for(int g=0;g<N;g++)for(int h:adj[g])if(g<h)f<<g<<' '<<h<<'\n';
}
struct Stat{
 int count=0,qpass=0,bbpass=0,joint=0,minq=INT_MAX,minbb=INT_MAX;long long best=LLONG_MAX;
 array<int,3>mins{N,N,N},zeros{};array<array<int,3>,3>lm,lz{};
 Stat(){for(auto&r:lm)r.fill(N);}
 void add(const Score&z,const Coverage&c){count++;qpass+=!c.quotient;bbpass+=!c.original;minq=min(minq,c.quotient);minbb=min(minbb,c.original);best=min(best,z.bad);joint+=!z.miss[1]&&!z.miss[2];for(int i=0;i<3;i++){mins[i]=min(mins[i],z.miss[i]);zeros[i]+=!z.miss[i];for(int j=0;j<3;j++){lm[i][j]=min(lm[i][j],z.layer[i][j]);lz[i][j]+=!z.layer[i][j];}}}
};
void stats(ostream&o,const Stat&s){
 o<<"{\"scored\":"<<s.count<<",\"quotient_BB_zero\":"<<s.qpass<<",\"original_BB_zero\":"<<s.bbpass<<",\"min_quotient_BB_missing\":"<<s.minq<<",\"min_original_BB_missing\":"<<s.minbb<<",\"head_and_block_zero\":"<<s.joint<<",\"minimum_bad_pairs\":"<<s.best<<",\"root_minimum_missing\":";list(o,s.mins);o<<",\"root_zero_counts\":";list(o,s.zeros);o<<",\"layer_minimum_missing\":[";for(int i=0;i<3;i++){if(i)o<<',';list(o,s.lm[i]);}o<<"],\"layer_zero_counts\":[";for(int i=0;i<3;i++){if(i)o<<',';list(o,s.lz[i]);}o<<"]}";
}
int main(int argc,char**argv){
 assert(argc==3);string base=argv[1];double budget=stod(argv[2]),start=cpu();init();init_sat();
 ifstream f(base+"/profile.inputs.txt");int n;f>>n;assert(n==192);Stat all;array<Stat,3> by_t;long long best=LLONG_MAX;int cur=0;double formula_time=0,build_time=0,bfs_time=0;string status="PROFILE_COMPLETE";
 ofstream rows(base+"/profile.results.jsonl");
 for(;cur<n;cur++){
  if(cpu()-start>=budget){status="CPU_LIMIT";break;}
  int cell,t;Gen S;f>>cell>>t;for(int&g:S)f>>g;assert(f&&cell==cur&&t>=2&&t<=4);
  auto sorted=S;sort(sorted.begin(),sorted.end());assert(sorted[0]>0&&adjacent_find(sorted.begin(),sorted.end())==sorted.end());for(int g:S)assert(binary_search(sorted.begin(),sorted.end(),ginv[g]));
  double tm=cpu();auto M=masks(S);auto QM=quotient_masks(S);auto c=coverage(M,QM);formula_time+=cpu()-tm;
  tm=cpu();build(S);build_time+=cpu()-tm;tm=cpu();auto z=score(M);bfs_time+=cpu()-tm;assert(z.layer[1][1]==c.original);
  all.add(z,c);by_t[t-2].add(z,c);outrow(rows,S,z,c,M,QM,cell,t);rows<<'\n';
  if(cur==0){save(base+"/preflight",S,z,c,M,QM,cell,t);cout<<"FIRST_ACTUAL_SAMPLE all3630 BB targets match, roots="<<z.miss[0]<<','<<z.miss[1]<<','<<z.miss[2]<<" quotientBB="<<c.quotient<<" originalBB="<<c.original<<endl;}
  if(z.bad<best){best=z.bad;save(base+"/profile.best",S,z,c,M,QM,cell,t);cout<<"best cell="<<cell<<" t="<<t<<" bad="<<best<<" roots="<<z.miss[0]<<','<<z.miss[1]<<','<<z.miss[2]<<" qBB="<<c.quotient<<" BB="<<c.original<<endl;}
  if(!z.bad){cur++;status="D5_CANDIDATE";break;}
 }
 ofstream o(base+"/profile.terminal.json");o<<setprecision(10)<<"{\"status\":\""<<status<<"\",\"planned_samples\":192,\"next_cell_id\":"<<cur<<",\"CPU_seconds\":"<<cpu()-start<<",\"formula_CPU_seconds\":"<<formula_time<<",\"build_CPU_seconds\":"<<build_time<<",\"BFS_CPU_seconds\":"<<bfs_time<<",\"all_samples_three_complete_BFS\":true,\"all_original_BB_targets_pointwise_matched\":true,\"targets_checked\":"<<1LL*cur*B<<",\"quotient_masks_match_projected_original_masks\":true,\"BB_filtering_used\":false,\"stats\":";stats(o,all);o<<",\"by_t2_t3_t4\":[";for(int i=0;i<3;i++){if(i)o<<',';stats(o,by_t[i]);}o<<"]}\n";
 cout<<status<<" samples="<<cur<<" CPU="<<cpu()-start<<" minbad="<<best<<" originalBBzero="<<all.bbpass<<endl;
}
