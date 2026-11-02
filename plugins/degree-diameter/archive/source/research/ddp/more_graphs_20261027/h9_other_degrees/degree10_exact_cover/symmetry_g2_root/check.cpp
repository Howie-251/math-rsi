#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
using V=array<int,7>;using M=array<int,49>;using Row=array<uint64_t,6>;using P=array<uint16_t,364>;
int mod(int x){x%=3;return x<0?x+3:x;}
int code7(V x){int c=0,m=1;for(int a:x){c+=a*m;m*=3;}return c;}
V norm(V x){int i=0;while(i<7&&!x[i])i++;assert(i<7);int k=x[i];for(int&v:x)v=mod(v*k);return x;}
V act(const M&A,V x){V y{};for(int i=0;i<7;i++)for(int j=0;j<7;j++)y[i]+=A[i*7+j]*x[j];for(int&v:y)v=mod(v);return y;}
M mul(const M&A,const M&B){M C{};for(int i=0;i<7;i++)for(int j=0;j<7;j++)for(int k=0;k<7;k++)C[i*7+j]+=A[i*7+k]*B[k*7+j];for(int&v:C)v=mod(v);return C;}
M eye(){M A{};for(int i=0;i<7;i++)A[i*7+i]=1;return A;}
int Q(V x){return mod(x[0]*x[4]+x[1]*x[5]+x[2]*x[6]-x[3]*x[3]);}
M lift(array<int,9>A){int a=A[0],b=A[1],c=A[2],d=A[3],e=A[4],f=A[5],g=A[6],h=A[7],i=A[8];array<int,9>C={mod(e*i-f*h),mod(f*g-d*i),mod(d*h-e*g),mod(c*h-b*i),mod(a*i-c*g),mod(b*g-a*h),mod(b*f-c*e),mod(c*d-a*f),mod(a*e-b*d)};M R{};for(int r=0;r<3;r++)for(int k=0;k<3;k++){R[r*7+k]=A[r*3+k];R[(r+4)*7+k+4]=C[r*3+k];}R[3*7+3]=1;return R;}
struct DSU{int p[364],components=364;DSU(){iota(p,p+364,0);}int get(int a){return p[a]==a?a:p[a]=get(p[a]);}void join(int a,int b){a=get(a);b=get(b);if(a!=b){p[a]=b;components--;}}};
int main(int argc,char**argv){
 rlimit lim{57,57};setrlimit(RLIMIT_CPU,&lim);clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};string base=argv[1],dir=base+"/symmetry_g2_root";
 ifstream in(base+"/symmetry/columns.txt");int N,R;in>>N>>R;assert(N==364&&R==26117);vector<int>pins(N);vector<V>coords(N);vector<int>pointidx(2187,-1);
 for(int i=0;i<N;i++){in>>pins[i];for(int&x:coords[i])in>>x;pointidx[code7(coords[i])]=i;assert(Q(coords[i])==0);}
 vector<Row>rows(R);vector<vector<int>>support(R);map<Row,int>rowidx;ifstream raw(base+"/unique_cover_rows.u8.bin",ios::binary);
 for(int i=0;i<R;i++){rows[i].fill(0);raw.read((char*)rows[i].data(),46);assert(raw.gcount()==46);assert(rowidx.emplace(rows[i],i).second);for(int j=0;j<N;j++)if(rows[i][j>>6]>>(j&63)&1)support[i].push_back(j);}
 vector<M>gens;vector<string>names;for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(i!=j){array<int,9>A{};for(int k=0;k<3;k++)A[k*3+k]=1;A[i*3+j]=1;gens.push_back(lift(A));names.push_back("E"+to_string(i)+to_string(j));}
 M T=eye();T[0*7+3]=2;T[0*7+4]=1;T[3*7+4]=1;T[5*7+2]=2;T[6*7+1]=1;assert(mul(mul(T,T),T)==eye());gens.push_back(T);names.push_back("T_e1");
 int qminus=0;for(int c=0;c<2187;c++){V x{};int z=c;for(int&i:x){i=z%3;z/=3;}qminus+=(Q(x)==2);for(auto&G:gens)assert(Q(act(G,x))==Q(x));}assert(qminus==756);
 V h{0,0,0,1,0,0,0};vector<V>states{h};vector<M>representatives{eye()};vector<int>parent{-1},parentgen{-1};vector<int>seen(2187,-1);seen[code7(h)]=0;
 for(int at=0;at<(int)states.size();at++)for(int gi=0;gi<7;gi++){V w=act(gens[gi],states[at]);int c=code7(w);if(seen[c]<0){seen[c]=states.size();states.push_back(w);representatives.push_back(mul(gens[gi],representatives[at]));parent.push_back(at);parentgen.push_back(gi);}}
 assert(states.size()==756);for(int k=0;k<756;k++)assert(act(representatives[k],h)==states[k]);
 auto perm=[&](M A){P p;vector<int>seen(N);for(int j=0;j<N;j++){V y=norm(act(A,coords[j]));p[j]=pointidx[code7(y)];assert(p[j]<N);seen[p[j]]++;}for(int t:seen)assert(t==1);return p;};
 vector<array<int,9>>slA;vector<int>slcode;vector<P>slperm;int reuse_i=-1,reuse_g=-1;
 for(int code=0;code<19683;code++){array<int,9>A;int z=code;for(int&i:A){i=z%3;z/=3;}int a=A[0],b=A[1],c=A[2],d=A[3],e=A[4],f=A[5],g=A[6],hh=A[7],i=A[8];if(mod(a*(e*i-f*hh)-b*(d*i-f*g)+c*(d*hh-e*g))!=1)continue;int k=slA.size();if(code==6643)reuse_i=k;if(code==13469)reuse_g=k;slA.push_back(A);slcode.push_back(code);slperm.push_back(perm(lift(A)));}assert(slA.size()==5616&&reuse_i>=0&&reuse_g>=0);
 struct Good{int w,a;P p;uint64_t offset;bool inherited;};vector<Good>good;DSU dsu;
 good.push_back({0,reuse_i,slperm[reuse_i],0,true});good.push_back({0,reuse_g,slperm[reuse_g],0,true});for(int i=0;i<N;i++)dsu.join(i,slperm[reuse_g][i]);assert(dsu.components==192);
 vector<int>probes;for(int i=0;i<16;i++)probes.push_back(i*(R-1)/15);uint64_t rowtests=0,examined=0,accepted=0;int currentw=0,currenta=-1,finishedw=0;uint64_t written=0;ofstream maps(dir+"/verified_new_row_maps.u16.bin",ios::binary),audit(dir+"/candidate_audit.u32.bin",ios::binary);vector<double>profile_cpu;vector<int>profile_orbits;string stop="";bool complete=false;
 auto transform=[&](const P&p,int r){Row out{};for(int c:support[r])out[p[c]>>6]|=1ULL<<(p[c]&63);return out;};
 for(int wi=1;wi<(int)states.size()&&!stop.size();wi++){
  P rp=perm(representatives[wi]);
  for(int ai=0;ai<5616;ai++){
   if(cpu()>53){stop="CPU_WINDOW_CLOSED";break;}currentw=wi;currenta=ai;P p;for(int j=0;j<N;j++)p[j]=rp[slperm[ai][j]];int bad=-1,tests=0;vector<uint16_t>rowmap;
   for(int r:probes){tests++;rowtests++;if(!rowidx.count(transform(p,r))){bad=r;break;}}
   if(bad<0){rowmap.resize(R);for(int r=0;r<R;r++){tests++;rowtests++;auto it=rowidx.find(transform(p,r));if(it==rowidx.end()){bad=r;break;}rowmap[r]=it->second;}}
   int id=-1;if(bad<0){vector<bool>seenrow(R);for(int x:rowmap){assert(!seenrow[x]);seenrow[x]=true;}id=good.size();good.push_back({wi,ai,p,written,false});maps.write((char*)rowmap.data(),2*R);written+=2*R;accepted++;for(int j=0;j<N;j++)dsu.join(j,p[j]);}
   uint32_t rec[5]={(uint32_t)wi,(uint32_t)ai,(uint32_t)(bad+1),(uint32_t)tests,(uint32_t)(id+1)};audit.write((char*)rec,sizeof(rec));examined++;
   if(dsu.components<=6){stop="USEFUL_ORBIT_THRESHOLD_REACHED";break;}
  }
  if(currenta==5615){finishedw=wi;if(wi<=2){profile_cpu.push_back(cpu());profile_orbits.push_back(dsu.components);cerr<<"profile w="<<wi<<" cpu="<<cpu()<<" orbits="<<dsu.components<<" accepted="<<accepted<<'\n';}
   if(wi==2&&stop.empty()){double rate=(profile_cpu[1]-profile_cpu[0]);double estimated=cpu()+rate*(755-2);if(estimated>53){stop="TWO_REPRESENTATIVE_PROFILE_EXCEEDS_FULL_BUDGET";}}
  }
 }
 if(stop.empty()){stop="COMPLETE_CANDIDATE_COSET_COLLECTION";complete=true;}maps.close();audit.close();
 vector<int>orbit(N,-1),oparent(N,-1),ogen(N,-1);vector<vector<int>>orbits;for(int r=0;r<N;r++)if(orbit[r]<0){int oid=orbits.size();vector<int>q{r};orbit[r]=oid;oparent[r]=r;for(int at=0;at<(int)q.size();at++)for(int gi=0;gi<(int)good.size();gi++){int v=good[gi].p[q[at]];if(orbit[v]<0){orbit[v]=oid;oparent[v]=q[at];ogen[v]=gi;q.push_back(v);}else assert(orbit[v]==oid);}sort(q.begin(),q.end());orbits.push_back(q);}assert((int)orbits.size()==dsu.components);
 ofstream out(dir+"/RESULT.json");auto vec=[&](auto const&v){out<<'[';bool first=true;for(auto x:v){if(!first)out<<',';first=false;out<<x;}out<<']';};
 out<<"{\"status\":\""<<stop<<"\",\"complete_candidate_collection\":"<<(complete?"true":"false")<<",\"Q_minus_one_vectors\":"<<qminus<<",\"h_orbit_size\":"<<states.size()<<",\"generators\":[";for(int i=0;i<7;i++){if(i)out<<',';out<<"{\"name\":\""<<names[i]<<"\",\"matrix\":";vec(gens[i]);out<<'}';}out<<"],\"h_states\":[";
 for(int i=0;i<756;i++){if(i)out<<',';out<<"{\"id\":"<<i<<",\"vector\":";vec(states[i]);out<<",\"parent\":"<<parent[i]<<",\"generator\":"<<parentgen[i]<<",\"representative_matrix\":";vec(representatives[i]);out<<'}';}
 out<<"],\"old_SL3_candidates_reused\":5616,\"new_candidates_examined\":"<<examined<<",\"new_verified_permutations\":"<<accepted<<",\"last_w_index\":"<<currentw<<",\"last_SL3_index\":"<<currenta<<",\"last_SL3_code\":"<<slcode[max(0,currenta)]<<",\"fully_processed_new_w\":"<<finishedw<<",\"profile_CPU\":";vec(profile_cpu);out<<",\"profile_orbits\":";vec(profile_orbits);out<<",\"row_membership_tests\":"<<rowtests<<",\"row_maps_bytes\":"<<written<<",\"audit_record_layout\":[\"w_index\",\"SL3_index\",\"first_bad_row_plus1_0means_pass\",\"row_tests\",\"verified_id_plus1_0means_rejected\"],\"audit_record_native_uint32_count\":5,\"permutations\":[";
 for(int i=0;i<(int)good.size();i++){if(i)out<<',';auto&v=good[i];out<<"{\"id\":"<<i<<",\"w_index\":"<<v.w<<",\"SL3_index\":"<<v.a<<",\"SL3_code\":"<<slcode[v.a]<<",\"SL3_matrix\":";vec(slA[v.a]);out<<",\"column_permutation\":";vec(v.p);out<<",\"row_map_file\":\""<<(v.inherited?"../symmetry/verified_row_maps.u16.bin":"verified_new_row_maps.u16.bin")<<"\",\"row_map_byte_offset\":"<<(v.inherited?uint64_t(i)*2*R:v.offset)<<",\"inherited_full_row_verification\":"<<(v.inherited?"true":"false")<<",\"all_rows_checked\":"<<R<<",\"bijective_row_map\":true}";}
 out<<"],\"pin_orbit_count\":"<<orbits.size()<<",\"pin_orbits\":[";for(int i=0;i<(int)orbits.size();i++){if(i)out<<',';out<<"{\"id\":"<<i<<",\"column_indices\":";vec(orbits[i]);vector<int>ps;for(int j:orbits[i])ps.push_back(pins[j]);out<<",\"pin_vertices\":";vec(ps);out<<'}';}out<<"],\"pin_orbit_BFS_parent\":";vec(oparent);out<<",\"pin_orbit_BFS_generator\":";vec(ogen);out<<",\"CPU_seconds\":"<<setprecision(12)<<cpu()<<",\"fullgraph_BFS\":0,\"MIP_calls\":0,\"new_graphs\":0}\n";out.close();cerr<<"FINAL "<<stop<<" new="<<examined<<" accepted="<<accepted<<" pinorbits="<<orbits.size()<<" cpu="<<cpu()<<'\n';
}
