#include <algorithm>
#include <array>
#include <cassert>
#include <csignal>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
constexpr int P=31,A=93,M=5,B=465,L=2790,N=3348,QL=1395,QN=1953,D=7;
constexpr long long SCOPE=405000;
using Gen=array<int,6>;
array<int,30> pw;
array<int,L> inverses;
array<int,QL> qinverses;
array<array<int,A>,A> adds;
array<array<int,A>,30> acts;
array<int,A> orbit;
vector<int> nonsquares, internal_pairs;
volatile sig_atomic_t stopped=0;
void stop_handler(int){stopped=1;}
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int gp(int g,int h,int order){return adds[g%A][acts[g/A][h%A]]+A*((g/A+h/A)%order);}
int invg(int g,int order){int j=(order-g/A)%order,x=acts[j][g%A];return (P-x%P)%P+P*((3-x/P)%3)+A*j;}
struct Key{int j,yi,k,ii;long long cursor;};
Key decode_key(long long c){long long x=c;int ii=x%225;x/=225;int k=x%15;x/=15;int yi=x%15;x/=15;return {int(x),yi,k,ii,c};}
array<int,3> reps(const Key&k){return {32+A*k.j,nonsquares[k.yi]+P+A*k.k,internal_pairs[k.ii]};}
Gen qgen(const Key&k){auto r=reps(k);Gen s{};for(int i=0;i<3;i++){s[2*i]=r[i];s[2*i+1]=qinverses[r[i]];}return s;}
Gen lift(const Key&k,int bits){auto r=reps(k);Gen s{};for(int i=0;i<3;i++){int g=r[i]+QL*((bits>>i)&1);s[2*i]=g;s[2*i+1]=inverses[g];}return s;}
void legal(const Gen&s,int order){auto t=s;sort(t.begin(),t.end());assert(t[0]>0&&adjacent_find(t.begin(),t.end())==t.end());for(int g:s){int h=invg(g,order);assert(h!=g&&find(s.begin(),s.end(),h)!=s.end());}}
void init(){
 pw[0]=1;for(int i=1;i<30;i++)pw[i]=pw[i-1]*9%P;assert(pw[15]==1);
 for(int x=0;x<A;x++)for(int y=0;y<A;y++)adds[x][y]=(x%P+y%P)%P+P*((x/P+y/P)%3);
 for(int j=0;j<30;j++)for(int x=0;x<A;x++)acts[j][x]=pw[j]*(x%P)%P+P*(x/P);
 for(int g=0;g<L;g++){inverses[g]=invg(g,30);assert(gp(g,inverses[g],30)==0);}
 for(int g=0;g<QL;g++){qinverses[g]=invg(g,15);assert(gp(g,qinverses[g],15)==0);}
 for(int x=1;x<P;x++)if(find(pw.begin(),pw.begin()+15,x)==pw.begin()+15)nonsquares.push_back(x);
 for(int g=1;g<QL;g++)if((g/P)%3==0&&g%P&&g<qinverses[g])internal_pairs.push_back(g);
 assert(nonsquares.size()==15&&internal_pairs.size()==225);
 orbit.fill(-1);int next=0;
 for(int w=0;w<3;w++){
  orbit[P*w]=next++;
  for(int x=1;x<P;x++)if(orbit[x+P*w]<0){for(int j=0;j<15;j+=5)orbit[pw[j]*x%P+P*w]=next;next++;}
 }assert(next==33);
}
array<uint64_t,M> bbmask(const Gen&s,int order){
 uint64_t p=0;for(int w=0;w<3;w++)p|=1ULL<<orbit[P*w];for(int g:s)p|=1ULL<<orbit[g%A];
 array<uint64_t,M> masks; masks.fill(p);
 for(int j=0;j<M;j++)for(int g:s)masks[j]|=1ULL<<orbit[acts[(j-g/A+order)%order][g%A]];
 auto ins=[&](int g){masks[g/A%M]|=1ULL<<orbit[g%A];};ins(0);
 for(int a:s){ins(a);for(int b:s)if(b!=invg(a,order)){int ab=gp(a,b,order);ins(ab);for(int c:s)if(c!=invg(b,order))ins(gp(ab,c,order));}}
 return masks;
}
int bbmissing(const array<uint64_t,M>&m){int answer=0;for(auto x:m)answer+=3*(33-__builtin_popcountll(x));return answer;}
struct Graph{
 int order,leaves,n;vector<array<int,D>>adj;vector<int>degree,dist,queue;
 Graph(int k):order(k),leaves(A*k),n(A*k+B+A),adj(n),degree(n),dist(n),queue(n){}
 void edge(int u,int v){assert(u!=v&&degree[u]<D&&degree[v]<D);adj[u][degree[u]++]=v;adj[v][degree[v]++]=u;}
 void build(const Gen&s){
  fill(degree.begin(),degree.end(),0);
  for(int g=0;g<leaves;g++){for(int a:s){int h=gp(g,a,order);if(g<h)edge(g,h);}edge(g,leaves+g%A+A*(g/A%M));}
  for(int z=0;z<B;z++)edge(leaves+z,leaves+B+z%A);
  for(int x=0;x<P;x++)for(int w=0;w<3;w++)edge(leaves+B+x+P*w,leaves+B+x+P*((w+1)%3));
  for(int u=0;u<n;u++)assert(degree[u]==(u>=leaves&&u<leaves+B?order/M+1:D));
 }
 void bfs(int root,bool full){
  fill(dist.begin(),dist.end(),-1);int first=0,end=1;queue[0]=root;dist[root]=0;
  while(first<end){int u=queue[first++];if(!full&&dist[u]==5)continue;for(int j=0;j<degree[u];j++){int v=adj[u][j];if(dist[v]<0){dist[v]=dist[u]+1;queue[end++]=v;}}}
 }
 int miss(bool original_weights=false)const{int m=0;for(int u=0;u<n;u++)if(dist[u]<0||dist[u]>5)m+=(original_weights&&u<leaves?2:1);return m;}
 array<int,3> layer_miss()const{array<int,3>m{};for(int u=0;u<n;u++)if(dist[u]<0||dist[u]>5)m[u<leaves?0:u<leaves+B?1:2]++;return m;}
 void save_edges(const string&name)const{ofstream f(name);long long edges=0;for(int d:degree)edges+=d;f<<n<<' '<<edges/2<<'\n';for(int u=0;u<n;u++)for(int j=0;j<degree[u];j++)if(u<adj[u][j])f<<u<<' '<<adj[u][j]<<'\n';}
};
template<class T>void list(ostream&o,const T&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<x;}o<<']';}
void keyout(ostream&o,const Key&k){o<<"{\"cursor\":"<<k.cursor<<",\"anchor_j\":"<<k.j<<",\"second_field\":"<<nonsquares[k.yi]<<",\"second_j\":"<<k.k<<",\"internal_pair_index\":"<<k.ii<<",\"internal_pair_representative\":"<<internal_pairs[k.ii]<<'}';}
struct Score{array<int,3>miss{},ecc{};array<array<int,3>,3>layer{};array<map<int,long long>,3>hist;long long bad;};
Score fullscore(Graph&g){Score z;array<int,3>roots{0,g.leaves,g.leaves+B};for(int t=0;t<3;t++){g.bfs(roots[t],true);z.miss[t]=g.miss();z.layer[t]=g.layer_miss();for(int d:g.dist)z.hist[t][d]++;z.ecc[t]=z.hist[t].begin()->first<0?-1:z.hist[t].rbegin()->first;}z.bad=(1LL*L*z.miss[0]+1LL*B*z.miss[1]+1LL*A*z.miss[2])/2;return z;}
void scoreout(ostream&o,const Score&s){o<<"{\"root_missing\":";list(o,s.miss);o<<",\"root_eccentricity\":";list(o,s.ecc);o<<",\"root_missing_by_target_layer\":[";for(int t=0;t<3;t++){if(t)o<<',';list(o,s.layer[t]);}o<<"],\"bad_unordered_pairs\":"<<s.bad<<",\"root_distance_histograms\":[";for(int t=0;t<3;t++){if(t)o<<',';o<<'{';bool first=true;for(auto [d,c]:s.hist[t]){if(!first)o<<',';first=false;o<<'\"'<<d<<"\":"<<c;}o<<'}';}o<<"]}";}
void save_original(const string&base,const Key&key,int bits,Graph&g,const string&selection){
 auto s=lift(key,bits);legal(s,30);g.build(s);auto z=fullscore(g);auto masks=bbmask(s,30);assert(z.layer[1][1]==bbmissing(masks));
 ofstream o(base+".json");o<<"{\"selection\":\""<<selection<<"\",\"key\":";keyout(o,key);o<<",\"lift_bits\":"<<bits<<",\"S\":";list(o,s);o<<",\"BB_missing\":"<<bbmissing(masks)<<",\"BB_masks\":";list(o,masks);o<<",\"graph\":";scoreout(o,z);o<<"}\n";g.save_edges(base+".edges");
}
int quotient_vertex(int u){if(u<L)return u%A+A*(u/A%15);if(u<L+B)return QL+u-L;return QL+B+u-L-B;}
void calibration(const string&base){
 double begin=cpu();Key key=decode_key(0);auto qs=qgen(key),os=lift(key,0);legal(qs,15);legal(os,30);Graph q(15),g(30);q.build(qs);g.build(os);
 auto qm=bbmask(qs,15),om=bbmask(os,30);assert(qm==om);array<int,2> qweighted{},original_missing{};long long checks=0;
 for(int t=0;t<2;t++){
  q.bfs(QL+(t?B:0),true);g.bfs(L+(t?B:0),true);
  for(int v=0;v<N;v++){assert(g.dist[v]==q.dist[quotient_vertex(v)]);checks++;}
  qweighted[t]=q.miss(true);original_missing[t]=g.miss();assert(qweighted[t]==original_missing[t]);
  if(t==0)for(int j=0;j<M;j++)for(int x=0;x<A;x++){bool expected=(qm[j]>>orbit[x])&1;assert(expected==(g.dist[L+x+A*j]>=0&&g.dist[L+x+A*j]<=5));assert(expected==(q.dist[QL+x+A*j]>=0&&q.dist[QL+x+A*j]<=5));}
 }
 save_original(base+"/calibration.original",key,0,g,"the_single_calibration_graph_not_a_search_result");q.save_edges(base+"/calibration.quotient.edges");
 ofstream o(base+"/calibration.json");o<<setprecision(10)<<"{\"status\":\"COMPLETE_ONE_ORIGINAL_AND_QUOTIENT_CALIBRATION\",\"key\":";keyout(o,key);o<<",\"original_S\":";list(o,os);o<<",\"quotient_S\":";list(o,qs);o<<",\"pointwise_BH_distance_comparisons\":"<<checks<<",\"original_BH_missing\":";list(o,original_missing);o<<",\"quotient_BH_original_weight_missing\":";list(o,qweighted);o<<",\"original_and_quotient_BB_masks_equal\":true,\"all_465_BB_targets_match_BFS\":true,\"BB_missing\":"<<bbmissing(qm)<<",\"CPU_seconds\":"<<cpu()-begin<<"}\n";
 cout<<"CALIBRATION exact "<<checks<<" BH distances, all 465 BB targets, CPU="<<cpu()-begin<<endl;
}
struct Counters{long long keys=0,bbpass=0,bhscored=0,bhcomplete=0,lifts=0,leaf_bfs=0;};
void countout(ostream&o,const Counters&c){o<<"{\"quotient_keys_checked\":"<<c.keys<<",\"quotient_BB_pass\":"<<c.bbpass<<",\"quotient_keys_with_BH_BFS\":"<<c.bhscored<<",\"quotient_keys_with_complete_BH\":"<<c.bhcomplete<<",\"original_lifts_expanded\":"<<c.lifts<<",\"original_leaf_BFS_runs\":"<<c.leaf_bfs<<'}';}
int main(int argc,char**argv){assert(argc>=3);string mode=argv[1],base=argv[2];double start=cpu();init();
 if(mode=="calibrate"){calibration(base);return 0;}assert(mode=="run"&&argc==4);double limit=stod(argv[3]);signal(SIGTERM,stop_handler);signal(SIGINT,stop_handler);
 Graph quotient(15),original(30);Counters counts;map<int,long long>bbhist,bhhist;int minbb=100000,minbh=100000,bestleaf=100000;Key minbbkey{},minkey{},bestkey{};int bestbits=0;long long cursor=0;string status="COMPLETE_NO_SOLUTION";bool have_original=false;double bbtime=0,bhtime=0,lifttime=0;
 for(;cursor<SCOPE;cursor++){
  if(stopped||cpu()-start>=limit){status=stopped?"STOPPED_ON_PARENT_SIGNAL":"CPU_LIMIT";break;}
  Key key=decode_key(cursor);auto qs=qgen(key);double tic=cpu();auto masks=bbmask(qs,15);int missing=bbmissing(masks);bbtime+=cpu()-tic;counts.keys++;bbhist[missing]++;
  if(missing<minbb){minbb=missing;minbbkey=key;}
  if(missing==0){
   counts.bbpass++;tic=cpu();quotient.build(qs);quotient.bfs(QL,false);int mb=quotient.miss(true);quotient.bfs(QL+B,false);int mh=quotient.miss(true);bhtime+=cpu()-tic;counts.bhscored++;bhhist[mb+mh]++;
   if(mb+mh<minbh){minbh=mb+mh;minkey=key;}
   if(mb==0&&mh==0){
    counts.bhcomplete++;if(counts.bhcomplete==1)cout<<"FIRST_COMPLETE_BH cursor="<<cursor<<endl;
    for(int bits=0;bits<8;bits++){
     tic=cpu();auto s=lift(key,bits);original.build(s);counts.lifts++;original.bfs(0,false);counts.leaf_bfs++;int miss=original.miss();auto lm=original.layer_miss();assert(lm[1]==0&&lm[2]==0);lifttime+=cpu()-tic;
     if(miss<bestleaf){bestleaf=miss;bestkey=key;bestbits=bits;have_original=true;cout<<"BEST_LEAF cursor="<<cursor<<" bits="<<bits<<" missing="<<miss<<endl;}
     if(miss==0){status="D5_CANDIDATE";cursor++;goto done;}
    }
   }
  }
  if(cursor+1==10000){ofstream o(base+"/production.first10000.json");o<<setprecision(10)<<"{\"completed_cursor\":10000,\"CPU_seconds\":"<<cpu()-start<<",\"BB_CPU_seconds\":"<<bbtime<<",\"BH_BFS_CPU_seconds\":"<<bhtime<<",\"original_lift_CPU_seconds\":"<<lifttime<<",\"counts\":";countout(o,counts);o<<"}\n";cout<<"FIRST_10000 CPU="<<cpu()-start<<" BBpass="<<counts.bbpass<<" BHcomplete="<<counts.bhcomplete<<" original_lifts="<<counts.lifts<<endl;}
  if((cursor+1)%50000==0)cout<<"PROGRESS cursor="<<cursor+1<<" CPU="<<cpu()-start<<" BBpass="<<counts.bbpass<<" BHcomplete="<<counts.bhcomplete<<" lifts="<<counts.lifts<<endl;
 }
done:
 string selection;
 if(have_original)selection="minimum_leaf_missing_among_actual_lifts_of_complete_BH_keys_in_completed_prefix";
 else if(counts.bhscored){bestkey=minkey;bestbits=0;selection="minimum_weighted_BH_missing_among_quotient_BB_pass_keys_one_original_lift_fallback";}
 else {bestkey=minbbkey;bestbits=0;selection="one_minimum_quotient_BB_key_one_original_lift_fallback";}
 if(counts.keys)save_original(base+"/production.best",bestkey,bestbits,original,selection);
 if(status=="D5_CANDIDATE"){auto score=fullscore(original);assert(score.bad==0);cout<<"D5_CANDIDATE_SAVED n=3348 degree=7 cursor="<<bestkey.cursor<<" bits="<<bestbits<<endl;}
 ofstream o(base+"/production.terminal.json");o<<setprecision(10)<<"{\"status\":\""<<status<<"\",\"quotient_scope\":405000,\"covered_original_lift_scope\":3240000,\"next_cursor\":"<<cursor<<",\"next_key\":";if(cursor<SCOPE&&status!="D5_CANDIDATE")keyout(o,decode_key(cursor));else o<<"null";o<<",\"counts\":";countout(o,counts);
 o<<",\"minimum_quotient_BB_missing\":"<<(counts.keys?minbb:-1)<<",\"minimum_weighted_BH_missing_among_BB_pass\":"<<(counts.bhscored?minbh:-1)<<",\"minimum_actual_leaf_missing_among_expanded_lifts\":"<<(have_original?bestleaf:-1)<<",\"selection\":\""<<selection<<"\",\"best_key\":";keyout(o,bestkey);o<<",\"best_lift_bits\":"<<bestbits<<",\"one_saved_original_full_three_root_check\":true,\"fallback_original_graph_outside_production_lift_count\":"<<(!have_original?"true":"false")<<",\"CPU_seconds\":"<<cpu()-start<<",\"BB_CPU_seconds\":"<<bbtime<<",\"BH_BFS_CPU_seconds\":"<<bhtime<<",\"original_lift_CPU_seconds\":"<<lifttime<<",\"BB_missing_histogram\":{";
 bool first=true;for(auto [k,v]:bbhist){if(!first)o<<',';first=false;o<<'\"'<<k<<"\":"<<v;}o<<"},\"weighted_BH_missing_histogram_on_BB_pass\":{";first=true;for(auto [k,v]:bhhist){if(!first)o<<',';first=false;o<<'\"'<<k<<"\":"<<v;}o<<"}}\n";
 cout<<status<<" keys="<<counts.keys<<" BBpass="<<counts.bbpass<<" BHcomplete="<<counts.bhcomplete<<" original_lifts="<<counts.lifts<<" CPU="<<cpu()-start<<endl;
}
