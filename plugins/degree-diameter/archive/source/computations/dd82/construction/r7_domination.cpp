// Exact necessary-condition search: does an 8-subset of 22 deficit vertices
// dominate all 57 old vertices after each seven-edge deletion pattern?
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using U=uint64_t; using namespace std;
const U FULL=(U(1)<<57)-1;
vector<U> cover; U candidates[57];long long nodes=0;bool timeout=false;U witness=0;
auto started=chrono::steady_clock::now();double cap=110;
int pop(U x){return __builtin_popcountll(x);}
bool dfs(U covered,U available,U selected,int left){
 ++nodes;
 if((nodes&4095)==0 && chrono::duration<double>(chrono::steady_clock::now()-started).count()>cap){timeout=true;return false;}
 if(covered==FULL){witness=selected;return true;}
 if(left==0||timeout)return false;
 U rem=FULL&~covered;int best=23;U options=0;int maxgain=0;U unioncover=covered;
 for(U a=available;a;a&=a-1){int s=__builtin_ctzll(a);maxgain=max(maxgain,pop(cover[s]&rem));unioncover|=cover[s];}
 if(unioncover!=FULL||maxgain*left<pop(rem))return false;
 for(U a=rem;a;a&=a-1){int v=__builtin_ctzll(a);U opts=candidates[v]&available;int count=pop(opts);if(count<best){best=count;options=opts;if(!count)return false;}}
 while(options){U bit=options&-options;options-=bit;available&=~bit;int s=__builtin_ctzll(bit);
  if(dfs(covered|cover[s],available,selected|bit,left-1))return true;
  if(timeout)return false;
 }
 return false;
}
int main(int argc,char**argv){
 if(argc<4)return 2;
 ifstream f(argv[1]);int n,m;f>>n>>m;vector<U> original(n);vector<pair<int,int>> edges;
 for(int i=0,u,v;i<m;++i){f>>u>>v;original[u]|=U(1)<<v;original[v]|=U(1)<<u;}
 ifstream p(argv[2]);ofstream out(argv[3]);int total;p>>total;int passed=0,closed=0,processed=0;
 out<<"pattern,status,nodes,witness_vertices\n";
 for(int pattern=0;pattern<total;++pattern){
  vector<U> adj=original;for(int k=0,u,v;k<7;++k){p>>u>>v;adj[u]&=~(U(1)<<v);adj[v]&=~(U(1)<<u);}
  vector<int>D;cover.clear();for(int v=0;v<n;++v)if(pop(adj[v])==7){D.push_back(v);cover.push_back(adj[v]|(U(1)<<v));}
  if(D.size()!=22){cerr<<"wrong deficit size\n";return 2;}
  for(int v=0;v<n;++v){candidates[v]=0;for(int i=0;i<22;++i)if(cover[i]&(U(1)<<v))candidates[v]|=U(1)<<i;}
  long long before=nodes;bool yes=dfs(0,(U(1)<<22)-1,0,8);
  out<<pattern<<','<<(timeout?"TIMEOUT":yes?"NECESSARY_DOMINATING_SET_FOUND":"NO_DOMINATING_8_SUBSET")<<','<<nodes-before<<",\"";
  if(yes){for(int i=0;i<22;++i)if(witness&(U(1)<<i))out<<D[i]<<' ';++passed;}
  else if(!timeout)++closed;
  out<<"\"\n";out.flush();++processed;
  if(timeout)break;
 }
 cout<<"{\"patterns_processed\":"<<processed<<",\"necessary_condition_passed\":"<<passed<<",\"necessary_condition_failed_exactly\":"<<closed<<",\"timeout\":"<<(timeout?"true":"false")<<",\"nodes\":"<<nodes<<",\"wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-started).count()<<"}\n";
}
