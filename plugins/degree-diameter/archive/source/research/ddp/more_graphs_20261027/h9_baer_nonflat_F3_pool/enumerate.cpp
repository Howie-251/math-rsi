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
using U=uint64_t;using P3=array<int,3>;using Key=array<int,21>;
struct Mask{U lo,hi;};
vector<int> members(Mask m){vector<int>v;while(m.lo){int j=__builtin_ctzll(m.lo);v.push_back(j);m.lo&=m.lo-1;}while(m.hi){int j=__builtin_ctzll(m.hi);v.push_back(64+j);m.hi&=m.hi-1;}return v;}
void setbit(Mask&m,int j){if(j<64)m.lo|=U(1)<<j;else m.hi|=U(1)<<(j-64);}
Key rref(array<Pt,3>a,int&rank){rank=0;for(int c=0;c<7;c++){int p=rank;while(p<3&&!a[p][c])p++;if(p==3)continue;swap(a[p],a[rank]);int s=I[a[rank][c]];for(int&v:a[rank])v=M[s][v];for(int r=0;r<3;r++)if(r!=rank&&a[r][c]){int f=a[r][c];for(int j=0;j<7;j++)a[r][j]=S[a[r][j]][M[f][a[rank][j]]];}rank++;if(rank==3)break;}Key k{};for(int r=0;r<3;r++)for(int j=0;j<7;j++)k[r*7+j]=a[r][j];return k;}
array<Pt,3> basis(Key k){array<Pt,3>b{};for(int r=0;r<3;r++)for(int j=0;j<7;j++)b[r][j]=k[r*7+j];return b;}
void basisjson(ostream&f,array<Pt,3>b){f<<'[';for(int j=0;j<3;j++){if(j)f<<',';ptjson(f,b[j]);}f<<']';}
struct Plane{Key key;vector<int>F3ids;int linepairs;};
struct Witness{int plane,baer;vector<int>ids;Key key;};
struct Rec{vector<int>pins;Witness w;vector<pair<int,int>>refs;};
int main(int argc,char**argv){try{
 require(argc==9,"usage enum COORD F11 F12 D11 D12 OUTDIR LIMIT OLDORBIT");double start=cpu();fields();string dir=argv[6],old=argv[8];double limit=stod(argv[7]);rlimit hard{(rlim_t)ceil(limit+1),(rlim_t)ceil(limit+1)};setrlimit(RLIMIT_CPU,&hard);
 vector<Pt>points(66430);{ifstream f(argv[1],ios::binary);for(auto&p:points)for(int&v:p){unsigned char c;require(bool(f.read((char*)&c,1)),"shortcoords");v=c;}}
 vector<unsigned short>fold[2];for(int d=0;d<2;d++){fold[d].resize(66430);ifstream f(argv[2+d],ios::binary);require(bool(f.read((char*)fold[d].data(),132860)),"shortfold");require(*max_element(fold[d].begin(),fold[d].end())==(d?41355:37470),"foldmax");}
 vector<int>degree[2];for(int d=0;d<2;d++){degree[d].resize(d?42398:37631);ifstream f(argv[4+d],ios::binary);for(int&v:degree[d]){unsigned char c;require(bool(f.read((char*)&c,1)),"shortdegree");v=c;}require(*max_element(degree[d].begin(),degree[d].end())==11+d,"degreecap");}
 vector<int>pointidx(pow9[7],-1),F3;for(int i=0;i<66430;i++){pointidx[code(points[i])]=i;if(all_of(points[i].begin(),points[i].end(),[](int x){return x<3;}))F3.push_back(i);}require(F3.size()==364,"F3pointsnot364");
 vector<P3>coeff(91);{ifstream f(dir+"/coefficient_points91.txt");int n;f>>n;require(n==91,"PG2pointcount");for(auto&p:coeff)for(int&x:p)f>>x;}
 vector<Mask>orbit(7560);{ifstream f(old+"/baer_masks.u64.bin",ios::binary);for(auto&m:orbit){require(bool(f.read((char*)&m.lo,8))&&bool(f.read((char*)&m.hi,8)),"shortorbit");require((m.hi>>27)==0&&members(m).size()==13,"badBaermask");}}
 vector<vector<int>>bm;for(auto m:orbit)bm.push_back(members(m));
 // Enumerate allF3maximal isotropic3spaces by independent pairwisepolar triples.
 bool orth[364][364];for(int i=0;i<364;i++)for(int j=0;j<364;j++)orth[i][j]=B(points[F3[i]],points[F3[j]])==0;
 set<Key>allplanes;long long independent=0,collinear=0;
 for(int i=0;i<364;i++)for(int j=i+1;j<364;j++)if(orth[i][j])for(int k=j+1;k<364;k++)if(orth[i][k]&&orth[j][k]){
  int rank;Key key=rref({points[F3[i]],points[F3[j]],points[F3[k]]},rank);if(rank==3){independent++;allplanes.insert(key);}else collinear++;
 }
 require(allplanes.size()==1120,"allF3planesnot1120");set<Key>oldflat;{ifstream f(dir+"/old_flat_bases.txt");int n;f>>n;require(n==364,"oldflatcount");for(int i=0;i<364;i++){array<Pt,3>b;for(auto&r:b)for(int&v:r)f>>v;int rank;Key key=rref(b,rank);require(rank==3&&allplanes.count(key),"oldflatnot inF3planes");oldflat.insert(key);}}require(oldflat.size()==364,"oldflatnotdistinct");
 vector<Plane>planes;long long nonflatLinePairs=0,oldflatLinePairs=0;ofstream full(dir+"/all_F3_planes.json");full<<"{\"total1120\":1120,\"records\":[";int ai=0;
 for(auto key:allplanes){auto b=basis(key);require(!Q(b[0])&&!Q(b[1])&&!Q(b[2])&&!B(b[0],b[1])&&!B(b[0],b[2])&&!B(b[1],b[2]),"notisotropicbasis");vector<int>ids13;
  for(auto c:coeff)if(c[0]<3&&c[1]<3&&c[2]<3){Pt v{};for(int k=0;k<7;k++)v[k]=A[A[M[c[0]][b[0][k]]][M[c[1]][b[1][k]]]][M[c[2]][b[2][k]]];int id=pointidx[code(norm(v))];require(id>=0,"F3planepointmissing");ids13.push_back(id);}require(set<int>(ids13.begin(),ids13.end()).size()==13,"F3plane13count");
  int lp=0;for(int i=0;i<13;i++)for(int j=i+1;j<13;j++)if(h9line(points[ids13[i]],points[ids13[j]]))lp++;bool isold=oldflat.count(key);
  if(ai++)full<<',';full<<"{\"RREF_basis\":";basisjson(full,b);full<<",\"F3_point_ids13\":";vecjson(full,ids13);full<<",\"old_flatplane\":"<<(isold?"true":"false")<<",\"H3_collinear_pointpairs\":"<<lp<<'}';
  if(isold)oldflatLinePairs+=lp;else{nonflatLinePairs+=lp;planes.push_back({key,ids13,lp});}
 }
 full<<"]}\n";full.close();require(planes.size()==756,"nonflatnot756");
 {ofstream p(dir+"/plane_calibration.json");p<<"{\"F3singularpoints\":364,\"independent_pairwisepolar_triples\":"<<independent<<",\"collinear_pairwisepolar_triples\":"<<collinear<<",\"RREF_maximal_isotropic3spaces\":1120,\"old_flatplanes_exactly_removed\":364,\"new_nonflat_planes\":756,\"old_flat_H3_collinear_pointpairs\":"<<oldflatLinePairs<<",\"nonflat_H3_collinear_pointpairs\":"<<nonflatLinePairs<<",\"Baer_orbit_reused\":7560,\"CPU_seconds\":"<<cpu()-start<<"}\n";}
 cerr<<"CALIBRATION 1120=364+756 nonflatH3pairs="<<nonflatLinePairs<<" cpu="<<cpu()-start<<'\n';
 map<vector<int>,int>classes[2];vector<Rec>records[2];map<int,long long>foldhist[2];long long rawallowed[2]{},feasible[2]{};int processed=0;bool profstop=false;double loopstart=cpu();
 ofstream plout(dir+"/nonflat_planes.json");plout<<"{\"records\":[";
 for(int pi=0;pi<756;pi++){
  if(cpu()-start>limit)break;auto&pl=planes[pi];auto b=basis(pl.key);vector<int>ids91;Mask allowed[2]{};
  for(int j=0;j<91;j++){Pt v{};for(int k=0;k<7;k++)v[k]=A[A[M[coeff[j][0]][b[0][k]]][M[coeff[j][1]][b[1][k]]]][M[coeff[j][2]][b[2][k]]];int id=pointidx[code(norm(v))];require(id>=0,"Q9planepointmissing");ids91.push_back(id);for(int d=0;d<2;d++)if(degree[d][fold[d][id]]<11+d)setbit(allowed[d],j);}require(set<int>(ids91.begin(),ids91.end()).size()==91,"Q9plane91count");
  if(processed)plout<<',';plout<<"{\"nonflat_plane_index\":"<<pi<<",\"RREF_basis\":";basisjson(plout,b);plout<<",\"F3_point_ids13\":";vecjson(plout,pl.F3ids);plout<<",\"Q9_point_ids91\":";vecjson(plout,ids91);plout<<'}';
  for(int bi=0;bi<7560;bi++)for(int d=0;d<2;d++){
   auto mask=orbit[bi];if((mask.lo&~allowed[d].lo)||(mask.hi&~allowed[d].hi))continue;rawallowed[d]++;vector<int>ids,pins;for(int j:bm[bi]){int id=ids91[j];ids.push_back(id);pins.push_back(fold[d][id]);}sort(pins.begin(),pins.end());pins.erase(unique(pins.begin(),pins.end()),pins.end());foldhist[d][pins.size()]++;if(pins.size()>size_t(11+d))continue;feasible[d]++;
   auto it=classes[d].find(pins);if(it==classes[d].end()){classes[d][pins]=records[d].size();records[d].push_back({pins,{pi,bi,ids,pl.key},{{pi,bi}}});}else records[d][it->second].refs.push_back({pi,bi});
  }
  processed++;
  if(processed==100){double elapsed=cpu()-loopstart,projected=cpu()-start+elapsed*(756-100)/100.;ofstream p(dir+"/profile100planes.json");p<<"{\"newplanes_processed\":100,\"Baer_occurrences\":756000,\"CPU_plane_enumeration\":"<<elapsed<<",\"projected_total_native_CPU\":"<<projected<<",\"distinct11\":"<<records[0].size()<<",\"distinct12\":"<<records[1].size()<<",\"native_limit\":"<<limit<<"}\n";p.close();cerr<<"PROFILE100 pools="<<records[0].size()<<','<<records[1].size()<<" projected="<<projected<<'\n';if(projected>limit){profstop=true;break;}}
 }
 plout<<"]}\n";plout.close();bool complete=processed==756;
 for(int d=0;d<2;d++){
  sort(records[d].begin(),records[d].end(),[](auto&a,auto&b){return a.pins<b.pins;});ofstream f(dir+"/pool"+to_string(11+d)+".json");f<<"{\"source_n\":"<<(d?42398:37631)<<",\"source_m\":"<<(d?245889:205329)<<",\"delta\":"<<11+d<<",\"complete756nonflat_scope\":"<<(complete?"true":"false")<<",\"records\":[";
  for(int i=0;i<(int)records[d].size();i++){if(i)f<<',';auto&r=records[d][i];auto&w=r.w;f<<"{\"pool_index\":"<<i<<",\"pins\":";vecjson(f,r.pins);f<<",\"anchor_cap\":"<<11+d-r.pins.size()<<",\"pin_current_degrees\":[";for(int j=0;j<(int)r.pins.size();j++){if(j)f<<',';f<<degree[d][r.pins[j]];}f<<"],\"raw_point_count\":13,\"witness_multiplicity\":"<<r.refs.size()<<",\"all_witness_plane_baer_refs\":[";for(int j=0;j<(int)r.refs.size();j++){if(j)f<<',';f<<'['<<r.refs[j].first<<','<<r.refs[j].second<<']';}f<<"],\"witness\":{\"nonflat_plane_index\":"<<w.plane<<",\"RREF_basis\":";basisjson(f,basis(w.key));f<<",\"Baer_orbit_index\":"<<w.baer<<",\"Baer_mask_words_u64\":[\""<<orbit[w.baer].lo<<"\",\""<<orbit[w.baer].hi<<"\"],\"Baer_point_indices13\":";vecjson(f,bm[w.baer]);f<<",\"original_point_ids13\":";vecjson(f,w.ids);f<<",\"original_point_coordinates13\":[";for(int j=0;j<13;j++){if(j)f<<',';ptjson(f,points[w.ids[j]]);}f<<"]}}";
  }f<<"]}\n";
 }
 {ofstream f(dir+"/native_result.json");f<<"{\"status\":\""<<(complete?"COMPLETE756_NONFLAT_F3_BAER_POOL":profstop?"PARTIAL_PROFILE_OVER_BUDGET":"PARTIAL_CPU_WINDOW")<<"\",\"total_F3_planes\":1120,\"old_flatplanes_removed\":364,\"nonflat_expected\":756,\"nonflat_processed\":"<<processed<<",\"Baer_orbit_reused\":7560,\"Baer_occurrences_processed\":"<<processed*7560<<",\"complete756nonflat_scope\":"<<(complete?"true":"false")<<",\"nonflat_H3_collinear_pointpairs\":"<<nonflatLinePairs<<",\"deltas\":[";
  for(int d=0;d<2;d++){if(d)f<<',';map<int,int>hist;for(auto&r:records[d])hist[r.pins.size()]++;f<<"{\"delta\":"<<11+d<<",\"raw_degree_allowed_occurrences\":"<<rawallowed[d]<<",\"degree_and_pincount_feasible_occurrences\":"<<feasible[d]<<",\"distinct_folded_pinsets\":"<<records[d].size()<<",\"pin_count_histogram\":{";bool first=true;for(auto[k,v]:hist){if(!first)f<<',';first=false;f<<'\"'<<k<<"\":"<<v;}f<<"},\"allowed_raw_fold_size_histogram\":{";first=true;for(auto[k,v]:foldhist[d]){if(!first)f<<',';first=false;f<<'\"'<<k<<"\":"<<v;}f<<"}}";}
  f<<"],\"native_CPU_seconds\":"<<cpu()-start<<",\"native_limit\":"<<limit<<",\"old_Baer_occurrences_repeated\":0,\"orbit_reenumerated\":false,\"BFS\":false,\"anchors\":false,\"new_graph\":false}\n";
 }
 cerr<<"FINAL nonflat="<<processed<<" pools="<<records[0].size()<<','<<records[1].size()<<" cpu="<<cpu()-start<<'\n';return 0;
 }catch(const exception&e){cerr<<e.what()<<'\n';return 2;}}
