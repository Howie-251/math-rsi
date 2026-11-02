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
constexpr int Q=31,K=30,N=930,D=11;
constexpr U SCOPE=1094587872ULL,PER_SCOPE=29583456ULL,PER_LEGAL=26782109ULL;
int powers[K],inverse_element[N];uint16_t product[N][N];
clock_t began;double cpu_limit;string directory;bool found=false,timeout=false;
double elapsed(){return double(clock()-began)/CLOCKS_PER_SEC;}
U pow31(int n){U r=1;while(n--)r*=31;return r;}
template<class T>void array_json(ostream&o,const T&a){o<<'[';bool first=true;for(auto x:a){if(!first)o<<',';first=false;o<<x;}o<<']';}
struct Fiber{int phase;vector<array<int,6>>forms;vector<uint8_t>base;array<vector<uint8_t>,31>tail;U epoch=0;};
struct Pattern{int source,anchor;U scope;array<int,4>phases;array<Fiber,30>fibers;};
struct Counts{U raw=0,legal=0,illegal=0,bfs=0;array<U,30>rejected{},passed{};};
struct Position{int pattern=0,lead=0,last=0;U prefix=0,local=0,global=0;};
vector<Pattern>patterns;vector<Counts>per;Counts all;Position next_position;U epoch=0,calibration_count=0;
array<int,6>best_z{};array<int,7>best_fields{};array<int,D>best_S{};array<int,N+1>best_hist{};int best_missing=N+1,best_diameter=-1,best_pattern=-1;Position best_position;
void pos_json(ostream&o,const Position&p){o<<"{\"pattern_index\":"<<p.pattern<<",\"lead\":"<<p.lead<<",\"prefix_code\":"<<p.prefix<<",\"last_coordinate\":"<<p.last<<",\"local_projective_index\":"<<p.local<<",\"global_index\":"<<p.global<<'}';}
void counts_json(ostream&o,const Counts&c){o<<"{\"processed_marked_inputs\":"<<c.raw<<",\"legal_marked_inputs\":"<<c.legal<<",\"illegal_marked_inputs\":"<<c.illegal<<",\"full_root_BFS\":"<<c.bfs<<",\"fiber_rejections_in_test_order\":";array_json(o,c.rejected);o<<",\"fiber_passes_in_test_order\":";array_json(o,c.passed);o<<'}';}
array<int,7>fields_from_z(const array<int,6>&z){array<int,7>x{};for(int j=0;j<6;++j)x[j+1]=z[j];return x;}
bool generators(const Pattern&p,const array<int,7>&x,array<int,D>&S){for(int j=0;j<4;++j){S[2*j]=x[j]+Q*p.phases[j];S[2*j+1]=inverse_element[S[2*j]];}for(int j=0;j<3;++j)S[8+j]=x[4+j]+Q*15;auto sorted=S;sort(sorted.begin(),sorted.end());return sorted[0]!=0&&adjacent_find(sorted.begin(),sorted.end())==sorted.end();}
void prepare_base(Fiber&f,const array<int,6>&z,U current_epoch){if(f.epoch==current_epoch)return;for(size_t i=0;i<f.forms.size();++i){int value=0;for(int k=0;k<5;++k)value+=f.forms[i][k]*z[k];f.base[i]=value%31;}f.epoch=current_epoch;}
bool covers(Fiber&f,const array<int,6>&z,U current_epoch){prepare_base(f,z,current_epoch);uint32_t seen=0;int losses=0,slack=int(f.forms.size())-31;const auto&t=f.tail[z[5]];
 for(size_t i=0;i<f.forms.size();++i){int value=f.base[i]+t[i];if(value>=31)value-=31;uint32_t bit=uint32_t(1)<<value;if(seen&bit){if(++losses>slack)return false;}else{seen|=bit;if(seen==0x7fffffffU)return true;}}
 assert(seen==0x7fffffffU);return true;
}
void calibration(Pattern&p,const array<int,6>&z,U current_epoch){
 auto fields=fields_from_z(z);array<int,D>S;generators(p,fields,S);array<uint32_t,30>actual{},symbolic{};actual[0]=1;
 vector<int>layer{0};for(int depth=0;depth<3;++depth){vector<int>next;for(int u:layer)for(int s:S){int v=product[u][s];actual[v/Q]|=uint32_t(1)<<(v%Q);next.push_back(v);}layer=move(next);}
 for(auto&f:p.fibers){prepare_base(f,z,current_epoch);for(size_t k=0;k<f.forms.size();++k){int value=f.base[k]+f.tail[z[5]][k];if(value>=31)value-=31;symbolic[f.phase]|=uint32_t(1)<<value;}}
 assert(actual==symbolic);calibration_count++;
}
void full_bfs(const Pattern&p,const Position&position,const array<int,6>&z,const array<int,D>&S){int dist[N],queue[N],head=0,tail=1;fill(dist,dist+N,-1);dist[0]=0;queue[0]=0;
 while(head<tail){int u=queue[head++],d=dist[u]+1;for(int s:S){int v=product[u][s];if(dist[v]<0){dist[v]=d;queue[tail++]=v;}}}
 int missing=0,diameter=0;for(int d:dist){missing+=(d<0||d>3);diameter=max(diameter,d);}if(tail<N)diameter=-1;
 if(missing<best_missing){best_missing=missing;best_diameter=diameter;best_pattern=position.pattern;best_position=position;best_z=z;best_fields=fields_from_z(z);best_S=S;best_hist.fill(0);for(int d:dist)best_hist[d<0?N:d]++;}
 // Every exact fiber passed, so this assertion also checks the screening/BFS connection.
 assert(missing==0&&tail==N&&diameter<=3);found=true;
 cout<<"FOUND_D3 source="<<p.source<<" global="<<position.global<<" CPU="<<elapsed()<<endl;
}
void save_best(){if(best_pattern<0)return;ofstream e(directory+"/production.best.edges");e<<N<<" 5115\n";int count=0;for(int u=0;u<N;++u)for(int s:best_S){int v=product[u][s];if(u<v){e<<u<<' '<<v<<'\n';count++;}}assert(count==5115);
 ofstream o(directory+"/production.best.json");o<<"{\"n\":930,\"m\":5115,\"degree\":11,\"action_root\":3,\"encoding\":\"x+31*j\",\"source_cursor\":"<<patterns[best_pattern].source<<",\"position\":";pos_json(o,best_position);o<<",\"pair_phases\":";array_json(o,patterns[best_pattern].phases);o<<",\"nullspace_z\":";array_json(o,best_z);o<<",\"fields\":";array_json(o,best_fields);o<<",\"S\":";array_json(o,best_S);o<<",\"root_missing\":"<<best_missing<<",\"diameter\":"<<best_diameter<<",\"bad_unordered_pairs\":"<<465LL*best_missing<<",\"root_distance_histogram\":{";bool first=true;for(int d=0;d<=N;++d)if(best_hist[d]){if(!first)o<<',';first=false;o<<'"'<<(d==N?-1:d)<<"\":"<<best_hist[d];}o<<"}}\n";
}
void progress(const string&status){ofstream o(directory+"/progress.json");o<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"processed_inputs\":"<<all.raw<<",\"raw_scope\":"<<SCOPE<<",\"CPU_seconds\":"<<elapsed()<<",\"actual_full_root_BFS\":"<<all.bfs<<",\"position\":";pos_json(o,next_position);o<<",\"counts\":";counts_json(o,all);o<<"}\n";}
int main(int argc,char**argv){assert(argc==3);directory=argv[1];cpu_limit=stod(argv[2]);began=clock();powers[0]=1;for(int j=1;j<K;++j)powers[j]=3*powers[j-1]%Q;assert(powers[15]==30);
 for(int u=0;u<N;++u){int j=u/Q;inverse_element[u]=(Q-powers[(K-j)%K]*(u%Q)%Q)%Q+Q*((K-j)%K);for(int s=0;s<N;++s)product[u][s]=(u%Q+powers[j]*(s%Q))%Q+Q*((j+s/Q)%K);assert(product[u][inverse_element[u]]==0);}
 ifstream input(directory+"/inputs.txt");int count;input>>count;assert(count==37);patterns.resize(count);per.resize(count);
 for(auto&p:patterns){input>>p.source>>p.anchor>>p.scope;assert(p.anchor==0&&p.scope==PER_SCOPE);for(int&j:p.phases)input>>j;int previous=0;for(auto&f:p.fibers){int m;input>>f.phase>>m;assert(m>=31&&m>=previous);previous=m;f.forms.resize(m);f.base.resize(m);for(auto&v:f.forms)for(int&x:v)input>>x;for(int z=0;z<31;++z){f.tail[z].resize(m);for(int k=0;k<m;++k)f.tail[z][k]=f.forms[k][5]*z%31;}}}assert(input);
 for(int pindex=0;pindex<count&&!found&&!timeout;++pindex){auto&p=patterns[pindex];auto&pc=per[pindex];
  for(int lead=0;lead<6&&!found&&!timeout;++lead){array<int,6>z{};z[lead]=1;U prefixes=lead<5?pow31(4-lead):1;auto&first=p.fibers[0];
   for(size_t k=0;k<first.forms.size();++k)first.base[k]=lead<5?first.forms[k][lead]:0;
   for(U prefix=0;prefix<prefixes&&!found&&!timeout;++prefix){++epoch;first.epoch=epoch;int last_start=lead==5?1:0,last_stop=lead==5?2:31;
    for(int last=last_start;last<last_stop;++last){z[5]=last;Position position{pindex,lead,last,prefix,pc.raw,all.raw};next_position=position;
     if((all.raw&8191)==0&&elapsed()>=cpu_limit){timeout=true;break;}
     // These three calibration coordinates are members of this exact production prefix.
     if(pindex==0&&(pc.raw==0||pc.raw==31||pc.raw==100000))calibration(p,z,epoch);
     pc.raw++;all.raw++;
     bool legal=z[3]!=z[4]&&z[3]!=z[5]&&z[4]!=z[5];
     if(!legal){pc.illegal++;all.illegal++;}
     else{pc.legal++;all.legal++;bool all_pass=true;
      for(int f=0;f<30;++f){if(!covers(p.fibers[f],z,epoch)){pc.rejected[f]++;all.rejected[f]++;all_pass=false;break;}pc.passed[f]++;all.passed[f]++;}
      if(all_pass){auto fields=fields_from_z(z);array<int,D>S;assert(generators(p,fields,S));pc.bfs++;all.bfs++;full_bfs(p,position,z,S);save_best();break;}
     }
     if(all.raw==100000||all.raw%5000000==0){progress("RUNNING");cout<<"PROGRESS raw="<<all.raw<<" legal="<<all.legal<<" BFS="<<all.bfs<<" CPU="<<elapsed()<<endl;
      if(all.raw==100000){ofstream o(directory+"/first100000.json");o<<setprecision(12)<<"{\"included_in_production_cursor\":true,\"processed_inputs\":100000,\"CPU_seconds\":"<<elapsed()<<",\"estimated_full_scope_CPU_at_this_prefix_rate\":"<<elapsed()*double(SCOPE)/100000<<",\"counts\":";counts_json(o,all);o<<"}\n";}
     }
    }
    // Lexicographic prefix increment; modular carry changes each touched coordinate by +1 in F31.
    if(prefix+1<prefixes){for(int k=4;k>lead;--k){z[k]=(z[k]+1)%31;for(size_t f=0;f<first.forms.size();++f){int value=first.base[f]+first.forms[f][k];first.base[f]=value>=31?value-31:value;}if(z[k]!=0)break;}}
   }
  }
  if(!found&&!timeout){assert(pc.raw==PER_SCOPE&&pc.legal==PER_LEGAL&&pc.raw==pc.legal+pc.illegal);cout<<"PATTERN_COMPLETE index="<<pindex<<" source="<<p.source<<" raw="<<pc.raw<<" legal="<<pc.legal<<" BFS="<<pc.bfs<<" CPU="<<elapsed()<<endl;progress("RUNNING");}
 }
 if(!found&&!timeout)assert(all.raw==SCOPE);string status=found?"FOUND_D3":timeout?"CPU_LIMIT_PREFIX_SAVED":"COMPLETE_FOURPAIR_SCOPE_NO_SOLUTION";
 U completed=0;for(auto&c:per)completed+=c.raw==PER_SCOPE;
 ofstream o(directory+"/terminal.json");o<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"running\":false,\"raw_scope\":"<<SCOPE<<",\"processed_inputs\":"<<all.raw<<",\"patterns_scope\":37,\"patterns_completed\":"<<completed<<",\"actual_full_root_BFS\":"<<all.bfs<<",\"saved_best_graph\":"<<(best_pattern>=0?"true":"false")<<",\"counts\":";counts_json(o,all);o<<",\"next_position\":";if(timeout)pos_json(o,next_position);else o<<"null";o<<",\"per_pattern\":[";
 for(int k=0;k<count;++k){if(k)o<<',';o<<"{\"pattern_index\":"<<k<<",\"source_cursor\":"<<patterns[k].source<<",\"scope\":"<<PER_SCOPE<<",\"counts\":";counts_json(o,per[k]);o<<'}';}
 o<<"],\"in_prefix_exact_short_word_calibrations\":"<<calibration_count<<",\"calibration_additional_BFS\":0,\"CPU_seconds\":"<<elapsed()<<",\"old_fivepair_modes_processed\":0,\"new_random_seeds\":0}\n";o.close();progress(status);cout<<status<<" raw="<<all.raw<<" BFS="<<all.bfs<<" CPU="<<elapsed()<<endl;
}
