#include <algorithm>
#include <sys/resource.h>
#include <cmath>
#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Pt=array<int,7>;
int A[9][9],M[9][9],S[9][9],I[9],NEG[9],pow9[8];
int EQ[6][4]={{1,2,3,4},{5,4,3,2},{2,0,3,5},{6,5,3,0},{0,1,3,6},{4,6,3,1}};
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
void require(bool yes,const string&msg){if(!yes)throw runtime_error(msg);}
void fields(){
 for(int a=0;a<9;a++){NEG[a]=(3-a%3)%3+3*((3-a/3)%3);
  for(int b=0;b<9;b++){
   A[a][b]=(a%3+b%3)%3+3*((a/3+b/3)%3);
   M[a][b]=((a%3*b%3-a/3*(b/3))%3+3)%3+3*((a%3*(b/3)+a/3*(b%3))%3);
  }}
 for(int a=0;a<9;a++)for(int b=0;b<9;b++)S[a][b]=A[a][NEG[b]];
 for(int a=1;a<9;a++)for(int b=1;b<9;b++)if(M[a][b]==1)I[a]=b;
 pow9[0]=1;for(int j=1;j<8;j++)pow9[j]=9*pow9[j-1];
}
Pt norm(Pt v){int lead=0;while(lead<7&&!v[lead])lead++;require(lead<7,"zero projective vector");int k=I[v[lead]];for(int&x:v)x=M[k][x];return v;}
int code(const Pt&v){int s=0;for(int j=0;j<7;j++)s+=pow9[j]*v[j];return s;}
int Q(const Pt&v){return S[A[A[M[v[0]][v[4]]][M[v[1]][v[5]]]][M[v[2]][v[6]]]][M[v[3]][v[3]]];}
int B(const Pt&x,const Pt&y){int s=M[x[3]][y[3]];for(int j=0;j<3;j++){s=A[s][M[x[j]][y[j+4]]];s=A[s][M[x[j+4]][y[j]]];}return s;}
vector<Pt> rows(const Pt&y){
 vector<Pt>r(7);for(int k=0;k<6;k++){auto*e=EQ[k];r[k][e[1]]=A[r[k][e[1]]][y[e[0]]];r[k][e[0]]=S[r[k][e[0]]][y[e[1]]];r[k][e[3]]=S[r[k][e[3]]][y[e[2]]];r[k][e[2]]=A[r[k][e[2]]][y[e[3]]];}
 r[6]={y[4],y[5],y[6],y[3],y[0],y[1],y[2]};return r;
}
vector<Pt> kernel(vector<Pt>a){
 vector<int>piv;int rank=0;
 for(int c=0;c<7;c++){int p=rank;while(p<int(a.size())&&!a[p][c])p++;if(p==int(a.size()))continue;swap(a[p],a[rank]);int scale=I[a[rank][c]];for(int&x:a[rank])x=M[scale][x];
  for(int r=0;r<int(a.size());r++)if(r!=rank&&a[r][c]){int f=a[r][c];for(int j=0;j<7;j++)a[r][j]=S[a[r][j]][M[f][a[rank][j]]];}
  piv.push_back(c);rank++;}
 vector<Pt>out;for(int c=0;c<7;c++)if(find(piv.begin(),piv.end(),c)==piv.end()){Pt v{};v[c]=1;for(int r=0;r<rank;r++)v[piv[r]]=NEG[a[r][c]];out.push_back(v);}return out;
}
int rankof(vector<Pt>a){
 int rank=0;for(int c=0;c<7;c++){int p=rank;while(p<int(a.size())&&!a[p][c])p++;if(p==int(a.size()))continue;swap(a[p],a[rank]);int scale=I[a[rank][c]];for(int&x:a[rank])x=M[scale][x];for(int r=rank+1;r<int(a.size());r++)if(a[r][c]){int f=a[r][c];for(int j=c;j<7;j++)a[r][j]=S[a[r][j]][M[f][a[rank][j]]];}rank++;}return rank;
}
bool h9line(const Pt&u,const Pt&v){for(auto&e:EQ)if(S[M[u[e[0]]][v[e[1]]]][M[u[e[1]]][v[e[0]]]]!=S[M[u[e[2]]][v[e[3]]]][M[u[e[3]]][v[e[2]]]])return false;return true;}
void vecjson(ostream&o,const vector<int>&v){o<<'[';for(size_t j=0;j<v.size();j++){if(j)o<<',';o<<v[j];}o<<']';}
void ptjson(ostream&o,const Pt&v){o<<'[';for(int j=0;j<7;j++){if(j)o<<',';o<<v[j];}o<<']';}
struct Witness{vector<int>ids,pins10;int center,a,b,bad;Pt y,x,z,u,v;};
struct Group{vector<int>pins;vector<int>witnesses;};
int main(int argc,char**argv){try{
 require(argc==6,"usage: enumerate COORDS FOLD DEGREES OUTDIR CPU_LIMIT");double start=cpu();fields();string outdir=argv[4];double limit=stod(argv[5]);rlimit hard{(rlim_t)ceil(limit+.5),(rlim_t)ceil(limit+.5)};setrlimit(RLIMIT_CPU,&hard);
 vector<Pt>points(66430);{ifstream f(argv[1],ios::binary);for(auto&p:points)for(int&x:p){unsigned char c;require(bool(f.read((char*)&c,1)),"short point cache");x=c;}}
 vector<unsigned short>fold(66430);{ifstream f(argv[2],ios::binary);require(bool(f.read((char*)fold.data(),2*fold.size())),"short fold cache");}require(*max_element(fold.begin(),fold.end())==37470,"wrongN11mapping");
 vector<int>degree(37631);{ifstream f(argv[3],ios::binary);for(int&d:degree){unsigned char c;require(bool(f.read((char*)&c,1)),"short degree file");d=c;}}require(*max_element(degree.begin(),degree.end())==11,"sourcecap mismatch");
 vector<int>index(pow9[7],-1);for(int p=0;p<66430;p++)index[code(points[p])]=p;
 map<vector<int>,int>classes;vector<Group>groups;vector<Witness>witnesses;long long rawlines=0,pointschecked=0,multiplebad=0,foldcollision=0,zerobad=0;int processed=0;bool time_stop=false,profile_stop=false;double profilecpu=0,projected=0,enumstart=cpu();
 for(int center=0;center<66430;center++){
  if(cpu()-start>limit){time_stop=true;break;}const Pt&y=points[center];auto K=kernel(rows(y));require(K.size()==3,"flatplane kernel not3");vector<Pt>basis{y};for(const Pt&v:K){auto test=basis;test.push_back(v);if(rankof(test)>int(basis.size()))basis.push_back(v);if(basis.size()==3)break;}require(basis.size()==3,"basis failure");Pt x=basis[1],z=basis[2];require(!Q(y)&&!Q(x)&&!Q(z)&&!B(y,x)&&!B(y,z)&&!B(x,z),"flatplane nonsingular");
  for(int a=0;a<9;a++)for(int b=0;b<9;b++){
   Pt u,v;for(int j=0;j<7;j++){u[j]=S[x[j]][M[a][y[j]]];v[j]=S[z[j]][M[b][y[j]]];}require(!h9line(u,v),"line unexpectedly H9");rawlines++;
   vector<int>ids,pins10,bads;bool good=true;
   for(int k=0;k<10;k++){
    Pt w;if(k==0)w=v;else{int t=k-1;for(int j=0;j<7;j++)w[j]=A[u[j]][M[t][v[j]]];}w=norm(w);int pid=index[code(w)];require(pid>=0,"point outside cache");pointschecked++;int pin=fold[pid];
    if(find(pins10.begin(),pins10.end(),pin)!=pins10.end()){foldcollision++;good=false;break;}
    ids.push_back(pid);pins10.push_back(pin);if(degree[pin]==11){bads.push_back(pin);if(bads.size()>1){multiplebad++;good=false;break;}}
   }
   if(!good)continue;require(pins10.size()==10,"wrong foldedimage size");if(bads.empty()){zerobad++;continue;}require(bads.size()==1,"wrong uniquefault count");
   sort(ids.begin(),ids.end());require(unique(ids.begin(),ids.end())==ids.end(),"duplicate originalpoint");sort(pins10.begin(),pins10.end());vector<int>pins9;for(int p:pins10)if(p!=bads[0]){require(degree[p]<11,"freepin saturated");pins9.push_back(p);}require(pins9.size()==9,"wrong ninepin size");
   int wi=witnesses.size();witnesses.push_back({ids,pins10,center,a,b,bads[0],y,x,z,norm(u),norm(v)});auto it=classes.find(pins9);if(it==classes.end()){classes[pins9]=groups.size();groups.push_back({pins9,{wi}});}else groups[it->second].witnesses.push_back(wi);
  }
  processed++;
  if(processed==1000){profilecpu=cpu()-enumstart;projected=cpu()-start+profilecpu*(66430-1000)/1000.;ofstream p(outdir+"/profile1000.json");p<<"{\"centers_processed\":1000,\"original_lines\":"<<rawlines<<",\"matching_original_lines\":"<<witnesses.size()<<",\"distinct9pinsets\":"<<groups.size()<<",\"CPU_seconds_enumeration\":"<<profilecpu<<",\"projected_total_native_CPU\":"<<projected<<",\"native_limit\":"<<limit<<"}\n";p.close();cerr<<"PROFILE1000 matching="<<witnesses.size()<<" pool="<<groups.size()<<" cpu="<<profilecpu<<" projected="<<projected<<'\n';if(projected>limit){profile_stop=true;break;}}
 }
 bool complete=processed==66430;sort(groups.begin(),groups.end(),[](auto&a,auto&b){return a.pins<b.pins;});
 {ofstream p(outdir+"/pool.json");p<<"{\"source_n\":37631,\"source_m\":205329,\"target_degree\":11,\"mandatory_pin_count\":9,\"anchor_cap\":2,\"complete_global_scope\":"<<(complete?"true":"false")<<",\"records\":[";
  for(int i=0;i<(int)groups.size();i++){if(i)p<<',';auto&g=groups[i];set<int>badset;for(int wi:g.witnesses)badset.insert(witnesses[wi].bad);vector<int>badids(badset.begin(),badset.end());p<<"{\"pool_index\":"<<i<<",\"pins\":";vecjson(p,g.pins);p<<",\"anchor_cap\":2,\"deleted_saturated_pins\":";vecjson(p,badids);p<<",\"geometric_line_multiplicity\":"<<g.witnesses.size()<<",\"geometric_witnesses\":[";
   for(int k=0;k<(int)g.witnesses.size();k++){if(k)p<<',';auto&w=witnesses[g.witnesses[k]];p<<"{\"center_original_label\":"<<w.center<<",\"center_coordinates\":";ptjson(p,w.y);p<<",\"plane_basis_y_x_z\":[";ptjson(p,w.y);p<<',';ptjson(p,w.x);p<<',';ptjson(p,w.z);p<<"],\"dual_coordinates\":[1,"<<w.a<<','<<w.b<<"],\"line_basis_coordinates\":[";ptjson(p,w.u);p<<',';ptjson(p,w.v);p<<"],\"original_point_labels\":";vecjson(p,w.ids);p<<",\"original_folded_image_size\":10,\"original_folded_pins\":";vecjson(p,w.pins10);p<<",\"deleted_saturated_pin\":"<<w.bad<<",\"deleted_pin_degree\":11}";
   }p<<"]}";
  }p<<"]}\n";
 }
 {ofstream p(outdir+"/native_result.json");p<<"{\"status\":\""<<(complete?"COMPLETE_GLOBAL_SINGLE_FAULT_DEGREE_ENUMERATION":profile_stop?"PARTIAL_PROFILE_OVER_BUDGET":"PARTIAL_CPU_WINDOW")<<"\",\"source_n\":37631,\"source_m\":205329,\"centers_expected\":66430,\"centers_processed\":"<<processed<<",\"original_lines_expected\":5380830,\"original_lines_processed\":"<<rawlines<<",\"complete_global_scope\":"<<(complete?"true":"false")<<",\"matching_original_lines\":"<<witnesses.size()<<",\"distinct9pinsets\":"<<groups.size()<<",\"merged_duplicate_witnesses\":"<<witnesses.size()-groups.size()<<",\"rawpoint_lookups\":"<<pointschecked<<",\"safe_early_rejects_two_distinct_saturated_foldpins\":"<<multiplebad<<",\"safe_early_rejects_foldimage_collision\":"<<foldcollision<<",\"complete10foldimages_with_zero_fault\":"<<zerobad<<",\"reused_old_zero_centers\":0,\"CPU_seconds_native\":"<<cpu()-start<<",\"CPU_seconds_profile1000\":"<<profilecpu<<",\"projected_total_native_CPU\":"<<projected<<",\"native_limit\":"<<limit<<",\"R4_search\":false,\"anchor_search\":false,\"BFS\":false,\"new_graph\":false}\n";}
 cerr<<"FINAL centers="<<processed<<" lines="<<rawlines<<" matching="<<witnesses.size()<<" pool="<<groups.size()<<" cpu="<<cpu()-start<<'\n';return 0;
 }catch(const exception&e){cerr<<e.what()<<'\n';return 2;}}
