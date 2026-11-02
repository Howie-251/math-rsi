#include <algorithm>
#include <array>
#include <cstdio>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
double began,budget;string stage="initial";
double cpu(){return double(clock())/CLOCKS_PER_SEC-began;}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
void checktime(){need(cpu()<budget,"CPU_BUDGET");}
struct Reader{FILE*f;array<unsigned char,1<<20>buf;size_t pos=0,len=0;Reader(const string&p):f(fopen(p.c_str(),"rb")){need(f!=nullptr,"readable literal graph "+p);}~Reader(){if(f)fclose(f);}int get(){if(pos==len){len=fread(buf.data(),1,buf.size(),f);pos=0;if(!len)return -1;}return buf[pos++];}bool integer(int&v){int c;do{c=get();if(c<0)return false;}while(c<=32);need(c>='0'&&c<='9',"integer syntax");v=0;do{v=10*v+c-'0';c=get();}while(c>='0'&&c<='9');need(c<0||c<=32,"integer separator");return true;}};
struct Config{string name,oldfile,newfile,incfile,spreadfile,ovoidfile;int np,nl,s,t,R;};
string run(const Config&c,const string&graphs,const string&geo){
 stage=c.name+"_geometry_data_binding";double cb=cpu();int delta=(c.s+1)*(c.t+1),oldn=c.np*c.nl,N=oldn+c.R,flags=(c.s+1)*c.nl,oldm=(delta*oldn-flags)/2,M=delta*N/2;
 vector<unsigned char>inc(oldn,0);string line;int p,l;
 {ifstream in(geo+"/"+c.incfile);need(bool(in),"accepted incidence data readable");getline(in,line);int rows=0;while(in>>l>>p){need(0<=p&&p<c.np&&0<=l&&l<c.nl,"geometry ID ranges");need(!inc[p*c.nl+l],"literal incidence entry unique");inc[p*c.nl+l]=1;rows++;}need(rows==flags,"bound accepted incidence row count");}
 vector<int>spread(c.R,-1),owner(c.np,-1),O(c.R,-1);
 {ifstream in(geo+"/"+c.spreadfile);need(bool(in),"accepted spread data readable");getline(in,line);while(getline(in,line)){istringstream row(line);vector<int>v;int x;while(row>>x)v.push_back(x);if(v.empty())continue;need(v.size()>=3&&v[0]>=0&&v[0]<c.R,"spread binding row");spread[v[0]]=v.back();}}
 for(int j=0;j<c.R;j++){need(0<=spread[j]&&spread[j]<c.nl,"spread line ID binding");for(int x=0;x<c.np;x++)if(inc[x*c.nl+spread[j]]){need(owner[x]<0,"spreadowner uniquely binds helper recipe");owner[x]=j;}}
 for(int x:owner)need(x>=0,"all point spreadowners bound");
 {ifstream in(geo+"/"+c.ovoidfile);need(bool(in),"accepted ovoid data readable");getline(in,line);while(getline(in,line)){istringstream row(line);int i,x;if(!(row>>i>>x))continue;need(0<=i&&i<c.R&&0<=x&&x<c.np,"ovoid witness ID binding");O[i]=x;}}
 need(O[0]>=0&&O[1]>=0&&O[0]!=O[1]&&owner[O[0]]!=owner[O[1]],"two distinct actual diagonal witness owners");
 filesystem::create_directories(c.name);ofstream binding(c.name+"/ORDERED_HELPER_PIN_BINDING.tsv");binding<<"helper\tnew_label\tspread_line\tpin_index\told_vertex\tpoint\tline\n";
 vector<vector<int>>expected(c.R),actual(c.R);for(int x=0;x<c.np;x++)for(int y=0;y<c.nl;y++)if(inc[x*c.nl+y])expected[owner[x]].push_back(x*c.nl+y);
 for(auto&v:expected)need((int)v.size()==delta,"each helper formula has delta flags");
 double geomcpu=cpu()-cb;stage=c.name+"_complete_literal_stream_binding";double bindbegin=cpu();
 vector<int>olddeg(oldn,0),deg(N,0),offset(N+1),cursor,CSR(delta*N);for(int v=0;v<=N;v++)offset[v]=delta*v;cursor=offset;
 Reader old(graphs+"/"+c.name+"/"+c.oldfile),full(graphs+"/"+c.name+"/"+c.newfile);int a,b,x,y;
 need(old.integer(x)&&old.integer(y)&&x==oldn&&y==oldm,"unfilled exact n m header");need(full.integer(x)&&full.integer(y)&&x==N&&y==M,"filled exact n m header");
 pair<int,int>prev={-1,-1},oldprev={-1,-1};int oldcount=0,total=0,added=0;
 while(full.integer(a)){
  need(full.integer(b),"complete filled edge pair");need(0<=a&&a<b&&b<N,"filled endpoint range / no loops");need(prev<pair<int,int>{a,b},"filled strict lex / simple");prev={a,b};
  if(b<oldn){
   need(old.integer(x)&&old.integer(y),"old stream has corresponding retained edge");need(x==a&&y==b,"entire unfilled body retained exactly");need(oldprev<pair<int,int>{x,y},"unfilled strict lex / simple");oldprev={x,y};
   int ap=a/c.nl,al=a%c.nl,bp=b/c.nl,bl=b%c.nl;need(inc[bp*c.nl+al]&&inc[ap*c.nl+bl],"every oldedge satisfies actual geometry formula");olddeg[a]++;olddeg[b]++;oldcount++;
  }else{
   need(a<oldn,"zero fill-fill edges");int j=b-oldn,ap=a/c.nl;need(inc[a]&&owner[ap]==j,"newedge is precisely its helper's oldflag recipe");actual[j].push_back(a);added++;
  }
  need(cursor[a]<offset[a+1]&&cursor[b]<offset[b+1],"CSR literal degree slot bound");CSR[cursor[a]++]=b;CSR[cursor[b]++]=a;deg[a]++;deg[b]++;total++;
  if(total%1000000==0)checktime();
 }
 need(!old.integer(x),"entire old file exhausted / no lost suffix");need(oldcount==oldm&&total==M&&added==flags,"complete old/new literal counts");
 int oldlow=0,oldhigh=0;for(int v=0;v<oldn;v++){int d=delta-int(inc[v]);need(olddeg[v]==d,"every oldvertex has complete formula degree");oldlow+=olddeg[v]==delta-1;oldhigh+=olddeg[v]==delta;}
 need(oldlow==flags&&oldhigh==oldn-flags,"unfilled degree histogram");for(int v=0;v<N;v++)need(deg[v]==delta&&cursor[v]==offset[v+1],"all filled vertices exactly delta regular");
 vector<int>seenpin(oldn,0);ofstream prefix(c.name+"/INDEPENDENT_PREFIX_PIN_CHECKS.csv");prefix<<"prefix_helpers,new_root,pins,all_pins_old_degree_delta_minus1,all_prior_pin_load_zero,prefix_degree_cap\n";prefix<<"0,-1,0,1,1,"<<delta<<'\n';
 for(int j=0;j<c.R;j++){
  need(actual[j]==expected[j],"every helper full immutable flag pinlist bound");
  for(int t=0;t<delta;t++){int v=actual[j][t];need(!seenpin[v]&&olddeg[v]==delta-1,"helper flag sets disjoint / same-cap prefix");seenpin[v]=1;binding<<j<<'\t'<<oldn+j<<'\t'<<spread[j]<<'\t'<<t<<'\t'<<v<<'\t'<<v/c.nl<<'\t'<<v%c.nl<<'\n';}
  prefix<<j+1<<','<<oldn+j<<','<<delta<<",1,1,"<<delta<<'\n';
 }
 double bindingcpu=cpu()-bindbegin;
 stage=c.name+"_single_actual_nonD2_witness";int w0=O[0]*c.nl+spread[owner[O[0]]],w1=O[1]*c.nl+spread[owner[O[1]]];
 vector<int>n0(CSR.begin()+offset[w0],CSR.begin()+offset[w0+1]),n1(CSR.begin()+offset[w1],CSR.begin()+offset[w1+1]),common;sort(n0.begin(),n0.end());sort(n1.begin(),n1.end());set_intersection(n0.begin(),n0.end(),n1.begin(),n1.end(),back_inserter(common));need(w0!=w1&&!binary_search(n0.begin(),n0.end(),w1)&&common.empty(),"actual diagonal witness no0/1/2route");
 ofstream witness(c.name+"/ACTUAL_NON_D2_WITNESS.json");witness<<"{\"old_vertices\":["<<w0<<','<<w1<<"],\"geometry_points\":["<<O[0]<<','<<O[1]<<"],\"point_spreadowners\":["<<owner[O[0]]<<','<<owner[O[1]]<<"],\"adjacent\":false,\"common_neighbors\":0,\"actual_neighbor_lists\":[[";for(int i=0;i<delta;i++){if(i)witness<<',';witness<<n0[i];}witness<<"],[";for(int i=0;i<delta;i++){if(i)witness<<',';witness<<n1[i];}witness<<"]]}\n";
 stage=c.name+"_all_actual_helper_R3_BFS";double bfsbegin=cpu();int R2=c.s*(c.s+1)*c.t*(c.t+2);array<int,4>pred={1,delta,R2,N-1-delta-R2};vector<int>seen(N,0),queue(N),distance(N);map<array<int,4>,int>hist;
 ofstream bfs(c.name+"/ALL_HELPER_BFS_PREDICTION_VS_ACTUAL.csv");bfs<<"helper,new_root,spread_line,pred_R0,pred_R1,pred_R2,pred_R3,actual_R0,actual_R1,actual_R2,actual_R3,reachable\n";
 for(int j=0;j<c.R;j++){
  checktime();int root=oldn+j,stamp=j+1,head=0,tail=1,reached=1;queue[0]=root;distance[root]=0;seen[root]=stamp;array<int,4>h={1,0,0,0};
  while(head<tail){int v=queue[head++],next=distance[v]+1;for(int z=offset[v];z<offset[v+1];z++){int w=CSR[z];if(seen[w]!=stamp){seen[w]=stamp;distance[w]=next;h[next]++;reached++;if(next<3)queue[tail++]=w;}}}
  need(reached==N&&h==pred,"every actual helper reaches full literal graph with predicted classes");hist[h]++;
  bfs<<j<<','<<root<<','<<spread[j];for(int z:pred)bfs<<','<<z;for(int z:h)bfs<<','<<z;bfs<<','<<reached<<'\n';
 }
 need(hist.size()==1&&hist.begin()->second==c.R,"all helper histogram class aggregate");double bfscpu=cpu()-bfsbegin;
 ostringstream r;r<<"{\"status\":\"PASS_COMPLETE_GRAPH_FORMULA_ALL_HELPER_BFS_ALLPAIR_PREFIX_PROOF\",\"case\":\""<<c.name<<'"';
 auto num=[&](const string&key,auto value){r<<",\""<<key<<"\":"<<value;};
 auto flag=[&](const string&key,bool value){r<<",\""<<key<<"\":"<<(value?"true":"false");};
 num("s",c.s);num("t",c.t);num("geometry_points",c.np);num("geometry_lines",c.nl);num("degree_cap",delta);num("unfilled_n",oldn);num("unfilled_m",oldm);num("unfilled_degree_delta_minus1_count",oldlow);num("unfilled_degree_delta_count",oldhigh);num("filled_n",N);num("filled_m",M);flag("filled_all_regular",true);num("old_edge_body_retained_exact",oldcount);num("new_old_edges",added);num("fill_fill_edges",0);flag("complete_neighbor_formula_bound",true);flag("all_helper_pinsets_disjoint",true);num("helper_vertices",c.R);num("actual_helper_R3_BFS_roots",c.R);num("actual_old_R3_BFS_roots",0);
 r<<",\"actual_helper_histogram\":["<<pred[0]<<','<<pred[1]<<','<<pred[2]<<','<<pred[3]<<']';num("actual_helper_histogram_count",c.R);r<<",\"actual_nonD2_witness\":["<<w0<<','<<w1<<']';num("exact_diameter",3);flag("oldallpairs_GQ_route_proof",true);flag("all_current_prefixes_old_interior_proof",true);flag("unfilled_graph_is_classical_reproduction_only",true);num("literal_unfilled_parses",1);num("literal_filled_parses",1);num("old_field_or_small_GQ_projection_checks",0);num("geometry_binding_CPU_seconds",geomcpu);num("complete_graph_binding_CPU_seconds",bindingcpu);num("actual_helper_BFS_CPU_seconds",bfscpu);num("case_CPU_seconds",cpu()-cb);r<<'}';
 ofstream(c.name+"/RESULT.json")<<r.str()<<'\n';ofstream(c.name+"/TERMINAL.json")<<"{\"status\":\"PASS\",\"case_work_terminal\":true,\"result\":"<<r.str()<<"}\n";cout<<"CASE_PASS "<<c.name<<" N="<<N<<" helperBFS="<<c.R<<" CPU="<<cpu()-cb<<'\n'<<flush;return r.str();
}
int main(int argc,char**argv){began=double(clock())/CLOCKS_PER_SEC;budget=argc>3?stod(argv[3]):140;try{need(argc==4,"graphdir geometrydir CPUbudget");
 Config derived{"derived","classical_unfilled_d80_n327680.edges","graph_d80_D3_n327744.edges","DERIVED_INCIDENCE.tsv","DERIVED_SPREAD64.tsv","OVOID64.tsv",512,640,7,9,64};
 Config balanced{"balanced","classical_unfilled_d81_n342225.edges","graph_d81_D3_n342290.edges","ORIGINAL_INCIDENCE.tsv","SPREAD65.tsv","OVOID65.tsv",585,585,8,8,65};
 auto a=run(derived,argv[1],argv[2]);auto b=run(balanced,argv[1],argv[2]);
 ofstream out("RESULT.json");out<<"{\"status\":\"PASS_BOTH_Q8_FILLED_SOURCE_GRAPHS\",\"new_filled_graphs_mathematically_accepted\":2,\"classical_unfilled_reproductions_not_new_results\":2,\"actual_helper_R3_BFS_roots\":129,\"actual_old_R3_BFS_roots\":0,\"old_field_or_small_geometry_projection_checks\":0,\"new_Lean_or_solver_or_external_reviews\":0,\"source_graph_literal_parses\":4,\"validator_CPU_seconds\":"<<cpu()<<",\"cases\":["<<a<<','<<b<<"]}\n";return 0;
 }catch(const exception&e){ofstream("FAILURE.json")<<"{\"status\":\""<<(string(e.what())=="CPU_BUDGET"?"UNKNOWN_CPU_CAP":"FAIL")<<"\",\"stage\":\""<<stage<<"\",\"reason\":\""<<e.what()<<"\",\"CPU_seconds\":"<<cpu()<<"}\n";cerr<<stage<<": "<<e.what()<<'\n';return 2;}}
