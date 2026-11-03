#include <algorithm>
#include <array>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Point=array<int,4>;
using Basis=array<Point,2>;
int m8[8][8],m64[64][64],inv8[8];
double startCPU,budget;string stage="initial";
double cpu(){return double(clock())/CLOCKS_PER_SEC-startCPU;}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
void checkpoint(const string&s){stage=s;ofstream("CHECKPOINT.json")<<"{\"stage\":\""<<s<<"\",\"validator_CPU_seconds\":"<<cpu()<<"}\n";need(cpu()<budget,"CPU_BUDGET");}
int mul8raw(int a,int b){int r=0;while(b){if(b&1)r^=a;b>>=1;a<<=1;if(a&8)a^=11;}return r;}
int B(const Point&x,const Point&y){return m8[x[0]][y[3]]^m8[x[1]][y[2]]^m8[x[1]][y[3]]^m8[y[0]][x[3]]^m8[y[1]][x[2]]^m8[y[1]][x[3]];}
int norm(int a,int b){return m8[a][a]^m8[a][b]^m8[b][b];}
int Q(const Point&x){return m8[x[0]][x[3]]^m8[x[1]][x[1]]^m8[x[1]][x[2]^x[3]]^m8[x[2]^x[3]][x[2]^x[3]];}
Point add(const Point&a,const Point&b){Point r{};for(int i=0;i<4;i++)r[i]=a[i]^b[i];return r;}
Point canonical(Point x){for(int a:x)if(a){for(int&i:x)i=m8[i][inv8[a]];return x;}throw runtime_error("zero projective vector");}
vector<int> linepoints(const Basis&b,const map<Point,int>&id){set<int>s;for(int a=0;a<8;a++)for(int c=0;c<8;c++)if(a||c){Point x{};for(int k=0;k<4;k++)x[k]=m8[a][b[0][k]]^m8[c][b[1][k]];auto it=id.find(canonical(x));need(it!=id.end(),"linepoint in canonical PG3");s.insert(it->second);}need(s.size()==9,"projective line has9points");return vector<int>(s.begin(),s.end());}
struct Geometry{int n;vector<vector<int>>lines;vector<int>pairline;long long projections=0,incidences=0,collinear_pairs=0;};
void geometry(Geometry&g,int line_size,int point_degree,const string&prefix){
 g.pairline.assign(g.n*g.n,-1);vector<int>degree(g.n,0);ofstream inc(prefix+"INCIDENCE.tsv");inc<<"line\tpoint\n";
 for(int l=0;l<(int)g.lines.size();l++){
  auto&v=g.lines[l];need((int)v.size()==line_size,"geometry line size "+prefix+to_string(l));
  for(int p:v){need(0<=p&&p<g.n,"geometry point range");degree[p]++;g.incidences++;inc<<l<<'\t'<<p<<'\n';}
  for(int i=0;i<line_size;i++)for(int j=0;j<i;j++){int p=v[i],q=v[j];need(p!=q&&g.pairline[p*g.n+q]<0,"two points have at most one line "+prefix);g.pairline[p*g.n+q]=g.pairline[q*g.n+p]=l;g.collinear_pairs++;}
 }
 for(int p=0;p<g.n;p++)need(degree[p]==point_degree,"point incidence degree "+prefix+to_string(p));
 ofstream proj(prefix+"ALL_NONINCIDENT_PROJECTIONS.csv");proj<<"point,line,projection_point,connector_line\n";
 for(int p=0;p<g.n;p++){
  if(p%32==0)need(cpu()<budget,"CPU_BUDGET");
  for(int l=0;l<(int)g.lines.size();l++){
   auto&v=g.lines[l];if(binary_search(v.begin(),v.end(),p))continue;int count=0,target=-1,connector=-1;
   for(int q:v)if(g.pairline[p*g.n+q]>=0){count++;target=q;connector=g.pairline[p*g.n+q];}
   need(count==1,"nonincident projection count "+prefix+"point="+to_string(p)+" line="+to_string(l)+" count="+to_string(count));
   proj<<p<<','<<l<<','<<target<<','<<connector<<'\n';g.projections++;
  }
 }
 need(g.projections==1LL*g.n*g.lines.size()-g.incidences,"all nonincident pairs accounted");
}
int main(int argc,char**argv){startCPU=double(clock())/CLOCKS_PER_SEC;budget=argc>1?stod(argv[1]):17.0;try{
 checkpoint("new_F8_F64_field_checks");
 for(int a=0;a<8;a++)for(int b=0;b<8;b++)m8[a][b]=mul8raw(a,b);
 for(int a=0;a<8;a++){need(m8[a][0]==0&&m8[a][1]==a,"F8zero/unit");if(a){int k=0;for(int b=1;b<8;b++)if(m8[a][b]==1){inv8[a]=b;k++;}need(k==1,"F8 unique inverse");}}
 for(int a=0;a<8;a++)for(int b=0;b<8;b++){need(m8[a][b]==m8[b][a],"F8 commutativity");for(int c=0;c<8;c++){need(m8[m8[a][b]][c]==m8[a][m8[b][c]],"F8 associativity");need(m8[a][b^c]==(m8[a][b]^m8[a][c]),"F8 distributivity");}}
 ofstream f8("F8_FIELD_TABLE.csv");f8<<"a,b,sum,product\n";for(int a=0;a<8;a++)for(int b=0;b<8;b++)f8<<a<<','<<b<<','<<(a^b)<<','<<m8[a][b]<<'\n';
 for(int x=0;x<64;x++)for(int y=0;y<64;y++){int a=x%8,b=x/8,c=y%8,d=y/8;m64[x][y]=(m8[a][c]^m8[b][d])+8*(m8[a][d]^m8[b][c]^m8[b][d]);}
 for(int x=0;x<64;x++){need(m64[x][0]==0&&m64[x][1]==x,"F64zero/unit");if(x){int k=0;for(int y=1;y<64;y++)k+=m64[x][y]==1;need(k==1,"F64 unique nonzero inverse");}}
 for(int x=0;x<64;x++)for(int y=0;y<64;y++){need(m64[x][y]==m64[y][x],"F64 commutativity");for(int z=0;z<64;z++){need(m64[m64[x][y]][z]==m64[x][m64[y][z]],"F64 associativity");need(m64[x][y^z]==(m64[x][y]^m64[x][z]),"F64 distributivity");}}
 ofstream f64("F64_FIELD_TABLE.csv");f64<<"a,b,sum,product\n";for(int x=0;x<64;x++)for(int y=0;y<64;y++)f64<<x<<','<<y<<','<<(x^y)<<','<<m64[x][y]<<'\n';
 ofstream tn("F64_TRACE_NORM.csv");tn<<"code,a,b,conjugate,power8,trace,norm\n";
 for(int x=0;x<64;x++){int a=x%8,b=x/8,conj=(a^b)+8*b,power=x;for(int k=0;k<3;k++)power=m64[power][power];need(power==conj,"F64 eighth-power conjugate");need((x^conj)==b,"F64 trace formula");need(m64[x][conj]==norm(a,b),"F64 norm formula");need((norm(a,b)==0)==(x==0),"F64 norm anisotropy");int sixtyfour=power;for(int k=0;k<3;k++)sixtyfour=m64[sixtyfour][sixtyfour];need(sixtyfour==x,"F64 Frobenius order");tn<<x<<','<<a<<','<<b<<','<<conj<<','<<power<<','<<b<<','<<norm(a,b)<<'\n';}
 int gram[4][4];for(int i=0;i<4;i++)for(int j=0;j<4;j++){Point x{},y{};x[i]=1;y[j]=1;gram[i][j]=B(x,y);}int rank=0;for(int c=0;c<4;c++){int r=rank;while(r<4&&!gram[r][c])r++;if(r==4)continue;for(int j=0;j<4;j++)swap(gram[r][j],gram[rank][j]);int inv=inv8[gram[rank][c]];for(int j=0;j<4;j++)gram[rank][j]=m8[gram[rank][j]][inv];for(int i=0;i<4;i++)if(i!=rank&&gram[i][c]){int a=gram[i][c];for(int j=0;j<4;j++)gram[i][j]^=m8[a][gram[rank][j]];}rank++;}need(rank==4,"Gram nondegenerate");
 checkpoint("canonical_PG3_and_RREF_lines");
 set<Point>ps;for(int v=1;v<4096;v++){int w=v;Point x{};for(int i=0;i<4;i++){x[i]=w%8;w/=8;}ps.insert(canonical(x));}
 vector<Point>points(ps.begin(),ps.end());need(points.size()==585,"585canonical PG3points");map<Point,int>pointid;ofstream pf("PG3_POINTS.tsv");pf<<"point\tx0\tx1\tx2\tx3\n";for(int i=0;i<585;i++){pointid[points[i]]=i;pf<<i;for(int a:points[i])pf<<'\t'<<a;pf<<'\n';}
 Geometry original;original.n=585;vector<Basis>bases;map<vector<int>,int>lineid;ofstream rref("ALL_4745_RREF_SUBSPACES.tsv");rref<<"subspace\tpivot0\tpivot1\tr00\tr01\tr02\tr03\tr10\tr11\tr12\tr13\tisotropic\tline\n";int spaces=0;
 for(int p=0;p<4;p++)for(int q=p+1;q<4;q++){
  vector<pair<int,int>>free;for(int j=p+1;j<4;j++)if(j!=q)free.push_back({0,j});for(int j=q+1;j<4;j++)free.push_back({1,j});int assignments=1;for(size_t j=0;j<free.size();j++)assignments*=8;
  for(int mask=0;mask<assignments;mask++){Basis basis{};basis[0][p]=basis[1][q]=1;int w=mask;for(auto[r,c]:free){basis[r][c]=w%8;w/=8;}bool iso=B(basis[0],basis[1])==0;int l=-1;if(iso){auto lp=linepoints(basis,pointid);l=original.lines.size();need(lineid.emplace(lp,l).second,"unique isotropic RREFline");original.lines.push_back(lp);bases.push_back(basis);}rref<<spaces++<<'\t'<<p<<'\t'<<q;for(auto row:basis)for(int a:row)rref<<'\t'<<a;rref<<'\t'<<iso<<'\t'<<l<<'\n';}
 }
 need(spaces==4745&&original.lines.size()==585,"4745allRREF /585isotropic lines");
 geometry(original,9,9,"ORIGINAL_");need(original.projections==336960,"original projection total");
 Point P={0,0,1,1};int Pid=pointid.at(P);long long bindingpairs=0;
 for(int i=0;i<585;i++){need(B(P,points[i])==points[i][0],"Pperp is x0=0");need(B(points[i],points[i])==0,"Gram alternating");for(int j=0;j<i;j++){const auto&x=points[i];const auto&y=points[j];int u=x[0]+8*x[1],v=x[2]+8*x[3],up=y[0]+8*y[1],vp=y[2]+8*y[3];int det=m64[u][vp]^m64[up][v];need((det/8)==B(x,y),"F64 trace determinant / Gram binding");need((Q(add(x,y))^Q(x)^Q(y))==B(x,y),"quadratic polar / Gram binding");need((original.pairline[i*585+j]>=0)==(B(x,y)==0),"isotropic incidence / Gram collinearity binding");bindingpairs++;}}
 checkpoint("full_ovoid65_and_spread65");
 vector<int>O;vector<array<int,3>>abn;for(int a=0;a<8;a++)for(int b=0;b<8;b++){int c=norm(a,b);O.push_back(pointid.at(Point{1,a,b^c,c}));abn.push_back({a,b,c});}O.push_back(Pid);need(set<int>(O.begin(),O.end()).size()==65,"65distinctovoidpoints");
 vector<int>isO(585,0);for(int p:O)isO[p]=1;for(int i=0;i<585;i++)need((Q(points[i])==0)==bool(isO[i]),"quadraticzero set is exactlyO65");
 ofstream opairs("OVOID65_ALL_PAIR_CHECKS.csv");opairs<<"i,j,B,expected_norm_or_one\n";int checkedpairs=0;for(int i=0;i<65;i++)for(int j=0;j<i;j++){int value=B(points[O[i]],points[O[j]]);int expected=i==64?1:norm(abn[i][0]^abn[j][0],abn[i][1]^abn[j][1]);need(value!=0&&value==expected,"O65 pair norm mechanism i="+to_string(i)+" j="+to_string(j));opairs<<i<<','<<j<<','<<value<<','<<expected<<'\n';checkedpairs++;}need(checkedpairs==2080,"2080ovoidpairs");
 ofstream omeet("OVOID65_LINE_INTERSECTIONS.csv");omeet<<"line,intersection_size,ovoid_point\n";for(int l=0;l<585;l++){int count=0,p=-1;for(int v:original.lines[l])if(isO[v]){count++;p=v;}need(count==1,"O65 full line coverage "+to_string(l));omeet<<l<<','<<count<<','<<p<<'\n';}
 vector<int>spread,spreadowner(585,-1);ofstream sf("SPREAD65.tsv");sf<<"spread\tlambda\toriginal_line\n";
 for(int lambda=0;lambda<65;lambda++){Basis b;if(lambda==64)b={Point{0,0,1,0},Point{0,0,0,1}};else{int a=lambda%8,c=lambda/8;b={Point{1,0,a,c},Point{0,1,c,a^c}};}need(B(b[0],b[1])==0,"F64slope isotropic");auto lp=linepoints(b,pointid);auto it=lineid.find(lp);need(it!=lineid.end(),"slope binds actual RREFline");spread.push_back(it->second);sf<<lambda<<'\t'<<lambda<<'\t'<<it->second<<'\n';for(int p:lp){need(spreadowner[p]<0,"spread65 disjoint");spreadowner[p]=lambda;}}
 need(set<int>(spread.begin(),spread.end()).size()==65,"65distinctspreadlines");for(int v:spreadowner)need(v>=0,"spread65 partition585");need(spreadowner[Pid]==64,"P on infinity spreadline");set<int>ovoidowners;ofstream of("OVOID65.tsv");of<<"i\tpoint\tx0\tx1\tx2\tx3\ta\tb\tnorm\tspreadowner\n";for(int i=0;i<65;i++){int p=O[i];need(ovoidowners.insert(spreadowner[p]).second,"65ovoidspreadowners distinct");of<<i<<'\t'<<p;for(int a:points[p])of<<'\t'<<a;if(i<64)for(int a:abn[i])of<<'\t'<<a;else of<<"\t-1\t-1\t-1";of<<'\t'<<spreadowner[p]<<'\n';}
 checkpoint("controlled_Payne_derived_geometry");
 vector<int>affine,old_to_derived(585,-1);ofstream dp("DERIVED_POINTS.tsv");dp<<"point\toriginal_point\tx0\tx1\tx2\tx3\n";for(int p=0;p<585;p++)if(points[p][0]==1){int d=affine.size();affine.push_back(p);old_to_derived[p]=d;dp<<d<<'\t'<<p;for(int a:points[p])dp<<'\t'<<a;dp<<'\n';}need(affine.size()==512,"512Payne affinepoints");
 Geometry derived;derived.n=512;map<vector<int>,int>derivedlineid;vector<int>old_line_to_derived(585,-1);ofstream dl("DERIVED_LINES.tsv");dl<<"line\ttype\toriginal_line\ta\tb\n";int throughP=0;
 for(int l=0;l<585;l++){const auto&v=original.lines[l];if(binary_search(v.begin(),v.end(),Pid)){throughP++;continue;}vector<int>q;for(int p:v)if(old_to_derived[p]>=0)q.push_back(old_to_derived[p]);need(q.size()==8,"old line retains8affinepoints");int d=derived.lines.size();derived.lines.push_back(q);need(derivedlineid.emplace(q,d).second,"distinct retained derivedline");old_line_to_derived[l]=d;dl<<d<<"\tretained\t"<<l<<"\t-1\t-1\n";}
 need(throughP==9&&derived.lines.size()==576,"9P-lines removed/576retainedlines");
 for(int a=0;a<8;a++)for(int b=0;b<8;b++){vector<int>q;for(int t=0;t<8;t++)q.push_back(old_to_derived[pointid.at(Point{1,a,b^t,t})]);sort(q.begin(),q.end());need(set<int>(q.begin(),q.end()).size()==8,"hyperbolicline8distinct");int d=derived.lines.size();need(derivedlineid.emplace(q,d).second,"distinct new hyperbolicline");derived.lines.push_back(q);dl<<d<<"\thyperbolic\t-1\t"<<a<<'\t'<<b<<'\n';}
 need(derived.lines.size()==640,"640derivedlines");geometry(derived,8,10,"DERIVED_");need(derived.projections==322560,"derived projection total");
 long long derivedrulepairs=0;for(int i=0;i<512;i++)for(int j=0;j<i;j++){const auto&x=points[affine[i]];const auto&y=points[affine[j]];bool sameH=x[1]==y[1]&&(x[2]^x[3])==(y[2]^y[3]);need((derived.pairline[i*512+j]>=0)==(B(x,y)==0||sameH),"derived isotropic-or-hyperbolic collinearity rule");derivedrulepairs++;}
 vector<int>isO64(512,0);ofstream o64("OVOID64.tsv");o64<<"i\tderived_point\toriginal_point\tx0\tx1\tx2\tx3\n";for(int i=0;i<64;i++){int d=old_to_derived[O[i]];need(d>=0&&!isO64[d],"O64 distinct retained points");isO64[d]=1;o64<<i<<'\t'<<d<<'\t'<<O[i];for(int a:points[O[i]])o64<<'\t'<<a;o64<<'\n';}
 ofstream o64meet("OVOID64_DERIVED_LINE_INTERSECTIONS.csv");o64meet<<"line,intersection_size,derived_ovoid_point\n";for(int l=0;l<640;l++){int count=0,p=-1;for(int v:derived.lines[l])if(isO64[v]){count++;p=v;}need(count==1,"O64 full derivedline coverage "+to_string(l));o64meet<<l<<','<<count<<','<<p<<'\n';}
 vector<int>derivedspreadowner(512,-1);ofstream ds("DERIVED_SPREAD64.tsv");ds<<"spread\tlambda\toriginal_line\tderived_line\n";for(int lambda=0;lambda<64;lambda++){int l=old_line_to_derived[spread[lambda]];need(l>=0,"noninfinity spreadline retained");ds<<lambda<<'\t'<<lambda<<'\t'<<spread[lambda]<<'\t'<<l<<'\n';for(int p:derived.lines[l]){need(derivedspreadowner[p]<0,"derivedspread64 disjoint");derivedspreadowner[p]=lambda;}}
 for(int s:derivedspreadowner)need(s>=0,"derivedspread partitions512");set<int>O64owners;for(int d=0;d<512;d++)if(isO64[d])need(O64owners.insert(derivedspreadowner[d]).second,"O64distinctspreadowners");need(O64owners.size()==64,"O64has64spreadowners");
 checkpoint("PASS_all_authorized_q8_checks");
 ofstream out("RESULT.json");out<<"{\"status\":\"PASS_Q8_FULL_OVOID_AND_CONTROLLED_PAYNE_GEOMETRY\",\"q\":8,\"F8_modulus\":\"x^3+x+1\",\"F64_modulus\":\"z^2+z+1\",\"field_addition\":\"XOR\",\"F8_associativity_triples\":512,\"F8_distributivity_triples\":512,\"F64_associativity_triples\":262144,\"F64_distributivity_triples\":262144,\"F64_trace_norm_conjugate_elements\":64,\"norm_anisotropic\":true,\"Gram_rank\":4,\"PG3_points\":585,\"all_RREF_subspaces\":4745,\"original_isotropic_lines\":585,\"original_line_size\":9,\"original_point_degree\":9,\"original_incidences\":"<<original.incidences<<",\"original_nonincident_projections\":"<<original.projections<<",\"original_collinear_pairs\":"<<original.collinear_pairs<<",\"Gram_trace_polar_incidence_binding_pairs\":"<<bindingpairs<<",\"ovoid65_points\":65,\"ovoid65_B_nonzero_pairs\":2080,\"ovoid65_every_line_meets_once\":true,\"spread65_lines\":65,\"spread65_partitions_points\":585,\"ovoid65_distinct_spreadowners\":65,\"P_original_point_id\":"<<Pid<<",\"P_spread_owner\":64,\"Payne_points\":512,\"Payne_retained_old_lines\":576,\"Payne_new_hyperbolic_lines\":64,\"Payne_lines\":640,\"Payne_line_size\":8,\"Payne_point_degree\":10,\"Payne_incidences\":"<<derived.incidences<<",\"Payne_nonincident_projections\":"<<derived.projections<<",\"Payne_collinear_pairs\":"<<derived.collinear_pairs<<",\"Payne_isotropic_or_hyperbolic_rule_pairs\":"<<derivedrulepairs<<",\"ovoid64_points\":64,\"ovoid64_every_derived_line_meets_once\":true,\"derived_spread64_lines\":64,\"derived_spread64_partitions_points\":512,\"ovoid64_distinct_spreadowners\":64,\"conditional_balanced_source\":{\"degree\":81,\"n\":342225,\"fill\":65,\"n_after_fill\":342290,\"product_centers\":4225},\"conditional_Payne_source\":{\"degree\":80,\"n\":327680,\"fill\":64,\"n_after_fill\":327744,\"product_centers\":4096},\"large_graphs_generated\":0,\"old_field_or_graph_checks\":0,\"BFS_runs\":0,\"Lean_runs\":0,\"solver_runs\":0,\"other_q_checked\":0,\"validator_CPU_seconds\":"<<cpu()<<"}\n";
 cout<<"PASS fieldlaws, original585/585/projections336960, O65/spread65, derived512/640/projections322560, O64/spread64 CPU="<<cpu()<<'\n';return 0;
 }catch(const exception&e){bool unknown=string(e.what())=="CPU_BUDGET";ofstream out("RESULT.json");out<<"{\"status\":\""<<(unknown?"UNKNOWN_CPU_CAP":"FAIL_COUNTEREXAMPLE")<<"\",\"stage\":\""<<stage<<"\",\"reason\":\""<<e.what()<<"\",\"validator_CPU_seconds\":"<<cpu()<<"}\n";ofstream(unknown?"UNKNOWN.json":"COUNTEREXAMPLE.json")<<"{\"stage\":\""<<stage<<"\",\"reason\":\""<<e.what()<<"\"}\n";cerr<<stage<<": "<<e.what()<<'\n';return unknown?3:2;}
}
