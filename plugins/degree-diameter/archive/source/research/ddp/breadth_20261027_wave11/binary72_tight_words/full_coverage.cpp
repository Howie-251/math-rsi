#include <bits/stdc++.h>
using namespace std;
constexpr int N=1152,W=18;
using Map=array<int,16>;
using Graph=array<array<int,8>,N>;
using Matrix=array<array<uint64_t,W>,N>;
struct Mat{array<int,4>col;Map m,inv;};
struct Passer{int ai,bi,bb;array<int,4>ac,bc;};
int rank4(array<int,4>c){int piv[4]{},r=0;for(int v:c)for(int j=3;j>=0;j--)if(v&(1<<j)){if(piv[j])v^=piv[j];else{piv[j]=v;r++;break;}}return r;}
Mat make_mat(array<int,4>c){Mat a;a.col=c;for(int x=0;x<16;x++){int v=0;for(int j=0;j<4;j++)if(x&(1<<j))v^=c[j];a.m[x]=v;a.inv[v]=x;}return a;}
array<int,4>wordcols(const array<Map,4>&m,const array<int,4>&b,const array<int,4>&w){return {m[w[3]][m[w[2]][m[w[1]][b[w[0]]]]],m[w[3]][m[w[2]][b[w[1]]]],m[w[3]][b[w[2]]],b[w[3]]};}
void data(const Passer&p,array<Map,4>&m,array<int,4>&b){Mat A=make_mat(p.ac),B=make_mat(p.bc);m={A.m,B.m,B.inv,A.inv};b={1,p.bb,B.inv[p.bb],A.inv[1]};}
Graph build(const Passer&p,const array<array<int,4>,72>&adj){
 array<Map,4>m;array<int,4>b;data(p,m,b);Graph g{};
 for(int u=0;u<72;u++)for(int x=0;x<16;x++)for(int t=0;t<4;t++)for(int l=0;l<2;l++)g[16*u+x][2*t+l]=16*adj[u][t]+(m[t][x]^(l*b[t]));
 return g;
}
int score(const Graph&g,Matrix&out){
 Matrix r2{};
 for(int u=0;u<N;u++){
  r2[u][u>>6]|=1ULL<<(u&63);
  for(int v:g[u]){r2[u][v>>6]|=1ULL<<(v&63);for(int x:g[v])r2[u][x>>6]|=1ULL<<(x&63);}
 }
 int missing=0;
 for(int u=0;u<N;u++){
  array<uint64_t,W>row{};
  for(int k=0;k<W;k++){uint64_t bits=r2[u][k];while(bits){int v=64*k+__builtin_ctzll(bits);bits&=bits-1;for(int j=0;j<W;j++)row[j]|=r2[v][j];}}
  int count=0;for(auto z:row)count+=__builtin_popcountll(z);missing+=N-count;out[u]=row;
 }assert(missing%2==0);return missing/2;
}
void rawwalk(const Graph&g,int r,int u,int depth,Matrix&seen){seen[r][u>>6]|=1ULL<<(u&63);if(depth==4)return;for(int v:g[u])rawwalk(g,r,v,depth+1,seen);}
void write_param(ostream&f,const Passer&p,int id){
 array<Map,4>m;array<int,4>b;data(p,m,b);
 f<<"{\"passer_id\":"<<id<<",\"companion_index\":"<<p.ai<<",\"B_GL_index\":"<<p.bi<<",\"b1\":"<<p.bb<<",\"matrix_columns\":[";
 for(int t=0;t<4;t++){if(t)f<<',';f<<'[';for(int j=0;j<4;j++){if(j)f<<',';f<<m[t][1<<j];}f<<']';}f<<"],\"b_codes\":[";
 for(int t=0;t<4;t++){if(t)f<<',';f<<b[t];}f<<"],\"offsets\":[0,0,0,0]}";
}
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1];double limit=stod(argv[2]);clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 ifstream wi(dir+"/words.txt");int wn;wi>>wn;assert(wn==26);vector<array<int,4>>words(wn);for(auto&w:words)for(int&t:w)wi>>t;
 array<array<int,4>,72>adj;ifstream ci(dir+"/controller.txt");for(auto&row:adj)for(int&v:row)ci>>v;
 const array<int,4>invlabel={3,2,1,0};for(int u=0;u<72;u++)for(int t=0;t<4;t++)assert(adj[adj[u][t]][invlabel[t]]==u);
 vector<Passer>passers;long long examined=0;bool cache=false,limited=false;
 ifstream cached(dir+"/all_passers.txt");
 if(cached.good()){
  cache=true;int count;cached>>count;assert(count==1024);
  for(int k=0;k<count;k++){Passer p;cached>>p.ai>>p.bi>>p.bb;for(int&x:p.ac)cached>>x;for(int&x:p.bc)cached>>x;passers.push_back(p);}
 }else{
  vector<Mat>gs;for(int code=0;code<65536;code++){array<int,4>c;for(int j=0;j<4;j++)c[j]=(code>>(4*j))&15;if(rank4(c)==4)gs.push_back(make_mat(c));}assert(gs.size()==20160);
  for(int ai=0;ai<8&&!limited;ai++){
   Mat A=make_mat({2,4,8,1+2*ai});
   for(int bi=0;bi<int(gs.size())&&!limited;bi++){
    const Mat&B=gs[bi];array<Map,4>m={A.m,B.m,B.inv,A.inv};
    for(int bb=1;bb<16;bb++){
     if((examined&4095)==0&&cpu()>=limit){limited=true;break;}
     examined++;array<int,4>b={1,bb,B.inv[bb],A.inv[1]};bool okay=true;
     for(auto&w:words)if(rank4(wordcols(m,b,w))!=4){okay=false;break;}
     if(okay)passers.push_back({ai,bi,bb,A.col,B.col});
    }
   }
  }
  assert(!limited&&examined==2419200&&passers.size()==1024);
  ofstream text(dir+"/all_passers.txt");text<<passers.size()<<'\n';
  ofstream pf(dir+"/all_passers.json");pf<<"{\"count\":1024,\"inverse_labels\":[3,2,1,0],\"criterion\":\"all26controller-requiredwords rank4; no bbbb filter\",\"passers\":[";
  for(int k=0;k<int(passers.size());k++){auto&p=passers[k];text<<p.ai<<' '<<p.bi<<' '<<p.bb;for(int x:p.ac)text<<' '<<x;for(int x:p.bc)text<<' '<<x;text<<'\n';if(k)pf<<',';write_param(pf,p,k);}pf<<"]}\n";
 }
 double enumeration_cpu=cpu();cout<<"PASSERS ready="<<passers.size()<<" reused_cache="<<cache<<" CPU="<<cpu()<<endl;
 Graph bestg{};Matrix bestreach{};int best=INT_MAX,bestid=-1,checked=0,hits=0;vector<int>scores;map<int,int>hist;
 for(int k=0;k<int(passers.size());k++){
  if(cpu()>=limit){limited=true;break;}
  Graph g=build(passers[k],adj);Matrix reach;int bad=score(g,reach);scores.push_back(bad);checked++;hist[bad]++;
  if(k==0){
   Matrix raw{};for(int u=0;u<N;u++)rawwalk(g,u,u,0,raw);assert(raw==reach);
   ofstream c(dir+"/first_finalist_calibration.json");c<<"{\"status\":\"MATCH\",\"passer_id\":0,\"all1152_R4_rows_match\":true,\"raw_walks_enumerated\":5392512,\"bad_unordered_pairs\":"<<bad<<",\"formal_score_reused\":true,\"BFS_performed\":false}\n";
  }
  if(bad<best){best=bad;bestid=k;bestg=g;bestreach=reach;}
  if(!bad){hits++;cout<<"HIT passer="<<k<<endl;}
 }
 assert(checked>0);set<pair<int,int>>E;
 for(int u=0;u<N;u++){set<int>ns(bestg[u].begin(),bestg[u].end());assert(ns.size()==8&&!ns.count(u));for(int v:ns){assert(find(bestg[v].begin(),bestg[v].end(),u)!=bestg[v].end());E.insert(minmax(u,v));}}
 assert(E.size()==4608);ofstream ef(dir+"/best.edges");ef<<"1152 4608\n";for(auto[u,v]:E)ef<<u<<' '<<v<<'\n';
 ofstream bp(dir+"/best_parameters.json");bp<<"{\"field\":2,\"fiber_dimension\":4,\"vertex_encoding\":\"16*u+x0+2*x1+4*x2+8*x3\",\"inverse_labels\":[3,2,1,0],\"global_label_parameters\":";write_param(bp,passers[bestid],bestid);bp<<",\"controller_out\":[";
 for(int u=0;u<72;u++){if(u)bp<<',';bp<<'[';for(int t=0;t<4;t++){if(t)bp<<',';bp<<adj[u][t];}bp<<']';}bp<<"]}\n";
 ofstream sf(dir+"/all_passers_scores.json");sf<<"{\"passers_total\":1024,\"checked\":"<<checked<<",\"score\":\"ordinary unordered pairs outside R4, possibly unreachable\",\"scores_by_passer_id\":[";
 for(int k=0;k<checked;k++){if(k)sf<<',';sf<<scores[k];}sf<<"],\"histogram\":{";bool comma=false;for(auto[bad,n]:hist){if(comma)sf<<',';comma=true;sf<<'"'<<bad<<"\":"<<n;}sf<<"}}\n";
 int same=0,cross=0;for(int u=0;u<N;u++)for(int v=u+1;v<N;v++)if(!(bestreach[u][v>>6]>>(v&63)&1)){if(u/16==v/16)same++;else cross++;}
 ofstream f(dir+"/coverage_result.json");f<<"{\"status\":\""<<(limited?"PARTIAL_COVERAGE_CPU_LIMIT":hits?"COMPLETE_GLOBAL_LABEL_OFFSET0_HITS_EXIST":"COMPLETE_GLOBAL_LABEL_OFFSET0_NO_D4")<<"\",\"passers_total\":1024,\"passers_checked\":"<<checked<<",\"complete\":"<<(!limited&&checked==1024?"true":"false")<<",\"hits\":"<<hits<<",\"best_passer_id\":"<<bestid<<",\"best_bad_unordered_pairs_gt4_or_unreachable\":"<<best<<",\"best_samefiber_bad_pairs\":"<<same<<",\"best_crossfiber_bad_pairs\":"<<cross<<",\"passer_cache_reused\":"<<(cache?"true":"false")<<",\"canonical_inputs_reenumerated_once_for_persistence\":"<<examined<<",\"enumeration_and_cache_CPU_seconds\":"<<enumeration_cpu<<",\"native_CPU_seconds\":"<<cpu()<<",\"native_soft_seconds\":"<<limit<<",\"n\":1152,\"m\":4608,\"degree\":8,\"ordinary_BFS_performed\":false,\"full_R4_calibration_once\":true,\"simple8regular_production_check\":true,\"offsets\":0,\"SLS_proposals\":0,\"new_seeds\":0}\n";
 cout<<"COVERAGE checked="<<checked<<" hits="<<hits<<" best_bad="<<best<<" best_id="<<bestid<<" CPU="<<cpu()<<endl;
}
