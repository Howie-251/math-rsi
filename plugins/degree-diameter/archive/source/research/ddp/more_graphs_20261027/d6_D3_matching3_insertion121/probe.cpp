#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;using U=uint64_t;
struct Mask{U a=0,b=0;Mask operator|(const Mask&x)const{return{a|x.a,b|x.b};}bool meet(const Mask&x)const{return(a&x.a)||(b&x.b);}void add(int x){if(x<64)a|=U(1)<<x;else b|=U(1)<<(x-64);}int count()const{return __builtin_popcountll(a)+__builtin_popcountll(b);}};
int main(int argc,char**argv){
 clock_t start=clock();string dir=argv[2];double budget=stod(argv[3]);auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 ifstream in(argv[1]);int n,m;in>>n>>m;assert(n==120&&m==360);
 array<array<int,6>,121>g{};array<int,121>degree{};vector<pair<int,int>>edges;
 for(int i=0;i<m;i++){int u,v;in>>u>>v;assert(u>=0&&v>=0&&u<n&&v<n&&u!=v);if(u>v)swap(u,v);edges.emplace_back(u,v);g[u][degree[u]++]=v;g[v][degree[v]++]=u;}
 sort(edges.begin(),edges.end());assert(adjacent_find(edges.begin(),edges.end())==edges.end());for(int u=0;u<n;u++){assert(degree[u]==6);sort(g[u].begin(),g[u].end());}
 array<Mask,120>r2;
 ofstream cache(dir+"/source_R2.u64le.bin",ios::binary);
 for(int u=0;u<n;u++){r2[u].add(u);for(int v:g[u]){r2[u].add(v);for(int w:g[v])r2[u].add(w);}cache.write((char*)&r2[u],sizeof(Mask));}
 cache.close();
 vector<Mask>end(m),ball(m);for(int i=0;i<m;i++){auto[u,v]=edges[i];end[i].add(u);end[i].add(v);ball[i]=r2[u]|r2[v];}
 long long raw=0,matching=0,gatepass=0,gatefail=0,oldfail=0,bfses=0;int maxroots=0;int ca=-1,cb=-1,cc=-1;bool hit=false,limited=false,profiled=false;
 int firsta=-1,firstb=-1,firstc=-1,firstroot=-1,firsttarget=-1,firstroots=0;
 auto dump=[&](){
  ofstream out(dir+"/NATIVE_RESULT.json");
  out<<"{\"source_n\":120,\"source_m\":360,\"raw_scope\":7711320,\"raw_visited\":"<<raw
   <<",\"matching_triples\":"<<matching<<",\"newroot_gate_pass\":"<<gatepass<<",\"newroot_gate_fail\":"<<gatefail
   <<",\"oldpair_fail\":"<<oldfail<<",\"modified_graph_root_BFS\":"<<bfses<<",\"max_roots_checked_per_candidate\":"<<maxroots
   <<",\"source_R2_roots\":120,\"source_full_D3_BFS\":0,\"hit\":"<<(hit?"true":"false")
   <<",\"CPU_limited\":"<<(limited?"true":"false")<<",\"cursor\":["<<ca<<','<<cb<<','<<cc
   <<"],\"first_gatepass_oldpair_failure\":{\"edge_indices\":["<<firsta<<','<<firstb<<','<<firstc
   <<"],\"root\":"<<firstroot<<",\"target\":"<<firsttarget<<",\"checked_roots\":"<<firstroots
   <<"},\"native_CPU_seconds\":"<<cpu()<<"}\n";
 };
 for(int a=0;a<m-2;a++)for(int b=a+1;b<m-1;b++)for(int c=b+1;c<m;c++){
  ++raw;ca=a;cb=b;cc=c;
  if((raw&4095)==0&&cpu()>budget){limited=true;goto terminal;}
  Mask ab=end[a]|end[b];
  if(end[a].meet(end[b])||ab.meet(end[c]))continue;
  ++matching;Mask coverage=ball[a]|ball[b]|ball[c];
  if(coverage.count()!=120){++gatefail;continue;}
  ++gatepass;auto h=g;vector<int>S;
  for(int e:{a,b,c}){auto[u,v]=edges[e];S.push_back(u);S.push_back(v);
   auto iu=find(h[u].begin(),h[u].end(),v),iv=find(h[v].begin(),h[v].end(),u);
   assert(iu!=h[u].end()&&iv!=h[v].end());*iu=120;*iv=120;
  }
  sort(S.begin(),S.end());assert(adjacent_find(S.begin(),S.end())==S.end());for(int j=0;j<6;j++)h[120][j]=S[j];
  Mask affected;for(int u:S){affected.add(u);for(int v:g[u])affected.add(v);}
  vector<int>roots{120};for(int u=0;u<120;u++)if(u<64?(affected.a>>(u)&1):(affected.b>>(u-64)&1))roots.push_back(u);
  assert(roots.size()<=43);int checked=0,badroot=-1,badtarget=-1;
  for(int root:roots){
   int d[121],q[121],lo=0,hi=0;fill(d,d+121,-1);d[root]=0;q[hi++]=root;
   while(lo<hi){int u=q[lo++];if(d[u]==3)continue;for(int v:h[u])if(d[v]<0){d[v]=d[u]+1;q[hi++]=v;}}
   ++bfses;++checked;
   for(int t=0;t<121;t++)if(d[t]<0){badroot=root;badtarget=t;break;}
   if(badroot>=0){assert(root!=120);break;}
  }
  maxroots=max(maxroots,checked);
  if(badroot>=0){
   ++oldfail;if(firsta<0){firsta=a;firstb=b;firstc=c;firstroot=badroot;firsttarget=badtarget;firstroots=checked;}
  }else{
   hit=true;ofstream out(dir+"/graph_d6_D3_n121.edges");out<<"121 363\n";
   for(int u=0;u<121;u++)for(int v:h[u])if(u<v)out<<u<<' '<<v<<'\n';
   ofstream params(dir+"/FIRST_HIT.json");params<<"{\"edge_indices\":["<<a<<','<<b<<','<<c<<"],\"deleted_edges\":[";
   for(int j=0;j<3;j++){if(j)params<<',';auto[u,v]=edges[j==0?a:j==1?b:c];params<<'['<<u<<','<<v<<']';}
   params<<"],\"new_vertex\":120,\"new_n\":121,\"new_m\":363,\"new_degree\":6,\"full_neighbor_set\":[";
   for(int j=0;j<6;j++){if(j)params<<',';params<<S[j];}
   params<<"],\"affected_old_roots\":[";
   for(size_t j=1;j<roots.size();j++){if(j>1)params<<',';params<<roots[j];}
   params<<"],\"actual_modified_roots_checked\":"<<checked<<",\"all_checked_roots_D3_cover\":true,\"root_independent_check_pending\":true}\n";
   goto terminal;
  }
  if(!profiled&&raw>=10000){
   profiled=true;ofstream profile(dir+"/FIRST_PROFILE.json");profile<<"{\"raw_visited\":"<<raw<<",\"matching_triples\":"<<matching<<",\"newroot_gate_pass\":"<<gatepass<<",\"CPU_seconds\":"<<cpu()<<"}\n";
  }
 }
terminal:dump();cout<<(hit?"FIRST_COMPLETE_HIT":limited?"CPU_LIMIT_UNKNOWN":"COMPLETE_NO_HIT")<<" raw "<<raw<<" matching "<<matching<<" gatepass "<<gatepass<<" CPU "<<cpu()<<endl;
}
