#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
using Row=array<uint64_t,6>;
int mod(int x){x%=3;return x<0?x+3:x;}
int code7(const array<int,7>&x){int r=0,p=1;for(int a:x){r+=p*a;p*=3;}return r;}
array<int,7>norm(array<int,7>x){int s=0;while(s<7&&!x[s])s++;assert(s<7);int k=x[s];for(int&i:x)i=mod(i*k);return x;}
int main(int argc,char**argv){
 rlimit lim{56,56};setrlimit(RLIMIT_CPU,&lim);clock_t start=clock();string dir=argv[1],rawpath=argv[2];
 ifstream in(dir+"/columns.txt");int N,R;in>>N>>R;assert(N==364&&R==26117);vector<int>pins(N);vector<array<int,7>>coords(N);vector<int>pointidx(2187,-1);
 for(int i=0;i<N;i++){in>>pins[i];for(int&x:coords[i])in>>x;pointidx[code7(coords[i])]=i;}
 vector<Row>rows(R);vector<vector<int>>support(R);map<Row,int>rowidx;ifstream raw(rawpath,ios::binary);
 for(int i=0;i<R;i++){rows[i].fill(0);raw.read((char*)rows[i].data(),46);assert(raw.gcount()==46);assert((rows[i][5]>>44)==0);assert(rowidx.emplace(rows[i],i).second);for(int j=0;j<N;j++)if(rows[i][j>>6]>>(j&63)&1)support[i].push_back(j);}
 vector<int>probes;for(int i=0;i<16;i++)probes.push_back(i*(R-1)/15);
 struct Verified{int type,code;array<int,9>A;vector<int>p;uint64_t offset;};vector<Verified>good;vector<array<int,5>>audit;
 ofstream mapsout(dir+"/verified_row_maps.u16.bin",ios::binary);uint64_t written=0,totalRowTests=0;int detone=0,cursor=0;bool complete=true;
 auto transform=[&](const vector<int>&p,int i){Row out{};for(int c:support[i])out[p[c]>>6]|=1ULL<<(p[c]&63);return out;};
 auto test=[&](int type,int code,const array<int,9>&A,vector<int>p){
  vector<int>tmp=p;sort(tmp.begin(),tmp.end());for(int i=0;i<N;i++)assert(tmp[i]==i);
  int bad=-1,tests=0;
  for(int i:probes){tests++;totalRowTests++;if(!rowidx.count(transform(p,i))){bad=i;break;}}
  vector<uint16_t>im;
  if(bad<0){im.resize(R);vector<bool>seen(R);for(int i=0;i<R;i++){tests++;totalRowTests++;auto it=rowidx.find(transform(p,i));if(it==rowidx.end()){bad=i;break;}im[i]=it->second;assert(!seen[im[i]]);seen[im[i]]=true;}}
  if(bad<0){uint64_t off=written;mapsout.write((char*)im.data(),R*sizeof(uint16_t));written+=R*sizeof(uint16_t);good.push_back({type,code,A,move(p),off});}
  audit.push_back({type,code,bad,tests,bad<0?(int)good.size()-1:-1});
 };
 for(int code=0;code<19683;code++){
  if(double(clock()-start)/CLOCKS_PER_SEC>51){complete=false;cursor=code;break;}
  array<int,9>A;int z=code;for(int&i:A){i=z%3;z/=3;}
  int a=A[0],b=A[1],c=A[2],d=A[3],e=A[4],f=A[5],g=A[6],h=A[7],i=A[8];
  if(mod(a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))!=1)continue;detone++;
  array<int,9>C={mod(e*i-f*h),mod(f*g-d*i),mod(d*h-e*g),mod(c*h-b*i),mod(a*i-c*g),mod(b*g-a*h),mod(b*f-c*e),mod(c*d-a*f),mod(a*e-b*d)};
  vector<int>p(N);
  for(int j=0;j<N;j++){auto x=coords[j];array<int,7>y{};for(int r=0;r<3;r++)for(int k=0;k<3;k++){y[r]+=A[3*r+k]*x[k];y[r+4]+=C[3*r+k]*x[k+4];}for(int&r:y)r=mod(r);y[3]=x[3];y=norm(y);p[j]=pointidx[code7(y)];assert(p[j]>=0);}
  test(0,code,A,move(p));cursor=code+1;
 }
 bool Jtested=false;
 if(complete){assert(detone==5616);array<int,9>dummy{};vector<int>p(N);for(int j=0;j<N;j++){auto x=coords[j];array<int,7>y={x[4],x[5],x[6],mod(-x[3]),x[0],x[1],x[2]};p[j]=pointidx[code7(norm(y))];assert(p[j]>=0);}test(1,-1,dummy,move(p));Jtested=true;}
 mapsout.close();
 vector<int>orbit(N,-1),parent(N,-1),gen(N,-1);vector<vector<int>>orbits;
 for(int r=0;r<N;r++)if(orbit[r]<0){int k=orbits.size();vector<int>q{r};orbit[r]=k;parent[r]=r;for(int at=0;at<(int)q.size();at++){int u=q[at];for(int gi=0;gi<(int)good.size();gi++){int v=good[gi].p[u];if(orbit[v]<0){orbit[v]=k;parent[v]=u;gen[v]=gi;q.push_back(v);}else assert(orbit[v]==k);}}sort(q.begin(),q.end());orbits.push_back(q);}
 ofstream out(dir+"/RESULT.json");out<<"{\n\"status\":\""<<(complete?"COMPLETE_VERIFIED_ROW_SYMMETRY_ENUMERATION":"PARTIAL_CPU_WINDOW_CLOSED")<<"\",\"complete\":"<<(complete?"true":"false")<<",\"SL3_candidates_examined\":"<<detone<<",\"matrix_cursor\":"<<cursor<<",\"J_tested\":"<<(Jtested?"true":"false")<<",\"verified_permutations\":"<<good.size()<<",\"exact_row_count\":"<<R<<",\"total_membership_tests\":"<<totalRowTests<<",\"row_maps_file\":\"verified_row_maps.u16.bin\",\"row_map_layout\":\"verifiedpermmajor26117nativeuint16indices\",\n\"permutations\":[";
 auto vec=[&](auto const&v){out<<'[';bool f=true;for(auto x:v){if(!f)out<<',';f=false;out<<x;}out<<']';};
 for(int k=0;k<(int)good.size();k++){if(k)out<<',';auto&v=good[k];out<<"{\"id\":"<<k<<",\"family\":\""<<(v.type?"J":"SL3F3")<<"\",\"matrix_code\":"<<v.code<<",\"matrix_rowmajor\":";vec(v.A);out<<",\"column_permutation\":";vec(v.p);out<<",\"row_map_byte_offset\":"<<v.offset<<",\"all_rows_checked\":"<<R<<",\"row_map_is_bijective\":true}";}
 out<<"],\n\"candidate_audit\":[";for(int k=0;k<(int)audit.size();k++){if(k)out<<',';vec(audit[k]);}out<<"],\"candidate_audit_columns\":[\"family0SL3_1J\",\"matrixcode\",\"first_bad_row_or_minus1\",\"rowtests\",\"verifiedperm_id_or_minus1\"],\n\"orbits\":[";
 for(int k=0;k<(int)orbits.size();k++){if(k)out<<',';out<<"{\"id\":"<<k<<",\"size\":"<<orbits[k].size()<<",\"column_indices\":";vec(orbits[k]);vector<int>vs;for(int j:orbits[k])vs.push_back(pins[j]);out<<",\"pin_vertices\":";vec(vs);out<<",\"representative_pin\":"<<pins[orbits[k][0]]<<'}';}
 out<<"],\"orbit_BFS_parent_columns\":";vec(parent);out<<",\"orbit_BFS_generator_ids\":";vec(gen);out<<",\"graph_distance_BFS\":0,\"new_graphs\":0,\"MIP_calls\":0,\"CPU_seconds\":"<<setprecision(12)<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";out.close();
 cout<<"complete="<<complete<<" SL3="<<detone<<" J="<<Jtested<<" verified="<<good.size()<<" orbits="<<orbits.size()<<" sizes=";for(auto&o:orbits)cout<<o.size()<<',';cout<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
