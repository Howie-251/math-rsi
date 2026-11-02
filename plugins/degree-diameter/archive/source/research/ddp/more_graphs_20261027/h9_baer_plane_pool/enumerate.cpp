#include <algorithm>
#include <cstdint>
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
using U=uint64_t;using P3=array<int,3>;
struct Mask{U lo=0,hi=0;bool operator<(const Mask&b)const{return pair(lo,hi)<pair(b.lo,b.hi);}};
void setbit(Mask&m,int i){if(i<64)m.lo|=U(1)<<i;else m.hi|=U(1)<<(i-64);}
vector<int> members(Mask m){vector<int>v;while(m.lo){int j=__builtin_ctzll(m.lo);v.push_back(j);m.lo&=m.lo-1;}while(m.hi){int j=__builtin_ctzll(m.hi);v.push_back(j+64);m.hi&=m.hi-1;}return v;}
P3 norm3(P3 p){int j=0;while(j<3&&!p[j])j++;require(j<3,"zero P3");int k=I[p[j]];for(int&x:p)x=M[k][x];return p;}
int code3(P3 p){return p[0]+9*p[1]+81*p[2];}
struct Witness{int center,plane,baer;vector<int>ids;Pt y,x,z;};
struct Rec{vector<int>pins;Witness first;vector<pair<int,int>>refs;};
int main(int argc,char**argv){try{
 require(argc==9,"usage: enum COORD FOLD11 FOLD12 DEG11 DEG12 OUT LIMIT UNUSED");double start=cpu();fields();string dir=argv[6];double limit=stod(argv[7]);rlimit hard{(rlim_t)ceil(limit+1),(rlim_t)ceil(limit+1)};setrlimit(RLIMIT_CPU,&hard);
 vector<Pt>points(66430);{ifstream f(argv[1],ios::binary);for(auto&p:points)for(int&x:p){unsigned char c;require(bool(f.read((char*)&c,1)),"short coord");x=c;}}
 vector<unsigned short>fold[2];for(int k=0;k<2;k++){fold[k].resize(66430);ifstream f(argv[2+k],ios::binary);require(bool(f.read((char*)fold[k].data(),132860)),"shortfold");require(*max_element(fold[k].begin(),fold[k].end())==(k?41355:37470),"wrongfoldmax");}
 vector<int>degree[2];for(int k=0;k<2;k++){degree[k].resize(k?42397:37631);ifstream f(argv[4+k],ios::binary);for(int&d:degree[k]){unsigned char c;require(bool(f.read((char*)&c,1)),"short degree");d=c;}require(*max_element(degree[k].begin(),degree[k].end())==11+k,"wrongdegreecap");}
 vector<int>pointidx(pow9[7],-1);vector<int>centers;for(int i=0;i<66430;i++){pointidx[code(points[i])]=i;if(all_of(points[i].begin(),points[i].end(),[](int x){return x<3;}))centers.push_back(i);}require(centers.size()==364,"F3centers not364");
 // Canonical PG2(F9) coefficient points and explicit projective generators.
 vector<P3>planePoints;vector<int>idx3(729,-1);for(int lead=0;lead<3;lead++){int tails=1;for(int j=lead+1;j<3;j++)tails*=9;for(int t=0;t<tails;t++){P3 p{};p[lead]=1;int v=t;for(int j=lead+1;j<3;j++){p[j]=v%9;v/=9;}idx3[code3(p)]=planePoints.size();planePoints.push_back(p);}}require(planePoints.size()==91,"PG2point count");
 int power=1,order4=0;do{power=M[power][4];order4++;}while(power!=1&&order4<9);require(order4==8,"4notprimitive");
 vector<vector<int>>perms(3,vector<int>(91));for(int gi=0;gi<3;gi++){vector<bool>used(91);for(int j=0;j<91;j++){P3 p=planePoints[j],q;if(gi==0)q={p[1],p[2],p[0]};if(gi==1)q={A[p[0]][p[1]],p[1],p[2]};if(gi==2)q={M[4][p[0]],p[1],p[2]};int v=idx3[code3(norm3(q))];require(v>=0&&!used[v],"generator notpermutation");used[v]=true;perms[gi][j]=v;}}
 Mask initial;for(int j=0;j<91;j++)if(all_of(planePoints[j].begin(),planePoints[j].end(),[](int x){return x<3;}))setbit(initial,j);require(members(initial).size()==13,"initialBaer not13");
 vector<Mask>orbit{initial};vector<int>parent{-1},parentgen{-1};map<Mask,int>which;which[initial]=0;
 for(int at=0;at<(int)orbit.size();at++){auto ids=members(orbit[at]);for(int gi=0;gi<3;gi++){Mask out;for(int j:ids)setbit(out,perms[gi][j]);auto it=which.find(out);if(it==which.end()){int id=orbit.size();which[out]=id;orbit.push_back(out);parent.push_back(at);parentgen.push_back(gi);}}}require(orbit.size()==7560,"orbit not7560");
 vector<vector<int>>baerMembers;for(auto m:orbit){baerMembers.push_back(members(m));require(baerMembers.back().size()==13,"wrong Baer cardinality");}
 {ofstream f(dir+"/baer_masks.u64.bin",ios::binary);for(auto m:orbit){f.write((char*)&m.lo,8);f.write((char*)&m.hi,8);}}
 {ofstream f(dir+"/orbit.json");f<<"{\"orbit_size\":7560,\"raw_points_per_Baer\":13,\"primitive4_order\":8,\"PGL3_9_order\":42456960,\"PGL3_3_order\":5616,\"orbit_stabilizer_quotient\":7560,\"coefficient_points_PG2F9\":[";for(int i=0;i<91;i++){if(i)f<<',';f<<'['<<planePoints[i][0]<<','<<planePoints[i][1]<<','<<planePoints[i][2]<<']';}f<<"],\"generator_permutations\":[";for(int i=0;i<3;i++){if(i)f<<',';vecjson(f,perms[i]);}f<<"],\"parent\":";vecjson(f,parent);f<<",\"generator\":";vecjson(f,parentgen);f<<",\"masks_file\":\"baer_masks.u64.bin\",\"mask_layout\":\"orbit-major pair(nativeuint64low64,high27),91coefficientpointindices\"}\n";}
 map<vector<int>,int>classes[2];vector<Rec>records[2];long long rawallowed[2]{},pinfeasible[2]{};map<int,long long>foldhist[2];int processed=0;bool limited=false,profileStop=false;double planeStart=cpu();
 ofstream planes(dir+"/planes.json");planes<<"{\"scope\":\"364F3center flatplanes only\",\"records\":[";
 for(int ci=0;ci<364;ci++){
  if(cpu()-start>limit){limited=true;break;}int center=centers[ci];Pt y=points[center];auto K=kernel(rows(y));require(K.size()==3,"badflatplane kernel");vector<Pt>basis{y};for(auto&v:K){auto test=basis;test.push_back(v);if(rankof(test)>int(basis.size()))basis.push_back(v);if(basis.size()==3)break;}require(basis.size()==3,"badbasis");Pt x=basis[1],z=basis[2];require(all_of(x.begin(),x.end(),[](int q){return q<3;})&&all_of(z.begin(),z.end(),[](int q){return q<3;}),"basisnotF3");require(!Q(y)&&!Q(x)&&!Q(z)&&!B(y,x)&&!B(y,z)&&!B(x,z),"planenottotallysingular");
  vector<int>ids91;Mask allowed[2];for(int j=0;j<91;j++){Pt p{};for(int k=0;k<7;k++)p[k]=A[A[M[planePoints[j][0]][y[k]]][M[planePoints[j][1]][x[k]]]][M[planePoints[j][2]][z[k]]];p=norm(p);int id=pointidx[code(p)];require(id>=0,"plane pointmissing");ids91.push_back(id);for(int d=0;d<2;d++)if(degree[d][fold[d][id]]<11+d)setbit(allowed[d],j);}require(set<int>(ids91.begin(),ids91.end()).size()==91,"planepoint collision");
  if(processed)planes<<',';planes<<"{\"plane_index\":"<<ci<<",\"center_original_label\":"<<center<<",\"basis_y_x_z\":[";ptjson(planes,y);planes<<',';ptjson(planes,x);planes<<',';ptjson(planes,z);planes<<"],\"point_ids91\":";vecjson(planes,ids91);planes<<'}';
  for(int bi=0;bi<7560;bi++)for(int d=0;d<2;d++){
   auto bm=orbit[bi];if((bm.lo&~allowed[d].lo)||(bm.hi&~allowed[d].hi))continue;rawallowed[d]++;vector<int>rawids,pins;for(int j:baerMembers[bi]){int id=ids91[j];rawids.push_back(id);pins.push_back(fold[d][id]);}sort(pins.begin(),pins.end());pins.erase(unique(pins.begin(),pins.end()),pins.end());foldhist[d][pins.size()]++;if(pins.size()>size_t(11+d))continue;pinfeasible[d]++;
   Witness w{center,ci,bi,rawids,y,x,z};auto it=classes[d].find(pins);if(it==classes[d].end()){classes[d][pins]=records[d].size();records[d].push_back({pins,w,{{ci,bi}}});}else records[d][it->second].refs.push_back({ci,bi});
  }
  processed++;
  if(processed==100){double elapsed=cpu()-planeStart;double projected=cpu()-start+elapsed*(364-100)/100.;ofstream p(dir+"/profile100planes.json");p<<"{\"planes_processed\":100,\"Baer_occurrences\":756000,\"CPU_plane_enumeration\":"<<elapsed<<",\"projected_total_nativeCPU\":"<<projected<<",\"distinct11\":"<<records[0].size()<<",\"distinct12\":"<<records[1].size()<<",\"native_limit\":"<<limit<<"}\n";p.close();cerr<<"PROFILE100 planesCPU="<<elapsed<<" projected="<<projected<<" pools="<<records[0].size()<<','<<records[1].size()<<'\n';if(projected>limit){profileStop=true;break;}}
 }
 planes<<"]}\n";planes.close();bool complete=processed==364;
 for(int d=0;d<2;d++){
  sort(records[d].begin(),records[d].end(),[](auto&a,auto&b){return a.pins<b.pins;});ofstream f(dir+"/pool"+to_string(11+d)+".json");f<<"{\"source_n\":"<<(d?42397:37631)<<",\"source_m\":"<<(d?245877:205329)<<",\"delta\":"<<11+d<<",\"complete364plane_scope\":"<<(complete?"true":"false")<<",\"records\":[";
  for(int i=0;i<(int)records[d].size();i++){if(i)f<<',';auto&r=records[d][i];auto&w=r.first;f<<"{\"pool_index\":"<<i<<",\"pins\":";vecjson(f,r.pins);f<<",\"anchor_cap\":"<<11+d-r.pins.size()<<",\"pin_current_degrees\":[";for(int j=0;j<(int)r.pins.size();j++){if(j)f<<',';f<<degree[d][r.pins[j]];}f<<"],\"raw_point_count\":13,\"witness_multiplicity\":"<<r.refs.size()<<",\"all_witness_plane_baer_refs\":[";for(int j=0;j<(int)r.refs.size();j++){if(j)f<<',';f<<'['<<r.refs[j].first<<','<<r.refs[j].second<<']';}f<<"],\"witness\":{\"center_original_label\":"<<w.center<<",\"plane_index\":"<<w.plane<<",\"plane_basis_y_x_z\":[";ptjson(f,w.y);f<<',';ptjson(f,w.x);f<<',';ptjson(f,w.z);f<<"],\"Baer_orbit_index\":"<<w.baer<<",\"Baer_mask_words_u64\":[\""<<orbit[w.baer].lo<<"\",\""<<orbit[w.baer].hi<<"\"],\"Baer_point_indices13\":";vecjson(f,baerMembers[w.baer]);f<<",\"original_point_ids13\":";vecjson(f,w.ids);f<<",\"original_point_coordinates13\":[";for(int j=0;j<13;j++){if(j)f<<',';ptjson(f,points[w.ids[j]]);}f<<"],\"contains_flatplane_center\":"<<(find(w.ids.begin(),w.ids.end(),w.center)!=w.ids.end()?"true":"false")<<"}}";
  }f<<"]}\n";
 }
 {ofstream f(dir+"/native_result.json");f<<"{\"status\":\""<<(complete?"COMPLETE364_F3_FLATPLANE_BAER_DEGREE_POOL":profileStop?"PARTIAL_PROFILE_OVER_BUDGET":"PARTIAL_CPU_WINDOW")<<"\",\"orbit_size\":7560,\"F3centers\":364,\"planes_processed\":"<<processed<<",\"Baer_occurrences_processed\":"<<processed*7560<<",\"complete364plane_scope\":"<<(complete?"true":"false")<<",\"deltas\":[";
  for(int d=0;d<2;d++){if(d)f<<',';map<int,int>hist;for(auto&r:records[d])hist[r.pins.size()]++;f<<"{\"delta\":"<<d+11<<",\"raw_degree_allowed_occurrences\":"<<rawallowed[d]<<",\"degree_and_pincount_feasible_occurrences\":"<<pinfeasible[d]<<",\"distinct_folded_pinsets\":"<<records[d].size()<<",\"distinct_pin_count_histogram\":{";bool first=true;for(auto[k,v]:hist){if(!first)f<<',';first=false;f<<'\"'<<k<<"\":"<<v;}f<<"},\"allowed_raw_fold_size_histogram\":{";first=true;for(auto[k,v]:foldhist[d]){if(!first)f<<',';first=false;f<<'\"'<<k<<"\":"<<v;}f<<"}}";}
  f<<"],\"native_CPU_seconds\":"<<cpu()-start<<",\"native_limit\":"<<limit<<",\"incidence_rebuilt\":false,\"WL_rebuilt\":false,\"BFS\":false,\"anchor_search\":false,\"new_graph\":false}\n";
 }
 cerr<<"FINAL planes="<<processed<<" pools="<<records[0].size()<<','<<records[1].size()<<" cpu="<<cpu()-start<<'\n';return 0;
 }catch(const exception&e){cerr<<e.what()<<'\n';return 2;}}
