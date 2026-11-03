#include <algorithm>
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
struct Record{vector<int>pins,ids;int center,a,b,multiplicity=1;Pt y,x,z,u,v;};
int main(int argc,char**argv){try{
 require(argc==7,"usage: enumerate COORDS FOLD RAWADJ EXCLUDED OUTDIR CPU_LIMIT");
 double start=cpu();fields();string outdir=argv[5];double limit=stod(argv[6]);
 vector<Pt>points(66430);{ifstream f(argv[1],ios::binary);for(auto&p:points)for(int&x:p){unsigned char c;require(bool(f.read((char*)&c,1)),"short point cache");x=c;}}
 vector<unsigned short>fold(66430);{ifstream f(argv[2],ios::binary);require(bool(f.read((char*)fold.data(),2*fold.size())),"short fold cache");}
 require(*max_element(fold.begin(),fold.end())==37470,"wrongN11core mapping");
 vector<int>index(pow9[7],-1);for(int p=0;p<66430;p++)index[code(points[p])]=p;
 set<int>excluded;{ifstream f(argv[4]);int p;while(f>>p)excluded.insert(p);}require(excluded.size()==118,"expected118 previously exhausted centers");
 vector<int>degree;{ifstream f(argv[3]);string line;while(getline(f,line)){if(line.empty()||line[0]=='#')continue;istringstream s(line);int u,v,d=0;s>>u;require(u==int(degree.size()),"wrongraw rows");while(s>>v)d++;degree.push_back(d);}}
 require(degree.size()==37628&&*max_element(degree.begin(),degree.end())==11,"wrongN11 source");long long sum=0;for(int d:degree)sum+=d;require(sum==410592,"wrongN11edgecount");
 map<vector<int>,int>pinclass;vector<Record>records;
 long long processed=0,rawlines=0,rejected=0,feasible=0,checkedpoints=0,duplicatepins=0;
 array<long long,10>reject_position{};map<int,long long>sizes;bool projected_stop=false,time_stop=false;double profile_cpu=0,projected_cpu=0;
 double enumeration_start=cpu();
 for(int center=0;center<66430;center++){
  if(excluded.count(center))continue;
  if(cpu()-start>limit){time_stop=true;break;}
  const Pt&y=points[center];auto K=kernel(rows(y));require(K.size()==3,"flatplane kernel not3");
  vector<Pt>basis{y};for(const Pt&v:K){auto test=basis;test.push_back(v);if(rankof(test)>int(basis.size()))basis.push_back(v);if(basis.size()==3)break;}require(basis.size()==3,"could not extend center basis");Pt x=basis[1],z=basis[2];
  require(!Q(y)&&!Q(x)&&!Q(z)&&!B(y,x)&&!B(y,z)&&!B(x,z),"flatplane not totally singular");
  for(int a=0;a<9;a++)for(int b=0;b<9;b++){
   Pt u,v;for(int j=0;j<7;j++){u[j]=S[x[j]][M[a][y[j]]];v[j]=S[z[j]][M[b][y[j]]];}
   require(!h9line(u,v),"external line unexpectedlyH9");rawlines++;
   vector<int>ids;ids.reserve(10);bool good=true;
   // Process infinity first, then t=0..8. A surviving line has every10point checked.
   for(int k=0;k<10;k++){
    Pt w;if(k==0)w=v;else{int t=k-1;for(int j=0;j<7;j++)w[j]=A[u[j]][M[t][v[j]]];}w=norm(w);
    int p=index[code(w)];require(p>=0,"generatedpoint outsideQcache");checkedpoints++;
    if(degree[fold[p]]>=11){rejected++;reject_position[k]++;good=false;break;}ids.push_back(p);
   }
   if(!good)continue;
   feasible++;sort(ids.begin(),ids.end());require(unique(ids.begin(),ids.end())==ids.end(),"duplicatepoint on line");
   vector<int>pins;for(int p:ids)pins.push_back(fold[p]);sort(pins.begin(),pins.end());pins.erase(unique(pins.begin(),pins.end()),pins.end());require(pins.size()<=10,"too many foldedpins");sizes[pins.size()]++;
   auto hit=pinclass.find(pins);if(hit!=pinclass.end()){duplicatepins++;records[hit->second].multiplicity++;}
   else{pinclass[pins]=records.size();records.push_back({pins,ids,center,a,b,1,y,x,z,norm(u),norm(v)});}
  }
  processed++;
  if(processed==1000){
   profile_cpu=cpu()-enumeration_start;projected_cpu=cpu()-start+profile_cpu*(66312-1000)/1000.;
   ofstream p(outdir+"/profile1000.json");p<<"{\"new_centers\":1000,\"raw_lines\":"<<rawlines<<",\"CPU_seconds_enumeration\":"<<profile_cpu<<",\"projected_total_native_CPU_seconds\":"<<projected_cpu<<",\"degree_feasible_original_lines\":"<<feasible<<",\"degree_feasible_distinct_pinsets\":"<<records.size()<<"}\n";
   cerr<<"PROFILE1000 CPU "<<profile_cpu<<" projected "<<projected_cpu<<" feasible "<<feasible<<'\n';
   if(projected_cpu>limit){projected_stop=true;break;}
  }
 }
 bool complete=processed==66312;
 {ofstream p(outdir+"/pool.json");p<<"{\"base_n\":37628,\"target_degree\":11,\"records\":[";
  for(size_t j=0;j<records.size();j++){if(j)p<<',';auto&r=records[j];p<<"{\"pins\":";vecjson(p,r.pins);p<<",\"anchor_cap\":"<<11-r.pins.size()<<",\"geometric_line_multiplicity\":"<<r.multiplicity<<",\"geometric_witnesses\":[{\"center_original_label\":"<<r.center<<",\"center_coordinates\":";ptjson(p,r.y);p<<",\"plane_basis_y_x_z\":[";ptjson(p,r.y);p<<',';ptjson(p,r.x);p<<',';ptjson(p,r.z);p<<"],\"dual_coordinates\":[1,"<<r.a<<','<<r.b<<"],\"line_basis_coordinates\":[";ptjson(p,r.u);p<<',';ptjson(p,r.v);p<<"],\"original_point_labels\":";vecjson(p,r.ids);p<<"}]}";}p<<"]}\n";}
 {ofstream p(outdir+"/native_result.json");p<<"{\"status\":\""<<(complete?"COMPLETE_GLOBAL_DEGREE_SCREEN":projected_stop?"PARTIAL_PROFILE_PROJECTED_OVER_BUDGET":"PARTIAL_CPU_LIMIT")<<"\",\"new_centers_expected\":66312,\"new_centers_processed\":"<<processed<<",\"reused_exhausted_centers\":118,\"reused_exhausted_original_lines\":9558,\"new_raw_lines_processed\":"<<rawlines<<",\"total_original_lines_covered\":"<<rawlines+9558<<",\"complete_all66430_center_scope\":"<<(complete?"true":"false")<<",\"new_degree_rejected_original_lines\":"<<rejected<<",\"new_degree_feasible_original_lines\":"<<feasible<<",\"degree_feasible_distinct_pinsets\":"<<records.size()<<",\"duplicate_feasible_fold_pinsets\":"<<duplicatepins<<",\"generated_points_actually_checked\":"<<checkedpoints<<",\"saturated_pin_early_rejections_by_point_position\":[";for(int k=0;k<10;k++){if(k)p<<',';p<<reject_position[k];}p<<"],\"feasible_pin_count_histogram\":{";bool first=true;for(auto[k,v]:sizes){if(!first)p<<',';first=false;p<<'"'<<k<<"\":"<<v;}p<<"},\"CPU_seconds_native\":"<<cpu()-start<<",\"CPU_seconds_profile1000\":"<<profile_cpu<<",\"projected_total_native_CPU_seconds\":"<<projected_cpu<<",\"BFS_performed\":false,\"anchors_optimized\":false,\"new_graph_generated\":false}\n";}
 cerr<<"TERMINAL newcenters "<<processed<<" lines "<<rawlines<<" distinct_feasible "<<records.size()<<" CPU "<<cpu()-start<<'\n';return 0;
 }catch(const exception&e){cerr<<e.what()<<'\n';return 2;}}
