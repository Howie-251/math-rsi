#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;
constexpr int Q=17,K=48,N=816,D=12;
constexpr U SCOPE=84607626;
constexpr uint32_t FULL=(1U<<Q)-1;
int powers[K],inverse_element[N];uint16_t product[N][N];
clock_t began;double cpu_limit;string directory;bool found=false,timeout=false;
double elapsed(){return double(clock()-began)/CLOCKS_PER_SEC;}
U powerq(int n){U r=1;while(n--)r*=Q;return r;}
template<class T>void arr(ostream&o,const T&a){o<<'[';bool first=true;for(auto x:a){if(!first)o<<',';first=false;o<<x;}o<<']';}
struct Fiber{int phase;vector<array<int,5>>forms;vector<uint8_t>base;array<vector<uint8_t>,Q>tail;U epoch=0;};
struct Pattern{int source,anchor,pairs,variables;U scope;vector<int>phases;int basis[5][6]{};array<Fiber,K>fibers;};
struct Counts{U raw=0,legal=0,illegal=0,bfs=0;array<U,K>rejected{},passed{};};
struct Position{int pattern=0,lead=0,last=0;U prefix=0,local=0,global=0;};
vector<Pattern>patterns;vector<Counts>per;Counts all;Position next_position;U epoch=0,calibration_count=0;
ofstream calibration_log;
void pos_json(ostream&o,const Position&p){o<<"{\"pattern_index\":"<<p.pattern<<",\"lead\":"<<p.lead<<",\"prefix_code\":"<<p.prefix<<",\"last_coordinate\":"<<p.last<<",\"local_projective_index\":"<<p.local<<",\"global_index\":"<<p.global<<'}';}
void counts_json(ostream&o,const Counts&c){o<<"{\"processed_marked_inputs\":"<<c.raw<<",\"legal_marked_inputs\":"<<c.legal<<",\"illegal_marked_inputs\":"<<c.illegal<<",\"full_root_BFS\":"<<c.bfs<<",\"fiber_rejections_in_test_order\":";arr(o,c.rejected);o<<",\"fiber_passes_in_test_order\":";arr(o,c.passed);o<<'}';}
vector<int> fields_from_z(const Pattern&p,const array<int,5>&z){vector<int>x(7);for(int k=0,j=0;k<7;k++)if(k!=p.anchor){int value=0;for(int a=0;a<p.variables;a++)value+=z[a]*p.basis[a][j];x[k]=value%Q;j++;}return x;}
bool generators(const Pattern&p,const vector<int>&x,array<int,D>&S){
 for(int j=0;j<p.pairs;j++){S[2*j]=x[j]+Q*p.phases[j];S[2*j+1]=inverse_element[S[2*j]];}
 for(int j=2*p.pairs;j<D;j++)S[j]=x[p.pairs+j-2*p.pairs]+Q*24;
 // Generic actual-element legality, including repeated phases and phase zero.
 for(int j=0;j<D;j++){if(S[j]==0)return false;for(int k=0;k<j;k++)if(S[j]==S[k])return false;}
 return true;
}
void prepare_base(Fiber&f,const Pattern&p,const array<int,5>&z,U current_epoch){if(f.epoch==current_epoch)return;for(size_t i=0;i<f.forms.size();i++){int value=0;for(int k=0;k<p.variables-1;k++)value+=f.forms[i][k]*z[k];f.base[i]=value%Q;}f.epoch=current_epoch;}
bool covers(Fiber&f,const Pattern&p,const array<int,5>&z,U current_epoch){
 prepare_base(f,p,z,current_epoch);uint32_t seen=0;int losses=0,slack=int(f.forms.size())-Q;const auto&t=f.tail[z[p.variables-1]];
 for(size_t i=0;i<f.forms.size();i++){int value=f.base[i]+t[i];if(value>=Q)value-=Q;uint32_t bit=1U<<value;if(seen&bit){if(++losses>slack)return false;}else{seen|=bit;if(seen==FULL)return true;}}
 assert(seen==FULL);return true;
}
void calibration(Pattern&p,const Position&position,const array<int,5>&z,U current_epoch,const array<int,D>&S,bool legal){
 array<uint32_t,K>actual{},symbolic{};actual[0]=1;vector<int>level{0};
 for(int depth=0;depth<3;depth++){vector<int>next;for(int u:level)for(int s:S){int v=product[u][s];actual[v/Q]|=1U<<(v%Q);next.push_back(v);}level=move(next);}
 for(auto&f:p.fibers){prepare_base(f,p,z,current_epoch);for(size_t k=0;k<f.forms.size();k++){int value=f.base[k]+f.tail[z[p.variables-1]][k];if(value>=Q)value-=Q;symbolic[f.phase]|=1U<<value;}}
 assert(actual==symbolic);calibration_count++;
 calibration_log<<"{\"position\":";pos_json(calibration_log,position);calibration_log<<",\"source_cursor\":"<<p.source<<",\"legal\":"<<(legal?"true":"false")<<",\"z\":";arr(calibration_log,z);calibration_log<<",\"restored_fields\":";arr(calibration_log,fields_from_z(p,z));calibration_log<<",\"S\":";arr(calibration_log,S);calibration_log<<",\"actual_masks\":";arr(calibration_log,actual);calibration_log<<",\"symbolic_masks\":";arr(calibration_log,symbolic);calibration_log<<",\"all48_equal\":true}\n";calibration_log.flush();
}
void full_bfs_save(const Pattern&p,const Position&position,const array<int,5>&z,const array<int,D>&S){
 int dist[N],queue[N],head=0,tail=1;fill(dist,dist+N,-1);dist[0]=0;queue[0]=0;
 while(head<tail){int u=queue[head++],d=dist[u]+1;for(int s:S){int v=product[u][s];if(dist[v]<0){dist[v]=d;queue[tail++]=v;}}}
 int missing=0,diameter=0;array<int,N+1>hist{};for(int d:dist){missing+=(d<0||d>3);diameter=max(diameter,d);hist[d<0?N:d]++;}
 assert(tail==N&&missing==0&&diameter<=3);found=true;
 ofstream edges(directory+"/production.best.edges");edges<<N<<' '<<N*D/2<<'\n';int count=0;for(int u=0;u<N;u++)for(int s:S){int v=product[u][s];if(u<v){edges<<u<<' '<<v<<'\n';count++;}}assert(count==N*D/2);
 ofstream o(directory+"/production.best.json");o<<"{\"n\":816,\"m\":4896,\"degree\":12,\"target_D\":3,\"action_root\":3,\"encoding\":\"x+17*j\",\"source_cursor\":"<<p.source<<",\"position\":";pos_json(o,position);o<<",\"pair_phases\":";arr(o,p.phases);o<<",\"anchor_component\":"<<p.anchor<<",\"z\":";arr(o,z);o<<",\"fields\":";arr(o,fields_from_z(p,z));o<<",\"S\":";arr(o,S);o<<",\"root_missing\":"<<missing<<",\"diameter\":"<<diameter<<",\"bad_unordered_pairs\":0,\"root_distance_histogram\":{";bool first=true;for(int d=0;d<=N;d++)if(hist[d]){if(!first)o<<',';first=false;o<<'"'<<(d==N?-1:d)<<"\":"<<hist[d];}o<<"}}\n";
 cout<<"FOUND_D3 source="<<p.source<<" global="<<position.global<<" CPU="<<elapsed()<<endl;
}
void progress(const string&status){ofstream o(directory+"/progress.json");o<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"processed_inputs\":"<<all.raw<<",\"raw_scope\":"<<SCOPE<<",\"CPU_seconds\":"<<elapsed()<<",\"actual_full_root_BFS\":"<<all.bfs<<",\"position\":";pos_json(o,next_position);o<<",\"counts\":";counts_json(o,all);o<<"}\n";}
int main(int argc,char**argv){
 assert(argc==3);directory=argv[1];cpu_limit=stod(argv[2]);began=clock();powers[0]=1;for(int j=1;j<K;j++)powers[j]=3*powers[j-1]%Q;assert(powers[16]==1&&powers[8]==16&&powers[24]==16);
 for(int u=0;u<N;u++){int j=u/Q;inverse_element[u]=(Q-powers[(K-j)%K]*(u%Q)%Q)%Q+Q*((K-j)%K);for(int s=0;s<N;s++)product[u][s]=(u%Q+powers[j]*(s%Q))%Q+Q*((j+s/Q)%K);assert(product[u][inverse_element[u]]==0);}
 ifstream input(directory+"/inputs.txt");int count;input>>count;assert(count==1091);patterns.resize(count);per.resize(count);U total_scope=0;
 for(auto&p:patterns){input>>p.source>>p.anchor>>p.pairs>>p.variables>>p.scope;assert(p.pairs==5&&p.variables>=3&&p.variables<=5);p.phases.resize(p.pairs);for(int&j:p.phases)input>>j;for(int i=0;i<p.variables;i++)for(int j=0;j<6;j++)input>>p.basis[i][j];assert(p.anchor<p.pairs&&powers[p.phases[p.anchor]]!=1);assert(p.scope==(powerq(p.variables)-1)/(Q-1));total_scope+=p.scope;int previous=0;for(auto&f:p.fibers){int m;input>>f.phase>>m;assert(m>=Q&&m>=previous);previous=m;f.forms.resize(m);f.base.resize(m);for(auto&v:f.forms)for(int j=0;j<p.variables;j++)input>>v[j];for(int z=0;z<Q;z++){f.tail[z].resize(m);for(int k=0;k<m;k++)f.tail[z][k]=f.forms[k][p.variables-1]*z%Q;}}}assert(input&&total_scope==SCOPE);
 calibration_log.open(directory+"/in_prefix_mask_calibration.jsonl");
 for(int pindex=0;pindex<count&&!found&&!timeout;pindex++){auto&p=patterns[pindex];auto&pc=per[pindex];int last_index=p.variables-1;
  for(int lead=0;lead<p.variables&&!found&&!timeout;lead++){array<int,5>z{};z[lead]=1;U prefixes=lead<last_index?powerq(last_index-1-lead):1;auto&first=p.fibers[0];
   for(size_t k=0;k<first.forms.size();k++)first.base[k]=lead<last_index?first.forms[k][lead]:0;
   for(U prefix=0;prefix<prefixes&&!found&&!timeout;prefix++){++epoch;first.epoch=epoch;int last_start=lead==last_index?1:0,last_stop=lead==last_index?2:Q;
    for(int last=last_start;last<last_stop;last++){z[last_index]=last;Position position{pindex,lead,last,prefix,pc.raw,all.raw};next_position=position;
     if((all.raw&2047)==0&&elapsed()>=cpu_limit){timeout=true;break;}
     auto fields=fields_from_z(p,z);array<int,D>S;bool legal=generators(p,fields,S);
     // Calibrate only actual members of the formal production prefix; no extra parameter or BFS.
     int first_field=0;for(int v:fields)if(v){first_field=v;break;}
     if(legal&&calibration_count==0&&first_field!=0&&first_field!=1)calibration(p,position,z,epoch,S,legal);
     pc.raw++;all.raw++;
     if(!legal){pc.illegal++;all.illegal++;}
     else{pc.legal++;all.legal++;bool all_pass=true;for(int f=0;f<K;f++){if(!covers(p.fibers[f],p,z,epoch)){pc.rejected[f]++;all.rejected[f]++;all_pass=false;break;}pc.passed[f]++;all.passed[f]++;}if(all_pass){pc.bfs++;all.bfs++;full_bfs_save(p,position,z,S);break;}}
     if(all.raw==100000||all.raw%5000000==0){progress("RUNNING");cout<<"PROGRESS raw="<<all.raw<<" legal="<<all.legal<<" BFS="<<all.bfs<<" CPU="<<elapsed()<<endl;if(all.raw==100000){ofstream o(directory+"/first100000.json");o<<setprecision(12)<<"{\"included_in_production_cursor\":true,\"processed_inputs\":100000,\"CPU_seconds\":"<<elapsed()<<",\"estimated_full_scope_CPU_at_this_prefix_rate\":"<<elapsed()*double(SCOPE)/100000<<",\"counts\":";counts_json(o,all);o<<"}\n";}}
    }
    // Prefix carry adds one modulo Q to each touched coordinate, including Q-1 -> 0.
    if(prefix+1<prefixes){for(int k=last_index-1;k>lead;k--){z[k]=(z[k]+1)%Q;for(size_t f=0;f<first.forms.size();f++){int value=first.base[f]+first.forms[f][k];first.base[f]=value>=Q?value-Q:value;}if(z[k]!=0)break;}}
   }
  }
  if(!found&&!timeout){assert(pc.raw==p.scope&&pc.raw==pc.legal+pc.illegal);cout<<"PATTERN_COMPLETE index="<<pindex<<" source="<<p.source<<" raw="<<pc.raw<<" legal="<<pc.legal<<" BFS="<<pc.bfs<<" CPU="<<elapsed()<<endl;progress("RUNNING");}
 }
 if(!found&&!timeout){assert(all.raw==SCOPE);assert(calibration_count==1);}string status=found?"FOUND_D3":timeout?"CPU_LIMIT_PREFIX_SAVED":"COMPLETE_REDUCED_FIVEPAIR_SCOPE_NO_SOLUTION";U completed=0;for(int i=0;i<count;i++)completed+=per[i].raw==patterns[i].scope;
 ofstream o(directory+"/terminal.json");o<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"running\":false,\"raw_scope\":"<<SCOPE<<",\"processed_inputs\":"<<all.raw<<",\"patterns_scope\":1091,\"patterns_completed\":"<<completed<<",\"actual_full_root_BFS\":"<<all.bfs<<",\"saved_best_graph\":"<<(found?"true":"false")<<",\"counts\":";counts_json(o,all);o<<",\"next_position\":";if(timeout)pos_json(o,next_position);else o<<"null";o<<",\"per_pattern\":[";
 for(int k=0;k<count;k++){if(k)o<<',';o<<"{\"pattern_index\":"<<k<<",\"source_cursor\":"<<patterns[k].source<<",\"scope\":"<<patterns[k].scope<<",\"counts\":";counts_json(o,per[k]);o<<'}';}
 o<<"],\"in_prefix_exact_short_word_calibrations\":"<<calibration_count<<",\"calibration_additional_BFS\":0,\"CPU_seconds\":"<<elapsed()<<",\"other_symbolic_survivors_processed\":0,\"new_random_seeds\":0}\n";o.close();progress(status);cout<<status<<" raw="<<all.raw<<" BFS="<<all.bfs<<" CPU="<<elapsed()<<endl;
}
