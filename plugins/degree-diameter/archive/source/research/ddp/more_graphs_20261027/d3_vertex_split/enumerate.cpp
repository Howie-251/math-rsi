#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
using U=uint64_t;
static clock_t started;
struct Check { int diameter=0; vector<U> bad; int maxdegree=0; };
Check all_bfs(const vector<vector<int>>&g){
 int n=g.size();Check out;vector<int>d(n),q(n);
 for(auto&a:g)out.maxdegree=max(out.maxdegree,int(a.size()));
 for(int s=0;s<n;s++){
  fill(d.begin(),d.end(),-1);int h=0,t=0;d[s]=0;q[t++]=s;
  while(h<t){int u=q[h++];for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;q[t++]=v;}}
  for(int v=s+1;v<n;v++){if(d[v]<0||d[v]>3)out.bad.push_back(U(s)*n+v);out.diameter=max(out.diameter,d[v]);}
 }
 return out;
}
struct Crit{int a,y;unsigned c;};
vector<vector<int>> split_graph(const vector<vector<int>>&g,int v,const vector<int>&N,unsigned mask){
 int n=g.size();vector<vector<int>>h(n+1);
 auto edge=[&](int a,int b){h[a].push_back(b);h[b].push_back(a);};
 for(int a=0;a<n;a++)if(a!=v)for(int b:g[a])if(b>a&&b!=v)edge(a,b);
 for(int j=0;j<(int)N.size();j++)edge((mask>>j&1)?v:n,N[j]);
 edge(v,n);return h;
}
void edges(const vector<vector<int>>&g,const string&file){
 ofstream f(file);long long m=0;for(auto&a:g)m+=a.size();f<<g.size()<<' '<<m/2<<'\n';
 for(int u=0;u<(int)g.size();u++)for(int v:g[u])if(u<v)f<<u<<' '<<v<<'\n';
}
void ints(ostream&f,const vector<int>&a){f<<'[';for(size_t i=0;i<a.size();i++){if(i)f<<',';f<<a[i];}f<<']';}
void run_case(const string&input,const string&outdir,int cap){
 ifstream f(input);int n;long long m;f>>n>>m;vector<vector<int>>g(n);set<pair<int,int>>es;
 for(long long k=0;k<m;k++){int u,v;f>>u>>v;assert(u!=v&&0<=u&&u<n&&0<=v&&v<n);if(u>v)swap(u,v);assert(es.insert({u,v}).second);g[u].push_back(v);g[v].push_back(u);}
 for(auto&a:g){sort(a.begin(),a.end());assert(a.size()<=size_t(cap));}
 string stem=outdir+"/d"+to_string(cap);int W=(n+63)/64;
 long long raw=0,capacityrej=0,evaluated=0,rejU=0,rejW=0,rejOld=0,passers=0,prodBFS=0,calibBFS=0;
 int vertices=0,lastv=-1;unsigned lastmask=0;bool complete=true,calibrated=false,calibmatch=false;
 int calibpred=-1,calibactual=-1,calibD=-1;long long neighborBFS=0;vector<tuple<int,unsigned,int>> passing;
 vector<array<long long,7>> pervertex;
 for(int v=0;v<n;v++){
  if(double(clock()-started)/CLOCKS_PER_SEC>105){complete=false;break;}
  lastv=v;const vector<int>&N=g[v];int d=N.size();unsigned M=1u<<d,ALL=M-1;
  vector<int>pos(n,-1);for(int j=0;j<d;j++)pos[N[j]]=j;
  vector<unsigned>Cy(n);for(int y=0;y<n;y++)for(int z:g[y])if(pos[z]>=0)Cy[y]|=1u<<pos[z];
  vector<U>R1(d*W),R2(d*W),U1(size_t(M)*W),U2(size_t(M)*W),full(W,~U(0));
  if(n%64)full.back()=(U(1)<<(n%64))-1;full[v/64]&=~(U(1)<<(v%64));
  vector<Crit>critical;vector<int>distance(n),q(n);
  for(int j=0;j<d;j++){
   neighborBFS++;fill(distance.begin(),distance.end(),-1);int h=0,t=0;distance[N[j]]=0;q[t++]=N[j];
   while(h<t){int a=q[h++];if(distance[a]==3)continue;for(int b:g[a])if(b!=v&&distance[b]<0){distance[b]=distance[a]+1;q[t++]=b;}}
   for(int y=0;y<n;y++)if(y!=v){
    if(distance[y]>=0&&distance[y]<=1)R1[j*W+y/64]|=U(1)<<(y%64);
    if(distance[y]>=0&&distance[y]<=2)R2[j*W+y/64]|=U(1)<<(y%64);
    if(pos[y]<0&&distance[y]<0)critical.push_back({j,y,Cy[y]});
   }
  }
  for(unsigned mask=1;mask<M;mask++){
   int j=__builtin_ctz(mask);unsigned prev=mask&(mask-1);
   for(int w=0;w<W;w++){U1[size_t(mask)*W+w]=U1[size_t(prev)*W+w]|R1[j*W+w];U2[size_t(mask)*W+w]=U2[size_t(prev)*W+w]|R2[j*W+w];}
  }
  array<long long,7> counts{};
  for(unsigned S=1;S<M-1;S+=2){
   if((S&511)==1&&double(clock()-started)/CLOCKS_PER_SEC>105){complete=false;break;}
   unsigned T=ALL^S;int a=__builtin_popcount(S),b=d-a;raw++;counts[0]++;lastmask=S;
   int small=min(a,b),large=max(a,b);
   int bound=2+small*(cap*cap-cap+1)+large*cap;
   if(a+1>cap||b+1>cap||bound<n+1){capacityrej++;counts[1]++;continue;}
   evaluated++;counts[2]++;
   bool okU=true,okW=true,okOld=true;
   for(int w=0;w<W;w++){
    if(((U2[size_t(S)*W+w]|U1[size_t(T)*W+w])&full[w])!=full[w])okU=false;
    if(((U2[size_t(T)*W+w]|U1[size_t(S)*W+w])&full[w])!=full[w])okW=false;
   }
   for(auto c:critical)if(!(c.c&((S>>c.a&1)?S:T))){okOld=false;break;}
   Check cached;bool reuse=false;
   if(!calibrated){
    vector<U>predicted;
    for(int y=0;y<n;y++)if(y!=v){
     if(!((U2[size_t(S)*W+y/64]|U1[size_t(T)*W+y/64])>>(y%64)&1))predicted.push_back(U(min(y,v))*(n+1)+max(y,v));
     if(!((U2[size_t(T)*W+y/64]|U1[size_t(S)*W+y/64])>>(y%64)&1))predicted.push_back(U(y)*(n+1)+n);
    }
    for(auto c:critical)if(!(c.c&((S>>c.a&1)?S:T))){int x=N[c.a];predicted.push_back(U(min(x,c.y))*(n+1)+max(x,c.y));}
    sort(predicted.begin(),predicted.end());predicted.erase(unique(predicted.begin(),predicted.end()),predicted.end());
    auto expanded=split_graph(g,v,N,S);cached=all_bfs(expanded);calibBFS++;calibrated=true;reuse=true;
    calibpred=predicted.size();calibactual=cached.bad.size();calibD=cached.diameter;calibmatch=predicted==cached.bad;
    if(!calibmatch){cerr<<"CALIBRATION_MISMATCH "<<cap<<'\n';exit(3);}
   }
   if(!okU){rejU++;counts[3]++;continue;}
   if(!okW){rejW++;counts[4]++;continue;}
   if(!okOld){rejOld++;counts[5]++;continue;}
   auto expanded=split_graph(g,v,N,S);Check ck=reuse?cached:all_bfs(expanded);if(!reuse)prodBFS++;
   if(!ck.bad.empty()||ck.maxdegree>cap){cerr<<"PASSER_MISMATCH "<<cap<<'\n';exit(4);}
   passers++;counts[6]++;passing.emplace_back(v,S,ck.diameter);
   if(passers==1){edges(expanded,stem+"_first_success.edges");cout<<"HIT d="<<cap<<" n="<<n+1<<" v="<<v<<" mask="<<S<<" D="<<ck.diameter<<endl;}
  }
  pervertex.push_back(counts);vertices++;if(!complete)break;
 }
 ofstream o(stem+"_RESULT.json");
 o<<"{\"degree_cap\":"<<cap<<",\"source_n\":"<<n<<",\"target_n\":"<<n+1<<",\"source_m\":"<<m
  <<",\"status\":\""<<(complete?(passers?"COMPLETE_WITH_PRODUCER_VERIFIED_HITS":"COMPLETE_NO_HITS"):"INCOMPLETE_CPU_LIMIT")
  <<"\",\"all_vertices_completed\":"<<vertices<<",\"last_vertex\":"<<lastv<<",\"last_mask\":"<<lastmask
  <<",\"raw_unordered_nonempty_partitions\":"<<raw<<",\"capacity_rejected\":"<<capacityrej<<",\"exact_condition_evaluated\":"<<evaluated
  <<",\"new_u_rejected\":"<<rejU<<",\"new_w_rejected_after_u_pass\":"<<rejW<<",\"old_cross_pair_rejected_after_newroots_pass\":"<<rejOld
  <<",\"passers\":"<<passers<<",\"neighbor_radius3_BFS\":"<<neighborBFS<<",\"producer_passer_allsource_BFS\":"<<prodBFS
  <<",\"first_partition_calibration_allsource_BFS\":"<<calibBFS<<",\"calibration_exact_bad_pair_set_match\":"<<(calibmatch?"true":"false")
  <<",\"calibration_predicted_bad_unordered_pairs\":"<<calibpred<<",\"calibration_actual_bad_unordered_pairs\":"<<calibactual<<",\"calibration_D\":"<<calibD
  <<",\"passing_partitions\":[";
 for(size_t k=0;k<passing.size();k++){
  if(k)o<<',';auto[v,S,D]=passing[k];vector<int>s,t;for(int j=0;j<(int)g[v].size();j++)((S>>j&1)?s:t).push_back(g[v][j]);
  o<<"{\"split_vertex\":"<<v<<",\"S\":";ints(o,s);o<<",\"T\":";ints(o,t);o<<",\"producer_D\":"<<D<<'}';
 }
 o<<"],\"per_vertex_counts_columns\":[\"raw\",\"capacityreject\",\"evaluated\",\"newUreject\",\"newWreject\",\"oldreject\",\"pass\"],\"per_vertex_counts\":[";
 for(size_t k=0;k<pervertex.size();k++){if(k)o<<',';o<<'[';for(int j=0;j<7;j++){if(j)o<<',';o<<pervertex[k][j];}o<<']';}
 o<<"],\"cumulative_CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<"}\n";
 cout<<"DONE d="<<cap<<" vertices="<<vertices<<" raw="<<raw<<" capacityrej="<<capacityrej<<" eval="<<evaluated<<" pass="<<passers<<" CPU="<<double(clock()-started)/CLOCKS_PER_SEC<<endl;
}
int main(int argc,char**argv){assert(argc==4);started=clock();rlimit lim{115,118};setrlimit(RLIMIT_CPU,&lim);run_case(argv[1],argv[3],8);run_case(argv[2],argv[3],12);}
