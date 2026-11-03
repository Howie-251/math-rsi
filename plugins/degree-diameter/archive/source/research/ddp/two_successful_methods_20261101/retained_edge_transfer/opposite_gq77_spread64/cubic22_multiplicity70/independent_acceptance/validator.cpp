#include <algorithm>
#include <array>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
constexpr int OLD=160050, N=166650, BASE=1100, COPIES=6, K=6600, D=70;
constexpr long long SM=5121600, M=5544000;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
struct Reader {
 FILE*f; static constexpr size_t B=1<<20; char buf[B]; size_t p=0,z=0;
 Reader(const string&s):f(fopen(s.c_str(),"rb")){need(f,"cannot open "+s);}
 ~Reader(){fclose(f);}
 int get(){if(p==z){z=fread(buf,1,B,f);p=0;if(!z)return EOF;}return (unsigned char)buf[p++];}
 bool next(long long&v){int c;do{c=get();}while(c!=EOF&&c<=32);if(c==EOF)return false;need(c>='0'&&c<='9',"non-integer literal");v=0;do{v=v*10+c-'0';c=get();}while(c>='0'&&c<='9');need(c==EOF||c<=32,"invalid integer suffix");return true;}
 long long val(){long long v;need(next(v),"unexpected EOF");return v;}
};
int main(int argc,char**argv){
 try{
  need(argc==6,"usage: validator SOURCE CANDIDATE INPUTS OUTDIR CPU_ALLOWANCE");
  const string source=argv[1],candidate=argv[2],out=argv[4];
  const double allowance=stod(argv[5]),t0=cpu();
  ifstream in(argv[3]);need(bool(in),"cannot read independent inputs");
  int point_count,spread_count;in>>point_count>>spread_count;need(point_count==22&&spread_count==50,"input sizes");
  vector<int>points(22),spread(50),centers,ci(OLD,-1);
  for(int&x:points)in>>x;for(int&x:spread)in>>x;need(bool(in),"input table truncated");
  for(int p:points)for(int l:spread){int c=400*p+l;need(c>=0&&c<OLD&&ci[c]<0,"center range or repetition");ci[c]=centers.size();centers.push_back(c);}
  need(centers.size()==BASE,"center count");
  vector<vector<int>>sn(BASE);vector<int>sd(OLD,0);long long source_center_edges=0;
  {
   Reader s(source);need(s.val()==OLD&&s.val()==SM,"source header");pair<int,int>prev={-1,-1};
   for(long long e=0;e<SM;e++){
    long long a=s.val(),b=s.val();need(a>=0&&a<b&&b<OLD,"source endpoint");pair<int,int>edge={(int)a,(int)b};need(prev<edge,"source sort or duplicate");prev=edge;sd[a]++;sd[b]++;
    if(ci[a]>=0)sn[ci[a]].push_back(b);if(ci[b]>=0)sn[ci[b]].push_back(a);
    if(ci[a]>=0&&ci[b]>=0)source_center_edges++;
   }
   long long extra;need(!s.next(extra),"source trailing data");
  }
  for(int d:sd)need(d==64,"literal source not 64 regular");
  vector<int>load(OLD,0);
  for(auto&v:sn){sort(v.begin(),v.end());need(v.size()==64&&adjacent_find(v.begin(),v.end())==v.end(),"source center full N cardinality");for(int u:v)load[u]++;}
  int maxbase=*max_element(load.begin(),load.end());need(maxbase<=1,"base old pin load exceeds one");
  vector<int>source_bonus_count(BASE,0);int classA=0,classB=0;
  for(int b=0;b<BASE;b++){for(int v:sn[b])if(v>=160000)source_bonus_count[b]++;need(source_bonus_count[b]<=1,"base source bonus count");if(source_bonus_count[b])classA++;else classB++;}
  need(classA==22&&classB==1078,"predicted base histogram class sizes");
  for(int&x:load)x*=COPIES;int maxload=*max_element(load.begin(),load.end());need(maxload==6,"old pin maxload6");
  vector<int>deg(N,0),adj((size_t)N*D,-1),new_count(K,0),literal_load(OLD,0);
  long long old_body=0,new_body=0,new_new=0;const double t_source=cpu();
  {
   Reader c(candidate),s(source);need(c.val()==N&&c.val()==M,"candidate header");need(s.val()==OLD&&s.val()==SM,"source second header");pair<int,int>prev={-1,-1};
   auto add=[&](int a,int b){need(deg[a]<D,"candidate degree exceeds70");adj[(size_t)a*D+deg[a]++]=b;};
   for(long long e=0;e<M;e++){
    long long a=c.val(),b=c.val();need(a>=0&&a<b&&b<N,"candidate endpoint");pair<int,int>edge={(int)a,(int)b};need(prev<edge,"candidate sort or duplicate");prev=edge;
    add(a,b);add(b,a);
    if(b<OLD){need(old_body<SM,"extra old edge");need(s.val()==a&&s.val()==b,"candidate old body differs from literal source");old_body++;}
    else if(a<OLD){int i=b-OLD;need(binary_search(sn[i%BASE].begin(),sn[i%BASE].end(),(int)a),"new edge outside immutable source full N");new_count[i]++;literal_load[a]++;new_body++;}
    else {new_new++;throw runtime_error("new-new edge");}
   }
   long long extra;need(!c.next(extra),"candidate trailing data");need(old_body==SM&&!s.next(extra),"missing old edge");
  }
  need(new_body==422400&&new_new==0,"new body cardinality");
  long long d64=0,d70=0,load0=0,load6=0;
  for(int u=0;u<OLD;u++){need(literal_load[u]==load[u],"per-old-vertex literal pin load differs");need(deg[u]==64+load[u],"per-old degree binding");if(load[u]==0)load0++;else if(load[u]==6)load6++;else throw runtime_error("old load outside0or6");}
  for(int i=0;i<K;i++)need(new_count[i]==64&&deg[OLD+i]==64,"new degree/full N exactness");
  for(int d:deg){if(d==64)d64++;else if(d==70)d70++;else throw runtime_error("unexpected degree");}
  need(d64==96250&&d70==70400,"candidate degree histogram");
  const double t_parse=cpu();
  ofstream csv(out+"/NEW_ROOT_BFS.csv");csv<<"root,copy,base_index,center,predicted_class,d0,d1,d2,d3,reached,max_distance,histogram_prediction_match,cpu_seconds\n";
  vector<int>dist(N,-1),q(N);array<long long,4>minhist={N,N,N,N},maxhist={0,0,0,0};
  long long actualA=0,actualB=0;int completed=0,planned=K;double bfs_cpu=0,pilot_cpu=0,pilot_prediction=0;bool pilot_full=true;
  for(int i=0;i<planned;i++){
   double bt=cpu();fill(dist.begin(),dist.end(),-1);int h=0,t=0;int r=OLD+i;dist[r]=0;q[t++]=r;
   // Ordinary FIFO queue BFS through radius3. Vertices at distance3 need
   // not be expanded: the acceptance obligation is that all N were reached.
   while(h<t){int u=q[h++];if(dist[u]==3)continue;for(int j=0;j<deg[u];j++){int v=adj[(size_t)u*D+j];if(dist[v]<0){dist[v]=dist[u]+1;q[t++]=v;}}}
   array<long long,4>hist={0,0,0,0};int mx=0;for(int d:dist){need(d>=0&&d<=3,"new root fails R3");hist[d]++;mx=max(mx,d);}need(t==N,"new root misses vertices");
   int b=i%BASE;bool typeA=source_bonus_count[b]!=0;array<long long,4>expected=typeA?array<long long,4>{1,64,3191,163394}:array<long long,4>{1,64,3254,163331};need(hist==expected,"per-root distance histogram prediction failed");if(typeA)actualA++;else actualB++;
   double bc=cpu()-bt;bfs_cpu+=bc;completed++;csv<<r<<','<<i/BASE<<','<<b<<','<<centers[b]<<','<<(typeA?"A":"B");for(int j=0;j<4;j++){csv<<','<<hist[j];minhist[j]=min(minhist[j],hist[j]);maxhist[j]=max(maxhist[j],hist[j]);}csv<<','<<t<<','<<mx<<",true,"<<setprecision(9)<<bc<<'\n';
   if(completed==10){pilot_cpu=bfs_cpu;pilot_prediction=(cpu()-t0)+pilot_cpu/10*(K-10);pilot_full=pilot_prediction<allowance-5;if(!pilot_full)planned=10;cout<<"PILOT10_CPU="<<pilot_cpu<<" PREDICTED_VALIDATOR_TOTAL="<<pilot_prediction<<" PLAN="<<planned<<endl;}
   need(cpu()-t0<allowance-1,"validator CPU allowance exhausted");
  }
  csv.close();if(completed==K)need(actualA==132&&actualB==6468,"all-root histogram prediction aggregate");const double done=cpu();
  ofstream result(out+"/RAW_RESULT.json");result<<setprecision(12);
  result<<"{\n  \"status\": \"PASS\",\n  \"vertices\": "<<N<<",\n  \"edges\": "<<M<<",\n  \"source_vertices\": "<<OLD<<",\n  \"source_edges\": "<<SM<<",\n  \"old_literal_body_exact\": true,\n  \"source_literal_sorted_simple_regular64\": true,\n  \"clone_instances\": "<<K<<",\n  \"distinct_base_centers\": "<<BASE<<",\n  \"full_source_neighborhood_exact_each\": 64,\n  \"new_edges\": "<<new_body<<",\n  \"new_new_edges\": "<<new_new<<",\n  \"source_induced_distinct_base_center_edges\": "<<source_center_edges<<",\n  \"degree_histogram\": {\"64\": "<<d64<<", \"70\": "<<d70<<"},\n  \"old_pin_load_histogram\": {\"0\": "<<load0<<", \"6\": "<<load6<<"},\n  \"max_old_pin_load\": "<<maxload<<",\n  \"all_old_pin_loads_individually_bound\": true,\n  \"new_root_BFS_runs\": "<<completed<<",\n  \"old_root_BFS_runs\": 0,\n  \"new_root_BFS_reach_each\": "<<N<<",\n  \"new_root_BFS_histogram_min\": ["<<minhist[0]<<','<<minhist[1]<<','<<minhist[2]<<','<<minhist[3]<<"],\n  \"new_root_BFS_histogram_max\": ["<<maxhist[0]<<','<<maxhist[1]<<','<<maxhist[2]<<','<<maxhist[3]<<"],\n  \"pilot10_BFS_CPU_seconds\": "<<pilot_cpu<<",\n  \"pilot_predicted_validator_total_CPU_seconds\": "<<pilot_prediction<<",\n  \"pilot_permitted_all6600\": "<<(pilot_full?"true":"false")<<",\n  \"per_root_histogram_prediction_match\": true,\n  \"actual_histogram_class_A_roots\": "<<actualA<<",\n  \"actual_histogram_class_B_roots\": "<<actualB<<",\n  \"CPU_seconds\": {\"source_parse_full_neighborhoods\": "<<t_source-t0<<", \"candidate_literal_binding\": "<<t_parse-t_source<<", \"new_root_BFS\": "<<bfs_cpu<<", \"whole_validator\": "<<done-t0<<"},\n  \"workers\": 1,\n  \"validator_CPU_allowance\": "<<allowance<<"\n}\n";
  cout<<"PASS literal m="<<M<<" old="<<old_body<<" added="<<new_body<<" degree64="<<d64<<" degree70="<<d70<<" maxload="<<maxload<<" BFS_new="<<completed<<" BFS_old=0 CPU="<<done-t0<<endl;
  return 0;
 }catch(const exception&e){cerr<<"FAIL "<<e.what()<<endl;return 1;}
}
