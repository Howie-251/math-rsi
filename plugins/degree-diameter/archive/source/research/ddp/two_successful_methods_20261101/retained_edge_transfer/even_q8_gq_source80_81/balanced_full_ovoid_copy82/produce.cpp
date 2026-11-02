#include <algorithm>
#include <array>
#include <cstdio>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using U=uint32_t;using Pair=std::pair<U,U>;
constexpr U SRCN=342290,SRCM=13862745,OLDN=342225,N=346515,M=14204970,K=4225;
struct Input{FILE*f;char b[1<<20];size_t at=0,sz=0;explicit Input(const char*p):f(fopen(p,"rb")){if(!f)throw std::runtime_error("sourceopen");}~Input(){fclose(f);}int ch(){if(at==sz){sz=fread(b,1,sizeof(b),f);at=0;if(!sz)return EOF;}return b[at++];}bool number(U&x){int c;do{c=ch();if(c==EOF)return false;}while(c<=32);x=0;do{x=x*10+U(c-'0');c=ch();}while(c>32&&c!=EOF);return true;}};
struct Output{FILE*f;char b[1<<20];size_t at=0;explicit Output(const char*p):f(fopen(p,"wb")){if(!f)throw std::runtime_error("outputopen");}void flush(){if(at&&fwrite(b,1,at,f)!=at)throw std::runtime_error("outputwrite");at=0;}void ch(char c){if(at==sizeof(b))flush();b[at++]=c;}void number(U x){char d[12];int n=0;do{d[n++]=char('0'+x%10);x/=10;}while(x);while(n)ch(d[--n]);}void pair(U a,U b){number(a);ch(' ');number(b);ch('\n');}void close(){flush();if(fclose(f))throw std::runtime_error("outputclose");f=nullptr;}~Output(){if(f){try{close();}catch(...){}}}};
void need(bool a,const char*m){if(!a)throw std::runtime_error(m);}
int main(int argc,char**argv){try{
 need(argc==3,"arguments");double start=double(clock())/CLOCKS_PER_SEC,budget=std::stod(argv[2]);
 auto tick=[&](){need(double(clock())/CLOCKS_PER_SEC-start<budget,"CPUbudget");};
 std::ifstream in("INPUT_TABLES.txt");U np,nl,a,b,j,oldn,oldm,srcn,srcm,degree;
 in>>np>>nl>>a>>b>>j>>oldn>>oldm>>srcn>>srcm>>degree;
 need(np==585&&nl==585&&a==9&&b==9&&j==65&&oldn==OLDN&&srcn==SRCN&&srcm==SRCM&&degree==81,"tableheader");
 std::vector<std::array<U,9>> lp(585),pl(585);std::array<U,65> spread{},ovoid{},ovowner{};std::array<U,585>owner{};
 for(auto&r:lp)for(U&x:r)in>>x;for(auto&r:pl)for(U&x:r)in>>x;for(U&x:spread)in>>x;for(U&x:owner)in>>x;need(bool(in),"tableparse");
 std::ifstream ov("OVOID_INPUT.txt");for(U i=0;i<65;i++){U idx;ov>>idx>>ovoid[i]>>ovowner[i];need(idx==i&&ovoid[i]<585&&ovowner[i]==owner[ovoid[i]],"ovoidphysicalbinding");}need(bool(ov),"ovoidparse");
 std::vector<int>centeridx(SRCN,-1);std::vector<U>centers(K),center_i(K),center_j(K);std::vector<bool>diagonal(K,false),isD(SRCN,false);
 std::vector<std::vector<U>>expected(K),actual(K);std::vector<U>pinload(SRCN,0),srcdeg(SRCN,0);std::vector<Pair>added;added.reserve(342225);
 std::ofstream centerfile("CENTERS.tsv"),pred("PREDICTED_NEWROOT_HISTOGRAMS.tsv"),efile("ORDERED_EXPECTED_N81.tsv");
 centerfile<<"index\ti\tovoid_point\tj\tspread_line\tcenter_label\tnew_label\tdiagonal\n";
 pred<<"index\tnew_label\tdiagonal\tr0\tr1\tr2\tr3\tstatus\n";efile<<"index\tcenter_label\tnew_label\tslot\tpin\n";
 for(U i=0;i<65;i++)for(U k=0;k<65;k++){
  U index=65*i+k,c=ovoid[i]*585+spread[k];need(centeridx[c]==-1,"duplicatecenter");centeridx[c]=index;centers[index]=c;center_i[index]=i;center_j[index]=k;diagonal[index]=k==owner[ovoid[i]];if(diagonal[index])isD[c]=true;
  auto&row=expected[index];for(U q:lp[spread[k]])for(U ell:pl[ovoid[i]]){U v=q*585+ell;if(v!=c)row.push_back(v);}
  if(diagonal[index])row.push_back(OLDN+k);std::sort(row.begin(),row.end());
  need(row.size()==81&&std::adjacent_find(row.begin(),row.end())==row.end(),"expectedNsize");
  for(U slot=0;slot<81;slot++){U v=row[slot];need(v<SRCN&&v!=c,"pinrange");need(++pinload[v]==1,"expectedpinsoverlap");added.emplace_back(v,SRCN+index);efile<<index<<'\t'<<c<<'\t'<<SRCN+index<<'\t'<<slot<<'\t'<<v<<'\n';}
  centerfile<<index<<'\t'<<i<<'\t'<<ovoid[i]<<'\t'<<k<<'\t'<<spread[k]<<'\t'<<c<<'\t'<<SRCN+index<<'\t'<<diagonal[index]<<'\n';
  pred<<index<<'\t'<<SRCN+index<<'\t'<<diagonal[index]<<"\t1\t81\t"<<(diagonal[index]?5249:5329)<<'\t'<<(diagonal[index]?341184:341104)<<"\tPREDICTION_ONLY_NOT_BFS\n";
 }
 efile.close();centerfile.close();pred.close();need(added.size()==342225,"addedcount");
 for(U v=0;v<SRCN;v++)need(pinload[v]==U(!isD[v]),"pinunion_not_source_minus_D65");
 std::sort(added.begin(),added.end());tick();
 Input source(argv[1]);U hn,hm;need(source.number(hn)&&source.number(hm)&&hn==SRCN&&hm==SRCM,"sourceheader");
 Output out("graph_d82_D3_n346515.edges");out.pair(N,M);size_t next=0;Pair prev(0,0),last(0,0);bool haveprev=false,havelast=false;uint64_t written=0;
 auto emit=[&](Pair e){need(e.first<e.second&&e.second<N,"outputlabel");need(!havelast||last<e,"outputstrictlex");out.pair(e.first,e.second);last=e;havelast=true;written++;};
 for(U e=0;e<SRCM;e++){
  U u,v;need(source.number(u)&&source.number(v),"sourcebodyearlyend");Pair edge(u,v);need(u<v&&v<SRCN&&(!haveprev||prev<edge),"sourcebodylabelsorder");prev=edge;haveprev=true;
  while(next<added.size()&&added[next]<edge)emit(added[next++]);emit(edge);
  srcdeg[u]++;srcdeg[v]++;if(centeridx[u]>=0)actual[centeridx[u]].push_back(v);if(centeridx[v]>=0)actual[centeridx[v]].push_back(u);
  if(e%262144==0)tick();
 }
 U extra;need(!source.number(extra),"sourceextraedges");while(next<added.size())emit(added[next++]);out.close();need(written==M,"outputedgecount");
 std::ofstream afile("ORDERED_ACTUAL_N81.tsv"),matching("CENTER_MATCHING.tsv");afile<<"index\tcenter_label\tnew_label\tslot\tpin\n";matching<<"left_index\tright_index\tleft_center\tright_center\n";
 U diag=0,matched_edges=0;
 for(U k=0;k<K;k++){
  std::sort(actual[k].begin(),actual[k].end());need(actual[k]==expected[k],"actual_immutable_source_N_mismatch");U internal=0;
  for(U slot=0;slot<81;slot++){U v=actual[k][slot];afile<<k<<'\t'<<centers[k]<<'\t'<<SRCN+k<<'\t'<<slot<<'\t'<<v<<'\n';if(centeridx[v]>=0){internal++;U z=U(centeridx[v]);need(!diagonal[k]&&z!=k,"diagonalcenteredge");if(k<z){matching<<k<<'\t'<<z<<'\t'<<centers[k]<<'\t'<<v<<'\n';matched_edges++;}}}
  need(internal==U(!diagonal[k]),"centerinducednotmatchingplusdiagonal");diag+=diagonal[k];
 }
 afile.close();matching.close();need(diag==65&&matched_edges==2080,"matchingcounts");
 U deg81=K,deg82=0;for(U v=0;v<SRCN;v++){need(srcdeg[v]==81,"parsed_sourcedegree");U d=srcdeg[v]+pinload[v];if(d==81)deg81++;else if(d==82)deg82++;else need(false,"finaldegree");}
 need(deg81==4290&&deg82==342225,"degreehist");
 std::ofstream prefix("PREFIX_DEGREES.csv");prefix<<"clones,current_n,current_m,pins_load1,old_load0,degree81_count,degree82_count,degree_cap\n";
 for(U k=0;k<=K;k++)prefix<<k<<','<<SRCN+k<<','<<SRCM+81*k<<','<<81*k<<','<<SRCN-81*k<<','<<SRCN-80*k<<','<<81*k<<",82\n";
 prefix.close();tick();
 std::cout<<std::setprecision(12)<<"{\"status\":\"PRODUCED_ONE_COMPLETE_GRAPH_AND_FULL_N81_INTERFACE_PENDING_FRESH_ACCEPTANCE\",\"n\":"<<N<<",\"m\":"<<M<<",\"source_n\":"<<SRCN<<",\"source_m\":"<<SRCM<<",\"source_parse_count\":1,\"centers\":4225,\"N_size\":81,\"expected_actual_ordered_rows\":342225,\"all_expected_actual_N_rows_equal\":true,\"pin_union\":342225,\"old_load0\":65,\"old_load1\":342225,\"degree81\":"<<deg81<<",\"degree82\":"<<deg82<<",\"retained_source_edges\":"<<SRCM<<",\"new_old_edges\":342225,\"new_new_edges\":0,\"center_matching_edges\":2080,\"center_induced_isolates\":65,\"header\":true,\"strictlex_body\":true,\"prefix_rows\":4226,\"predicted_diag_roots\":65,\"predicted_offdiag_roots\":4160,\"BFS_runs\":0,\"Lean_runs\":0,\"old_field_geometry_projection_checks\":0,\"accepted_graphs\":0,\"producer_CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";
 return 0;
 }catch(const std::exception&e){std::cerr<<"PRODUCTION_STOP: "<<e.what()<<'\n';return 2;}}
