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
using U=uint64_t;using P3=array<int,3>;using Key=array<int,21>;using LKey=array<int,14>;
struct Mask{U lo=0,hi=0;};
void setbit(Mask&m,int j){if(j<64)m.lo|=U(1)<<j;else m.hi|=U(1)<<(j-64);}
vector<int> members(Mask m){vector<int>a;while(m.lo){int j=__builtin_ctzll(m.lo);a.push_back(j);m.lo&=m.lo-1;}while(m.hi){int j=__builtin_ctzll(m.hi);a.push_back(j+64);m.hi&=m.hi-1;}return a;}
Key rref(vector<Pt>a,int&rank){rank=0;for(int c=0;c<7;c++){int p=rank;while(p<(int)a.size()&&!a[p][c])p++;if(p==(int)a.size())continue;swap(a[p],a[rank]);int sc=I[a[rank][c]];for(int&v:a[rank])v=M[sc][v];for(int r=0;r<(int)a.size();r++)if(r!=rank&&a[r][c]){int f=a[r][c];for(int j=0;j<7;j++)a[r][j]=S[a[r][j]][M[f][a[rank][j]]];}rank++;if(rank==(int)a.size())break;}Key k{};for(int r=0;r<(int)a.size();r++)for(int j=0;j<7;j++)k[r*7+j]=a[r][j];return k;}
vector<Pt> getbasis(Key k,int rows=3){vector<Pt>b(rows);for(int r=0;r<rows;r++)for(int j=0;j<7;j++)b[r][j]=k[r*7+j];return b;}
void basisjson(ostream&f,vector<Pt>b){f<<'[';for(int i=0;i<(int)b.size();i++){if(i)f<<',';ptjson(f,b[i]);}f<<']';}
struct Line{Key key;vector<int>ids10;vector<pair<int,int>>pairs;int eligible[2]{};vector<int>planes;};
struct Plane{Key key;int line;};
struct Witness{int plane,line,baer;vector<int>ids;};
struct Rec{vector<int>pins;Witness w;vector<pair<int,int>>refs;};
int main(int argc,char**argv){try{
 require(argc==9,"usage enum COORD F11 F12 D11 D12 DIR LIMIT OLDORBIT");double start=cpu();fields();string dir=argv[6],old=argv[8];double limit=stod(argv[7]);rlimit hard{(rlim_t)ceil(limit+1),(rlim_t)ceil(limit+1)};setrlimit(RLIMIT_CPU,&hard);
 vector<Pt>points(66430);{ifstream f(argv[1],ios::binary);for(auto&p:points)for(int&v:p){unsigned char c;require(bool(f.read((char*)&c,1)),"shortcoords");v=c;}}
 vector<unsigned short>fold[2];for(int d=0;d<2;d++){fold[d].resize(66430);ifstream f(argv[2+d],ios::binary);require(bool(f.read((char*)fold[d].data(),132860)),"shortfold");require(*max_element(fold[d].begin(),fold[d].end())==(d?41355:37470),"wrongfold");}
 vector<int>degree[2];for(int d=0;d<2;d++){degree[d].resize(d?42398:37631);ifstream f(argv[4+d],ios::binary);for(int&v:degree[d]){unsigned char c;require(bool(f.read((char*)&c,1)),"shortdegree");v=c;}require(*max_element(degree[d].begin(),degree[d].end())==11+d,"cap");}
 vector<int>index(pow9[7],-1),F3,F3index(66430,-1),partA(66430),partB(66430);for(int i=0;i<66430;i++){index[code(points[i])]=i;if(all_of(points[i].begin(),points[i].end(),[](int v){return v<3;})){F3index[i]=F3.size();F3.push_back(i);}int m=1;for(int j=0;j<7;j++){partA[i]+=m*(points[i][j]%3);partB[i]+=m*(points[i][j]/3);m*=3;}}require(F3.size()==364,"F3pointsnot364");
 vector<P3>coeff(91);{ifstream f(dir+"/coefficient_points91.txt");int n;f>>n;require(n==91,"coeffcount");for(auto&p:coeff)for(int&v:p)f>>v;}
 vector<Mask>orbit(7560);vector<vector<int>>bm;{ifstream f(old+"/baer_masks.u64.bin",ios::binary);for(auto&m:orbit){require(bool(f.read((char*)&m.lo,8))&&bool(f.read((char*)&m.hi,8)),"shortmasks");require((m.hi>>27)==0,"badmask");bm.push_back(members(m));require(bm.back().size()==13,"Baernot13");}}
 // All3640F3singularlines by RREF of polar projective pointpairs.
 set<LKey>linekeys;for(int i=0;i<364;i++)for(int j=i+1;j<364;j++)if(B(points[F3[i]],points[F3[j]])==0){int rank;Key k=rref({points[F3[i]],points[F3[j]]},rank);require(rank==2,"rank1line");LKey l;copy(k.begin(),k.begin()+14,l.begin());linekeys.insert(l);}require(linekeys.size()==3640,"F3linesnot3640");
 // PolarQ9point masks for each F3point via two F3dot products.
 int PW=(66430+63)/64;vector<vector<U>>polar(364,vector<U>(PW));vector<array<int,7>>digits(2187);for(int c=0;c<2187;c++){int v=c;for(int&x:digits[c]){x=v%3;v/=3;}}
 for(int pi=0;pi<364;pi++){auto x=points[F3[pi]];array<int,7>c={x[4],x[5],x[6],x[3],x[0],x[1],x[2]};vector<unsigned char>zero(2187);for(int k=0;k<2187;k++){int s=0;for(int j=0;j<7;j++)s+=c[j]*digits[k][j];zero[k]=s%3==0;}for(int p=0;p<66430;p++)if(zero[partA[p]]&&zero[partB[p]])polar[pi][p>>6]|=U(1)<<(p&63);}
 set<Key>oldF3;{ifstream f(dir+"/old_F3_planes.txt");int n;f>>n;require(n==1120,"oldplane count");for(int i=0;i<n;i++){Key k;for(int&v:k)f>>v;oldF3.insert(k);}}require(oldF3.size()==1120,"oldplanesnotdistinct");
 vector<Line>lines;vector<Plane>planes;map<Key,int>newseen;set<Key>stableSeen;long long prunedLines[2]{},bothPruned=0;long long commonCount=0;int minCommon=99999,maxCommon=0;
 auto fail=[&](int li,const string&message,int c1,int c2){ofstream f(dir+"/CLASSIFICATION_COUNTEREXAMPLE.json");f<<"{\"line_index\":"<<li<<",\"message\":\""<<message<<"\",\"count1\":"<<c1<<",\"count2\":"<<c2<<"}\n";throw runtime_error(message);};
 for(auto lk:linekeys){
  int li=lines.size();Key key{};copy(lk.begin(),lk.end(),key.begin());auto b=getbasis(key,2);Line L;L.key=key;
  for(int t=0;t<10;t++){Pt p{};for(int j=0;j<7;j++)p[j]=t==9?b[1][j]:A[b[0][j]][M[t][b[1][j]]];int id=index[code(norm(p))];require(id>=0,"line pointmissing");L.ids10.push_back(id);}require(set<int>(L.ids10.begin(),L.ids10.end()).size()==10,"line10count");
  int fixed=0;for(int p:L.ids10){Pt conjugate=points[p];for(int&v:conjugate)v=M[M[v][v]][v];int q=index[code(norm(conjugate))];require(find(L.ids10.begin(),L.ids10.end(),q)!=L.ids10.end(),"line notFrob-stable");if(q==p)fixed++;else if(p<q){L.pairs.push_back({p,q});for(int d=0;d<2;d++)if(fold[d][p]==fold[d][q]&&degree[d][fold[d][p]]<11+d)L.eligible[d]++;}}
  if(fixed!=4||L.pairs.size()!=3)fail(li,"F3linefixedpaircount",fixed,L.pairs.size());for(int d=0;d<2;d++)if(L.eligible[d]<(d?1:2))prunedLines[d]++;if(L.eligible[0]<2&&L.eligible[1]<1)bothPruned++;
  int rawU=index[code(b[0])],rawV=index[code(b[1])];require(rawU>=0&&rawV>=0&&F3index[rawU]>=0&&F3index[rawV]>=0,"linebasis notF3point");int iu=F3index[rawU],iv=F3index[rawV];int pivot0=0,pivot1=0;while(!b[0][pivot0])pivot0++;while(!b[1][pivot1])pivot1++;
  map<int,Pt>quotient;int common=0,lineRaw=0;
  for(int w=0;w<PW;w++){U bits=polar[iu][w]&polar[iv][w];while(bits){int bit=__builtin_ctzll(bits);bits&=bits-1;int p=w*64+bit;require(p<66430,"polar padding");common++;Pt v=points[p];int s0=v[pivot0];for(int j=0;j<7;j++)v[j]=S[v[j]][M[s0][b[0][j]]];int s1=v[pivot1];for(int j=0;j<7;j++)v[j]=S[v[j]][M[s1][b[1][j]]];if(all_of(v.begin(),v.end(),[](int x){return x==0;})){lineRaw++;continue;}v=norm(v);quotient.emplace(code(v),v);}}
  if(common!=820||lineRaw!=10||quotient.size()!=10)fail(li,"quotientconic classification",common,quotient.size());minCommon=min(minCommon,common);maxCommon=max(maxCommon,common);commonCount+=common;
  int stable=0,unstable=0;for(auto&kv:quotient){int rank;Key pk=rref({b[0],b[1],kv.second},rank);require(rank==3,"planerank");bool isF3=all_of(pk.begin(),pk.end(),[](int x){return x<3;});if(isF3){stable++;stableSeen.insert(pk);if(!oldF3.count(pk))fail(li,"unmatchedF3stableplane",stable,0);}else{unstable++;if(newseen.count(pk))fail(li,"nonstableplanehasmultipleF3lines",newseen[pk],li);int idx=planes.size();newseen[pk]=li;planes.push_back({pk,li});L.planes.push_back(idx);}}
  if(stable!=4||unstable!=6)fail(li,"stable-nonstable count",stable,unstable);lines.push_back(move(L));
 }
 require(lines.size()==3640&&planes.size()==21840&&stableSeen==oldF3,"global classification mismatch");
 {ofstream f(dir+"/classification.json");f<<"{\"F3singularlines\":3640,\"commonperpQ9points_min\":"<<minCommon<<",\"commonperpQ9points_max\":"<<maxCommon<<",\"quotientplanes_eachline\":10,\"stable_eachline\":4,\"nonstable_eachline\":6,\"distinct_stableF3planes\":1120,\"old1120_RREF_set_matches\":true,\"distinct_nonstable_planes\":21840,\"nonstable_planes_unique_F3line\":true,\"both_delta_linepruned\":"<<bothPruned<<",\"linepair_pruned11\":"<<prunedLines[0]<<",\"linepair_pruned12\":"<<prunedLines[1]<<",\"CPU_seconds\":"<<cpu()-start<<"}\n";}
 {ofstream f(dir+"/F3_lines.json");f<<"{\"records\":[";for(int i=0;i<3640;i++){if(i)f<<',';auto&L=lines[i];f<<"{\"line_index\":"<<i<<",\"RREF_basis\":";basisjson(f,getbasis(L.key,2));f<<",\"Q9point_ids10\":";vecjson(f,L.ids10);f<<",\"eligible_unsplit_pair_counts\":["<<L.eligible[0]<<','<<L.eligible[1]<<"],\"nonstable_plane_indices\":";vecjson(f,L.planes);f<<",\"taupairs\":[";for(int j=0;j<3;j++){if(j)f<<',';auto[p,q]=L.pairs[j];f<<"{\"point_ids\":["<<p<<','<<q<<"],\"fold11\":["<<fold[0][p]<<','<<fold[0][q]<<"],\"fold12\":["<<fold[1][p]<<','<<fold[1][q]<<"],\"eligible11\":"<<(fold[0][p]==fold[0][q]&&degree[0][fold[0][p]]<11?"true":"false")<<",\"eligible12\":"<<(fold[1][p]==fold[1][q]&&degree[1][fold[1][p]]<12?"true":"false")<<'}';}f<<"]}";}f<<"]}\n";}
 {ofstream f(dir+"/nonstable_planes.json");f<<"{\"records\":[";for(int i=0;i<21840;i++){if(i)f<<',';f<<"{\"plane_index\":"<<i<<",\"F3line_index\":"<<planes[i].line<<",\"RREF_basis\":";basisjson(f,getbasis(planes[i].key));f<<'}';}f<<"]}\n";}
 cerr<<"CLASSIFICATION lines3640 planes21840 pruned11="<<prunedLines[0]<<" pruned12="<<prunedLines[1]<<" cpu="<<cpu()-start<<'\n';
 map<vector<int>,int>classes[2];vector<Rec>records[2];long long rawallowed[2]{},feasible[2]{},bitmap[2]{};map<int,long long>foldhist[2];int processedLines=0;bool profileStop=false;double loopstart=cpu();
 for(int li=0;li<3640;li++){
  if(cpu()-start>limit)break;auto&L=lines[li];bool active[2]={L.eligible[0]>=2,L.eligible[1]>=1};
  if(active[0]||active[1])for(int pi:L.planes){auto b=getbasis(planes[pi].key);vector<int>ids91;Mask allowed[2]{};
   for(int j=0;j<91;j++){Pt v{};for(int k=0;k<7;k++)v[k]=A[A[M[coeff[j][0]][b[0][k]]][M[coeff[j][1]][b[1][k]]]][M[coeff[j][2]][b[2][k]]];int id=index[code(norm(v))];require(id>=0,"planepointmissing");ids91.push_back(id);for(int d=0;d<2;d++)if(active[d]&&degree[d][fold[d][id]]<11+d)setbit(allowed[d],j);}
   for(int bi=0;bi<7560;bi++)for(int d=0;d<2;d++)if(active[d]){bitmap[d]++;auto mask=orbit[bi];if((mask.lo&~allowed[d].lo)||(mask.hi&~allowed[d].hi))continue;rawallowed[d]++;vector<int>ids,pins;for(int j:bm[bi]){int id=ids91[j];ids.push_back(id);pins.push_back(fold[d][id]);}sort(pins.begin(),pins.end());pins.erase(unique(pins.begin(),pins.end()),pins.end());foldhist[d][pins.size()]++;if(pins.size()>size_t(11+d))continue;feasible[d]++;auto it=classes[d].find(pins);if(it==classes[d].end()){classes[d][pins]=records[d].size();records[d].push_back({pins,{pi,li,bi,ids},{{pi,bi}}});}else records[d][it->second].refs.push_back({pi,bi});}
  }
  processedLines++;
  if(processedLines==100){double elapsed=cpu()-loopstart,projected=cpu()-start+elapsed*(3640-100)/100.;ofstream f(dir+"/profile100lines.json");f<<"{\"F3lines_processed\":100,\"nominal_geometry_planes\":600,\"nominal_Baer_occurrences\":4536000,\"actual_bitmap_tests11\":"<<bitmap[0]<<",\"actual_bitmap_tests12\":"<<bitmap[1]<<",\"distinct11\":"<<records[0].size()<<",\"distinct12\":"<<records[1].size()<<",\"CPU_pool100lines\":"<<elapsed<<",\"projected_total_nativeCPU\":"<<projected<<",\"native_limit\":"<<limit<<"}\n";f.close();cerr<<"PROFILE100 bitmap="<<bitmap[0]<<','<<bitmap[1]<<" pools="<<records[0].size()<<','<<records[1].size()<<" projected="<<projected<<'\n';if(projected>limit){profileStop=true;break;}}
 }
 bool complete=processedLines==3640;
 for(int d=0;d<2;d++){
  sort(records[d].begin(),records[d].end(),[](auto&a,auto&b){return a.pins<b.pins;});ofstream f(dir+"/pool"+to_string(11+d)+".json");f<<"{\"source_n\":"<<(d?42398:37631)<<",\"source_m\":"<<(d?245889:205329)<<",\"delta\":"<<11+d<<",\"complete21840newplane_scope\":"<<(complete?"true":"false")<<",\"records\":[";
  for(int i=0;i<(int)records[d].size();i++){if(i)f<<',';auto&r=records[d][i];auto&w=r.w;f<<"{\"pool_index\":"<<i<<",\"pins\":";vecjson(f,r.pins);f<<",\"anchor_cap\":"<<11+d-r.pins.size()<<",\"pin_current_degrees\":[";for(int j=0;j<(int)r.pins.size();j++){if(j)f<<',';f<<degree[d][r.pins[j]];}f<<"],\"raw_point_count\":13,\"witness_multiplicity\":"<<r.refs.size()<<",\"all_witness_plane_baer_refs\":[";for(int j=0;j<(int)r.refs.size();j++){if(j)f<<',';f<<'['<<r.refs[j].first<<','<<r.refs[j].second<<']';}f<<"],\"witness\":{\"plane_index\":"<<w.plane<<",\"plane_RREF_basis\":";basisjson(f,getbasis(planes[w.plane].key));f<<",\"F3line_index\":"<<w.line<<",\"F3line_RREF_basis\":";basisjson(f,getbasis(lines[w.line].key,2));f<<",\"F3line_Q9point_ids10\":";vecjson(f,lines[w.line].ids10);f<<",\"Baer_orbit_index\":"<<w.baer<<",\"Baer_mask_words_u64\":[\""<<orbit[w.baer].lo<<"\",\""<<orbit[w.baer].hi<<"\"],\"Baer_point_indices13\":";vecjson(f,bm[w.baer]);f<<",\"original_point_ids13\":";vecjson(f,w.ids);f<<",\"original_point_coordinates13\":[";for(int j=0;j<13;j++){if(j)f<<',';ptjson(f,points[w.ids[j]]);}f<<"]}}";
  }f<<"]}\n";
 }
 {ofstream f(dir+"/native_result.json");f<<"{\"status\":\""<<(complete?"COMPLETE21840_NONSTABLE_GALOIS_PLANE_POOL":profileStop?"PARTIAL_PROFILE_OVER_BUDGET":"PARTIAL_CPU_WINDOW")<<"\",\"classification_F3lines\":3640,\"new_generatorplanes\":21840,\"oldstableplanes_exactly_excluded\":1120,\"F3lines_pool_processed\":"<<processedLines<<",\"complete21840newplane_scope\":"<<(complete?"true":"false")<<",\"nominal_Baer_occurrences_geometry\":165110400,\"actual_all598600planes_enumerated\":false,\"deltas\":[";
  for(int d=0;d<2;d++){if(d)f<<',';map<int,int>hist;for(auto&r:records[d])hist[r.pins.size()]++;f<<"{\"delta\":"<<11+d<<",\"linepair_threshold\":"<<(d?1:2)<<",\"F3lines_pruned_by_eligible_pair_rule\":"<<prunedLines[d]<<",\"generatorplanes_pruned_by_pair_rule\":"<<prunedLines[d]*6<<",\"nominal_Baer_occurrences_pruned_by_pair_rule\":"<<prunedLines[d]*6*7560<<",\"actual_bitmap_tests\":"<<bitmap[d]<<",\"raw_degree_allowed_occurrences\":"<<rawallowed[d]<<",\"degree_and_pincount_feasible_occurrences\":"<<feasible[d]<<",\"distinct_folded_pinsets\":"<<records[d].size()<<",\"pin_count_histogram\":{";bool first=true;for(auto[k,v]:hist){if(!first)f<<',';first=false;f<<'\"'<<k<<"\":"<<v;}f<<"},\"allowed_raw_fold_size_histogram\":{";first=true;for(auto[k,v]:foldhist[d]){if(!first)f<<',';first=false;f<<'\"'<<k<<"\":"<<v;}f<<"}}";}
  f<<"],\"native_CPU_seconds\":"<<cpu()-start<<",\"native_limit\":"<<limit<<",\"old1120_Baer_repeated\":false,\"orbit_reenumerated\":false,\"BFS\":false,\"anchor_search\":false,\"new_graph\":false}\n";
 }
 cerr<<"FINAL lines="<<processedLines<<" pools="<<records[0].size()<<','<<records[1].size()<<" cpu="<<cpu()-start<<'\n';return 0;
 }catch(const exception&e){cerr<<e.what()<<'\n';return 2;}}
