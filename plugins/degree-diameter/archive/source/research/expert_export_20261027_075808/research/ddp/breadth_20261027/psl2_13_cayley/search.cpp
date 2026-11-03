#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;
constexpr int P=13,N=1092,D=12;
struct M {int a,b,c,d;};
int mod(int x){x%=13;return x<0?x+13:x;}
int code(M a){return a.a+13*a.b+169*a.c+2197*a.d;}
int canon(M a){return min(code(a),code({mod(-a.a),mod(-a.b),mod(-a.c),mod(-a.d)}));}
M decode(int x){M a; a.a=x%13;x/=13;a.b=x%13;x/=13;a.c=x%13;x/=13;a.d=x;return a;}
M mul(M a,M b){return {mod(a.a*b.a+a.b*b.c),mod(a.a*b.b+a.b*b.d),mod(a.c*b.a+a.d*b.c),mod(a.c*b.b+a.d*b.d)};}
vector<int>codes,inverse_id,invol;vector<array<int,2>>pairs;vector<M>mat;
vector<unsigned short>product;array<int,28561>index_code;
struct State{vector<int>pa,iv;array<int,D>S{};int missing=N+1;};
State best,current,neighbor;long long evals=0,full_scans=0,moves=0,kicks=0;
bool hit=false,limit=false;clock_t begin_cpu;double budget;string dir;
int stcur=-1,segcur=-1,roundcur=-1,slotcur=-1,idcur=-1,kindcur=-1;
double cpu(){return double(clock()-begin_cpu)/CLOCKS_PER_SEC;}
template<class T>void arr(ostream&o,const T&a){o<<'[';bool f=true;for(auto x:a){if(!f)o<<',';f=false;o<<x;}o<<']';}
void mk(State&x){int j=0;for(int q:x.pa){x.S[j++]=pairs[q][0];x.S[j++]=pairs[q][1];}for(int q:x.iv)x.S[j++]=invol[q];assert(j==12);auto s=x.S;sort(s.begin(),s.end());assert(s[0]>0&&adjacent_find(s.begin(),s.end())==s.end());}
void sj(ostream&o,const State&s){o<<"{\"pairs\":";arr(o,s.pa);o<<",\"involutions\":";arr(o,s.iv);o<<",\"S\":";arr(o,s.S);o<<",\"root_missing\":"<<s.missing<<'}';}
vector<int> dist3(const State&s){vector<int>d(N,-1),q(N);int h=0,t=1;q[0]=0;d[0]=0;while(h<t){int u=q[h++];if(d[u]==3)continue;const auto*r=&product[u*N];for(int g:s.S){int v=r[g];if(d[v]<0){d[v]=d[u]+1;q[t++]=v;}}}return d;}
ofstream events;
void score(State&x){mk(x);auto d=dist3(x);x.missing=count(d.begin(),d.end(),-1);evals++;if(x.missing<best.missing){best=x;events<<"{\"evaluation\":"<<evals<<",\"CPU_seconds\":"<<cpu()<<",\"candidate\":";sj(events,x);events<<"}\n";events.flush();cout<<"BEST missing="<<x.missing<<" eval="<<evals<<" CPU="<<cpu()<<endl;}if(x.missing==0)hit=true;}
bool expired(){if(cpu()<budget)return false;limit=true;return true;}
bool scan(){neighbor=current;vector<bool>up(pairs.size()),ui(invol.size());for(int p:current.pa)up[p]=true;for(int p:current.iv)ui[p]=true;
 kindcur=0;for(int a=0;a<(int)current.pa.size();a++)for(int b=0;b<(int)pairs.size();b++)if(!up[b]){slotcur=a;idcur=b;if(expired())return false;auto x=current;x.pa[a]=b;score(x);if(x.missing<neighbor.missing)neighbor=x;if(hit)return false;}
 kindcur=1;for(int a=0;a<(int)current.iv.size();a++)for(int b=0;b<(int)invol.size();b++)if(!ui[b]){slotcur=a;idcur=b;if(expired())return false;auto x=current;x.iv[a]=b;score(x);if(x.missing<neighbor.missing)neighbor=x;if(hit)return false;}
 full_scans++;return true;}
int main(int argc,char**argv){assert(argc==3);dir=argv[1];budget=stod(argv[2]);begin_cpu=clock();index_code.fill(-1);
 ifstream input(dir+"/input.txt");int n;input>>n;assert(n==N);for(int k=0;k<N;k++){int x;input>>x;codes.push_back(x);mat.push_back(decode(x));index_code[x]=k;}assert(codes[0]==canon({1,0,0,1}));
 product.resize(N*N);inverse_id.resize(N);for(int a=0;a<N;a++){auto m=mat[a];inverse_id[a]=index_code[canon({m.d,mod(-m.b),mod(-m.c),m.a})];for(int b=0;b<N;b++){int v=index_code[canon(mul(m,mat[b]))];assert(v>=0);product[a*N+b]=v;}assert(product[a*N+inverse_id[a]]==0);}
 for(int a=1;a<N;a++){int b=inverse_id[a];if(a==b)invol.push_back(a);else if(a<b)pairs.push_back({a,b});}assert(invol.size()==91&&pairs.size()==500);
 int count_starts;input>>count_starts;assert(count_starts==12);vector<State>starts(12);for(auto&x:starts){int p,i;input>>p>>i;x.pa.resize(p);x.iv.resize(i);for(int&v:x.pa)input>>v;for(int&v:x.iv)input>>v;mk(x);}
 vector<int>expected(N);for(int&x:expected)input>>x;
 events.open(dir+"/improvements.jsonl");ofstream trace(dir+"/segments.jsonl");mt19937_64 rng(20261027131ULL);int starts_completed=0,segments_completed=0,starts_started=0;
 for(stcur=0;stcur<12&&!hit&&!limit;stcur++){if(expired())break;current=starts[stcur];score(current);starts_started++;
  if(stcur==0){auto got=dist3(current);assert(got==expected);ofstream o(dir+"/first_cpp_check.json");o<<"{\"all_1092_radius3_distances_match_independent_Python\":true,\"first_score_reused\":true,\"root_missing\":"<<current.missing<<"}\n";}
  for(segcur=0;segcur<3&&!hit&&!limit;segcur++){
   int accepted=0;for(roundcur=0;roundcur<12&&!hit&&!limit;roundcur++){if(!scan())break;if(neighbor.missing>=current.missing)break;current=neighbor;moves++;accepted++;}
   if(hit||limit)break;segments_completed++;trace<<"{\"start\":"<<stcur<<",\"segment\":"<<segcur<<",\"accepted\":"<<accepted<<",\"missing\":"<<current.missing<<"}\n";trace.flush();
   if(segcur<2){vector<bool>up(pairs.size()),ui(invol.size());for(int x:current.pa)up[x]=true;for(int x:current.iv)ui[x]=true;for(int k=0;k<2;k++){int slot=rng()%(current.pa.size()+current.iv.size());if(slot<(int)current.pa.size()){int q;do{q=rng()%pairs.size();}while(up[q]);up[current.pa[slot]]=false;current.pa[slot]=q;up[q]=true;}else{slot-=current.pa.size();int q;do{q=rng()%invol.size();}while(ui[q]);ui[current.iv[slot]]=false;current.iv[slot]=q;ui[q]=true;}}score(current);kicks++;}
  }
  if(!hit&&!limit)starts_completed++;
 }
 assert(best.missing<=N);ofstream b(dir+"/best.json");b<<"{\"n\":1092,\"degree\":12,\"m\":6552,\"candidate\":";sj(b,best);b<<",\"S_matrix_codes\":[";for(int k=0;k<12;k++){if(k)b<<',';b<<codes[best.S[k]];}b<<"],\"bad_unordered_pairs\":"<<546LL*best.missing<<",\"target_D\":3}\n";
 ofstream edge(dir+"/best.edges");edge<<N<<" 6552\n";int ec=0;for(int u=0;u<N;u++)for(int s:best.S){int v=product[u*N+s];if(u<v){edge<<u<<' '<<v<<'\n';ec++;}}assert(ec==6552);
 auto bd=dist3(best);ofstream mask(dir+"/best_radius3_distances.json");arr(mask,bd);mask<<'\n';
 ofstream o(dir+"/terminal.json");o<<"{\"status\":\""<<(hit?"FOUND_D3":limit?"CPU_LIMIT_PREFIX_SAVED":"COMPLETE_12_START_PROFILE_NO_D3")<<"\",\"running\":false,\"found_D3\":"<<(hit?"true":"false")<<",\"starts_scope\":12,\"starts_started\":"<<starts_started<<",\"starts_completed\":"<<starts_completed<<",\"segments_completed\":"<<segments_completed<<",\"full_coordinate_scans\":"<<full_scans<<",\"strict_moves\":"<<moves<<",\"two_coordinate_kicks\":"<<kicks<<",\"radius3_evaluations\":"<<evals<<",\"best_root_missing\":"<<best.missing<<",\"production_CPU_seconds\":"<<cpu()<<",\"scope_exhausted\":"<<(!hit&&!limit?"true":"false")<<",\"entire_group_family_exhausted\":false,\"cursor\":{\"start\":"<<stcur<<",\"segment\":"<<segcur<<",\"round\":"<<roundcur<<",\"kind\":"<<kindcur<<",\"slot\":"<<slotcur<<",\"pool_id\":"<<idcur<<"},\"current\":";sj(o,current);o<<",\"best_neighbor_seen\":";sj(o,neighbor);o<<",\"pending\":[\"root independent final saved-edge verification\"]}\n";
 cout<<"TERMINAL evals="<<evals<<" best="<<best.missing<<" CPU="<<cpu()<<" complete="<<starts_completed<<endl;
}
