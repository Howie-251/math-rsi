// General single-bridge necessary screen. No triangle closure constraints.
#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using Perm=std::array<int,10>;
using Rows=std::array<unsigned,10>;
constexpr unsigned ALL=1023;
struct Choice { Perm s; std::vector<std::vector<int>> cycles; std::string type; };
struct Config { int id,offset; Rows z,zt; std::vector<Choice> p,d; };
struct Stats { long long bases=0,bridges=0,left=0,right=0,both=0; };
struct Witness { int choice; Perm m,n; };
clock_t began;
bool stopped=false;
long long nodes=0,solver_calls=0,base_started=0;
constexpr double CPU_CAP=9.8; // leave room to flush exact prefix statistics within 10 CPU seconds
bool limit(){ if(double(clock()-began)/CLOCKS_PER_SEC>=CPU_CAP)stopped=true; return stopped; }
Rows transpose(const Rows&a){Rows b{};for(int u=0;u<10;u++){unsigned t=a[u];while(t){int v=__builtin_ctz(t);t&=t-1;b[v]|=1U<<u;}}return b;}
// Return J-AB. In this domain AB is zero-one, not a Boolean approximation.
bool complement_product(const Rows&a,const Rows&b,Rows&r){
 for(int u=0;u<10;u++){unsigned covered=0,t=a[u];while(t){int v=__builtin_ctz(t);t&=t-1;if(covered&b[v])return false;covered|=b[v];}r[u]=ALL^covered;if(__builtin_popcount(r[u])!=4)return false;}return true;
}
bool exact_witness(const Rows&r,const Perm&s,const Perm&t,const Perm&m,Perm&n){
 std::array<int,10> col{}; unsigned used=0;
 for(int u=0;u<10;u++){if(m[u]<0||m[u]>=10||(used>>m[u]&1))return false;used|=1U<<m[u];}
 for(int u=0;u<10;u++){
  std::array<int,10> row{};for(int v=0;v<10;v++)row[v]=(r[u]>>v)&1;
  row[m[u]]--;row[m[s[u]]]--;row[t[m[u]]]--;
  int found=-1;for(int v=0;v<10;v++){if(row[v]<0||row[v]>1)return false;if(row[v]){if(found>=0)return false;found=v;col[v]++;}}
  if(found<0)return false;n[u]=found;
 }for(int x:col)if(x!=1)return false;return true;
}
struct Solver {
 const Rows&r; const Perm&s,&t; Rows allowed{}; Perm m{},answer{},residue{};
 Solver(const Rows&rr,const Perm&ss,const Perm&tt):r(rr),s(ss),t(tt){
  m.fill(-1);for(int u=0;u<10;u++){unsigned transformed=0,z=r[u];while(z){int v=__builtin_ctz(z);z&=z-1;transformed|=1U<<t[v];}allowed[u]=r[u]&r[s[u]]&transformed;}
 }
 bool visit(unsigned used,int depth){
  nodes++;if((nodes&1023)==0&&limit())return false;
  if(depth==10){assert(exact_witness(r,s,t,m,residue));answer=m;return true;}
  int best=11,row=-1;unsigned options=0;
  for(int u=0;u<10;u++)if(m[u]<0){unsigned a=allowed[u]&~used;if(m[s[u]]>=0)a&=~(1U<<t[m[s[u]]]);int n=__builtin_popcount(a);if(n<best){best=n;row=u;options=a;if(!n)return false;}}
  while(options&&!stopped){int v=__builtin_ctz(options);options&=options-1;m[row]=v;if(visit(used|(1U<<v),depth+1))return true;m[row]=-1;}return false;
 }
 bool solve(){solver_calls++;if((solver_calls&255)==0&&limit())return false;return visit(0,0);}
};
template<class T>void arr(std::ostream&o,const T&a){o<<'[';for(unsigned i=0;i<a.size();i++){if(i)o<<',';o<<a[i];}o<<']';}
void statsjson(std::ostream&o,const Stats&s){o<<"{\"base_Y_alignments\":"<<s.bases<<",\"state_Y_bridges\":"<<s.bridges<<",\"left_M_feasible_bridges\":"<<s.left<<",\"right_M_feasible_bridges\":"<<s.right<<",\"both_M_feasible_bridges\":"<<s.both<<'}';}
void add(Stats&x,const Stats&y){x.bases+=y.bases;x.bridges+=y.bridges;x.left+=y.left;x.right+=y.right;x.both+=y.both;}
struct Run {
 std::vector<Config> configs; std::array<Stats,100> bypair{};std::map<std::string,Stats> bytype;Stats total;std::ofstream witnesses;
 explicit Run(const std::string&prefix):witnesses(prefix+".witnesses.jsonl"){}
 void bridge(int ci,int cj,int pi,int dj,const Rows&y){
  base_started++;if((base_started&63)==0&&limit())return;
  const auto&i=configs[ci];const auto&j=configs[cj];Rows rl{},rr{};
  // Two-sided same-fiber conditions prove disjointness of these products.
  assert(complement_product(y,j.zt,rl));assert(complement_product(i.zt,y,rr));
  std::vector<Witness> left,right;
  for(int pj=0;pj<int(j.p.size())&&!stopped;pj++){Solver s(rl,i.p[pi].s,j.p[pj].s);if(s.solve())left.push_back({pj,s.answer,s.residue});}
  for(int di=0;di<int(i.d.size())&&!stopped;di++){Solver s(rr,i.d[di].s,j.d[dj].s);if(s.solve())right.push_back({di,s.answer,s.residue});}
  if(stopped)return; // unfinished base contributes no completed-domain count
  for(const auto&l:left)for(const auto&r:right){
   const int sid=i.offset+pi*int(i.d.size())+r.choice;
   const int tid=j.offset+l.choice*int(j.d.size())+dj;
   witnesses<<"{\"source_state\":"<<sid<<",\"target_state\":"<<tid<<",\"Y_rows\":";arr(witnesses,y);
   witnesses<<",\"M_L\":";arr(witnesses,l.m);witnesses<<",\"N_L\":";arr(witnesses,l.n);
   witnesses<<",\"M_R\":";arr(witnesses,r.m);witnesses<<",\"N_R\":";arr(witnesses,r.n);witnesses<<"}\n";
  }
  Stats x; x.bases=1;x.bridges=i.d.size()*j.p.size();x.left=left.size()*i.d.size();x.right=right.size()*j.p.size();x.both=left.size()*right.size();
  add(total,x);add(bypair[10*ci+cj],x);add(bytype[i.p[pi].type],x);
 }
 void align(int ci,int cj,int pi,int dj){
  const auto&lc=configs[ci].p[pi].cycles;const auto&rc=configs[cj].d[dj].cycles;
  if(configs[ci].p[pi].type!=configs[cj].d[dj].type)return;
  std::vector<int> pairing(rc.size());for(int k=0;k<int(rc.size());k++)pairing[k]=k;
  do{
   bool valid=true;for(int k=0;k<int(lc.size());k++)if(lc[k].size()!=rc[pairing[k]].size())valid=false;
   if(valid){Rows y{};cycle_align(ci,cj,pi,dj,pairing,0,y);}
  }while(!stopped&&std::next_permutation(pairing.begin(),pairing.end()));
 }
 void cycle_align(int ci,int cj,int pi,int dj,const std::vector<int>&pairing,int depth,Rows&y){
  if(stopped)return;const auto&lc=configs[ci].p[pi].cycles;const auto&rc=configs[cj].d[dj].cycles;
  if(depth==int(lc.size())){bridge(ci,cj,pi,dj,y);return;}
  const auto&a=lc[depth];const auto&b=rc[pairing[depth]];int len=a.size();
  for(int shift=0;shift<len&&!stopped;shift++)for(int sign:{1,-1}){
   for(int u:a)y[u]=0;
   for(int k=0;k<len;k++){int e=(shift+sign*k+len)%len;y[a[e]]|=1U<<b[k];y[a[(e+1)%len]]|=1U<<b[k];}
   cycle_align(ci,cj,pi,dj,pairing,depth+1,y);if(stopped)return;
  }
 }
};
int main(int argc,char**argv){
 assert(argc==3);began=clock();std::ifstream in(argv[1]);const std::string prefix=argv[2];Run run(prefix);int n;in>>n;assert(n==10);int offset=0;
 for(int k=0;k<n;k++){
  Config c;int np,nd;in>>c.id>>np>>nd;c.offset=offset;offset+=np*nd;for(auto&v:c.z)in>>v;c.zt=transpose(c.z);
  for(auto item:{std::pair{&c.p,np},std::pair{&c.d,nd}})for(int h=0;h<item.second;h++){
   Choice ch;for(int&v:ch.s)in>>v;int count;in>>count;
   for(int e=0;e<count;e++){int length;in>>length;std::vector<int>cy(length);for(int&v:cy)in>>v;ch.cycles.push_back(cy);if(e)ch.type+=",";ch.type+=std::to_string(length);}item.first->push_back(ch);
  }run.configs.push_back(c);
 }assert(offset==531);
 for(int i=0;i<10&&!stopped;i++)for(int j=0;j<10&&!stopped;j++)for(int p=0;p<int(run.configs[i].p.size())&&!stopped;p++)for(int d=0;d<int(run.configs[j].d.size())&&!stopped;d++)run.align(i,j,p,d);
 const std::map<std::string,long long> expected={{"5,5",1377800},{"10",1788020},{"4,6",921984},{"3,7",162624},{"3,3,4",28224}};
 bool complete=!stopped;if(complete){assert(run.total.bridges==4278652);for(const auto&[key,value]:expected)assert(run.bytype[key].bridges==value);}
 run.witnesses.flush();std::ofstream out(prefix+".json");
 out<<"{\"complete\":"<<(complete?"true":"false")<<",\"stop_reason\":\""<<(complete?"complete_general_bridge_domain":"cpu_cap")<<"\",\"cpu_budget_seconds\":10,\"internal_stop_seconds\":"<<CPU_CAP<<",\"cpu_seconds\":"<<double(clock()-began)/CLOCKS_PER_SEC<<",\"threads\":1,\"state_count\":531,\"expected_bridges\":4278652,\"base_alignments_started\":"<<base_started<<",\"solver_calls\":"<<solver_calls<<",\"backtracking_nodes\":"<<nodes<<",\"witness_semantics\":\"Each surviving state-Y bridge retains its first local M and exact N on each side; no triangle closure was imposed or tested\",\"total\":";statsjson(out,run.total);
 out<<",\"cycle_types\":[";bool comma=false;for(const auto&[key,value]:expected){if(comma)out<<',';comma=true;out<<"{\"type\":\""<<key<<"\",\"expected\":"<<value<<",\"actual\":";statsjson(out,run.bytype[key]);out<<'}';}
 out<<"],\"configuration_pairs\":[";for(int i=0;i<10;i++)for(int j=0;j<10;j++){if(i||j)out<<',';out<<"{\"source_configuration\":"<<run.configs[i].id<<",\"target_configuration\":"<<run.configs[j].id<<",\"stats\":";statsjson(out,run.bypair[10*i+j]);out<<'}';}out<<"]}\n";
 std::cout<<"complete="<<complete<<" bridges="<<run.total.bridges<<" both="<<run.total.both<<" bases="<<run.total.bases<<" CPU="<<double(clock()-began)/CLOCKS_PER_SEC<<'\n';
}
