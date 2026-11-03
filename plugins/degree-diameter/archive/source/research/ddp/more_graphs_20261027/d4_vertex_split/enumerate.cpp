#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint64_t;
static clock_t started;
struct Check{int diameter=0,maxdegree=0;long long bad=0;};
vector<int> bfs(const vector<vector<int>>&g,int root,int bound,int removed=-1){
 int n=g.size();vector<int>d(n,-1),q(n);int h=0,t=0;d[root]=0;q[t++]=root;
 while(h<t){int x=q[h++];if(d[x]==bound)continue;for(int y:g[x])if(y!=removed&&d[y]<0){d[y]=d[x]+1;q[t++]=y;}}
 return d;
}
Check all_bfs(const vector<vector<int>>&g){
 Check r;int n=g.size();for(auto&a:g)r.maxdegree=max(r.maxdegree,int(a.size()));
 for(int x=0;x<n;x++){auto d=bfs(g,x,n);for(int y=x+1;y<n;y++){if(d[y]<0||d[y]>4)r.bad++;r.diameter=max(r.diameter,d[y]);}}
 return r;
}
vector<vector<int>> split_graph(const vector<vector<int>>&g,int v,const vector<int>&N,unsigned S){
 int n=g.size();vector<vector<int>>h(n+1);auto edge=[&](int a,int b){h[a].push_back(b);h[b].push_back(a);};
 for(int a=0;a<n;a++)if(a!=v)for(int b:g[a])if(b>a&&b!=v)edge(a,b);
 for(int j=0;j<(int)N.size();j++)edge((S>>j&1)?v:n,N[j]);edge(v,n);return h;
}
void save_edges(const vector<vector<int>>&g,const string&path){
 long long m=0;for(auto&a:g)m+=a.size();ofstream f(path);f<<g.size()<<' '<<m/2<<'\n';
 for(int x=0;x<(int)g.size();x++)for(int y:g[x])if(x<y)f<<x<<' '<<y<<'\n';
}
void ints(ostream&f,const vector<int>&v){f<<'[';for(size_t j=0;j<v.size();j++){if(j)f<<',';f<<v[j];}f<<']';}
void run_case(const string&input,const string&outdir,int cap){
 ifstream f(input);int n;long long m;f>>n>>m;vector<vector<int>>g(n);set<pair<int,int>>es;
 for(long long k=0;k<m;k++){int x,y;f>>x>>y;assert(x!=y&&0<=x&&x<n&&0<=y&&y<n);if(x>y)swap(x,y);assert(es.insert({x,y}).second);g[x].push_back(y);g[y].push_back(x);}
 for(auto&a:g){sort(a.begin(),a.end());assert(a.size()==size_t(cap));}
 string stem=outdir+"/d"+to_string(cap);int W=(n+63)/64;
 long long raw=0,caprej=0,eval=0,rejS=0,rejT=0,rootpass=0,oldrej=0,passers=0,neighborBFS=0,oldHBFS=0,producerBFS=0;
 long long farPairTotal=0;int vertices=0,lastv=-1;unsigned lastmask=0;bool complete=true,calibrated=false,calibmatch=false;
 int calibv=-1;unsigned calibmask=0;vector<int>calibmissS,calibmissT;vector<tuple<int,unsigned,int>>passing;
 vector<array<long long,8>>pervertex;
 for(int v=0;v<n;v++){
  if(double(clock()-started)/CLOCKS_PER_SEC>105){complete=false;break;}
  lastv=v;const auto&N=g[v];int d=N.size();unsigned M=1u<<d,ALL=M-1;
  vector<uint8_t>distN(d*n,5);vector<U>R2(d*W),R3(d*W),U2(size_t(M)*W),U3(size_t(M)*W),full(W,~U(0));
  if(n%64)full.back()=(U(1)<<(n%64))-1;full[v/64]&=~(U(1)<<(v%64));
  for(int j=0;j<d;j++){
   auto dd=bfs(g,N[j],4,v);neighborBFS++;
   for(int y=0;y<n;y++)if(y!=v){
    if(dd[y]>=0)distN[j*n+y]=dd[y];
    if(dd[y]>=0&&dd[y]<=2)R2[j*W+y/64]|=U(1)<<(y%64);
    if(dd[y]>=0&&dd[y]<=3)R3[j*W+y/64]|=U(1)<<(y%64);
   }
  }
  for(unsigned s=1;s<M;s++){int j=__builtin_ctz(s);unsigned p=s&(s-1);for(int w=0;w<W;w++){
   U2[size_t(s)*W+w]=U2[size_t(p)*W+w]|R2[j*W+w];U3[size_t(s)*W+w]=U3[size_t(p)*W+w]|R3[j*W+w];}}
  vector<unsigned>rootpassing;array<long long,8>counts{};
  int A=0,B=0,power=1;for(int j=0;j<4;j++){A+=power;if(j<3)B+=power;power*=cap-1;}
  for(unsigned S=1;S<M-1;S+=2){
   raw++;counts[0]++;lastmask=S;unsigned T=ALL^S;int a=__builtin_popcount(S),b=d-a;
   if(a+1>cap||b+1>cap||2+min(a,b)*A+max(a,b)*B<n+1){caprej++;counts[1]++;continue;}
   eval++;counts[2]++;bool okS=true,okT=true;
   for(int w=0;w<W;w++){
    if(((U3[size_t(S)*W+w]|U2[size_t(T)*W+w])&full[w])!=full[w])okS=false;
    if(((U3[size_t(T)*W+w]|U2[size_t(S)*W+w])&full[w])!=full[w])okT=false;
   }
   if(!calibrated){
    auto h=split_graph(g,v,N,S);auto ds=bfs(h,v,4),dt=bfs(h,n,4);vector<int>predS,predT,actS,actT;
    for(int y=0;y<n;y++)if(y!=v){
     if(!((U3[size_t(S)*W+y/64]|U2[size_t(T)*W+y/64])>>(y%64)&1))predS.push_back(y);
     if(!((U3[size_t(T)*W+y/64]|U2[size_t(S)*W+y/64])>>(y%64)&1))predT.push_back(y);
     if(ds[y]<0)actS.push_back(y);if(dt[y]<0)actT.push_back(y);
    }
    calibrated=true;calibmatch=predS==actS&&predT==actT;calibv=v;calibmask=S;calibmissS=actS;calibmissT=actT;
    if(!calibmatch){cerr<<"ROOT_CALIBRATION_MISMATCH d="<<cap<<'\n';exit(3);}
   }
   if(!okS){rejS++;counts[3]++;continue;}if(!okT){rejT++;counts[4]++;continue;}
   rootpass++;counts[5]++;rootpassing.push_back(S);
  }
  if(!rootpassing.empty()){
   vector<pair<int,int>>far;
   for(int x=0;x<n;x++)if(x!=v){
    auto dd=bfs(g,x,4,v);oldHBFS++;
    for(int y=x+1;y<n;y++)if(y!=v&&dd[y]<0)far.push_back({x,y});
   }
   farPairTotal+=far.size();
   vector<uint8_t>D(size_t(M)*n,5);
   for(unsigned S=1;S<M;S++){int j=__builtin_ctz(S);unsigned P=S&(S-1);for(int y=0;y<n;y++)D[size_t(S)*n+y]=min(D[size_t(P)*n+y],distN[j*n+y]);}
   for(unsigned S:rootpassing){
    if(double(clock()-started)/CLOCKS_PER_SEC>105){complete=false;break;}
    unsigned T=ALL^S;bool okay=true;
    for(auto[x,y]:far){
     int sx=D[size_t(S)*n+x],sy=D[size_t(S)*n+y],tx=D[size_t(T)*n+x],ty=D[size_t(T)*n+y];
     if(min({sx+sy+2,tx+ty+2,sx+ty+3,tx+sy+3})>4){okay=false;break;}
    }
    if(!okay){oldrej++;counts[6]++;continue;}
    auto expanded=split_graph(g,v,N,S);auto checked=all_bfs(expanded);producerBFS++;
    if(checked.bad||checked.maxdegree>cap){cerr<<"FULL_PREDICATE_MISMATCH d="<<cap<<'\n';exit(4);}
    passers++;counts[7]++;passing.emplace_back(v,S,checked.diameter);
    if(passers==1){save_edges(expanded,stem+"_first_success.edges");cout<<"HIT d="<<cap<<" n="<<n+1<<" v="<<v<<" mask="<<S<<" D="<<checked.diameter<<endl;}
   }
  }
  pervertex.push_back(counts);vertices++;if(!complete)break;
 }
 ofstream o(stem+"_RESULT.json");
 o<<"{\"degree_cap\":"<<cap<<",\"source_n\":"<<n<<",\"target_n\":"<<n+1<<",\"source_m\":"<<m
  <<",\"status\":\""<<(complete?(passers?"COMPLETE_WITH_PRODUCER_VERIFIED_HITS":"COMPLETE_NO_HITS"):"INCOMPLETE_CPU_LIMIT")<<"\",\"all_vertices_completed\":"<<vertices
  <<",\"last_vertex\":"<<lastv<<",\"last_raw_mask\":"<<lastmask<<",\"raw_unordered_nonempty_partitions\":"<<raw<<",\"capacity_rejected\":"<<caprej
  <<",\"newroot_condition_evaluated\":"<<eval<<",\"S_root_rejected\":"<<rejS<<",\"T_root_rejected_after_S_pass\":"<<rejT
  <<",\"both_newroots_pass\":"<<rootpass<<",\"old_pair_rejected_after_roots_pass\":"<<oldrej<<",\"complete_passers\":"<<passers
  <<",\"neighbor_radius4_BFS\":"<<neighborBFS<<",\"old_H_radius4_BFS\":"<<oldHBFS<<",\"old_H_far_pairs_total_over_v\":"<<farPairTotal
  <<",\"producer_passer_allsource_BFS\":"<<producerBFS<<",\"newroot_calibration_BFS\":2,\"calibration_exact_root_miss_sets_match\":"<<(calibmatch?"true":"false")
  <<",\"calibration_vertex\":"<<calibv<<",\"calibration_mask\":"<<calibmask<<",\"calibration_S_missing\":";ints(o,calibmissS);o<<",\"calibration_T_missing\":";ints(o,calibmissT);
 o<<",\"passing_partitions\":[";
 for(size_t k=0;k<passing.size();k++){if(k)o<<',';auto[v,S,D]=passing[k];vector<int>s,t;for(int j=0;j<(int)g[v].size();j++)((S>>j&1)?s:t).push_back(g[v][j]);o<<"{\"split_vertex\":"<<v<<",\"S\":";ints(o,s);o<<",\"T\":";ints(o,t);o<<",\"producer_D\":"<<D<<'}';}
 o<<"],\"per_vertex_counts_columns\":[\"raw\",\"capacityreject\",\"root_evaluated\",\"Sreject\",\"Treject\",\"bothrootpass\",\"oldreject\",\"fullpass\"],\"per_vertex_counts\":[";
 for(size_t k=0;k<pervertex.size();k++){if(k)o<<',';o<<'[';for(int j=0;j<8;j++){if(j)o<<',';o<<pervertex[k][j];}o<<']';}
 o<<"],\"cumulative_CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<"}\n";
 cout<<"DONE d="<<cap<<" vertices="<<vertices<<" raw="<<raw<<" caprej="<<caprej<<" evaluated="<<eval<<" rootpass="<<rootpass<<" oldrej="<<oldrej<<" fullpass="<<passers<<" CPU="<<double(clock()-started)/CLOCKS_PER_SEC<<endl;
}
int main(int argc,char**argv){assert(argc==5);started=clock();rlimit lim{115,118};setrlimit(RLIMIT_CPU,&lim);run_case(argv[1],argv[4],4);run_case(argv[2],argv[4],6);run_case(argv[3],argv[4],7);}
